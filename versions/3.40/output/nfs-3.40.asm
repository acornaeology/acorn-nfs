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
l0006                                   = &0006
zp_temp_10                              = &0010
zp_temp_11                              = &0011
l0012                                   = &0012
l0013                                   = &0013
l0014                                   = &0014
l0015                                   = &0015
zp_63                                   = &005f
l0063                                   = &0063
l0088                                   = &0088
l0094                                   = &0094
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
l1e02                                   = &1e02
l3af0                                   = &3af0
l5801                                   = &5801
l5e41                                   = &5e41
l6e04                                   = &6e04
lac85                                   = &ac85
lb7f6                                   = &b7f6
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
oseven                                  = &ffbf
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

    org &931c

.c931c

; Move 1: &931c to &16 for length 65
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
; &931c referenced 1 time by &8178
.nmi_workspace_start
.tube_brk_handler
    lda #&ff                                                          ; 931c: a9 ff       ..  :0016[1]
    jsr tube_send_r4                                                  ; 931e: 20 9e 06     .. :0018[1]
    lda tube_data_register_2                                          ; 9321: ad e3 fe    ... :001b[1]
    lda #0                                                            ; 9324: a9 00       ..  :001e[1]
; &9326 referenced 1 time by &0626[4]
.c0020
    jsr tube_send_r2                                                  ; 9326: 20 95 06     .. :0020[1]
    tay                                                               ; 9329: a8          .   :0023[1]
    lda (l00fd),y                                                     ; 932a: b1 fd       ..  :0024[1]
    jsr tube_send_r2                                                  ; 932c: 20 95 06     .. :0026[1]
; &932f referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 932f: c8          .   :0029[1]
; &9330 referenced 1 time by &053d[3]
.c002a
    lda (l00fd),y                                                     ; 9330: b1 fd       ..  :002a[1]
    jsr tube_send_r2                                                  ; 9332: 20 95 06     .. :002c[1]
    tax                                                               ; 9335: aa          .   :002f[1]
    bne tube_brk_send_loop                                            ; 9336: d0 f7       ..  :0030[1]
; &9338 referenced 1 time by &046a[2]
.tube_reset_stack
    ldx #&ff                                                          ; 9338: a2 ff       ..  :0032[1]
    txs                                                               ; 933a: 9a          .   :0034[1]
    cli                                                               ; 933b: 58          X   :0035[1]
; &933c referenced 6 times by &0044[1], &057f[3], &05a6[3], &0604[4], &0665[4], &0692[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; 933c: 2c e0 fe    ,.. :0036[1]
    bpl tube_poll_r2                                                  ; 933f: 10 06       ..  :0039[1]
; &9341 referenced 1 time by &0049[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; 9341: ad e1 fe    ... :003b[1]
    jsr oswrch                                                        ; 9344: 20 ee ff     .. :003e[1]   ; Write character
; &9347 referenced 1 time by &0039[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 9347: 2c e2 fe    ,.. :0041[1]
    bpl tube_main_loop                                                ; 934a: 10 f0       ..  :0044[1]
    bit tube_status_1_and_tube_control                                ; 934c: 2c e0 fe    ,.. :0046[1]
    bmi tube_handle_wrch                                              ; 934f: 30 f0       0.  :0049[1]
    ldx tube_data_register_2                                          ; 9351: ae e3 fe    ... :004b[1]
    stx l0051                                                         ; 9354: 86 51       .Q  :004e[1]
.tube_dispatch_cmd
l0051 = tube_dispatch_cmd+1
    jmp (l0500)                                                       ; 9356: 6c 00 05    l.. :0050[1]

; &9357 referenced 1 time by &004e[1]
; &9359 referenced 2 times by &04d7[2], &04e7[2]
.tube_transfer_addr
    equb 0                                                            ; 9359: 00          .   :0053[1]
; &935a referenced 3 times by &04af[2], &04cd[2], &04ec[2]
.l0054
    equb &80                                                          ; 935a: 80          .   :0054[1]
; &935b referenced 2 times by &04b3[2], &04f6[2]
.l0055
    equb 0                                                            ; 935b: 00          .   :0055[1]
; &935c referenced 2 times by &04b7[2], &04f4[2]
.l0056
    equb 0                                                            ; 935c: 00          .   :0056[1]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock nmi_workspace_start, *, c931c

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear nmi_workspace_start, &0057

    ; Set the program counter to the next position in the binary file.
    org c931c + (* - nmi_workspace_start)

.c935d

; Move 2: &935d to &0400 for length 249
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
; &935d referenced 1 time by &815e
.tube_code_page4
    jmp c047d                                                         ; 935d: 4c 7d 04    L}. :0400[2]

.tube_escape_entry
    jmp tube_escape_check                                             ; 9360: 4c a7 06    L.. :0403[2]

; &9363 referenced 10 times by &0493[2], &04c8[2], &8b5d, &8b74, &8bd1, &8e19, &99d1, &9a3a, &9f75, &9f7d
.tube_addr_claim
    cmp #&80                                                          ; 9363: c9 80       ..  :0406[2]
    bcc c0430                                                         ; 9365: 90 26       .&  :0408[2]
    cmp #&c0                                                          ; 9367: c9 c0       ..  :040a[2]
    bcs c0423                                                         ; 9369: b0 15       ..  :040c[2]
    ora #&40 ; '@'                                                    ; 936b: 09 40       .@  :040e[2]
    cmp l0015                                                         ; 936d: c5 15       ..  :0410[2]
    bne return_tube_init                                              ; 936f: d0 1b       ..  :0412[2]
; &9371 referenced 1 time by &0464[2]
.sub_c0414
    lda #5                                                            ; 9371: a9 05       ..  :0414[2]
    jsr tube_send_r4                                                  ; 9373: 20 9e 06     .. :0416[2]
    lda l0015                                                         ; 9376: a5 15       ..  :0419[2]
    jsr tube_send_r4                                                  ; 9378: 20 9e 06     .. :041b[2]
; &937b referenced 1 time by &8170
.tube_post_init
    lda #&80                                                          ; 937b: a9 80       ..  :041e[2]
    sta l0014                                                         ; 937d: 85 14       ..  :0420[2]
    rts                                                               ; 937f: 60          `   :0422[2]

; &9380 referenced 1 time by &040c[2]
.c0423
    asl l0014                                                         ; 9380: 06 14       ..  :0423[2]
    bcs c042d                                                         ; 9382: b0 06       ..  :0425[2]
    cmp l0015                                                         ; 9384: c5 15       ..  :0427[2]
    beq return_tube_init                                              ; 9386: f0 04       ..  :0429[2]
    clc                                                               ; 9388: 18          .   :042b[2]
    rts                                                               ; 9389: 60          `   :042c[2]

; &938a referenced 1 time by &0425[2]
.c042d
    sta l0015                                                         ; 938a: 85 15       ..  :042d[2]
; &938c referenced 2 times by &0412[2], &0429[2]
.return_tube_init
    rts                                                               ; 938c: 60          `   :042f[2]

; &938d referenced 1 time by &0408[2]
.c0430
    php                                                               ; 938d: 08          .   :0430[2]
    sei                                                               ; 938e: 78          x   :0431[2]
    sty l0013                                                         ; 938f: 84 13       ..  :0432[2]
    stx l0012                                                         ; 9391: 86 12       ..  :0434[2]
    jsr tube_send_r4                                                  ; 9393: 20 9e 06     .. :0436[2]
    tax                                                               ; 9396: aa          .   :0439[2]
    ldy #3                                                            ; 9397: a0 03       ..  :043a[2]
    lda l0015                                                         ; 9399: a5 15       ..  :043c[2]
    jsr tube_send_r4                                                  ; 939b: 20 9e 06     .. :043e[2]
; &939e referenced 1 time by &0447[2]
.loop_c0441
    lda (l0012),y                                                     ; 939e: b1 12       ..  :0441[2]
    jsr tube_send_r4                                                  ; 93a0: 20 9e 06     .. :0443[2]
    dey                                                               ; 93a3: 88          .   :0446[2]
    bpl loop_c0441                                                    ; 93a4: 10 f8       ..  :0447[2]
    jsr tube_send_r4                                                  ; 93a6: 20 9e 06     .. :0449[2]
    ldy #&18                                                          ; 93a9: a0 18       ..  :044c[2]
    sty tube_status_1_and_tube_control                                ; 93ab: 8c e0 fe    ... :044e[2]
    lda l0518,x                                                       ; 93ae: bd 18 05    ... :0451[2]
    sta tube_status_1_and_tube_control                                ; 93b1: 8d e0 fe    ... :0454[2]
    lsr a                                                             ; 93b4: 4a          J   :0457[2]
    lsr a                                                             ; 93b5: 4a          J   :0458[2]
; &93b6 referenced 1 time by &045c[2]
.loop_c0459
    bit tube_status_register_4_and_cpu_control                        ; 93b6: 2c e6 fe    ,.. :0459[2]
    bvc loop_c0459                                                    ; 93b9: 50 fb       P.  :045c[2]
    bcs c046d                                                         ; 93bb: b0 0d       ..  :045e[2]
    cpx #4                                                            ; 93bd: e0 04       ..  :0460[2]
    bne c047b                                                         ; 93bf: d0 17       ..  :0462[2]
; &93c1 referenced 1 time by &048f[2]
.c0464
    jsr sub_c0414                                                     ; 93c1: 20 14 04     .. :0464[2]
    jsr tube_send_r2                                                  ; 93c4: 20 95 06     .. :0467[2]
    jmp tube_reset_stack                                              ; 93c7: 4c 32 00    L2. :046a[2]

; &93ca referenced 1 time by &045e[2]
.c046d
    bit tube_data_register_3                                          ; 93ca: 2c e5 fe    ,.. :046d[2]
    bit tube_data_register_3                                          ; 93cd: 2c e5 fe    ,.. :0470[2]
    lsr a                                                             ; 93d0: 4a          J   :0473[2]
    bcc c047b                                                         ; 93d1: 90 05       ..  :0474[2]
    ldy #&88                                                          ; 93d3: a0 88       ..  :0476[2]
    sty tube_status_1_and_tube_control                                ; 93d5: 8c e0 fe    ... :0478[2]
; &93d8 referenced 2 times by &0462[2], &0474[2]
.c047b
    plp                                                               ; 93d8: 28          (   :047b[2]
.return_tube_xfer
    rts                                                               ; 93d9: 60          `   :047c[2]

; &93da referenced 1 time by &0400[2]
.c047d
    cli                                                               ; 93da: 58          X   :047d[2]
    bcs c0491                                                         ; 93db: b0 11       ..  :047e[2]
    bne c0485                                                         ; 93dd: d0 03       ..  :0480[2]
    jmp tube_reply_ack                                                ; 93df: 4c 9c 05    L.. :0482[2]

; &93e2 referenced 1 time by &0480[2]
.c0485
    ldx #0                                                            ; 93e2: a2 00       ..  :0485[2]
    ldy #&ff                                                          ; 93e4: a0 ff       ..  :0487[2]
    lda #osbyte_read_write_last_break_type                            ; 93e6: a9 fd       ..  :0489[2]
    jsr osbyte                                                        ; 93e8: 20 f4 ff     .. :048b[2]   ; Read type of last reset
    txa                                                               ; 93eb: 8a          .   :048e[2]   ; X=value of type of last reset
    beq c0464                                                         ; 93ec: f0 d3       ..  :048f[2]
; &93ee referenced 2 times by &047e[2], &0496[2]
.c0491
    lda #&ff                                                          ; 93ee: a9 ff       ..  :0491[2]
    jsr tube_addr_claim                                               ; 93f0: 20 06 04     .. :0493[2]
    bcc c0491                                                         ; 93f3: 90 f9       ..  :0496[2]
    jsr sub_c04cb                                                     ; 93f5: 20 cb 04     .. :0498[2]
; &93f8 referenced 1 time by &04bd[2]
.c049b
    lda #7                                                            ; 93f8: a9 07       ..  :049b[2]
    jsr sub_c04c4                                                     ; 93fa: 20 c4 04     .. :049d[2]
    ldy #0                                                            ; 93fd: a0 00       ..  :04a0[2]
    sty l0000                                                         ; 93ff: 84 00       ..  :04a2[2]
; &9401 referenced 1 time by &04ad[2]
.loop_c04a4
    lda (l0000),y                                                     ; 9401: b1 00       ..  :04a4[2]
    sta tube_data_register_3                                          ; 9403: 8d e5 fe    ... :04a6[2]
    lda rom_header                                                    ; 9406: ad 00 80    ... :04a9[2]
    iny                                                               ; 9409: c8          .   :04ac[2]
    bne loop_c04a4                                                    ; 940a: d0 f5       ..  :04ad[2]
    inc l0054                                                         ; 940c: e6 54       .T  :04af[2]
    bne c04b9                                                         ; 940e: d0 06       ..  :04b1[2]
    inc l0055                                                         ; 9410: e6 55       .U  :04b3[2]
    bne c04b9                                                         ; 9412: d0 02       ..  :04b5[2]
    inc l0056                                                         ; 9414: e6 56       .V  :04b7[2]
; &9416 referenced 2 times by &04b1[2], &04b5[2]
.c04b9
    inc l0001                                                         ; 9416: e6 01       ..  :04b9[2]
    bit l0001                                                         ; 9418: 24 01       $.  :04bb[2]
    bvc c049b                                                         ; 941a: 50 dc       P.  :04bd[2]
    jsr sub_c04cb                                                     ; 941c: 20 cb 04     .. :04bf[2]
    lda #4                                                            ; 941f: a9 04       ..  :04c2[2]
; &9421 referenced 1 time by &049d[2]
.sub_c04c4
    ldy #0                                                            ; 9421: a0 00       ..  :04c4[2]
    ldx #&53 ; 'S'                                                    ; 9423: a2 53       .S  :04c6[2]
    jmp tube_addr_claim                                               ; 9425: 4c 06 04    L.. :04c8[2]

; &9428 referenced 2 times by &0498[2], &04bf[2]
.sub_c04cb
    lda #&80                                                          ; 9428: a9 80       ..  :04cb[2]
    sta l0054                                                         ; 942a: 85 54       .T  :04cd[2]
    sta l0001                                                         ; 942c: 85 01       ..  :04cf[2]
    lda #&20 ; ' '                                                    ; 942e: a9 20       .   :04d1[2]
    and rom_type                                                      ; 9430: 2d 06 80    -.. :04d3[2]
    tay                                                               ; 9433: a8          .   :04d6[2]
    sty tube_transfer_addr                                            ; 9434: 84 53       .S  :04d7[2]
    beq c04f4                                                         ; 9436: f0 19       ..  :04d9[2]
    ldx copyright_offset                                              ; 9438: ae 07 80    ... :04db[2]
; &943b referenced 1 time by &04e2[2]
.loop_c04de
    inx                                                               ; 943b: e8          .   :04de[2]
    lda rom_header,x                                                  ; 943c: bd 00 80    ... :04df[2]
    bne loop_c04de                                                    ; 943f: d0 fa       ..  :04e2[2]
    lda l8001,x                                                       ; 9441: bd 01 80    ... :04e4[2]
    sta tube_transfer_addr                                            ; 9444: 85 53       .S  :04e7[2]
    lda l8002,x                                                       ; 9446: bd 02 80    ... :04e9[2]
    sta l0054                                                         ; 9449: 85 54       .T  :04ec[2]
    ldy service_entry,x                                               ; 944b: bc 03 80    ... :04ee[2]
    lda l8004,x                                                       ; 944e: bd 04 80    ... :04f1[2]
; &9451 referenced 1 time by &04d9[2]
.c04f4
    sta l0056                                                         ; 9451: 85 56       .V  :04f4[2]
    sty l0055                                                         ; 9453: 84 55       .U  :04f6[2]
    rts                                                               ; 9455: 60          `   :04f8[2]


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, c935d

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &04f9

    ; Set the program counter to the next position in the binary file.
    org c935d + (* - tube_code_page4)

.l9456

; Move 3: &9456 to &0500 for length 256
    org &0500
; &9456 referenced 2 times by &0050[1], &8164
.l0500
    equb &37, 5, &96, 5, &f2, 5,   7, 6, &27, 6, &68, 6, &5e, 5       ; 9456: 37 05 96... 7.. :0500[3]
    equb &2d, 5, &20, 5, &42, 5, &a9, 5, &d1, 5                       ; 9464: 2d 05 20... -.  :050e[3]
; &946e referenced 1 time by &0451[2]
.l0518
    equb &86, &88, &96, &98, &18, &18, &82, &18                       ; 946e: 86 88 96... ... :0518[3]

.tube_osbput
    jsr c06c5                                                         ; 9476: 20 c5 06     .. :0520[3]
    tay                                                               ; 9479: a8          .   :0523[3]
    jsr c06c5                                                         ; 947a: 20 c5 06     .. :0524[3]
    jsr osbput                                                        ; 947d: 20 d4 ff     .. :0527[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 9480: 4c 9c 05    L.. :052a[3]

.tube_osbget
    jsr c06c5                                                         ; 9483: 20 c5 06     .. :052d[3]
    tay                                                               ; 9486: a8          .   :0530[3]   ; Y=file handle
    jsr osbget                                                        ; 9487: 20 d7 ff     .. :0531[3]   ; Read a single byte from an open file Y
    jmp tube_rdch_reply                                               ; 948a: 4c 3a 05    L:. :0534[3]

.tube_osrdch
    jsr osrdch                                                        ; 948d: 20 e0 ff     .. :0537[3]   ; Read a character from the current input stream
; &9490 referenced 2 times by &0534[3], &05ef[3]
.tube_rdch_reply
    ror a                                                             ; 9490: 6a          j   :053a[3]
    equb &20, &95                                                     ; 9491: 20 95        .  :053b[3]

    asl c002a                                                         ; 9493: 06 2a       .*  :053d[3]
    jmp tube_reply_byte                                               ; 9495: 4c 9e 05    L.. :053f[3]

.tube_osfind
    jsr c06c5                                                         ; 9498: 20 c5 06     .. :0542[3]
    beq tube_osfind_close                                             ; 949b: f0 0b       ..  :0545[3]
    pha                                                               ; 949d: 48          H   :0547[3]
    jsr tube_read_string                                              ; 949e: 20 82 05     .. :0548[3]
    pla                                                               ; 94a1: 68          h   :054b[3]
    jsr osfind                                                        ; 94a2: 20 ce ff     .. :054c[3]   ; Open or close file(s)
    jmp tube_reply_byte                                               ; 94a5: 4c 9e 05    L.. :054f[3]

; &94a8 referenced 1 time by &0545[3]
.tube_osfind_close
    jsr c06c5                                                         ; 94a8: 20 c5 06     .. :0552[3]
    tay                                                               ; 94ab: a8          .   :0555[3]
    lda #osfind_close                                                 ; 94ac: a9 00       ..  :0556[3]
    jsr osfind                                                        ; 94ae: 20 ce ff     .. :0558[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94b1: 4c 9c 05    L.. :055b[3]

.tube_osargs
    jsr c06c5                                                         ; 94b4: 20 c5 06     .. :055e[3]
    tay                                                               ; 94b7: a8          .   :0561[3]
.tube_read_params
    ldx #4                                                            ; 94b8: a2 04       ..  :0562[3]
; &94ba referenced 1 time by &056a[3]
.loop_c0564
    jsr c06c5                                                         ; 94ba: 20 c5 06     .. :0564[3]
    sta l00ff,x                                                       ; 94bd: 95 ff       ..  :0567[3]
    dex                                                               ; 94bf: ca          .   :0569[3]
    bne loop_c0564                                                    ; 94c0: d0 f8       ..  :056a[3]
    jsr c06c5                                                         ; 94c2: 20 c5 06     .. :056c[3]
    jsr osargs                                                        ; 94c5: 20 da ff     .. :056f[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 94c8: 20 95 06     .. :0572[3]
    ldx #3                                                            ; 94cb: a2 03       ..  :0575[3]
; &94cd referenced 1 time by &057d[3]
.loop_c0577
    lda l0000,x                                                       ; 94cd: b5 00       ..  :0577[3]
    jsr tube_send_r2                                                  ; 94cf: 20 95 06     .. :0579[3]
    dex                                                               ; 94d2: ca          .   :057c[3]
    bpl loop_c0577                                                    ; 94d3: 10 f8       ..  :057d[3]
    jmp tube_main_loop                                                ; 94d5: 4c 36 00    L6. :057f[3]

; &94d8 referenced 3 times by &0548[3], &0596[3], &05b3[3]
.tube_read_string
    ldx #0                                                            ; 94d8: a2 00       ..  :0582[3]
    ldy #0                                                            ; 94da: a0 00       ..  :0584[3]
; &94dc referenced 1 time by &0591[3]
.strnh
    jsr c06c5                                                         ; 94dc: 20 c5 06     .. :0586[3]
    sta l0700,y                                                       ; 94df: 99 00 07    ... :0589[3]
    iny                                                               ; 94e2: c8          .   :058c[3]
    beq c0593                                                         ; 94e3: f0 04       ..  :058d[3]
    cmp #&0d                                                          ; 94e5: c9 0d       ..  :058f[3]
    bne strnh                                                         ; 94e7: d0 f3       ..  :0591[3]
; &94e9 referenced 1 time by &058d[3]
.c0593
    ldy #7                                                            ; 94e9: a0 07       ..  :0593[3]
    rts                                                               ; 94eb: 60          `   :0595[3]

.tube_oscli
    jsr tube_read_string                                              ; 94ec: 20 82 05     .. :0596[3]
    jsr oscli                                                         ; 94ef: 20 f7 ff     .. :0599[3]
; &94f2 referenced 3 times by &0482[2], &052a[3], &055b[3]
.tube_reply_ack
    lda #&7f                                                          ; 94f2: a9 7f       ..  :059c[3]
; &94f4 referenced 4 times by &053f[3], &054f[3], &05a1[3], &067d[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 94f4: 2c e2 fe    ,.. :059e[3]
    bvc tube_reply_byte                                               ; 94f7: 50 fb       P.  :05a1[3]
    sta tube_data_register_2                                          ; 94f9: 8d e3 fe    ... :05a3[3]
; &94fc referenced 1 time by &05cf[3]
.mj
    jmp tube_main_loop                                                ; 94fc: 4c 36 00    L6. :05a6[3]

.tube_osfile
    ldx #&10                                                          ; 94ff: a2 10       ..  :05a9[3]
; &9501 referenced 1 time by &05b1[3]
.argsw
    jsr c06c5                                                         ; 9501: 20 c5 06     .. :05ab[3]
    sta l0001,x                                                       ; 9504: 95 01       ..  :05ae[3]
    dex                                                               ; 9506: ca          .   :05b0[3]
    bne argsw                                                         ; 9507: d0 f8       ..  :05b1[3]
    jsr tube_read_string                                              ; 9509: 20 82 05     .. :05b3[3]
    stx l0000                                                         ; 950c: 86 00       ..  :05b6[3]
    sty l0001                                                         ; 950e: 84 01       ..  :05b8[3]
    ldy #0                                                            ; 9510: a0 00       ..  :05ba[3]
    jsr c06c5                                                         ; 9512: 20 c5 06     .. :05bc[3]
    jsr osfile                                                        ; 9515: 20 dd ff     .. :05bf[3]
    jsr tube_send_r2                                                  ; 9518: 20 95 06     .. :05c2[3]
    ldx #&10                                                          ; 951b: a2 10       ..  :05c5[3]
; &951d referenced 1 time by &05cd[3]
.loop_c05c7
    lda l0001,x                                                       ; 951d: b5 01       ..  :05c7[3]
    jsr tube_send_r2                                                  ; 951f: 20 95 06     .. :05c9[3]
    dex                                                               ; 9522: ca          .   :05cc[3]
    bne loop_c05c7                                                    ; 9523: d0 f8       ..  :05cd[3]
    beq mj                                                            ; 9525: f0 d5       ..  :05cf[3]   ; ALWAYS branch

    ldx #&0d                                                          ; 9527: a2 0d       ..  :05d1[3]
; &9529 referenced 1 time by &05d9[3]
.loop_c05d3
    jsr c06c5                                                         ; 9529: 20 c5 06     .. :05d3[3]
    sta l00ff,x                                                       ; 952c: 95 ff       ..  :05d6[3]
    dex                                                               ; 952e: ca          .   :05d8[3]
    bne loop_c05d3                                                    ; 952f: d0 f8       ..  :05d9[3]
    jsr c06c5                                                         ; 9531: 20 c5 06     .. :05db[3]
    ldy #0                                                            ; 9534: a0 00       ..  :05de[3]
    jsr osgbpb                                                        ; 9536: 20 d1 ff     .. :05e0[3]   ; Read or write multiple bytes to an open file
    pha                                                               ; 9539: 48          H   :05e3[3]
    ldx #&0c                                                          ; 953a: a2 0c       ..  :05e4[3]
; &953c referenced 1 time by &05ec[3]
.loop_c05e6
    lda l0000,x                                                       ; 953c: b5 00       ..  :05e6[3]
    jsr tube_send_r2                                                  ; 953e: 20 95 06     .. :05e8[3]
    dex                                                               ; 9541: ca          .   :05eb[3]
    bpl loop_c05e6                                                    ; 9542: 10 f8       ..  :05ec[3]
    pla                                                               ; 9544: 68          h   :05ee[3]
    jmp tube_rdch_reply                                               ; 9545: 4c 3a 05    L:. :05ef[3]

    jsr c06c5                                                         ; 9548: 20 c5 06     .. :05f2[3]
    tax                                                               ; 954b: aa          .   :05f5[3]
    jsr c06c5                                                         ; 954c: 20 c5 06     .. :05f6[3]
    jsr osbyte                                                        ; 954f: 20 f4 ff     .. :05f9[3]
; &9552 referenced 1 time by &05ff[3]
.loop_c05fc
    bit tube_status_register_2                                        ; 9552: 2c e2 fe    ,.. :05fc[3]
    equb &50                                                          ; 9555: 50          P   :05ff[3]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock l0500, *, l9456

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear l0500, &0600

    ; Set the program counter to the next position in the binary file.
    org l9456 + (* - l0500)

.l9556

; Move 4: &9556 to &0600 for length 256
    org &0600
    equb &fb                                                          ; 9556: fb          .   :0600[4]

    stx tube_data_register_2                                          ; 9557: 8e e3 fe    ... :0601[4]
; &955a referenced 1 time by &0617[4]
.bytex
    jmp tube_main_loop                                                ; 955a: 4c 36 00    L6. :0604[4]

.tube_osbyte_long
    jsr c06c5                                                         ; 955d: 20 c5 06     .. :0607[4]
    tax                                                               ; 9560: aa          .   :060a[4]
    jsr c06c5                                                         ; 9561: 20 c5 06     .. :060b[4]
    tay                                                               ; 9564: a8          .   :060e[4]
    jsr c06c5                                                         ; 9565: 20 c5 06     .. :060f[4]
    jsr osbyte                                                        ; 9568: 20 f4 ff     .. :0612[4]
    eor #&9d                                                          ; 956b: 49 9d       I.  :0615[4]
    beq bytex                                                         ; 956d: f0 eb       ..  :0617[4]
    ror a                                                             ; 956f: 6a          j   :0619[4]
    jsr tube_send_r2                                                  ; 9570: 20 95 06     .. :061a[4]
; &9573 referenced 1 time by &0620[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 9573: 2c e2 fe    ,.. :061d[4]
    bvc tube_osbyte_send_y                                            ; 9576: 50 fb       P.  :0620[4]
    sty tube_data_register_2                                          ; 9578: 8c e3 fe    ... :0622[4]
    equb &70                                                          ; 957b: 70          p   :0625[4]

    cmp c0020,x                                                       ; 957c: d5 20       .   :0626[4]
    cmp l0006                                                         ; 957e: c5 06       ..  :0628[4]
    tay                                                               ; 9580: a8          .   :062a[4]
; &9581 referenced 1 time by &062e[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 9581: 2c e2 fe    ,.. :062b[4]
    bpl tube_osword_read                                              ; 9584: 10 fb       ..  :062e[4]
    ldx tube_data_register_2                                          ; 9586: ae e3 fe    ... :0630[4]
    dex                                                               ; 9589: ca          .   :0633[4]
    bmi c0645                                                         ; 958a: 30 0f       0.  :0634[4]
; &958c referenced 2 times by &0639[4], &0642[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 958c: 2c e2 fe    ,.. :0636[4]
    bpl tube_osword_read_lp                                           ; 958f: 10 fb       ..  :0639[4]
    lda tube_data_register_2                                          ; 9591: ad e3 fe    ... :063b[4]
    sta l0128,x                                                       ; 9594: 9d 28 01    .(. :063e[4]
    dex                                                               ; 9597: ca          .   :0641[4]
    bpl tube_osword_read_lp                                           ; 9598: 10 f2       ..  :0642[4]
    tya                                                               ; 959a: 98          .   :0644[4]
; &959b referenced 1 time by &0634[4]
.c0645
    ldx #<(l0128)                                                     ; 959b: a2 28       .(  :0645[4]
    ldy #>(l0128)                                                     ; 959d: a0 01       ..  :0647[4]
    jsr osword                                                        ; 959f: 20 f1 ff     .. :0649[4]
; &95a2 referenced 1 time by &064f[4]
.loop_c064c
    bit tube_status_register_2                                        ; 95a2: 2c e2 fe    ,.. :064c[4]
    bpl loop_c064c                                                    ; 95a5: 10 fb       ..  :064f[4]
    ldx tube_data_register_2                                          ; 95a7: ae e3 fe    ... :0651[4]
    dex                                                               ; 95aa: ca          .   :0654[4]
    bmi tube_return_main                                              ; 95ab: 30 0e       0.  :0655[4]
; &95ad referenced 1 time by &0663[4]
.tube_osword_write
    ldy l0128,x                                                       ; 95ad: bc 28 01    .(. :0657[4]
; &95b0 referenced 1 time by &065d[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95b0: 2c e2 fe    ,.. :065a[4]
    bvc tube_osword_write_lp                                          ; 95b3: 50 fb       P.  :065d[4]
    sty tube_data_register_2                                          ; 95b5: 8c e3 fe    ... :065f[4]
    dex                                                               ; 95b8: ca          .   :0662[4]
    bpl tube_osword_write                                             ; 95b9: 10 f2       ..  :0663[4]
; &95bb referenced 1 time by &0655[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95bb: 4c 36 00    L6. :0665[4]

.tube_osword_rdln
    ldx #4                                                            ; 95be: a2 04       ..  :0668[4]
; &95c0 referenced 1 time by &0670[4]
.loop_c066a
    jsr c06c5                                                         ; 95c0: 20 c5 06     .. :066a[4]
    sta l0000,x                                                       ; 95c3: 95 00       ..  :066d[4]
    dex                                                               ; 95c5: ca          .   :066f[4]
    bpl loop_c066a                                                    ; 95c6: 10 f8       ..  :0670[4]
    inx                                                               ; 95c8: e8          .   :0672[4]
    ldy #0                                                            ; 95c9: a0 00       ..  :0673[4]
    txa                                                               ; 95cb: 8a          .   :0675[4]
    jsr osword                                                        ; 95cc: 20 f1 ff     .. :0676[4]
    bcc tube_rdln_send_line                                           ; 95cf: 90 05       ..  :0679[4]
    lda #&ff                                                          ; 95d1: a9 ff       ..  :067b[4]
    jmp tube_reply_byte                                               ; 95d3: 4c 9e 05    L.. :067d[4]

; &95d6 referenced 1 time by &0679[4]
.tube_rdln_send_line
    ldx #0                                                            ; 95d6: a2 00       ..  :0680[4]
    lda #&7f                                                          ; 95d8: a9 7f       ..  :0682[4]
    jsr tube_send_r2                                                  ; 95da: 20 95 06     .. :0684[4]
; &95dd referenced 1 time by &0690[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 95dd: bd 00 07    ... :0687[4]
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 95e0: 20 95 06     .. :068a[4]
    inx                                                               ; 95e3: e8          .   :068d[4]
    cmp #&0d                                                          ; 95e4: c9 0d       ..  :068e[4]
    bne tube_rdln_send_loop                                           ; 95e6: d0 f5       ..  :0690[4]
    jmp tube_main_loop                                                ; 95e8: 4c 36 00    L6. :0692[4]

; &95eb referenced 13 times by &0020[1], &0026[1], &002c[1], &0467[2], &0572[3], &0579[3], &05c2[3], &05c9[3], &05e8[3], &061a[4], &0684[4], &068a[4], &0698[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 95eb: 2c e2 fe    ,.. :0695[4]
    bvc tube_send_r2                                                  ; 95ee: 50 fb       P.  :0698[4]
    sta tube_data_register_2                                          ; 95f0: 8d e3 fe    ... :069a[4]
    rts                                                               ; 95f3: 60          `   :069d[4]

; &95f4 referenced 8 times by &0018[1], &0416[2], &041b[2], &0436[2], &043e[2], &0443[2], &0449[2], &06a1[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 95f4: 2c e6 fe    ,.. :069e[4]
    bvc tube_send_r4                                                  ; 95f7: 50 fb       P.  :06a1[4]
    sta tube_data_register_4                                          ; 95f9: 8d e7 fe    ... :06a3[4]
    rts                                                               ; 95fc: 60          `   :06a6[4]

; &95fd referenced 1 time by &0403[2]
.tube_escape_check
    lda l00ff                                                         ; 95fd: a5 ff       ..  :06a7[4]
    sec                                                               ; 95ff: 38          8   :06a9[4]
    ror a                                                             ; 9600: 6a          j   :06aa[4]
    bmi tube_send_r1                                                  ; 9601: 30 0f       0.  :06ab[4]
.tube_event_handler
    pha                                                               ; 9603: 48          H   :06ad[4]
    lda #0                                                            ; 9604: a9 00       ..  :06ae[4]
    jsr tube_send_r1                                                  ; 9606: 20 bc 06     .. :06b0[4]
    tya                                                               ; 9609: 98          .   :06b3[4]
    jsr tube_send_r1                                                  ; 960a: 20 bc 06     .. :06b4[4]
    txa                                                               ; 960d: 8a          .   :06b7[4]
    jsr tube_send_r1                                                  ; 960e: 20 bc 06     .. :06b8[4]
    pla                                                               ; 9611: 68          h   :06bb[4]
; &9612 referenced 5 times by &06ab[4], &06b0[4], &06b4[4], &06b8[4], &06bf[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 9612: 2c e0 fe    ,.. :06bc[4]
    bvc tube_send_r1                                                  ; 9615: 50 fb       P.  :06bf[4]
    sta tube_data_register_1                                          ; 9617: 8d e1 fe    ... :06c1[4]
    rts                                                               ; 961a: 60          `   :06c4[4]

; &961b referenced 20 times by &0520[3], &0524[3], &052d[3], &0542[3], &0552[3], &055e[3], &0564[3], &056c[3], &0586[3], &05ab[3], &05bc[3], &05d3[3], &05db[3], &05f2[3], &05f6[3], &0607[4], &060b[4], &060f[4], &066a[4], &06c8[4]
.c06c5
    bit tube_status_register_2                                        ; 961b: 2c e2 fe    ,.. :06c5[4]
    bpl c06c5                                                         ; 961e: 10 fb       ..  :06c8[4]
    lda tube_data_register_2                                          ; 9620: ad e3 fe    ... :06ca[4]
    rts                                                               ; 9623: 60          `   :06cd[4]

    equs "Jes"                                                        ; 9624: 4a 65 73    Jes :06ce[4]
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9627: ff ff ff... ... :06d1[4]
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9633: ff ff ff... ... :06dd[4]
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 963f: ff ff ff... ... :06e9[4]
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff        ; 964b: ff ff ff... ... :06f5[4]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock &0600, *, l9556

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear &0600, &0700

    ; Set the program counter to the next position in the binary file.
    org l9556 + (* - &0600)


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
; &8000 referenced 3 times by &04a9[2], &04df[2], &9b9b
.pydis_start
.rom_header
.language_entry
l8001 = rom_header+1
l8002 = rom_header+2
    jmp language_handler                                              ; 8000: 4c e1 80    L..

; &8001 referenced 1 time by &04e4[2]
; &8002 referenced 1 time by &04e9[2]
; &8003 referenced 1 time by &04ee[2]
.service_entry
l8004 = service_entry+1
    jmp service_handler                                               ; 8003: 4c f7 80    L..

; &8004 referenced 1 time by &04f1[2]
; &8006 referenced 1 time by &04d3[2]
.rom_type
    equb &82                                                          ; 8006: 82          .
; &8007 referenced 1 time by &04db[2]
.copyright_offset
    equb copyright - rom_header                                       ; 8007: 10          .
; &8008 referenced 1 time by &836a
.binary_version
    equb &83                                                          ; 8008: 83          .
.title
    equs "    NET"                                                    ; 8009: 20 20 20...
.copyright
    equb 0                                                            ; 8010: 00          .
; The 'ROFF' suffix at &8010 is reused by the *ROFF
; command matcher (svc_star_command) — a space-saving
; trick that shares ROM bytes between the copyright
; string and the star command table.
.l8011
l8018 = l8011+7
    equs "(C)ROFF", 0                                                 ; 8011: 28 43 29... (C)
; &8018 referenced 1 time by &8500
    equb &0d, &18                                                     ; 8019: 0d 18       ..
    equs "'1119"                                                      ; 801b: 27 31 31... '11
; Dispatch table: low bytes of (handler_address - 1)
; Each entry stores the low byte of a handler address minus 1,
; for use with the PHA/PHA/RTS dispatch trick at &80DA.
; See dispatch_hi (&8044) for the corresponding high bytes.
; Indexed by service number (1-13), language reason (14-18),
; or *NET command (33-36), with a base offset added by the caller.
.dispatch_lo
    equb &45                                                          ; 8020: 45          E
    equb <(l1e02-1)                                                   ; 8021: 01          .
    equb <(l5801-1)                                                   ; 8022: 00          .
    equb <(l5e41-1)                                                   ; 8023: 40          @
; &8024 referenced 1 time by &80f0
.l8024
    equb <(l6e04-1)                                                   ; 8024: 03          .
    equb <(lb7f6-1)                                                   ; 8025: f5          .
    equb <(sub_c80b8-1)                                               ; 8026: b7          .
    equb <(sub_c82c1-1)                                               ; 8027: c0          .
    equb <(svc_autoboot-1)                                            ; 8028: 18          .
    equb <(sub_c82b1-1)                                               ; 8029: b0          .
    equb <(sub_c816c-1)                                               ; 802a: 6b          k
    equb <(sub_c96f6-1)                                               ; 802b: f5          .
    equb <(sub_c806f-1)                                               ; 802c: 6e          n
    equb <(sub_c807f-1)                                               ; 802d: 7e          ~
    equb <(l8e04-1)                                                   ; 802e: 03          .
    equb <(sub_c82f6-1)                                               ; 802f: f5          .
    equb <(dispatch_net_cmd-1)                                        ; 8030: 68          h
    equb <(svc_nmi_release-1)                                         ; 8031: 65          e
    equb <(l96ed-1)                                                   ; 8032: ec          .
    equb <(sub_c81e8-1)                                               ; 8033: e7          .
    equb <(remote_boot_handler-1)                                     ; 8034: 99          .
    equb <(l84a6-1)                                                   ; 8035: a5          .
    equb <(sub_c92c8-1)                                               ; 8036: c7          .
    equb <(remote_validated-1)                                        ; 8037: d7          .
    equb <(insert_remote_key-1)                                       ; 8038: e7          .
    equb <(sub_c8969-1)                                               ; 8039: 68          h
    equb <(sub_c88cf-1)                                               ; 803a: ce          .
    equb <(sub_c8dd7-1)                                               ; 803b: d6          .
    equb <(tube_claim_loop-1)                                         ; 803c: ce          .
    equb <(sub_c8d21-1)                                               ; 803d: 20
    equb &4c                                                          ; 803e: 4c          L
    equb <(sub_c8374-1)                                               ; 803f: 73          s
    equb <(sub_c8689-1)                                               ; 8040: 88          .
    equb <(sub_c8d2a-1)                                               ; 8041: 29          )
    equb <(copy_handles-1)                                            ; 8042: 2a          *
    equb <(set_csd_handle-1)                                          ; 8043: 23          #
; Dispatch table: high bytes of (handler_address - 1)
; Paired with dispatch_lo (&8020). Together they form a table of
; 37 handler addresses, used via the PHA/PHA/RTS trick at &80DA.
.dispatch_hi
    equb <(sub_c8ed5-1)                                               ; 8044: d4          .
    equb >(l1e02-1)                                                   ; 8045: 1e          .
    equb >(l5801-1)                                                   ; 8046: 58          X
    equb >(l5e41-1)                                                   ; 8047: 5e          ^
    equb >(l6e04-1)                                                   ; 8048: 6e          n
; &8049 referenced 1 time by &80ec
.l8049
    equb >(lb7f6-1)                                                   ; 8049: b7          .
    equb >(sub_c80b8-1)                                               ; 804a: 80          .
    equb >(sub_c82c1-1)                                               ; 804b: 82          .
    equb >(svc_autoboot-1)                                            ; 804c: 82          .
    equb >(sub_c82b1-1)                                               ; 804d: 82          .
    equb >(sub_c816c-1)                                               ; 804e: 81          .
    equb >(sub_c96f6-1)                                               ; 804f: 96          .
    equb >(sub_c806f-1)                                               ; 8050: 80          .
    equb >(sub_c807f-1)                                               ; 8051: 80          .
    equb >(l8e04-1)                                                   ; 8052: 8e          .
    equb >(sub_c82f6-1)                                               ; 8053: 82          .
    equb >(dispatch_net_cmd-1)                                        ; 8054: 80          .
    equb >(svc_nmi_release-1)                                         ; 8055: 96          .
    equb >(l96ed-1)                                                   ; 8056: 96          .
    equb >(sub_c81e8-1)                                               ; 8057: 81          .
    equb >(remote_boot_handler-1)                                     ; 8058: 84          .
    equb >(l84a6-1)                                                   ; 8059: 84          .
    equb >(sub_c92c8-1)                                               ; 805a: 92          .
    equb >(remote_validated-1)                                        ; 805b: 84          .
    equb >(insert_remote_key-1)                                       ; 805c: 84          .
    equb >(sub_c8969-1)                                               ; 805d: 89          .
    equb >(sub_c88cf-1)                                               ; 805e: 88          .
    equb >(sub_c8dd7-1)                                               ; 805f: 8d          .
    equb >(tube_claim_loop-1)                                         ; 8060: 8b          .
    equb >(sub_c8d21-1)                                               ; 8061: 8d          .
    equb &8c                                                          ; 8062: 8c          .
    equb >(sub_c8374-1)                                               ; 8063: 83          .
    equb >(sub_c8689-1)                                               ; 8064: 86          .
    equb >(sub_c8d2a-1)                                               ; 8065: 8d          .
    equb >(copy_handles-1)                                            ; 8066: 8e          .
    equb >(set_csd_handle-1)                                          ; 8067: 8e          .
    equb >(sub_c8ed5-1)                                               ; 8068: 8e          .

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
; *NET2 (&8E56): read handle entry from workspace
; (net2_read_handle_entry)
; 
; *NET3 (&8E66): close handle / mark as unused
; (net3_close_handle)
; 
; *NET4 (&8180): resume after remote operation
; (resume_after_remote)
; ***************************************************************************************
.dispatch_net_cmd
    sta c8e8e                                                         ; 8069: 8d 8e 8e    ...            ; Read command character following *NET
    stx l818e                                                         ; 806c: 8e 8e 81    ...
.sub_c806f
    lda l00ef                                                         ; 806f: a5 ef       ..
    sbc #&31 ; '1'                                                    ; 8071: e9 31       .1             ; Subtract ASCII '1' to get 0-based command index
    cmp #4                                                            ; 8073: c9 04       ..
    bcs c80e3                                                         ; 8075: b0 6c       .l
    tax                                                               ; 8077: aa          .
    lda #0                                                            ; 8078: a9 00       ..
    sta l00a9                                                         ; 807a: 85 a9       ..
    tya                                                               ; 807c: 98          .
    ldy #&21 ; '!'                                                    ; 807d: a0 21       .!             ; Y=&20: base offset for *NET commands (index 33+)
.sub_c807f
    bne dispatch                                                      ; 807f: d0 66       .f
; &8081 referenced 1 time by &8086
.loop_c8081
    iny                                                               ; 8081: c8          .
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
    lda (fs_options),y                                                ; 8082: b1 bb       ..
    cmp #&20 ; ' '                                                    ; 8084: c9 20       .
    beq loop_c8081                                                    ; 8086: f0 f9       ..
    cmp #&3a ; ':'                                                    ; 8088: c9 3a       .:
    bcs c809d                                                         ; 808a: b0 11       ..
    jsr sub_c8620                                                     ; 808c: 20 20 86      .
    bcc c8098                                                         ; 808f: 90 07       ..
    sta fs_server_net                                                 ; 8091: 8d 01 0e    ...
    iny                                                               ; 8094: c8          .
    jsr sub_c8620                                                     ; 8095: 20 20 86      .
; &8098 referenced 1 time by &808f
.c8098
    beq c809d                                                         ; 8098: f0 03       ..
    sta fs_server_stn                                                 ; 809a: 8d 00 0e    ...
; &809d referenced 2 times by &808a, &8098
.c809d
    jsr copy_filename                                                 ; 809d: 20 75 8d     u.
; &80a0 referenced 2 times by &80a8, &80bf
.c80a0
    dey                                                               ; 80a0: 88          .
    beq c80c5                                                         ; 80a1: f0 22       ."
    lda fs_cmd_data,y                                                 ; 80a3: b9 05 0f    ...
    cmp #&3a ; ':'                                                    ; 80a6: c9 3a       .:
    bne c80a0                                                         ; 80a8: d0 f6       ..
    jsr oswrch                                                        ; 80aa: 20 ee ff     ..            ; Write character
; &80ad referenced 1 time by &80ba
.loop_c80ad
    jsr osrdch                                                        ; 80ad: 20 e0 ff     ..            ; Read a character from the current input stream
    jsr l854d                                                         ; 80b0: 20 4d 85     M.
    sta fs_cmd_data,y                                                 ; 80b3: 99 05 0f    ...
    iny                                                               ; 80b6: c8          .
    inx                                                               ; 80b7: e8          .
.sub_c80b8
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
; and catch-all entries in the command match table at &8BE4, and
; from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
; in), returns without sending.
; ***************************************************************************************
.forward_star_cmd
    jsr copy_filename                                                 ; 80c1: 20 75 8d     u.
    tay                                                               ; 80c4: a8          .              ; Y=function code for HDRFN
; &80c5 referenced 1 time by &80a1
.c80c5
    jsr prepare_fs_cmd                                                ; 80c5: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
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
    jsr save_fscv_args_with_ptrs                                      ; 80d4: 20 c8 85     ..            ; Store A/X/Y in FS workspace
    cmp #8                                                            ; 80d7: c9 08       ..
    bcs return_1                                                      ; 80d9: b0 1b       ..             ; Function code >= 8? Return (unsupported)
    tax                                                               ; 80db: aa          .
    tya                                                               ; 80dc: 98          .
    ldy #&13                                                          ; 80dd: a0 13       ..             ; Y=&12: base offset for FSCV dispatch (indices 19+)
    bne dispatch                                                      ; 80df: d0 06       ..             ; ALWAYS branch

; ***************************************************************************************
; Language entry dispatcher
; 
; Called when the NFS ROM is entered as a language. X = reason code
; (0-4). Dispatches via table indices 14-18 (base offset Y=&0D).
; ***************************************************************************************
; &80e1 referenced 1 time by &8000
.language_handler
    cpx #5                                                            ; 80e1: e0 05       ..
; &80e3 referenced 1 time by &8075
.c80e3
    bcs return_1                                                      ; 80e3: b0 11       ..
    ldy #&0e                                                          ; 80e5: a0 0e       ..             ; Y=&0D: base offset for language handlers (index 14+)
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
; &80e7 referenced 5 times by &807f, &80d2, &80df, &80e9, &819d
.dispatch
    inx                                                               ; 80e7: e8          .              ; Add base offset Y to index X (loop: X += Y+1)
    dey                                                               ; 80e8: 88          .
    bpl dispatch                                                      ; 80e9: 10 fc       ..
    tay                                                               ; 80eb: a8          .
    lda l8049,x                                                       ; 80ec: bd 49 80    .I.            ; Load high byte of (handler - 1) from table
    pha                                                               ; 80ef: 48          H              ; Push high byte onto stack
    lda l8024,x                                                       ; 80f0: bd 24 80    .$.            ; Load low byte of (handler - 1) from table
    pha                                                               ; 80f3: 48          H              ; Push low byte onto stack
    ldx fs_options                                                    ; 80f4: a6 bb       ..             ; Restore X (fileserver options) for use by handler
; &80f6 referenced 3 times by &80cb, &80d9, &80e3
.return_1
    rts                                                               ; 80f6: 60          `              ; RTS pops address, adds 1, jumps to handler

; &80f7 referenced 1 time by &8003
.service_handler
    nop                                                               ; 80f7: ea          .
    nop                                                               ; 80f8: ea          .
    nop                                                               ; 80f9: ea          .
    nop                                                               ; 80fa: ea          .
    nop                                                               ; 80fb: ea          .
    nop                                                               ; 80fc: ea          .
    nop                                                               ; 80fd: ea          .
    nop                                                               ; 80fe: ea          .
    nop                                                               ; 80ff: ea          .
    pha                                                               ; 8100: 48          H
    lda l0df0,x                                                       ; 8101: bd f0 0d    ...
    pha                                                               ; 8104: 48          H
    bne c8118                                                         ; 8105: d0 11       ..
    inc l0df0,x                                                       ; 8107: fe f0 0d    ...
    lda station_id_disable_net_nmis                                   ; 810a: ad 18 fe    ...
    beq c8114                                                         ; 810d: f0 05       ..
    cmp station_id_disable_net_nmis                                   ; 810f: cd 18 fe    ...
    beq c8118                                                         ; 8112: f0 04       ..
; &8114 referenced 1 time by &810d
.c8114
    sec                                                               ; 8114: 38          8
    ror l0df0,x                                                       ; 8115: 7e f0 0d    ~..
; &8118 referenced 2 times by &8105, &8112
.c8118
    pla                                                               ; 8118: 68          h
    asl a                                                             ; 8119: 0a          .
    pla                                                               ; 811a: 68          h
    bmi c811f                                                         ; 811b: 30 02       0.
    bcs c818d                                                         ; 811d: b0 6e       .n
; ***************************************************************************************
; Service handler entry
; 
; Intercepts three service calls before normal dispatch:
;   &FE: Tube init -- explode character definitions
;   &FF: Full init -- vector setup, copy code to RAM, select NFS
;   &12 (Y=5): Select NFS as active filing system
; All other service calls < &0D dispatch via c8146.
; 3.35K removes the per-ROM disable flag check that 3.35D has.
; ***************************************************************************************
; &811f referenced 1 time by &811b
.c811f
    cmp #&fe                                                          ; 811f: c9 fe       ..
    bcc c817f                                                         ; 8121: 90 5c       .\
    bne c8140                                                         ; 8123: d0 1b       ..
    cpy #0                                                            ; 8125: c0 00       ..
    beq c817f                                                         ; 8127: f0 56       .V
    ldx #6                                                            ; 8129: a2 06       ..
    lda #osbyte_explode_chars                                         ; 812b: a9 14       ..
    jsr osbyte                                                        ; 812d: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
; &8130 referenced 2 times by &8133, &813d
.c8130
    bit tube_status_1_and_tube_control                                ; 8130: 2c e0 fe    ,..
    bpl c8130                                                         ; 8133: 10 fb       ..
    lda tube_data_register_1                                          ; 8135: ad e1 fe    ...
    beq c817d                                                         ; 8138: f0 43       .C
    jsr oswrch                                                        ; 813a: 20 ee ff     ..            ; Write character
    jmp c8130                                                         ; 813d: 4c 30 81    L0.

; &8140 referenced 1 time by &8123
.c8140
    lda #&ad                                                          ; 8140: a9 ad       ..
    sta evntv                                                         ; 8142: 8d 20 02    . .
    lda #6                                                            ; 8145: a9 06       ..
    sta evntv+1                                                       ; 8147: 8d 21 02    .!.
    lda #&16                                                          ; 814a: a9 16       ..
    sta brkv                                                          ; 814c: 8d 02 02    ...
    lda #0                                                            ; 814f: a9 00       ..
    sta brkv+1                                                        ; 8151: 8d 03 02    ...
    lda #&8e                                                          ; 8154: a9 8e       ..
    sta tube_status_1_and_tube_control                                ; 8156: 8d e0 fe    ...
    ldy #0                                                            ; 8159: a0 00       ..
; Copy NMI handler code from ROM to RAM pages &04-&06
; &815b referenced 1 time by &816e
.cloop
    lda c935d,y                                                       ; 815b: b9 5d 93    .].
    sta tube_code_page4,y                                             ; 815e: 99 00 04    ...
    lda l9456,y                                                       ; 8161: b9 56 94    .V.
    sta l0500,y                                                       ; 8164: 99 00 05    ...
    lda l9556,y                                                       ; 8167: b9 56 95    .V.
    equb &99, 0                                                       ; 816a: 99 00       ..

.sub_c816c
    asl l0088                                                         ; 816c: 06 88       ..
    bne cloop                                                         ; 816e: d0 eb       ..
    jsr tube_post_init                                                ; 8170: 20 1e 04     ..
    ldx #&60 ; '`'                                                    ; 8173: a2 60       .`
; Copy NMI workspace initialiser from ROM to &0016-&0076
; &8175 referenced 1 time by &817b
.loop_c8175
    lda c931c,x                                                       ; 8175: bd 1c 93    ...
    sta nmi_workspace_start,x                                         ; 8178: 95 16       ..
    dex                                                               ; 817a: ca          .
    bpl loop_c8175                                                    ; 817b: 10 f8       ..
; &817d referenced 1 time by &8138
.c817d
    lda #0                                                            ; 817d: a9 00       ..
; &817f referenced 2 times by &8121, &8127
.c817f
    cmp #&12                                                          ; 817f: c9 12       ..
    bne c818b                                                         ; 8181: d0 08       ..
    cpy #5                                                            ; 8183: c0 05       ..
    bne c818b                                                         ; 8185: d0 04       ..
    lda #&0d                                                          ; 8187: a9 0d       ..
    bne c818f                                                         ; 8189: d0 04       ..             ; ALWAYS branch

; &818b referenced 2 times by &8181, &8185
.c818b
    cmp #&0d                                                          ; 818b: c9 0d       ..
; &818d referenced 1 time by &811d
.c818d
l818e = c818d+1
    bcs return_2                                                      ; 818d: b0 1c       ..
; &818e referenced 1 time by &806c
; &818f referenced 1 time by &8189
.c818f
    tax                                                               ; 818f: aa          .
    lda l00a9                                                         ; 8190: a5 a9       ..
    pha                                                               ; 8192: 48          H
    lda l00a8                                                         ; 8193: a5 a8       ..
    pha                                                               ; 8195: 48          H
    stx l00a9                                                         ; 8196: 86 a9       ..
    sty l00a8                                                         ; 8198: 84 a8       ..
    tya                                                               ; 819a: 98          .
    ldy #0                                                            ; 819b: a0 00       ..
    jsr dispatch                                                      ; 819d: 20 e7 80     ..
    ldx l00a9                                                         ; 81a0: a6 a9       ..
    pla                                                               ; 81a2: 68          h
    sta l00a8                                                         ; 81a3: 85 a8       ..
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
    pla                                                               ; 81a5: 68          h
    sta l00a9                                                         ; 81a6: 85 a9       ..
    txa                                                               ; 81a8: 8a          .
    ldx romsel_copy                                                   ; 81a9: a6 f4       ..
; &81ab referenced 1 time by &818d
.return_2
    rts                                                               ; 81ab: 60          `

    nop                                                               ; 81ac: ea          .
    nop                                                               ; 81ad: ea          .
    nop                                                               ; 81ae: ea          .
    nop                                                               ; 81af: ea          .
    nop                                                               ; 81b0: ea          .
    ldx #&0c                                                          ; 81b1: a2 0c       ..
    jsr sub_c835e                                                     ; 81b3: 20 5e 83     ^.
    bne c81e6                                                         ; 81b6: d0 2e       ..
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
    ldy #4                                                            ; 81b8: a0 04       ..
    lda (net_rx_ptr),y                                                ; 81ba: b1 9c       ..
    beq c81df                                                         ; 81bc: f0 21       .!
    lda #0                                                            ; 81be: a9 00       ..
    tax                                                               ; 81c0: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 81c1: 91 9c       ..
    tay                                                               ; 81c3: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 81c4: a9 c9       ..
    jsr osbyte                                                        ; 81c6: 20 f4 ff     ..            ; Enable keyboard (for Econet)
    lda #&0a                                                          ; 81c9: a9 0a       ..
    jsr setup_tx_and_send                                             ; 81cb: 20 ba 90     ..
; &81ce referenced 1 time by &84b9
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 81ce: 86 9e       ..
    lda #&ce                                                          ; 81d0: a9 ce       ..
; &81d2 referenced 1 time by &81dd
.loop_c81d2
    ldx nfs_workspace                                                 ; 81d2: a6 9e       ..
    ldy #&7f                                                          ; 81d4: a0 7f       ..
    jsr osbyte                                                        ; 81d6: 20 f4 ff     ..
    adc #1                                                            ; 81d9: 69 01       i.
    cmp #&d0                                                          ; 81db: c9 d0       ..
    beq loop_c81d2                                                    ; 81dd: f0 f3       ..
; &81df referenced 1 time by &81bc
.c81df
    lda #0                                                            ; 81df: a9 00       ..
    sta l00a9                                                         ; 81e1: 85 a9       ..
    sta nfs_workspace                                                 ; 81e3: 85 9e       ..
    rts                                                               ; 81e5: 60          `

; &81e6 referenced 1 time by &81b6
.c81e6
    ldx #5                                                            ; 81e6: a2 05       ..
.sub_c81e8
    jsr sub_c835e                                                     ; 81e8: 20 5e 83     ^.
    bne c8211                                                         ; 81eb: d0 24       .$
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
.select_nfs
    jsr call_fscv_shutdown                                            ; 81ed: 20 14 82     ..
    sec                                                               ; 81f0: 38          8
    ror l00a8                                                         ; 81f1: 66 a8       f.
    jsr issue_vectors_claimed                                         ; 81f3: 20 77 82     w.
    ldy #&1d                                                          ; 81f6: a0 1d       ..
; &81f8 referenced 1 time by &8200
.initl
    lda (net_rx_ptr),y                                                ; 81f8: b1 9c       ..
    sta fs_state_deb,y                                                ; 81fa: 99 eb 0d    ...
    dey                                                               ; 81fd: 88          .
    cpy #&14                                                          ; 81fe: c0 14       ..
    bne initl                                                         ; 8200: d0 f6       ..
    beq c8260                                                         ; 8202: f0 5c       .\             ; ALWAYS branch

; ***************************************************************************************
; Service 9: *HELP
; 
; Prints the ROM identification string using print_inline.
; ***************************************************************************************
.svc_help
    jsr print_inline                                                  ; 8204: 20 05 86     ..
    equs &0d, "NFS 3.40", &0d                                         ; 8207: 0d 4e 46... .NF

; &8211 referenced 2 times by &81eb, &8226
.c8211
    ldy l00a8                                                         ; 8211: a4 a8       ..
    rts                                                               ; 8213: 60          `

; ***************************************************************************************
; Notify filing system of shutdown
; 
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; ***************************************************************************************
; &8214 referenced 2 times by &81ed, &8219
.call_fscv_shutdown
    lda #6                                                            ; 8214: a9 06       ..
    jmp (fscv)                                                        ; 8216: 6c 1e 02    l..

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
    jsr call_fscv_shutdown                                            ; 8219: 20 14 82     ..
    lda #osbyte_scan_keyboard_from_16                                 ; 821c: a9 7a       .z
    jsr osbyte                                                        ; 821e: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 8221: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi c822e                                                         ; 8222: 30 0a       0.
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
    eor #&55 ; 'U'                                                    ; 8224: 49 55       IU             ; Copy 14 bytes: FS vector addresses → FILEV-FSCV
    bne c8211                                                         ; 8226: d0 e9       ..
    tay                                                               ; 8228: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 8229: a9 78       .x
    jsr osbyte                                                        ; 822b: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; &822e referenced 1 time by &8222
.c822e
    jsr print_inline                                                  ; 822e: 20 05 86     ..
    equs "Econet Station "                                            ; 8231: 45 63 6f... Eco

    ldy #&14                                                          ; 8240: a0 14       ..
    lda (net_rx_ptr),y                                                ; 8242: b1 9c       ..
    jsr print_decimal                                                 ; 8244: 20 b0 8d     ..
    lda #&20 ; ' '                                                    ; 8247: a9 20       .
    bit econet_control23_or_status2                                   ; 8249: 2c a1 fe    ,..
    beq c825b                                                         ; 824c: f0 0d       ..
    jsr print_inline                                                  ; 824e: 20 05 86     ..
    equs " No Clock"                                                  ; 8251: 20 4e 6f...  No

    nop                                                               ; 825a: ea          .
; &825b referenced 1 time by &824c
.c825b
    jsr print_inline                                                  ; 825b: 20 05 86     ..
    equs &0d, &0d                                                     ; 825e: 0d 0d       ..

; &8260 referenced 1 time by &8202
.c8260
    ldy #&0d                                                          ; 8260: a0 0d       ..
; &8262 referenced 1 time by &8269
.loop_c8262
    lda l8296,y                                                       ; 8262: b9 96 82    ...
    sta filev,y                                                       ; 8265: 99 12 02    ...
    dey                                                               ; 8268: 88          .
    bpl loop_c8262                                                    ; 8269: 10 f7       ..
    jsr setup_rom_ptrs_netv                                           ; 826b: 20 21 83     !.
    ldy #&1b                                                          ; 826e: a0 1b       ..
    ldx #7                                                            ; 8270: a2 07       ..
    jsr store_rom_ptr_pair                                            ; 8272: 20 35 83     5.
    stx l00a9                                                         ; 8275: 86 a9       ..
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
; &8277 referenced 1 time by &81f3
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 8277: a9 8f       ..
    ldx #&0f                                                          ; 8279: a2 0f       ..
    jsr osbyte                                                        ; 827b: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 827e: a2 0a       ..
    jsr osbyte                                                        ; 8280: 20 f4 ff     ..
    ldx l00a8                                                         ; 8283: a6 a8       ..
    bne return_3                                                      ; 8285: d0 37       .7
    ldx #&8e                                                          ; 8287: a2 8e       ..
; &8289 referenced 2 times by &8335, &833b
.c8289
    ldy #&82                                                          ; 8289: a0 82       ..
    jmp fscv_star_handler                                             ; 828b: 4c d7 8b    L..

    equb &49                                                          ; 828e: 49          I
    equb &20                                                          ; 828f: 20
    equb &2e                                                          ; 8290: 2e          .
    equb &42                                                          ; 8291: 42          B
    equb &4f                                                          ; 8292: 4f          O
    equb &4f                                                          ; 8293: 4f          O
    equb &54                                                          ; 8294: 54          T
    equb &0d                                                          ; 8295: 0d          .
; &8296 referenced 1 time by &8262
.l8296
    equb &1b                                                          ; 8296: 1b          .
    equb &ff                                                          ; 8297: ff          .
    equb &1e                                                          ; 8298: 1e          .
    equb &ff                                                          ; 8299: ff          .
    equb &21                                                          ; 829a: 21          !
    equb &ff                                                          ; 829b: ff          .
    equb &24                                                          ; 829c: 24          $
    equb &ff                                                          ; 829d: ff          .
    equb &27                                                          ; 829e: 27          '
    equb &ff                                                          ; 829f: ff          .
    equb &2a                                                          ; 82a0: 2a          *
    equb &ff                                                          ; 82a1: ff          .
    equb &2d, &ff,   5, &87, &4a, &24, &89, &44, &5c, &85, &57, &0f   ; 82a2: 2d ff 05... -..
    equb &84, &42, &2e                                                ; 82ae: 84 42 2e    .B.

.sub_c82b1
    txa                                                               ; 82b1: 8a          .
    eor (l0094,x)                                                     ; 82b2: 41 94       A.
    equb &89, &52, &d4, &80                                           ; 82b4: 89 52 d4... .R.

; ***************************************************************************************
; Service 1: claim absolute workspace
; 
; Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
; and FS command buffer (&0F). If Y >= &10, workspace already
; allocated — returns unchanged.
; ***************************************************************************************
.svc_abs_workspace
    cpy #&10                                                          ; 82b8: c0 10       ..
    bcs return_3                                                      ; 82ba: b0 02       ..
    ldy #&10                                                          ; 82bc: a0 10       ..
; &82be referenced 2 times by &8285, &82ba
.return_3
    rts                                                               ; 82be: 60          `

    equb &76, &90                                                     ; 82bf: 76 90       v.

.sub_c82c1
    sty net_rx_ptr_hi                                                 ; 82c1: 84 9d       ..
    iny                                                               ; 82c3: c8          .
    sty nfs_workspace_hi                                              ; 82c4: 84 9f       ..
    lda #0                                                            ; 82c6: a9 00       ..
    ldy #4                                                            ; 82c8: a0 04       ..
    sta (net_rx_ptr),y                                                ; 82ca: 91 9c       ..
    ldy #&ff                                                          ; 82cc: a0 ff       ..
    sta net_rx_ptr                                                    ; 82ce: 85 9c       ..
    sta nfs_workspace                                                 ; 82d0: 85 9e       ..
    sta l00a8                                                         ; 82d2: 85 a8       ..
    sta tx_clear_flag                                                 ; 82d4: 8d 62 0d    .b.
    tax                                                               ; 82d7: aa          .              ; X=&00
    lda #osbyte_read_write_last_break_type                            ; 82d8: a9 fd       ..             ; OSBYTE &FD: read type of last reset
    jsr osbyte                                                        ; 82da: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 82dd: 8a          .              ; X=value of type of last reset
    beq c8312                                                         ; 82de: f0 32       .2             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 82e0: a0 15       ..
    lda #&fe                                                          ; 82e2: a9 fe       ..
    sta fs_server_stn                                                 ; 82e4: 8d 00 0e    ...            ; Station &FE = no server selected
    sta (net_rx_ptr),y                                                ; 82e7: 91 9c       ..
    lda #0                                                            ; 82e9: a9 00       ..
    sta fs_server_net                                                 ; 82eb: 8d 01 0e    ...
    sta prot_status                                                   ; 82ee: 8d 63 0d    .c.
    sta fs_messages_flag                                              ; 82f1: 8d 06 0e    ...
    equb &8d, 5                                                       ; 82f4: 8d 05       ..

.sub_c82f6
    asl l91c8                                                         ; 82f6: 0e c8 91    ...
    equb &9c                                                          ; 82f9: 9c          .

    ldy #3                                                            ; 82fa: a0 03       ..
    sta (nfs_workspace),y                                             ; 82fc: 91 9e       ..
    dey                                                               ; 82fe: 88          .              ; Y=&02
    lda #&eb                                                          ; 82ff: a9 eb       ..
    sta (nfs_workspace),y                                             ; 8301: 91 9e       ..
; &8303 referenced 1 time by &8310
.loop_c8303
    lda l00a8                                                         ; 8303: a5 a8       ..
    jsr calc_handle_offset                                            ; 8305: 20 47 8e     G.
    bcs c8312                                                         ; 8308: b0 08       ..
    lda #&3f ; '?'                                                    ; 830a: a9 3f       .?
    sta (nfs_workspace),y                                             ; 830c: 91 9e       ..
    inc l00a8                                                         ; 830e: e6 a8       ..
    bne loop_c8303                                                    ; 8310: d0 f1       ..
; &8312 referenced 2 times by &82de, &8308
.c8312
    lda station_id_disable_net_nmis                                   ; 8312: ad 18 fe    ...            ; Read station ID (also INTOFF)
    ldy #&14                                                          ; 8315: a0 14       ..
    sta (net_rx_ptr),y                                                ; 8317: 91 9c       ..
    jsr trampoline_adlc_init                                          ; 8319: 20 63 96     c.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 831c: a9 40       .@
    sta rx_flags                                                      ; 831e: 8d 64 0d    .d.
; ***************************************************************************************
; Set up ROM pointer table and NETV
; 
; Reads the ROM pointer table base address via OSBYTE &A8, stores
; it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
; one 3-byte extended vector entry (addr=&9074, rom=current) into
; the ROM pointer table at offset &36, installing osword_dispatch
; as the NETV handler.
; ***************************************************************************************
; &8321 referenced 1 time by &826b
.setup_rom_ptrs_netv
    lda #osbyte_read_rom_ptr_table_low                                ; 8321: a9 a8       ..
    ldx #0                                                            ; 8323: a2 00       ..
    ldy #&ff                                                          ; 8325: a0 ff       ..
    jsr osbyte                                                        ; 8327: 20 f4 ff     ..            ; Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 832a: 86 f6       ..             ; X=value of address of ROM pointer table (low byte)
    sty l00f7                                                         ; 832c: 84 f7       ..             ; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 832e: a0 36       .6
    sty netv                                                          ; 8330: 8c 24 02    .$.
    ldx #1                                                            ; 8333: a2 01       ..
; &8335 referenced 2 times by &8272, &8347
.store_rom_ptr_pair
    lda c8289,y                                                       ; 8335: b9 89 82    ...
    sta (osrdsc_ptr),y                                                ; 8338: 91 f6       ..
    iny                                                               ; 833a: c8          .
    lda c8289,y                                                       ; 833b: b9 89 82    ...
    sta (osrdsc_ptr),y                                                ; 833e: 91 f6       ..
    iny                                                               ; 8340: c8          .
    lda romsel_copy                                                   ; 8341: a5 f4       ..
    sta (osrdsc_ptr),y                                                ; 8343: 91 f6       ..
    iny                                                               ; 8345: c8          .
    dex                                                               ; 8346: ca          .
    bne store_rom_ptr_pair                                            ; 8347: d0 ec       ..
    ldy nfs_workspace_hi                                              ; 8349: a4 9f       ..
    iny                                                               ; 834b: c8          .
    rts                                                               ; 834c: 60          `

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
    ldy #&1d                                                          ; 834d: a0 1d       ..
; &834f referenced 1 time by &8357
.fsdiel
    lda fs_state_deb,y                                                ; 834f: b9 eb 0d    ...
    sta (net_rx_ptr),y                                                ; 8352: 91 9c       ..
    dey                                                               ; 8354: 88          .
    cpy #&14                                                          ; 8355: c0 14       ..
    bne fsdiel                                                        ; 8357: d0 f6       ..
    lda #osbyte_close_spool_exec                                      ; 8359: a9 77       .w
    jmp osbyte                                                        ; 835b: 4c f4 ff    L..            ; Close any *SPOOL and *EXEC files

; &835e referenced 2 times by &81b3, &81e8
.sub_c835e
    ldy l00a8                                                         ; 835e: a4 a8       ..
; &8360 referenced 1 time by &8371
.loop_c8360
    lda (os_text_ptr),y                                               ; 8360: b1 f2       ..
    cmp #&2e ; '.'                                                    ; 8362: c9 2e       ..
    beq c8379                                                         ; 8364: f0 13       ..
    and #&df                                                          ; 8366: 29 df       ).
    beq l8373                                                         ; 8368: f0 09       ..
    cmp binary_version,x                                              ; 836a: dd 08 80    ...
    bne l8373                                                         ; 836d: d0 04       ..
    iny                                                               ; 836f: c8          .
    inx                                                               ; 8370: e8          .
    bne loop_c8360                                                    ; 8371: d0 ed       ..
; &8373 referenced 2 times by &8368, &836d
.l8373
    equb &bd                                                          ; 8373: bd          .

.sub_c8374
    php                                                               ; 8374: 08          .
    equb &80                                                          ; 8375: 80          .

    beq c837a                                                         ; 8376: f0 02       ..
    rts                                                               ; 8378: 60          `

; &8379 referenced 2 times by &8364, &837e
.c8379
    iny                                                               ; 8379: c8          .
; &837a referenced 2 times by &8376, &8de0
.c837a
    lda (os_text_ptr),y                                               ; 837a: b1 f2       ..
    cmp #&20 ; ' '                                                    ; 837c: c9 20       .
    beq c8379                                                         ; 837e: f0 f9       ..
    eor #&0d                                                          ; 8380: 49 0d       I.
    rts                                                               ; 8382: 60          `

; &8383 referenced 1 time by &83f0
.sub_c8383
    lda #&90                                                          ; 8383: a9 90       ..
; &8385 referenced 1 time by &885a
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 8385: 20 91 83     ..
    sta l00c1                                                         ; 8388: 85 c1       ..
    lda #3                                                            ; 838a: a9 03       ..
    sta l00c4                                                         ; 838c: 85 c4       ..
    dec l00c0                                                         ; 838e: c6 c0       ..
    rts                                                               ; 8390: 60          `

; ***************************************************************************************
; Initialise TX control block at &00C0 from template
; 
; Copies 12 bytes from tx_ctrl_template (&836E) to &00C0.
; For the first 2 bytes (Y=0,1), also copies the fileserver
; station/network from &0E00/&0E01 to &00C2/&00C3.
; The template sets up: control=&80, port=&99 (FS command port),
; command data length=&0F, plus padding bytes.
; ***************************************************************************************
; &8391 referenced 4 times by &8385, &83df, &8428, &8fee
.init_tx_ctrl_block
    pha                                                               ; 8391: 48          H
    ldy #&0b                                                          ; 8392: a0 0b       ..
; &8394 referenced 1 time by &83a5
.fstxl1
    lda tx_ctrl_template,y                                            ; 8394: b9 a9 83    ...
    sta l00c0,y                                                       ; 8397: 99 c0 00    ...
    cpy #2                                                            ; 839a: c0 02       ..
    bpl fstxl2                                                        ; 839c: 10 06       ..
    lda fs_server_stn,y                                               ; 839e: b9 00 0e    ...
    sta l00c2,y                                                       ; 83a1: 99 c2 00    ...
; &83a4 referenced 1 time by &839c
.fstxl2
    dey                                                               ; 83a4: 88          .
    bpl fstxl1                                                        ; 83a5: 10 ed       ..
    pla                                                               ; 83a7: 68          h
    rts                                                               ; 83a8: 60          `

; ***************************************************************************************
; TX control block template (TXTAB, 12 bytes)
; 
; 12-byte template copied to &00C0 by init_tx_ctrl. Defines the
; TX control block for FS commands: control flag, port, station/
; network, and data buffer pointers (&0F00-&0FFF). The 4-byte
; Econet addresses use only the low 2 bytes; upper bytes are &FF.
; ***************************************************************************************
; &83a9 referenced 1 time by &8394
.tx_ctrl_template
    equb &80, &99, 0, 0, 0, &0f                                       ; 83a9: 80 99 00... ...
; &83af referenced 3 times by &88d8, &89b7, &9177
.l83af
    equb &ff, &ff, &ff, &0f, &ff, &ff                                 ; 83af: ff ff ff... ...

; ***************************************************************************************
; Prepare FS command with carry set
; 
; Alternate entry to prepare_fs_cmd that pushes A, loads &2A
; into fs_error_ptr, and enters with carry set (SEC). The carry
; flag is later tested by build_send_fs_cmd to select the
; byte-stream (BSXMIT) transmission path.
; ***************************************************************************************
; &83b5 referenced 1 time by &8a7f
.prepare_cmd_with_flag
    pha                                                               ; 83b5: 48          H
    sec                                                               ; 83b6: 38          8
    bcs c83cb                                                         ; 83b7: b0 12       ..             ; ALWAYS branch

; &83b9 referenced 2 times by &8720, &87c7
.prepare_cmd_clv
    clv                                                               ; 83b9: b8          .
    bvc c83ca                                                         ; 83ba: 50 0e       P.             ; ALWAYS branch

; ***************************************************************************************
; *BYE handler (logoff)
; 
; Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
; Dispatched from the command match table at &8BE4 for "BYE".
; ***************************************************************************************
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 83bc: a9 77       .w
    jsr osbyte                                                        ; 83be: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #&17                                                          ; 83c1: a0 17       ..             ; Y=function code for HDRFN
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
; &83c3 referenced 12 times by &80c5, &887d, &88f3, &893f, &8966, &89dd, &8a04, &8ada, &8b95, &8c3c, &8c73, &8cde
.prepare_fs_cmd
    clv                                                               ; 83c3: b8          .
; &83c4 referenced 2 times by &88db, &89ba
.init_tx_ctrl_data
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 83c4: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 83c7: 8d 02 0f    ...
; &83ca referenced 1 time by &83ba
.c83ca
    clc                                                               ; 83ca: 18          .
; &83cb referenced 1 time by &83b7
.c83cb
    sty fs_cmd_y_param                                                ; 83cb: 8c 01 0f    ...
    ldy #1                                                            ; 83ce: a0 01       ..
; &83d0 referenced 1 time by &83d7
.loop_c83d0
    lda fs_csd_handle,y                                               ; 83d0: b9 03 0e    ...            ; A=timeout period for FS reply
    sta fs_cmd_csd,y                                                  ; 83d3: 99 03 0f    ...
    dey                                                               ; 83d6: 88          .              ; Y=function code
    bpl loop_c83d0                                                    ; 83d7: 10 f7       ..
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
; &83d9 referenced 1 time by &8b33
.build_send_fs_cmd
    php                                                               ; 83d9: 08          .
    lda #&90                                                          ; 83da: a9 90       ..
    sta fs_cmd_type                                                   ; 83dc: 8d 00 0f    ...
    jsr init_tx_ctrl_block                                            ; 83df: 20 91 83     ..
    txa                                                               ; 83e2: 8a          .
    adc #5                                                            ; 83e3: 69 05       i.
    sta l00c8                                                         ; 83e5: 85 c8       ..
    plp                                                               ; 83e7: 28          (
    bcs dofsl5                                                        ; 83e8: b0 1a       ..
    php                                                               ; 83ea: 08          .
    jsr setup_tx_ptr_c0                                               ; 83eb: 20 87 86     ..
    plp                                                               ; 83ee: 28          (
; &83ef referenced 2 times by &87d3, &8ab7
.send_fs_reply_cmd
    php                                                               ; 83ef: 08          .
    jsr sub_c8383                                                     ; 83f0: 20 83 83     ..
    jsr c851b                                                         ; 83f3: 20 1b 85     ..
    plp                                                               ; 83f6: 28          (
; &83f7 referenced 1 time by &840d
.dofsl7
    iny                                                               ; 83f7: c8          .
    lda (l00c4),y                                                     ; 83f8: b1 c4       ..
    tax                                                               ; 83fa: aa          .
    beq return_dofsl7                                                 ; 83fb: f0 06       ..
    bvc c8401                                                         ; 83fd: 50 02       P.
    adc #&2a ; '*'                                                    ; 83ff: 69 2a       i*
; &8401 referenced 1 time by &83fd
.c8401
    bne store_fs_error                                                ; 8401: d0 70       .p
; &8403 referenced 1 time by &83fb
.return_dofsl7
    rts                                                               ; 8403: 60          `

; &8404 referenced 1 time by &83e8
.dofsl5
    pla                                                               ; 8404: 68          h
    ldx #&c0                                                          ; 8405: a2 c0       ..
    iny                                                               ; 8407: c8          .
    jsr econet_tx_retry                                               ; 8408: 20 61 92     a.
    sta l00b3                                                         ; 840b: 85 b3       ..
    bcc dofsl7                                                        ; 840d: 90 e8       ..
.bputv_handler
    clc                                                               ; 840f: 18          .
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
.handle_bput_bget
    pha                                                               ; 8410: 48          H
    sta l0fdf                                                         ; 8411: 8d df 0f    ...
    txa                                                               ; 8414: 8a          .
    pha                                                               ; 8415: 48          H
    tya                                                               ; 8416: 98          .
    pha                                                               ; 8417: 48          H
    php                                                               ; 8418: 08          .
    sty l00ba                                                         ; 8419: 84 ba       ..
    jsr handle_to_mask_clc                                            ; 841b: 20 44 86     D.
    sty l0fde                                                         ; 841e: 8c de 0f    ...
    sty l00cf                                                         ; 8421: 84 cf       ..
    ldy #&90                                                          ; 8423: a0 90       ..
    sty fs_putb_buf                                                   ; 8425: 8c dc 0f    ...
    jsr init_tx_ctrl_block                                            ; 8428: 20 91 83     ..
    lda #&dc                                                          ; 842b: a9 dc       ..
    sta l00c4                                                         ; 842d: 85 c4       ..
    lda #&e0                                                          ; 842f: a9 e0       ..
    sta l00c8                                                         ; 8431: 85 c8       ..
    iny                                                               ; 8433: c8          .
    ldx #9                                                            ; 8434: a2 09       ..
    plp                                                               ; 8436: 28          (
    bcc store_retry_count                                             ; 8437: 90 01       ..
    dex                                                               ; 8439: ca          .              ; X=&08
; &843a referenced 1 time by &8437
.store_retry_count
    stx fs_getb_buf                                                   ; 843a: 8e dd 0f    ...
    lda l00cf                                                         ; 843d: a5 cf       ..
    ldx #&c0                                                          ; 843f: a2 c0       ..
    jsr econet_tx_retry                                               ; 8441: 20 61 92     a.
    ldx fs_getb_buf                                                   ; 8444: ae dd 0f    ...
    beq update_sequence_return                                        ; 8447: f0 48       .H
    ldy #&1f                                                          ; 8449: a0 1f       ..
; &844b referenced 1 time by &8452
.error1
    lda fs_putb_buf,y                                                 ; 844b: b9 dc 0f    ...
    sta l0fe0,y                                                       ; 844e: 99 e0 0f    ...
    dey                                                               ; 8451: 88          .
    bpl error1                                                        ; 8452: 10 f7       ..
    tax                                                               ; 8454: aa          .              ; X=File handle
    lda #osbyte_read_write_exec_file_handle                           ; 8455: a9 c6       ..
    jsr osbyte                                                        ; 8457: 20 f4 ff     ..            ; Read/Write *EXEC file handle
    lda #&14                                                          ; 845a: a9 14       ..
    cpy l00ba                                                         ; 845c: c4 ba       ..             ; Y=value of *SPOOL file handle
    beq c8466                                                         ; 845e: f0 06       ..
    lda #&18                                                          ; 8460: a9 18       ..
    cpx l00ba                                                         ; 8462: e4 ba       ..             ; X=value of *EXEC file handle
    bne c846c                                                         ; 8464: d0 06       ..
; &8466 referenced 1 time by &845e
.c8466
    tax                                                               ; 8466: aa          .
    ldy #&85                                                          ; 8467: a0 85       ..
    jsr oscli                                                         ; 8469: 20 f7 ff     ..
; &846c referenced 1 time by &8464
.c846c
    lda #&e0                                                          ; 846c: a9 e0       ..
    sta l00c4                                                         ; 846e: 85 c4       ..
    ldx fs_getb_buf                                                   ; 8470: ae dd 0f    ...
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
; &8473 referenced 1 time by &8401
.store_fs_error
    stx fs_last_error                                                 ; 8473: 8e 09 0e    ...
    ldy #1                                                            ; 8476: a0 01       ..
    cpx #&a8                                                          ; 8478: e0 a8       ..
    bcs c8480                                                         ; 847a: b0 04       ..
    lda #&a8                                                          ; 847c: a9 a8       ..
    sta (l00c4),y                                                     ; 847e: 91 c4       ..
; &8480 referenced 1 time by &847a
.c8480
    ldy #&ff                                                          ; 8480: a0 ff       ..
; &8482 referenced 1 time by &848a
.loop_c8482
    iny                                                               ; 8482: c8          .
    lda (l00c4),y                                                     ; 8483: b1 c4       ..
    sta l0100,y                                                       ; 8485: 99 00 01    ...
    eor #&0d                                                          ; 8488: 49 0d       I.
    bne loop_c8482                                                    ; 848a: d0 f6       ..
    sta l0100,y                                                       ; 848c: 99 00 01    ...
    beq c84d5                                                         ; 848f: f0 44       .D             ; ALWAYS branch

; &8491 referenced 1 time by &8447
.update_sequence_return
    sta fs_sequence_nos                                               ; 8491: 8d 08 0e    ...
    pla                                                               ; 8494: 68          h
    tay                                                               ; 8495: a8          .
    pla                                                               ; 8496: 68          h
    tax                                                               ; 8497: aa          .
    pla                                                               ; 8498: 68          h
.return_remote_cmd
    rts                                                               ; 8499: 60          `

; ***************************************************************************************
; Remote boot/execute handler
; 
; Checks byte 4 of the RX control block (remote status flag).
; If zero (not currently remoted), falls through to remot1 to
; set up a new remote session. If non-zero (already remoted),
; jumps to clear_jsr_protection and returns.
; ***************************************************************************************
.remote_boot_handler
    ldy #4                                                            ; 849a: a0 04       ..
    lda (net_rx_ptr),y                                                ; 849c: b1 9c       ..
    beq remot1                                                        ; 849e: f0 03       ..
; &84a0 referenced 1 time by &84e6
.rchex
    jmp clear_jsr_protection                                          ; 84a0: 4c eb 92    L..

; &84a3 referenced 2 times by &849e, &84dc
.remot1
    ora #9                                                            ; 84a3: 09 09       ..
.sub_c84a5
l84a6 = sub_c84a5+1
    sta (net_rx_ptr),y                                                ; 84a5: 91 9c       ..
    ldx #&80                                                          ; 84a7: a2 80       ..
    ldy #&80                                                          ; 84a9: a0 80       ..
    lda (net_rx_ptr),y                                                ; 84ab: b1 9c       ..
    pha                                                               ; 84ad: 48          H
    iny                                                               ; 84ae: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 84af: b1 9c       ..
    ldy #&0f                                                          ; 84b1: a0 0f       ..
    sta (nfs_workspace),y                                             ; 84b3: 91 9e       ..
    dey                                                               ; 84b5: 88          .              ; Y=&0e
    pla                                                               ; 84b6: 68          h
    sta (nfs_workspace),y                                             ; 84b7: 91 9e       ..
    jsr clear_osbyte_ce_cf                                            ; 84b9: 20 ce 81     ..
    jsr ctrl_block_setup                                              ; 84bc: 20 7c 91     |.
    ldx #1                                                            ; 84bf: a2 01       ..
    ldy #0                                                            ; 84c1: a0 00       ..
    lda #osbyte_read_write_econet_keyboard_disable                    ; 84c3: a9 c9       ..
    jsr osbyte                                                        ; 84c5: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; ***************************************************************************************
; Execute code at &0100
; 
; Clears JSR protection, zeroes &0100-&0102 (creating a BRK
; instruction at &0100 as a safe default), then JMP &0100 to
; execute code received over the network. If no code was loaded,
; the BRK triggers an error handler.
; ***************************************************************************************
.execute_at_0100
    jsr clear_jsr_protection                                          ; 84c8: 20 eb 92     ..
    ldx #2                                                            ; 84cb: a2 02       ..
    lda #0                                                            ; 84cd: a9 00       ..
; &84cf referenced 1 time by &84d3
.loop_c84cf
    sta l0100,x                                                       ; 84cf: 9d 00 01    ...
    dex                                                               ; 84d2: ca          .
    bpl loop_c84cf                                                    ; 84d3: 10 fa       ..
; &84d5 referenced 2 times by &848f, &850e
.c84d5
    jmp l0100                                                         ; 84d5: 4c 00 01    L..

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
    ldy #4                                                            ; 84d8: a0 04       ..
    lda (net_rx_ptr),y                                                ; 84da: b1 9c       ..
    beq remot1                                                        ; 84dc: f0 c5       ..
    ldy #&80                                                          ; 84de: a0 80       ..
    lda (net_rx_ptr),y                                                ; 84e0: b1 9c       ..
    ldy #&0e                                                          ; 84e2: a0 0e       ..
    cmp (nfs_workspace),y                                             ; 84e4: d1 9e       ..
    bne rchex                                                         ; 84e6: d0 b8       ..
; ***************************************************************************************
; Insert remote keypress
; 
; Reads a character from RX block offset &82 and inserts it into
; keyboard input buffer 0 via OSBYTE &99.
; ***************************************************************************************
.insert_remote_key
    ldy #&82                                                          ; 84e8: a0 82       ..
    lda (net_rx_ptr),y                                                ; 84ea: b1 9c       ..
    tay                                                               ; 84ec: a8          .
    ldx #0                                                            ; 84ed: a2 00       ..
    jsr clear_jsr_protection                                          ; 84ef: 20 eb 92     ..
    lda #osbyte_insert_input_buffer                                   ; 84f2: a9 99       ..
    jmp osbyte                                                        ; 84f4: 4c f4 ff    L..            ; Insert character Y into input buffer X

; &84f7 referenced 1 time by &854a
.c84f7
    lda #8                                                            ; 84f7: a9 08       ..
    bne set_listen_offset                                             ; 84f9: d0 04       ..             ; ALWAYS branch

; &84fb referenced 1 time by &86d0
.nlistn
    lda (net_tx_ptr,x)                                                ; 84fb: a1 9a       ..
; &84fd referenced 1 time by &89fc
.nlisne
    and #7                                                            ; 84fd: 29 07       ).
; &84ff referenced 1 time by &84f9
.set_listen_offset
    tax                                                               ; 84ff: aa          .
    ldy l8018,x                                                       ; 8500: bc 18 80    ...
    ldx #0                                                            ; 8503: a2 00       ..
    stx l0100                                                         ; 8505: 8e 00 01    ...
; &8508 referenced 1 time by &8512
.loop_c8508
    lda l8579,y                                                       ; 8508: b9 79 85    .y.
    sta l0101,x                                                       ; 850b: 9d 01 01    ...
    beq c84d5                                                         ; 850e: f0 c5       ..
    iny                                                               ; 8510: c8          .
    inx                                                               ; 8511: e8          .
    bne loop_c8508                                                    ; 8512: d0 f4       ..
    equs "SP."                                                        ; 8514: 53 50 2e    SP.
    equb &0d, &45, &2e, &0d                                           ; 8517: 0d 45 2e... .E.

; &851b referenced 5 times by &83f3, &8779, &8864, &9031, &9296
.c851b
    lda #&2a ; '*'                                                    ; 851b: a9 2a       .*
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
.send_to_fs
    pha                                                               ; 851d: 48          H
    lda rx_flags                                                      ; 851e: ad 64 0d    .d.
    pha                                                               ; 8521: 48          H
    ora #&80                                                          ; 8522: 09 80       ..
    sta rx_flags                                                      ; 8524: 8d 64 0d    .d.
    lda #0                                                            ; 8527: a9 00       ..
    pha                                                               ; 8529: 48          H
    pha                                                               ; 852a: 48          H
    tay                                                               ; 852b: a8          .              ; Y=&00
    tsx                                                               ; 852c: ba          .
; &852d referenced 3 times by &8537, &853c, &8541
.c852d
    jsr l854d                                                         ; 852d: 20 4d 85     M.
.incpx
    lda (net_tx_ptr),y                                                ; 8530: b1 9a       ..
    bmi fs_wait_cleanup                                               ; 8532: 30 0f       0.
    dec l0101,x                                                       ; 8534: de 01 01    ...
    bne c852d                                                         ; 8537: d0 f4       ..
    dec l0102,x                                                       ; 8539: de 02 01    ...
    bne c852d                                                         ; 853c: d0 ef       ..
    dec l0104,x                                                       ; 853e: de 04 01    ...
    bne c852d                                                         ; 8541: d0 ea       ..
; &8543 referenced 1 time by &8532
.fs_wait_cleanup
    pla                                                               ; 8543: 68          h
    pla                                                               ; 8544: 68          h
    pla                                                               ; 8545: 68          h
    sta rx_flags                                                      ; 8546: 8d 64 0d    .d.
    pla                                                               ; 8549: 68          h
    beq c84f7                                                         ; 854a: f0 ab       ..
    rts                                                               ; 854c: 60          `

; &854d referenced 3 times by &80b0, &852d, &86b7
.l854d
    equb &24                                                          ; 854d: 24          $
.l854e
l8579 = l854e+43
    equs &ff, &10, "'", &a9, "~ ", &f4, &ff, "J", &91, &9a, &0a, &d0  ; 854e: ff 10 27... ..'
    equs &a1, "8 ", &10, &84, "8", &a9, &fe, ",", &df, &0f, "p", &10  ; 855b: a1 38 20... .8
    equs &18, 8, &a5, &cf, "(0", 3, " ~", &86, " y", &86, &ad, &de    ; 8568: 18 08 a5... ...
    equs &0f, "`", &a0, "Line Jammed", 0                              ; 8577: 0f 60 a0... .`.
; &8579 referenced 1 time by &8508
    equb &a1                                                          ; 8586: a1          .
    equs "Net Error", 0                                               ; 8587: 4e 65 74... Net
    equb &a2                                                          ; 8591: a2          .
    equs "Not listening", 0                                           ; 8592: 4e 6f 74... Not
    equb &a3                                                          ; 85a0: a3          .
    equs "No Clock", 0                                                ; 85a1: 4e 6f 20... No
    equb &11                                                          ; 85aa: 11          .
    equs "Escape", 0                                                  ; 85ab: 45 73 63... Esc
    equb &cb                                                          ; 85b2: cb          .
    equs "Bad Option", 0                                              ; 85b3: 42 61 64... Bad
    equb &a5                                                          ; 85be: a5          .
    equs "No reply", 0                                                ; 85bf: 4e 6f 20... No

; ***************************************************************************************
; Save FSCV arguments with text pointers
; 
; Extended entry used by FSCV, FINDV, and fscv_star_handler.
; Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
; falls through to save_fscv_args to store A/X/Y in the FS
; workspace.
; ***************************************************************************************
; &85c8 referenced 3 times by &80d4, &8994, &8bd7
.save_fscv_args_with_ptrs
    stx os_text_ptr                                                   ; 85c8: 86 f2       ..
    sty l00f3                                                         ; 85ca: 84 f3       ..
    stx fs_cmd_ptr                                                    ; 85cc: 8e 10 0e    ...
    sty l0e11                                                         ; 85cf: 8c 11 0e    ...
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
; &85d2 referenced 3 times by &8705, &8924, &8a2e
.save_fscv_args
    sta fs_last_byte_flag                                             ; 85d2: 85 bd       ..
    stx fs_options                                                    ; 85d4: 86 bb       ..
    sty fs_block_offset                                               ; 85d6: 84 bc       ..
    stx fs_crc_lo                                                     ; 85d8: 86 be       ..
    sty fs_crc_hi                                                     ; 85da: 84 bf       ..
    rts                                                               ; 85dc: 60          `

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
; &85dd referenced 2 times by &88b7, &88e2
.decode_attribs_6bit
    ldy #&0e                                                          ; 85dd: a0 0e       ..
    lda (fs_options),y                                                ; 85df: b1 bb       ..
    and #&3f ; '?'                                                    ; 85e1: 29 3f       )?
    ldx #4                                                            ; 85e3: a2 04       ..
    bne c85eb                                                         ; 85e5: d0 04       ..             ; ALWAYS branch

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
; &85e7 referenced 2 times by &87de, &88ff
.decode_attribs_5bit
    and #&1f                                                          ; 85e7: 29 1f       ).
    ldx #&ff                                                          ; 85e9: a2 ff       ..
; &85eb referenced 1 time by &85e5
.c85eb
    sta fs_error_ptr                                                  ; 85eb: 85 b8       ..
    lda #0                                                            ; 85ed: a9 00       ..
; &85ef referenced 1 time by &85f7
.loop_c85ef
    inx                                                               ; 85ef: e8          .
    lsr fs_error_ptr                                                  ; 85f0: 46 b8       F.
    bcc c85f7                                                         ; 85f2: 90 03       ..
    ora access_bit_table,x                                            ; 85f4: 1d fa 85    ...
; &85f7 referenced 1 time by &85f2
.c85f7
    bne loop_c85ef                                                    ; 85f7: d0 f6       ..
    rts                                                               ; 85f9: 60          `

; &85fa referenced 1 time by &85f4
.access_bit_table
    equb &50, &20, 5, 2, &88, 4, 8, &80, &10, 1, 2                    ; 85fa: 50 20 05... P .

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
; &8605 referenced 13 times by &8204, &822e, &824e, &825b, &8c44, &8c4e, &8c5c, &8c67, &8c7c, &8c91, &8ca4, &8cb3, &8d9e
.print_inline
    pla                                                               ; 8605: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 8606: 85 b0       ..
    pla                                                               ; 8608: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 8609: 85 b1       ..
    ldy #0                                                            ; 860b: a0 00       ..
; &860d referenced 1 time by &861a
.loop_c860d
    inc fs_load_addr                                                  ; 860d: e6 b0       ..             ; Advance pointer past return address / to next char
    bne c8613                                                         ; 860f: d0 02       ..
    inc fs_load_addr_hi                                               ; 8611: e6 b1       ..
; &8613 referenced 1 time by &860f
.c8613
    lda (fs_load_addr),y                                              ; 8613: b1 b0       ..             ; Load next byte from inline string
    bmi parse_decimal                                                 ; 8615: 30 06       0.             ; Bit 7 set? Done — this byte is the next opcode; Parse decimal number from (fs_options),Y (DECIN)
    jsr osasci                                                        ; 8617: 20 e3 ff     ..            ; Write character
    jmp loop_c860d                                                    ; 861a: 4c 0d 86    L..

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
; &861d referenced 1 time by &8615
.parse_decimal
    jmp (fs_load_addr)                                                ; 861d: 6c b0 00    l..            ; Jump to address of high-bit byte (resumes code after string)

; &8620 referenced 2 times by &808c, &8095
.sub_c8620
    lda #0                                                            ; 8620: a9 00       ..
    sta fs_load_addr_2                                                ; 8622: 85 b2       ..
; &8624 referenced 1 time by &863d
.loop_c8624
    lda (fs_options),y                                                ; 8624: b1 bb       ..
    cmp #&2e ; '.'                                                    ; 8626: c9 2e       ..
    beq c8640                                                         ; 8628: f0 16       ..
    bcc c863f                                                         ; 862a: 90 13       ..
    and #&0f                                                          ; 862c: 29 0f       ).
    sta l00b3                                                         ; 862e: 85 b3       ..
    asl fs_load_addr_2                                                ; 8630: 06 b2       ..
    lda fs_load_addr_2                                                ; 8632: a5 b2       ..
    asl a                                                             ; 8634: 0a          .
    asl a                                                             ; 8635: 0a          .
    adc fs_load_addr_2                                                ; 8636: 65 b2       e.
    adc l00b3                                                         ; 8638: 65 b3       e.
    sta fs_load_addr_2                                                ; 863a: 85 b2       ..
    iny                                                               ; 863c: c8          .
    bne loop_c8624                                                    ; 863d: d0 e5       ..
; &863f referenced 1 time by &862a
.c863f
    clc                                                               ; 863f: 18          .
; &8640 referenced 1 time by &8628
.c8640
    lda fs_load_addr_2                                                ; 8640: a5 b2       ..
    rts                                                               ; 8642: 60          `

; &8643 referenced 3 times by &886b, &8a49, &8f53
.handle_to_mask_a
    tay                                                               ; 8643: a8          .
; &8644 referenced 2 times by &841b, &892f
.handle_to_mask_clc
    clc                                                               ; 8644: 18          .
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
; &8645 referenced 1 time by &8998
.handle_to_mask
    pha                                                               ; 8645: 48          H
    txa                                                               ; 8646: 8a          .
    pha                                                               ; 8647: 48          H
    tya                                                               ; 8648: 98          .
    bcc y2fsl5                                                        ; 8649: 90 02       ..
    beq c865c                                                         ; 864b: f0 0f       ..
; &864d referenced 1 time by &8649
.y2fsl5
    sec                                                               ; 864d: 38          8
    sbc #&1f                                                          ; 864e: e9 1f       ..
    tax                                                               ; 8650: aa          .
    lda #1                                                            ; 8651: a9 01       ..
; &8653 referenced 1 time by &8655
.y2fsl2
    asl a                                                             ; 8653: 0a          .
    dex                                                               ; 8654: ca          .
    bne y2fsl2                                                        ; 8655: d0 fc       ..
    ror a                                                             ; 8657: 6a          j
    tay                                                               ; 8658: a8          .
    bne c865c                                                         ; 8659: d0 01       ..
    dey                                                               ; 865b: 88          .
; &865c referenced 2 times by &864b, &8659
.c865c
    pla                                                               ; 865c: 68          h
    tax                                                               ; 865d: aa          .
    pla                                                               ; 865e: 68          h
    rts                                                               ; 865f: 60          `

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
; &8660 referenced 2 times by &89c7, &8f6b
.mask_to_handle
    ldx #&1f                                                          ; 8660: a2 1f       ..
; &8662 referenced 1 time by &8664
.fs2al1
    inx                                                               ; 8662: e8          .
    lsr a                                                             ; 8663: 4a          J
    bne fs2al1                                                        ; 8664: d0 fc       ..
    txa                                                               ; 8666: 8a          .
    rts                                                               ; 8667: 60          `

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
; &8668 referenced 2 times by &875f, &8815
.compare_addresses
    ldx #4                                                            ; 8668: a2 04       ..
; &866a referenced 1 time by &8671
.loop_c866a
    lda l00af,x                                                       ; 866a: b5 af       ..
    eor l00b3,x                                                       ; 866c: 55 b3       U.
    bne return_compare                                                ; 866e: d0 03       ..
    dex                                                               ; 8670: ca          .
    bne loop_c866a                                                    ; 8671: d0 f7       ..
; &8673 referenced 1 time by &866e
.return_compare
    rts                                                               ; 8673: 60          `

.fscv_read_handles
    ldx #&20 ; ' '                                                    ; 8674: a2 20       .
    ldy #&27 ; '''                                                    ; 8676: a0 27       .'
.return_fscv_handles
    rts                                                               ; 8678: 60          `

; &8679 referenced 4 times by &896c, &89c3, &89e3, &8ac4
.sub_c8679
    ora fs_eof_flags                                                  ; 8679: 0d 07 0e    ...
    bne store_fs_flag                                                 ; 867c: d0 05       ..
; ***************************************************************************************
; Clear bit(s) in FS flags (&0E07)
; 
; Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
; the specified bits. JMPs to the shared STA at &865C, skipping
; the ORA in set_fs_flag.
; ***************************************************************************************
; &867e referenced 2 times by &8886, &8ac1
.clear_fs_flag
    eor #&ff                                                          ; 867e: 49 ff       I.
; ***************************************************************************************
; Set bit(s) in FS flags (&0E07)
; 
; ORs A into fs_work_0e07 (EOF hint byte), then falls through
; to STA fs_eof_flags at &865C (shared with clear_fs_flag).
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
    and fs_eof_flags                                                  ; 8680: 2d 07 0e    -..
; &8683 referenced 1 time by &867c
.store_fs_flag
    sta fs_eof_flags                                                  ; 8683: 8d 07 0e    ...
    rts                                                               ; 8686: 60          `

; ***************************************************************************************
; Set up TX pointer to control block at &00C0
; 
; Points net_tx_ptr to &00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; ***************************************************************************************
; &8687 referenced 2 times by &83eb, &8855
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 8687: a2 c0       ..
.sub_c8689
    stx net_tx_ptr                                                    ; 8689: 86 9a       ..
    ldx #0                                                            ; 868b: a2 00       ..
    stx net_tx_ptr_hi                                                 ; 868d: 86 9b       ..
; ***************************************************************************************
; Transmit and poll for result (full retry)
; 
; Sets A=&FF (retry count) and Y=&60 (timeout parameter).
; Falls through to tx_poll_core.
; ***************************************************************************************
; &868f referenced 4 times by &901a, &9073, &90d0, &9274
.tx_poll_ff
    lda #&ff                                                          ; 868f: a9 ff       ..
.tx_poll_timeout
    ldy #&60 ; '`'                                                    ; 8691: a0 60       .`             ; Y=timeout parameter (&60 = standard)
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
.tx_poll_core
    pha                                                               ; 8693: 48          H
    tya                                                               ; 8694: 98          .
    pha                                                               ; 8695: 48          H
    ldx #0                                                            ; 8696: a2 00       ..
    lda (net_tx_ptr,x)                                                ; 8698: a1 9a       ..
; &869a referenced 1 time by &86cd
.c869a
    sta (net_tx_ptr,x)                                                ; 869a: 81 9a       ..
    pha                                                               ; 869c: 48          H
; &869d referenced 1 time by &86a0
.loop_c869d
    asl tx_clear_flag                                                 ; 869d: 0e 62 0d    .b.
    bcc loop_c869d                                                    ; 86a0: 90 fb       ..
    lda net_tx_ptr                                                    ; 86a2: a5 9a       ..
    sta nmi_tx_block                                                  ; 86a4: 85 a0       ..
    lda net_tx_ptr_hi                                                 ; 86a6: a5 9b       ..
    sta nmi_tx_block_hi                                               ; 86a8: 85 a1       ..
    jsr trampoline_tx_setup                                           ; 86aa: 20 60 96     `.
; &86ad referenced 1 time by &86af
.l4
    lda (net_tx_ptr,x)                                                ; 86ad: a1 9a       ..
    bmi l4                                                            ; 86af: 30 fc       0.
    asl a                                                             ; 86b1: 0a          .
    bpl c86d3                                                         ; 86b2: 10 1f       ..
    asl a                                                             ; 86b4: 0a          .
    beq c86cf                                                         ; 86b5: f0 18       ..
    jsr l854d                                                         ; 86b7: 20 4d 85     M.
    pla                                                               ; 86ba: 68          h
    tax                                                               ; 86bb: aa          .
    pla                                                               ; 86bc: 68          h
    tay                                                               ; 86bd: a8          .
    pla                                                               ; 86be: 68          h
    beq c86cf                                                         ; 86bf: f0 0e       ..
    sbc #1                                                            ; 86c1: e9 01       ..
    pha                                                               ; 86c3: 48          H
    tya                                                               ; 86c4: 98          .
    pha                                                               ; 86c5: 48          H
    txa                                                               ; 86c6: 8a          .
; &86c7 referenced 2 times by &86c8, &86cb
.c86c7
    dex                                                               ; 86c7: ca          .
    bne c86c7                                                         ; 86c8: d0 fd       ..
    dey                                                               ; 86ca: 88          .
    bne c86c7                                                         ; 86cb: d0 fa       ..
    beq c869a                                                         ; 86cd: f0 cb       ..             ; ALWAYS branch

; &86cf referenced 2 times by &86b5, &86bf
.c86cf
    tax                                                               ; 86cf: aa          .
    jmp nlistn                                                        ; 86d0: 4c fb 84    L..

; &86d3 referenced 1 time by &86b2
.c86d3
    pla                                                               ; 86d3: 68          h
    pla                                                               ; 86d4: 68          h
    pla                                                               ; 86d5: 68          h
    rts                                                               ; 86d6: 60          `

; &86d7 referenced 1 time by &8708
.sub_c86d7
    ldy #1                                                            ; 86d7: a0 01       ..
; &86d9 referenced 1 time by &86df
.file1
    lda (fs_options),y                                                ; 86d9: b1 bb       ..
    sta os_text_ptr,y                                                 ; 86db: 99 f2 00    ...
    dey                                                               ; 86de: 88          .
    bpl file1                                                         ; 86df: 10 f8       ..
; ***************************************************************************************
; Parse filename using GSINIT/GSREAD into &0E30
; 
; Uses the MOS GSINIT/GSREAD API to parse a filename string from
; (os_text_ptr),Y, handling quoted strings and |-escaped characters.
; Stores the parsed result CR-terminated at &0E30 and sets up
; fs_crc_lo/hi to point to that buffer. Sub-entry at &86C5 allows
; a non-zero starting Y offset.
; 
; On Entry:
;     Y: offset into (os_text_ptr) buffer (0 at &86C3)
; 
; On Exit:
;     X: length of parsed string
;     Y: preserved
; ***************************************************************************************
; &86e1 referenced 2 times by &89ad, &8dcf
.parse_filename_gs
    ldy #0                                                            ; 86e1: a0 00       ..
; &86e3 referenced 1 time by &8c32
.sub_c86e3
    ldx #&ff                                                          ; 86e3: a2 ff       ..
    clc                                                               ; 86e5: 18          .
    jsr gsinit                                                        ; 86e6: 20 c2 ff     ..
    beq c86f6                                                         ; 86e9: f0 0b       ..
; &86eb referenced 1 time by &86f4
.delay_1ms
.quote1
    jsr gsread                                                        ; 86eb: 20 c5 ff     ..
    bcs c86f6                                                         ; 86ee: b0 06       ..
    inx                                                               ; 86f0: e8          .
    sta l0e30,x                                                       ; 86f1: 9d 30 0e    .0.
    bcc delay_1ms                                                     ; 86f4: 90 f5       ..             ; ALWAYS branch

; &86f6 referenced 2 times by &86e9, &86ee
.c86f6
    inx                                                               ; 86f6: e8          .
    lda #&0d                                                          ; 86f7: a9 0d       ..
    sta l0e30,x                                                       ; 86f9: 9d 30 0e    .0.
    lda #&30 ; '0'                                                    ; 86fc: a9 30       .0
    sta fs_crc_lo                                                     ; 86fe: 85 be       ..
    lda #&0e                                                          ; 8700: a9 0e       ..
    sta fs_crc_hi                                                     ; 8702: 85 bf       ..
    rts                                                               ; 8704: 60          `

; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Calls save_fscv_args (&85A6) to preserve A/X/Y, then JSR &86B0
; to copy the 2-byte filename pointer from the parameter block to
; os_text_ptr and fall through to parse_filename_gs (&86BA) which
; parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
; the parsed filename buffer.
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
    jsr save_fscv_args                                                ; 8705: 20 d2 85     ..
    jsr sub_c86d7                                                     ; 8708: 20 d7 86     ..
    lda fs_last_byte_flag                                             ; 870b: a5 bd       ..
    bpl saveop                                                        ; 870d: 10 7b       .{
    cmp #&ff                                                          ; 870f: c9 ff       ..
    beq loadop                                                        ; 8711: f0 03       ..
    jmp restore_args_return                                           ; 8713: 4c 6f 89    Lo.

; &8716 referenced 1 time by &8711
.loadop
    jsr copy_filename                                                 ; 8716: 20 75 8d     u.
    ldy #2                                                            ; 8719: a0 02       ..
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
; &871b referenced 1 time by &8e00
.send_fs_examine
    lda #&92                                                          ; 871b: a9 92       ..
    sta fs_cmd_urd                                                    ; 871d: 8d 02 0f    ...
    jsr prepare_cmd_clv                                               ; 8720: 20 b9 83     ..
    ldy #6                                                            ; 8723: a0 06       ..
    lda (fs_options),y                                                ; 8725: b1 bb       ..
    bne lodfil                                                        ; 8727: d0 08       ..
    jsr copy_load_addr_from_params                                    ; 8729: 20 f0 87     ..
    jsr copy_reply_to_params                                          ; 872c: 20 02 88     ..
    bcc c8737                                                         ; 872f: 90 06       ..
; &8731 referenced 1 time by &8727
.lodfil
    jsr copy_reply_to_params                                          ; 8731: 20 02 88     ..
    jsr copy_load_addr_from_params                                    ; 8734: 20 f0 87     ..
; &8737 referenced 1 time by &872f
.c8737
    ldy #4                                                            ; 8737: a0 04       ..
; &8739 referenced 1 time by &8744
.loop_c8739
    lda fs_load_addr,x                                                ; 8739: b5 b0       ..
    sta l00c8,x                                                       ; 873b: 95 c8       ..
    adc l0f0d,x                                                       ; 873d: 7d 0d 0f    }..
    sta l00b4,x                                                       ; 8740: 95 b4       ..
    inx                                                               ; 8742: e8          .
    dey                                                               ; 8743: 88          .
    bne loop_c8739                                                    ; 8744: d0 f3       ..
    sec                                                               ; 8746: 38          8
    sbc l0f10                                                         ; 8747: ed 10 0f    ...
    sta l00b7                                                         ; 874a: 85 b7       ..
    jsr print_file_info                                               ; 874c: 20 24 8d     $.
    jsr send_data_blocks                                              ; 874f: 20 5f 87     _.
    ldx #2                                                            ; 8752: a2 02       ..
; &8754 referenced 1 time by &875b
.floop
    lda l0f10,x                                                       ; 8754: bd 10 0f    ...
    sta fs_cmd_data,x                                                 ; 8757: 9d 05 0f    ...
    dex                                                               ; 875a: ca          .
    bpl floop                                                         ; 875b: 10 f7       ..
    bmi c87d3                                                         ; 875d: 30 74       0t             ; ALWAYS branch

; ***************************************************************************************
; Send file data in multi-block chunks
; 
; Repeatedly sends &80-byte (128-byte) blocks of file data to the
; fileserver using command &7F. Compares current address (&C8-&CB)
; against end address (&B4-&B7) via compare_addresses, and loops
; until the entire file has been transferred. Each block is sent
; via send_to_fs_star.
; ***************************************************************************************
; &875f referenced 2 times by &874f, &8ab4
.send_data_blocks
    jsr compare_addresses                                             ; 875f: 20 68 86     h.            ; Compare two 4-byte addresses
    beq return_lodchk                                                 ; 8762: f0 25       .%
    lda #&92                                                          ; 8764: a9 92       ..
    sta l00c1                                                         ; 8766: 85 c1       ..
; &8768 referenced 1 time by &8784
.loop_c8768
    ldx #3                                                            ; 8768: a2 03       ..
; &876a referenced 1 time by &8773
.loop_c876a
    lda l00c8,x                                                       ; 876a: b5 c8       ..
    sta l00c4,x                                                       ; 876c: 95 c4       ..
    lda l00b4,x                                                       ; 876e: b5 b4       ..
    sta l00c8,x                                                       ; 8770: 95 c8       ..
    dex                                                               ; 8772: ca          .
    bpl loop_c876a                                                    ; 8773: 10 f5       ..
    lda #&7f                                                          ; 8775: a9 7f       ..
    sta l00c0                                                         ; 8777: 85 c0       ..
    jsr c851b                                                         ; 8779: 20 1b 85     ..
    ldy #3                                                            ; 877c: a0 03       ..
; &877e referenced 1 time by &8787
.lodchk
    lda l00c8,y                                                       ; 877e: b9 c8 00    ...
    eor l00b4,y                                                       ; 8781: 59 b4 00    Y..
    bne loop_c8768                                                    ; 8784: d0 e2       ..
    dey                                                               ; 8786: 88          .
    bpl lodchk                                                        ; 8787: 10 f5       ..
; &8789 referenced 1 time by &8762
.return_lodchk
    rts                                                               ; 8789: 60          `

; &878a referenced 1 time by &870d
.saveop
    beq filev_save                                                    ; 878a: f0 03       ..
    jmp filev_attrib_dispatch                                         ; 878c: 4c 8d 88    L..

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
; &878f referenced 1 time by &878a
.filev_save
    ldx #4                                                            ; 878f: a2 04       ..
    ldy #&0e                                                          ; 8791: a0 0e       ..
; &8793 referenced 1 time by &87ad
.savsiz
    lda (fs_options),y                                                ; 8793: b1 bb       ..
    sta port_ws_offset,y                                              ; 8795: 99 a6 00    ...
    jsr sub_4_from_y                                                  ; 8798: 20 0f 88     ..
    sbc (fs_options),y                                                ; 879b: f1 bb       ..
    sta fs_cmd_csd,y                                                  ; 879d: 99 03 0f    ...
    pha                                                               ; 87a0: 48          H
    lda (fs_options),y                                                ; 87a1: b1 bb       ..
    sta port_ws_offset,y                                              ; 87a3: 99 a6 00    ...
    pla                                                               ; 87a6: 68          h
    sta (fs_options),y                                                ; 87a7: 91 bb       ..
    jsr add_5_to_y                                                    ; 87a9: 20 fc 87     ..
    dex                                                               ; 87ac: ca          .
    bne savsiz                                                        ; 87ad: d0 e4       ..
    ldy #9                                                            ; 87af: a0 09       ..
; &87b1 referenced 1 time by &87b7
.loop_c87b1
    lda (fs_options),y                                                ; 87b1: b1 bb       ..
    sta fs_cmd_csd,y                                                  ; 87b3: 99 03 0f    ...
    dey                                                               ; 87b6: 88          .
    bne loop_c87b1                                                    ; 87b7: d0 f8       ..
    lda #&91                                                          ; 87b9: a9 91       ..
    sta fs_cmd_urd                                                    ; 87bb: 8d 02 0f    ...
    sta fs_error_ptr                                                  ; 87be: 85 b8       ..
    ldx #&0b                                                          ; 87c0: a2 0b       ..
    jsr copy_string_to_cmd                                            ; 87c2: 20 77 8d     w.
    ldy #1                                                            ; 87c5: a0 01       ..
    jsr prepare_cmd_clv                                               ; 87c7: 20 b9 83     ..
    jsr print_file_info                                               ; 87ca: 20 24 8d     $.
    lda fs_cmd_data                                                   ; 87cd: ad 05 0f    ...
    jsr transfer_file_blocks                                          ; 87d0: 20 14 88     ..
; &87d3 referenced 1 time by &875d
.c87d3
    jsr send_fs_reply_cmd                                             ; 87d3: 20 ef 83     ..
    stx l0f08                                                         ; 87d6: 8e 08 0f    ...
    ldy #&0e                                                          ; 87d9: a0 0e       ..
    lda fs_cmd_data                                                   ; 87db: ad 05 0f    ...
    jsr decode_attribs_5bit                                           ; 87de: 20 e7 85     ..
    beq c87e6                                                         ; 87e1: f0 03       ..
; &87e3 referenced 1 time by &87eb
.loop_c87e3
    lda l0ef7,y                                                       ; 87e3: b9 f7 0e    ...
; &87e6 referenced 1 time by &87e1
.c87e6
    sta (fs_options),y                                                ; 87e6: 91 bb       ..
    iny                                                               ; 87e8: c8          .
    cpy #&12                                                          ; 87e9: c0 12       ..
    bne loop_c87e3                                                    ; 87eb: d0 f6       ..
    jmp restore_args_return                                           ; 87ed: 4c 6f 89    Lo.

; ***************************************************************************************
; Copy load address from parameter block
; 
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to &AE-&B3 (local workspace).
; ***************************************************************************************
; &87f0 referenced 2 times by &8729, &8734
.copy_load_addr_from_params
    ldy #5                                                            ; 87f0: a0 05       ..
; &87f2 referenced 1 time by &87fa
.lodrl1
    lda (fs_options),y                                                ; 87f2: b1 bb       ..
    sta l00ae,y                                                       ; 87f4: 99 ae 00    ...
    dey                                                               ; 87f7: 88          .
    cpy #2                                                            ; 87f8: c0 02       ..
    bcs lodrl1                                                        ; 87fa: b0 f6       ..
; &87fc referenced 1 time by &87a9
.add_5_to_y
    iny                                                               ; 87fc: c8          .
; &87fd referenced 1 time by &8a91
.add_4_to_y
    iny                                                               ; 87fd: c8          .
    iny                                                               ; 87fe: c8          .
    iny                                                               ; 87ff: c8          .
    iny                                                               ; 8800: c8          .
    rts                                                               ; 8801: 60          `

; ***************************************************************************************
; Copy FS reply data to parameter block
; 
; Copies bytes from the FS command reply buffer (&0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; ***************************************************************************************
; &8802 referenced 2 times by &872c, &8731
.copy_reply_to_params
    ldy #&0d                                                          ; 8802: a0 0d       ..
    txa                                                               ; 8804: 8a          .
; &8805 referenced 1 time by &880d
.lodrl2
    sta (fs_options),y                                                ; 8805: 91 bb       ..
    lda fs_cmd_urd,y                                                  ; 8807: b9 02 0f    ...
    dey                                                               ; 880a: 88          .
    cpy #2                                                            ; 880b: c0 02       ..
    bcs lodrl2                                                        ; 880d: b0 f6       ..
; &880f referenced 1 time by &8798
.sub_4_from_y
    dey                                                               ; 880f: 88          .
; &8810 referenced 2 times by &88a5, &8a99
.sub_3_from_y
    dey                                                               ; 8810: 88          .
    dey                                                               ; 8811: 88          .
    dey                                                               ; 8812: 88          .
    rts                                                               ; 8813: 60          `

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
; &8814 referenced 2 times by &87d0, &8aaf
.transfer_file_blocks
    pha                                                               ; 8814: 48          H
    jsr compare_addresses                                             ; 8815: 20 68 86     h.            ; Compare two 4-byte addresses
    beq c8889                                                         ; 8818: f0 6f       .o
; &881a referenced 1 time by &8867
.c881a
    ldx #0                                                            ; 881a: a2 00       ..
    ldy #4                                                            ; 881c: a0 04       ..
    stx l0f08                                                         ; 881e: 8e 08 0f    ...
    stx l0f09                                                         ; 8821: 8e 09 0f    ...
    clc                                                               ; 8824: 18          .
; &8825 referenced 1 time by &8832
.loop_c8825
    lda fs_load_addr,x                                                ; 8825: b5 b0       ..
    sta l00c4,x                                                       ; 8827: 95 c4       ..
    adc l0f06,x                                                       ; 8829: 7d 06 0f    }..
    sta l00c8,x                                                       ; 882c: 95 c8       ..
    sta fs_load_addr,x                                                ; 882e: 95 b0       ..
    inx                                                               ; 8830: e8          .
    dey                                                               ; 8831: 88          .
    bne loop_c8825                                                    ; 8832: d0 f1       ..
    bcs c8843                                                         ; 8834: b0 0d       ..
    sec                                                               ; 8836: 38          8
; &8837 referenced 1 time by &883f
.savchk
    lda fs_load_addr,y                                                ; 8837: b9 b0 00    ...
    sbc l00b4,y                                                       ; 883a: f9 b4 00    ...
    iny                                                               ; 883d: c8          .
    dex                                                               ; 883e: ca          .
    bne savchk                                                        ; 883f: d0 f6       ..
    bcc c884c                                                         ; 8841: 90 09       ..
; &8843 referenced 1 time by &8834
.c8843
    ldx #3                                                            ; 8843: a2 03       ..
; &8845 referenced 1 time by &884a
.loop_c8845
    lda l00b4,x                                                       ; 8845: b5 b4       ..
    sta l00c8,x                                                       ; 8847: 95 c8       ..
    dex                                                               ; 8849: ca          .
    bpl loop_c8845                                                    ; 884a: 10 f9       ..
; &884c referenced 1 time by &8841
.c884c
    pla                                                               ; 884c: 68          h
    pha                                                               ; 884d: 48          H
    php                                                               ; 884e: 08          .
    sta l00c1                                                         ; 884f: 85 c1       ..
    lda #&80                                                          ; 8851: a9 80       ..
    sta l00c0                                                         ; 8853: 85 c0       ..
    jsr setup_tx_ptr_c0                                               ; 8855: 20 87 86     ..
    lda fs_error_ptr                                                  ; 8858: a5 b8       ..
    jsr init_tx_ctrl_port                                             ; 885a: 20 85 83     ..
    plp                                                               ; 885d: 28          (
    bcs c8889                                                         ; 885e: b0 29       .)
    lda #&91                                                          ; 8860: a9 91       ..
    sta l00c1                                                         ; 8862: 85 c1       ..
    jsr c851b                                                         ; 8864: 20 1b 85     ..
    bne c881a                                                         ; 8867: d0 b1       ..
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
    pha                                                               ; 8869: 48          H
    txa                                                               ; 886a: 8a          .
    jsr handle_to_mask_a                                              ; 886b: 20 43 86     C.
    tya                                                               ; 886e: 98          .
    and fs_eof_flags                                                  ; 886f: 2d 07 0e    -..
    tax                                                               ; 8872: aa          .
    beq c8889                                                         ; 8873: f0 14       ..
    pha                                                               ; 8875: 48          H
    sty fs_cmd_data                                                   ; 8876: 8c 05 0f    ...
    ldy #&11                                                          ; 8879: a0 11       ..             ; Y=function code for HDRFN
    ldx #1                                                            ; 887b: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 887d: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    pla                                                               ; 8880: 68          h
    ldx fs_cmd_data                                                   ; 8881: ae 05 0f    ...
    bne c8889                                                         ; 8884: d0 03       ..
    jsr clear_fs_flag                                                 ; 8886: 20 7e 86     ~.
; &8889 referenced 4 times by &8818, &885e, &8873, &8884
.c8889
    pla                                                               ; 8889: 68          h
    ldy fs_block_offset                                               ; 888a: a4 bc       ..
    rts                                                               ; 888c: 60          `

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
; &888d referenced 1 time by &878c
.filev_attrib_dispatch
    sta fs_cmd_data                                                   ; 888d: 8d 05 0f    ...
    cmp #6                                                            ; 8890: c9 06       ..
    beq cha6                                                          ; 8892: f0 3f       .?
    bcs c88de                                                         ; 8894: b0 48       .H
    cmp #5                                                            ; 8896: c9 05       ..
    beq cha5                                                          ; 8898: f0 52       .R
    cmp #4                                                            ; 889a: c9 04       ..
    beq cha4                                                          ; 889c: f0 44       .D
    cmp #1                                                            ; 889e: c9 01       ..
    beq get_file_protection                                           ; 88a0: f0 15       ..
    asl a                                                             ; 88a2: 0a          .
    asl a                                                             ; 88a3: 0a          .
    tay                                                               ; 88a4: a8          .
    jsr sub_3_from_y                                                  ; 88a5: 20 10 88     ..
    ldx #3                                                            ; 88a8: a2 03       ..
; &88aa referenced 1 time by &88b1
.chalp1
    lda (fs_options),y                                                ; 88aa: b1 bb       ..
    sta l0f06,x                                                       ; 88ac: 9d 06 0f    ...
    dey                                                               ; 88af: 88          .
    dex                                                               ; 88b0: ca          .
    bpl chalp1                                                        ; 88b1: 10 f7       ..
    ldx #5                                                            ; 88b3: a2 05       ..
    bne copy_filename_to_cmd                                          ; 88b5: d0 15       ..             ; ALWAYS branch

; &88b7 referenced 1 time by &88a0
.get_file_protection
    jsr decode_attribs_6bit                                           ; 88b7: 20 dd 85     ..
    sta l0f0e                                                         ; 88ba: 8d 0e 0f    ...
    ldy #9                                                            ; 88bd: a0 09       ..
    ldx #8                                                            ; 88bf: a2 08       ..
; &88c1 referenced 1 time by &88c8
.chalp2
    lda (fs_options),y                                                ; 88c1: b1 bb       ..
    sta fs_cmd_data,x                                                 ; 88c3: 9d 05 0f    ...
    dey                                                               ; 88c6: 88          .
    dex                                                               ; 88c7: ca          .
    bne chalp2                                                        ; 88c8: d0 f7       ..
    ldx #&0a                                                          ; 88ca: a2 0a       ..
; &88cc referenced 2 times by &88b5, &88ea
.copy_filename_to_cmd
    jsr copy_string_to_cmd                                            ; 88cc: 20 77 8d     w.
.sub_c88cf
    ldy #&13                                                          ; 88cf: a0 13       ..
    bne c88d8                                                         ; 88d1: d0 05       ..             ; ALWAYS branch

; &88d3 referenced 1 time by &8892
.cha6
    jsr copy_filename                                                 ; 88d3: 20 75 8d     u.
    ldy #&14                                                          ; 88d6: a0 14       ..
; &88d8 referenced 1 time by &88d1
.c88d8
    bit l83af                                                         ; 88d8: 2c af 83    ,..
    jsr init_tx_ctrl_data                                             ; 88db: 20 c4 83     ..
; &88de referenced 1 time by &8894
.c88de
    bcs c8922                                                         ; 88de: b0 42       .B
    bcc c8953                                                         ; 88e0: 90 71       .q             ; ALWAYS branch

; &88e2 referenced 1 time by &889c
.cha4
    jsr decode_attribs_6bit                                           ; 88e2: 20 dd 85     ..
    sta l0f06                                                         ; 88e5: 8d 06 0f    ...
    ldx #2                                                            ; 88e8: a2 02       ..
    bne copy_filename_to_cmd                                          ; 88ea: d0 e0       ..             ; ALWAYS branch

; &88ec referenced 1 time by &8898
.cha5
    ldx #1                                                            ; 88ec: a2 01       ..
    jsr copy_string_to_cmd                                            ; 88ee: 20 77 8d     w.
    ldy #&12                                                          ; 88f1: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 88f3: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    lda l0f11                                                         ; 88f6: ad 11 0f    ...
    stx l0f11                                                         ; 88f9: 8e 11 0f    ...            ; X=0 on success, &D6 on not-found
    stx l0f14                                                         ; 88fc: 8e 14 0f    ...
    jsr decode_attribs_5bit                                           ; 88ff: 20 e7 85     ..
    ldy #&0e                                                          ; 8902: a0 0e       ..
    sta (fs_options),y                                                ; 8904: 91 bb       ..
    dey                                                               ; 8906: 88          .              ; Y=&0d
    ldx #&0c                                                          ; 8907: a2 0c       ..
; &8909 referenced 1 time by &8910
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 8909: bd 05 0f    ...
    sta (fs_options),y                                                ; 890c: 91 bb       ..
    dey                                                               ; 890e: 88          .
    dex                                                               ; 890f: ca          .
    bne copy_fs_reply_to_cb                                           ; 8910: d0 f7       ..
    inx                                                               ; 8912: e8          .
    inx                                                               ; 8913: e8          .
    ldy #&11                                                          ; 8914: a0 11       ..
; &8916 referenced 1 time by &891d
.cha5lp
    lda l0f12,x                                                       ; 8916: bd 12 0f    ...
    sta (fs_options),y                                                ; 8919: 91 bb       ..
    dey                                                               ; 891b: 88          .
    dex                                                               ; 891c: ca          .
    bpl cha5lp                                                        ; 891d: 10 f7       ..
    lda fs_cmd_data                                                   ; 891f: ad 05 0f    ...
; &8922 referenced 1 time by &88de
.c8922
    bpl c8971                                                         ; 8922: 10 4d       .M
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
    jsr save_fscv_args                                                ; 8924: 20 d2 85     ..
    cmp #3                                                            ; 8927: c9 03       ..
    bcs restore_args_return                                           ; 8929: b0 44       .D
    cpy #0                                                            ; 892b: c0 00       ..
    beq c8976                                                         ; 892d: f0 47       .G
    jsr handle_to_mask_clc                                            ; 892f: 20 44 86     D.
    sty fs_cmd_data                                                   ; 8932: 8c 05 0f    ...
    lsr a                                                             ; 8935: 4a          J
    sta l0f06                                                         ; 8936: 8d 06 0f    ...
    bcs save_args_handle                                              ; 8939: b0 1a       ..
    ldy #&0c                                                          ; 893b: a0 0c       ..             ; Y=function code for HDRFN
    ldx #2                                                            ; 893d: a2 02       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 893f: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 8942: 85 bd       ..             ; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 8944: a6 bb       ..
    ldy #2                                                            ; 8946: a0 02       ..
    sta l0003,x                                                       ; 8948: 95 03       ..
; &894a referenced 1 time by &8951
.loop_c894a
    lda fs_cmd_data,y                                                 ; 894a: b9 05 0f    ...
    sta l0002,x                                                       ; 894d: 95 02       ..
    dex                                                               ; 894f: ca          .
    dey                                                               ; 8950: 88          .
    bpl loop_c894a                                                    ; 8951: 10 f7       ..
; &8953 referenced 1 time by &88e0
.c8953
    bcc restore_args_return                                           ; 8953: 90 1a       ..
; &8955 referenced 1 time by &8939
.save_args_handle
    tya                                                               ; 8955: 98          .
    pha                                                               ; 8956: 48          H
    ldy #3                                                            ; 8957: a0 03       ..
; &8959 referenced 1 time by &8960
.loop_c8959
    lda l0003,x                                                       ; 8959: b5 03       ..
    sta l0f07,y                                                       ; 895b: 99 07 0f    ...
    dex                                                               ; 895e: ca          .
    dey                                                               ; 895f: 88          .
    bpl loop_c8959                                                    ; 8960: 10 f7       ..
    ldy #&0d                                                          ; 8962: a0 0d       ..             ; Y=function code for HDRFN
    ldx #5                                                            ; 8964: a2 05       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8966: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
.sub_c8969
    stx fs_last_byte_flag                                             ; 8969: 86 bd       ..             ; X=0 on success, &D6 on not-found
    pla                                                               ; 896b: 68          h
    jsr sub_c8679                                                     ; 896c: 20 79 86     y.
; ***************************************************************************************
; Restore arguments and return
; 
; Common exit point for FS vector handlers. Reloads A from
; fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
; fs_block_offset (&BC) — the values saved at entry by
; save_fscv_args — and returns to the caller.
; ***************************************************************************************
; &896f referenced 7 times by &8713, &87ed, &8929, &8953, &89e6, &8a39, &8e27
.restore_args_return
    lda fs_last_byte_flag                                             ; 896f: a5 bd       ..
; &8971 referenced 5 times by &8922, &8982, &8992, &89bd, &89ca
.c8971
    ldx fs_options                                                    ; 8971: a6 bb       ..
    ldy fs_block_offset                                               ; 8973: a4 bc       ..
    rts                                                               ; 8975: 60          `

; &8976 referenced 1 time by &892d
.c8976
    cmp #2                                                            ; 8976: c9 02       ..
    beq c8981                                                         ; 8978: f0 07       ..
    bcs c8990                                                         ; 897a: b0 14       ..
    tay                                                               ; 897c: a8          .
    bne osarg1                                                        ; 897d: d0 05       ..
    lda #&0a                                                          ; 897f: a9 0a       ..
; &8981 referenced 1 time by &8978
.c8981
    lsr a                                                             ; 8981: 4a          J
    bne c8971                                                         ; 8982: d0 ed       ..
; &8984 referenced 2 times by &897d, &898a
.osarg1
    lda fs_cmd_context,y                                              ; 8984: b9 0a 0e    ...
    sta (fs_options),y                                                ; 8987: 91 bb       ..
    dey                                                               ; 8989: 88          .
    bpl osarg1                                                        ; 898a: 10 f8       ..
    sty l0002,x                                                       ; 898c: 94 02       ..
    sty l0003,x                                                       ; 898e: 94 03       ..
; &8990 referenced 4 times by &897a, &89a0, &8ad5, &8b77
.c8990
    lda #0                                                            ; 8990: a9 00       ..             ; A=operation (0=close, &40=read, &80=write, &C0=R/W)
    bpl c8971                                                         ; 8992: 10 dd       ..             ; ALWAYS branch

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
    jsr save_fscv_args_with_ptrs                                      ; 8994: 20 c8 85     ..
    sec                                                               ; 8997: 38          8
    jsr handle_to_mask                                                ; 8998: 20 45 86     E.            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 899b: aa          .              ; A=preserved
    beq close_handle                                                  ; 899c: f0 2e       ..
    and #&3f ; '?'                                                    ; 899e: 29 3f       )?
    bne c8990                                                         ; 89a0: d0 ee       ..
    txa                                                               ; 89a2: 8a          .
    eor #&80                                                          ; 89a3: 49 80       I.
    asl a                                                             ; 89a5: 0a          .
    sta fs_cmd_data                                                   ; 89a6: 8d 05 0f    ...
    rol a                                                             ; 89a9: 2a          *
    sta l0f06                                                         ; 89aa: 8d 06 0f    ...
    jsr parse_filename_gs                                             ; 89ad: 20 e1 86     ..
    ldx #2                                                            ; 89b0: a2 02       ..
    jsr copy_string_to_cmd                                            ; 89b2: 20 77 8d     w.
    ldy #6                                                            ; 89b5: a0 06       ..
    bit l83af                                                         ; 89b7: 2c af 83    ,..
    jsr init_tx_ctrl_data                                             ; 89ba: 20 c4 83     ..
    bcs c8971                                                         ; 89bd: b0 b2       ..
    lda fs_cmd_data                                                   ; 89bf: ad 05 0f    ...
    tax                                                               ; 89c2: aa          .
    jsr sub_c8679                                                     ; 89c3: 20 79 86     y.
; 3.35K fix: OR handle bit into fs_sequence_nos
; (&0E08). Without this, a newly opened file could
; inherit a stale sequence number from a previous
; file using the same handle, causing byte-stream
; protocol errors.
    txa                                                               ; 89c6: 8a          .              ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 89c7: 20 60 86     `.            ; Convert bitmask to handle number (FS2A)
    bne c8971                                                         ; 89ca: d0 a5       ..
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
; &89cc referenced 1 time by &899c
.close_handle
    tya                                                               ; 89cc: 98          .              ; Y=preserved
    bne close_single_handle                                           ; 89cd: d0 07       ..
    lda #osbyte_close_spool_exec                                      ; 89cf: a9 77       .w
    jsr osbyte                                                        ; 89d1: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 89d4: a0 00       ..
; &89d6 referenced 1 time by &89cd
.close_single_handle
    sty fs_cmd_data                                                   ; 89d6: 8c 05 0f    ...
    ldx #1                                                            ; 89d9: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 89db: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89dd: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 89e0: ad 05 0f    ...
    jsr sub_c8679                                                     ; 89e3: 20 79 86     y.
; &89e6 referenced 1 time by &8a0c
.c89e6
    bcc restore_args_return                                           ; 89e6: 90 87       ..
    beq c89f5                                                         ; 89e8: f0 0b       ..
; ***************************************************************************************
; FSCV 0: *OPT handler (OPTION)
; 
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
; Other combinations generate error &CB (OPTER: "bad option").
; ***************************************************************************************
.opt_handler
    cpx #4                                                            ; 89ea: e0 04       ..
    bne c89f2                                                         ; 89ec: d0 04       ..
    cpy #4                                                            ; 89ee: c0 04       ..
    bcc optl1                                                         ; 89f0: 90 0d       ..
; &89f2 referenced 1 time by &89ec
.c89f2
    dex                                                               ; 89f2: ca          .
    bne opter1                                                        ; 89f3: d0 05       ..
; &89f5 referenced 1 time by &89e8
.c89f5
    sty fs_messages_flag                                              ; 89f5: 8c 06 0e    ...
    bcc c8a0c                                                         ; 89f8: 90 12       ..
; &89fa referenced 1 time by &89f3
.opter1
    lda #7                                                            ; 89fa: a9 07       ..
    jmp nlisne                                                        ; 89fc: 4c fd 84    L..

; &89ff referenced 1 time by &89f0
.optl1
    sty fs_cmd_data                                                   ; 89ff: 8c 05 0f    ...
    ldy #&16                                                          ; 8a02: a0 16       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8a04: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 8a07: a4 bc       ..
    sty fs_boot_option                                                ; 8a09: 8c 05 0e    ...
; &8a0c referenced 1 time by &89f8
.c8a0c
    bcc c89e6                                                         ; 8a0c: 90 d8       ..
; &8a0e referenced 1 time by &8ac9
.adjust_addrs_9
    ldy #9                                                            ; 8a0e: a0 09       ..
    jsr adjust_addrs_clc                                              ; 8a10: 20 15 8a     ..
; &8a13 referenced 1 time by &8bbe
.adjust_addrs_1
    ldy #1                                                            ; 8a13: a0 01       ..
; &8a15 referenced 1 time by &8a10
.adjust_addrs_clc
    clc                                                               ; 8a15: 18          .
; ***************************************************************************************
; Bidirectional 4-byte address adjustment
; 
; Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
;   If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
;   If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
; Starting offset X=&FC means it reads from &0E06-&0E09 area.
; Used to convert between absolute and relative file positions.
; ***************************************************************************************
; &8a16 referenced 2 times by &8acf, &8bca
.adjust_addrs
    ldx #&fc                                                          ; 8a16: a2 fc       ..
; &8a18 referenced 1 time by &8a2b
.loop_c8a18
    lda (fs_options),y                                                ; 8a18: b1 bb       ..
    bit fs_load_addr_2                                                ; 8a1a: 24 b2       $.
    bmi c8a24                                                         ; 8a1c: 30 06       0.
    adc fs_cmd_context,x                                              ; 8a1e: 7d 0a 0e    }..
    jmp gbpbx                                                         ; 8a21: 4c 27 8a    L'.

; &8a24 referenced 1 time by &8a1c
.c8a24
    sbc fs_cmd_context,x                                              ; 8a24: fd 0a 0e    ...
; &8a27 referenced 1 time by &8a21
.gbpbx
    sta (fs_options),y                                                ; 8a27: 91 bb       ..
    iny                                                               ; 8a29: c8          .
    inx                                                               ; 8a2a: e8          .
    bne loop_c8a18                                                    ; 8a2b: d0 eb       ..
    rts                                                               ; 8a2d: 60          `

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
    jsr save_fscv_args                                                ; 8a2e: 20 d2 85     ..
    tax                                                               ; 8a31: aa          .
    beq c8a39                                                         ; 8a32: f0 05       ..
    dex                                                               ; 8a34: ca          .
    cpx #8                                                            ; 8a35: e0 08       ..
    bcc gbpbx1                                                        ; 8a37: 90 03       ..
; &8a39 referenced 1 time by &8a32
.c8a39
    jmp restore_args_return                                           ; 8a39: 4c 6f 89    Lo.

; &8a3c referenced 1 time by &8a37
.gbpbx1
    txa                                                               ; 8a3c: 8a          .
    ldy #0                                                            ; 8a3d: a0 00       ..
    pha                                                               ; 8a3f: 48          H
    cmp #4                                                            ; 8a40: c9 04       ..
    bcc gbpbe1                                                        ; 8a42: 90 03       ..
    jmp osgbpb_info                                                   ; 8a44: 4c ed 8a    L..

; &8a47 referenced 1 time by &8a42
.gbpbe1
    lda (fs_options),y                                                ; 8a47: b1 bb       ..
    jsr handle_to_mask_a                                              ; 8a49: 20 43 86     C.
    sty fs_cmd_data                                                   ; 8a4c: 8c 05 0f    ...
    ldy #&0b                                                          ; 8a4f: a0 0b       ..
    ldx #6                                                            ; 8a51: a2 06       ..
; &8a53 referenced 1 time by &8a5f
.gbpbf1
    lda (fs_options),y                                                ; 8a53: b1 bb       ..
    sta l0f06,x                                                       ; 8a55: 9d 06 0f    ...
    dey                                                               ; 8a58: 88          .
    cpy #8                                                            ; 8a59: c0 08       ..
    bne gbpbx0                                                        ; 8a5b: d0 01       ..
    dey                                                               ; 8a5d: 88          .
; &8a5e referenced 1 time by &8a5b
.gbpbx0
.gbpbf2
    dex                                                               ; 8a5e: ca          .
    bne gbpbf1                                                        ; 8a5f: d0 f2       ..
    pla                                                               ; 8a61: 68          h
    lsr a                                                             ; 8a62: 4a          J
    pha                                                               ; 8a63: 48          H
    bcc gbpbl1                                                        ; 8a64: 90 01       ..
    inx                                                               ; 8a66: e8          .
; &8a67 referenced 1 time by &8a64
.gbpbl1
    stx l0f06                                                         ; 8a67: 8e 06 0f    ...
    ldy #&0b                                                          ; 8a6a: a0 0b       ..
    ldx #&91                                                          ; 8a6c: a2 91       ..
    pla                                                               ; 8a6e: 68          h
    pha                                                               ; 8a6f: 48          H
    beq c8a75                                                         ; 8a70: f0 03       ..
    ldx #&92                                                          ; 8a72: a2 92       ..
    dey                                                               ; 8a74: 88          .              ; Y=&0a
; &8a75 referenced 1 time by &8a70
.c8a75
    stx fs_cmd_urd                                                    ; 8a75: 8e 02 0f    ...
    stx fs_error_ptr                                                  ; 8a78: 86 b8       ..
    ldx #8                                                            ; 8a7a: a2 08       ..
    lda fs_cmd_data                                                   ; 8a7c: ad 05 0f    ...
    jsr prepare_cmd_with_flag                                         ; 8a7f: 20 b5 83     ..
    lda l00b3                                                         ; 8a82: a5 b3       ..
    sta fs_sequence_nos                                               ; 8a84: 8d 08 0e    ...
    ldx #4                                                            ; 8a87: a2 04       ..
; &8a89 referenced 1 time by &8a9d
.gbpbl3
    lda (fs_options),y                                                ; 8a89: b1 bb       ..
    sta l00af,y                                                       ; 8a8b: 99 af 00    ...
    sta l00c7,y                                                       ; 8a8e: 99 c7 00    ...
    jsr add_4_to_y                                                    ; 8a91: 20 fd 87     ..
    adc (fs_options),y                                                ; 8a94: 71 bb       q.
    sta l00af,y                                                       ; 8a96: 99 af 00    ...
    jsr sub_3_from_y                                                  ; 8a99: 20 10 88     ..
    dex                                                               ; 8a9c: ca          .
    bne gbpbl3                                                        ; 8a9d: d0 ea       ..
    inx                                                               ; 8a9f: e8          .
; &8aa0 referenced 1 time by &8aa7
.gbpbf3
    lda fs_cmd_csd,x                                                  ; 8aa0: bd 03 0f    ...
    sta l0f06,x                                                       ; 8aa3: 9d 06 0f    ...
    dex                                                               ; 8aa6: ca          .
    bpl gbpbf3                                                        ; 8aa7: 10 f7       ..
    pla                                                               ; 8aa9: 68          h
    bne c8ab4                                                         ; 8aaa: d0 08       ..
    lda fs_cmd_urd                                                    ; 8aac: ad 02 0f    ...
    jsr transfer_file_blocks                                          ; 8aaf: 20 14 88     ..
    bcs c8ab7                                                         ; 8ab2: b0 03       ..
; &8ab4 referenced 1 time by &8aaa
.c8ab4
    jsr send_data_blocks                                              ; 8ab4: 20 5f 87     _.
; &8ab7 referenced 1 time by &8ab2
.c8ab7
    jsr send_fs_reply_cmd                                             ; 8ab7: 20 ef 83     ..
    lda (fs_options,x)                                                ; 8aba: a1 bb       ..
    bit fs_cmd_data                                                   ; 8abc: 2c 05 0f    ,..
    bmi c8ac4                                                         ; 8abf: 30 03       0.
    jsr clear_fs_flag                                                 ; 8ac1: 20 7e 86     ~.
; &8ac4 referenced 1 time by &8abf
.c8ac4
    jsr sub_c8679                                                     ; 8ac4: 20 79 86     y.
    stx fs_load_addr_2                                                ; 8ac7: 86 b2       ..
    jsr adjust_addrs_9                                                ; 8ac9: 20 0e 8a     ..
    dec fs_load_addr_2                                                ; 8acc: c6 b2       ..
    sec                                                               ; 8ace: 38          8
    jsr adjust_addrs                                                  ; 8acf: 20 16 8a     ..
    asl fs_cmd_data                                                   ; 8ad2: 0e 05 0f    ...
    jmp c8990                                                         ; 8ad5: 4c 90 89    L..

; &8ad8 referenced 1 time by &8b08
.c8ad8
    ldy #&15                                                          ; 8ad8: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8ada: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8add: ad 05 0e    ...
    sta l0f16                                                         ; 8ae0: 8d 16 0f    ...
    stx fs_load_addr                                                  ; 8ae3: 86 b0       ..             ; X=0 on success, &D6 on not-found
    stx fs_load_addr_hi                                               ; 8ae5: 86 b1       ..
    lda #&12                                                          ; 8ae7: a9 12       ..
    sta fs_load_addr_2                                                ; 8ae9: 85 b2       ..
    bne copy_reply_to_caller                                          ; 8aeb: d0 4e       .N             ; ALWAYS branch

; ***************************************************************************************
; OSGBPB 5-8 info handler (OSINFO)
; 
; Handles the "messy interface tacked onto OSGBPB" (original source).
; Checks whether the destination address is in Tube space by comparing
; the high bytes against TBFLAG. If in Tube space, data must be
; copied via the Tube FIFO registers (with delays to accommodate the
; slow 16032 co-processor) instead of direct memory access.
; ***************************************************************************************
; &8aed referenced 1 time by &8a44
.osgbpb_info
    ldy #4                                                            ; 8aed: a0 04       ..
    lda tube_flag                                                     ; 8aef: ad 67 0d    .g.
    beq c8afb                                                         ; 8af2: f0 07       ..
    cmp (fs_options),y                                                ; 8af4: d1 bb       ..
    bne c8afb                                                         ; 8af6: d0 03       ..
    dey                                                               ; 8af8: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8af9: f1 bb       ..
; &8afb referenced 2 times by &8af2, &8af6
.c8afb
    sta l00a9                                                         ; 8afb: 85 a9       ..
; &8afd referenced 1 time by &8b03
.info2
    lda (fs_options),y                                                ; 8afd: b1 bb       ..
    sta fs_last_byte_flag,y                                           ; 8aff: 99 bd 00    ...
    dey                                                               ; 8b02: 88          .
    bne info2                                                         ; 8b03: d0 f8       ..
    pla                                                               ; 8b05: 68          h
    and #3                                                            ; 8b06: 29 03       ).
    beq c8ad8                                                         ; 8b08: f0 ce       ..
    lsr a                                                             ; 8b0a: 4a          J
    beq c8b0f                                                         ; 8b0b: f0 02       ..
    bcs c8b7a                                                         ; 8b0d: b0 6b       .k
; &8b0f referenced 1 time by &8b0b
.c8b0f
    tay                                                               ; 8b0f: a8          .              ; Y=function code
    lda fs_csd_handle,y                                               ; 8b10: b9 03 0e    ...
    sta fs_cmd_csd                                                    ; 8b13: 8d 03 0f    ...
    lda fs_lib_handle                                                 ; 8b16: ad 04 0e    ...
    sta fs_cmd_lib                                                    ; 8b19: 8d 04 0f    ...
    lda fs_urd_handle                                                 ; 8b1c: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 8b1f: 8d 02 0f    ...
    ldx #&12                                                          ; 8b22: a2 12       ..             ; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8b24: 8e 01 0f    ...
    lda #&0d                                                          ; 8b27: a9 0d       ..
    sta l0f06                                                         ; 8b29: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8b2c: 85 b2       ..
    lsr a                                                             ; 8b2e: 4a          J              ; A=timeout period for FS reply
    sta fs_cmd_data                                                   ; 8b2f: 8d 05 0f    ...
    clc                                                               ; 8b32: 18          .
    jsr build_send_fs_cmd                                             ; 8b33: 20 d9 83     ..            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8b36: 86 b1       ..             ; X=0 on success, &D6 on not-found
    inx                                                               ; 8b38: e8          .
    stx fs_load_addr                                                  ; 8b39: 86 b0       ..
; &8b3b referenced 2 times by &8aeb, &8bb3
.copy_reply_to_caller
    lda l00a9                                                         ; 8b3b: a5 a9       ..
    bne c8b50                                                         ; 8b3d: d0 11       ..
    ldx fs_load_addr                                                  ; 8b3f: a6 b0       ..
    ldy fs_load_addr_hi                                               ; 8b41: a4 b1       ..
; &8b43 referenced 1 time by &8b4c
.loop_c8b43
    lda fs_cmd_data,x                                                 ; 8b43: bd 05 0f    ...
    sta (fs_crc_lo),y                                                 ; 8b46: 91 be       ..
    inx                                                               ; 8b48: e8          .
    iny                                                               ; 8b49: c8          .
    dec fs_load_addr_2                                                ; 8b4a: c6 b2       ..
    bne loop_c8b43                                                    ; 8b4c: d0 f5       ..
    beq c8b77                                                         ; 8b4e: f0 27       .'             ; ALWAYS branch

; &8b50 referenced 1 time by &8b3d
.c8b50
    jsr tube_claim_loop                                               ; 8b50: 20 cf 8b     ..
    lda #1                                                            ; 8b53: a9 01       ..
    ldx fs_options                                                    ; 8b55: a6 bb       ..
    ldy fs_block_offset                                               ; 8b57: a4 bc       ..
    inx                                                               ; 8b59: e8          .
    bne c8b5d                                                         ; 8b5a: d0 01       ..
    iny                                                               ; 8b5c: c8          .
; &8b5d referenced 1 time by &8b5a
.c8b5d
    jsr tube_addr_claim                                               ; 8b5d: 20 06 04     ..
    ldx fs_load_addr                                                  ; 8b60: a6 b0       ..
; &8b62 referenced 1 time by &8b70
.tbcop1
    lda fs_cmd_data,x                                                 ; 8b62: bd 05 0f    ...
    sta tube_data_register_3                                          ; 8b65: 8d e5 fe    ...
    inx                                                               ; 8b68: e8          .
    ldy #6                                                            ; 8b69: a0 06       ..
; &8b6b referenced 1 time by &8b6c
.loop_c8b6b
    dey                                                               ; 8b6b: 88          .
    bne loop_c8b6b                                                    ; 8b6c: d0 fd       ..
    dec fs_load_addr_2                                                ; 8b6e: c6 b2       ..
    bne tbcop1                                                        ; 8b70: d0 f0       ..
    lda #&83                                                          ; 8b72: a9 83       ..
    jsr tube_addr_claim                                               ; 8b74: 20 06 04     ..
; &8b77 referenced 2 times by &8b4e, &8bcd
.c8b77
    jmp c8990                                                         ; 8b77: 4c 90 89    L..

; &8b7a referenced 1 time by &8b0d
.c8b7a
    ldy #9                                                            ; 8b7a: a0 09       ..
    lda (fs_options),y                                                ; 8b7c: b1 bb       ..
    sta l0f06                                                         ; 8b7e: 8d 06 0f    ...
    ldy #5                                                            ; 8b81: a0 05       ..
    lda (fs_options),y                                                ; 8b83: b1 bb       ..
    sta l0f07                                                         ; 8b85: 8d 07 0f    ...
    ldx #&0d                                                          ; 8b88: a2 0d       ..             ; X=preserved through header build
    stx l0f08                                                         ; 8b8a: 8e 08 0f    ...
    ldy #2                                                            ; 8b8d: a0 02       ..
    sty fs_load_addr                                                  ; 8b8f: 84 b0       ..
    sty fs_cmd_data                                                   ; 8b91: 8c 05 0f    ...
    iny                                                               ; 8b94: c8          .              ; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8b95: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8b98: 86 b1       ..             ; X=0 on success, &D6 on not-found
    lda l0f06                                                         ; 8b9a: ad 06 0f    ...
    sta (fs_options,x)                                                ; 8b9d: 81 bb       ..
    lda fs_cmd_data                                                   ; 8b9f: ad 05 0f    ...
    ldy #9                                                            ; 8ba2: a0 09       ..
    adc (fs_options),y                                                ; 8ba4: 71 bb       q.
    sta (fs_options),y                                                ; 8ba6: 91 bb       ..
    lda l00c8                                                         ; 8ba8: a5 c8       ..
    sbc #7                                                            ; 8baa: e9 07       ..
    sta l0f06                                                         ; 8bac: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8baf: 85 b2       ..
    beq c8bb6                                                         ; 8bb1: f0 03       ..
    jsr copy_reply_to_caller                                          ; 8bb3: 20 3b 8b     ;.
; &8bb6 referenced 1 time by &8bb1
.c8bb6
    ldx #2                                                            ; 8bb6: a2 02       ..
; &8bb8 referenced 1 time by &8bbc
.loop_c8bb8
    sta l0f07,x                                                       ; 8bb8: 9d 07 0f    ...
    dex                                                               ; 8bbb: ca          .
    bpl loop_c8bb8                                                    ; 8bbc: 10 fa       ..
    jsr adjust_addrs_1                                                ; 8bbe: 20 13 8a     ..
    sec                                                               ; 8bc1: 38          8
    dec fs_load_addr_2                                                ; 8bc2: c6 b2       ..
    lda fs_cmd_data                                                   ; 8bc4: ad 05 0f    ...
    sta l0f06                                                         ; 8bc7: 8d 06 0f    ...
    jsr adjust_addrs                                                  ; 8bca: 20 16 8a     ..
    beq c8b77                                                         ; 8bcd: f0 a8       ..
; &8bcf referenced 3 times by &8b50, &8bd4, &8e10
.tube_claim_loop
    lda #&c3                                                          ; 8bcf: a9 c3       ..
    jsr tube_addr_claim                                               ; 8bd1: 20 06 04     ..
    bcc tube_claim_loop                                               ; 8bd4: 90 f9       ..
    rts                                                               ; 8bd6: 60          `

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
; &8bd7 referenced 1 time by &828b
.fscv_star_handler
    jsr save_fscv_args_with_ptrs                                      ; 8bd7: 20 c8 85     ..
    ldx #&ff                                                          ; 8bda: a2 ff       ..
    stx l00b9                                                         ; 8bdc: 86 b9       ..
; &8bde referenced 1 time by &8bf9
.loop_c8bde
    ldy #&ff                                                          ; 8bde: a0 ff       ..
; &8be0 referenced 1 time by &8beb
.decfir
    iny                                                               ; 8be0: c8          .
    inx                                                               ; 8be1: e8          .
; &8be2 referenced 1 time by &8bfd
.decmor
    lda fs_cmd_match_table,x                                          ; 8be2: bd 05 8c    ...
    bmi c8bff                                                         ; 8be5: 30 18       0.
    eor (fs_crc_lo),y                                                 ; 8be7: 51 be       Q.
    and #&df                                                          ; 8be9: 29 df       ).
    beq decfir                                                        ; 8beb: f0 f3       ..
    dex                                                               ; 8bed: ca          .
; &8bee referenced 1 time by &8bf2
.decmin
    inx                                                               ; 8bee: e8          .
    lda fs_cmd_match_table,x                                          ; 8bef: bd 05 8c    ...
    bpl decmin                                                        ; 8bf2: 10 fa       ..
    lda (fs_crc_lo),y                                                 ; 8bf4: b1 be       ..
    inx                                                               ; 8bf6: e8          .
    cmp #&2e ; '.'                                                    ; 8bf7: c9 2e       ..
    bne loop_c8bde                                                    ; 8bf9: d0 e3       ..
    iny                                                               ; 8bfb: c8          .
    dex                                                               ; 8bfc: ca          .
    bcs decmor                                                        ; 8bfd: b0 e3       ..
; &8bff referenced 1 time by &8be5
.c8bff
    pha                                                               ; 8bff: 48          H
    lda l8c06,x                                                       ; 8c00: bd 06 8c    ...
    pha                                                               ; 8c03: 48          H
    rts                                                               ; 8c04: 60          `

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
; &8c05 referenced 2 times by &8be2, &8bef
.fs_cmd_match_table
l8c06 = fs_cmd_match_table+1
    eor #&2e ; '.'                                                    ; 8c05: 49 2e       I.
; &8c06 referenced 1 time by &8c00
    equb &80, &c0                                                     ; 8c07: 80 c0       ..
    equs "I AM"                                                       ; 8c09: 49 20 41... I A
    equb &80, &81, &45, &58, &8c, &1a                                 ; 8c0d: 80 81 45... ..E
    equs "BYE"                                                        ; 8c13: 42 59 45    BYE
    equb &0d, &83, &bb, &80, &c0, &a2, 1, &a9, 3, &d0, 8              ; 8c16: 0d 83 bb... ...

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
    ldx #3                                                            ; 8c21: a2 03       ..
    stx l00b9                                                         ; 8c23: 86 b9       ..
    ldy #0                                                            ; 8c25: a0 00       ..
    lda #&0b                                                          ; 8c27: a9 0b       ..
    sta l00b5                                                         ; 8c29: 85 b5       ..
    stx l00b7                                                         ; 8c2b: 86 b7       ..
    lda #6                                                            ; 8c2d: a9 06       ..
    sta fs_cmd_data                                                   ; 8c2f: 8d 05 0f    ...
    jsr sub_c86e3                                                     ; 8c32: 20 e3 86     ..
    ldx #1                                                            ; 8c35: a2 01       ..
    jsr copy_string_to_cmd                                            ; 8c37: 20 77 8d     w.
    ldy #&12                                                          ; 8c3a: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c3c: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c3f: a2 03       ..
    jsr l8cfb                                                         ; 8c41: 20 fb 8c     ..
    jsr print_inline                                                  ; 8c44: 20 05 86     ..
    equs "("                                                          ; 8c47: 28          (

    lda l0f13                                                         ; 8c48: ad 13 0f    ...
    jsr print_decimal                                                 ; 8c4b: 20 b0 8d     ..
    jsr print_inline                                                  ; 8c4e: 20 05 86     ..
    equs ")     "                                                     ; 8c51: 29 20 20... )

    ldx l0f12                                                         ; 8c57: ae 12 0f    ...
    bne c8c67                                                         ; 8c5a: d0 0b       ..
    jsr print_inline                                                  ; 8c5c: 20 05 86     ..
    equs "Owner", &0d                                                 ; 8c5f: 4f 77 6e... Own

    bne c8c71                                                         ; 8c65: d0 0a       ..
; &8c67 referenced 1 time by &8c5a
.c8c67
    jsr print_inline                                                  ; 8c67: 20 05 86     ..
    equs "Public", &0d                                                ; 8c6a: 50 75 62... Pub

; &8c71 referenced 1 time by &8c65
.c8c71
    ldy #&15                                                          ; 8c71: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c73: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8c76: e8          .
    ldy #&10                                                          ; 8c77: a0 10       ..
    jsr c8cfd                                                         ; 8c79: 20 fd 8c     ..
    jsr print_inline                                                  ; 8c7c: 20 05 86     ..
    equs "    Option "                                                ; 8c7f: 20 20 20...

    lda fs_boot_option                                                ; 8c8a: ad 05 0e    ...
    tax                                                               ; 8c8d: aa          .
    jsr sub_c9fe0                                                     ; 8c8e: 20 e0 9f     ..
    jsr print_inline                                                  ; 8c91: 20 05 86     ..
    equs " ("                                                         ; 8c94: 20 28        (

    ldy l8d08,x                                                       ; 8c96: bc 08 8d    ...
; &8c99 referenced 1 time by &8ca2
.loop_c8c99
    lda l8d08,y                                                       ; 8c99: b9 08 8d    ...
    bmi c8ca4                                                         ; 8c9c: 30 06       0.
    jsr osasci                                                        ; 8c9e: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8ca1: c8          .
    bne loop_c8c99                                                    ; 8ca2: d0 f5       ..
; &8ca4 referenced 1 time by &8c9c
.c8ca4
    jsr print_inline                                                  ; 8ca4: 20 05 86     ..
    equs ")", &0d, "Dir. "                                            ; 8ca7: 29 0d 44... ).D

    ldx #&11                                                          ; 8cae: a2 11       ..
    jsr l8cfb                                                         ; 8cb0: 20 fb 8c     ..
    jsr print_inline                                                  ; 8cb3: 20 05 86     ..
    equs "     Lib. "                                                 ; 8cb6: 20 20 20...

    ldx #&1b                                                          ; 8cc0: a2 1b       ..
    jsr l8cfb                                                         ; 8cc2: 20 fb 8c     ..
    jsr osnewl                                                        ; 8cc5: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    sty l0f06                                                         ; 8cc8: 8c 06 0f    ...
    sty l00b4                                                         ; 8ccb: 84 b4       ..
    ldx l00b5                                                         ; 8ccd: a6 b5       ..
    stx l0f07                                                         ; 8ccf: 8e 07 0f    ...
    ldx l00b7                                                         ; 8cd2: a6 b7       ..
    stx fs_cmd_data                                                   ; 8cd4: 8e 05 0f    ...
    ldx #3                                                            ; 8cd7: a2 03       ..
    jsr copy_string_to_cmd                                            ; 8cd9: 20 77 8d     w.
    ldy #3                                                            ; 8cdc: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cde: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8ce1: e8          .
    lda fs_cmd_data                                                   ; 8ce2: ad 05 0f    ...
    beq c8d55                                                         ; 8ce5: f0 6e       .n
    pha                                                               ; 8ce7: 48          H
; &8ce8 referenced 1 time by &8cec
.loop_c8ce8
    iny                                                               ; 8ce8: c8          .
    lda fs_cmd_data,y                                                 ; 8ce9: b9 05 0f    ...
    bpl loop_c8ce8                                                    ; 8cec: 10 fa       ..
    sta fs_cmd_lib,y                                                  ; 8cee: 99 04 0f    ...
    jsr sub_c8d92                                                     ; 8cf1: 20 92 8d     ..
    equb &68                                                          ; 8cf4: 68          h
    equb &18                                                          ; 8cf5: 18          .
    equb &65                                                          ; 8cf6: 65          e
    equb &b4                                                          ; 8cf7: b4          .
.l8cf8
l8cfb = l8cf8+3
    equs &a8, &d0, &cd, &a0                                           ; 8cf8: a8 d0 cd... ...
; &8cfb referenced 3 times by &8c41, &8cb0, &8cc2
    equb &0a                                                          ; 8cfc: 0a          .

; &8cfd referenced 2 times by &8c79, &8d05
.c8cfd
    lda fs_cmd_data,x                                                 ; 8cfd: bd 05 0f    ...
    jsr osasci                                                        ; 8d00: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8d03: e8          .
    dey                                                               ; 8d04: 88          .
    bne c8cfd                                                         ; 8d05: d0 f6       ..
; Option name encoding: in 3.35, the boot option names ("Off",
; "Load", "Run", "Exec") are scattered through the code rather
; than stored as a contiguous table. They are addressed via
; base+offset from return_9 (&8CE0), whose first four bytes
; (starting with the RTS opcode &60) double as the offset table:
;   &60→&8D40 "Off", &73→&8D53 "Load",
;   &9B→&8D7B "Run", &18→&8CF8 "Exec"
; Each string is terminated by the next instruction's opcode
; having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).
.return_9
    rts                                                               ; 8d07: 60          `

; &8d08 referenced 2 times by &8c96, &8c99
.l8d08
    equb &6a, &7d, &a5, &18                                           ; 8d08: 6a 7d a5... j}.
    equs "L.!"                                                        ; 8d0c: 4c 2e 21    L.!
; ***************************************************************************************
; Boot command strings for auto-boot
; 
; The four boot options use OSCLI strings at offsets within page &8C:
;   Option 0 (Off):  offset &F3 → &8CF3 = bare CR (empty command)
;   Option 1 (Load): offset &E4 → &8CE4 = "L.!BOOT" (dual-purpose:
;       the bytes &4C='L', &2E='.', &21='!' at &8CE4 are followed
;       by "BOOT" at &8CE7, forming the OSCLI string "L.!BOOT")
;   Option 2 (Run):  offset &E6 → &8CE6 = "!BOOT" (bare filename = *RUN)
;   Option 3 (Exec): offset &EC → &8CEC = "E.!BOOT"
; 
; This is a classic BBC ROM space optimisation: the string data
; overlaps with other byte sequences to save space.
; ***************************************************************************************
.boot_cmd_strings
    equs "BOOT"                                                       ; 8d0f: 42 4f 4f... BOO
    equb &0d                                                          ; 8d13: 0d          .
    equs "E.!BOOT"                                                    ; 8d14: 45 2e 21... E.!
    equb &0d                                                          ; 8d1b: 0d          .
; &8d1c referenced 1 time by &8e3d
.l8d1c
    equb &1b, &0c, &0e, &14, &45                                      ; 8d1c: 1b 0c 0e... ...

.sub_c8d21
    sei                                                               ; 8d21: 78          x
    adc l0063                                                         ; 8d22: 65 63       ec
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
; &8d24 referenced 2 times by &874c, &87ca
.print_file_info
    ldy fs_messages_flag                                              ; 8d24: ac 06 0e    ...
    beq return_5                                                      ; 8d27: f0 5b       .[
    equb &a0                                                          ; 8d29: a0          .

.sub_c8d2a
    brk                                                               ; 8d2a: 00          .

    ldx fs_cmd_csd                                                    ; 8d2b: ae 03 0f    ...
    beq c8d35                                                         ; 8d2e: f0 05       ..
    jsr print_dir_from_offset                                         ; 8d30: 20 8b 8d     ..
    bmi c8d4d                                                         ; 8d33: 30 18       0.
; &8d35 referenced 2 times by &8d2e, &8d43
.c8d35
    lda (fs_crc_lo),y                                                 ; 8d35: b1 be       ..
    cmp #&0d                                                          ; 8d37: c9 0d       ..
    beq pad_filename_spaces                                           ; 8d39: f0 0a       ..
    cmp #&20 ; ' '                                                    ; 8d3b: c9 20       .
    beq pad_filename_spaces                                           ; 8d3d: f0 06       ..
    jsr osasci                                                        ; 8d3f: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8d42: c8          .
    bne c8d35                                                         ; 8d43: d0 f0       ..
; &8d45 referenced 3 times by &8d39, &8d3d, &8d4b
.pad_filename_spaces
    jsr print_space                                                   ; 8d45: 20 6e 8d     n.
    iny                                                               ; 8d48: c8          .
    cpy #&0c                                                          ; 8d49: c0 0c       ..
    bcc pad_filename_spaces                                           ; 8d4b: 90 f8       ..
; &8d4d referenced 1 time by &8d33
.c8d4d
    ldy #5                                                            ; 8d4d: a0 05       ..
    jsr print_hex_bytes                                               ; 8d4f: 20 63 8d     c.
    jsr print_exec_and_len                                            ; 8d52: 20 58 8d     X.
; &8d55 referenced 1 time by &8ce5
.c8d55
    jmp osnewl                                                        ; 8d55: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &8d58 referenced 1 time by &8d52
.print_exec_and_len
    ldy #9                                                            ; 8d58: a0 09       ..
    jsr print_hex_bytes                                               ; 8d5a: 20 63 8d     c.
    ldy #&0c                                                          ; 8d5d: a0 0c       ..
    ldx #3                                                            ; 8d5f: a2 03       ..
    bne num01                                                         ; 8d61: d0 02       ..             ; ALWAYS branch

; &8d63 referenced 2 times by &8d4f, &8d5a
.print_hex_bytes
    ldx #4                                                            ; 8d63: a2 04       ..
; &8d65 referenced 2 times by &8d61, &8d6c
.num01
    lda (fs_options),y                                                ; 8d65: b1 bb       ..
    jsr sub_c9fe0                                                     ; 8d67: 20 e0 9f     ..
    dey                                                               ; 8d6a: 88          .
    dex                                                               ; 8d6b: ca          .
    bne num01                                                         ; 8d6c: d0 f7       ..
; &8d6e referenced 1 time by &8d45
.print_space
    lda #&20 ; ' '                                                    ; 8d6e: a9 20       .
    bne c8dcc                                                         ; 8d70: d0 5a       .Z             ; ALWAYS branch

    equs "Off"                                                        ; 8d72: 4f 66 66    Off

; ***************************************************************************************
; Copy filename to FS command buffer
; 
; Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; ***************************************************************************************
; &8d75 referenced 5 times by &809d, &80c1, &8716, &88d3, &8dd2
.copy_filename
    ldx #0                                                            ; 8d75: a2 00       ..
; ***************************************************************************************
; Copy string to FS command buffer
; 
; Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
; to &0F05+X, stopping when a CR (&0D) is encountered. The CR
; itself is also copied. Returns with X pointing past the last
; byte written.
; ***************************************************************************************
; &8d77 referenced 6 times by &87c2, &88cc, &88ee, &89b2, &8c37, &8cd9
.copy_string_to_cmd
    ldy #0                                                            ; 8d77: a0 00       ..
; &8d79 referenced 1 time by &8d82
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d79: b1 be       ..
    sta fs_cmd_data,x                                                 ; 8d7b: 9d 05 0f    ...
    inx                                                               ; 8d7e: e8          .
    iny                                                               ; 8d7f: c8          .
    eor #&0d                                                          ; 8d80: 49 0d       I.
    bne copy_string_from_offset                                       ; 8d82: d0 f5       ..
; &8d84 referenced 2 times by &8d27, &8d8e
.return_5
    rts                                                               ; 8d84: 60          `

    equs "Load"                                                       ; 8d85: 4c 6f 61... Loa

; ***************************************************************************************
; Print directory name from reply buffer
; 
; Prints characters from the FS reply buffer (&0F05+X onwards).
; Null bytes (&00) are replaced with CR (&0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by cat_handler to display Dir. and Lib. paths.
; ***************************************************************************************
.print_dir_name
    ldx #0                                                            ; 8d89: a2 00       ..
; &8d8b referenced 2 times by &8d30, &8dab
.print_dir_from_offset
    lda fs_cmd_data,x                                                 ; 8d8b: bd 05 0f    ...
    bmi return_5                                                      ; 8d8e: 30 f4       0.
    bne c8da7                                                         ; 8d90: d0 15       ..
; &8d92 referenced 1 time by &8cf1
.sub_c8d92
    ldy l00b9                                                         ; 8d92: a4 b9       ..
    bmi c8da5                                                         ; 8d94: 30 0f       0.
    iny                                                               ; 8d96: c8          .
    tya                                                               ; 8d97: 98          .
    and #3                                                            ; 8d98: 29 03       ).
    sta l00b9                                                         ; 8d9a: 85 b9       ..
    beq c8da5                                                         ; 8d9c: f0 07       ..
    jsr print_inline                                                  ; 8d9e: 20 05 86     ..
    equs "  "                                                         ; 8da1: 20 20

    bne c8daa                                                         ; 8da3: d0 05       ..
; &8da5 referenced 2 times by &8d94, &8d9c
.c8da5
    lda #&0d                                                          ; 8da5: a9 0d       ..
; &8da7 referenced 1 time by &8d90
.c8da7
    jsr osasci                                                        ; 8da7: 20 e3 ff     ..            ; Write character 13
; &8daa referenced 1 time by &8da3
.c8daa
    inx                                                               ; 8daa: e8          .
    bne print_dir_from_offset                                         ; 8dab: d0 de       ..
    equs "Run"                                                        ; 8dad: 52 75 6e    Run

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
; &8db0 referenced 2 times by &8244, &8c4b
.print_decimal
    tay                                                               ; 8db0: a8          .
    lda #&64 ; 'd'                                                    ; 8db1: a9 64       .d
    jsr print_decimal_digit                                           ; 8db3: 20 bd 8d     ..
    lda #&0a                                                          ; 8db6: a9 0a       ..
    jsr print_decimal_digit                                           ; 8db8: 20 bd 8d     ..
    lda #1                                                            ; 8dbb: a9 01       ..
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
; &8dbd referenced 2 times by &8db3, &8db8
.print_decimal_digit
    sta fs_error_ptr                                                  ; 8dbd: 85 b8       ..
    tya                                                               ; 8dbf: 98          .
    ldx #&2f ; '/'                                                    ; 8dc0: a2 2f       ./
    sec                                                               ; 8dc2: 38          8
; &8dc3 referenced 1 time by &8dc6
.loop_c8dc3
    inx                                                               ; 8dc3: e8          .
    sbc fs_error_ptr                                                  ; 8dc4: e5 b8       ..
    bcs loop_c8dc3                                                    ; 8dc6: b0 fb       ..
    adc fs_error_ptr                                                  ; 8dc8: 65 b8       e.
    tay                                                               ; 8dca: a8          .
    txa                                                               ; 8dcb: 8a          .
; &8dcc referenced 1 time by &8d70
.c8dcc
    jmp osasci                                                        ; 8dcc: 4c e3 ff    L..            ; Write character

    jsr parse_filename_gs                                             ; 8dcf: 20 e1 86     ..
    jsr copy_filename                                                 ; 8dd2: 20 75 8d     u.
    ldy #0                                                            ; 8dd5: a0 00       ..
.sub_c8dd7
    clc                                                               ; 8dd7: 18          .
    jsr gsinit                                                        ; 8dd8: 20 c2 ff     ..
; &8ddb referenced 1 time by &8dde
.loop_c8ddb
    jsr gsread                                                        ; 8ddb: 20 c5 ff     ..
    bcc loop_c8ddb                                                    ; 8dde: 90 fb       ..
    jsr c837a                                                         ; 8de0: 20 7a 83     z.
    clc                                                               ; 8de3: 18          .
    tya                                                               ; 8de4: 98          .
    adc os_text_ptr                                                   ; 8de5: 65 f2       e.
    sta fs_cmd_context                                                ; 8de7: 8d 0a 0e    ...
    lda l00f3                                                         ; 8dea: a5 f3       ..
    adc #0                                                            ; 8dec: 69 00       i.
    sta l0e0b                                                         ; 8dee: 8d 0b 0e    ...
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
    ldx #&0e                                                          ; 8df1: a2 0e       ..
    stx fs_block_offset                                               ; 8df3: 86 bc       ..
    lda #&10                                                          ; 8df5: a9 10       ..
    sta fs_options                                                    ; 8df7: 85 bb       ..
    sta l0e16                                                         ; 8df9: 8d 16 0e    ...
    ldx #&4a ; 'J'                                                    ; 8dfc: a2 4a       .J
    ldy #5                                                            ; 8dfe: a0 05       ..
    jsr send_fs_examine                                               ; 8e00: 20 1b 87     ..
.sub_c8e03
l8e04 = sub_c8e03+1
    lda tube_flag                                                     ; 8e03: ad 67 0d    .g.
    beq c8e1c                                                         ; 8e06: f0 14       ..
    adc l0f0b                                                         ; 8e08: 6d 0b 0f    m..
    adc l0f0c                                                         ; 8e0b: 6d 0c 0f    m..
    bcs c8e1c                                                         ; 8e0e: b0 0c       ..
    jsr tube_claim_loop                                               ; 8e10: 20 cf 8b     ..
    ldx #9                                                            ; 8e13: a2 09       ..
    ldy #&0f                                                          ; 8e15: a0 0f       ..
    lda #4                                                            ; 8e17: a9 04       ..
    jmp tube_addr_claim                                               ; 8e19: 4c 06 04    L..

; &8e1c referenced 2 times by &8e06, &8e0e
.c8e1c
    jmp (l0f09)                                                       ; 8e1c: 6c 09 0f    l..

; ***************************************************************************************
; Set library handle
; 
; Stores Y into &0E04 (library directory handle in FS workspace).
; Falls through to JMP restore_args_return if Y is non-zero.
; ***************************************************************************************
.set_lib_handle
    sty fs_lib_handle                                                 ; 8e1f: 8c 04 0e    ...
    bcc c8e27                                                         ; 8e22: 90 03       ..
; ***************************************************************************************
; Set CSD handle
; 
; Stores Y into &0E03 (current selected directory handle).
; Falls through to JMP restore_args_return.
; ***************************************************************************************
.set_csd_handle
    sty fs_csd_handle                                                 ; 8e24: 8c 03 0e    ...
; &8e27 referenced 2 times by &8e22, &8e38
.c8e27
    jmp restore_args_return                                           ; 8e27: 4c 6f 89    Lo.

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
    sec                                                               ; 8e2a: 38          8
; ***************************************************************************************
; Copy FS reply handles to workspace (no boot)
; 
; CLC entry (SDISC): copies handles only, then jumps to c8cff.
; Called when the FS reply contains updated handle values
; but no boot action is needed.
; ***************************************************************************************
.copy_handles
    ldx #3                                                            ; 8e2b: a2 03       ..
    bcc c8e35                                                         ; 8e2d: 90 06       ..
; &8e2f referenced 1 time by &8e36
.logon2
    lda fs_cmd_data,x                                                 ; 8e2f: bd 05 0f    ...
    sta fs_urd_handle,x                                               ; 8e32: 9d 02 0e    ...
; &8e35 referenced 1 time by &8e2d
.c8e35
    dex                                                               ; 8e35: ca          .
    bpl logon2                                                        ; 8e36: 10 f7       ..
    bcc c8e27                                                         ; 8e38: 90 ed       ..
    ldy fs_boot_option                                                ; 8e3a: ac 05 0e    ...
    ldx l8d1c,y                                                       ; 8e3d: be 1c 8d    ...
    ldy #&8d                                                          ; 8e40: a0 8d       ..
    jmp oscli                                                         ; 8e42: 4c f7 ff    L..

; &8e45 referenced 2 times by &8e5f, &8e6f
.sub_c8e45
    lda l00f0                                                         ; 8e45: a5 f0       ..
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
; &8e47 referenced 3 times by &8305, &8f85, &8f9e
.calc_handle_offset
    asl a                                                             ; 8e47: 0a          .
    asl a                                                             ; 8e48: 0a          .
    pha                                                               ; 8e49: 48          H
    asl a                                                             ; 8e4a: 0a          .
    tsx                                                               ; 8e4b: ba          .
    adc l0101,x                                                       ; 8e4c: 7d 01 01    }..
    tay                                                               ; 8e4f: a8          .
    pla                                                               ; 8e50: 68          h
    cmp #&48 ; 'H'                                                    ; 8e51: c9 48       .H
    bcc return_6                                                      ; 8e53: 90 03       ..
    ldy #0                                                            ; 8e55: a0 00       ..
    tya                                                               ; 8e57: 98          .              ; A=&00
; &8e58 referenced 1 time by &8e53
.return_6
.return_calc_handle
    rts                                                               ; 8e58: 60          `

    ldy #&6f ; 'o'                                                    ; 8e59: a0 6f       .o
    lda (net_rx_ptr),y                                                ; 8e5b: b1 9c       ..
    bcc c8e6c                                                         ; 8e5d: 90 0d       ..
; ***************************************************************************************
; *NET2: read handle entry from workspace
; 
; Looks up the handle in &F0 via calc_handle_offset. If the
; workspace slot contains &3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears rom_svc_num on exit.
; ***************************************************************************************
.net2_read_handle_entry
    jsr sub_c8e45                                                     ; 8e5f: 20 45 8e     E.
    bcs rxpol2                                                        ; 8e62: b0 06       ..
    lda (nfs_workspace),y                                             ; 8e64: b1 9e       ..
    cmp #&3f ; '?'                                                    ; 8e66: c9 3f       .?
    bne c8e6c                                                         ; 8e68: d0 02       ..
; &8e6a referenced 2 times by &8e62, &8e72
.rxpol2
    lda #0                                                            ; 8e6a: a9 00       ..
; &8e6c referenced 2 times by &8e5d, &8e68
.c8e6c
    sta l00f0                                                         ; 8e6c: 85 f0       ..
    rts                                                               ; 8e6e: 60          `

; ***************************************************************************************
; *NET3: close handle (mark as unused)
; 
; Looks up the handle in &F0 via calc_handle_offset. Writes
; &3F ('?') to mark the handle slot as closed in the NFS
; workspace. Preserves the carry flag state across the write
; using ROL/ROR on rx_status_flags. Clears rom_svc_num on exit.
; ***************************************************************************************
.net3_close_handle
    jsr sub_c8e45                                                     ; 8e6f: 20 45 8e     E.
    bcs rxpol2                                                        ; 8e72: b0 f6       ..
    ror rx_flags                                                      ; 8e74: 6e 64 0d    nd.
    lda #&3f ; '?'                                                    ; 8e77: a9 3f       .?
    sta (nfs_workspace),y                                             ; 8e79: 91 9e       ..
    rol rx_flags                                                      ; 8e7b: 2e 64 0d    .d.
    rts                                                               ; 8e7e: 60          `

; ***************************************************************************************
; Filing system OSWORD entry
; 
; Subtracts &0F from the command code in &EF, giving a 0-4 index
; for OSWORD calls &0F-&13 (15-19). Falls through to the
; PHA/PHA/RTS dispatch at &8E80.
; ***************************************************************************************
.osword_fs_entry
    lda l00ef                                                         ; 8e7f: a5 ef       ..             ; Command code from &EF
    sbc #&0f                                                          ; 8e81: e9 0f       ..             ; Subtract &0F: OSWORD &0F-&13 become indices 0-4
    bmi return_7                                                      ; 8e83: 30 2a       0*
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
    cmp #5                                                            ; 8e85: c9 05       ..
    bcs return_7                                                      ; 8e87: b0 26       .&
    jsr fs_osword_dispatch                                            ; 8e89: 20 97 8e     ..
    ldy #2                                                            ; 8e8c: a0 02       ..
; &8e8e referenced 2 times by &8069, &8e94
.c8e8e
    lda (net_rx_ptr),y                                                ; 8e8e: b1 9c       ..
    sta l00aa,y                                                       ; 8e90: 99 aa 00    ...
    dey                                                               ; 8e93: 88          .
    bpl c8e8e                                                         ; 8e94: 10 f8       ..
    rts                                                               ; 8e96: 60          `

; ***************************************************************************************
; PHA/PHA/RTS dispatch for filing system OSWORDs
; 
; X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
; at &8E9F (low) / &8EA4 (high).
; ***************************************************************************************
; &8e97 referenced 1 time by &8e89
.fs_osword_dispatch
    tax                                                               ; 8e97: aa          .
    lda fs_osword_tbl_hi,x                                            ; 8e98: bd b5 8e    ...
    pha                                                               ; 8e9b: 48          H
    lda l8eb0,x                                                       ; 8e9c: bd b0 8e    ...
    pha                                                               ; 8e9f: 48          H
    ldy #2                                                            ; 8ea0: a0 02       ..
; &8ea2 referenced 1 time by &8ea8
.save1
    lda l00aa,y                                                       ; 8ea2: b9 aa 00    ...
    sta (net_rx_ptr),y                                                ; 8ea5: 91 9c       ..
    dey                                                               ; 8ea7: 88          .
    bpl save1                                                         ; 8ea8: 10 f8       ..
    iny                                                               ; 8eaa: c8          .
    lda (l00f0),y                                                     ; 8eab: b1 f0       ..
    sty l00a9                                                         ; 8ead: 84 a9       ..
; &8eaf referenced 2 times by &8e83, &8e87
.return_7
    rts                                                               ; 8eaf: 60          `

; &8eb0 referenced 1 time by &8e9c
.l8eb0
    equb <(osword_0f_handler-1)                                       ; 8eb0: b9          .
    equb <(osword_10_handler-1)                                       ; 8eb1: 73          s
    equb <(osword_11_handler-1)                                       ; 8eb2: d3          .
    equb <(sub_c8ef9-1)                                               ; 8eb3: f8          .
    equb <(econet_tx_rx-1)                                            ; 8eb4: e7          .
; &8eb5 referenced 1 time by &8e98
.fs_osword_tbl_hi
    equb >(osword_0f_handler-1)                                       ; 8eb5: 8e          .              ; Dispatch table: high bytes for OSWORD &0F-&13 handlers
    equb >(osword_10_handler-1)                                       ; 8eb6: 8f          .
    equb >(osword_11_handler-1)                                       ; 8eb7: 8e          .
    equb >(sub_c8ef9-1)                                               ; 8eb8: 8e          .
    equb >(econet_tx_rx-1)                                            ; 8eb9: 8f          .

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
    asl tx_clear_flag                                                 ; 8eba: 0e 62 0d    .b.
    tya                                                               ; 8ebd: 98          .
    bcc readry                                                        ; 8ebe: 90 34       .4
    lda net_rx_ptr_hi                                                 ; 8ec0: a5 9d       ..
    sta l00ac                                                         ; 8ec2: 85 ac       ..
    sta nmi_tx_block_hi                                               ; 8ec4: 85 a1       ..
    lda #&6f ; 'o'                                                    ; 8ec6: a9 6f       .o
    sta l00ab                                                         ; 8ec8: 85 ab       ..
    sta nmi_tx_block                                                  ; 8eca: 85 a0       ..
    ldx #&0f                                                          ; 8ecc: a2 0f       ..
    jsr c8f14                                                         ; 8ece: 20 14 8f     ..
    jmp trampoline_tx_setup                                           ; 8ed1: 4c 60 96    L`.

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
    equb &a5                                                          ; 8ed4: a5          .

.sub_c8ed5
    sta lac85,x                                                       ; 8ed5: 9d 85 ac    ...
    ldy #&7f                                                          ; 8ed8: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8eda: b1 9c       ..
    iny                                                               ; 8edc: c8          .              ; Y=&80
    sty l00ab                                                         ; 8edd: 84 ab       ..
    tax                                                               ; 8edf: aa          .
    dex                                                               ; 8ee0: ca          .
    ldy #0                                                            ; 8ee1: a0 00       ..
    jsr c8f14                                                         ; 8ee3: 20 14 8f     ..
    jmp clear_jsr_protection                                          ; 8ee6: 4c eb 92    L..

; &8ee9 referenced 1 time by &8f44
.read_args_size
    ldy #&7f                                                          ; 8ee9: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8eeb: b1 9c       ..
    ldy #1                                                            ; 8eed: a0 01       ..
    sta (l00f0),y                                                     ; 8eef: 91 f0       ..
    iny                                                               ; 8ef1: c8          .              ; Y=&02
    lda #&80                                                          ; 8ef2: a9 80       ..
; &8ef4 referenced 1 time by &8ebe
.readry
    sta (l00f0),y                                                     ; 8ef4: 91 f0       ..
    rts                                                               ; 8ef6: 60          `

; &8ef7 referenced 1 time by &8f0b
.l8ef7
    equb &ff, 1                                                       ; 8ef7: ff 01       ..

.sub_c8ef9
    cmp #6                                                            ; 8ef9: c9 06       ..
    bcs rsl1                                                          ; 8efb: b0 41       .A
    cmp #4                                                            ; 8efd: c9 04       ..
    bcs rssl1                                                         ; 8eff: b0 22       ."
    lsr a                                                             ; 8f01: 4a          J
    ldx #&0d                                                          ; 8f02: a2 0d       ..
    tay                                                               ; 8f04: a8          .
    beq c8f09                                                         ; 8f05: f0 02       ..
    ldx nfs_workspace_hi                                              ; 8f07: a6 9f       ..
; &8f09 referenced 1 time by &8f05
.c8f09
    stx l00ac                                                         ; 8f09: 86 ac       ..
    lda l8ef7,y                                                       ; 8f0b: b9 f7 8e    ...
    sta l00ab                                                         ; 8f0e: 85 ab       ..
    ldx #1                                                            ; 8f10: a2 01       ..
    ldy #1                                                            ; 8f12: a0 01       ..
; &8f14 referenced 4 times by &8ece, &8ee3, &8f20, &8fb5
.c8f14
    bcc c8f1a                                                         ; 8f14: 90 04       ..
    lda (l00f0),y                                                     ; 8f16: b1 f0       ..
    sta (l00ab),y                                                     ; 8f18: 91 ab       ..
; &8f1a referenced 1 time by &8f14
.c8f1a
    lda (l00ab),y                                                     ; 8f1a: b1 ab       ..
; ***************************************************************************************
; Bidirectional block copy between OSWORD param block and workspace.
; 
; C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
; C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)
; ***************************************************************************************
.copy_param_block
    sta (l00f0),y                                                     ; 8f1c: 91 f0       ..
    iny                                                               ; 8f1e: c8          .
    dex                                                               ; 8f1f: ca          .
    bpl c8f14                                                         ; 8f20: 10 f2       ..
    rts                                                               ; 8f22: 60          `

; &8f23 referenced 1 time by &8eff
.rssl1
    lsr a                                                             ; 8f23: 4a          J
    iny                                                               ; 8f24: c8          .
    lda (l00f0),y                                                     ; 8f25: b1 f0       ..
    bcs rssl2                                                         ; 8f27: b0 05       ..
    lda prot_status                                                   ; 8f29: ad 63 0d    .c.
    sta (l00f0),y                                                     ; 8f2c: 91 f0       ..
; &8f2e referenced 1 time by &8f27
.rssl2
    sta prot_status                                                   ; 8f2e: 8d 63 0d    .c.
    sta saved_jsr_mask                                                ; 8f31: 8d 65 0d    .e.
    rts                                                               ; 8f34: 60          `

; &8f35 referenced 1 time by &8f40
.loop_c8f35
    ldy #&14                                                          ; 8f35: a0 14       ..
    lda (net_rx_ptr),y                                                ; 8f37: b1 9c       ..
    ldy #1                                                            ; 8f39: a0 01       ..
    sta (l00f0),y                                                     ; 8f3b: 91 f0       ..
    rts                                                               ; 8f3d: 60          `

; &8f3e referenced 1 time by &8efb
.rsl1
    cmp #8                                                            ; 8f3e: c9 08       ..
    beq loop_c8f35                                                    ; 8f40: f0 f3       ..
    cmp #9                                                            ; 8f42: c9 09       ..
    beq read_args_size                                                ; 8f44: f0 a3       ..
    bpl c8f61                                                         ; 8f46: 10 19       ..
    ldy #3                                                            ; 8f48: a0 03       ..
    lsr a                                                             ; 8f4a: 4a          J
    bcc readc1                                                        ; 8f4b: 90 1b       ..
    sty l00a8                                                         ; 8f4d: 84 a8       ..
; &8f4f referenced 1 time by &8f5e
.loop_c8f4f
    ldy l00a8                                                         ; 8f4f: a4 a8       ..
    lda (l00f0),y                                                     ; 8f51: b1 f0       ..
    jsr handle_to_mask_a                                              ; 8f53: 20 43 86     C.
    tya                                                               ; 8f56: 98          .
    ldy l00a8                                                         ; 8f57: a4 a8       ..
    sta fs_server_net,y                                               ; 8f59: 99 01 0e    ...
    dec l00a8                                                         ; 8f5c: c6 a8       ..
    bne loop_c8f4f                                                    ; 8f5e: d0 ef       ..
    rts                                                               ; 8f60: 60          `

; &8f61 referenced 1 time by &8f46
.c8f61
    iny                                                               ; 8f61: c8          .
    lda fs_last_error                                                 ; 8f62: ad 09 0e    ...
    sta (l00f0),y                                                     ; 8f65: 91 f0       ..
    rts                                                               ; 8f67: 60          `

; &8f68 referenced 2 times by &8f4b, &8f71
.readc1
    lda fs_server_net,y                                               ; 8f68: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8f6b: 20 60 86     `.            ; Convert bitmask to handle number (FS2A)
    sta (l00f0),y                                                     ; 8f6e: 91 f0       ..             ; A=handle number (&20-&27); Y=preserved
    dey                                                               ; 8f70: 88          .
    bne readc1                                                        ; 8f71: d0 f5       ..
    rts                                                               ; 8f73: 60          `

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
    ldx nfs_workspace_hi                                              ; 8f74: a6 9f       ..
    stx l00ac                                                         ; 8f76: 86 ac       ..
    sty l00ab                                                         ; 8f78: 84 ab       ..
    ror rx_flags                                                      ; 8f7a: 6e 64 0d    nd.
    lda (l00f0),y                                                     ; 8f7d: b1 f0       ..
    sta l00aa                                                         ; 8f7f: 85 aa       ..             ; Load from ROM template (zero = use NMI workspace value)
    bne c8f9e                                                         ; 8f81: d0 1b       ..
    lda #3                                                            ; 8f83: a9 03       ..
; &8f85 referenced 1 time by &8f97
.scan0
    jsr calc_handle_offset                                            ; 8f85: 20 47 8e     G.
    bcs openl4                                                        ; 8f88: b0 3d       .=
    lsr a                                                             ; 8f8a: 4a          J
    lsr a                                                             ; 8f8b: 4a          J
    tax                                                               ; 8f8c: aa          .
    lda (l00ab),y                                                     ; 8f8d: b1 ab       ..
    beq openl4                                                        ; 8f8f: f0 36       .6
    cmp #&3f ; '?'                                                    ; 8f91: c9 3f       .?
    beq scan1                                                         ; 8f93: f0 04       ..
    inx                                                               ; 8f95: e8          .
    txa                                                               ; 8f96: 8a          .
    bne scan0                                                         ; 8f97: d0 ec       ..
; &8f99 referenced 1 time by &8f93
.scan1
    txa                                                               ; 8f99: 8a          .
    ldx #0                                                            ; 8f9a: a2 00       ..
    sta (l00f0,x)                                                     ; 8f9c: 81 f0       ..
; &8f9e referenced 1 time by &8f81
.c8f9e
    jsr calc_handle_offset                                            ; 8f9e: 20 47 8e     G.
    bcs openl4                                                        ; 8fa1: b0 24       .$
    dey                                                               ; 8fa3: 88          .
    sty l00ab                                                         ; 8fa4: 84 ab       ..
    lda #&c0                                                          ; 8fa6: a9 c0       ..
    ldy #1                                                            ; 8fa8: a0 01       ..
    ldx #&0b                                                          ; 8faa: a2 0b       ..             ; Enable interrupts before transmit
    cpy l00aa                                                         ; 8fac: c4 aa       ..
    adc (l00ab),y                                                     ; 8fae: 71 ab       q.
    beq openl6                                                        ; 8fb0: f0 03       ..             ; Dest station = &FFFF (accept reply from any station)
    bmi openl7                                                        ; 8fb2: 30 0e       0.
; &8fb4 referenced 1 time by &8fc4
.loop_c8fb4
    clc                                                               ; 8fb4: 18          .
; &8fb5 referenced 1 time by &8fb0
.openl6
    jsr c8f14                                                         ; 8fb5: 20 14 8f     ..
    bcs c8fc9                                                         ; 8fb8: b0 0f       ..
    lda #&3f ; '?'                                                    ; 8fba: a9 3f       .?
    ldy #1                                                            ; 8fbc: a0 01       ..
    sta (l00ab),y                                                     ; 8fbe: 91 ab       ..
    bne c8fc9                                                         ; 8fc0: d0 07       ..             ; ALWAYS branch

; &8fc2 referenced 1 time by &8fb2
.openl7
    adc #1                                                            ; 8fc2: 69 01       i.             ; Initiate receive with timeout
    bne loop_c8fb4                                                    ; 8fc4: d0 ee       ..
    dey                                                               ; 8fc6: 88          .
; &8fc7 referenced 3 times by &8f88, &8f8f, &8fa1
.openl4
    sta (l00f0),y                                                     ; 8fc7: 91 f0       ..
; &8fc9 referenced 2 times by &8fb8, &8fc0
.c8fc9
    rol rx_flags                                                      ; 8fc9: 2e 64 0d    .d.
    rts                                                               ; 8fcc: 60          `

; ***************************************************************************************
; Set up RX buffer pointers in NFS workspace
; 
; Calculates the start address of the RX data area (&F0+1) and stores
; it at workspace offset &28. Also reads the data length from (&F0)+1
; and adds it to &F0 to compute the end address at offset &2C.
; ***************************************************************************************
; &8fcd referenced 1 time by &9000
.setup_rx_buffer_ptrs
    ldy #&1c                                                          ; 8fcd: a0 1c       ..
    lda l00f0                                                         ; 8fcf: a5 f0       ..
    adc #1                                                            ; 8fd1: 69 01       i.
    jsr store_16bit_at_y                                              ; 8fd3: 20 de 8f     ..            ; Receive data blocks until command byte = &00 or &0D
    ldy #1                                                            ; 8fd6: a0 01       ..
    lda (l00f0),y                                                     ; 8fd8: b1 f0       ..
    ldy #&20 ; ' '                                                    ; 8fda: a0 20       .
    adc l00f0                                                         ; 8fdc: 65 f0       e.
; &8fde referenced 1 time by &8fd3
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8fde: 91 9e       ..
    iny                                                               ; 8fe0: c8          .
    lda l00f1                                                         ; 8fe1: a5 f1       ..
    adc #0                                                            ; 8fe3: 69 00       i.
    sta (nfs_workspace),y                                             ; 8fe5: 91 9e       ..
    rts                                                               ; 8fe7: 60          `

; ***************************************************************************************
; Econet transmit/receive handler
; 
; A=0: Initialise TX control block from ROM template at &834A
;      (zero entries substituted from NMI workspace &0DDA), transmit
;      it, set up RX control block, and receive reply.
; A>=1: Handle transmit result (branch to cleanup at &8F49).
; ***************************************************************************************
.econet_tx_rx
    cmp #1                                                            ; 8fe8: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs c9034                                                         ; 8fea: b0 48       .H
    ldy #&23 ; '#'                                                    ; 8fec: a0 23       .#
; &8fee referenced 1 time by &8ffb
.dofs01
    lda init_tx_ctrl_block,y                                          ; 8fee: b9 91 83    ...
    bne c8ff6                                                         ; 8ff1: d0 03       ..
    lda l0de6,y                                                       ; 8ff3: b9 e6 0d    ...
; &8ff6 referenced 1 time by &8ff1
.c8ff6
    sta (nfs_workspace),y                                             ; 8ff6: 91 9e       ..
    dey                                                               ; 8ff8: 88          .
    cpy #&17                                                          ; 8ff9: c0 17       ..
    bne dofs01                                                        ; 8ffb: d0 f1       ..
    iny                                                               ; 8ffd: c8          .
    sty net_tx_ptr                                                    ; 8ffe: 84 9a       ..
    jsr setup_rx_buffer_ptrs                                          ; 9000: 20 cd 8f     ..
    ldy #2                                                            ; 9003: a0 02       ..
    lda #&90                                                          ; 9005: a9 90       ..
    sta (l00f0),y                                                     ; 9007: 91 f0       ..
    iny                                                               ; 9009: c8          .              ; Y=&03
    iny                                                               ; 900a: c8          .              ; Retrieve original A (function code) from stack; Y=&04
; &900b referenced 1 time by &9013
.loop_c900b
    lda l0dfe,y                                                       ; 900b: b9 fe 0d    ...
    sta (l00f0),y                                                     ; 900e: 91 f0       ..
    iny                                                               ; 9010: c8          .
    cpy #7                                                            ; 9011: c0 07       ..
    bne loop_c900b                                                    ; 9013: d0 f6       ..
    lda nfs_workspace_hi                                              ; 9015: a5 9f       ..
    sta net_tx_ptr_hi                                                 ; 9017: 85 9b       ..
    cli                                                               ; 9019: 58          X
    jsr tx_poll_ff                                                    ; 901a: 20 8f 86     ..
    ldy #&20 ; ' '                                                    ; 901d: a0 20       .
    lda #&ff                                                          ; 901f: a9 ff       ..
    sta (nfs_workspace),y                                             ; 9021: 91 9e       ..
    iny                                                               ; 9023: c8          .              ; Y=&21
    sta (nfs_workspace),y                                             ; 9024: 91 9e       ..
    ldy #&19                                                          ; 9026: a0 19       ..
    lda #&90                                                          ; 9028: a9 90       ..
    sta (nfs_workspace),y                                             ; 902a: 91 9e       ..
    dey                                                               ; 902c: 88          .              ; Y=&18
    lda #&7f                                                          ; 902d: a9 7f       ..
    sta (nfs_workspace),y                                             ; 902f: 91 9e       ..
    jmp c851b                                                         ; 9031: 4c 1b 85    L..

; &9034 referenced 1 time by &8fea
.c9034
    php                                                               ; 9034: 08          .
    ldy #1                                                            ; 9035: a0 01       ..             ; Y=character to write
    lda (l00f0),y                                                     ; 9037: b1 f0       ..
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
    tax                                                               ; 9039: aa          .
    iny                                                               ; 903a: c8          .              ; ROR/ASL on stacked P: zeros carry to signal success
    lda (l00f0),y                                                     ; 903b: b1 f0       ..
    iny                                                               ; 903d: c8          .
    sty l00ab                                                         ; 903e: 84 ab       ..
    ldy #&72 ; 'r'                                                    ; 9040: a0 72       .r
    sta (net_rx_ptr),y                                                ; 9042: 91 9c       ..
    dey                                                               ; 9044: 88          .              ; Y=&71
    txa                                                               ; 9045: 8a          .
    sta (net_rx_ptr),y                                                ; 9046: 91 9c       ..
    plp                                                               ; 9048: 28          (
    bne dofs2                                                         ; 9049: d0 1c       ..
; &904b referenced 1 time by &9064
.loop_c904b
    ldy l00ab                                                         ; 904b: a4 ab       ..
    inc l00ab                                                         ; 904d: e6 ab       ..
    lda (l00f0),y                                                     ; 904f: b1 f0       ..
    beq return_8                                                      ; 9051: f0 13       ..
    ldy #&7d ; '}'                                                    ; 9053: a0 7d       .}
    sta (net_rx_ptr),y                                                ; 9055: 91 9c       ..
    pha                                                               ; 9057: 48          H
    jsr ctrl_block_setup_alt                                          ; 9058: 20 73 91     s.
    jsr sub_c9072                                                     ; 905b: 20 72 90     r.
; &905e referenced 1 time by &905f
.loop_c905e
    dex                                                               ; 905e: ca          .
    bne loop_c905e                                                    ; 905f: d0 fd       ..
    pla                                                               ; 9061: 68          h
    eor #&0d                                                          ; 9062: 49 0d       I.             ; Test for end-of-data marker (&0D)
    bne loop_c904b                                                    ; 9064: d0 e5       ..
; &9066 referenced 1 time by &9051
.return_8
    rts                                                               ; 9066: 60          `

; &9067 referenced 1 time by &9049
.dofs2
    jsr ctrl_block_setup_alt                                          ; 9067: 20 73 91     s.
    ldy #&7b ; '{'                                                    ; 906a: a0 7b       .{
    lda (net_rx_ptr),y                                                ; 906c: b1 9c       ..
    adc #3                                                            ; 906e: 69 03       i.
    sta (net_rx_ptr),y                                                ; 9070: 91 9c       ..
; &9072 referenced 1 time by &905b
.sub_c9072
    cli                                                               ; 9072: 58          X
    jmp tx_poll_ff                                                    ; 9073: 4c 8f 86    L..

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
    php                                                               ; 9076: 08          .
    pha                                                               ; 9077: 48          H
    txa                                                               ; 9078: 8a          .
    pha                                                               ; 9079: 48          H
    tya                                                               ; 907a: 98          .
    pha                                                               ; 907b: 48          H
    tsx                                                               ; 907c: ba          .
    lda l0103,x                                                       ; 907d: bd 03 01    ...
    cmp #9                                                            ; 9080: c9 09       ..
    bcs entry1                                                        ; 9082: b0 04       ..
    tax                                                               ; 9084: aa          .
    jsr osword_trampoline                                             ; 9085: 20 8f 90     ..
; &9088 referenced 1 time by &9082
.entry1
    pla                                                               ; 9088: 68          h
    tay                                                               ; 9089: a8          .
    pla                                                               ; 908a: 68          h
    tax                                                               ; 908b: aa          .
    pla                                                               ; 908c: 68          h
    plp                                                               ; 908d: 28          (
    rts                                                               ; 908e: 60          `

; &908f referenced 1 time by &9085
.osword_trampoline
    lda l90a3,x                                                       ; 908f: bd a3 90    ...            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 9092: 48          H
    lda l909a,x                                                       ; 9093: bd 9a 90    ...
    pha                                                               ; 9096: 48          H
    lda l00ef                                                         ; 9097: a5 ef       ..
    rts                                                               ; 9099: 60          `

; &909a referenced 1 time by &9093
.l909a
    equb <(return_1-1)                                                ; 909a: f5          .
    equb <(remote_print_handler-1)                                    ; 909b: de          .
    equb <(remote_print_handler-1)                                    ; 909c: de          .
    equb <(remote_print_handler-1)                                    ; 909d: de          .
    equb <(sub_c90ac-1)                                               ; 909e: ab          .
    equb <(printer_select_handler-1)                                  ; 909f: ce          .
    equb <(return_1-1)                                                ; 90a0: f5          .
    equb <(remote_cmd_dispatch-1)                                     ; 90a1: dd          .
    equb <(sub_c9148-1)                                               ; 90a2: 47          G
; &90a3 referenced 1 time by &908f
.l90a3
    equb >(return_1-1)                                                ; 90a3: 80          .
    equb >(remote_print_handler-1)                                    ; 90a4: 91          .
    equb >(remote_print_handler-1)                                    ; 90a5: 91          .
    equb >(remote_print_handler-1)                                    ; 90a6: 91          .
    equb >(sub_c90ac-1)                                               ; 90a7: 90          .
    equb >(printer_select_handler-1)                                  ; 90a8: 91          .
    equb >(return_1-1)                                                ; 90a9: 80          .
    equb >(remote_cmd_dispatch-1)                                     ; 90aa: 90          .
    equb >(sub_c9148-1)                                               ; 90ab: 91          .

.sub_c90ac
    tsx                                                               ; 90ac: ba          .
    ror l0106,x                                                       ; 90ad: 7e 06 01    ~..
    asl l0106,x                                                       ; 90b0: 1e 06 01    ...
    tya                                                               ; 90b3: 98          .
    ldy #&da                                                          ; 90b4: a0 da       ..
    sta (nfs_workspace),y                                             ; 90b6: 91 9e       ..
    lda #0                                                            ; 90b8: a9 00       ..
; ***************************************************************************************
; Set up TX control block and send
; 
; Builds a TX control block at (nfs_workspace)+&0C from the current
; workspace state, then initiates transmission via the ADLC TX path.
; This is the common send routine used after command data has been
; prepared. The exact control block layout and field mapping need
; further analysis.
; ***************************************************************************************
; &90ba referenced 3 times by &81cb, &910d, &916e
.setup_tx_and_send
    ldy #&d9                                                          ; 90ba: a0 d9       ..
    sta (nfs_workspace),y                                             ; 90bc: 91 9e       ..
    lda #&80                                                          ; 90be: a9 80       ..
    ldy #&0c                                                          ; 90c0: a0 0c       ..
    sta (nfs_workspace),y                                             ; 90c2: 91 9e       ..
    lda net_tx_ptr                                                    ; 90c4: a5 9a       ..
    pha                                                               ; 90c6: 48          H
    lda net_tx_ptr_hi                                                 ; 90c7: a5 9b       ..
    pha                                                               ; 90c9: 48          H
    sty net_tx_ptr                                                    ; 90ca: 84 9a       ..
    ldx nfs_workspace_hi                                              ; 90cc: a6 9f       ..
    stx net_tx_ptr_hi                                                 ; 90ce: 86 9b       ..
    jsr tx_poll_ff                                                    ; 90d0: 20 8f 86     ..
    lda #&3f ; '?'                                                    ; 90d3: a9 3f       .?
    sta (net_tx_ptr,x)                                                ; 90d5: 81 9a       ..
    pla                                                               ; 90d7: 68          h
    sta net_tx_ptr_hi                                                 ; 90d8: 85 9b       ..
    pla                                                               ; 90da: 68          h
    sta net_tx_ptr                                                    ; 90db: 85 9a       ..
    rts                                                               ; 90dd: 60          `

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
    ldy l00f1                                                         ; 90de: a4 f1       ..
    cmp #&81                                                          ; 90e0: c9 81       ..
    beq c90f7                                                         ; 90e2: f0 13       ..
    ldy #1                                                            ; 90e4: a0 01       ..
    ldx #7                                                            ; 90e6: a2 07       ..
    jsr match_osbyte_code                                             ; 90e8: 20 30 91     0.
    beq c90f7                                                         ; 90eb: f0 0a       ..
    dey                                                               ; 90ed: 88          .
    dey                                                               ; 90ee: 88          .
    ldx #&0e                                                          ; 90ef: a2 0e       ..
    jsr match_osbyte_code                                             ; 90f1: 20 30 91     0.
    beq c90f7                                                         ; 90f4: f0 01       ..
    iny                                                               ; 90f6: c8          .
; &90f7 referenced 3 times by &90e2, &90eb, &90f4
.c90f7
    ldx #2                                                            ; 90f7: a2 02       ..
    tya                                                               ; 90f9: 98          .
    beq return_nbyte                                                  ; 90fa: f0 33       .3
    php                                                               ; 90fc: 08          .
    bpl nbyte6                                                        ; 90fd: 10 01       ..
    inx                                                               ; 90ff: e8          .              ; X=&03
; &9100 referenced 1 time by &90fd
.nbyte6
    ldy #&dc                                                          ; 9100: a0 dc       ..
; &9102 referenced 1 time by &910a
.nbyte1
    lda l0015,y                                                       ; 9102: b9 15 00    ...
    sta (nfs_workspace),y                                             ; 9105: 91 9e       ..
    dey                                                               ; 9107: 88          .
    cpy #&da                                                          ; 9108: c0 da       ..
    bpl nbyte1                                                        ; 910a: 10 f6       ..
    txa                                                               ; 910c: 8a          .
    jsr setup_tx_and_send                                             ; 910d: 20 ba 90     ..
    plp                                                               ; 9110: 28          (
    bpl return_nbyte                                                  ; 9111: 10 1c       ..
    lda #&7f                                                          ; 9113: a9 7f       ..
    sta (net_tx_ptr,x)                                                ; 9115: 81 9a       ..
; &9117 referenced 1 time by &9119
.loop_c9117
    lda (net_tx_ptr,x)                                                ; 9117: a1 9a       ..
    bpl loop_c9117                                                    ; 9119: 10 fc       ..
    tsx                                                               ; 911b: ba          .
    ldy #&dd                                                          ; 911c: a0 dd       ..
    lda (nfs_workspace),y                                             ; 911e: b1 9e       ..
    ora #&44 ; 'D'                                                    ; 9120: 09 44       .D
    bne nbyte5                                                        ; 9122: d0 04       ..             ; ALWAYS branch

; &9124 referenced 1 time by &912d
.nbyte4
    dey                                                               ; 9124: 88          .
    dex                                                               ; 9125: ca          .
    lda (nfs_workspace),y                                             ; 9126: b1 9e       ..
; &9128 referenced 1 time by &9122
.nbyte5
    sta l0106,x                                                       ; 9128: 9d 06 01    ...
    cpy #&da                                                          ; 912b: c0 da       ..
    bne nbyte4                                                        ; 912d: d0 f5       ..
; &912f referenced 2 times by &90fa, &9111
.return_nbyte
    rts                                                               ; 912f: 60          `

; &9130 referenced 3 times by &90e8, &90f1, &9136
.match_osbyte_code
    cmp l9139,x                                                       ; 9130: dd 39 91    .9.
    beq return_match_osbyte                                           ; 9133: f0 03       ..
    dex                                                               ; 9135: ca          .
    bpl match_osbyte_code                                             ; 9136: 10 f8       ..
; &9138 referenced 2 times by &9133, &9150
.return_match_osbyte
    rts                                                               ; 9138: 60          `

; &9139 referenced 1 time by &9130
.l9139
    equb   4,   9, &0a, &14, &15, &9a, &9b, &e2, &0b, &0c, &0f, &79   ; 9139: 04 09 0a... ...
    equb &7a, &e3, &e4                                                ; 9145: 7a e3 e4    z..

.sub_c9148
    ldy #&0e                                                          ; 9148: a0 0e       ..
    cmp #7                                                            ; 914a: c9 07       ..
    beq c9152                                                         ; 914c: f0 04       ..
    cmp #8                                                            ; 914e: c9 08       ..
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
    bne return_match_osbyte                                           ; 9150: d0 e6       ..
; &9152 referenced 1 time by &914c
.c9152
    ldx #&db                                                          ; 9152: a2 db       ..
    stx nfs_workspace                                                 ; 9154: 86 9e       ..
; &9156 referenced 1 time by &915b
.loop_c9156
    lda (l00f0),y                                                     ; 9156: b1 f0       ..
    sta (nfs_workspace),y                                             ; 9158: 91 9e       ..
    dey                                                               ; 915a: 88          .
    bpl loop_c9156                                                    ; 915b: 10 f9       ..
    iny                                                               ; 915d: c8          .
    dec nfs_workspace                                                 ; 915e: c6 9e       ..
    lda l00ef                                                         ; 9160: a5 ef       ..
    sta (nfs_workspace),y                                             ; 9162: 91 9e       ..
    sty nfs_workspace                                                 ; 9164: 84 9e       ..
    ldy #&14                                                          ; 9166: a0 14       ..
    lda #&e9                                                          ; 9168: a9 e9       ..
    sta (nfs_workspace),y                                             ; 916a: 91 9e       ..
    lda #1                                                            ; 916c: a9 01       ..
    jsr setup_tx_and_send                                             ; 916e: 20 ba 90     ..            ; Load template byte from ctrl_block_template[X]
    stx nfs_workspace                                                 ; 9171: 86 9e       ..
; ***************************************************************************************
; Alternate entry into control block setup
; 
; Sets X=&0D, Y=&7C. Tests bit 6 of &8374 to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; ***************************************************************************************
; &9173 referenced 2 times by &9058, &9067
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 9173: a2 0d       ..
    ldy #&7c ; '|'                                                    ; 9175: a0 7c       .|
    bit l83af                                                         ; 9177: 2c af 83    ,..
    bvs cbset2                                                        ; 917a: 70 05       p.
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
; &917c referenced 1 time by &84bc
.ctrl_block_setup
    ldy #&17                                                          ; 917c: a0 17       ..
    ldx #&1a                                                          ; 917e: a2 1a       ..
; &9180 referenced 1 time by &9244
.ctrl_block_setup_clv
    clv                                                               ; 9180: b8          .
; &9181 referenced 1 time by &917a
.cbset2
    lda ctrl_block_template,x                                         ; 9181: bd a8 91    ...
    cmp #&fe                                                          ; 9184: c9 fe       ..
    beq l91a4                                                         ; 9186: f0 1c       ..
    cmp #&fd                                                          ; 9188: c9 fd       ..
    beq l91a0                                                         ; 918a: f0 14       ..
    cmp #&fc                                                          ; 918c: c9 fc       ..
    bne cbset3                                                        ; 918e: d0 08       ..
    lda net_rx_ptr_hi                                                 ; 9190: a5 9d       ..
    bvs c9196                                                         ; 9192: 70 02       p.
    lda nfs_workspace_hi                                              ; 9194: a5 9f       ..
; &9196 referenced 1 time by &9192
.c9196
    sta net_tx_ptr_hi                                                 ; 9196: 85 9b       ..
; &9198 referenced 1 time by &918e
.cbset3
    bvs cbset4                                                        ; 9198: 70 04       p.
    sta (nfs_workspace),y                                             ; 919a: 91 9e       ..
    equb &50                                                          ; 919c: 50          P
    equb 2                                                            ; 919d: 02          .
; &919e referenced 1 time by &9198
.cbset4
    equb &91                                                          ; 919e: 91          .
    equb &9c                                                          ; 919f: 9c          .
; &91a0 referenced 1 time by &918a
.l91a0
    equb &88                                                          ; 91a0: 88          .
    equb &ca                                                          ; 91a1: ca          .
    equb &10                                                          ; 91a2: 10          .
    equb &dd                                                          ; 91a3: dd          .
; &91a4 referenced 1 time by &9186
.l91a4
    equb &c8                                                          ; 91a4: c8          .
    equb &84                                                          ; 91a5: 84          .
    equb &9a                                                          ; 91a6: 9a          .
    equb &60                                                          ; 91a7: 60          `
; ***************************************************************************************
; Control block initialisation template
; 
; Read by the loop at &9176, indexed by X from a starting value
; down to 0. Values are stored into either (nfs_workspace) or
; (net_rx_ptr) at offset Y, depending on the V flag.
; 
; Two entry paths read different slices of this table:
;   ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
;   ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &8374
; 
; Sentinel values:
;   &FE = stop processing
;   &FD = skip this offset (decrement Y but don't store)
;   &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)
; ***************************************************************************************
; &91a8 referenced 1 time by &9181
.ctrl_block_template
    equb &85                                                          ; 91a8: 85          .              ; Alt-path only → Y=&6F
    equb 0                                                            ; 91a9: 00          .
    equb &fd                                                          ; 91aa: fd          .              ; SKIP
    equb &fd                                                          ; 91ab: fd          .
    equb &7d                                                          ; 91ac: 7d          }
    equb &fc                                                          ; 91ad: fc          .              ; PAGE byte → Y=&02 / Y=&74
    equb &ff                                                          ; 91ae: ff          .              ; → Y=&03 / Y=&75
    equb &ff                                                          ; 91af: ff          .              ; → Y=&04 / Y=&76
    equb &7e                                                          ; 91b0: 7e          ~              ; → Y=&05 / Y=&77
    equb &fc                                                          ; 91b1: fc          .
    equb &ff                                                          ; 91b2: ff          .
    equb &ff                                                          ; 91b3: ff          .              ; → Y=&08 / Y=&7A
    equb 0                                                            ; 91b4: 00          .              ; → Y=&09 / Y=&7B
    equb 0                                                            ; 91b5: 00          .              ; → Y=&0A / Y=&7C
    equb &fe                                                          ; 91b6: fe          .              ; STOP — main-path boundary
    equb &80                                                          ; 91b7: 80          .
    equb &93, &fd, &fd, &d9, &fc, &ff, &ff, &de, &fc, &ff, &ff, &fe   ; 91b8: 93 fd fd... ...
    equb &d1, &fd, &fd, &1f                                           ; 91c4: d1 fd fd... ...
; &91c8 referenced 1 time by &82f6
.l91c8
    equb &fd, &ff, &ff, &fd, &fd, &ff, &ff                            ; 91c8: fd ff ff... ...

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
    dex                                                               ; 91cf: ca          .
    cpx l00f0                                                         ; 91d0: e4 f0       ..
    bne setup1                                                        ; 91d2: d0 07       ..
    lda #&1f                                                          ; 91d4: a9 1f       ..
    sta printer_buf_ptr                                               ; 91d6: 8d 61 0d    .a.
    lda #&41 ; 'A'                                                    ; 91d9: a9 41       .A
; &91db referenced 1 time by &91d2
.setup1
    sta l0d60                                                         ; 91db: 8d 60 0d    .`.
; &91de referenced 2 times by &91e1, &91f5
.return_printer_select
    rts                                                               ; 91de: 60          `

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
    cpy #4                                                            ; 91df: c0 04       ..
    bne return_printer_select                                         ; 91e1: d0 fb       ..
    txa                                                               ; 91e3: 8a          .
    dex                                                               ; 91e4: ca          .
    bne c920d                                                         ; 91e5: d0 26       .&
    tsx                                                               ; 91e7: ba          .
    ora l0106,x                                                       ; 91e8: 1d 06 01    ...
    sta l0106,x                                                       ; 91eb: 9d 06 01    ...
; &91ee referenced 2 times by &91fd, &9202
.prlp1
    lda #osbyte_read_buffer                                           ; 91ee: a9 91       ..
    ldx #buffer_printer                                               ; 91f0: a2 03       ..
    jsr osbyte                                                        ; 91f2: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_printer_select                                         ; 91f5: b0 e7       ..
    tya                                                               ; 91f7: 98          .              ; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 91f8: 20 04 92     ..
    cpy #&6e ; 'n'                                                    ; 91fb: c0 6e       .n
    bcc prlp1                                                         ; 91fd: 90 ef       ..
    jsr flush_output_block                                            ; 91ff: 20 30 92     0.
    bcc prlp1                                                         ; 9202: 90 ea       ..
; ***************************************************************************************
; Store output byte to network buffer
; 
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; ***************************************************************************************
; &9204 referenced 2 times by &91f8, &9211
.store_output_byte
    ldy printer_buf_ptr                                               ; 9204: ac 61 0d    .a.
    sta (net_rx_ptr),y                                                ; 9207: 91 9c       ..
    inc printer_buf_ptr                                               ; 9209: ee 61 0d    .a.
    rts                                                               ; 920c: 60          `

; &920d referenced 1 time by &91e5
.c920d
    pha                                                               ; 920d: 48          H
    txa                                                               ; 920e: 8a          .
    eor #1                                                            ; 920f: 49 01       I.
    jsr store_output_byte                                             ; 9211: 20 04 92     ..
    eor l0d60                                                         ; 9214: 4d 60 0d    M`.
    ror a                                                             ; 9217: 6a          j
    bcc c9221                                                         ; 9218: 90 07       ..
    rol a                                                             ; 921a: 2a          *
    sta l0d60                                                         ; 921b: 8d 60 0d    .`.
    jsr flush_output_block                                            ; 921e: 20 30 92     0.
; &9221 referenced 1 time by &9218
.c9221
    lda l0d60                                                         ; 9221: ad 60 0d    .`.
    and #&f0                                                          ; 9224: 29 f0       ).
    ror a                                                             ; 9226: 6a          j
    tax                                                               ; 9227: aa          .
    pla                                                               ; 9228: 68          h
    ror a                                                             ; 9229: 6a          j
    txa                                                               ; 922a: 8a          .
    rol a                                                             ; 922b: 2a          *
    sta l0d60                                                         ; 922c: 8d 60 0d    .`.
    rts                                                               ; 922f: 60          `

; ***************************************************************************************
; Flush output block
; 
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; ***************************************************************************************
; &9230 referenced 2 times by &91ff, &921e
.flush_output_block
    ldy #8                                                            ; 9230: a0 08       ..
    lda printer_buf_ptr                                               ; 9232: ad 61 0d    .a.
    sta (nfs_workspace),y                                             ; 9235: 91 9e       ..
    lda net_rx_ptr_hi                                                 ; 9237: a5 9d       ..
    iny                                                               ; 9239: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 923a: 91 9e       ..
    ldy #5                                                            ; 923c: a0 05       ..
    sta (nfs_workspace),y                                             ; 923e: 91 9e       ..
    ldy #&0b                                                          ; 9240: a0 0b       ..
    ldx #&26 ; '&'                                                    ; 9242: a2 26       .&
    jsr ctrl_block_setup_clv                                          ; 9244: 20 80 91     ..
    dey                                                               ; 9247: 88          .
    lda l0d60                                                         ; 9248: ad 60 0d    .`.
    pha                                                               ; 924b: 48          H
    rol a                                                             ; 924c: 2a          *
    pla                                                               ; 924d: 68          h
    eor #&80                                                          ; 924e: 49 80       I.
    sta l0d60                                                         ; 9250: 8d 60 0d    .`.
    rol a                                                             ; 9253: 2a          *
    sta (nfs_workspace),y                                             ; 9254: 91 9e       ..
    ldy #&1f                                                          ; 9256: a0 1f       ..
    sty printer_buf_ptr                                               ; 9258: 8c 61 0d    .a.
    lda #0                                                            ; 925b: a9 00       ..
    tax                                                               ; 925d: aa          .              ; X=&00
    ldy nfs_workspace_hi                                              ; 925e: a4 9f       ..
    cli                                                               ; 9260: 58          X
; ***************************************************************************************
; Transmit with retry loop (XMITFS/XMITFY)
; 
; Calls the low-level transmit routine (BRIANX) with FSTRY (&FF = 255)
; retries and FSDELY (&60 = 96) ms delay between attempts. On each
; iteration, checks the result code: zero means success, non-zero
; means retry. After all retries exhausted, reports a 'Net error'.
; Entry point XMITFY allows a custom delay in Y.
; ***************************************************************************************
; &9261 referenced 2 times by &8408, &8441
.econet_tx_retry
    stx net_tx_ptr                                                    ; 9261: 86 9a       ..
    sty net_tx_ptr_hi                                                 ; 9263: 84 9b       ..
    pha                                                               ; 9265: 48          H
    and fs_sequence_nos                                               ; 9266: 2d 08 0e    -..
    beq bsxl1                                                         ; 9269: f0 02       ..
    lda #1                                                            ; 926b: a9 01       ..
; &926d referenced 1 time by &9269
.bsxl1
    ldy #0                                                            ; 926d: a0 00       ..
    ora (net_tx_ptr),y                                                ; 926f: 11 9a       ..
    pha                                                               ; 9271: 48          H
    sta (net_tx_ptr),y                                                ; 9272: 91 9a       ..
    jsr tx_poll_ff                                                    ; 9274: 20 8f 86     ..
    lda #&ff                                                          ; 9277: a9 ff       ..
    ldy #8                                                            ; 9279: a0 08       ..
    sta (net_tx_ptr),y                                                ; 927b: 91 9a       ..
    iny                                                               ; 927d: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 927e: 91 9a       ..
    pla                                                               ; 9280: 68          h
    tax                                                               ; 9281: aa          .
    ldy #&d1                                                          ; 9282: a0 d1       ..
    pla                                                               ; 9284: 68          h
    pha                                                               ; 9285: 48          H
    beq bspsx                                                         ; 9286: f0 02       ..
    ldy #&90                                                          ; 9288: a0 90       ..
; &928a referenced 1 time by &9286
.bspsx
    tya                                                               ; 928a: 98          .
    ldy #1                                                            ; 928b: a0 01       ..
    sta (net_tx_ptr),y                                                ; 928d: 91 9a       ..
    txa                                                               ; 928f: 8a          .
    dey                                                               ; 9290: 88          .              ; Y=&00
    pha                                                               ; 9291: 48          H
; &9292 referenced 1 time by &929e
.bsxl0
    lda #&7f                                                          ; 9292: a9 7f       ..
    sta (net_tx_ptr),y                                                ; 9294: 91 9a       ..
    jsr c851b                                                         ; 9296: 20 1b 85     ..
    pla                                                               ; 9299: 68          h
    pha                                                               ; 929a: 48          H
    eor (net_tx_ptr),y                                                ; 929b: 51 9a       Q.
    ror a                                                             ; 929d: 6a          j
    bcs bsxl0                                                         ; 929e: b0 f2       ..
    pla                                                               ; 92a0: 68          h
    pla                                                               ; 92a1: 68          h
    eor fs_sequence_nos                                               ; 92a2: 4d 08 0e    M..
.return_bspsx
    rts                                                               ; 92a5: 60          `

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
    lda l00ad                                                         ; 92a6: a5 ad       ..
    pha                                                               ; 92a8: 48          H
    lda #&e9                                                          ; 92a9: a9 e9       ..
    sta nfs_workspace                                                 ; 92ab: 85 9e       ..
    ldy #0                                                            ; 92ad: a0 00       ..
    sty l00ad                                                         ; 92af: 84 ad       ..
    lda l0350                                                         ; 92b1: ad 50 03    .P.
    sta (nfs_workspace),y                                             ; 92b4: 91 9e       ..
    inc nfs_workspace                                                 ; 92b6: e6 9e       ..
    lda l0351                                                         ; 92b8: ad 51 03    .Q.
    pha                                                               ; 92bb: 48          H
    tya                                                               ; 92bc: 98          .              ; A=&00
; &92bd referenced 1 time by &92dc
.loop_c92bd
    sta (nfs_workspace),y                                             ; 92bd: 91 9e       ..
    ldx nfs_workspace                                                 ; 92bf: a6 9e       ..
    ldy nfs_workspace_hi                                              ; 92c1: a4 9f       ..
    lda #osword_read_palette                                          ; 92c3: a9 0b       ..
    jsr osword                                                        ; 92c5: 20 f1 ff     ..            ; Read palette
.sub_c92c8
    pla                                                               ; 92c8: 68          h
    ldy #0                                                            ; 92c9: a0 00       ..
    sta (nfs_workspace),y                                             ; 92cb: 91 9e       ..
    iny                                                               ; 92cd: c8          .              ; Y=&01
    lda (nfs_workspace),y                                             ; 92ce: b1 9e       ..
    pha                                                               ; 92d0: 48          H
    ldx nfs_workspace                                                 ; 92d1: a6 9e       ..
    inc nfs_workspace                                                 ; 92d3: e6 9e       ..
    inc l00ad                                                         ; 92d5: e6 ad       ..
    dey                                                               ; 92d7: 88          .              ; Y=&00
    lda l00ad                                                         ; 92d8: a5 ad       ..
    cpx #&f9                                                          ; 92da: e0 f9       ..
    bne loop_c92bd                                                    ; 92dc: d0 df       ..
    pla                                                               ; 92de: 68          h
    sty l00ad                                                         ; 92df: 84 ad       ..
    inc nfs_workspace                                                 ; 92e1: e6 9e       ..
    jsr save_vdu_state                                                ; 92e3: 20 f2 92     ..
    inc nfs_workspace                                                 ; 92e6: e6 9e       ..
    pla                                                               ; 92e8: 68          h
    sta l00ad                                                         ; 92e9: 85 ad       ..
; &92eb referenced 4 times by &84a0, &84c8, &84ef, &8ee6
.clear_jsr_protection
    lda saved_jsr_mask                                                ; 92eb: ad 65 0d    .e.
    sta prot_status                                                   ; 92ee: 8d 63 0d    .c.
    rts                                                               ; 92f1: 60          `

; ***************************************************************************************
; Save VDU workspace state
; 
; Stores the cursor position value from &0355 into NFS workspace,
; then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
; and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
; each result into consecutive workspace bytes.
; ***************************************************************************************
; &92f2 referenced 1 time by &92e3
.save_vdu_state
    lda l0355                                                         ; 92f2: ad 55 03    .U.
    sta (nfs_workspace),y                                             ; 92f5: 91 9e       ..
    tax                                                               ; 92f7: aa          .
    jsr read_vdu_osbyte                                               ; 92f8: 20 05 93     ..
    inc nfs_workspace                                                 ; 92fb: e6 9e       ..
    tya                                                               ; 92fd: 98          .
    sta (nfs_workspace,x)                                             ; 92fe: 81 9e       ..
    jsr read_vdu_osbyte_x0                                            ; 9300: 20 03 93     ..
; &9303 referenced 1 time by &9300
.read_vdu_osbyte_x0
    ldx #0                                                            ; 9303: a2 00       ..
; &9305 referenced 1 time by &92f8
.read_vdu_osbyte
    ldy l00ad                                                         ; 9305: a4 ad       ..
    inc l00ad                                                         ; 9307: e6 ad       ..
    inc nfs_workspace                                                 ; 9309: e6 9e       ..
    lda l9319,y                                                       ; 930b: b9 19 93    ...
    ldy #&ff                                                          ; 930e: a0 ff       ..
    jsr osbyte                                                        ; 9310: 20 f4 ff     ..
    txa                                                               ; 9313: 8a          .
    ldx #0                                                            ; 9314: a2 00       ..
    sta (nfs_workspace,x)                                             ; 9316: 81 9e       ..
    rts                                                               ; 9318: 60          `

; &9319 referenced 1 time by &930b
.l9319
    equb &85, &c2, &c3                                                ; 9319: 85 c2 c3    ...
; &931c referenced 1 time by &8175

    org &9656

    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff             ; 9656: ff ff ff... ...

; &9660 referenced 2 times by &86aa, &8ed1
.trampoline_tx_setup
    jmp c9bc7                                                         ; 9660: 4c c7 9b    L..

; &9663 referenced 1 time by &8319
.trampoline_adlc_init
    jmp adlc_init                                                     ; 9663: 4c 6f 96    Lo.

.svc_nmi_release
    jmp c96b2                                                         ; 9666: 4c b2 96    L..

.svc_nmi_claim
    jmp c968d                                                         ; 9669: 4c 8d 96    L..

.svc_unknown_irq
    jmp c9b35                                                         ; 966c: 4c 35 9b    L5.

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
    jsr adlc_full_reset                                               ; 9672: 20 d8 96     ..
    lda #osbyte_read_tube_presence                                    ; 9675: a9 ea       ..
    ldx #0                                                            ; 9677: a2 00       ..
    stx econet_init_flag                                              ; 9679: 8e 66 0d    .f.
    ldy #&ff                                                          ; 967c: a0 ff       ..
    jsr osbyte                                                        ; 967e: 20 f4 ff     ..            ; Read Tube present flag
    stx tube_flag                                                     ; 9681: 8e 67 0d    .g.            ; X=value of Tube present flag
    lda #osbyte_issue_service_request                                 ; 9684: a9 8f       ..
    ldx #&0c                                                          ; 9686: a2 0c       ..
    ldy #&ff                                                          ; 9688: a0 ff       ..
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
    jsr osbyte                                                        ; 968a: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=12 - NMI claim
; &968d referenced 1 time by &9669
.c968d
    ldy #&20 ; ' '                                                    ; 968d: a0 20       .
; &968f referenced 1 time by &9696
.loop_c968f
    lda nmi_shim_rom_src,y                                            ; 968f: b9 a7 9f    ...
    sta l0cff,y                                                       ; 9692: 99 ff 0c    ...
    dey                                                               ; 9695: 88          .
    bne loop_c968f                                                    ; 9696: d0 f7       ..
    lda romsel_copy                                                   ; 9698: a5 f4       ..
    sta nmi_shim_07                                                   ; 969a: 8d 07 0d    ...
    lda #&80                                                          ; 969d: a9 80       ..
    sta tx_clear_flag                                                 ; 969f: 8d 62 0d    .b.
    sta econet_init_flag                                              ; 96a2: 8d 66 0d    .f.
    lda station_id_disable_net_nmis                                   ; 96a5: ad 18 fe    ...
    sta tx_src_stn                                                    ; 96a8: 8d 22 0d    .".
    sty tx_src_net                                                    ; 96ab: 8c 23 0d    .#.
    bit video_ula_control                                             ; 96ae: 2c 20 fe    , .
    rts                                                               ; 96b1: 60          `

; &96b2 referenced 1 time by &9666
.c96b2
    bit econet_init_flag                                              ; 96b2: 2c 66 0d    ,f.
    bpl c96d5                                                         ; 96b5: 10 1e       ..
; &96b7 referenced 2 times by &96bc, &96c3
.c96b7
    lda nmi_jmp_lo                                                    ; 96b7: ad 0c 0d    ...
    cmp #&f2                                                          ; 96ba: c9 f2       ..
    bne c96b7                                                         ; 96bc: d0 f9       ..
    lda nmi_jmp_hi                                                    ; 96be: ad 0d 0d    ...
    cmp #&96                                                          ; 96c1: c9 96       ..
    bne c96b7                                                         ; 96c3: d0 f2       ..
    bit station_id_disable_net_nmis                                   ; 96c5: 2c 18 fe    ,..
; ***************************************************************************************
; Save Econet state to RX control block
; 
; Stores rx_status_flags, protection_mask, and tx_in_progress
; to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.
; ***************************************************************************************
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 96c8: 2c 18 fe    ,..
    lda #0                                                            ; 96cb: a9 00       ..
    sta tx_clear_flag                                                 ; 96cd: 8d 62 0d    .b.
    sta econet_init_flag                                              ; 96d0: 8d 66 0d    .f.
    ldy #5                                                            ; 96d3: a0 05       ..
; &96d5 referenced 1 time by &96b5
.c96d5
    jmp adlc_rx_listen                                                ; 96d5: 4c e7 96    L..

; ***************************************************************************************
; ADLC full reset
; 
; Aborts all activity and returns to idle RX listen mode.
; ***************************************************************************************
; &96d8 referenced 3 times by &9672, &973a, &987a
.adlc_full_reset
    lda #&c1                                                          ; 96d8: a9 c1       ..             ; CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 96da: 8d a0 fe    ...
    lda #&1e                                                          ; 96dd: a9 1e       ..
    sta econet_data_terminate_frame                                   ; 96df: 8d a3 fe    ...
    lda #0                                                            ; 96e2: a9 00       ..             ; CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 96e4: 8d a1 fe    ...
; ***************************************************************************************
; Enter RX listen mode
; 
; TX held in reset, RX active with interrupts. Clears all status.
; ***************************************************************************************
; &96e7 referenced 2 times by &96d5, &9a3d
.adlc_rx_listen
    lda #&82                                                          ; 96e7: a9 82       ..             ; CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding; CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 96e9: 8d a0 fe    ...
.sub_c96ec
l96ed = sub_c96ec+1
    lda #&67 ; 'g'                                                    ; 96ec: a9 67       .g             ; CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 96ee: 8d a1 fe    ...
    rts                                                               ; 96f1: 60          `

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
; &96f2 referenced 1 time by &9fb3
.nmi_rx_scout
    lda #1                                                            ; 96f2: a9 01       ..             ; A=&01: mask for SR2 bit0 (AP = Address Present)
    equb &2c, &a1                                                     ; 96f4: 2c a1       ,.             ; BIT SR2: Z = A AND SR2 -- tests if AP is set

.sub_c96f6
    inc l3af0,x                                                       ; 96f6: fe f0 3a    ..:
    lda econet_data_continue_frame                                    ; 96f9: ad a2 fe    ...            ; Read first RX byte (destination station address)
    cmp station_id_disable_net_nmis                                   ; 96fc: cd 18 fe    ...            ; Compare to our station ID (&FE18 read = INTOFF, disables NMIs)
    beq c970a                                                         ; 96ff: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 9701: c9 ff       ..             ; Check for broadcast address (&FF)
    bne scout_reject                                                  ; 9703: d0 1a       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 9705: a9 40       .@             ; Flag &40 = broadcast frame
    sta tx_flags                                                      ; 9707: 8d 4a 0d    .J.
; &970a referenced 1 time by &96ff
.c970a
    lda #&11                                                          ; 970a: a9 11       ..             ; Install next NMI handler at &9715 (RX scout second byte)
    ldy #&97                                                          ; 970c: a0 97       ..
    jmp set_nmi_vector                                                ; 970e: 4c 0e 0d    L..

; ***************************************************************************************
; RX scout second byte handler
; 
; Reads the second byte of an incoming scout (destination network).
; Checks for network match: 0 = local network (accept), &FF = broadcast
; (accept and flag), anything else = reject.
; Installs the scout data reading loop handler at &9747.
; ***************************************************************************************
.nmi_rx_scout_net
    bit econet_control23_or_status2                                   ; 9711: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl scout_error                                                   ; 9714: 10 1d       ..             ; No RDA -- check errors
    lda econet_data_continue_frame                                    ; 9716: ad a2 fe    ...            ; Read destination network byte
    beq c9727                                                         ; 9719: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 971b: 49 ff       I.             ; EOR &FF: test if network = &FF (broadcast)
    beq c972a                                                         ; 971d: f0 0b       ..             ; Broadcast network -- accept
; &971f referenced 1 time by &9703
.scout_reject
    lda #&a2                                                          ; 971f: a9 a2       ..             ; Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 9721: 8d a0 fe    ...
    jmp c9a40                                                         ; 9724: 4c 40 9a    L@.

; &9727 referenced 1 time by &9719
.c9727
    sta tx_flags                                                      ; 9727: 8d 4a 0d    .J.            ; Network = &FF broadcast: clear &0D4A
; &972a referenced 1 time by &971d
.c972a
    sta port_buf_len                                                  ; 972a: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #&43 ; 'C'                                                    ; 972c: a9 43       .C             ; Install scout data reading loop at &9747
    ldy #&97                                                          ; 972e: a0 97       ..
    jmp set_nmi_vector                                                ; 9730: 4c 0e 0d    L..

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
; &9733 referenced 4 times by &9714, &9748, &977c, &977e
.scout_error
    lda econet_control23_or_status2                                   ; 9733: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 9736: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 9738: f0 06       ..             ; Neither set -- clean end, discard via &9A40
    jsr adlc_full_reset                                               ; 973a: 20 d8 96     ..            ; Unexpected data/status: full ADLC reset
    jmp c9a40                                                         ; 973d: 4c 40 9a    L@.            ; Discard and return to idle

; &9740 referenced 1 time by &9738
.scout_discard
    jmp discard_listen                                                ; 9740: 4c 3d 9a    L=.

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
    ldy port_buf_len                                                  ; 9743: a4 a2       ..             ; Y = buffer offset
    lda econet_control23_or_status2                                   ; 9745: ad a1 fe    ...            ; Read SR2
; &9748 referenced 1 time by &9768
.scout_loop_rda
    bpl scout_error                                                   ; 9748: 10 e9       ..             ; No RDA -- error handler &9737
    lda econet_data_continue_frame                                    ; 974a: ad a2 fe    ...            ; Read data byte from RX FIFO
    sta rx_src_stn,y                                                  ; 974d: 99 3d 0d    .=.            ; Store at &0D3D+Y (scout buffer)
    iny                                                               ; 9750: c8          .              ; Advance buffer index
    lda econet_control23_or_status2                                   ; 9751: ad a1 fe    ...            ; Read SR2 again (FV detection point)
    bmi scout_loop_second                                             ; 9754: 30 02       0.             ; RDA set -- more data, read second byte
    bne scout_complete                                                ; 9756: d0 15       ..             ; SR2 non-zero (FV or other) -- scout completion
; &9758 referenced 1 time by &9754
.scout_loop_second
    lda econet_data_continue_frame                                    ; 9758: ad a2 fe    ...            ; Read second byte of pair
    sta rx_src_stn,y                                                  ; 975b: 99 3d 0d    .=.            ; Store at &0D3D+Y
    iny                                                               ; 975e: c8          .              ; Advance and check buffer limit
    cpy #&0c                                                          ; 975f: c0 0c       ..
    beq scout_complete                                                ; 9761: f0 0a       ..             ; Buffer full (Y=12) -- force completion
    sty port_buf_len                                                  ; 9763: 84 a2       ..
    lda econet_control23_or_status2                                   ; 9765: ad a1 fe    ...            ; Read SR2 for next pair
    bne scout_loop_rda                                                ; 9768: d0 de       ..             ; SR2 non-zero -- loop back for more bytes
    jmp nmi_rti                                                       ; 976a: 4c 14 0d    L..            ; SR2 = 0 -- RTI, wait for next NMI

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
; &976d referenced 2 times by &9756, &9761
.scout_complete
    lda #0                                                            ; 976d: a9 00       ..             ; Save Y for next iteration; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 976f: 8d a0 fe    ...
    lda #&84                                                          ; 9772: a9 84       ..             ; CR2=&84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 9774: 8d a1 fe    ...
    lda #2                                                            ; 9777: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9779: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 977c: f0 b5       ..             ; No FV -- not a valid frame end, error
    bpl scout_error                                                   ; 977e: 10 b3       ..             ; FV set but no RDA -- missing last byte, error
    lda econet_data_continue_frame                                    ; 9780: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9783: 99 3d 0d    .=.            ; Store last byte at &0D3D+Y
    lda #&44 ; 'D'                                                    ; 9786: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 9788: 8d a0 fe    ...
    lda rx_port                                                       ; 978b: ad 40 0d    .@.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 978e: d0 06       ..             ; Port non-zero -- look for matching receive block
    jmp immediate_op                                                  ; 9790: 4c 56 9a    LV.            ; Port = 0 -- immediate operation handler

; &9793 referenced 3 times by &97de, &97e3, &9801
.scout_no_match
    jmp c9872                                                         ; 9793: 4c 72 98    Lr.

; &9796 referenced 1 time by &978e
.scout_match_port
    bit tx_flags                                                      ; 9796: 2c 4a 0d    ,J.
    bvc c97a0                                                         ; 9799: 50 05       P.
    lda #7                                                            ; 979b: a9 07       ..
    sta econet_control23_or_status2                                   ; 979d: 8d a1 fe    ...
; &97a0 referenced 1 time by &9799
.c97a0
    bit rx_flags                                                      ; 97a0: 2c 64 0d    ,d.
    bpl c97e0                                                         ; 97a3: 10 3b       .;
    lda #&c0                                                          ; 97a5: a9 c0       ..
    sta port_ws_offset                                                ; 97a7: 85 a6       ..
    lda #0                                                            ; 97a9: a9 00       ..
    sta rx_buf_offset                                                 ; 97ab: 85 a7       ..
; &97ad referenced 1 time by &97da
.c97ad
    ldy #0                                                            ; 97ad: a0 00       ..
; &97af referenced 1 time by &97ed
.c97af
    lda (port_ws_offset),y                                            ; 97af: b1 a6       ..
    beq c97dc                                                         ; 97b1: f0 29       .)
    cmp #&7f                                                          ; 97b3: c9 7f       ..
    bne c97d3                                                         ; 97b5: d0 1c       ..
    iny                                                               ; 97b7: c8          .
    lda (port_ws_offset),y                                            ; 97b8: b1 a6       ..
    beq c97c1                                                         ; 97ba: f0 05       ..
    cmp rx_port                                                       ; 97bc: cd 40 0d    .@.
    bne c97d3                                                         ; 97bf: d0 12       ..
; &97c1 referenced 1 time by &97ba
.c97c1
    iny                                                               ; 97c1: c8          .
    lda (port_ws_offset),y                                            ; 97c2: b1 a6       ..
    beq c97cb                                                         ; 97c4: f0 05       ..
    cmp rx_src_stn                                                    ; 97c6: cd 3d 0d    .=.
    bne c97d3                                                         ; 97c9: d0 08       ..
; &97cb referenced 1 time by &97c4
.c97cb
    iny                                                               ; 97cb: c8          .
    lda (port_ws_offset),y                                            ; 97cc: b1 a6       ..
    cmp rx_src_net                                                    ; 97ce: cd 3e 0d    .>.
    beq c97ef                                                         ; 97d1: f0 1c       ..
; &97d3 referenced 3 times by &97b5, &97bf, &97c9
.c97d3
    lda port_ws_offset                                                ; 97d3: a5 a6       ..
    clc                                                               ; 97d5: 18          .
    adc #&0c                                                          ; 97d6: 69 0c       i.
    sta port_ws_offset                                                ; 97d8: 85 a6       ..
    bcc c97ad                                                         ; 97da: 90 d1       ..
; &97dc referenced 1 time by &97b1
.c97dc
    lda rx_buf_offset                                                 ; 97dc: a5 a7       ..
    bne scout_no_match                                                ; 97de: d0 b3       ..
; &97e0 referenced 1 time by &97a3
.c97e0
    bit rx_flags                                                      ; 97e0: 2c 64 0d    ,d.
    bvc scout_no_match                                                ; 97e3: 50 ae       P.
    lda nfs_workspace_hi                                              ; 97e5: a5 9f       ..
    sta rx_buf_offset                                                 ; 97e7: 85 a7       ..
    ldy #0                                                            ; 97e9: a0 00       ..
    sty port_ws_offset                                                ; 97eb: 84 a6       ..
    beq c97af                                                         ; 97ed: f0 c0       ..             ; ALWAYS branch

; &97ef referenced 1 time by &97d1
.c97ef
    bit tx_flags                                                      ; 97ef: 2c 4a 0d    ,J.
    bvc c97f7                                                         ; 97f2: 50 03       P.
    jmp c9a47                                                         ; 97f4: 4c 47 9a    LG.

; &97f7 referenced 2 times by &97f2, &9abb
.c97f7
    lda #3                                                            ; 97f7: a9 03       ..
    sta scout_status                                                  ; 97f9: 8d 5c 0d    .\.
    jsr tx_calc_transfer                                              ; 97fc: 20 38 9f     8.
    bcs c9804                                                         ; 97ff: b0 03       ..
    jmp scout_no_match                                                ; 9801: 4c 93 97    L..

; &9804 referenced 2 times by &97ff, &9ab0
.c9804
    lda #&44 ; 'D'                                                    ; 9804: a9 44       .D
    sta econet_control1_or_status1                                    ; 9806: 8d a0 fe    ...
    lda #&a7                                                          ; 9809: a9 a7       ..
    sta econet_control23_or_status2                                   ; 980b: 8d a1 fe    ...
    lda #&15                                                          ; 980e: a9 15       ..
    ldy #&98                                                          ; 9810: a0 98       ..
    jmp ack_tx_write_dest                                             ; 9812: 4c 5d 99    L].

.data_rx_setup
    lda #&82                                                          ; 9815: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 9817: 8d a0 fe    ...
    lda #&21 ; '!'                                                    ; 981a: a9 21       .!
    ldy #&98                                                          ; 981c: a0 98       ..
    jmp set_nmi_vector                                                ; 981e: 4c 0e 0d    L..

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
    lda #1                                                            ; 9821: a9 01       ..             ; Read SR2 for AP check
    bit econet_control23_or_status2                                   ; 9823: 2c a1 fe    ,..
    beq c9872                                                         ; 9826: f0 4a       .J
    lda econet_data_continue_frame                                    ; 9828: ad a2 fe    ...
    cmp station_id_disable_net_nmis                                   ; 982b: cd 18 fe    ...
    bne c9872                                                         ; 982e: d0 42       .B
    lda #&37 ; '7'                                                    ; 9830: a9 37       .7
    ldy #&98                                                          ; 9832: a0 98       ..
    jmp set_nmi_vector                                                ; 9834: 4c 0e 0d    L..

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 9837: 2c a1 fe    ,..            ; Validate source network = 0
    bpl c9872                                                         ; 983a: 10 36       .6
    lda econet_data_continue_frame                                    ; 983c: ad a2 fe    ...
    bne c9872                                                         ; 983f: d0 31       .1
    lda #&4d ; 'M'                                                    ; 9841: a9 4d       .M
    ldy #&98                                                          ; 9843: a0 98       ..
    bit econet_control1_or_status1                                    ; 9845: 2c a0 fe    ,..
    bmi nmi_data_rx_skip                                              ; 9848: 30 03       0.
    jmp set_nmi_vector                                                ; 984a: 4c 0e 0d    L..

; &984d referenced 1 time by &9848
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 984d: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl c9872                                                         ; 9850: 10 20       .
    lda econet_data_continue_frame                                    ; 9852: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 9855: ad a2 fe    ...            ; Discard port byte
; &9858 referenced 1 time by &9f0c
.c9858
    lda #2                                                            ; 9858: a9 02       ..
    bit tx_flags                                                      ; 985a: 2c 4a 0d    ,J.
    bne c986b                                                         ; 985d: d0 0c       ..
    lda #&80                                                          ; 985f: a9 80       ..
    ldy #&98                                                          ; 9861: a0 98       ..
    bit econet_control1_or_status1                                    ; 9863: 2c a0 fe    ,..
    bmi nmi_data_rx_bulk                                              ; 9866: 30 18       0.
    jmp set_nmi_vector                                                ; 9868: 4c 0e 0d    L..

; &986b referenced 1 time by &985d
.c986b
    lda #&dd                                                          ; 986b: a9 dd       ..
    ldy #&98                                                          ; 986d: a0 98       ..
    jmp set_nmi_vector                                                ; 986f: 4c 0e 0d    L..

; &9872 referenced 12 times by &9793, &9826, &982e, &983a, &983f, &9850, &9893, &98c5, &98cb, &9916, &99a1, &9a82
.c9872
    lda tx_flags                                                      ; 9872: ad 4a 0d    .J.
    bpl rx_error                                                      ; 9875: 10 03       ..
    jmp tx_result_fail                                                ; 9877: 4c 1a 9f    L..

; &987a referenced 1 time by &9875
.rx_error
.rx_error_reset
    jsr adlc_full_reset                                               ; 987a: 20 d8 96     ..
    jmp discard_reset_listen                                          ; 987d: 4c 2e 9a    L..

; ***************************************************************************************
; Data frame bulk read loop
; 
; Reads data payload bytes from the RX FIFO and stores them into
; the open port buffer at (open_port_buf),Y. Reads bytes in pairs
; (like the scout data loop), checking SR2 between each pair.
; SR2 non-zero (FV or other) -> frame completion at &98D8.
; SR2 = 0 -> RTI, wait for next NMI to continue.
; ***************************************************************************************
; &9880 referenced 1 time by &9866
.nmi_data_rx_bulk
    ldy port_buf_len                                                  ; 9880: a4 a2       ..             ; Y = buffer offset, resume from last position
    lda econet_control23_or_status2                                   ; 9882: ad a1 fe    ...            ; Read SR2 for next pair
; &9885 referenced 1 time by &98af
.c9885
    bpl data_rx_complete                                              ; 9885: 10 2d       .-
    lda econet_data_continue_frame                                    ; 9887: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 988a: 91 a4       ..
    iny                                                               ; 988c: c8          .
    bne c9895                                                         ; 988d: d0 06       ..
    inc open_port_buf_hi                                              ; 988f: e6 a5       ..
    dec port_buf_len_hi                                               ; 9891: c6 a3       ..
    beq c9872                                                         ; 9893: f0 dd       ..
; &9895 referenced 1 time by &988d
.c9895
    lda econet_control23_or_status2                                   ; 9895: ad a1 fe    ...
    bmi c989c                                                         ; 9898: 30 02       0.
    bne data_rx_complete                                              ; 989a: d0 18       ..
; &989c referenced 1 time by &9898
.c989c
    lda econet_data_continue_frame                                    ; 989c: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 989f: 91 a4       ..
    iny                                                               ; 98a1: c8          .
    sty port_buf_len                                                  ; 98a2: 84 a2       ..
    bne c98ac                                                         ; 98a4: d0 06       ..
    inc open_port_buf_hi                                              ; 98a6: e6 a5       ..
    dec port_buf_len_hi                                               ; 98a8: c6 a3       ..
    beq data_rx_complete                                              ; 98aa: f0 08       ..
; &98ac referenced 1 time by &98a4
.c98ac
    lda econet_control23_or_status2                                   ; 98ac: ad a1 fe    ...
    bne c9885                                                         ; 98af: d0 d4       ..
    jmp nmi_rti                                                       ; 98b1: 4c 14 0d    L..

; ***************************************************************************************
; Data frame completion
; 
; Reached when SR2 non-zero during data RX (FV detected).
; Same pattern as scout completion (&977B): disables PSE (CR1=&00,
; CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
; If extra data available and buffer space remains, stores it.
; Proceeds to send the final ACK via &9968.
; ***************************************************************************************
; &98b4 referenced 3 times by &9885, &989a, &98aa
.data_rx_complete
    lda #0                                                            ; 98b4: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 98b6: 8d a0 fe    ...
    lda #&84                                                          ; 98b9: a9 84       ..             ; CR2=&84: disable PSE for individual bit testing
    sta econet_control23_or_status2                                   ; 98bb: 8d a1 fe    ...
    sty port_buf_len                                                  ; 98be: 84 a2       ..
    lda #2                                                            ; 98c0: a9 02       ..             ; A=&02: FV mask
    bit econet_control23_or_status2                                   ; 98c2: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq c9872                                                         ; 98c5: f0 ab       ..             ; No FV -- error
    bpl c98da                                                         ; 98c7: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 98c9: a5 a3       ..
    beq c9872                                                         ; 98cb: f0 a5       ..
    lda econet_data_continue_frame                                    ; 98cd: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 98d0: a4 a2       ..
    sta (open_port_buf),y                                             ; 98d2: 91 a4       ..
    inc port_buf_len                                                  ; 98d4: e6 a2       ..
    bne c98da                                                         ; 98d6: d0 02       ..
    inc open_port_buf_hi                                              ; 98d8: e6 a5       ..
; &98da referenced 2 times by &98c7, &98d6
.c98da
    jmp ack_tx                                                        ; 98da: 4c 44 99    LD.

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 98dd: ad a1 fe    ...
; &98e0 referenced 1 time by &9911
.c98e0
    bpl data_rx_tube_complete                                         ; 98e0: 10 37       .7
    lda econet_data_continue_frame                                    ; 98e2: ad a2 fe    ...
    inc port_buf_len                                                  ; 98e5: e6 a2       ..
    sta tube_data_register_3                                          ; 98e7: 8d e5 fe    ...
    bne c98f8                                                         ; 98ea: d0 0c       ..
    inc port_buf_len_hi                                               ; 98ec: e6 a3       ..
    bne c98f8                                                         ; 98ee: d0 08       ..
    inc open_port_buf                                                 ; 98f0: e6 a4       ..
    bne c98f8                                                         ; 98f2: d0 04       ..
    inc open_port_buf_hi                                              ; 98f4: e6 a5       ..
    beq data_rx_tube_error                                            ; 98f6: f0 1e       ..
; &98f8 referenced 3 times by &98ea, &98ee, &98f2
.c98f8
    lda econet_data_continue_frame                                    ; 98f8: ad a2 fe    ...
    sta tube_data_register_3                                          ; 98fb: 8d e5 fe    ...
    inc port_buf_len                                                  ; 98fe: e6 a2       ..
    bne c990e                                                         ; 9900: d0 0c       ..
    inc port_buf_len_hi                                               ; 9902: e6 a3       ..
    bne c990e                                                         ; 9904: d0 08       ..
    inc open_port_buf                                                 ; 9906: e6 a4       ..
    bne c990e                                                         ; 9908: d0 04       ..
    inc open_port_buf_hi                                              ; 990a: e6 a5       ..
    beq data_rx_tube_complete                                         ; 990c: f0 0b       ..
; &990e referenced 3 times by &9900, &9904, &9908
.c990e
    lda econet_control23_or_status2                                   ; 990e: ad a1 fe    ...
    bne c98e0                                                         ; 9911: d0 cd       ..
    jmp nmi_rti                                                       ; 9913: 4c 14 0d    L..

; &9916 referenced 3 times by &98f6, &9928, &9934
.data_rx_tube_error
    jmp c9872                                                         ; 9916: 4c 72 98    Lr.

; &9919 referenced 2 times by &98e0, &990c
.data_rx_tube_complete
    lda #0                                                            ; 9919: a9 00       ..
    sta econet_control1_or_status1                                    ; 991b: 8d a0 fe    ...
    lda #&84                                                          ; 991e: a9 84       ..
    sta econet_control23_or_status2                                   ; 9920: 8d a1 fe    ...
    lda #2                                                            ; 9923: a9 02       ..
    bit econet_control23_or_status2                                   ; 9925: 2c a1 fe    ,..
    beq data_rx_tube_error                                            ; 9928: f0 ec       ..
    bpl ack_tx                                                        ; 992a: 10 18       ..
    lda port_buf_len                                                  ; 992c: a5 a2       ..
    ora port_buf_len_hi                                               ; 992e: 05 a3       ..
    ora open_port_buf                                                 ; 9930: 05 a4       ..
    ora open_port_buf_hi                                              ; 9932: 05 a5       ..
    beq data_rx_tube_error                                            ; 9934: f0 e0       ..
    lda econet_data_continue_frame                                    ; 9936: ad a2 fe    ...
    sta rx_extra_byte                                                 ; 9939: 8d 5d 0d    .].
    lda #&20 ; ' '                                                    ; 993c: a9 20       .
    ora tx_flags                                                      ; 993e: 0d 4a 0d    .J.
    sta tx_flags                                                      ; 9941: 8d 4a 0d    .J.
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
; &9944 referenced 2 times by &98da, &992a
.ack_tx
    lda tx_flags                                                      ; 9944: ad 4a 0d    .J.
    bpl ack_tx_configure                                              ; 9947: 10 06       ..
    jsr sub_c99a4                                                     ; 9949: 20 a4 99     ..
    jmp tx_result_ok                                                  ; 994c: 4c 16 9f    L..

; &994f referenced 1 time by &9947
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 994f: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 9951: 8d a0 fe    ...
    lda #&a7                                                          ; 9954: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9956: 8d a1 fe    ...
    lda #&e8                                                          ; 9959: a9 e8       ..             ; Install saved next handler (&99BB for scout ACK)
    ldy #&99                                                          ; 995b: a0 99       ..
; &995d referenced 2 times by &9812, &9af9
.ack_tx_write_dest
    sta nmi_next_lo                                                   ; 995d: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 9960: 8c 4c 0d    .L.
    lda rx_src_stn                                                    ; 9963: ad 3d 0d    .=.            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 9966: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc c99a1                                                         ; 9969: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 996b: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda rx_src_net                                                    ; 996e: ad 3e 0d    .>.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9971: 8d a2 fe    ...
    lda #&7b ; '{'                                                    ; 9974: a9 7b       .{             ; Install handler at &9992 (write src addr)
    ldy #&99                                                          ; 9976: a0 99       ..
    jmp set_nmi_vector                                                ; 9978: 4c 0e 0d    L..

; ***************************************************************************************
; ACK TX continuation
; 
; Writes source station and network to TX FIFO, completing the 4-byte
; ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 997b: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 997e: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc c99a1                                                         ; 9981: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9983: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9986: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 9988: 8d a2 fe    ...
    lda tx_flags                                                      ; 998b: ad 4a 0d    .J.
    bmi c999e                                                         ; 998e: 30 0e       0.
    lda #&3f ; '?'                                                    ; 9990: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
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
    sta econet_control23_or_status2                                   ; 9992: 8d a1 fe    ...
    lda nmi_next_lo                                                   ; 9995: ad 4b 0d    .K.            ; Install saved handler from &0D4B/&0D4C
    ldy nmi_next_hi                                                   ; 9998: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 999b: 4c 0e 0d    L..

; &999e referenced 1 time by &998e
.c999e
    jmp data_tx_begin                                                 ; 999e: 4c 1a 9e    L..

; &99a1 referenced 2 times by &9969, &9981
.c99a1
    jmp c9872                                                         ; 99a1: 4c 72 98    Lr.

; &99a4 referenced 2 times by &9949, &99f7
.sub_c99a4
    lda #2                                                            ; 99a4: a9 02       ..
    bit tx_flags                                                      ; 99a6: 2c 4a 0d    ,J.
    beq return_10                                                     ; 99a9: f0 3c       .<
    clc                                                               ; 99ab: 18          .
    php                                                               ; 99ac: 08          .
    ldy #8                                                            ; 99ad: a0 08       ..
; &99af referenced 1 time by &99bb
.loop_c99af
    lda (port_ws_offset),y                                            ; 99af: b1 a6       ..
    plp                                                               ; 99b1: 28          (
    adc net_tx_ptr,y                                                  ; 99b2: 79 9a 00    y..
    sta (port_ws_offset),y                                            ; 99b5: 91 a6       ..
    iny                                                               ; 99b7: c8          .
    php                                                               ; 99b8: 08          .
    cpy #&0c                                                          ; 99b9: c0 0c       ..
    bcc loop_c99af                                                    ; 99bb: 90 f2       ..
    plp                                                               ; 99bd: 28          (
    lda #&20 ; ' '                                                    ; 99be: a9 20       .
    bit tx_flags                                                      ; 99c0: 2c 4a 0d    ,J.
    beq c99e5                                                         ; 99c3: f0 20       .
    txa                                                               ; 99c5: 8a          .
    pha                                                               ; 99c6: 48          H
    lda #8                                                            ; 99c7: a9 08       ..
    clc                                                               ; 99c9: 18          .
    adc port_ws_offset                                                ; 99ca: 65 a6       e.
    tax                                                               ; 99cc: aa          .
    ldy rx_buf_offset                                                 ; 99cd: a4 a7       ..
    lda #1                                                            ; 99cf: a9 01       ..
    jsr tube_addr_claim                                               ; 99d1: 20 06 04     ..
    lda rx_extra_byte                                                 ; 99d4: ad 5d 0d    .].
    sta tube_data_register_3                                          ; 99d7: 8d e5 fe    ...
    pla                                                               ; 99da: 68          h
    tax                                                               ; 99db: aa          .
    ldy #8                                                            ; 99dc: a0 08       ..
    lda (port_ws_offset),y                                            ; 99de: b1 a6       ..
    sec                                                               ; 99e0: 38          8
    adc #0                                                            ; 99e1: 69 00       i.
    sta (port_ws_offset),y                                            ; 99e3: 91 a6       ..
; &99e5 referenced 1 time by &99c3
.c99e5
    lda #&ff                                                          ; 99e5: a9 ff       ..
; &99e7 referenced 1 time by &99a9
.return_10
    rts                                                               ; 99e7: 60          `

    lda rx_port                                                       ; 99e8: ad 40 0d    .@.
    bne c99f7                                                         ; 99eb: d0 0a       ..
    ldy rx_ctrl                                                       ; 99ed: ac 3f 0d    .?.
    cpy #&82                                                          ; 99f0: c0 82       ..
    beq c99f7                                                         ; 99f2: f0 03       ..
    jmp c9afc                                                         ; 99f4: 4c fc 9a    L..

; &99f7 referenced 2 times by &99eb, &99f2
.c99f7
    jsr sub_c99a4                                                     ; 99f7: 20 a4 99     ..
    bne c9a0e                                                         ; 99fa: d0 12       ..
    lda port_buf_len                                                  ; 99fc: a5 a2       ..
    clc                                                               ; 99fe: 18          .
    adc open_port_buf                                                 ; 99ff: 65 a4       e.
    bcc c9a05                                                         ; 9a01: 90 02       ..
.sub_c9a03
l9a04 = sub_c9a03+1
    inc open_port_buf_hi                                              ; 9a03: e6 a5       ..
; &9a04 referenced 1 time by &9a7d
; &9a05 referenced 1 time by &9a01
.c9a05
    ldy #8                                                            ; 9a05: a0 08       ..
    sta (port_ws_offset),y                                            ; 9a07: 91 a6       ..
    iny                                                               ; 9a09: c8          .              ; Y=&09
    lda open_port_buf_hi                                              ; 9a0a: a5 a5       ..
; &9a0c referenced 1 time by &9a79
.c9a0c
    sta (port_ws_offset),y                                            ; 9a0c: 91 a6       ..
; &9a0e referenced 2 times by &99fa, &9a53
.c9a0e
    lda rx_port                                                       ; 9a0e: ad 40 0d    .@.
    beq discard_reset_listen                                          ; 9a11: f0 1b       ..
    lda rx_src_net                                                    ; 9a13: ad 3e 0d    .>.
    ldy #3                                                            ; 9a16: a0 03       ..
    sta (port_ws_offset),y                                            ; 9a18: 91 a6       ..
    dey                                                               ; 9a1a: 88          .              ; Y=&02
    lda rx_src_stn                                                    ; 9a1b: ad 3d 0d    .=.
    sta (port_ws_offset),y                                            ; 9a1e: 91 a6       ..
    dey                                                               ; 9a20: 88          .              ; Y=&01
    lda rx_port                                                       ; 9a21: ad 40 0d    .@.
    sta (port_ws_offset),y                                            ; 9a24: 91 a6       ..
    dey                                                               ; 9a26: 88          .              ; Y=&00
    lda rx_ctrl                                                       ; 9a27: ad 3f 0d    .?.
    ora #&80                                                          ; 9a2a: 09 80       ..
    sta (port_ws_offset),y                                            ; 9a2c: 91 a6       ..
; ***************************************************************************************
; Discard with full ADLC reset
; 
; Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
; then falls through to discard_after_reset. Used when the ADLC is
; in an unexpected state and needs a hard reset before returning
; to idle listen mode. 5 references — the main error recovery path.
; ***************************************************************************************
; &9a2e referenced 4 times by &987d, &9a11, &9e72, &9f25
.discard_reset_listen
    lda #2                                                            ; 9a2e: a9 02       ..
    and tube_flag                                                     ; 9a30: 2d 67 0d    -g.
    bit tx_flags                                                      ; 9a33: 2c 4a 0d    ,J.
    beq discard_listen                                                ; 9a36: f0 05       ..
    lda #&82                                                          ; 9a38: a9 82       ..
    jsr tube_addr_claim                                               ; 9a3a: 20 06 04     ..
; ***************************************************************************************
; Discard frame (gentle)
; 
; Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
; current frame reception without a full reset, then falls through
; to discard_after_reset. Used for clean rejection of frames that
; are correctly formatted but not for us (wrong station/network).
; ***************************************************************************************
; &9a3d referenced 3 times by &9740, &9a36, &9b32
.discard_listen
    jsr adlc_rx_listen                                                ; 9a3d: 20 e7 96     ..
; &9a40 referenced 2 times by &9724, &973d
.c9a40
    lda #&f2                                                          ; 9a40: a9 f2       ..
    ldy #&96                                                          ; 9a42: a0 96       ..
    jmp set_nmi_vector                                                ; 9a44: 4c 0e 0d    L..

; &9a47 referenced 1 time by &97f4
.c9a47
    ldy #4                                                            ; 9a47: a0 04       ..
; &9a49 referenced 1 time by &9a51
.loop_c9a49
    lda rx_src_stn,y                                                  ; 9a49: b9 3d 0d    .=.
    sta (port_ws_offset),y                                            ; 9a4c: 91 a6       ..
    iny                                                               ; 9a4e: c8          .
    cpy #&0c                                                          ; 9a4f: c0 0c       ..
    bne loop_c9a49                                                    ; 9a51: d0 f6       ..
    jmp c9a0e                                                         ; 9a53: 4c 0e 9a    L..

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
; &9a56 referenced 1 time by &9790
.immediate_op
.discard_after_reset
    ldy rx_ctrl                                                       ; 9a56: ac 3f 0d    .?.
    cpy #&81                                                          ; 9a59: c0 81       ..
    bcc c9a82                                                         ; 9a5b: 90 25       .%
    cpy #&89                                                          ; 9a5d: c0 89       ..
    bcs c9a82                                                         ; 9a5f: b0 21       .!
    cpy #&87                                                          ; 9a61: c0 87       ..
    bcs c9a76                                                         ; 9a63: b0 11       ..
    tya                                                               ; 9a65: 98          .
    sec                                                               ; 9a66: 38          8
    sbc #&81                                                          ; 9a67: e9 81       ..
    tay                                                               ; 9a69: a8          .
    lda prot_status                                                   ; 9a6a: ad 63 0d    .c.
; &9a6d referenced 1 time by &9a6f
.loop_c9a6d
    ror a                                                             ; 9a6d: 6a          j
    dey                                                               ; 9a6e: 88          .
    bpl loop_c9a6d                                                    ; 9a6f: 10 fc       ..
    bcc c9a76                                                         ; 9a71: 90 03       ..
    jmp c9b32                                                         ; 9a73: 4c 32 9b    L2.

; &9a76 referenced 2 times by &9a63, &9a71
.c9a76
    ldy rx_ctrl                                                       ; 9a76: ac 3f 0d    .?.
    lda c9a0c,y                                                       ; 9a79: b9 0c 9a    ...
    pha                                                               ; 9a7c: 48          H
    lda l9a04,y                                                       ; 9a7d: b9 04 9a    ...
    pha                                                               ; 9a80: 48          H
    rts                                                               ; 9a81: 60          `

; &9a82 referenced 2 times by &9a5b, &9a5f
.c9a82
    jmp c9872                                                         ; 9a82: 4c 72 98    Lr.

    equb <(sub_c9ad1-1)                                               ; 9a85: d0          .
    equb <(rx_imm_poke-1)                                             ; 9a86: b2          .
    equb <(rx_imm_exec-1)                                             ; 9a87: 94          .
    equb <(rx_imm_exec-1)                                             ; 9a88: 94          .
    equb <(rx_imm_exec-1)                                             ; 9a89: 94          .
    equb <(sub_c9aeb-1)                                               ; 9a8a: ea          .
    equb <(sub_c9aeb-1)                                               ; 9a8b: ea          .
    equb <(rx_imm_machine_type-1)                                     ; 9a8c: bd          .
    equb >(sub_c9ad1-1)                                               ; 9a8d: 9a          .
    equb >(rx_imm_poke-1)                                             ; 9a8e: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a8f: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a90: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a91: 9a          .
    equb >(sub_c9aeb-1)                                               ; 9a92: 9a          .
    equb >(sub_c9aeb-1)                                               ; 9a93: 9a          .
    equb >(rx_imm_machine_type-1)                                     ; 9a94: 9a          .

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
    lda #0                                                            ; 9a95: a9 00       ..
    sta open_port_buf                                                 ; 9a97: 85 a4       ..
    lda #&82                                                          ; 9a99: a9 82       ..
    sta port_buf_len                                                  ; 9a9b: 85 a2       ..
    lda #1                                                            ; 9a9d: a9 01       ..
    sta port_buf_len_hi                                               ; 9a9f: 85 a3       ..
    lda net_rx_ptr_hi                                                 ; 9aa1: a5 9d       ..
    sta open_port_buf_hi                                              ; 9aa3: 85 a5       ..
    ldy #3                                                            ; 9aa5: a0 03       ..
; &9aa7 referenced 1 time by &9aae
.loop_c9aa7
    lda rx_remote_addr,y                                              ; 9aa7: b9 41 0d    .A.
    sta l0d58,y                                                       ; 9aaa: 99 58 0d    .X.
    dey                                                               ; 9aad: 88          .
    bpl loop_c9aa7                                                    ; 9aae: 10 f7       ..
    jmp c9804                                                         ; 9ab0: 4c 04 98    L..

; ***************************************************************************************
; RX immediate: POKE setup
; 
; Sets up workspace offsets for receiving POKE data.
; port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
; the common data-receive path at c9805.
; ***************************************************************************************
.rx_imm_poke
    lda #&3d ; '='                                                    ; 9ab3: a9 3d       .=
    sta port_ws_offset                                                ; 9ab5: 85 a6       ..
    lda #&0d                                                          ; 9ab7: a9 0d       ..
    sta rx_buf_offset                                                 ; 9ab9: 85 a7       ..
    jmp c97f7                                                         ; 9abb: 4c f7 97    L..

; ***************************************************************************************
; RX immediate: machine type query
; 
; Sets up a buffer at &7F21 (length #&01FC) for the machine
; type query response, then jumps to the query handler at
; c9b0f. Returns system identification data to the remote
; station.
; ***************************************************************************************
.rx_imm_machine_type
    lda #1                                                            ; 9abe: a9 01       ..
    sta port_buf_len_hi                                               ; 9ac0: 85 a3       ..
    lda #&fc                                                          ; 9ac2: a9 fc       ..
    sta port_buf_len                                                  ; 9ac4: 85 a2       ..
    lda #&25 ; '%'                                                    ; 9ac6: a9 25       .%
    sta open_port_buf                                                 ; 9ac8: 85 a4       ..
    lda #&7f                                                          ; 9aca: a9 7f       ..
    sta open_port_buf_hi                                              ; 9acc: 85 a5       ..
    jmp c9ae3                                                         ; 9ace: 4c e3 9a    L..

.sub_c9ad1
    lda #&3d ; '='                                                    ; 9ad1: a9 3d       .=
    sta port_ws_offset                                                ; 9ad3: 85 a6       ..
    lda #&0d                                                          ; 9ad5: a9 0d       ..
    sta rx_buf_offset                                                 ; 9ad7: 85 a7       ..
    lda #2                                                            ; 9ad9: a9 02       ..
    sta scout_status                                                  ; 9adb: 8d 5c 0d    .\.
    jsr tx_calc_transfer                                              ; 9ade: 20 38 9f     8.
    bcc c9b32                                                         ; 9ae1: 90 4f       .O
; &9ae3 referenced 1 time by &9ace
.c9ae3
    lda tx_flags                                                      ; 9ae3: ad 4a 0d    .J.
    ora #&80                                                          ; 9ae6: 09 80       ..
    sta tx_flags                                                      ; 9ae8: 8d 4a 0d    .J.
.sub_c9aeb
    lda #&44 ; 'D'                                                    ; 9aeb: a9 44       .D
    sta econet_control1_or_status1                                    ; 9aed: 8d a0 fe    ...
.sub_c9af0
l9af1 = sub_c9af0+1
    lda #&a7                                                          ; 9af0: a9 a7       ..
; &9af1 referenced 1 time by &9b6f
    sta econet_control23_or_status2                                   ; 9af2: 8d a1 fe    ...
.sub_c9af5
l9af6 = sub_c9af5+1
    lda #&12                                                          ; 9af5: a9 12       ..
; &9af6 referenced 1 time by &9b6b
    ldy #&9b                                                          ; 9af7: a0 9b       ..
    jmp ack_tx_write_dest                                             ; 9af9: 4c 5d 99    L].

; &9afc referenced 1 time by &99f4
.c9afc
    lda port_buf_len                                                  ; 9afc: a5 a2       ..
    clc                                                               ; 9afe: 18          .
    adc #&80                                                          ; 9aff: 69 80       i.
    ldy #&7f                                                          ; 9b01: a0 7f       ..
    sta (net_rx_ptr),y                                                ; 9b03: 91 9c       ..
    ldy #&80                                                          ; 9b05: a0 80       ..
    lda rx_src_stn                                                    ; 9b07: ad 3d 0d    .=.
    sta (net_rx_ptr),y                                                ; 9b0a: 91 9c       ..
    iny                                                               ; 9b0c: c8          .              ; Y=&81
    lda rx_src_net                                                    ; 9b0d: ad 3e 0d    .>.
    sta (net_rx_ptr),y                                                ; 9b10: 91 9c       ..
    lda rx_ctrl                                                       ; 9b12: ad 3f 0d    .?.
    sta tx_work_57                                                    ; 9b15: 8d 57 0d    .W.
    lda #&84                                                          ; 9b18: a9 84       ..
    sta system_via_ier                                                ; 9b1a: 8d 4e fe    .N.
    lda system_via_acr                                                ; 9b1d: ad 4b fe    .K.
    and #&1c                                                          ; 9b20: 29 1c       ).
    sta tx_work_51                                                    ; 9b22: 8d 51 0d    .Q.
    lda system_via_acr                                                ; 9b25: ad 4b fe    .K.
    and #&e3                                                          ; 9b28: 29 e3       ).
    ora #8                                                            ; 9b2a: 09 08       ..
    sta system_via_acr                                                ; 9b2c: 8d 4b fe    .K.
    bit system_via_sr                                                 ; 9b2f: 2c 4a fe    ,J.
; &9b32 referenced 2 times by &9a73, &9ae1
.c9b32
    jmp discard_listen                                                ; 9b32: 4c 3d 9a    L=.

; &9b35 referenced 1 time by &966c
.c9b35
    lda #4                                                            ; 9b35: a9 04       ..
    bit system_via_ifr                                                ; 9b37: 2c 4d fe    ,M.
    bne c9b3f                                                         ; 9b3a: d0 03       ..
    lda #5                                                            ; 9b3c: a9 05       ..
    rts                                                               ; 9b3e: 60          `

; &9b3f referenced 1 time by &9b3a
.c9b3f
    txa                                                               ; 9b3f: 8a          .
    pha                                                               ; 9b40: 48          H
    tya                                                               ; 9b41: 98          .
    pha                                                               ; 9b42: 48          H
    lda system_via_acr                                                ; 9b43: ad 4b fe    .K.
    and #&e3                                                          ; 9b46: 29 e3       ).
    ora tx_work_51                                                    ; 9b48: 0d 51 0d    .Q.
    sta system_via_acr                                                ; 9b4b: 8d 4b fe    .K.
    lda system_via_sr                                                 ; 9b4e: ad 4a fe    .J.
    lda #4                                                            ; 9b51: a9 04       ..
    sta system_via_ifr                                                ; 9b53: 8d 4d fe    .M.
    sta system_via_ier                                                ; 9b56: 8d 4e fe    .N.
    ldy tx_work_57                                                    ; 9b59: ac 57 0d    .W.
    cpy #&86                                                          ; 9b5c: c0 86       ..
    bcs c9b6b                                                         ; 9b5e: b0 0b       ..
    lda prot_status                                                   ; 9b60: ad 63 0d    .c.
    sta saved_jsr_mask                                                ; 9b63: 8d 65 0d    .e.
    ora #&1c                                                          ; 9b66: 09 1c       ..
    sta prot_status                                                   ; 9b68: 8d 63 0d    .c.
; &9b6b referenced 1 time by &9b5e
.c9b6b
    lda l9af6,y                                                       ; 9b6b: b9 f6 9a    ...
    pha                                                               ; 9b6e: 48          H
    lda l9af1,y                                                       ; 9b6f: b9 f1 9a    ...
    pha                                                               ; 9b72: 48          H
    rts                                                               ; 9b73: 60          `

    equb <(tx_done_jsr-1)                                             ; 9b74: 7d          }
    equb <(tx_done_user_proc-1)                                       ; 9b75: 86          .
    equb <(tx_done_os_proc-1)                                         ; 9b76: 94          .
    equb <(tx_done_halt-1)                                            ; 9b77: a0          .
    equb <(tx_done_continue-1)                                        ; 9b78: b7          .
    equb >(tx_done_jsr-1)                                             ; 9b79: 9b          .
    equb >(tx_done_user_proc-1)                                       ; 9b7a: 9b          .
    equb >(tx_done_os_proc-1)                                         ; 9b7b: 9b          .
    equb >(tx_done_halt-1)                                            ; 9b7c: 9b          .
    equb >(tx_done_continue-1)                                        ; 9b7d: 9b          .

; ***************************************************************************************
; TX done: remote JSR execution
; 
; Pushes address &9BEB on the stack (so RTS returns to
; tx_done_exit), then does JMP (l0d58) to call the remote
; JSR target routine. When that routine returns via RTS,
; control resumes at tx_done_exit.
; ***************************************************************************************
.tx_done_jsr
    lda #&9b                                                          ; 9b7e: a9 9b       ..
    pha                                                               ; 9b80: 48          H
    lda #&bf                                                          ; 9b81: a9 bf       ..
    pha                                                               ; 9b83: 48          H
    jmp (l0d58)                                                       ; 9b84: 6c 58 0d    lX.

; ***************************************************************************************
; TX done: UserProc event
; 
; Generates a network event (event 8) via OSEVEN with
; X=l0d58, A=l0d59 (the remote address). This notifies
; the user program that a UserProc operation has completed.
; ***************************************************************************************
.tx_done_user_proc
    ldy #event_network_error                                          ; 9b87: a0 08       ..
    ldx l0d58                                                         ; 9b89: ae 58 0d    .X.
    lda l0d59                                                         ; 9b8c: ad 59 0d    .Y.
    jsr oseven                                                        ; 9b8f: 20 bf ff     ..            ; Generate event Y='Network error'
    jmp tx_done_exit                                                  ; 9b92: 4c c0 9b    L..

; ***************************************************************************************
; TX done: OSProc call
; 
; Calls the ROM entry point at &8000 (rom_header) with
; X=l0d58, Y=l0d59. This invokes an OS-level procedure
; on behalf of the remote station.
; ***************************************************************************************
.tx_done_os_proc
    ldx l0d58                                                         ; 9b95: ae 58 0d    .X.
    ldy l0d59                                                         ; 9b98: ac 59 0d    .Y.
    jsr rom_header                                                    ; 9b9b: 20 00 80     ..
    jmp tx_done_exit                                                  ; 9b9e: 4c c0 9b    L..

; ***************************************************************************************
; TX done: HALT
; 
; Sets bit 2 of rx_flags (&0D64), enables interrupts, and
; spin-waits until bit 2 is cleared (by a CONTINUE from the
; remote station). If bit 2 is already set, skips to exit.
; ***************************************************************************************
.tx_done_halt
    lda #4                                                            ; 9ba1: a9 04       ..
    bit rx_flags                                                      ; 9ba3: 2c 64 0d    ,d.
    bne tx_done_exit                                                  ; 9ba6: d0 18       ..
    ora rx_flags                                                      ; 9ba8: 0d 64 0d    .d.
    sta rx_flags                                                      ; 9bab: 8d 64 0d    .d.
    lda #4                                                            ; 9bae: a9 04       ..
    cli                                                               ; 9bb0: 58          X
; &9bb1 referenced 1 time by &9bb4
.loop_c9bb1
    bit rx_flags                                                      ; 9bb1: 2c 64 0d    ,d.
    bne loop_c9bb1                                                    ; 9bb4: d0 fb       ..
    beq tx_done_exit                                                  ; 9bb6: f0 08       ..             ; ALWAYS branch

; ***************************************************************************************
; TX done: CONTINUE
; 
; Clears bit 2 of rx_flags (&0D64), releasing any station
; that is halted and spinning in tx_done_halt.
; ***************************************************************************************
.tx_done_continue
    lda rx_flags                                                      ; 9bb8: ad 64 0d    .d.
    and #&fb                                                          ; 9bbb: 29 fb       ).
    sta rx_flags                                                      ; 9bbd: 8d 64 0d    .d.
; &9bc0 referenced 4 times by &9b92, &9b9e, &9ba6, &9bb6
.tx_done_exit
    pla                                                               ; 9bc0: 68          h
    tay                                                               ; 9bc1: a8          .
    pla                                                               ; 9bc2: 68          h
    tax                                                               ; 9bc3: aa          .
    lda #0                                                            ; 9bc4: a9 00       ..
    rts                                                               ; 9bc6: 60          `

; &9bc7 referenced 1 time by &9660
.c9bc7
    txa                                                               ; 9bc7: 8a          .
    pha                                                               ; 9bc8: 48          H
    ldy #2                                                            ; 9bc9: a0 02       ..
    lda (nmi_tx_block),y                                              ; 9bcb: b1 a0       ..
    sta tx_dst_stn                                                    ; 9bcd: 8d 20 0d    . .
    iny                                                               ; 9bd0: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 9bd1: b1 a0       ..
    sta tx_dst_net                                                    ; 9bd3: 8d 21 0d    .!.
    ldy #0                                                            ; 9bd6: a0 00       ..
    lda (nmi_tx_block),y                                              ; 9bd8: b1 a0       ..
    bmi c9bdf                                                         ; 9bda: 30 03       0.
    jmp tx_active_start                                               ; 9bdc: 4c 6b 9c    Lk.

; &9bdf referenced 1 time by &9bda
.c9bdf
    sta tx_ctrl_byte                                                  ; 9bdf: 8d 24 0d    .$.
    tax                                                               ; 9be2: aa          .
    iny                                                               ; 9be3: c8          .
    lda (nmi_tx_block),y                                              ; 9be4: b1 a0       ..
    sta tx_port                                                       ; 9be6: 8d 25 0d    .%.
    bne c9c1e                                                         ; 9be9: d0 33       .3
    cpx #&83                                                          ; 9beb: e0 83       ..
    bcs c9c0a                                                         ; 9bed: b0 1b       ..
    sec                                                               ; 9bef: 38          8
    php                                                               ; 9bf0: 08          .
    ldy #8                                                            ; 9bf1: a0 08       ..
; &9bf3 referenced 1 time by &9c07
.loop_c9bf3
    lda (nmi_tx_block),y                                              ; 9bf3: b1 a0       ..
    dey                                                               ; 9bf5: 88          .
    dey                                                               ; 9bf6: 88          .
    dey                                                               ; 9bf7: 88          .
    dey                                                               ; 9bf8: 88          .
    plp                                                               ; 9bf9: 28          (
    sbc (nmi_tx_block),y                                              ; 9bfa: f1 a0       ..
    sta tx_data_start,y                                               ; 9bfc: 99 26 0d    .&.
    iny                                                               ; 9bff: c8          .
    iny                                                               ; 9c00: c8          .
    iny                                                               ; 9c01: c8          .
    iny                                                               ; 9c02: c8          .
    iny                                                               ; 9c03: c8          .
    php                                                               ; 9c04: 08          .
    cpy #&0c                                                          ; 9c05: c0 0c       ..
    bcc loop_c9bf3                                                    ; 9c07: 90 ea       ..
    plp                                                               ; 9c09: 28          (
; &9c0a referenced 1 time by &9bed
.c9c0a
    cpx #&81                                                          ; 9c0a: e0 81       ..
    bcc tx_active_start                                               ; 9c0c: 90 5d       .]
    cpx #&89                                                          ; 9c0e: e0 89       ..
    bcs tx_active_start                                               ; 9c10: b0 59       .Y
    ldy #&0c                                                          ; 9c12: a0 0c       ..
; &9c14 referenced 1 time by &9c1c
.loop_c9c14
    lda (nmi_tx_block),y                                              ; 9c14: b1 a0       ..
    sta nmi_shim_1a,y                                                 ; 9c16: 99 1a 0d    ...
    iny                                                               ; 9c19: c8          .
    cpy #&10                                                          ; 9c1a: c0 10       ..
    bcc loop_c9c14                                                    ; 9c1c: 90 f6       ..
; &9c1e referenced 1 time by &9be9
.c9c1e
    lda #&20 ; ' '                                                    ; 9c1e: a9 20       .
    bit econet_control23_or_status2                                   ; 9c20: 2c a1 fe    ,..
    bne c9c7b                                                         ; 9c23: d0 56       .V
    lda #&fd                                                          ; 9c25: a9 fd       ..
    pha                                                               ; 9c27: 48          H
    lda #6                                                            ; 9c28: a9 06       ..
    sta tx_length                                                     ; 9c2a: 8d 50 0d    .P.
    lda #0                                                            ; 9c2d: a9 00       ..
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
    sta tx_index                                                      ; 9c2f: 8d 4f 0d    .O.
    pha                                                               ; 9c32: 48          H
    pha                                                               ; 9c33: 48          H
    ldy #&e7                                                          ; 9c34: a0 e7       ..             ; Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &9c36 referenced 3 times by &9c5c, &9c61, &9c66
.c9c36
    lda #4                                                            ; 9c36: a9 04       ..             ; A=&04: INACTIVE mask for SR2 bit2
    php                                                               ; 9c38: 08          .
    sei                                                               ; 9c39: 78          x
; &9c3a referenced 1 time by &9cb6
.c9c3a
    bit station_id_disable_net_nmis                                   ; 9c3a: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
    bit station_id_disable_net_nmis                                   ; 9c3d: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
.sub_c9c40
l9c42 = sub_c9c40+2
    bit econet_control23_or_status2                                   ; 9c40: 2c a1 fe    ,..            ; BIT SR2: Z = &04 AND SR2 -- tests INACTIVE
; &9c42 referenced 1 time by &9cb2
    beq c9c54                                                         ; 9c43: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 9c45: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 9c48: a9 67       .g             ; CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9c4a: 8d a1 fe    ...
    lda #&10                                                          ; 9c4d: a9 10       ..             ; A=&10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 9c4f: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 9c52: d0 35       .5             ; CTS set -- clock hardware detected, start TX
; &9c54 referenced 1 time by &9c43
.c9c54
    bit video_ula_control                                             ; 9c54: 2c 20 fe    , .            ; INTON -- re-enable NMIs (&FE20 read)
    plp                                                               ; 9c57: 28          (
    tsx                                                               ; 9c58: ba          .              ; 3-byte timeout counter on stack
    inc l0101,x                                                       ; 9c59: fe 01 01    ...
    bne c9c36                                                         ; 9c5c: d0 d8       ..
    inc l0102,x                                                       ; 9c5e: fe 02 01    ...
    bne c9c36                                                         ; 9c61: d0 d3       ..
    inc l0103,x                                                       ; 9c63: fe 03 01    ...
    bne c9c36                                                         ; 9c66: d0 ce       ..
    jmp tx_line_jammed                                                ; 9c68: 4c 6f 9c    Lo.

; TX_ACTIVE branch (A=&44 = CR1 value for TX active)
; &9c6b referenced 3 times by &9bdc, &9c0c, &9c10
.tx_active_start
    lda #&44 ; 'D'                                                    ; 9c6b: a9 44       .D
    bne c9c7d                                                         ; 9c6d: d0 0e       ..             ; ALWAYS branch

; ***************************************************************************************
; TX timeout error handler (Line Jammed)
; 
; Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
; timeout loop's state), then stores error code &40 ("Line
; Jammed") into the TX control block and signals completion.
; ***************************************************************************************
; &9c6f referenced 1 time by &9c68
.tx_line_jammed
    lda #7                                                            ; 9c6f: a9 07       ..             ; CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)
    sta econet_control23_or_status2                                   ; 9c71: 8d a1 fe    ...
    pla                                                               ; 9c74: 68          h
    pla                                                               ; 9c75: 68          h
    pla                                                               ; 9c76: 68          h
    lda #&40 ; '@'                                                    ; 9c77: a9 40       .@             ; Error &40 = 'Line Jammed'
    bne c9c7d                                                         ; 9c79: d0 02       ..             ; ALWAYS branch

; &9c7b referenced 1 time by &9c23
.c9c7b
    lda #&43 ; 'C'                                                    ; 9c7b: a9 43       .C
; &9c7d referenced 2 times by &9c6d, &9c79
.c9c7d
    ldy #0                                                            ; 9c7d: a0 00       ..
    sta (nmi_tx_block),y                                              ; 9c7f: 91 a0       ..
    lda #&80                                                          ; 9c81: a9 80       ..
    sta tx_clear_flag                                                 ; 9c83: 8d 62 0d    .b.
    pla                                                               ; 9c86: 68          h
    tax                                                               ; 9c87: aa          .
    rts                                                               ; 9c88: 60          `

; ***************************************************************************************
; TX preparation
; 
; Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
; installs NMI TX handler at &9D5B, and re-enables NMIs.
; ***************************************************************************************
; &9c89 referenced 1 time by &9c52
.tx_prepare
    sty econet_control23_or_status2                                   ; 9c89: 8c a1 fe    ...            ; Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
    ldx #&44 ; 'D'                                                    ; 9c8c: a2 44       .D             ; CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)
    stx econet_control1_or_status1                                    ; 9c8e: 8e a0 fe    ...
    ldx #&2d ; '-'                                                    ; 9c91: a2 2d       .-             ; Install NMI handler at &9D4C (TX data handler)
    ldy #&9d                                                          ; 9c93: a0 9d       ..
    stx nmi_jmp_lo                                                    ; 9c95: 8e 0c 0d    ...
    sty nmi_jmp_hi                                                    ; 9c98: 8c 0d 0d    ...
    bit video_ula_control                                             ; 9c9b: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA (&FE20 read)
    lda tx_port                                                       ; 9c9e: ad 25 0d    .%.
    bne c9cef                                                         ; 9ca1: d0 4c       .L
    ldy tx_ctrl_byte                                                  ; 9ca3: ac 24 0d    .$.
    lda l9eaf,y                                                       ; 9ca6: b9 af 9e    ...
    sta tx_flags                                                      ; 9ca9: 8d 4a 0d    .J.
    lda l9ea7,y                                                       ; 9cac: b9 a7 9e    ...
    sta tx_length                                                     ; 9caf: 8d 50 0d    .P.
    lda l9c42,y                                                       ; 9cb2: b9 42 9c    .B.
    pha                                                               ; 9cb5: 48          H
    lda c9c3a,y                                                       ; 9cb6: b9 3a 9c    .:.
    pha                                                               ; 9cb9: 48          H
    rts                                                               ; 9cba: 60          `

    equb <(tx_ctrl_peek-1)                                            ; 9cbb: ce          .
    equb <(tx_ctrl_poke-1)                                            ; 9cbc: d2          .
    equb <(sub_c9d16-1)                                               ; 9cbd: 15          .
    equb <(sub_c9d16-1)                                               ; 9cbe: 15          .
    equb <(sub_c9d16-1)                                               ; 9cbf: 15          .
    equb <(tx_ctrl_exit-1)                                            ; 9cc0: 25          %
    equb <(tx_ctrl_exit-1)                                            ; 9cc1: 25          %
    equb <(sub_c9ccb-1)                                               ; 9cc2: ca          .
    equb >(tx_ctrl_peek-1)                                            ; 9cc3: 9c          .
    equb >(tx_ctrl_poke-1)                                            ; 9cc4: 9c          .
    equb >(sub_c9d16-1)                                               ; 9cc5: 9d          .
    equb >(sub_c9d16-1)                                               ; 9cc6: 9d          .
    equb >(sub_c9d16-1)                                               ; 9cc7: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cc8: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cc9: 9d          .
    equb >(sub_c9ccb-1)                                               ; 9cca: 9c          .

.sub_c9ccb
    lda #3                                                            ; 9ccb: a9 03       ..
    bne c9d18                                                         ; 9ccd: d0 49       .I             ; ALWAYS branch

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
    lda #3                                                            ; 9ccf: a9 03       ..
    bne c9cd5                                                         ; 9cd1: d0 02       ..             ; ALWAYS branch

; ***************************************************************************************
; TX ctrl: POKE transfer setup
; 
; Sets scout_status=2 and shares the 4-byte addition and
; transfer calculation path with tx_ctrl_peek.
; ***************************************************************************************
.tx_ctrl_poke
    lda #2                                                            ; 9cd3: a9 02       ..
; &9cd5 referenced 1 time by &9cd1
.c9cd5
    sta scout_status                                                  ; 9cd5: 8d 5c 0d    .\.
    clc                                                               ; 9cd8: 18          .
    php                                                               ; 9cd9: 08          .
    ldy #&0c                                                          ; 9cda: a0 0c       ..
; &9cdc referenced 1 time by &9ce9
.loop_c9cdc
    lda l0d1e,y                                                       ; 9cdc: b9 1e 0d    ...
    plp                                                               ; 9cdf: 28          (
    adc (nmi_tx_block),y                                              ; 9ce0: 71 a0       q.
    sta l0d1e,y                                                       ; 9ce2: 99 1e 0d    ...
    iny                                                               ; 9ce5: c8          .
    php                                                               ; 9ce6: 08          .
; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_proc
    cpy #&10                                                          ; 9ce7: c0 10       ..
    bcc loop_c9cdc                                                    ; 9ce9: 90 f1       ..
    plp                                                               ; 9ceb: 28          (
    jmp c9d1b                                                         ; 9cec: 4c 1b 9d    L..

; &9cef referenced 1 time by &9ca1
.c9cef
    lda tx_dst_stn                                                    ; 9cef: ad 20 0d    . .
    and tx_dst_net                                                    ; 9cf2: 2d 21 0d    -!.
    cmp #&ff                                                          ; 9cf5: c9 ff       ..
    bne c9d11                                                         ; 9cf7: d0 18       ..
    lda #&0e                                                          ; 9cf9: a9 0e       ..
    sta tx_length                                                     ; 9cfb: 8d 50 0d    .P.
    lda #&40 ; '@'                                                    ; 9cfe: a9 40       .@
    sta tx_flags                                                      ; 9d00: 8d 4a 0d    .J.
    ldy #4                                                            ; 9d03: a0 04       ..
; &9d05 referenced 1 time by &9d0d
.loop_c9d05
    lda (nmi_tx_block),y                                              ; 9d05: b1 a0       ..
    sta tx_src_stn,y                                                  ; 9d07: 99 22 0d    .".
    iny                                                               ; 9d0a: c8          .
    cpy #&0c                                                          ; 9d0b: c0 0c       ..
    bcc loop_c9d05                                                    ; 9d0d: 90 f6       ..
    bcs tx_ctrl_exit                                                  ; 9d0f: b0 15       ..             ; ALWAYS branch

; &9d11 referenced 1 time by &9cf7
.c9d11
    lda #0                                                            ; 9d11: a9 00       ..
    sta tx_flags                                                      ; 9d13: 8d 4a 0d    .J.
.sub_c9d16
    lda #2                                                            ; 9d16: a9 02       ..
; &9d18 referenced 1 time by &9ccd
.c9d18
    sta scout_status                                                  ; 9d18: 8d 5c 0d    .\.
; &9d1b referenced 1 time by &9cec
.c9d1b
    lda nmi_tx_block                                                  ; 9d1b: a5 a0       ..
    sta port_ws_offset                                                ; 9d1d: 85 a6       ..
    lda nmi_tx_block_hi                                               ; 9d1f: a5 a1       ..
    sta rx_buf_offset                                                 ; 9d21: 85 a7       ..
    jsr tx_calc_transfer                                              ; 9d23: 20 38 9f     8.
; &9d26 referenced 1 time by &9d0f
.tx_ctrl_exit
    plp                                                               ; 9d26: 28          (
    pla                                                               ; 9d27: 68          h
    pla                                                               ; 9d28: 68          h
    pla                                                               ; 9d29: 68          h
    pla                                                               ; 9d2a: 68          h
    tax                                                               ; 9d2b: aa          .
    rts                                                               ; 9d2c: 60          `

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
    ldy tx_index                                                      ; 9d2d: ac 4f 0d    .O.            ; Load TX buffer index
    bit econet_control1_or_status1                                    ; 9d30: 2c a0 fe    ,..            ; BIT SR1: V=bit6(TDRA), N=bit7(IRQ)
; &9d33 referenced 1 time by &9d4e
.loop_c9d33
    bvc c9d57                                                         ; 9d33: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 9d35: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 9d38: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 9d3b: c8          .
    lda tx_dst_stn,y                                                  ; 9d3c: b9 20 0d    . .
    iny                                                               ; 9d3f: c8          .
    sty tx_index                                                      ; 9d40: 8c 4f 0d    .O.
    sta econet_data_continue_frame                                    ; 9d43: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy tx_length                                                     ; 9d46: cc 50 0d    .P.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 9d49: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA
    bit econet_control1_or_status1                                    ; 9d4b: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi loop_c9d33                                                    ; 9d4e: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 9d50: 4c 14 0d    L..            ; RTI -- wait for next NMI

; TX error path
; &9d53 referenced 1 time by &9d98
.tx_error
    lda #&42 ; 'B'                                                    ; 9d53: a9 42       .B             ; Error &42
    bne c9d5e                                                         ; 9d55: d0 07       ..             ; ALWAYS branch

; &9d57 referenced 1 time by &9d33
.c9d57
    lda #&67 ; 'g'                                                    ; 9d57: a9 67       .g             ; CR2=&67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 9d59: 8d a1 fe    ...
    lda #&41 ; 'A'                                                    ; 9d5c: a9 41       .A             ; Error &41 (TDRA not ready)
; &9d5e referenced 1 time by &9d55
.c9d5e
    ldy station_id_disable_net_nmis                                   ; 9d5e: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &9d61 referenced 1 time by &9d64
.loop_c9d61
    pha                                                               ; 9d61: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 9d62: 68          h
    iny                                                               ; 9d63: c8          .
    bne loop_c9d61                                                    ; 9d64: d0 fb       ..
    jmp tx_store_result                                               ; 9d66: 4c 1c 9f    L..

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
; &9d69 referenced 1 time by &9d49
.tx_last_data
    lda #&3f ; '?'                                                    ; 9d69: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 9d6b: 8d a1 fe    ...
    lda #&75 ; 'u'                                                    ; 9d6e: a9 75       .u             ; Install NMI handler at &9D94 (TX completion)
    ldy #&9d                                                          ; 9d70: a0 9d       ..
    jmp set_nmi_vector                                                ; 9d72: 4c 0e 0d    L..

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
    lda #&82                                                          ; 9d75: a9 82       ..             ; Jump to error handler; CR1=&82: TX_RESET | RIE (now in RX mode)
    sta econet_control1_or_status1                                    ; 9d77: 8d a0 fe    ...
    bit tx_flags                                                      ; 9d7a: 2c 4a 0d    ,J.            ; Test workspace flags
    bvc c9d82                                                         ; 9d7d: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 9d7f: 4c 16 9f    L..            ; bit6 set -- TX completion

; &9d82 referenced 1 time by &9d7d
.c9d82
    lda #1                                                            ; 9d82: a9 01       ..
    bit tx_flags                                                      ; 9d84: 2c 4a 0d    ,J.
    beq c9d8c                                                         ; 9d87: f0 03       ..
    jmp handshake_await_ack                                           ; 9d89: 4c ba 9e    L..            ; bit0 set -- four-way handshake data phase

; &9d8c referenced 1 time by &9d87
.c9d8c
    lda #&93                                                          ; 9d8c: a9 93       ..             ; Install RX reply handler at &9DB2
    ldy #&9d                                                          ; 9d8e: a0 9d       ..
    jmp set_nmi_vector                                                ; 9d90: 4c 0e 0d    L..

; ***************************************************************************************
; RX reply scout handler
; 
; Handles reception of the reply scout frame after transmission.
; Checks SR2 bit0 (AP) for incoming data, reads the first byte
; (destination station) and compares to our station ID via &FE18
; (which also disables NMIs as a side effect).
; ***************************************************************************************
.nmi_reply_scout
    lda #1                                                            ; 9d93: a9 01       ..             ; A=&01: AP mask for SR2
    bit econet_control23_or_status2                                   ; 9d95: 2c a1 fe    ,..            ; BIT SR2: test AP (Address Present)
    beq tx_error                                                      ; 9d98: f0 b9       ..             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9d9a: ad a2 fe    ...
    cmp station_id_disable_net_nmis                                   ; 9d9d: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne c9dbf                                                         ; 9da0: d0 1d       ..             ; Not our station -- error/reject
    lda #&a9                                                          ; 9da2: a9 a9       ..             ; Install next handler at &9DC8 (reply continuation)
    ldy #&9d                                                          ; 9da4: a0 9d       ..
    jmp set_nmi_vector                                                ; 9da6: 4c 0e 0d    L..

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
    bit econet_control23_or_status2                                   ; 9da9: 2c a1 fe    ,..            ; Read RX byte (destination station); BIT SR2: test for RDA (bit7 = data available)
    bpl c9dbf                                                         ; 9dac: 10 11       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9dae: ad a2 fe    ...            ; Read destination network byte
    bne c9dbf                                                         ; 9db1: d0 0c       ..             ; Non-zero -- network mismatch, error
    lda #&c2                                                          ; 9db3: a9 c2       ..             ; Install next handler at &9DE3 (reply validation)
    ldy #&9d                                                          ; 9db5: a0 9d       ..
    bit econet_control1_or_status1                                    ; 9db7: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 9dba: 30 06       0.             ; IRQ set -- fall through to &9DE3 without RTI
    jmp set_nmi_vector                                                ; 9dbc: 4c 0e 0d    L..            ; IRQ not set -- install handler and RTI

; &9dbf referenced 7 times by &9da0, &9dac, &9db1, &9dc5, &9dcd, &9dd5, &9ddc
.c9dbf
    jmp tx_result_fail                                                ; 9dbf: 4c 1a 9f    L..

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
; &9dc2 referenced 1 time by &9dba
.nmi_reply_validate
    bit econet_control23_or_status2                                   ; 9dc2: 2c a1 fe    ,..            ; BIT SR2: test RDA (bit7). Must be set for valid reply.
    bpl c9dbf                                                         ; 9dc5: 10 f8       ..             ; No RDA -- error (FV masking RDA via PSE would cause this)
    lda econet_data_continue_frame                                    ; 9dc7: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9dca: cd 20 0d    . .            ; Compare to original TX destination station (&0D20)
    bne c9dbf                                                         ; 9dcd: d0 f0       ..             ; Mismatch -- not the expected reply, error
    lda econet_data_continue_frame                                    ; 9dcf: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9dd2: cd 21 0d    .!.            ; Compare to original TX destination network (&0D21)
    bne c9dbf                                                         ; 9dd5: d0 e8       ..             ; Mismatch -- error
    lda #2                                                            ; 9dd7: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9dd9: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq c9dbf                                                         ; 9ddc: f0 e1       ..             ; No FV -- incomplete frame, error
    lda #&a7                                                          ; 9dde: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)
    sta econet_control23_or_status2                                   ; 9de0: 8d a1 fe    ...
    lda #&44 ; 'D'                                                    ; 9de3: a9 44       .D             ; CR1=&44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 9de5: 8d a0 fe    ...
    lda #&ba                                                          ; 9de8: a9 ba       ..             ; Install next handler at &9EDD (four-way data phase) into &0D4B/&0D4C
    ldy #&9e                                                          ; 9dea: a0 9e       ..
    sta nmi_next_lo                                                   ; 9dec: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 9def: 8c 4c 0d    .L.
    lda tx_dst_stn                                                    ; 9df2: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 9df5: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc data_tx_error                                                 ; 9df8: 50 73       Ps             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9dfa: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 9dfd: ad 21 0d    .!.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9e00: 8d a2 fe    ...
    lda #&0a                                                          ; 9e03: a9 0a       ..             ; Install handler at &9E2B (write src addr for scout ACK)
    ldy #&9e                                                          ; 9e05: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e07: 4c 0e 0d    L..

; ***************************************************************************************
; TX scout ACK: write source address
; 
; Writes our station ID and network=0 to TX FIFO, completing the
; 4-byte scout ACK frame. Then proceeds to send the data frame.
; ***************************************************************************************
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 9e0a: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9e0d: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc data_tx_error                                                 ; 9e10: 50 5b       P[             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9e12: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9e15: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 9e17: 8d a2 fe    ...
; &9e1a referenced 1 time by &999e
.data_tx_begin
    lda #2                                                            ; 9e1a: a9 02       ..
    bit tx_flags                                                      ; 9e1c: 2c 4a 0d    ,J.
    bne c9e28                                                         ; 9e1f: d0 07       ..
    lda #&2f ; '/'                                                    ; 9e21: a9 2f       ./
    ldy #&9e                                                          ; 9e23: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e25: 4c 0e 0d    L..

; &9e28 referenced 1 time by &9e1f
.c9e28
    lda #&81                                                          ; 9e28: a9 81       ..
    ldy #&9e                                                          ; 9e2a: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e2c: 4c 0e 0d    L..

; ***************************************************************************************
; TX data phase: send payload
; 
; Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
; Same pattern as the NMI TX handler at &9D5B but reads from the port
; buffer instead of the TX workspace. Writes two bytes per iteration,
; checking SR1 IRQ between pairs for tight looping.
; ***************************************************************************************
.nmi_data_tx
    ldy port_buf_len                                                  ; 9e2f: a4 a2       ..             ; Y = buffer offset, resume from last position
    bit econet_control1_or_status1                                    ; 9e31: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
; &9e34 referenced 1 time by &9e57
.c9e34
    bvc data_tx_error                                                 ; 9e34: 50 37       P7             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 9e36: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 9e38: 8d a2 fe    ...
    iny                                                               ; 9e3b: c8          .
    bne c9e44                                                         ; 9e3c: d0 06       ..
    dec port_buf_len_hi                                               ; 9e3e: c6 a3       ..
    beq data_tx_last                                                  ; 9e40: f0 1a       ..
    inc open_port_buf_hi                                              ; 9e42: e6 a5       ..
; &9e44 referenced 1 time by &9e3c
.c9e44
    lda (open_port_buf),y                                             ; 9e44: b1 a4       ..
    sta econet_data_continue_frame                                    ; 9e46: 8d a2 fe    ...
    iny                                                               ; 9e49: c8          .
    sty port_buf_len                                                  ; 9e4a: 84 a2       ..
    bne c9e54                                                         ; 9e4c: d0 06       ..
    dec port_buf_len_hi                                               ; 9e4e: c6 a3       ..
    beq data_tx_last                                                  ; 9e50: f0 0a       ..
    inc open_port_buf_hi                                              ; 9e52: e6 a5       ..
; &9e54 referenced 1 time by &9e4c
.c9e54
    bit econet_control1_or_status1                                    ; 9e54: 2c a0 fe    ,..
    bmi c9e34                                                         ; 9e57: 30 db       0.
    jmp nmi_rti                                                       ; 9e59: 4c 14 0d    L..

; &9e5c referenced 4 times by &9e40, &9e50, &9e9a, &9eb0
.data_tx_last
    lda #&3f ; '?'                                                    ; 9e5c: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 9e5e: 8d a1 fe    ...
    lda tx_flags                                                      ; 9e61: ad 4a 0d    .J.
    bpl install_saved_handler                                         ; 9e64: 10 12       ..
    lda #&2e ; '.'                                                    ; 9e66: a9 2e       ..
    ldy #&9a                                                          ; 9e68: a0 9a       ..
    jmp set_nmi_vector                                                ; 9e6a: 4c 0e 0d    L..

; &9e6d referenced 4 times by &9df8, &9e10, &9e34, &9e84
.data_tx_error
    lda tx_flags                                                      ; 9e6d: ad 4a 0d    .J.
    bpl c9e75                                                         ; 9e70: 10 03       ..
    jmp discard_reset_listen                                          ; 9e72: 4c 2e 9a    L..

; &9e75 referenced 1 time by &9e70
.c9e75
    jmp tx_result_fail                                                ; 9e75: 4c 1a 9f    L..

; &9e78 referenced 1 time by &9e64
.install_saved_handler
    lda nmi_next_lo                                                   ; 9e78: ad 4b 0d    .K.
    ldy nmi_next_hi                                                   ; 9e7b: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 9e7e: 4c 0e 0d    L..

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 9e81: 2c a0 fe    ,..
; &9e84 referenced 1 time by &9eb5
.c9e84
    bvc data_tx_error                                                 ; 9e84: 50 e7       P.
    lda tube_data_register_3                                          ; 9e86: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9e89: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9e8c: e6 a2       ..
    bne c9e9c                                                         ; 9e8e: d0 0c       ..
    inc port_buf_len_hi                                               ; 9e90: e6 a3       ..
    bne c9e9c                                                         ; 9e92: d0 08       ..
    inc open_port_buf                                                 ; 9e94: e6 a4       ..
    bne c9e9c                                                         ; 9e96: d0 04       ..
    inc open_port_buf_hi                                              ; 9e98: e6 a5       ..
    beq data_tx_last                                                  ; 9e9a: f0 c0       ..
; &9e9c referenced 3 times by &9e8e, &9e92, &9e96
.c9e9c
    lda tube_data_register_3                                          ; 9e9c: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9e9f: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9ea2: e6 a2       ..
    bne c9eb2                                                         ; 9ea4: d0 0c       ..
.sub_c9ea6
l9ea7 = sub_c9ea6+1
    inc port_buf_len_hi                                               ; 9ea6: e6 a3       ..
; &9ea7 referenced 1 time by &9cac
    bne c9eb2                                                         ; 9ea8: d0 08       ..
    inc open_port_buf                                                 ; 9eaa: e6 a4       ..
    bne c9eb2                                                         ; 9eac: d0 04       ..
.sub_c9eae
l9eaf = sub_c9eae+1
    inc open_port_buf_hi                                              ; 9eae: e6 a5       ..
; &9eaf referenced 1 time by &9ca6
    beq data_tx_last                                                  ; 9eb0: f0 aa       ..
; &9eb2 referenced 3 times by &9ea4, &9ea8, &9eac
.c9eb2
    bit econet_control1_or_status1                                    ; 9eb2: 2c a0 fe    ,..
    bmi c9e84                                                         ; 9eb5: 30 cd       0.
    jmp nmi_rti                                                       ; 9eb7: 4c 14 0d    L..

; ***************************************************************************************
; Four-way handshake: switch to RX for final ACK
; 
; After the data frame TX completes, switches to RX mode (CR1=&82)
; and installs &9EF8 to receive the final ACK from the remote station.
; ***************************************************************************************
; &9eba referenced 1 time by &9d89
.handshake_await_ack
    lda #&82                                                          ; 9eba: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 9ebc: 8d a0 fe    ...
    lda #&c6                                                          ; 9ebf: a9 c6       ..             ; Install handler at &9EE9 (RX final ACK)
    ldy #&9e                                                          ; 9ec1: a0 9e       ..
    jmp set_nmi_vector                                                ; 9ec3: 4c 0e 0d    L..

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
    lda #1                                                            ; 9ec6: a9 01       ..             ; A=&01: AP mask
    bit econet_control23_or_status2                                   ; 9ec8: 2c a1 fe    ,..            ; BIT SR2: test AP
    beq tx_result_fail                                                ; 9ecb: f0 4d       .M             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9ecd: ad a2 fe    ...            ; Read dest station
    cmp station_id_disable_net_nmis                                   ; 9ed0: cd 18 fe    ...            ; Compare to our station (INTOFF side effect)
    bne tx_result_fail                                                ; 9ed3: d0 45       .E             ; Not our station -- error
    lda #&dc                                                          ; 9ed5: a9 dc       ..             ; Install handler at &9EFF (final ACK continuation)
    ldy #&9e                                                          ; 9ed7: a0 9e       ..
    jmp set_nmi_vector                                                ; 9ed9: 4c 0e 0d    L..

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 9edc: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9edf: 10 39       .9             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9ee1: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 9ee4: d0 34       .4             ; Non-zero -- network mismatch, error
    lda #&f2                                                          ; 9ee6: a9 f2       ..             ; Install handler at &9F15 (final ACK validation)
    ldy #&9e                                                          ; 9ee8: a0 9e       ..
    bit econet_control1_or_status1                                    ; 9eea: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 9eed: 30 03       0.             ; IRQ set -- fall through to &9F15 without RTI
    jmp set_nmi_vector                                                ; 9eef: 4c 0e 0d    L..

; ***************************************************************************************
; Final ACK validation
; 
; Reads and validates src_stn and src_net against original TX dest.
; Then checks FV for frame completion.
; ***************************************************************************************
; &9ef2 referenced 1 time by &9eed
.nmi_final_ack_validate
    bit econet_control23_or_status2                                   ; 9ef2: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9ef5: 10 23       .#             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9ef7: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9efa: cd 20 0d    . .            ; Compare to TX dest station (&0D20)
    bne tx_result_fail                                                ; 9efd: d0 1b       ..             ; Mismatch -- error
    lda econet_data_continue_frame                                    ; 9eff: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9f02: cd 21 0d    .!.            ; Compare to TX dest network (&0D21)
    bne tx_result_fail                                                ; 9f05: d0 13       ..             ; Mismatch -- error
    lda tx_flags                                                      ; 9f07: ad 4a 0d    .J.
    bpl c9f0f                                                         ; 9f0a: 10 03       ..
    jmp c9858                                                         ; 9f0c: 4c 58 98    LX.

; &9f0f referenced 1 time by &9f0a
.c9f0f
    lda #2                                                            ; 9f0f: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9f11: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq tx_result_fail                                                ; 9f14: f0 04       ..             ; No FV -- error
; ***************************************************************************************
; TX completion handler
; 
; Stores result code 0 (success) into the first byte of the TX control
; block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
; and calls full ADLC reset + idle listen via &9A4A.
; ***************************************************************************************
; &9f16 referenced 2 times by &994c, &9d7f
.tx_result_ok
    lda #0                                                            ; 9f16: a9 00       ..             ; A=0: success result code
    beq tx_store_result                                               ; 9f18: f0 02       ..             ; BEQ: always taken (A=0); ALWAYS branch

; &9f1a referenced 11 times by &9877, &9dbf, &9e75, &9ecb, &9ed3, &9edf, &9ee4, &9ef5, &9efd, &9f05, &9f14
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 9f1a: a9 41       .A
; ***************************************************************************************
; TX error handler
; 
; Stores error code (A) into the TX control block, sets &0D3A bit7
; for completion, and returns to idle via &9A4A.
; Error codes: &00=success, &40=line jammed, &41=not listening,
; &42=net error.
; ***************************************************************************************
; &9f1c referenced 2 times by &9d66, &9f18
.tx_store_result
    ldy #0                                                            ; 9f1c: a0 00       ..             ; Y=0: index into TX control block
    sta (nmi_tx_block),y                                              ; 9f1e: 91 a0       ..             ; Store result/error code at (nmi_tx_block),0
    lda #&80                                                          ; 9f20: a9 80       ..             ; &80: completion flag for &0D3A
    sta tx_clear_flag                                                 ; 9f22: 8d 62 0d    .b.            ; Signal TX complete
    jmp discard_reset_listen                                          ; 9f25: 4c 2e 9a    L..            ; Full ADLC reset and return to idle listen

; Unreferenced data block (purpose unknown)
    equb &0e, &0e, &0a, &0a, &0a, 6, 6, &0a, &81, 0, 0, 0, 0, 1, 1    ; 9f28: 0e 0e 0a... ...
    equb &81                                                          ; 9f37: 81          .

; ***************************************************************************************
; Calculate transfer size
; 
; Computes the number of bytes actually transferred during a data
; frame reception. Subtracts the low pointer (LPTR, offset 4 in
; the RXCB) from the current buffer position to get the byte count,
; and stores it back into the RXCB's high pointer field (HPTR,
; offset 8). This tells the caller how much data was received.
; ***************************************************************************************
; &9f38 referenced 3 times by &97fc, &9ade, &9d23
.tx_calc_transfer
    ldy #6                                                            ; 9f38: a0 06       ..
    lda (port_ws_offset),y                                            ; 9f3a: b1 a6       ..
    iny                                                               ; 9f3c: c8          .              ; Y=&07
    and (port_ws_offset),y                                            ; 9f3d: 31 a6       1.
    cmp #&ff                                                          ; 9f3f: c9 ff       ..
    beq c9f84                                                         ; 9f41: f0 41       .A
    lda tube_flag                                                     ; 9f43: ad 67 0d    .g.
    beq c9f84                                                         ; 9f46: f0 3c       .<
    lda tx_flags                                                      ; 9f48: ad 4a 0d    .J.
    ora #2                                                            ; 9f4b: 09 02       ..
    sta tx_flags                                                      ; 9f4d: 8d 4a 0d    .J.
    sec                                                               ; 9f50: 38          8
    php                                                               ; 9f51: 08          .
    ldy #4                                                            ; 9f52: a0 04       ..
    lda (port_ws_offset),y                                            ; 9f54: b1 a6       ..
    iny                                                               ; 9f56: c8          .
    iny                                                               ; 9f57: c8          .
    iny                                                               ; 9f58: c8          .
    iny                                                               ; 9f59: c8          .
    equb &28, &f1, &a6, &99, &9a, 0, &88, &88, &88, 8, &c0, 8, &90    ; 9f5a: 28 f1 a6... (..
    equb &ec, &28, &8a                                                ; 9f67: ec 28 8a    .(.

    pha                                                               ; 9f6a: 48          H
    lda #4                                                            ; 9f6b: a9 04       ..
    clc                                                               ; 9f6d: 18          .
    adc port_ws_offset                                                ; 9f6e: 65 a6       e.
    tax                                                               ; 9f70: aa          .
    ldy rx_buf_offset                                                 ; 9f71: a4 a7       ..
    lda #&c2                                                          ; 9f73: a9 c2       ..
    jsr tube_addr_claim                                               ; 9f75: 20 06 04     ..
    bcc c9f81                                                         ; 9f78: 90 07       ..
    lda scout_status                                                  ; 9f7a: ad 5c 0d    .\.
    jsr tube_addr_claim                                               ; 9f7d: 20 06 04     ..
    sec                                                               ; 9f80: 38          8
; &9f81 referenced 1 time by &9f78
.c9f81
    pla                                                               ; 9f81: 68          h
    tax                                                               ; 9f82: aa          .
    rts                                                               ; 9f83: 60          `

; &9f84 referenced 2 times by &9f41, &9f46
.c9f84
    ldy #4                                                            ; 9f84: a0 04       ..
    lda (port_ws_offset),y                                            ; 9f86: b1 a6       ..
    ldy #8                                                            ; 9f88: a0 08       ..
    sec                                                               ; 9f8a: 38          8
    sbc (port_ws_offset),y                                            ; 9f8b: f1 a6       ..
    sta port_buf_len                                                  ; 9f8d: 85 a2       ..
    ldy #5                                                            ; 9f8f: a0 05       ..
    lda (port_ws_offset),y                                            ; 9f91: b1 a6       ..
    sbc #0                                                            ; 9f93: e9 00       ..
    sta open_port_buf_hi                                              ; 9f95: 85 a5       ..
    ldy #8                                                            ; 9f97: a0 08       ..
    lda (port_ws_offset),y                                            ; 9f99: b1 a6       ..
    sta open_port_buf                                                 ; 9f9b: 85 a4       ..
    ldy #9                                                            ; 9f9d: a0 09       ..
    lda (port_ws_offset),y                                            ; 9f9f: b1 a6       ..
    sec                                                               ; 9fa1: 38          8
    sbc open_port_buf_hi                                              ; 9fa2: e5 a5       ..
    sta port_buf_len_hi                                               ; 9fa4: 85 a3       ..
    sec                                                               ; 9fa6: 38          8
; &9fa7 referenced 1 time by &968f
.nmi_shim_rom_src
    rts                                                               ; 9fa7: 60          `

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
    bit station_id_disable_net_nmis                                   ; 9fa8: 2c 18 fe    ,..
    pha                                                               ; 9fab: 48          H
    tya                                                               ; 9fac: 98          .
    pha                                                               ; 9fad: 48          H
    lda #0                                                            ; 9fae: a9 00       ..
    sta romsel                                                        ; 9fb0: 8d 30 fe    .0.
    jmp nmi_rx_scout                                                  ; 9fb3: 4c f2 96    L..

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
    sty nmi_jmp_hi                                                    ; 9fb6: 8c 0d 0d    ...
    sta nmi_jmp_lo                                                    ; 9fb9: 8d 0c 0d    ...
    lda romsel_copy                                                   ; 9fbc: a5 f4       ..
    sta romsel                                                        ; 9fbe: 8d 30 fe    .0.
    pla                                                               ; 9fc1: 68          h
    tay                                                               ; 9fc2: a8          .
    pla                                                               ; 9fc3: 68          h
    bit video_ula_control                                             ; 9fc4: 2c 20 fe    , .
    rti                                                               ; 9fc7: 40          @

    equs "Brian,Hugo,Jes and Roger"                                   ; 9fc8: 42 72 69... Bri

; &9fe0 referenced 2 times by &8c8e, &8d67
.sub_c9fe0
    pha                                                               ; 9fe0: 48          H
    lsr a                                                             ; 9fe1: 4a          J
    lsr a                                                             ; 9fe2: 4a          J
    lsr a                                                             ; 9fe3: 4a          J
    lsr a                                                             ; 9fe4: 4a          J
    jsr sub_c9fe9                                                     ; 9fe5: 20 e9 9f     ..
    pla                                                               ; 9fe8: 68          h
; &9fe9 referenced 1 time by &9fe5
.sub_c9fe9
    and #&0f                                                          ; 9fe9: 29 0f       ).
    cmp #&0a                                                          ; 9feb: c9 0a       ..
    bcc c9ff1                                                         ; 9fed: 90 02       ..
    adc #6                                                            ; 9fef: 69 06       i.
; &9ff1 referenced 1 time by &9fed
.c9ff1
    adc #&30 ; '0'                                                    ; 9ff1: 69 30       i0
    jsr osasci                                                        ; 9ff3: 20 e3 ff     ..            ; Write character
    sec                                                               ; 9ff6: 38          8
    rts                                                               ; 9ff7: 60          `

    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff                       ; 9ff8: ff ff ff... ...
.pydis_end

    assert <(copy_handles-1) == &2a
    assert <(dispatch_net_cmd-1) == &68
    assert <(econet_tx_rx-1) == &e7
    assert <(insert_remote_key-1) == &e7
    assert <(l0128) == &28
    assert <(l1e02-1) == &01
    assert <(l5801-1) == &00
    assert <(l5e41-1) == &40
    assert <(l6e04-1) == &03
    assert <(l84a6-1) == &a5
    assert <(l8e04-1) == &03
    assert <(l96ed-1) == &ec
    assert <(lb7f6-1) == &f5
    assert <(osword_0f_handler-1) == &b9
    assert <(osword_10_handler-1) == &73
    assert <(osword_11_handler-1) == &d3
    assert <(printer_select_handler-1) == &ce
    assert <(remote_boot_handler-1) == &99
    assert <(remote_cmd_dispatch-1) == &dd
    assert <(remote_print_handler-1) == &de
    assert <(remote_validated-1) == &d7
    assert <(return_1-1) == &f5
    assert <(rx_imm_exec-1) == &94
    assert <(rx_imm_machine_type-1) == &bd
    assert <(rx_imm_poke-1) == &b2
    assert <(set_csd_handle-1) == &23
    assert <(sub_c806f-1) == &6e
    assert <(sub_c807f-1) == &7e
    assert <(sub_c80b8-1) == &b7
    assert <(sub_c816c-1) == &6b
    assert <(sub_c81e8-1) == &e7
    assert <(sub_c82b1-1) == &b0
    assert <(sub_c82c1-1) == &c0
    assert <(sub_c82f6-1) == &f5
    assert <(sub_c8374-1) == &73
    assert <(sub_c8689-1) == &88
    assert <(sub_c88cf-1) == &ce
    assert <(sub_c8969-1) == &68
    assert <(sub_c8d21-1) == &20
    assert <(sub_c8d2a-1) == &29
    assert <(sub_c8dd7-1) == &d6
    assert <(sub_c8ed5-1) == &d4
    assert <(sub_c8ef9-1) == &f8
    assert <(sub_c90ac-1) == &ab
    assert <(sub_c9148-1) == &47
    assert <(sub_c92c8-1) == &c7
    assert <(sub_c96f6-1) == &f5
    assert <(sub_c9ad1-1) == &d0
    assert <(sub_c9aeb-1) == &ea
    assert <(sub_c9ccb-1) == &ca
    assert <(sub_c9d16-1) == &15
    assert <(svc_autoboot-1) == &18
    assert <(svc_nmi_release-1) == &65
    assert <(tube_claim_loop-1) == &ce
    assert <(tx_ctrl_exit-1) == &25
    assert <(tx_ctrl_peek-1) == &ce
    assert <(tx_ctrl_poke-1) == &d2
    assert <(tx_done_continue-1) == &b7
    assert <(tx_done_halt-1) == &a0
    assert <(tx_done_jsr-1) == &7d
    assert <(tx_done_os_proc-1) == &94
    assert <(tx_done_user_proc-1) == &86
    assert >(copy_handles-1) == &8e
    assert >(dispatch_net_cmd-1) == &80
    assert >(econet_tx_rx-1) == &8f
    assert >(insert_remote_key-1) == &84
    assert >(l0128) == &01
    assert >(l1e02-1) == &1e
    assert >(l5801-1) == &58
    assert >(l5e41-1) == &5e
    assert >(l6e04-1) == &6e
    assert >(l84a6-1) == &84
    assert >(l8e04-1) == &8e
    assert >(l96ed-1) == &96
    assert >(lb7f6-1) == &b7
    assert >(osword_0f_handler-1) == &8e
    assert >(osword_10_handler-1) == &8f
    assert >(osword_11_handler-1) == &8e
    assert >(printer_select_handler-1) == &91
    assert >(remote_boot_handler-1) == &84
    assert >(remote_cmd_dispatch-1) == &90
    assert >(remote_print_handler-1) == &91
    assert >(remote_validated-1) == &84
    assert >(return_1-1) == &80
    assert >(rx_imm_exec-1) == &9a
    assert >(rx_imm_machine_type-1) == &9a
    assert >(rx_imm_poke-1) == &9a
    assert >(set_csd_handle-1) == &8e
    assert >(sub_c806f-1) == &80
    assert >(sub_c807f-1) == &80
    assert >(sub_c80b8-1) == &80
    assert >(sub_c816c-1) == &81
    assert >(sub_c81e8-1) == &81
    assert >(sub_c82b1-1) == &82
    assert >(sub_c82c1-1) == &82
    assert >(sub_c82f6-1) == &82
    assert >(sub_c8374-1) == &83
    assert >(sub_c8689-1) == &86
    assert >(sub_c88cf-1) == &88
    assert >(sub_c8969-1) == &89
    assert >(sub_c8d21-1) == &8d
    assert >(sub_c8d2a-1) == &8d
    assert >(sub_c8dd7-1) == &8d
    assert >(sub_c8ed5-1) == &8e
    assert >(sub_c8ef9-1) == &8e
    assert >(sub_c90ac-1) == &90
    assert >(sub_c9148-1) == &91
    assert >(sub_c92c8-1) == &92
    assert >(sub_c96f6-1) == &96
    assert >(sub_c9ad1-1) == &9a
    assert >(sub_c9aeb-1) == &9a
    assert >(sub_c9ccb-1) == &9c
    assert >(sub_c9d16-1) == &9d
    assert >(svc_autoboot-1) == &82
    assert >(svc_nmi_release-1) == &96
    assert >(tube_claim_loop-1) == &8b
    assert >(tx_ctrl_exit-1) == &9d
    assert >(tx_ctrl_peek-1) == &9c
    assert >(tx_ctrl_poke-1) == &9c
    assert >(tx_done_continue-1) == &9b
    assert >(tx_done_halt-1) == &9b
    assert >(tx_done_jsr-1) == &9b
    assert >(tx_done_os_proc-1) == &9b
    assert >(tx_done_user_proc-1) == &9b
    assert copyright - rom_header == &10

save pydis_start, pydis_end

; Label references by decreasing frequency:
;     nfs_workspace:                           53
;     econet_control23_or_status2:             44
;     fs_options:                              41
;     econet_data_continue_frame:              37
;     fs_cmd_data:                             37
;     port_ws_offset:                          34
;     econet_control1_or_status1:              31
;     net_rx_ptr:                              31
;     l00f0:                                   26
;     tx_flags:                                26
;     net_tx_ptr:                              23
;     osbyte:                                  22
;     set_nmi_vector:                          22
;     c06c5:                                   20
;     port_buf_len:                            20
;     station_id_disable_net_nmis:             17
;     open_port_buf_hi:                        16
;     rx_flags:                                16
;     fs_load_addr_2:                          15
;     l00a8:                                   14
;     l0f06:                                   14
;     nmi_tx_block:                            14
;     open_port_buf:                           14
;     fs_load_addr:                            13
;     l00ab:                                   13
;     port_buf_len_hi:                         13
;     print_inline:                            13
;     tube_send_r2:                            13
;     c9872:                                   12
;     prepare_fs_cmd:                          12
;     tube_data_register_2:                    11
;     tx_result_fail:                          11
;     l00a9:                                   10
;     nfs_workspace_hi:                        10
;     tube_addr_claim:                         10
;     tube_status_register_2:                  10
;     l00c8:                                    9
;     tube_data_register_3:                     9
;     fs_error_ptr:                             8
;     l00ad:                                    8
;     l00c4:                                    8
;     net_tx_ptr_hi:                            8
;     rx_buf_offset:                            8
;     rx_src_stn:                               8
;     tube_send_r4:                             8
;     tube_status_1_and_tube_control:           8
;     c9dbf:                                    7
;     fs_cmd_csd:                               7
;     fs_cmd_urd:                               7
;     fs_crc_lo:                                7
;     l0d60:                                    7
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
;     l0015:                                    6
;     l00b4:                                    6
;     nmi_rti:                                  6
;     tube_main_loop:                           6
;     c851b:                                    5
;     c8971:                                    5
;     copy_filename:                            5
;     dispatch:                                 5
;     l00b3:                                    5
;     l0100:                                    5
;     l0106:                                    5
;     net_rx_ptr_hi:                            5
;     os_text_ptr:                              5
;     printer_buf_ptr:                          5
;     rx_ctrl:                                  5
;     rx_port:                                  5
;     scout_status:                             5
;     system_via_acr:                           5
;     tube_flag:                                5
;     tube_send_r1:                             5
;     tx_dst_net:                               5
;     c8889:                                    4
;     c8990:                                    4
;     c8f14:                                    4
;     clear_jsr_protection:                     4
;     data_tx_error:                            4
;     data_tx_last:                             4
;     discard_reset_listen:                     4
;     econet_init_flag:                         4
;     fs_boot_option:                           4
;     fs_cmd_context:                           4
;     fs_eof_flags:                             4
;     fs_sequence_nos:                          4
;     fs_server_net:                            4
;     init_tx_ctrl_block:                       4
;     l00aa:                                    4
;     l00b9:                                    4
;     l00c0:                                    4
;     l00c1:                                    4
;     l00ef:                                    4
;     l0101:                                    4
;     l0d58:                                    4
;     l0f07:                                    4
;     nmi_next_hi:                              4
;     nmi_next_lo:                              4
;     osrdsc_ptr:                               4
;     romsel_copy:                              4
;     rx_src_net:                               4
;     scout_error:                              4
;     sub_c8679:                                4
;     tube_reply_byte:                          4
;     tx_done_exit:                             4
;     tx_length:                                4
;     tx_poll_ff:                               4
;     video_ula_control:                        4
;     adlc_full_reset:                          3
;     c852d:                                    3
;     c90f7:                                    3
;     c97d3:                                    3
;     c98f8:                                    3
;     c990e:                                    3
;     c9c36:                                    3
;     c9e9c:                                    3
;     c9eb2:                                    3
;     calc_handle_offset:                       3
;     data_rx_complete:                         3
;     data_rx_tube_error:                       3
;     discard_listen:                           3
;     fs_csd_handle:                            3
;     fs_getb_buf:                              3
;     fs_messages_flag:                         3
;     fs_server_stn:                            3
;     fs_urd_handle:                            3
;     handle_to_mask_a:                         3
;     l0003:                                    3
;     l0054:                                    3
;     l00ac:                                    3
;     l00af:                                    3
;     l00b7:                                    3
;     l00ba:                                    3
;     l00ff:                                    3
;     l0df0:                                    3
;     l0f08:                                    3
;     l83af:                                    3
;     l854d:                                    3
;     l8cfb:                                    3
;     language_entry:                           3
;     match_osbyte_code:                        3
;     nmi_jmp_hi:                               3
;     nmi_jmp_lo:                               3
;     nmi_tx_block_hi:                          3
;     openl4:                                   3
;     oscli:                                    3
;     osnewl:                                   3
;     osword:                                   3
;     oswrch:                                   3
;     pad_filename_spaces:                      3
;     pydis_start:                              3
;     return_1:                                 3
;     rom_header:                               3
;     save_fscv_args:                           3
;     save_fscv_args_with_ptrs:                 3
;     saved_jsr_mask:                           3
;     scout_no_match:                           3
;     setup_tx_and_send:                        3
;     tube_claim_loop:                          3
;     tube_data_register_1:                     3
;     tube_read_string:                         3
;     tube_reply_ack:                           3
;     tx_active_start:                          3
;     tx_calc_transfer:                         3
;     tx_index:                                 3
;     ack_tx:                                   2
;     ack_tx_write_dest:                        2
;     adjust_addrs:                             2
;     adlc_rx_listen:                           2
;     c047b:                                    2
;     c0491:                                    2
;     c04b9:                                    2
;     c809d:                                    2
;     c80a0:                                    2
;     c8118:                                    2
;     c8130:                                    2
;     c817f:                                    2
;     c818b:                                    2
;     c8211:                                    2
;     c8289:                                    2
;     c8312:                                    2
;     c8379:                                    2
;     c837a:                                    2
;     c84d5:                                    2
;     c865c:                                    2
;     c86c7:                                    2
;     c86cf:                                    2
;     c86f6:                                    2
;     c8afb:                                    2
;     c8b77:                                    2
;     c8cfd:                                    2
;     c8d35:                                    2
;     c8da5:                                    2
;     c8e1c:                                    2
;     c8e27:                                    2
;     c8e6c:                                    2
;     c8e8e:                                    2
;     c8fc9:                                    2
;     c96b7:                                    2
;     c97f7:                                    2
;     c9804:                                    2
;     c98da:                                    2
;     c99a1:                                    2
;     c99f7:                                    2
;     c9a0e:                                    2
;     c9a40:                                    2
;     c9a76:                                    2
;     c9a82:                                    2
;     c9b32:                                    2
;     c9c7d:                                    2
;     c9f84:                                    2
;     call_fscv_shutdown:                       2
;     clear_fs_flag:                            2
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
;     l00cf:                                    2
;     l00f1:                                    2
;     l00f3:                                    2
;     l00fd:                                    2
;     l0102:                                    2
;     l0103:                                    2
;     l0128:                                    2
;     l0500:                                    2
;     l0700:                                    2
;     l0d1e:                                    2
;     l0d59:                                    2
;     l0e30:                                    2
;     l0f09:                                    2
;     l0f10:                                    2
;     l0f11:                                    2
;     l0f12:                                    2
;     l8373:                                    2
;     l8d08:                                    2
;     mask_to_handle:                           2
;     num01:                                    2
;     osarg1:                                   2
;     osfind:                                   2
;     osrdch:                                   2
;     parse_filename_gs:                        2
;     prepare_cmd_clv:                          2
;     prepare_fs_cmd_v:                         2
;     print_decimal:                            2
;     print_decimal_digit:                      2
;     print_dir_from_offset:                    2
;     print_file_info:                          2
;     print_hex_bytes:                          2
;     prlp1:                                    2
;     readc1:                                   2
;     remot1:                                   2
;     return_3:                                 2
;     return_5:                                 2
;     return_7:                                 2
;     return_match_osbyte:                      2
;     return_nbyte:                             2
;     return_printer_select:                    2
;     return_tube_init:                         2
;     romsel:                                   2
;     rx_extra_byte:                            2
;     rxpol2:                                   2
;     scout_complete:                           2
;     send_data_blocks:                         2
;     send_fs_reply_cmd:                        2
;     setup_tx_ptr_c0:                          2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     sub_3_from_y:                             2
;     sub_c04cb:                                2
;     sub_c835e:                                2
;     sub_c8620:                                2
;     sub_c8e45:                                2
;     sub_c99a4:                                2
;     sub_c9fe0:                                2
;     system_via_ier:                           2
;     system_via_ifr:                           2
;     system_via_sr:                            2
;     trampoline_tx_setup:                      2
;     transfer_file_blocks:                     2
;     tube_osword_read_lp:                      2
;     tube_rdch_reply:                          2
;     tube_status_register_4_and_cpu_control:   2
;     tube_transfer_addr:                       2
;     tx_ctrl_byte:                             2
;     tx_port:                                  2
;     tx_result_ok:                             2
;     tx_src_stn:                               2
;     tx_store_result:                          2
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
;     binary_version:                           1
;     brkv:                                     1
;     bspsx:                                    1
;     bsxl0:                                    1
;     bsxl1:                                    1
;     build_send_fs_cmd:                        1
;     bytex:                                    1
;     c0020:                                    1
;     c002a:                                    1
;     c0423:                                    1
;     c042d:                                    1
;     c0430:                                    1
;     c0464:                                    1
;     c046d:                                    1
;     c047d:                                    1
;     c0485:                                    1
;     c049b:                                    1
;     c04f4:                                    1
;     c0593:                                    1
;     c0645:                                    1
;     c8098:                                    1
;     c80c5:                                    1
;     c80e3:                                    1
;     c8114:                                    1
;     c811f:                                    1
;     c8140:                                    1
;     c817d:                                    1
;     c818d:                                    1
;     c818f:                                    1
;     c81df:                                    1
;     c81e6:                                    1
;     c822e:                                    1
;     c825b:                                    1
;     c8260:                                    1
;     c83ca:                                    1
;     c83cb:                                    1
;     c8401:                                    1
;     c8466:                                    1
;     c846c:                                    1
;     c8480:                                    1
;     c84f7:                                    1
;     c85eb:                                    1
;     c85f7:                                    1
;     c8613:                                    1
;     c863f:                                    1
;     c8640:                                    1
;     c869a:                                    1
;     c86d3:                                    1
;     c8737:                                    1
;     c87d3:                                    1
;     c87e6:                                    1
;     c881a:                                    1
;     c8843:                                    1
;     c884c:                                    1
;     c88d8:                                    1
;     c88de:                                    1
;     c8922:                                    1
;     c8953:                                    1
;     c8976:                                    1
;     c8981:                                    1
;     c89e6:                                    1
;     c89f2:                                    1
;     c89f5:                                    1
;     c8a0c:                                    1
;     c8a24:                                    1
;     c8a39:                                    1
;     c8a75:                                    1
;     c8ab4:                                    1
;     c8ab7:                                    1
;     c8ac4:                                    1
;     c8ad8:                                    1
;     c8b0f:                                    1
;     c8b50:                                    1
;     c8b5d:                                    1
;     c8b7a:                                    1
;     c8bb6:                                    1
;     c8bff:                                    1
;     c8c67:                                    1
;     c8c71:                                    1
;     c8ca4:                                    1
;     c8d4d:                                    1
;     c8d55:                                    1
;     c8da7:                                    1
;     c8daa:                                    1
;     c8dcc:                                    1
;     c8e35:                                    1
;     c8f09:                                    1
;     c8f1a:                                    1
;     c8f61:                                    1
;     c8f9e:                                    1
;     c8ff6:                                    1
;     c9034:                                    1
;     c9152:                                    1
;     c9196:                                    1
;     c920d:                                    1
;     c9221:                                    1
;     c931c:                                    1
;     c935d:                                    1
;     c968d:                                    1
;     c96b2:                                    1
;     c96d5:                                    1
;     c970a:                                    1
;     c9727:                                    1
;     c972a:                                    1
;     c97a0:                                    1
;     c97ad:                                    1
;     c97af:                                    1
;     c97c1:                                    1
;     c97cb:                                    1
;     c97dc:                                    1
;     c97e0:                                    1
;     c97ef:                                    1
;     c9858:                                    1
;     c986b:                                    1
;     c9885:                                    1
;     c9895:                                    1
;     c989c:                                    1
;     c98ac:                                    1
;     c98e0:                                    1
;     c999e:                                    1
;     c99e5:                                    1
;     c9a05:                                    1
;     c9a0c:                                    1
;     c9a47:                                    1
;     c9ae3:                                    1
;     c9afc:                                    1
;     c9b35:                                    1
;     c9b3f:                                    1
;     c9b6b:                                    1
;     c9bc7:                                    1
;     c9bdf:                                    1
;     c9c0a:                                    1
;     c9c1e:                                    1
;     c9c3a:                                    1
;     c9c54:                                    1
;     c9c7b:                                    1
;     c9cd5:                                    1
;     c9cef:                                    1
;     c9d11:                                    1
;     c9d18:                                    1
;     c9d1b:                                    1
;     c9d57:                                    1
;     c9d5e:                                    1
;     c9d82:                                    1
;     c9d8c:                                    1
;     c9e28:                                    1
;     c9e34:                                    1
;     c9e44:                                    1
;     c9e54:                                    1
;     c9e75:                                    1
;     c9e84:                                    1
;     c9f0f:                                    1
;     c9f81:                                    1
;     c9ff1:                                    1
;     cbset2:                                   1
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
;     dofs01:                                   1
;     dofs2:                                    1
;     dofsl5:                                   1
;     dofsl7:                                   1
;     econet_data_terminate_frame:              1
;     entry1:                                   1
;     error1:                                   1
;     evntv:                                    1
;     file1:                                    1
;     filev:                                    1
;     filev_attrib_dispatch:                    1
;     filev_save:                               1
;     floop:                                    1
;     fs2al1:                                   1
;     fs_cmd_ptr:                               1
;     fs_cmd_type:                              1
;     fs_osword_dispatch:                       1
;     fs_osword_tbl_hi:                         1
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
;     handle_to_mask:                           1
;     handshake_await_ack:                      1
;     immediate_op:                             1
;     info2:                                    1
;     init_tx_ctrl_port:                        1
;     initl:                                    1
;     install_saved_handler:                    1
;     issue_vectors_claimed:                    1
;     l0006:                                    1
;     l0013:                                    1
;     l0051:                                    1
;     l0063:                                    1
;     l0088:                                    1
;     l0094:                                    1
;     l00ae:                                    1
;     l00c2:                                    1
;     l00c7:                                    1
;     l00f7:                                    1
;     l0104:                                    1
;     l0350:                                    1
;     l0351:                                    1
;     l0355:                                    1
;     l0518:                                    1
;     l0cff:                                    1
;     l0de6:                                    1
;     l0dfe:                                    1
;     l0e0b:                                    1
;     l0e11:                                    1
;     l0e16:                                    1
;     l0ef7:                                    1
;     l0f0b:                                    1
;     l0f0c:                                    1
;     l0f0d:                                    1
;     l0f0e:                                    1
;     l0f13:                                    1
;     l0f14:                                    1
;     l0f16:                                    1
;     l0fde:                                    1
;     l0fdf:                                    1
;     l0fe0:                                    1
;     l3af0:                                    1
;     l4:                                       1
;     l8001:                                    1
;     l8002:                                    1
;     l8004:                                    1
;     l8018:                                    1
;     l8024:                                    1
;     l8049:                                    1
;     l818e:                                    1
;     l8296:                                    1
;     l8579:                                    1
;     l8c06:                                    1
;     l8d1c:                                    1
;     l8eb0:                                    1
;     l8ef7:                                    1
;     l909a:                                    1
;     l90a3:                                    1
;     l9139:                                    1
;     l91a0:                                    1
;     l91a4:                                    1
;     l91c8:                                    1
;     l9319:                                    1
;     l9456:                                    1
;     l9556:                                    1
;     l9a04:                                    1
;     l9af1:                                    1
;     l9af6:                                    1
;     l9c42:                                    1
;     l9ea7:                                    1
;     l9eaf:                                    1
;     lac85:                                    1
;     language_handler:                         1
;     loadop:                                   1
;     lodchk:                                   1
;     lodfil:                                   1
;     lodrl1:                                   1
;     lodrl2:                                   1
;     logon2:                                   1
;     loop_c0441:                               1
;     loop_c0459:                               1
;     loop_c04a4:                               1
;     loop_c04de:                               1
;     loop_c0564:                               1
;     loop_c0577:                               1
;     loop_c05c7:                               1
;     loop_c05d3:                               1
;     loop_c05e6:                               1
;     loop_c05fc:                               1
;     loop_c064c:                               1
;     loop_c066a:                               1
;     loop_c8081:                               1
;     loop_c80ad:                               1
;     loop_c8175:                               1
;     loop_c81d2:                               1
;     loop_c8262:                               1
;     loop_c8303:                               1
;     loop_c8360:                               1
;     loop_c83d0:                               1
;     loop_c8482:                               1
;     loop_c84cf:                               1
;     loop_c8508:                               1
;     loop_c85ef:                               1
;     loop_c860d:                               1
;     loop_c8624:                               1
;     loop_c866a:                               1
;     loop_c869d:                               1
;     loop_c8739:                               1
;     loop_c8768:                               1
;     loop_c876a:                               1
;     loop_c87b1:                               1
;     loop_c87e3:                               1
;     loop_c8825:                               1
;     loop_c8845:                               1
;     loop_c894a:                               1
;     loop_c8959:                               1
;     loop_c8a18:                               1
;     loop_c8b43:                               1
;     loop_c8b6b:                               1
;     loop_c8bb8:                               1
;     loop_c8bde:                               1
;     loop_c8c99:                               1
;     loop_c8ce8:                               1
;     loop_c8dc3:                               1
;     loop_c8ddb:                               1
;     loop_c8f35:                               1
;     loop_c8f4f:                               1
;     loop_c8fb4:                               1
;     loop_c900b:                               1
;     loop_c904b:                               1
;     loop_c905e:                               1
;     loop_c9117:                               1
;     loop_c9156:                               1
;     loop_c92bd:                               1
;     loop_c968f:                               1
;     loop_c99af:                               1
;     loop_c9a49:                               1
;     loop_c9a6d:                               1
;     loop_c9aa7:                               1
;     loop_c9bb1:                               1
;     loop_c9bf3:                               1
;     loop_c9c14:                               1
;     loop_c9cdc:                               1
;     loop_c9d05:                               1
;     loop_c9d33:                               1
;     loop_c9d61:                               1
;     mj:                                       1
;     nbyte1:                                   1
;     nbyte4:                                   1
;     nbyte5:                                   1
;     nbyte6:                                   1
;     netv:                                     1
;     nlisne:                                   1
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
;     openl6:                                   1
;     openl7:                                   1
;     opter1:                                   1
;     optl1:                                    1
;     osargs:                                   1
;     osbget:                                   1
;     osbput:                                   1
;     oseven:                                   1
;     osfile:                                   1
;     osgbpb:                                   1
;     osgbpb_info:                              1
;     osword_trampoline:                        1
;     parse_decimal:                            1
;     prepare_cmd_with_flag:                    1
;     print_exec_and_len:                       1
;     print_space:                              1
;     quote1:                                   1
;     rchex:                                    1
;     read_args_size:                           1
;     read_vdu_osbyte:                          1
;     read_vdu_osbyte_x0:                       1
;     readry:                                   1
;     return_10:                                1
;     return_2:                                 1
;     return_6:                                 1
;     return_8:                                 1
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
;     sub_c04c4:                                1
;     sub_c8383:                                1
;     sub_c86d7:                                1
;     sub_c86e3:                                1
;     sub_c8d92:                                1
;     sub_c9072:                                1
;     sub_c9fe9:                                1
;     tbcop1:                                   1
;     trampoline_adlc_init:                     1
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
;     c0020
;     c002a
;     c0423
;     c042d
;     c0430
;     c0464
;     c046d
;     c047b
;     c047d
;     c0485
;     c0491
;     c049b
;     c04b9
;     c04f4
;     c0593
;     c0645
;     c06c5
;     c8098
;     c809d
;     c80a0
;     c80c5
;     c80e3
;     c8114
;     c8118
;     c811f
;     c8130
;     c8140
;     c817d
;     c817f
;     c818b
;     c818d
;     c818f
;     c81df
;     c81e6
;     c8211
;     c822e
;     c825b
;     c8260
;     c8289
;     c8312
;     c8379
;     c837a
;     c83ca
;     c83cb
;     c8401
;     c8466
;     c846c
;     c8480
;     c84d5
;     c84f7
;     c851b
;     c852d
;     c85eb
;     c85f7
;     c8613
;     c863f
;     c8640
;     c865c
;     c869a
;     c86c7
;     c86cf
;     c86d3
;     c86f6
;     c8737
;     c87d3
;     c87e6
;     c881a
;     c8843
;     c884c
;     c8889
;     c88d8
;     c88de
;     c8922
;     c8953
;     c8971
;     c8976
;     c8981
;     c8990
;     c89e6
;     c89f2
;     c89f5
;     c8a0c
;     c8a24
;     c8a39
;     c8a75
;     c8ab4
;     c8ab7
;     c8ac4
;     c8ad8
;     c8afb
;     c8b0f
;     c8b50
;     c8b5d
;     c8b77
;     c8b7a
;     c8bb6
;     c8bff
;     c8c67
;     c8c71
;     c8ca4
;     c8cfd
;     c8d35
;     c8d4d
;     c8d55
;     c8da5
;     c8da7
;     c8daa
;     c8dcc
;     c8e1c
;     c8e27
;     c8e35
;     c8e6c
;     c8e8e
;     c8f09
;     c8f14
;     c8f1a
;     c8f61
;     c8f9e
;     c8fc9
;     c8ff6
;     c9034
;     c90f7
;     c9152
;     c9196
;     c920d
;     c9221
;     c931c
;     c935d
;     c968d
;     c96b2
;     c96b7
;     c96d5
;     c970a
;     c9727
;     c972a
;     c97a0
;     c97ad
;     c97af
;     c97c1
;     c97cb
;     c97d3
;     c97dc
;     c97e0
;     c97ef
;     c97f7
;     c9804
;     c9858
;     c986b
;     c9872
;     c9885
;     c9895
;     c989c
;     c98ac
;     c98da
;     c98e0
;     c98f8
;     c990e
;     c999e
;     c99a1
;     c99e5
;     c99f7
;     c9a05
;     c9a0c
;     c9a0e
;     c9a40
;     c9a47
;     c9a76
;     c9a82
;     c9ae3
;     c9afc
;     c9b32
;     c9b35
;     c9b3f
;     c9b6b
;     c9bc7
;     c9bdf
;     c9c0a
;     c9c1e
;     c9c36
;     c9c3a
;     c9c54
;     c9c7b
;     c9c7d
;     c9cd5
;     c9cef
;     c9d11
;     c9d18
;     c9d1b
;     c9d57
;     c9d5e
;     c9d82
;     c9d8c
;     c9dbf
;     c9e28
;     c9e34
;     c9e44
;     c9e54
;     c9e75
;     c9e84
;     c9e9c
;     c9eb2
;     c9f0f
;     c9f81
;     c9f84
;     c9ff1
;     l0000
;     l0001
;     l0002
;     l0003
;     l0006
;     l0012
;     l0013
;     l0014
;     l0015
;     l0051
;     l0054
;     l0055
;     l0056
;     l0063
;     l0088
;     l0094
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
;     l0500
;     l0518
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
;     l1e02
;     l3af0
;     l5801
;     l5e41
;     l6e04
;     l8001
;     l8002
;     l8004
;     l8011
;     l8018
;     l8024
;     l8049
;     l818e
;     l8296
;     l8373
;     l83af
;     l84a6
;     l854d
;     l854e
;     l8579
;     l8c06
;     l8cf8
;     l8cfb
;     l8d08
;     l8d1c
;     l8e04
;     l8eb0
;     l8ef7
;     l909a
;     l90a3
;     l9139
;     l91a0
;     l91a4
;     l91c8
;     l9319
;     l9456
;     l9556
;     l96ed
;     l9a04
;     l9af1
;     l9af6
;     l9c42
;     l9ea7
;     l9eaf
;     lac85
;     lb7f6
;     loop_c0441
;     loop_c0459
;     loop_c04a4
;     loop_c04de
;     loop_c0564
;     loop_c0577
;     loop_c05c7
;     loop_c05d3
;     loop_c05e6
;     loop_c05fc
;     loop_c064c
;     loop_c066a
;     loop_c8081
;     loop_c80ad
;     loop_c8175
;     loop_c81d2
;     loop_c8262
;     loop_c8303
;     loop_c8360
;     loop_c83d0
;     loop_c8482
;     loop_c84cf
;     loop_c8508
;     loop_c85ef
;     loop_c860d
;     loop_c8624
;     loop_c866a
;     loop_c869d
;     loop_c8739
;     loop_c8768
;     loop_c876a
;     loop_c87b1
;     loop_c87e3
;     loop_c8825
;     loop_c8845
;     loop_c894a
;     loop_c8959
;     loop_c8a18
;     loop_c8b43
;     loop_c8b6b
;     loop_c8bb8
;     loop_c8bde
;     loop_c8c99
;     loop_c8ce8
;     loop_c8dc3
;     loop_c8ddb
;     loop_c8f35
;     loop_c8f4f
;     loop_c8fb4
;     loop_c900b
;     loop_c904b
;     loop_c905e
;     loop_c9117
;     loop_c9156
;     loop_c92bd
;     loop_c968f
;     loop_c99af
;     loop_c9a49
;     loop_c9a6d
;     loop_c9aa7
;     loop_c9bb1
;     loop_c9bf3
;     loop_c9c14
;     loop_c9cdc
;     loop_c9d05
;     loop_c9d33
;     loop_c9d61
;     sub_c0414
;     sub_c04c4
;     sub_c04cb
;     sub_c806f
;     sub_c807f
;     sub_c80b8
;     sub_c816c
;     sub_c81e8
;     sub_c82b1
;     sub_c82c1
;     sub_c82f6
;     sub_c835e
;     sub_c8374
;     sub_c8383
;     sub_c84a5
;     sub_c8620
;     sub_c8679
;     sub_c8689
;     sub_c86d7
;     sub_c86e3
;     sub_c88cf
;     sub_c8969
;     sub_c8d21
;     sub_c8d2a
;     sub_c8d92
;     sub_c8dd7
;     sub_c8e03
;     sub_c8e45
;     sub_c8ed5
;     sub_c8ef9
;     sub_c9072
;     sub_c90ac
;     sub_c9148
;     sub_c92c8
;     sub_c96ec
;     sub_c96f6
;     sub_c99a4
;     sub_c9a03
;     sub_c9ad1
;     sub_c9aeb
;     sub_c9af0
;     sub_c9af5
;     sub_c9c40
;     sub_c9ccb
;     sub_c9d16
;     sub_c9ea6
;     sub_c9eae
;     sub_c9fe0
;     sub_c9fe9

; Stats:
;     Total size (Code + Data) = 8192 bytes
;     Code                     = 7424 bytes (91%)
;     Data                     = 768 bytes (9%)
;
;     Number of instructions   = 3572
;     Number of data bytes     = 479 bytes
;     Number of data words     = 0 bytes
;     Number of string bytes   = 289 bytes
;     Number of strings        = 35
