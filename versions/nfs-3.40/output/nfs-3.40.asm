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
l0006                                   = &0006
zp_temp_10                              = &0010
zp_temp_11                              = &0011
tube_data_ptr                           = &0012
tube_data_ptr_hi                        = &0013
tube_claim_flag                         = &0014
tube_claimed_id                         = &0015
zp_63                                   = &005f
l0063                                   = &0063
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
ws_page                                 = &00a8
svc_state                               = &00a9
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
nfs_temp                                = &00cd
rom_svc_num                             = &00ce
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

.reloc_zp_src

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
; 12-entry table at &0500). The R2 command byte is stored at &55
; before dispatch via JMP (&0500).
; ***************************************************************************************
; &931c referenced 1 time by &8178
.nmi_workspace_start
.tube_brk_handler
    lda #&ff                                                          ; 931c: a9 ff       ..  :0016[1]   ; A=&FF: signal error to co-processor via R4
    jsr tube_send_r4                                                  ; 931e: 20 9e 06     .. :0018[1]   ; Send &FF error signal to Tube R4
    lda tube_data_register_2                                          ; 9321: ad e3 fe    ... :001b[1]   ; Flush any pending R2 byte
    lda #0                                                            ; 9324: a9 00       ..  :001e[1]   ; A=0: send zero prefix to R2
; &9326 referenced 1 time by &0626[4]
.tube_send_zero_r2
    jsr tube_send_r2                                                  ; 9326: 20 95 06     .. :0020[1]   ; Send zero prefix byte via R2
    tay                                                               ; 9329: a8          .   :0023[1]   ; Y=0: start of error block at (&FD)
    lda (brk_ptr),y                                                   ; 932a: b1 fd       ..  :0024[1]   ; Load error number from (&FD),0
    jsr tube_send_r2                                                  ; 932c: 20 95 06     .. :0026[1]   ; Send error number via R2
; &932f referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 932f: c8          .   :0029[1]   ; Advance to next error string byte
; &9330 referenced 1 time by &053d[3]
.tube_send_error_byte
    lda (brk_ptr),y                                                   ; 9330: b1 fd       ..  :002a[1]   ; Load next error string byte
    jsr tube_send_r2                                                  ; 9332: 20 95 06     .. :002c[1]   ; Send error string byte via R2
    tax                                                               ; 9335: aa          .   :002f[1]   ; Zero byte = end of error string
    bne tube_brk_send_loop                                            ; 9336: d0 f7       ..  :0030[1]   ; Loop until zero terminator sent
; &9338 referenced 1 time by &046a[2]
.tube_reset_stack
    ldx #&ff                                                          ; 9338: a2 ff       ..  :0032[1]   ; Reset stack pointer to top
    txs                                                               ; 933a: 9a          .   :0034[1]   ; TXS: set stack pointer from X
    cli                                                               ; 933b: 58          X   :0035[1]   ; Enable interrupts for main loop
; &933c referenced 6 times by &0044[1], &057f[3], &05a6[3], &0604[4], &0665[4], &0692[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; 933c: 2c e0 fe    ,.. :0036[1]   ; BIT R1 status: check WRCH request
    bpl tube_poll_r2                                                  ; 933f: 10 06       ..  :0039[1]   ; R1 not ready: check R2 instead
; &9341 referenced 1 time by &0049[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; 9341: ad e1 fe    ... :003b[1]   ; Read character from Tube R1 data
    jsr oswrch                                                        ; 9344: 20 ee ff     .. :003e[1]   ; Write character
; &9347 referenced 1 time by &0039[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 9347: 2c e2 fe    ,.. :0041[1]   ; BIT R2 status: check command byte
    bpl tube_main_loop                                                ; 934a: 10 f0       ..  :0044[1]   ; R2 not ready: loop back to R1 check
    bit tube_status_1_and_tube_control                                ; 934c: 2c e0 fe    ,.. :0046[1]   ; Re-check R1: WRCH has priority over R2
    bmi tube_handle_wrch                                              ; 934f: 30 f0       0.  :0049[1]   ; R1 ready: handle WRCH first
    ldx tube_data_register_2                                          ; 9351: ae e3 fe    ... :004b[1]   ; Read command byte from Tube R2 data
    stx tube_jmp_target                                               ; 9354: 86 51       .Q  :004e[1]   ; Self-modify JMP low byte for dispatch
.tube_dispatch_cmd
tube_jmp_target = tube_dispatch_cmd+1
    jmp (tube_dispatch_table)                                         ; 9356: 6c 00 05    l.. :0050[1]   ; Dispatch to handler via indirect JMP

; &9357 referenced 1 time by &004e[1]
; &9359 referenced 2 times by &04d7[2], &04e7[2]
.tube_transfer_addr
    equb 0                                                            ; 9359: 00          .   :0053[1]
; &935a referenced 3 times by &04af[2], &04cd[2], &04ec[2]
.tube_xfer_page
    equb &80                                                          ; 935a: 80          .   :0054[1]
; &935b referenced 2 times by &04b3[2], &04f6[2]
.tube_xfer_addr_2
    equb 0                                                            ; 935b: 00          .   :0055[1]
; &935c referenced 2 times by &04b7[2], &04f4[2]
.tube_xfer_addr_3
    equb 0                                                            ; 935c: 00          .   :0056[1]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock nmi_workspace_start, *, reloc_zp_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear nmi_workspace_start, &0057

    ; Set the program counter to the next position in the binary file.
    org reloc_zp_src + (* - nmi_workspace_start)

.reloc_p4_src

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
;   &04D2: sub_c04d2 — extract relocation address from ROM table
; ***************************************************************************************
; &935d referenced 1 time by &815e
.tube_code_page4
    jmp tube_begin                                                    ; 935d: 4c 7d 04    L}. :0400[2]   ; JMP to BEGIN startup entry

.tube_escape_entry
    jmp tube_escape_check                                             ; 9360: 4c a7 06    L.. :0403[2]   ; JMP to tube_escape_check (&06A7)

; &9363 referenced 10 times by &0493[2], &04c8[2], &8b5d, &8b74, &8bd1, &8e19, &99d1, &9a3a, &9f75, &9f7d
.tube_addr_claim
    cmp #&80                                                          ; 9363: c9 80       ..  :0406[2]   ; A>=&80: address claim; A<&80: data transfer
    bcc tube_transfer_setup                                           ; 9365: 90 26       .&  :0408[2]   ; A<&80: data transfer setup (SENDW)
    cmp #&c0                                                          ; 9367: c9 c0       ..  :040a[2]   ; A>=&C0: new address claim from another host
    bcs addr_claim_external                                           ; 9369: b0 15       ..  :040c[2]   ; C=1: external claim, check ownership
    ora #&40 ; '@'                                                    ; 936b: 09 40       .@  :040e[2]   ; Map &80-&BF range to &C0-&FF for comparison
    cmp tube_claimed_id                                               ; 936d: c5 15       ..  :0410[2]   ; Is this for our currently-claimed address?
    bne return_tube_init                                              ; 936f: d0 1b       ..  :0412[2]   ; Match: we own it, return (no release)
; &9371 referenced 1 time by &0464[2]
.tube_send_release
    lda #5                                                            ; 9371: a9 05       ..  :0414[2]   ; A=5: Tube release request code
    jsr tube_send_r4                                                  ; 9373: 20 9e 06     .. :0416[2]   ; Send release code via R4
    lda tube_claimed_id                                               ; 9376: a5 15       ..  :0419[2]   ; Load current Tube claim ID
    jsr tube_send_r4                                                  ; 9378: 20 9e 06     .. :041b[2]   ; Send claim ID via R4
; &937b referenced 1 time by &8170
.tube_post_init
    lda #&80                                                          ; 937b: a9 80       ..  :041e[2]   ; &80 sentinel: clear address claim
    sta tube_claim_flag                                               ; 937d: 85 14       ..  :0420[2]   ; Store to claim-in-progress flag
    rts                                                               ; 937f: 60          `   :0422[2]   ; Return from tube_post_init

; &9380 referenced 1 time by &040c[2]
.addr_claim_external
    asl tube_claim_flag                                               ; 9380: 06 14       ..  :0423[2]   ; Another host claiming; check if we're owner
    bcs accept_new_claim                                              ; 9382: b0 06       ..  :0425[2]   ; C=1: we have an active claim
    cmp tube_claimed_id                                               ; 9384: c5 15       ..  :0427[2]   ; Compare with our claimed address
    beq return_tube_init                                              ; 9386: f0 04       ..  :0429[2]   ; Match: return (we already have it)
    clc                                                               ; 9388: 18          .   :042b[2]   ; Not ours: CLC = we don't own this address
    rts                                                               ; 9389: 60          `   :042c[2]   ; Return with C=0 (claim denied)

; &938a referenced 1 time by &0425[2]
.accept_new_claim
    sta tube_claimed_id                                               ; 938a: 85 15       ..  :042d[2]   ; Accept new claim: update our address
; &938c referenced 2 times by &0412[2], &0429[2]
.return_tube_init
    rts                                                               ; 938c: 60          `   :042f[2]   ; Return with address updated

; &938d referenced 1 time by &0408[2]
.tube_transfer_setup
    php                                                               ; 938d: 08          .   :0430[2]   ; PHP: save interrupt state
    sei                                                               ; 938e: 78          x   :0431[2]   ; SEI: disable interrupts for R4 protocol
.setup_data_transfer
    sty tube_data_ptr_hi                                              ; 938f: 84 13       ..  :0432[2]   ; Save 16-bit transfer address from (X,Y)
    stx tube_data_ptr                                                 ; 9391: 86 12       ..  :0434[2]   ; Store address pointer low byte
    jsr tube_send_r4                                                  ; 9393: 20 9e 06     .. :0436[2]   ; Send transfer type byte to co-processor
    tax                                                               ; 9396: aa          .   :0439[2]   ; X = transfer type for table lookup
    ldy #3                                                            ; 9397: a0 03       ..  :043a[2]   ; Y=3: send 4 bytes (address + claimed addr)
    lda tube_claimed_id                                               ; 9399: a5 15       ..  :043c[2]   ; Send our claimed address + 4-byte xfer addr
    jsr tube_send_r4                                                  ; 939b: 20 9e 06     .. :043e[2]   ; Send transfer address byte
; &939e referenced 1 time by &0447[2]
.send_xfer_addr_bytes
    lda (tube_data_ptr),y                                             ; 939e: b1 12       ..  :0441[2]   ; Load transfer address byte from (X,Y)
    jsr tube_send_r4                                                  ; 93a0: 20 9e 06     .. :0443[2]   ; Send address byte to co-processor via R4
    dey                                                               ; 93a3: 88          .   :0446[2]   ; Previous byte (big-endian: 3,2,1,0)
    bpl send_xfer_addr_bytes                                          ; 93a4: 10 f8       ..  :0447[2]   ; Loop for all 4 address bytes
    jsr tube_send_r4                                                  ; 93a6: 20 9e 06     .. :0449[2]   ; Send claimed address via R4
    ldy #&18                                                          ; 93a9: a0 18       ..  :044c[2]   ; Y=&18: enable Tube control register
    sty tube_status_1_and_tube_control                                ; 93ab: 8c e0 fe    ... :044e[2]   ; Enable Tube interrupt generation
    lda r2_cmd_table,x                                                ; 93ae: bd 18 05    ... :0451[2]   ; Look up Tube control bits for this xfer type
    sta tube_status_1_and_tube_control                                ; 93b1: 8d e0 fe    ... :0454[2]   ; Apply transfer-specific control bits
    lsr a                                                             ; 93b4: 4a          J   :0457[2]   ; LSR: check bit 2 (2-byte flush needed?)
    lsr a                                                             ; 93b5: 4a          J   :0458[2]   ; LSR: shift bit 2 to carry
; &93b6 referenced 1 time by &045c[2]
.poll_r4_copro_ack
    bit tube_status_register_4_and_cpu_control                        ; 93b6: 2c e6 fe    ,.. :0459[2]   ; Poll R4 status for co-processor response
    bvc poll_r4_copro_ack                                             ; 93b9: 50 fb       P.  :045c[2]   ; Bit 6 clear: not ready, keep polling
    bcs flush_r3_nmi_check                                            ; 93bb: b0 0d       ..  :045e[2]   ; R4 bit 7: co-processor acknowledged transfer
    cpx #4                                                            ; 93bd: e0 04       ..  :0460[2]   ; Type 4 = SENDW (host-to-parasite word xfer)
    bne skip_nmi_release                                              ; 93bf: d0 17       ..  :0462[2]   ; Not SENDW type: skip release path
; &93c1 referenced 1 time by &048f[2]
.tube_sendw_complete
    jsr tube_send_release                                             ; 93c1: 20 14 04     .. :0464[2]   ; SENDW complete: release, sync, restart
    jsr tube_send_r2                                                  ; 93c4: 20 95 06     .. :0467[2]   ; Sync via R2 send
    jmp tube_reset_stack                                              ; 93c7: 4c 32 00    L2. :046a[2]   ; Restart Tube main loop

; &93ca referenced 1 time by &045e[2]
.flush_r3_nmi_check
    bit tube_data_register_3                                          ; 93ca: 2c e5 fe    ,.. :046d[2]   ; Flush R3 data (first byte)
    bit tube_data_register_3                                          ; 93cd: 2c e5 fe    ,.. :0470[2]   ; Flush R3 data (second byte)
.copro_ack_nmi_check
    lsr a                                                             ; 93d0: 4a          J   :0473[2]   ; LSR: check bit 0 (NMI used?)
    bcc skip_nmi_release                                              ; 93d1: 90 05       ..  :0474[2]   ; C=0: NMI not used, skip NMI release
    ldy #&88                                                          ; 93d3: a0 88       ..  :0476[2]   ; Release Tube NMI (transfer used interrupts)
    sty tube_status_1_and_tube_control                                ; 93d5: 8c e0 fe    ... :0478[2]   ; Write &88 to Tube control to release NMI
; &93d8 referenced 2 times by &0462[2], &0474[2]
.skip_nmi_release
    plp                                                               ; 93d8: 28          (   :047b[2]   ; Restore interrupt state
.return_tube_xfer
    rts                                                               ; 93d9: 60          `   :047c[2]   ; Return from transfer setup

; &93da referenced 1 time by &0400[2]
.tube_begin
    cli                                                               ; 93da: 58          X   :047d[2]   ; BEGIN: enable interrupts for Tube host code
    bcs claim_addr_ff                                                 ; 93db: b0 11       ..  :047e[2]   ; C=1: hard break, claim addr &FF
    bne check_break_type                                              ; 93dd: d0 03       ..  :0480[2]   ; C=0, A!=0: re-init path
    jmp tube_reply_ack                                                ; 93df: 4c 9c 05    L.. :0482[2]   ; Z=1 from C=0 path: just acknowledge

; &93e2 referenced 1 time by &0480[2]
.check_break_type
    ldx #0                                                            ; 93e2: a2 00       ..  :0485[2]   ; X=0 for OSBYTE
    ldy #&ff                                                          ; 93e4: a0 ff       ..  :0487[2]   ; Y=&FF for OSBYTE
    lda #osbyte_read_write_last_break_type                            ; 93e6: a9 fd       ..  :0489[2]   ; OSBYTE &FD: what type of reset was this?
    jsr osbyte                                                        ; 93e8: 20 f4 ff     .. :048b[2]   ; Read type of last reset
    txa                                                               ; 93eb: 8a          .   :048e[2]   ; X=value of type of last reset
    beq tube_sendw_complete                                           ; 93ec: f0 d3       ..  :048f[2]   ; Soft break (X=0): re-init Tube and restart
; &93ee referenced 2 times by &047e[2], &0496[2]
.claim_addr_ff
    lda #&ff                                                          ; 93ee: a9 ff       ..  :0491[2]   ; Claim address &FF (startup = highest prio)
    jsr tube_addr_claim                                               ; 93f0: 20 06 04     .. :0493[2]   ; Request address claim from Tube system
    bcc claim_addr_ff                                                 ; 93f3: 90 f9       ..  :0496[2]   ; C=0: claim failed, retry
    jsr tube_init_reloc                                               ; 93f5: 20 cb 04     .. :0498[2]   ; Init reloc pointers from ROM header
; &93f8 referenced 1 time by &04bd[2]
.next_rom_page
    lda #7                                                            ; 93f8: a9 07       ..  :049b[2]   ; R4 cmd 7: SENDW to send ROM to parasite
    jsr tube_claim_default                                            ; 93fa: 20 c4 04     .. :049d[2]   ; Set up Tube for SENDW transfer
    ldy #0                                                            ; 93fd: a0 00       ..  :04a0[2]   ; Y=0: start at beginning of page
    sty zp_ptr_lo                                                     ; 93ff: 84 00       ..  :04a2[2]   ; Store to zero page pointer low byte
; &9401 referenced 1 time by &04ad[2]
.send_rom_page_bytes
    lda (zp_ptr_lo),y                                                 ; 9401: b1 00       ..  :04a4[2]   ; Send 256-byte page via R3, byte at a time
    sta tube_data_register_3                                          ; 9403: 8d e5 fe    ... :04a6[2]   ; Write byte to Tube R3 data register
    lda rom_header                                                    ; 9406: ad 00 80    ... :04a9[2]   ; Load ROM header byte for TX
    iny                                                               ; 9409: c8          .   :04ac[2]   ; Next byte in page
    bne send_rom_page_bytes                                           ; 940a: d0 f5       ..  :04ad[2]   ; Loop for all 256 bytes
    inc tube_xfer_page                                                ; 940c: e6 54       .T  :04af[2]   ; Increment 24-bit destination addr
    bne skip_addr_carry                                               ; 940e: d0 06       ..  :04b1[2]   ; No carry: skip higher bytes
    inc tube_xfer_addr_2                                              ; 9410: e6 55       .U  :04b3[2]   ; Carry into second byte
    bne skip_addr_carry                                               ; 9412: d0 02       ..  :04b5[2]   ; No carry: skip third byte
    inc tube_xfer_addr_3                                              ; 9414: e6 56       .V  :04b7[2]   ; Carry into third byte
; &9416 referenced 2 times by &04b1[2], &04b5[2]
.skip_addr_carry
    inc zp_ptr_hi                                                     ; 9416: e6 01       ..  :04b9[2]   ; Increment page counter
    bit zp_ptr_hi                                                     ; 9418: 24 01       $.  :04bb[2]   ; Bit 6 set = all pages transferred
    bvc next_rom_page                                                 ; 941a: 50 dc       P.  :04bd[2]   ; More pages: loop back to SENDW
    jsr tube_init_reloc                                               ; 941c: 20 cb 04     .. :04bf[2]   ; Re-init reloc pointers for final claim
    lda #4                                                            ; 941f: a9 04       ..  :04c2[2]   ; A=4: transfer type for final address claim
; &9421 referenced 1 time by &049d[2]
.tube_claim_default
    ldy #0                                                            ; 9421: a0 00       ..  :04c4[2]   ; Y=0: transfer address low byte
    ldx #&53 ; 'S'                                                    ; 9423: a2 53       .S  :04c6[2]   ; X=&53: transfer address high byte (&0053)
    jmp tube_addr_claim                                               ; 9425: 4c 06 04    L.. :04c8[2]   ; Claim Tube address for transfer

; ***************************************************************************************
; Initialise relocation address for ROM transfer
; 
; Sets source page to &8000 and page counter to &80. Checks
; ROM type bit 5 for a relocation address in the ROM header;
; if present, extracts the 4-byte address from after the
; copyright string. Otherwise uses default &8000 start.
; ***************************************************************************************
; &9428 referenced 2 times by &0498[2], &04bf[2]
.tube_init_reloc
    lda #&80                                                          ; 9428: a9 80       ..  :04cb[2]   ; Init: start sending from &8000
    sta tube_xfer_page                                                ; 942a: 85 54       .T  :04cd[2]   ; Store &80 as source page high byte
    sta zp_ptr_hi                                                     ; 942c: 85 01       ..  :04cf[2]   ; Store &80 as page counter initial value
    lda #&20 ; ' '                                                    ; 942e: a9 20       .   :04d1[2]   ; A=&20: bit 5 mask for ROM type check
    and rom_type                                                      ; 9430: 2d 06 80    -.. :04d3[2]   ; ROM type bit 5: reloc address in header?
    tay                                                               ; 9433: a8          .   :04d6[2]   ; Y = 0 or &20 (reloc flag)
    sty tube_transfer_addr                                            ; 9434: 84 53       .S  :04d7[2]   ; Store as transfer address selector
    beq store_xfer_end_addr                                           ; 9436: f0 19       ..  :04d9[2]   ; No reloc addr: use defaults
    ldx copyright_offset                                              ; 9438: ae 07 80    ... :04db[2]   ; Skip past copyright string to find reloc addr
; &943b referenced 1 time by &04e2[2]
.scan_copyright_end
    inx                                                               ; 943b: e8          .   :04de[2]   ; Skip past null-terminated copyright string
    lda rom_header,x                                                  ; 943c: bd 00 80    ... :04df[2]   ; Load next byte from ROM header
    bne scan_copyright_end                                            ; 943f: d0 fa       ..  :04e2[2]   ; Loop until null terminator found
    lda lang_entry_lo,x                                               ; 9441: bd 01 80    ... :04e4[2]   ; Read 4-byte reloc address from ROM header
    sta tube_transfer_addr                                            ; 9444: 85 53       .S  :04e7[2]   ; Store reloc addr byte 1 as transfer addr
    lda lang_entry_hi,x                                               ; 9446: bd 02 80    ... :04e9[2]   ; Load reloc addr byte 2
    sta tube_xfer_page                                                ; 9449: 85 54       .T  :04ec[2]   ; Store as source page start
    ldy service_entry,x                                               ; 944b: bc 03 80    ... :04ee[2]   ; Load reloc addr byte 3
    lda svc_entry_lo,x                                                ; 944e: bd 04 80    ... :04f1[2]   ; Load reloc addr byte 4 (highest)
; &9451 referenced 1 time by &04d9[2]
.store_xfer_end_addr
    sta tube_xfer_addr_3                                              ; 9451: 85 56       .V  :04f4[2]   ; Store high byte of end address
    sty tube_xfer_addr_2                                              ; 9453: 84 55       .U  :04f6[2]   ; Store byte 3 of end address
    rts                                                               ; 9455: 60          `   :04f8[2]   ; Return with pointers initialised


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, reloc_p4_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &04f9

    ; Set the program counter to the next position in the binary file.
    org reloc_p4_src + (* - tube_code_page4)

.reloc_p5_src

; Move 3: &9456 to &0500 for length 256
    org &0500
; ***************************************************************************************
; Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)
; 
; Copied from ROM at &944D during init. Contains:
;   &0500: tube_dispatch_table — 12-entry handler address table
;   &0518: R2 command byte table — 8 even command bytes (&00-&0E)
;   &0520: tube_osbput — write byte to file
;   &052D: tube_osbget — read byte from file
;   &0537: tube_osrdch — read character
;   &053A: tube_rdch_reply — ROR carry into byte, send via R2
;   &053D: tube_release_return — dead code (unreferenced)
;   &0542: tube_osfind — open file
;   &0552: tube_osfind_close — close file (A=0)
;   &055E: tube_osargs — file argument read/write
;   &0582: tube_read_string — read CR-terminated string into &0700
;   &0596: tube_oscli — execute * command
;   &059C: tube_reply_ack — send &7F acknowledge
;   &059E: tube_reply_byte — send byte and return to main loop
;   &05A9: tube_osfile — whole file operation
; ***************************************************************************************
; &9456 referenced 2 times by &0050[1], &8164
.tube_dispatch_table
    equb &37, 5, &96, 5, &f2, 5,   7, 6, &27, 6, &68, 6, &5e, 5       ; 9456: 37 05 96... 7.. :0500[3]
    equb &2d, 5, &20, 5, &42, 5, &a9, 5, &d1, 5                       ; 9464: 2d 05 20... -.  :050e[3]
; &946e referenced 1 time by &0451[2]
.r2_cmd_table
    equb &86, &88, &96, &98, &18, &18, &82, &18                       ; 946e: 86 88 96... ... :0518[3]

.tube_osbput
    jsr tube_read_r2                                                  ; 9476: 20 c5 06     .. :0520[3]   ; Read channel handle from R2
    tay                                                               ; 9479: a8          .   :0523[3]   ; Y=channel handle from R2
    jsr tube_read_r2                                                  ; 947a: 20 c5 06     .. :0524[3]   ; Read data byte from R2 for BPUT
.tube_poll_r1_wrch
    jsr osbput                                                        ; 947d: 20 d4 ff     .. :0527[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 9480: 4c 9c 05    L.. :052a[3]   ; BPUT done: send acknowledge, return

.tube_osbget
    jsr tube_read_r2                                                  ; 9483: 20 c5 06     .. :052d[3]   ; Read channel handle from R2
    tay                                                               ; 9486: a8          .   :0530[3]   ; Y=channel handle for OSBGET; Y=file handle
    jsr osbget                                                        ; 9487: 20 d7 ff     .. :0531[3]   ; Read a single byte from an open file Y
    jmp tube_rdch_reply                                               ; 948a: 4c 3a 05    L:. :0534[3]   ; Send carry+byte reply (BGET result)

.tube_osrdch
    jsr osrdch                                                        ; 948d: 20 e0 ff     .. :0537[3]   ; Read a character from the current input stream
; &9490 referenced 2 times by &0534[3], &05ef[3]
.tube_rdch_reply
    ror a                                                             ; 9490: 6a          j   :053a[3]   ; ROR A: encode carry (error flag) into bit 7
; Overlapping code: bytes &053B-&053D (20 95 06) are
; JSR tube_send_r2 when falling through from ROR A
; above. tube_release_return at &053D is dead code.
    equb &20, &95                                                     ; 9491: 20 95        .  :053b[3]   ; = JSR tube_send_r2 (overlaps &053D entry)

.tube_release_return
    asl tube_send_error_byte                                          ; 9493: 06 2a       .*  :053d[3]   ; Shift error flag for test
    jmp tube_reply_byte                                               ; 9495: 4c 9e 05    L.. :053f[3]   ; JMP tube_reply_byte (dead code path)

.tube_osfind
    jsr tube_read_r2                                                  ; 9498: 20 c5 06     .. :0542[3]   ; Read open mode from R2
    beq tube_osfind_close                                             ; 949b: f0 0b       ..  :0545[3]   ; A=0: close file, else open with filename
    pha                                                               ; 949d: 48          H   :0547[3]   ; Save open mode while reading filename
    jsr tube_read_string                                              ; 949e: 20 82 05     .. :0548[3]   ; Read filename string from R2 into &0700
    pla                                                               ; 94a1: 68          h   :054b[3]   ; Recover open mode from stack
    jsr osfind                                                        ; 94a2: 20 ce ff     .. :054c[3]   ; Open or close file(s)
    jmp tube_reply_byte                                               ; 94a5: 4c 9e 05    L.. :054f[3]   ; Send file handle result to co-processor

; &94a8 referenced 1 time by &0545[3]
.tube_osfind_close
    jsr tube_read_r2                                                  ; 94a8: 20 c5 06     .. :0552[3]   ; OSFIND close: read handle from R2
    tay                                                               ; 94ab: a8          .   :0555[3]   ; Y=handle to close
    lda #osfind_close                                                 ; 94ac: a9 00       ..  :0556[3]   ; A=0: close command for OSFIND
    jsr osfind                                                        ; 94ae: 20 ce ff     .. :0558[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94b1: 4c 9c 05    L.. :055b[3]   ; Close done: send acknowledge, return

.tube_osargs
    jsr tube_read_r2                                                  ; 94b4: 20 c5 06     .. :055e[3]   ; Read file handle from R2
    tay                                                               ; 94b7: a8          .   :0561[3]   ; Y=file handle for OSARGS
.tube_read_params
    ldx #4                                                            ; 94b8: a2 04       ..  :0562[3]   ; Read 4-byte arg + reason from R2 into ZP
; &94ba referenced 1 time by &056a[3]
.read_osargs_params
    jsr tube_read_r2                                                  ; 94ba: 20 c5 06     .. :0564[3]   ; Read next param byte from R2
    sta escape_flag,x                                                 ; 94bd: 95 ff       ..  :0567[3]   ; Params stored at &00-&03 (little-endian)
    dex                                                               ; 94bf: ca          .   :0569[3]   ; Decrement byte counter
    bne read_osargs_params                                            ; 94c0: d0 f8       ..  :056a[3]   ; Loop for 4 bytes
    jsr tube_read_r2                                                  ; 94c2: 20 c5 06     .. :056c[3]   ; Read OSARGS reason code from R2
    jsr osargs                                                        ; 94c5: 20 da ff     .. :056f[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 94c8: 20 95 06     .. :0572[3]   ; Send result A back to co-processor
    ldx #3                                                            ; 94cb: a2 03       ..  :0575[3]   ; Return 4-byte result from ZP &00-&03
; &94cd referenced 1 time by &057d[3]
.send_osargs_result
    lda zp_ptr_lo,x                                                   ; 94cd: b5 00       ..  :0577[3]   ; Load result byte from zero page
    jsr tube_send_r2                                                  ; 94cf: 20 95 06     .. :0579[3]   ; Send byte to co-processor via R2
    dex                                                               ; 94d2: ca          .   :057c[3]   ; Previous byte (count down)
    bpl send_osargs_result                                            ; 94d3: 10 f8       ..  :057d[3]   ; Loop for all 4 bytes
    jmp tube_main_loop                                                ; 94d5: 4c 36 00    L6. :057f[3]   ; Return to Tube main loop

; &94d8 referenced 3 times by &0548[3], &0596[3], &05b3[3]
.tube_read_string
    ldx #0                                                            ; 94d8: a2 00       ..  :0582[3]   ; X=0: initialise string buffer index
    ldy #0                                                            ; 94da: a0 00       ..  :0584[3]   ; X=0, Y=0: buffer at &0700, offset 0
; &94dc referenced 1 time by &0591[3]
.strnh
    jsr tube_read_r2                                                  ; 94dc: 20 c5 06     .. :0586[3]   ; Read next string byte from R2
    sta l0700,y                                                       ; 94df: 99 00 07    ... :0589[3]   ; Store byte in string buffer at &0700+Y
    iny                                                               ; 94e2: c8          .   :058c[3]   ; Next buffer position
    beq string_buf_done                                               ; 94e3: f0 04       ..  :058d[3]   ; Y overflow: string too long, truncate
    cmp #&0d                                                          ; 94e5: c9 0d       ..  :058f[3]   ; Check for CR terminator
    bne strnh                                                         ; 94e7: d0 f3       ..  :0591[3]   ; Not CR: continue reading string
; &94e9 referenced 1 time by &058d[3]
.string_buf_done
    ldy #7                                                            ; 94e9: a0 07       ..  :0593[3]   ; Y=7: set XY=&0700 for OSCLI/OSFIND
    rts                                                               ; 94eb: 60          `   :0595[3]   ; Return with XY pointing to &0700

.tube_oscli
    jsr tube_read_string                                              ; 94ec: 20 82 05     .. :0596[3]   ; Read command string from R2
    jsr oscli                                                         ; 94ef: 20 f7 ff     .. :0599[3]   ; Execute * command via OSCLI
; &94f2 referenced 3 times by &0482[2], &052a[3], &055b[3]
.tube_reply_ack
    lda #&7f                                                          ; 94f2: a9 7f       ..  :059c[3]   ; &7F = success acknowledgement
; &94f4 referenced 4 times by &053f[3], &054f[3], &05a1[3], &067d[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 94f4: 2c e2 fe    ,.. :059e[3]   ; Poll R2 status until ready
    bvc tube_reply_byte                                               ; 94f7: 50 fb       P.  :05a1[3]   ; Bit 6 clear: not ready, loop
    sta tube_data_register_2                                          ; 94f9: 8d e3 fe    ... :05a3[3]   ; Write byte to R2 data register
; &94fc referenced 1 time by &05cf[3]
.mj
    jmp tube_main_loop                                                ; 94fc: 4c 36 00    L6. :05a6[3]   ; Return to Tube main loop

.tube_osfile
    ldx #&10                                                          ; 94ff: a2 10       ..  :05a9[3]   ; X=&10: 16 bytes for OSFILE CB
; &9501 referenced 1 time by &05b1[3]
.argsw
    jsr tube_read_r2                                                  ; 9501: 20 c5 06     .. :05ab[3]   ; Read next control block byte from R2
    sta zp_ptr_hi,x                                                   ; 9504: 95 01       ..  :05ae[3]   ; Store at &01+X (descending)
    dex                                                               ; 9506: ca          .   :05b0[3]   ; Decrement byte counter
    bne argsw                                                         ; 9507: d0 f8       ..  :05b1[3]   ; Loop for all 16 bytes
    jsr tube_read_string                                              ; 9509: 20 82 05     .. :05b3[3]   ; Read filename string from R2 into &0700
    stx zp_ptr_lo                                                     ; 950c: 86 00       ..  :05b6[3]   ; XY=&0700: filename pointer for OSFILE
    sty zp_ptr_hi                                                     ; 950e: 84 01       ..  :05b8[3]   ; Store Y=7 as pointer high byte
    ldy #0                                                            ; 9510: a0 00       ..  :05ba[3]   ; Y=0 for OSFILE control block offset
    jsr tube_read_r2                                                  ; 9512: 20 c5 06     .. :05bc[3]   ; Read OSFILE reason code from R2
    jsr osfile                                                        ; 9515: 20 dd ff     .. :05bf[3]   ; Execute OSFILE operation
    jsr tube_send_r2                                                  ; 9518: 20 95 06     .. :05c2[3]   ; Send result A (object type) to co-processor
    ldx #&10                                                          ; 951b: a2 10       ..  :05c5[3]   ; Return 16-byte control block to co-processor
; &951d referenced 1 time by &05cd[3]
.send_osfile_ctrl_blk
    lda zp_ptr_hi,x                                                   ; 951d: b5 01       ..  :05c7[3]   ; Load control block byte
    jsr tube_send_r2                                                  ; 951f: 20 95 06     .. :05c9[3]   ; Send byte to co-processor via R2
    dex                                                               ; 9522: ca          .   :05cc[3]   ; Decrement byte counter
    bne send_osfile_ctrl_blk                                          ; 9523: d0 f8       ..  :05cd[3]   ; Loop for all 16 bytes
    beq mj                                                            ; 9525: f0 d5       ..  :05cf[3]   ; ALWAYS branch to main loop; ALWAYS branch

    ldx #&0d                                                          ; 9527: a2 0d       ..  :05d1[3]   ; Read 13-byte OSGBPB control block from R2
; &9529 referenced 1 time by &05d9[3]
.read_osgbpb_ctrl_blk
    jsr tube_read_r2                                                  ; 9529: 20 c5 06     .. :05d3[3]   ; Read next control block byte from R2
    sta escape_flag,x                                                 ; 952c: 95 ff       ..  :05d6[3]   ; Store at &FF+X (descending into &00-&0C)
    dex                                                               ; 952e: ca          .   :05d8[3]   ; Decrement byte counter
    bne read_osgbpb_ctrl_blk                                          ; 952f: d0 f8       ..  :05d9[3]   ; Loop for all 13 bytes
    jsr tube_read_r2                                                  ; 9531: 20 c5 06     .. :05db[3]   ; Read OSGBPB reason code from R2
    ldy #0                                                            ; 9534: a0 00       ..  :05de[3]   ; Y=0 for OSGBPB control block
    jsr osgbpb                                                        ; 9536: 20 d1 ff     .. :05e0[3]   ; Read or write multiple bytes to an open file
    pha                                                               ; 9539: 48          H   :05e3[3]   ; Save A (completion status) for later
    ldx #&0c                                                          ; 953a: a2 0c       ..  :05e4[3]   ; Return 13-byte result block to co-processor
; &953c referenced 1 time by &05ec[3]
.send_osgbpb_result
    lda zp_ptr_lo,x                                                   ; 953c: b5 00       ..  :05e6[3]   ; Load result byte from zero page
    jsr tube_send_r2                                                  ; 953e: 20 95 06     .. :05e8[3]   ; Send byte to co-processor via R2
    dex                                                               ; 9541: ca          .   :05eb[3]   ; Decrement byte counter
    bpl send_osgbpb_result                                            ; 9542: 10 f8       ..  :05ec[3]   ; Loop for 13 bytes (X=12..0)
    pla                                                               ; 9544: 68          h   :05ee[3]   ; Recover completion status from stack
    jmp tube_rdch_reply                                               ; 9545: 4c 3a 05    L:. :05ef[3]   ; Send carry+status as RDCH-style reply

    jsr tube_read_r2                                                  ; 9548: 20 c5 06     .. :05f2[3]   ; Read OSWORD number from R2
    tax                                                               ; 954b: aa          .   :05f5[3]   ; X = first parameter
    jsr tube_read_r2                                                  ; 954c: 20 c5 06     .. :05f6[3]   ; Read A (OSBYTE number) from R2
    jsr osbyte                                                        ; 954f: 20 f4 ff     .. :05f9[3]   ; Execute OSBYTE call
; &9552 referenced 1 time by &05ff[3]
.tube_poll_r2_result
    bit tube_status_register_2                                        ; 9552: 2c e2 fe    ,.. :05fc[3]   ; Poll R2 status for result send
    equb &50                                                          ; 9555: 50          P   :05ff[3]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_dispatch_table, *, reloc_p5_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_dispatch_table, &0600

    ; Set the program counter to the next position in the binary file.
    org reloc_p5_src + (* - tube_dispatch_table)

.l9556

; Move 4: &9556 to &0600 for length 256
    org &0600
; &9556 referenced 1 time by &816a
.tube_page6_start
    equb &fb                                                          ; 9556: fb          .   :0600[4]

    stx tube_data_register_2                                          ; 9557: 8e e3 fe    ... :0601[4]   ; Send X result for 2-param OSBYTE
; &955a referenced 1 time by &0617[4]
.bytex
    jmp tube_main_loop                                                ; 955a: 4c 36 00    L6. :0604[4]   ; Return to main event loop

.tube_osbyte_long
    jsr tube_read_r2                                                  ; 955d: 20 c5 06     .. :0607[4]
    tax                                                               ; 9560: aa          .   :060a[4]   ; Save in X
    jsr tube_read_r2                                                  ; 9561: 20 c5 06     .. :060b[4]   ; Read Y parameter from co-processor
    tay                                                               ; 9564: a8          .   :060e[4]   ; Save in Y
    jsr tube_read_r2                                                  ; 9565: 20 c5 06     .. :060f[4]   ; Read A (OSBYTE function code)
    jsr osbyte                                                        ; 9568: 20 f4 ff     .. :0612[4]   ; Execute OSBYTE A,X,Y
    eor #&9d                                                          ; 956b: 49 9d       I.  :0615[4]   ; Send carry result to co-processor
    beq bytex                                                         ; 956d: f0 eb       ..  :0617[4]   ; OSBYTE &9D (fast Tube BPUT): no result needed
    ror a                                                             ; 956f: 6a          j   :0619[4]   ; Encode carry (error flag) into bit 7
    jsr tube_send_r2                                                  ; 9570: 20 95 06     .. :061a[4]   ; Send carry+status byte via R2
; &9573 referenced 1 time by &0620[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 9573: 2c e2 fe    ,.. :061d[4]   ; Poll R2 status for ready
    bvc tube_osbyte_send_y                                            ; 9576: 50 fb       P.  :0620[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; 9578: 8c e3 fe    ... :0622[4]   ; Send Y result, then fall through to send X
    equb &70                                                          ; 957b: 70          p   :0625[4]

.tube_osbyte_short
tube_osword = tube_osbyte_short+1
    cmp tube_send_zero_r2,x                                           ; 957c: d5 20       .   :0626[4]
    cmp l0006                                                         ; 957e: c5 06       ..  :0628[4]
    tay                                                               ; 9580: a8          .   :062a[4]   ; Save OSWORD number in Y
; &9581 referenced 1 time by &062e[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 9581: 2c e2 fe    ,.. :062b[4]   ; Poll R2 status for data ready
    bpl tube_osword_read                                              ; 9584: 10 fb       ..  :062e[4]   ; Not ready: keep polling
.tube_osbyte_send_x
    ldx tube_data_register_2                                          ; 9586: ae e3 fe    ... :0630[4]   ; Read param block length from R2
    dex                                                               ; 9589: ca          .   :0633[4]   ; DEX: length 0 means no params to read
    bmi skip_param_read                                               ; 958a: 30 0f       0.  :0634[4]   ; No params (length=0): skip read loop
; &958c referenced 2 times by &0639[4], &0642[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 958c: 2c e2 fe    ,.. :0636[4]   ; Poll R2 status for data ready
    bpl tube_osword_read_lp                                           ; 958f: 10 fb       ..  :0639[4]   ; Not ready: keep polling
    lda tube_data_register_2                                          ; 9591: ad e3 fe    ... :063b[4]   ; Read param byte from R2
    sta l0128,x                                                       ; 9594: 9d 28 01    .(. :063e[4]   ; Store param bytes into block at &0128
    dex                                                               ; 9597: ca          .   :0641[4]   ; Next param byte (descending)
    bpl tube_osword_read_lp                                           ; 9598: 10 f2       ..  :0642[4]   ; Loop until all params read
    tya                                                               ; 959a: 98          .   :0644[4]   ; Restore OSWORD number from Y
; &959b referenced 1 time by &0634[4]
.skip_param_read
    ldx #<(l0128)                                                     ; 959b: a2 28       .(  :0645[4]   ; XY=&0128: param block address for OSWORD
    ldy #>(l0128)                                                     ; 959d: a0 01       ..  :0647[4]   ; Y=&01: param block at &0128
    jsr osword                                                        ; 959f: 20 f1 ff     .. :0649[4]   ; Send result marker via R2
; &95a2 referenced 1 time by &064f[4]
.poll_r2_osword_result
    bit tube_status_register_2                                        ; 95a2: 2c e2 fe    ,.. :064c[4]   ; Poll R2 status for ready
    bpl poll_r2_osword_result                                         ; 95a5: 10 fb       ..  :064f[4]   ; Not ready: keep polling
    ldx tube_data_register_2                                          ; 95a7: ae e3 fe    ... :0651[4]   ; Read result block length from R2
    dex                                                               ; 95aa: ca          .   :0654[4]   ; Decrement result byte counter
    bmi tube_return_main                                              ; 95ab: 30 0e       0.  :0655[4]   ; No results to send: return to main loop
; &95ad referenced 1 time by &0663[4]
.tube_osword_write
    ldy l0128,x                                                       ; 95ad: bc 28 01    .(. :0657[4]   ; Send result block bytes from &0128 via R2
; &95b0 referenced 1 time by &065d[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95b0: 2c e2 fe    ,.. :065a[4]   ; Poll R2 status for ready
    bvc tube_osword_write_lp                                          ; 95b3: 50 fb       P.  :065d[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; 95b5: 8c e3 fe    ... :065f[4]   ; Send result byte via R2
    dex                                                               ; 95b8: ca          .   :0662[4]   ; Next result byte (descending)
    bpl tube_osword_write                                             ; 95b9: 10 f2       ..  :0663[4]   ; Loop until all results sent
; &95bb referenced 1 time by &0655[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95bb: 4c 36 00    L6. :0665[4]   ; Return to main event loop

.tube_osword_rdln
    ldx #4                                                            ; 95be: a2 04       ..  :0668[4]
; &95c0 referenced 1 time by &0670[4]
.read_rdln_ctrl_block
    jsr tube_read_r2                                                  ; 95c0: 20 c5 06     .. :066a[4]   ; Read control block byte from R2
    sta zp_ptr_lo,x                                                   ; 95c3: 95 00       ..  :066d[4]   ; Store in zero page params
    dex                                                               ; 95c5: ca          .   :066f[4]   ; Next byte (descending)
    bpl read_rdln_ctrl_block                                          ; 95c6: 10 f8       ..  :0670[4]   ; Loop until all 5 bytes read
    inx                                                               ; 95c8: e8          .   :0672[4]   ; X=0 after loop, A=0 for OSWORD 0 (read line)
    ldy #0                                                            ; 95c9: a0 00       ..  :0673[4]   ; Y=0 for OSWORD 0
    txa                                                               ; 95cb: 8a          .   :0675[4]   ; A=0: OSWORD 0 (read line)
    jsr osword                                                        ; 95cc: 20 f1 ff     .. :0676[4]   ; Read input line from keyboard
    bcc tube_rdln_send_line                                           ; 95cf: 90 05       ..  :0679[4]   ; C=0: line read OK; C=1: escape pressed
    lda #&ff                                                          ; 95d1: a9 ff       ..  :067b[4]   ; &FF = escape/error signal to co-processor
    jmp tube_reply_byte                                               ; 95d3: 4c 9e 05    L.. :067d[4]   ; Escape: send &FF error to co-processor

; &95d6 referenced 1 time by &0679[4]
.tube_rdln_send_line
    ldx #0                                                            ; 95d6: a2 00       ..  :0680[4]   ; X=0: start of input buffer at &0700
    lda #&7f                                                          ; 95d8: a9 7f       ..  :0682[4]   ; &7F = line read successfully
    jsr tube_send_r2                                                  ; 95da: 20 95 06     .. :0684[4]   ; Send &7F (success) to co-processor
; &95dd referenced 1 time by &0690[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 95dd: bd 00 07    ... :0687[4]   ; Load char from input buffer
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 95e0: 20 95 06     .. :068a[4]   ; Send char to co-processor
    inx                                                               ; 95e3: e8          .   :068d[4]   ; Next character
    cmp #&0d                                                          ; 95e4: c9 0d       ..  :068e[4]   ; Loop until CR terminator sent
    bne tube_rdln_send_loop                                           ; 95e6: d0 f5       ..  :0690[4]   ; Loop until CR terminator sent
    jmp tube_main_loop                                                ; 95e8: 4c 36 00    L6. :0692[4]   ; Return to main event loop

; &95eb referenced 13 times by &0020[1], &0026[1], &002c[1], &0467[2], &0572[3], &0579[3], &05c2[3], &05c9[3], &05e8[3], &061a[4], &0684[4], &068a[4], &0698[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 95eb: 2c e2 fe    ,.. :0695[4]   ; Poll R2 status (bit 6 = ready)
    bvc tube_send_r2                                                  ; 95ee: 50 fb       P.  :0698[4]   ; Not ready: keep polling
    sta tube_data_register_2                                          ; 95f0: 8d e3 fe    ... :069a[4]   ; Write A to Tube R2 data register
    rts                                                               ; 95f3: 60          `   :069d[4]   ; Return to caller

; &95f4 referenced 8 times by &0018[1], &0416[2], &041b[2], &0436[2], &043e[2], &0443[2], &0449[2], &06a1[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 95f4: 2c e6 fe    ,.. :069e[4]   ; Poll R4 status (bit 6 = ready)
    bvc tube_send_r4                                                  ; 95f7: 50 fb       P.  :06a1[4]   ; Not ready: keep polling
    sta tube_data_register_4                                          ; 95f9: 8d e7 fe    ... :06a3[4]   ; Write A to Tube R4 data register
    rts                                                               ; 95fc: 60          `   :06a6[4]   ; Return to caller

; &95fd referenced 1 time by &0403[2]
.tube_escape_check
    lda escape_flag                                                   ; 95fd: a5 ff       ..  :06a7[4]   ; Check OS escape flag at &FF
    sec                                                               ; 95ff: 38          8   :06a9[4]   ; SEC+ROR: put bit 7 of &FF into carry+bit 7
    ror a                                                             ; 9600: 6a          j   :06aa[4]   ; ROR: shift escape bit 7 to carry
    bmi tube_send_r1                                                  ; 9601: 30 0f       0.  :06ab[4]   ; Escape set: forward to co-processor via R1
.tube_event_handler
    pha                                                               ; 9603: 48          H   :06ad[4]   ; EVNTV: forward event A, Y, X to co-processor
    lda #0                                                            ; 9604: a9 00       ..  :06ae[4]   ; Send &00 prefix (event notification)
    jsr tube_send_r1                                                  ; 9606: 20 bc 06     .. :06b0[4]   ; Send event number via R1
    tya                                                               ; 9609: 98          .   :06b3[4]   ; Y value for event
    jsr tube_send_r1                                                  ; 960a: 20 bc 06     .. :06b4[4]   ; Send Y via R1
    txa                                                               ; 960d: 8a          .   :06b7[4]   ; X value for event
    jsr tube_send_r1                                                  ; 960e: 20 bc 06     .. :06b8[4]   ; Send X via R1
    pla                                                               ; 9611: 68          h   :06bb[4]   ; Restore A (event type)
; &9612 referenced 5 times by &06ab[4], &06b0[4], &06b4[4], &06b8[4], &06bf[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 9612: 2c e0 fe    ,.. :06bc[4]   ; Poll R1 status (bit 6 = ready)
    bvc tube_send_r1                                                  ; 9615: 50 fb       P.  :06bf[4]   ; Not ready: keep polling
    sta tube_data_register_1                                          ; 9617: 8d e1 fe    ... :06c1[4]   ; Write A to Tube R1 data register
    rts                                                               ; 961a: 60          `   :06c4[4]   ; Return to caller

; &961b referenced 20 times by &0520[3], &0524[3], &052d[3], &0542[3], &0552[3], &055e[3], &0564[3], &056c[3], &0586[3], &05ab[3], &05bc[3], &05d3[3], &05db[3], &05f2[3], &05f6[3], &0607[4], &060b[4], &060f[4], &066a[4], &06c8[4]
.tube_read_r2
    bit tube_status_register_2                                        ; 961b: 2c e2 fe    ,.. :06c5[4]
    bpl tube_read_r2                                                  ; 961e: 10 fb       ..  :06c8[4]
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
    copyblock tube_page6_start, *, l9556

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_page6_start, &0700

    ; Set the program counter to the next position in the binary file.
    org l9556 + (* - tube_page6_start)


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
lang_entry_lo = rom_header+1
lang_entry_hi = rom_header+2
    jmp language_handler                                              ; 8000: 4c e1 80    L..

; &8001 referenced 1 time by &04e4[2]
; &8002 referenced 1 time by &04e9[2]
; &8003 referenced 1 time by &04ee[2]
.service_entry
svc_entry_lo = service_entry+1
    jmp service_handler                                               ; 8003: 4c f7 80    L..

; &8004 referenced 1 time by &04f1[2]
; &8006 referenced 1 time by &04d3[2]
.rom_type
    equb &82                                                          ; 8006: 82          .
; &8007 referenced 1 time by &04db[2]
.copyright_offset
    equb copyright - rom_header                                       ; 8007: 10          .
; &8008 referenced 2 times by &836a, &8373
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
; &8018 referenced 1 time by &8500
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
    equb &40                                                          ; 8023: 40          @              ; Purpose unknown
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
    equb <(svc_1_abs_workspace-1)                                     ; 8026: b7          .              ; lo - Svc 1: absolute workspace
    equb <(svc_2_private_workspace-1)                                 ; 8027: c0          .              ; lo - Svc 2: private workspace
    equb <(svc_3_autoboot-1)                                          ; 8028: 18          .              ; lo - Svc 3: auto-boot
    equb <(svc_4_star_command-1)                                      ; 8029: b0          .              ; lo - Svc 4: unrecognised star command
    equb <(svc_5_unknown_irq-1)                                       ; 802a: 6b          k              ; lo - Svc 5: unrecognised interrupt
    equb <(return_1-1)                                                ; 802b: f5          .              ; lo - Svc 6: BRK (no-op)
    equb <(dispatch_net_cmd-1)                                        ; 802c: 6e          n              ; lo - Svc 7: unrecognised OSBYTE
    equb <(svc_8_osword-1)                                            ; 802d: 7e          ~              ; lo - Svc 8: unrecognised OSWORD
    equb <(svc_9_help-1)                                              ; 802e: 03          .              ; lo - Svc 9: *HELP
    equb <(return_1-1)                                                ; 802f: f5          .              ; lo - Svc 10: static workspace (no-op)
    equb <(svc_11_nmi_claim-1)                                        ; 8030: 68          h              ; lo - Svc 11: NMI release (reclaim NMIs)
    equb <(svc_12_nmi_release-1)                                      ; 8031: 65          e              ; lo - Svc 12: NMI claim (save NMI state)
    equb <(svc_13_select_nfs-1)                                       ; 8032: ec          .              ; lo - Svc 13: select NFS (intercepted before dispatch)
    equb <(lang_0_insert_remote_key-1)                                ; 8033: e7          .              ; lo - Lang 0: no language / Tube
    equb <(lang_1_remote_boot-1)                                      ; 8034: 99          .              ; lo - Lang 1: normal startup
    equb <(lang_2_save_palette_vdu-1)                                 ; 8035: a5          .              ; lo - Lang 2: softkey byte (Electron)
    equb <(lang_3_execute_at_0100-1)                                  ; 8036: c7          .              ; lo - Lang 3: softkey length (Electron)
    equb <(lang_4_remote_validated-1)                                 ; 8037: d7          .              ; lo - Lang 4: remote validated
    equb <(fscv_0_opt_entry-1)                                        ; 8038: e7          .              ; lo - FSCV 0: *OPT
    equb <(fscv_1_eof-1)                                              ; 8039: 68          h              ; lo - FSCV 1: EOF check
    equb <(fscv_2_star_run-1)                                         ; 803a: ce          .              ; lo - FSCV 2: */ (run)
    equb <(fscv_3_star_cmd-1)                                         ; 803b: d6          .              ; lo - FSCV 3: unrecognised star command
    equb <(fscv_2_star_run-1)                                         ; 803c: ce          .              ; lo - FSCV 4: *RUN
    equb <(fscv_5_cat-1)                                              ; 803d: 20                         ; lo - FSCV 5: *CAT
    equb <(fscv_6_shutdown-1)                                         ; 803e: 4c          L              ; lo - FSCV 6: shutdown
    equb <(fscv_7_read_handles-1)                                     ; 803f: 73          s              ; lo - FSCV 7: read handle range
    equb <(fsreply_0_print_dir-1)                                     ; 8040: 88          .              ; lo - FS reply: print directory name
    equb <(fsreply_1_copy_handles_boot-1)                             ; 8041: 29          )              ; lo - FS reply: copy handles + boot
    equb <(fsreply_2_copy_handles-1)                                  ; 8042: 2a          *              ; lo - FS reply: copy handles
    equb <(fsreply_3_set_csd-1)                                       ; 8043: 23          #              ; lo - FS reply: set CSD handle
    equb <(fsreply_4_notify_exec-1)                                   ; 8044: d4          .              ; lo - FS reply: notify + execute
    equb <(fsreply_5_set_lib-1)                                       ; 8045: 1e          .              ; lo - FS reply: set library handle
    equb <(net_1_read_handle-1)                                       ; 8046: 58          X              ; lo - *NET1: read handle from packet
    equb <(net_2_read_handle_entry-1)                                 ; 8047: 5e          ^              ; lo - *NET2: read handle from workspace
    equb <(net_3_close_handle-1)                                      ; 8048: 6e          n              ; lo - *NET3: close handle
; &8049 referenced 1 time by &80ec
    equb <(net_4_resume_remote-1)                                     ; 8049: b7          .              ; lo - *NET4: resume remote
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
    equb >(svc_5_unknown_irq-1)                                       ; 804f: 96          .              ; hi - Svc 5: unrecognised interrupt
    equb >(return_1-1)                                                ; 8050: 80          .              ; hi - Svc 6: BRK (no-op)
    equb >(dispatch_net_cmd-1)                                        ; 8051: 80          .              ; hi - Svc 7: unrecognised OSBYTE
    equb >(svc_8_osword-1)                                            ; 8052: 8e          .              ; hi - Svc 8: unrecognised OSWORD
    equb >(svc_9_help-1)                                              ; 8053: 82          .              ; hi - Svc 9: *HELP
    equb >(return_1-1)                                                ; 8054: 80          .              ; hi - Svc 10: static workspace (no-op)
    equb >(svc_11_nmi_claim-1)                                        ; 8055: 96          .              ; hi - Svc 11: NMI release (reclaim NMIs)
    equb >(svc_12_nmi_release-1)                                      ; 8056: 96          .              ; hi - Svc 12: NMI claim (save NMI state)
    equb >(svc_13_select_nfs-1)                                       ; 8057: 81          .              ; hi - Svc 13: select NFS (intercepted before dispatch)
    equb >(lang_0_insert_remote_key-1)                                ; 8058: 84          .              ; hi - Lang 0: no language / Tube
    equb >(lang_1_remote_boot-1)                                      ; 8059: 84          .              ; hi - Lang 1: normal startup
    equb >(lang_2_save_palette_vdu-1)                                 ; 805a: 92          .              ; hi - Lang 2: softkey byte (Electron)
    equb >(lang_3_execute_at_0100-1)                                  ; 805b: 84          .              ; hi - Lang 3: softkey length (Electron)
    equb >(lang_4_remote_validated-1)                                 ; 805c: 84          .              ; hi - Lang 4: remote validated
    equb >(fscv_0_opt_entry-1)                                        ; 805d: 89          .              ; hi - FSCV 0: *OPT
    equb >(fscv_1_eof-1)                                              ; 805e: 88          .              ; hi - FSCV 1: EOF check
    equb >(fscv_2_star_run-1)                                         ; 805f: 8d          .              ; hi - FSCV 2: */ (run)
    equb >(fscv_3_star_cmd-1)                                         ; 8060: 8b          .              ; hi - FSCV 3: unrecognised star command
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
    lda osbyte_a_copy                                                 ; 806f: a5 ef       ..             ; Read command character following *NET
    sbc #&31 ; '1'                                                    ; 8071: e9 31       .1             ; Subtract ASCII '1' to get 0-based command index
    cmp #4                                                            ; 8073: c9 04       ..             ; Command index >= 4: invalid *NET sub-command
    bcs svc_dispatch_range                                            ; 8075: b0 6c       .l             ; Out of range: return via c80e3/RTS
    tax                                                               ; 8077: aa          .              ; X = command index (0-3)
    lda #0                                                            ; 8078: a9 00       ..             ; Clear &A9 (used by dispatch)
    sta svc_state                                                     ; 807a: 85 a9       ..             ; Store zero to &A9
    tya                                                               ; 807c: 98          .              ; Preserve A before dispatch
    ldy #&21 ; '!'                                                    ; 807d: a0 21       .!             ; Y=&21: base offset for *NET commands (index 33+); Y=&20: base offset for *NET commands (index 33+)
    bne dispatch                                                      ; 807f: d0 66       .f             ; ALWAYS branch to dispatch; ALWAYS branch

; &8081 referenced 1 time by &8086
.skip_cmd_spaces
    iny                                                               ; 8081: c8          .              ; Advance past matched command text
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
    lda (fs_options),y                                                ; 8082: b1 bb       ..             ; Load next char from command line
    cmp #&20 ; ' '                                                    ; 8084: c9 20       .              ; Skip spaces
    beq skip_cmd_spaces                                               ; 8086: f0 f9       ..             ; Loop back to skip leading spaces
    cmp #&3a ; ':'                                                    ; 8088: c9 3a       .:             ; Colon = interactive remote command prefix
    bcs skip_stn_parse                                                ; 808a: b0 11       ..             ; Char >= ':': skip number parsing
    jsr parse_decimal                                                 ; 808c: 20 20 86      .            ; Parse decimal number from (fs_options),Y (DECIN)
    bcc got_station_num                                               ; 808f: 90 07       ..             ; C=1: dot found, first number was network
    sta fs_server_net                                                 ; 8091: 8d 01 0e    ...            ; Store network number (n.s = network.station); A=parsed value (accumulated in &B2)
    iny                                                               ; 8094: c8          .              ; Y=offset into (fs_options) buffer
    jsr parse_decimal                                                 ; 8095: 20 20 86      .            ; Parse decimal number from (fs_options),Y (DECIN)
; &8098 referenced 1 time by &808f
.got_station_num
    beq skip_stn_parse                                                ; 8098: f0 03       ..             ; Z=1: no station parsed (empty or non-numeric)
    sta fs_server_stn                                                 ; 809a: 8d 00 0e    ...            ; A=parsed value (accumulated in &B2)
; &809d referenced 2 times by &808a, &8098
.skip_stn_parse
    jsr infol2                                                        ; 809d: 20 75 8d     u.            ; Copy command text to FS buffer
; &80a0 referenced 2 times by &80a8, &80bf
.scan_for_colon
    dey                                                               ; 80a0: 88          .              ; Scan backward for ':' (interactive prefix)
    beq prepare_cmd_dispatch                                          ; 80a1: f0 22       ."             ; Y=0: no colon found, send command
    lda fs_cmd_data,y                                                 ; 80a3: b9 05 0f    ...            ; Read char from FS command buffer
    cmp #&3a ; ':'                                                    ; 80a6: c9 3a       .:             ; Test for colon separator
    bne scan_for_colon                                                ; 80a8: d0 f6       ..             ; Not colon: keep scanning backward
    jsr oswrch                                                        ; 80aa: 20 ee ff     ..            ; Echo colon, then read user input from keyboard; Write character
; &80ad referenced 1 time by &80ba
.read_remote_cmd_line
    jsr osrdch                                                        ; 80ad: 20 e0 ff     ..            ; Check for escape condition; Read a character from the current input stream
    jsr check_escape_handler                                          ; 80b0: 20 4d 85     M.            ; Test escape flag before FS reply
    sta fs_cmd_data,y                                                 ; 80b3: 99 05 0f    ...            ; Append typed character to command buffer
    iny                                                               ; 80b6: c8          .              ; Advance write pointer
    inx                                                               ; 80b7: e8          .              ; Increment character count
    cmp #&0d                                                          ; 80b8: c9 0d       ..             ; Test for CR (end of line)
    bne read_remote_cmd_line                                          ; 80ba: d0 f1       ..             ; Not CR: continue reading input
    jsr osnewl                                                        ; 80bc: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    bne scan_for_colon                                                ; 80bf: d0 df       ..             ; After OSNEWL: loop back to scan for colon
; ***************************************************************************************
; Forward unrecognised * command to fileserver (COMERR)
; 
; Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
; prepares an FS command with function code 0, and sends it to the
; fileserver to request decoding. The server returns a command code
; indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
; 5=load-as-command). This mechanism allows the fileserver to extend
; the client's command set without ROM updates. Called from the "I."
; and catch-all entries in the command match table at &8C05, and
; from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
; in), returns without sending.
; ***************************************************************************************
.forward_star_cmd
    jsr infol2                                                        ; 80c1: 20 75 8d     u.            ; Copy command text to FS buffer
    tay                                                               ; 80c4: a8          .              ; Y=function code for HDRFN
; &80c5 referenced 1 time by &80a1
.prepare_cmd_dispatch
    jsr prepare_fs_cmd                                                ; 80c5: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    ldx fs_cmd_csd                                                    ; 80c8: ae 03 0f    ...            ; X=depends on function
    beq return_1                                                      ; 80cb: f0 29       .)             ; CSD handle zero: not logged in
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
    jsr save_fscv_args_with_ptrs                                      ; 80d4: 20 c8 85     ..            ; Store A/X/Y in FS workspace
    cmp #8                                                            ; 80d7: c9 08       ..             ; FSCV function >= 8?
    bcs return_1                                                      ; 80d9: b0 1b       ..             ; Function code >= 8? Return (unsupported)
    tax                                                               ; 80db: aa          .              ; X = function code for dispatch
    tya                                                               ; 80dc: 98          .              ; Save Y (command text ptr hi)
    ldy #&13                                                          ; 80dd: a0 13       ..             ; Y=&13: base offset for FSCV dispatch (indices 20+); Y=&12: base offset for FSCV dispatch (indices 19+)
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
    cpx #5                                                            ; 80e1: e0 05       ..             ; X >= 5: invalid reason code, return
; &80e3 referenced 1 time by &8075
.svc_dispatch_range
    bcs return_1                                                      ; 80e3: b0 11       ..             ; Out of range: return via RTS
    ldy #&0e                                                          ; 80e5: a0 0e       ..             ; Y=&0E: base offset for language handlers (index 15+); Y=&0D: base offset for language handlers (index 14+)
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
; &80e7 referenced 5 times by &807f, &80d2, &80df, &80e9, &819d
.dispatch
    inx                                                               ; 80e7: e8          .              ; Add base offset Y to index X (loop: X += Y+1)
    dey                                                               ; 80e8: 88          .              ; Decrement base offset counter
    bpl dispatch                                                      ; 80e9: 10 fc       ..             ; Loop until Y exhausted
    tay                                                               ; 80eb: a8          .              ; Y=&FF (no further use)
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
    nop                                                               ; 80f8: ea          .              ; (bus settling continued)
    nop                                                               ; 80f9: ea          .              ; (bus settling continued)
    nop                                                               ; 80fa: ea          .              ; (bus settling continued)
    nop                                                               ; 80fb: ea          .              ; (bus settling continued)
    nop                                                               ; 80fc: ea          .              ; (bus settling continued)
    nop                                                               ; 80fd: ea          .              ; (bus settling continued)
    nop                                                               ; 80fe: ea          .              ; (bus settling continued)
    nop                                                               ; 80ff: ea          .              ; (bus settling continued)
    pha                                                               ; 8100: 48          H              ; Save service call number
    lda rom_ws_table,x                                                ; 8101: bd f0 0d    ...            ; Load workspace byte for this ROM slot
    pha                                                               ; 8104: 48          H              ; Push detection flag
    bne adlc_detect_done                                              ; 8105: d0 11       ..             ; Non-zero: ROM already detected, skip probe
    inc rom_ws_table,x                                                ; 8107: fe f0 0d    ...            ; First call: mark ROM as present
    lda station_id_disable_net_nmis                                   ; 810a: ad 18 fe    ...            ; Read station ID (INTOFF side effect)
    beq no_adlc_found                                                 ; 810d: f0 05       ..             ; Zero: no ADLC hardware, skip
    cmp station_id_disable_net_nmis                                   ; 810f: cd 18 fe    ...            ; Second read: bus stability check
    beq adlc_detect_done                                              ; 8112: f0 04       ..             ; Same value: ADLC present, continue
; &8114 referenced 1 time by &810d
.no_adlc_found
    sec                                                               ; 8114: 38          8              ; C=1: prepare to set disable flag
    ror rom_ws_table,x                                                ; 8115: 7e f0 0d    ~..            ; Bit 7 into workspace: disable this ROM
; &8118 referenced 2 times by &8105, &8112
.adlc_detect_done
    pla                                                               ; 8118: 68          h              ; Restore detection flag
    asl a                                                             ; 8119: 0a          .              ; C into bit 7 of A
    pla                                                               ; 811a: 68          h              ; Restore service call number
    bmi check_svc_high                                                ; 811b: 30 02       0.             ; Service >= &80: always handle (Tube/init)
    bcs svc_unhandled_return                                          ; 811d: b0 6e       .n             ; C=1 (ADLC active): duplicate ROM, skip
; ***************************************************************************************
; Service handler entry
; 
; Intercepts three service calls before normal dispatch:
;   &FE: Tube init -- explode character definitions
;   &FF: Full init -- vector setup, copy code to RAM, select NFS
;   &12 (Y=5): Select NFS as active filing system
; All other service calls < &0D dispatch via c8146.
; ***************************************************************************************
; &811f referenced 1 time by &811b
.check_svc_high
    cmp #&fe                                                          ; 811f: c9 fe       ..             ; Service >= &FE?
    bcc check_svc_12                                                  ; 8121: 90 5c       .\             ; Service < &FE: skip to &12/dispatch check
    bne init_vectors_and_copy                                         ; 8123: d0 1b       ..             ; Service &FF: full init (vectors + RAM copy)
    cpy #0                                                            ; 8125: c0 00       ..             ; Service &FE: Y=0?
    beq check_svc_12                                                  ; 8127: f0 56       .V             ; Y=0: no Tube data, skip to &12 check
    ldx #6                                                            ; 8129: a2 06       ..             ; X=6 extra pages for char definitions
    lda #osbyte_explode_chars                                         ; 812b: a9 14       ..             ; OSBYTE &14: explode character RAM
    jsr osbyte                                                        ; 812d: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
; &8130 referenced 2 times by &8133, &813d
.poll_tube_ready
    bit tube_status_1_and_tube_control                                ; 8130: 2c e0 fe    ,..            ; Poll Tube status register 1
    bpl poll_tube_ready                                               ; 8133: 10 fb       ..             ; Loop until Tube ready (bit 7 set)
    lda tube_data_register_1                                          ; 8135: ad e1 fe    ...            ; Read byte from Tube data register 1
    beq tube_chars_done                                               ; 8138: f0 43       .C             ; Zero byte: Tube transfer complete
    jsr oswrch                                                        ; 813a: 20 ee ff     ..            ; Send Tube char to screen via OSWRCH; Write character
    jmp poll_tube_ready                                               ; 813d: 4c 30 81    L0.            ; Loop for next Tube byte

; &8140 referenced 1 time by &8123
.init_vectors_and_copy
    lda #&ad                                                          ; 8140: a9 ad       ..             ; EVNTV low = &AD (event handler address)
    sta evntv                                                         ; 8142: 8d 20 02    . .            ; Set EVNTV low byte at &0220
    lda #6                                                            ; 8145: a9 06       ..             ; EVNTV high = &06 (page 6)
    sta evntv+1                                                       ; 8147: 8d 21 02    .!.            ; Set EVNTV high byte at &0221
    lda #&16                                                          ; 814a: a9 16       ..             ; BRKV low = &16 (NMI workspace)
    sta brkv                                                          ; 814c: 8d 02 02    ...            ; Set BRKV low byte at &0202
    lda #0                                                            ; 814f: a9 00       ..             ; BRKV high = &00 (zero page)
    sta brkv+1                                                        ; 8151: 8d 03 02    ...            ; Set BRKV high byte at &0203
    lda #&8e                                                          ; 8154: a9 8e       ..             ; Tube control register init value &8E
    sta tube_status_1_and_tube_control                                ; 8156: 8d e0 fe    ...            ; Write to Tube control register
    ldy #0                                                            ; 8159: a0 00       ..             ; Y=0: copy 256 bytes per page
; Copy NMI handler code from ROM to RAM pages &04-&06
; &815b referenced 1 time by &816e
.cloop
    lda reloc_p4_src,y                                                ; 815b: b9 5d 93    .].            ; Load ROM byte from page &93
    sta tube_code_page4,y                                             ; 815e: 99 00 04    ...            ; Store to page &04 (Tube code)
    lda reloc_p5_src,y                                                ; 8161: b9 56 94    .V.            ; Load ROM byte from page &94
    sta tube_dispatch_table,y                                         ; 8164: 99 00 05    ...            ; Store to page &05 (dispatch table)
    lda l9556,y                                                       ; 8167: b9 56 95    .V.            ; Load ROM byte from page &95
    sta tube_page6_start,y                                            ; 816a: 99 00 06    ...            ; Store to page &06
    dey                                                               ; 816d: 88          .              ; DEY wraps 0 -> &FF on first iteration
    bne cloop                                                         ; 816e: d0 eb       ..             ; Loop until 256 bytes copied per page
    jsr tube_post_init                                                ; 8170: 20 1e 04     ..            ; Run post-init routine in copied code
    ldx #&60 ; '`'                                                    ; 8173: a2 60       .`             ; X=&60: copy 97 bytes (&60..&00)
; Copy NMI workspace initialiser from ROM to &0016-&0076
; &8175 referenced 1 time by &817b
.copy_nmi_workspace
    lda reloc_zp_src,x                                                ; 8175: bd 1c 93    ...            ; Load NMI workspace init byte from ROM
    sta nmi_workspace_start,x                                         ; 8178: 95 16       ..             ; Store to zero page &16+X
    dex                                                               ; 817a: ca          .              ; Next byte
    bpl copy_nmi_workspace                                            ; 817b: 10 f8       ..             ; Loop until all workspace bytes copied
; &817d referenced 1 time by &8138
.tube_chars_done
    lda #0                                                            ; 817d: a9 00       ..             ; A=0: fall through to service &12 check
; &817f referenced 2 times by &8121, &8127
.check_svc_12
    cmp #&12                                                          ; 817f: c9 12       ..             ; Is this service &12 (select FS)?
    bne not_svc_12_nfs                                                ; 8181: d0 08       ..             ; No: check if service < &0D
    cpy #5                                                            ; 8183: c0 05       ..             ; Service &12: Y=5 (NFS)?
    bne not_svc_12_nfs                                                ; 8185: d0 04       ..             ; Not NFS: check if service < &0D
    lda #&0d                                                          ; 8187: a9 0d       ..             ; A=&0D: dispatch index for svc_13_select_nfs
    bne do_svc_dispatch                                               ; 8189: d0 04       ..             ; ALWAYS branch to dispatch; ALWAYS branch

; &818b referenced 2 times by &8181, &8185
.not_svc_12_nfs
    cmp #&0d                                                          ; 818b: c9 0d       ..             ; Service >= &0D?
; &818d referenced 1 time by &811d
.svc_unhandled_return
    bcs return_2                                                      ; 818d: b0 1c       ..             ; Service >= &0D: not handled, return
; &818f referenced 1 time by &8189
.do_svc_dispatch
    tax                                                               ; 818f: aa          .              ; X = service number (dispatch index)
    lda svc_state                                                     ; 8190: a5 a9       ..             ; Save &A9 (current service state)
    pha                                                               ; 8192: 48          H              ; Push saved &A9
    lda ws_page                                                       ; 8193: a5 a8       ..             ; Save &A8 (workspace page number)
    pha                                                               ; 8195: 48          H              ; Push saved &A8
    stx svc_state                                                     ; 8196: 86 a9       ..             ; Store service number to &A9
    sty ws_page                                                       ; 8198: 84 a8       ..             ; Store Y (page number) to &A8
    tya                                                               ; 819a: 98          .              ; A = Y for dispatch table offset
    ldy #0                                                            ; 819b: a0 00       ..             ; Y=0: base offset for service dispatch
    jsr dispatch                                                      ; 819d: 20 e7 80     ..            ; Dispatch to service handler
    ldx svc_state                                                     ; 81a0: a6 a9       ..             ; Recover service claim status from &A9
    pla                                                               ; 81a2: 68          h              ; Restore saved &A8 from stack
    sta ws_page                                                       ; 81a3: 85 a8       ..             ; Write back &A8
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
    pla                                                               ; 81a5: 68          h              ; Restore saved A from service dispatch
    sta svc_state                                                     ; 81a6: 85 a9       ..             ; Save to workspace &A9
    txa                                                               ; 81a8: 8a          .              ; Return ROM number in A
    ldx romsel_copy                                                   ; 81a9: a6 f4       ..             ; Restore X from MOS ROM select copy
; &81ab referenced 1 time by &818d
.return_2
    rts                                                               ; 81ab: 60          `              ; Return to MOS service handler

    nop                                                               ; 81ac: ea          .              ; Padding: dispatch targets &81B5
    nop                                                               ; 81ad: ea          .              ; NOP padding for command table
    nop                                                               ; 81ae: ea          .              ; NOP padding
    nop                                                               ; 81af: ea          .              ; NOP padding
    nop                                                               ; 81b0: ea          .              ; NOP padding
.svc_4_star_command
    ldx #&0c                                                          ; 81b1: a2 0c       ..             ; ROM offset for "ROFF" (copyright suffix)
    jsr match_rom_string                                              ; 81b3: 20 5e 83     ^.            ; Try matching *ROFF command
    bne match_net_cmd                                                 ; 81b6: d0 2e       ..             ; No match: try *NET
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
    ldy #4                                                            ; 81b8: a0 04       ..             ; Y=4: offset of keyboard disable flag
    lda (net_rx_ptr),y                                                ; 81ba: b1 9c       ..             ; Read flag from RX buffer
    beq skip_kbd_reenable                                             ; 81bc: f0 21       .!             ; Zero: keyboard not disabled, skip
    lda #0                                                            ; 81be: a9 00       ..             ; A=0: value to clear flag and re-enable
    tax                                                               ; 81c0: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 81c1: 91 9c       ..             ; Clear keyboard disable flag in buffer
    tay                                                               ; 81c3: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 81c4: a9 c9       ..             ; OSBYTE &C9: Econet keyboard disable
    jsr osbyte                                                        ; 81c6: 20 f4 ff     ..            ; Re-enable keyboard (X=0, Y=0); Enable keyboard (for Econet)
    lda #&0a                                                          ; 81c9: a9 0a       ..             ; Function &0A: remote operation complete
    jsr setup_tx_and_send                                             ; 81cb: 20 ba 90     ..            ; Send notification to controlling station
; &81ce referenced 1 time by &84b9
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 81ce: 86 9e       ..             ; Save X (return value from TX)
    lda #&ce                                                          ; 81d0: a9 ce       ..             ; OSBYTE &CE: first system mask to reset
; &81d2 referenced 1 time by &81dd
.clear_osbyte_masks
    ldx nfs_workspace                                                 ; 81d2: a6 9e       ..             ; Restore X for OSBYTE call
    ldy #&7f                                                          ; 81d4: a0 7f       ..             ; Y=&7F: AND mask (clear bit 7)
    jsr osbyte                                                        ; 81d6: 20 f4 ff     ..            ; Reset system mask byte
    adc #1                                                            ; 81d9: 69 01       i.             ; Advance to next OSBYTE (&CE -> &CF)
    cmp #&d0                                                          ; 81db: c9 d0       ..             ; Reached &D0? (past &CF)
.cmd_name_matched
    beq clear_osbyte_masks                                            ; 81dd: f0 f3       ..             ; No: reset &CF too
; &81df referenced 1 time by &81bc
.skip_kbd_reenable
    lda #0                                                            ; 81df: a9 00       ..             ; A=0: clear remote state
    sta svc_state                                                     ; 81e1: 85 a9       ..             ; Clear &A9 (service dispatch state)
.skpspi
    sta nfs_workspace                                                 ; 81e3: 85 9e       ..             ; Clear workspace byte
    rts                                                               ; 81e5: 60          `              ; Return

; &81e6 referenced 1 time by &81b6
.match_net_cmd
    ldx #5                                                            ; 81e6: a2 05       ..             ; X=5: ROM offset for "NET" match
    jsr match_rom_string                                              ; 81e8: 20 5e 83     ^.            ; Try matching *NET command
    bne return_service                                                ; 81eb: d0 24       .$             ; No match: return unclaimed
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
    jsr call_fscv_shutdown                                            ; 81ed: 20 14 82     ..            ; Notify current FS of shutdown (FSCV A=6)
    sec                                                               ; 81f0: 38          8              ; C=1 for ROR
    ror ws_page                                                       ; 81f1: 66 a8       f.             ; Set bit 7 of l00a8 (inhibit auto-boot)
    jsr issue_vectors_claimed                                         ; 81f3: 20 77 82     w.            ; Claim OS vectors, issue service &0F
    ldy #&1d                                                          ; 81f6: a0 1d       ..             ; Y=&1D: top of FS state range
; &81f8 referenced 1 time by &8200
.initl
    lda (net_rx_ptr),y                                                ; 81f8: b1 9c       ..             ; Copy FS state from RX buffer...
    sta fs_state_deb,y                                                ; 81fa: 99 eb 0d    ...            ; ...to workspace (offsets &15-&1D)
    dey                                                               ; 81fd: 88          .              ; Next byte (descending)
    cpy #&14                                                          ; 81fe: c0 14       ..             ; Loop until offset &14 done
    bne initl                                                         ; 8200: d0 f6       ..             ; Continue loop
    beq init_fs_vectors                                               ; 8202: f0 5c       .\             ; ALWAYS branch to init_fs_vectors; ALWAYS branch

; ***************************************************************************************
; Service 9: *HELP
; 
; Prints the ROM identification string using print_inline.
; ***************************************************************************************
.svc_9_help
    jsr print_inline                                                  ; 8204: 20 05 86     ..            ; Print ROM identification string
    equs &0d, "NFS 3.40", &0d                                         ; 8207: 0d 4e 46... .NF

; &8211 referenced 2 times by &81eb, &8226
.return_service
    ldy ws_page                                                       ; 8211: a4 a8       ..             ; Load workspace page for printing
    rts                                                               ; 8213: 60          `              ; Return (service not claimed)

; ***************************************************************************************
; Notify filing system of shutdown
; 
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; ***************************************************************************************
; &8214 referenced 2 times by &81ed, &8219
.call_fscv_shutdown
    lda #6                                                            ; 8214: a9 06       ..             ; FSCV reason 6 = FS shutdown
    jmp (fscv)                                                        ; 8216: 6c 1e 02    l..            ; Tail-call via filing system control vector

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
    jsr call_fscv_shutdown                                            ; 8219: 20 14 82     ..            ; Notify current FS of shutdown
    lda #osbyte_scan_keyboard_from_16                                 ; 821c: a9 7a       .z             ; OSBYTE &7A: scan keyboard
    jsr osbyte                                                        ; 821e: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 8221: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi print_station_info                                            ; 8222: 30 0a       0.             ; No key pressed: proceed with auto-boot
; ***************************************************************************************
; Check boot key
; 
; Checks if the pressed key (in A) is 'N' (matrix address &55). If
; not 'N', returns to the MOS without claiming the service call
; (another ROM may boot instead). If 'N', forgets the keypress via
; OSBYTE &78 and falls through to print_station_info.
; ***************************************************************************************
.check_boot_key
    eor #&55 ; 'U'                                                    ; 8224: 49 55       IU             ; XOR with &55: result=0 if key is 'N'
    bne return_service                                                ; 8226: d0 e9       ..             ; Not 'N': return without claiming
    tay                                                               ; 8228: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 8229: a9 78       .x             ; OSBYTE &78: clear key-pressed state
    jsr osbyte                                                        ; 822b: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; ***************************************************************************************
; Print station identification
; 
; Prints "Econet Station <n>" using the station number from the net
; receive buffer, then tests ADLC SR2 for the network clock signal —
; prints " No Clock" if absent. Falls through to init_fs_vectors.
; ***************************************************************************************
; &822e referenced 1 time by &8222
.print_station_info
    jsr print_inline                                                  ; 822e: 20 05 86     ..            ; Print 'Econet Station ' banner
    equs "Econet Station "                                            ; 8231: 45 63 6f... Eco

    ldy #&14                                                          ; 8240: a0 14       ..             ; Y=&14: offset for station number
    lda (net_rx_ptr),y                                                ; 8242: b1 9c       ..             ; Load station number
    jsr print_decimal                                                 ; 8244: 20 b0 8d     ..            ; Print as 3-digit decimal
    lda #&20 ; ' '                                                    ; 8247: a9 20       .              ; BIT trick: bit 5 of SR2 = clock present
    bit econet_control23_or_status2                                   ; 8249: 2c a1 fe    ,..            ; Test DCD: clock present if bit 5 clear
.dofsl1
    beq skip_no_clock_msg                                             ; 824c: f0 0d       ..             ; Clock present: skip warning
    jsr print_inline                                                  ; 824e: 20 05 86     ..            ; Print ' No Clock' warning
    equs " No Clock"                                                  ; 8251: 20 4e 6f...  No

    nop                                                               ; 825a: ea          .              ; NOP (padding after inline string)
; &825b referenced 1 time by &824c
.skip_no_clock_msg
    jsr print_inline                                                  ; 825b: 20 05 86     ..            ; Print two CRs (blank line)
    equs &0d, &0d                                                     ; 825e: 0d 0d       ..

; ***************************************************************************************
; Initialise filing system vectors
; 
; Copies 14 bytes from fs_vector_addrs (&8296) into FILEV-FSCV (&0212),
; setting all 7 filing system vectors to the extended vector dispatch
; addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
; ROM pointer table entries with the actual NFS handler addresses. Also
; reached directly from svc_13_select_nfs, bypassing the station display.
; Falls through to issue_vectors_claimed.
; ***************************************************************************************
; &8260 referenced 1 time by &8202
.init_fs_vectors
    ldy #&0d                                                          ; 8260: a0 0d       ..             ; Copy 14 bytes: FS vector addresses → FILEV-FSCV
; &8262 referenced 1 time by &8269
.copy_vectors_loop
    lda fs_vector_addrs,y                                             ; 8262: b9 96 82    ...            ; Load vector address from table
    sta filev,y                                                       ; 8265: 99 12 02    ...            ; Write to FILEV-FSCV vector table
    dey                                                               ; 8268: 88          .              ; Next byte (descending)
    bpl copy_vectors_loop                                             ; 8269: 10 f7       ..             ; Loop until all 14 bytes copied
    jsr setup_rom_ptrs_netv                                           ; 826b: 20 21 83     !.            ; Read ROM ptr table addr, install NETV
    ldy #&1b                                                          ; 826e: a0 1b       ..             ; Install 7 handler entries in ROM ptr table
    ldx #7                                                            ; 8270: a2 07       ..             ; 7 FS vectors to install
    jsr store_rom_ptr_pair                                            ; 8272: 20 35 83     5.            ; Install each 3-byte vector entry
    stx svc_state                                                     ; 8275: 86 a9       ..             ; X=0 after loop; store as workspace offset
; ***************************************************************************************
; Issue 'vectors claimed' service and optionally auto-boot
; 
; Issues service &0F (vectors claimed) via OSBYTE &8F, then
; service &0A. If nfs_temp is zero (auto-boot not inhibited),
; sets up the command string "I .BOOT" at &828E and jumps to
; the FSCV 3 unrecognised-command handler (which matches against
; the command table at &8C05). The "I." prefix triggers the
; catch-all entry which forwards the command to the fileserver.
; Falls through to run_fscv_cmd.
; ***************************************************************************************
; &8277 referenced 1 time by &81f3
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 8277: a9 8f       ..             ; A=&8F: issue service request
    ldx #&0f                                                          ; 8279: a2 0f       ..             ; X=&0F: 'vectors claimed' service
    jsr osbyte                                                        ; 827b: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 827e: a2 0a       ..             ; X=&0A: service &0A
    jsr osbyte                                                        ; 8280: 20 f4 ff     ..            ; Issue service &0A
    ldx ws_page                                                       ; 8283: a6 a8       ..             ; Non-zero after hard reset: skip auto-boot
    bne return_3                                                      ; 8285: d0 37       .7             ; Non-zero: skip auto-boot
    ldx #&8e                                                          ; 8287: a2 8e       ..             ; X = lo byte of auto-boot string at &8292
; ***************************************************************************************
; Run FSCV command from ROM
; 
; Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
; to execute the command string at (X, Y). X is pre-loaded by the
; caller with the low byte of the string address. Also used as a
; data base address by store_rom_ptr_pair for Y-indexed access to
; the handler address table.
; ***************************************************************************************
; &8289 referenced 2 times by &8335, &833b
.run_fscv_cmd
    ldy #&82                                                          ; 8289: a0 82       ..             ; Y=&82: ROM page high byte
    jmp fscv_3_star_cmd                                               ; 828b: 4c d7 8b    L..            ; Execute command string at (X, Y)

; Synthetic auto-boot command string. "I " does not match any
; entry in NFS's local command table — "I." requires a dot, and
; "I AM" requires 'A' after the space — so fscv_3_star_cmd
; forwards the entire string to the fileserver, which executes
; the .BOOT file.
    equs "I .BOOT", &0d                                               ; 828e: 49 20 2e... I .            ; Auto-boot string tail / NETV handler data
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
; &8296 referenced 1 time by &8262
.fs_vector_addrs
    equb &1b, &ff                                                     ; 8296: 1b ff       ..             ; FILEV dispatch (&FF1B)
    equb &1e, &ff                                                     ; 8298: 1e ff       ..             ; ARGSV dispatch (&FF1E); ARGSV dispatch lo
    equb &21, &ff                                                     ; 829a: 21 ff       !.             ; BGETV dispatch (&FF21); BGETV dispatch hi
    equb &24, &ff                                                     ; 829c: 24 ff       $.             ; BPUTV dispatch (&FF24); BPUTV dispatch lo
    equb &27, &ff                                                     ; 829e: 27 ff       '.             ; GBPBV dispatch (&FF27); GBPBV dispatch lo; GBPBV dispatch hi
    equb &2a, &ff                                                     ; 82a0: 2a ff       *.             ; FINDV dispatch (&FF2A); FINDV dispatch lo; FINDV dispatch hi
    equb &2d, &ff                                                     ; 82a2: 2d ff       -.             ; FSCV dispatch (&FF2D); FSCV dispatch lo
    equb 5                                                            ; 82a4: 05          .              ; FILEV handler lo (&8705)
    equb &87                                                          ; 82a5: 87          .              ; FILEV handler hi
    equb &4a                                                          ; 82a6: 4a          J              ; (ROM bank — not read)
    equb &24                                                          ; 82a7: 24          $              ; ARGSV handler lo (&8924)
    equb &89                                                          ; 82a8: 89          .              ; ARGSV handler hi
    equb &44                                                          ; 82a9: 44          D              ; (ROM bank — not read)
    equb &5c                                                          ; 82aa: 5c          \              ; BGETV handler lo (&855C)
    equb &85                                                          ; 82ab: 85          .              ; BGETV handler hi
    equb &57                                                          ; 82ac: 57          W              ; (ROM bank — not read)
    equb &0f                                                          ; 82ad: 0f          .              ; BPUTV handler lo (&840F)
    equb &84                                                          ; 82ae: 84          .              ; BPUTV handler hi
    equb &42                                                          ; 82af: 42          B              ; (ROM bank — not read)
    equb &2e                                                          ; 82b0: 2e          .              ; GBPBV handler lo (&8A2E)
    equb &8a                                                          ; 82b1: 8a          .              ; GBPBV handler hi
    equb &41                                                          ; 82b2: 41          A              ; (ROM bank — not read)
    equb &94                                                          ; 82b3: 94          .              ; FINDV handler lo (&8994)
    equb &89                                                          ; 82b4: 89          .              ; FINDV handler hi
    equb &52                                                          ; 82b5: 52          R              ; (ROM bank — not read)
    equb &d4                                                          ; 82b6: d4          .              ; FSCV handler lo (&80D4)
    equb &80                                                          ; 82b7: 80          .              ; FSCV handler hi; FSCV handler hi

; ***************************************************************************************
; Service 1: claim absolute workspace
; 
; Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
; and FS command buffer (&0F). If Y >= &10, workspace already
; allocated — returns unchanged.
; ***************************************************************************************
.svc_1_abs_workspace
    cpy #&10                                                          ; 82b8: c0 10       ..             ; Already at page &10 or above?
    bcs return_3                                                      ; 82ba: b0 02       ..             ; Yes: nothing to claim
    ldy #&10                                                          ; 82bc: a0 10       ..             ; Claim pages &0D-&0F (3 pages)
; &82be referenced 2 times by &8285, &82ba
.return_3
    rts                                                               ; 82be: 60          `              ; Return (workspace claim done)

    equb &76, &90                                                     ; 82bf: 76 90       v.

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
    sty net_rx_ptr_hi                                                 ; 82c1: 84 9d       ..             ; Store page as RX buffer high byte
    iny                                                               ; 82c3: c8          .              ; Next page for NFS workspace
    sty nfs_workspace_hi                                              ; 82c4: 84 9f       ..             ; Store page as NFS workspace high
    lda #0                                                            ; 82c6: a9 00       ..             ; A=0 for clearing workspace
    ldy #4                                                            ; 82c8: a0 04       ..             ; Y=4: remote status offset
    sta (net_rx_ptr),y                                                ; 82ca: 91 9c       ..             ; Clear status byte in net receive buffer
    ldy #&ff                                                          ; 82cc: a0 ff       ..             ; Y=&FF: used for later iteration
    sta net_rx_ptr                                                    ; 82ce: 85 9c       ..             ; Clear RX ptr low byte
    sta nfs_workspace                                                 ; 82d0: 85 9e       ..             ; Clear workspace ptr low byte
    sta ws_page                                                       ; 82d2: 85 a8       ..             ; Clear RXCB iteration counter
    sta tx_clear_flag                                                 ; 82d4: 8d 62 0d    .b.            ; Clear TX semaphore (no TX in progress)
    tax                                                               ; 82d7: aa          .              ; X=0 for OSBYTE; X=&00
    lda #osbyte_read_write_last_break_type                            ; 82d8: a9 fd       ..             ; OSBYTE &FD: read type of last reset
    jsr osbyte                                                        ; 82da: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 82dd: 8a          .              ; X = break type from OSBYTE result; X=value of type of last reset
    beq read_station_id                                               ; 82de: f0 32       .2             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 82e0: a0 15       ..             ; Y=&15: printer station offset in RX buffer
    lda #&fe                                                          ; 82e2: a9 fe       ..             ; &FE = no server selected
    sta fs_server_stn                                                 ; 82e4: 8d 00 0e    ...            ; Station &FE = no server selected
    sta (net_rx_ptr),y                                                ; 82e7: 91 9c       ..             ; Store &FE at printer station offset
    lda #0                                                            ; 82e9: a9 00       ..             ; A=0 for clearing workspace fields
    sta fs_server_net                                                 ; 82eb: 8d 01 0e    ...            ; Clear network number
    sta prot_status                                                   ; 82ee: 8d 63 0d    .c.            ; Clear protection status
    sta fs_messages_flag                                              ; 82f1: 8d 06 0e    ...            ; Clear message flag
    sta fs_boot_option                                                ; 82f4: 8d 05 0e    ...            ; Clear boot option
    iny                                                               ; 82f7: c8          .              ; Y=&16
    sta (net_rx_ptr),y                                                ; 82f8: 91 9c       ..             ; Clear net number at RX buffer offset &16
    ldy #3                                                            ; 82fa: a0 03       ..             ; Init printer server: station &FE, net 0
    sta (nfs_workspace),y                                             ; 82fc: 91 9e       ..             ; Store net 0 at workspace offset 3
    dey                                                               ; 82fe: 88          .              ; Y=2: printer station offset; Y=&02
    lda #&eb                                                          ; 82ff: a9 eb       ..             ; &FE = no printer server
    sta (nfs_workspace),y                                             ; 8301: 91 9e       ..             ; Store &FE at printer station in workspace
; &8303 referenced 1 time by &8310
.init_rxcb_entries
    lda ws_page                                                       ; 8303: a5 a8       ..             ; Load RXCB counter
    jsr calc_handle_offset                                            ; 8305: 20 47 8e     G.            ; Convert to workspace byte offset
    bcs read_station_id                                               ; 8308: b0 08       ..             ; C=1: past max handles, done
    lda #&3f ; '?'                                                    ; 830a: a9 3f       .?             ; Mark RXCB as available
    sta (nfs_workspace),y                                             ; 830c: 91 9e       ..             ; Write &3F flag to workspace
    inc ws_page                                                       ; 830e: e6 a8       ..             ; Next RXCB number
    bne init_rxcb_entries                                             ; 8310: d0 f1       ..             ; Loop for all RXCBs
; &8312 referenced 2 times by &82de, &8308
.read_station_id
    lda station_id_disable_net_nmis                                   ; 8312: ad 18 fe    ...            ; Read station ID (also INTOFF)
    ldy #&14                                                          ; 8315: a0 14       ..             ; Y=&14: station ID offset in RX buffer
    sta (net_rx_ptr),y                                                ; 8317: 91 9c       ..             ; Store our station number
    jsr trampoline_adlc_init                                          ; 8319: 20 63 96     c.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 831c: a9 40       .@             ; Enable user-level RX (LFLAG=&40)
    sta rx_flags                                                      ; 831e: 8d 64 0d    .d.            ; Store to rx_flags
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
    lda #osbyte_read_rom_ptr_table_low                                ; 8321: a9 a8       ..             ; OSBYTE &A8: read ROM pointer table address
    ldx #0                                                            ; 8323: a2 00       ..             ; X=0: read low byte
    ldy #&ff                                                          ; 8325: a0 ff       ..             ; Y=&FF: read high byte
    jsr osbyte                                                        ; 8327: 20 f4 ff     ..            ; Returns table address in X (lo) Y (hi); Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 832a: 86 f6       ..             ; Store table base address low byte; X=value of address of ROM pointer table (low byte)
    sty osrdsc_ptr_hi                                                 ; 832c: 84 f7       ..             ; Store table base address high byte; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 832e: a0 36       .6             ; NETV extended vector offset in ROM ptr table
    sty netv                                                          ; 8330: 8c 24 02    .$.            ; Set NETV low byte = &36 (vector dispatch)
    ldx #1                                                            ; 8333: a2 01       ..             ; Install 1 entry (NETV) in ROM ptr table
; &8335 referenced 2 times by &8272, &8347
.store_rom_ptr_pair
    lda run_fscv_cmd,y                                                ; 8335: b9 89 82    ...            ; Load handler address low byte from table
    sta (osrdsc_ptr),y                                                ; 8338: 91 f6       ..             ; Store to ROM pointer table
    iny                                                               ; 833a: c8          .              ; Next byte
    lda run_fscv_cmd,y                                                ; 833b: b9 89 82    ...            ; Load handler address high byte from table
    sta (osrdsc_ptr),y                                                ; 833e: 91 f6       ..             ; Store to ROM pointer table
    iny                                                               ; 8340: c8          .              ; Next byte
    lda romsel_copy                                                   ; 8341: a5 f4       ..             ; Write current ROM bank number
    sta (osrdsc_ptr),y                                                ; 8343: 91 f6       ..             ; Store ROM number to ROM pointer table
    iny                                                               ; 8345: c8          .              ; Advance to next entry position
    dex                                                               ; 8346: ca          .              ; Count down entries
    bne store_rom_ptr_pair                                            ; 8347: d0 ec       ..             ; Loop until all entries installed
    ldy nfs_workspace_hi                                              ; 8349: a4 9f       ..             ; Y = workspace high byte + 1 = next free page; Y = next workspace page for MOS
    iny                                                               ; 834b: c8          .              ; Advance past workspace page
    rts                                                               ; 834c: 60          `              ; Return; Y = page after NFS workspace

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
    ldy #&1d                                                          ; 834d: a0 1d       ..             ; Copy 10 bytes: FS state to workspace backup
; &834f referenced 1 time by &8357
.fsdiel
    lda fs_state_deb,y                                                ; 834f: b9 eb 0d    ...            ; Load FS state byte at offset Y
    sta (net_rx_ptr),y                                                ; 8352: 91 9c       ..             ; Store to workspace backup area
    dey                                                               ; 8354: 88          .              ; Next byte down
    cpy #&14                                                          ; 8355: c0 14       ..             ; Offsets &15-&1D: server, handles, OPT, etc.
    bne fsdiel                                                        ; 8357: d0 f6       ..             ; Loop for offsets &1D..&15
    lda #osbyte_close_spool_exec                                      ; 8359: a9 77       .w             ; A=&7B: printer driver going dormant
    jmp osbyte                                                        ; 835b: 4c f4 ff    L..            ; Close any *SPOOL and *EXEC files

; &835e referenced 2 times by &81b3, &81e8
.match_rom_string
    ldy ws_page                                                       ; 835e: a4 a8       ..             ; Y = saved text pointer offset
; &8360 referenced 1 time by &8371
.match_cmd_chars
    lda (os_text_ptr),y                                               ; 8360: b1 f2       ..             ; Load next input character
    cmp #&2e ; '.'                                                    ; 8362: c9 2e       ..             ; Is it a '.' (abbreviation)?
    beq skip_space_next                                               ; 8364: f0 13       ..             ; Yes: skip to space skipper (match)
    and #&df                                                          ; 8366: 29 df       ).             ; Force uppercase (clear bit 5)
    beq check_rom_end                                                 ; 8368: f0 09       ..             ; Input char is NUL/space: check ROM byte
    cmp binary_version,x                                              ; 836a: dd 08 80    ...            ; Compare with ROM string byte
    bne check_rom_end                                                 ; 836d: d0 04       ..             ; Mismatch: check if ROM string ended
    iny                                                               ; 836f: c8          .              ; Advance input pointer
    inx                                                               ; 8370: e8          .              ; Advance ROM string pointer
    bne match_cmd_chars                                               ; 8371: d0 ed       ..             ; Continue matching (always taken)
; &8373 referenced 2 times by &8368, &836d
.check_rom_end
    lda binary_version,x                                              ; 8373: bd 08 80    ...            ; Load ROM string byte at match point
    beq skip_spaces                                                   ; 8376: f0 02       ..             ; Zero = end of ROM string = full match
    rts                                                               ; 8378: 60          `              ; Non-zero = partial/no match; Z=0

; &8379 referenced 2 times by &8364, &837e
.skip_space_next
    iny                                                               ; 8379: c8          .              ; Skip this space
; &837a referenced 2 times by &8376, &8de0
.skip_spaces
    lda (os_text_ptr),y                                               ; 837a: b1 f2       ..             ; Load next input character
    cmp #&20 ; ' '                                                    ; 837c: c9 20       .              ; Is it a space?
    beq skip_space_next                                               ; 837e: f0 f9       ..             ; Yes: keep skipping
    eor #&0d                                                          ; 8380: 49 0d       I.             ; XOR with CR: Z=1 if end of line
    rts                                                               ; 8382: 60          `              ; Mark TX semaphore as available

; ***************************************************************************************
; Initialise TX control block for FS reply on port &90
; 
; Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
; up the TX control block, stores the port and control bytes, then
; decrements the control flag. Used by send_fs_reply_cmd to prepare
; for receiving the fileserver's reply.
; ***************************************************************************************
; &8383 referenced 1 time by &83f0
.init_tx_reply_port
    lda #&90                                                          ; 8383: a9 90       ..             ; A=&90: FS reply port (PREPLY)
; &8385 referenced 1 time by &885a
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 8385: 20 91 83     ..            ; Init TXCB from template
    sta txcb_port                                                     ; 8388: 85 c1       ..             ; Store port number in TXCB
    lda #3                                                            ; 838a: a9 03       ..             ; Control byte: 3 = transmit
    sta txcb_start                                                    ; 838c: 85 c4       ..             ; Store control byte in TXCB
    dec txcb_ctrl                                                     ; 838e: c6 c0       ..             ; Decrement TXCB flag to arm TX
    rts                                                               ; 8390: 60          `              ; Return after port setup

; ***************************************************************************************
; Initialise TX control block at &00C0 from template
; 
; Copies 12 bytes from tx_ctrl_template (&83A9) to &00C0.
; For the first 2 bytes (Y=0,1), also copies the fileserver
; station/network from &0E00/&0E01 to &00C2/&00C3.
; The template sets up: control=&80, port=&99 (FS command port),
; command data length=&0F, plus padding bytes.
; ***************************************************************************************
; &8391 referenced 4 times by &8385, &83df, &8428, &8fee
.init_tx_ctrl_block
    pha                                                               ; 8391: 48          H              ; Preserve A across call
    ldy #&0b                                                          ; 8392: a0 0b       ..             ; Copy 12 bytes (Y=11..0)
; &8394 referenced 1 time by &83a5
.fstxl1
    lda tx_ctrl_template,y                                            ; 8394: b9 a9 83    ...            ; Load template byte
    sta txcb_ctrl,y                                                   ; 8397: 99 c0 00    ...            ; Store to TX control block at &00C0
    cpy #2                                                            ; 839a: c0 02       ..             ; Y < 2: also copy FS server station/network
    bpl fstxl2                                                        ; 839c: 10 06       ..             ; Skip station/network copy for Y >= 2
    lda fs_server_stn,y                                               ; 839e: b9 00 0e    ...            ; Load FS server station (Y=0) or network (Y=1)
    sta txcb_dest,y                                                   ; 83a1: 99 c2 00    ...            ; Store to dest station/network at &00C2
; &83a4 referenced 1 time by &839c
.fstxl2
    dey                                                               ; 83a4: 88          .              ; Next byte (descending)
    bpl fstxl1                                                        ; 83a5: 10 ed       ..             ; Loop until all 12 bytes copied
    pla                                                               ; 83a7: 68          h              ; Restore A
    rts                                                               ; 83a8: 60          `              ; Return

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
    equb &80, &99, 0, 0, 0, &0f                                       ; 83a9: 80 99 00... ...            ; Control flag; Port (FS command = &99); Buffer start low; Buffer start high (page &0F)
; &83af referenced 3 times by &88d8, &89b7, &9177
.tx_ctrl_upper
    equb &ff, &ff, &ff, &0f, &ff, &ff                                 ; 83af: ff ff ff... ...            ; Buffer start pad (4-byte Econet addr); Buffer start pad; Buffer end low; Buffer end high (page &0F); Buffer end pad; Buffer end pad

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
    pha                                                               ; 83b5: 48          H              ; Save flag byte for command
    sec                                                               ; 83b6: 38          8              ; C=1: include flag in FS command
    bcs store_fs_hdr_fn                                               ; 83b7: b0 12       ..             ; ALWAYS branch to prepare_fs_cmd; ALWAYS branch

; &83b9 referenced 2 times by &8720, &87c7
.prepare_cmd_clv
    clv                                                               ; 83b9: b8          .              ; V=0: command has no flag byte
    bvc store_fs_hdr_clc                                              ; 83ba: 50 0e       P.             ; ALWAYS branch to prepare_fs_cmd; ALWAYS branch

; ***************************************************************************************
; *BYE handler (logoff)
; 
; Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
; Dispatched from the command match table at &8C05 for "BYE".
; ***************************************************************************************
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 83bc: a9 77       .w             ; A=&77: OSBYTE close spool/exec
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
    clv                                                               ; 83c3: b8          .              ; V=0: standard FS command path
; &83c4 referenced 2 times by &88db, &89ba
.init_tx_ctrl_data
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 83c4: ad 02 0e    ...            ; Copy URD handle from workspace to buffer
    sta fs_cmd_urd                                                    ; 83c7: 8d 02 0f    ...            ; Store URD at &0F02
; &83ca referenced 1 time by &83ba
.store_fs_hdr_clc
    clc                                                               ; 83ca: 18          .              ; CLC: no byte-stream path
; &83cb referenced 1 time by &83b7
.store_fs_hdr_fn
    sty fs_cmd_y_param                                                ; 83cb: 8c 01 0f    ...            ; Store function code at &0F01
    ldy #1                                                            ; 83ce: a0 01       ..             ; Y=1: copy CSD (offset 1) then LIB (offset 0)
; &83d0 referenced 1 time by &83d7
.copy_dir_handles
    lda fs_csd_handle,y                                               ; 83d0: b9 03 0e    ...            ; Copy CSD and LIB handles to command buffer; A=timeout period for FS reply
    sta fs_cmd_csd,y                                                  ; 83d3: 99 03 0f    ...            ; Store at &0F03 (CSD) and &0F04 (LIB)
    dey                                                               ; 83d6: 88          .              ; Y=function code
    bpl copy_dir_handles                                              ; 83d7: 10 f7       ..             ; Loop for both handles
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
    php                                                               ; 83d9: 08          .              ; Save carry (FS path vs byte-stream)
    lda #&90                                                          ; 83da: a9 90       ..             ; Reply port &90 (PREPLY)
    sta fs_cmd_type                                                   ; 83dc: 8d 00 0f    ...            ; Store at &0F00 (HDRREP)
    jsr init_tx_ctrl_block                                            ; 83df: 20 91 83     ..            ; Copy TX template to &00C0
    txa                                                               ; 83e2: 8a          .              ; A = X (buffer extent)
    adc #5                                                            ; 83e3: 69 05       i.             ; HPTR = header (5) + data (X) bytes to send
    sta txcb_end                                                      ; 83e5: 85 c8       ..             ; Store to TXCB end-pointer low
    plp                                                               ; 83e7: 28          (              ; Restore carry flag
    bcs dofsl5                                                        ; 83e8: b0 1a       ..             ; C=1: byte-stream path (BSXMIT)
    php                                                               ; 83ea: 08          .              ; Save flags for send_fs_reply_cmd
    jsr setup_tx_ptr_c0                                               ; 83eb: 20 87 86     ..            ; Point net_tx_ptr to &00C0; transmit
    plp                                                               ; 83ee: 28          (              ; Restore flags
; &83ef referenced 2 times by &87d3, &8ab7
.send_fs_reply_cmd
    php                                                               ; 83ef: 08          .              ; Save flags (V flag state)
    jsr init_tx_reply_port                                            ; 83f0: 20 83 83     ..            ; Set up RX wait for FS reply
    jsr send_to_fs_star                                               ; 83f3: 20 1b 85     ..            ; Transmit and wait (BRIANX)
    plp                                                               ; 83f6: 28          (              ; Restore flags
; &83f7 referenced 1 time by &840d
.dofsl7
    iny                                                               ; 83f7: c8          .              ; Y=1: skip past command code byte
    lda (txcb_start),y                                                ; 83f8: b1 c4       ..             ; Load return code from FS reply
    tax                                                               ; 83fa: aa          .              ; X = return code
    beq return_dofsl7                                                 ; 83fb: f0 06       ..             ; Zero: success, return
    bvc check_fs_error                                                ; 83fd: 50 02       P.             ; V=0: standard path, error is fatal
    adc #&2a ; '*'                                                    ; 83ff: 69 2a       i*             ; ADC #&2A: test for &D6 (not found)
; &8401 referenced 1 time by &83fd
.check_fs_error
    bne store_fs_error                                                ; 8401: d0 70       .p             ; Non-zero: hard error, go to FSERR
; &8403 referenced 1 time by &83fb
.return_dofsl7
    rts                                                               ; 8403: 60          `              ; Return (success or soft &D6 error)

; &8404 referenced 1 time by &83e8
.dofsl5
    pla                                                               ; 8404: 68          h              ; Discard saved flags from stack
    ldx #&c0                                                          ; 8405: a2 c0       ..             ; X=&C0: TXCB address for byte-stream TX
    iny                                                               ; 8407: c8          .              ; Y++ past command code
    jsr econet_tx_retry                                               ; 8408: 20 61 92     a.            ; Byte-stream transmit with retry
    sta fs_load_addr_3                                                ; 840b: 85 b3       ..             ; Store result to &B3
    bcc dofsl7                                                        ; 840d: 90 e8       ..             ; C=0: success, check reply code
.bputv_handler
    clc                                                               ; 840f: 18          .              ; CLC for address addition
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
; &8410 referenced 1 time by &855d
.handle_bput_bget
    pha                                                               ; 8410: 48          H              ; Save A (BPUT byte) on stack
    sta fs_error_flags                                                ; 8411: 8d df 0f    ...            ; Also save byte at &0FDF for BSXMIT
    txa                                                               ; 8414: 8a          .              ; Transfer X for stack save
    pha                                                               ; 8415: 48          H              ; Save X on stack
    tya                                                               ; 8416: 98          .              ; Transfer Y (handle) for stack save
    pha                                                               ; 8417: 48          H              ; Save Y (handle) on stack
    php                                                               ; 8418: 08          .              ; Save P (C = BPUT/BGET selector) on stack
    sty fs_spool_handle                                               ; 8419: 84 ba       ..             ; Save handle for SPOOL/EXEC comparison later
    jsr handle_to_mask_clc                                            ; 841b: 20 44 86     D.            ; Convert handle Y to single-bit mask
    sty fs_handle_mask                                                ; 841e: 8c de 0f    ...            ; Store handle bitmask at &0FDE
    sty fs_spool0                                                     ; 8421: 84 cf       ..             ; Store handle bitmask for sequence tracking
    ldy #&90                                                          ; 8423: a0 90       ..             ; &90 = data port (PREPLY)
    sty fs_putb_buf                                                   ; 8425: 8c dc 0f    ...            ; Store reply port in command buffer
    jsr init_tx_ctrl_block                                            ; 8428: 20 91 83     ..            ; Set up 12-byte TXCB from template
    lda #&dc                                                          ; 842b: a9 dc       ..             ; CB reply buffer at &0FDC
    sta txcb_start                                                    ; 842d: 85 c4       ..             ; Store reply buffer ptr low in TXCB
    lda #&e0                                                          ; 842f: a9 e0       ..             ; Error buffer at &0FE0
    sta txcb_end                                                      ; 8431: 85 c8       ..             ; Store error buffer ptr low in TXCB
    iny                                                               ; 8433: c8          .              ; Y=1 (from init_tx_ctrl_block exit)
    ldx #9                                                            ; 8434: a2 09       ..             ; X=9: BPUT function code
    plp                                                               ; 8436: 28          (              ; Restore C: selects BPUT (0) vs BGET (1)
    bcc store_retry_count                                             ; 8437: 90 01       ..             ; C=0 (BPUT): keep X=9
    dex                                                               ; 8439: ca          .              ; X=&08
; &843a referenced 1 time by &8437
.store_retry_count
    stx fs_getb_buf                                                   ; 843a: 8e dd 0f    ...            ; Store function code at &0FDD
    lda fs_spool0                                                     ; 843d: a5 cf       ..             ; Load handle bitmask for BSXMIT
    ldx #&c0                                                          ; 843f: a2 c0       ..             ; X=&C0: TXCB address for econet_tx_retry
    jsr econet_tx_retry                                               ; 8441: 20 61 92     a.            ; Transmit via byte-stream protocol
    ldx fs_getb_buf                                                   ; 8444: ae dd 0f    ...            ; Load reply byte from buffer
    beq update_sequence_return                                        ; 8447: f0 48       .H             ; Zero reply = success, skip error handling
    ldy #&1f                                                          ; 8449: a0 1f       ..             ; Copy 32-byte reply to error buffer at &0FE0
; &844b referenced 1 time by &8452
.error1
    lda fs_putb_buf,y                                                 ; 844b: b9 dc 0f    ...            ; Load reply byte at offset Y
    sta fs_error_buf,y                                                ; 844e: 99 e0 0f    ...            ; Store to error buffer at &0FE0+Y
    dey                                                               ; 8451: 88          .              ; Next byte (descending)
    bpl error1                                                        ; 8452: 10 f7       ..             ; Loop until all 32 bytes copied
    tax                                                               ; 8454: aa          .              ; X=File handle
    lda #osbyte_read_write_exec_file_handle                           ; 8455: a9 c6       ..             ; Returns X=EXEC handle, Y=SPOOL handle
    jsr osbyte                                                        ; 8457: 20 f4 ff     ..            ; Read/Write *EXEC file handle
    lda #&14                                                          ; 845a: a9 14       ..             ; ')': offset into "SP." string at &8529
    cpy fs_spool_handle                                               ; 845c: c4 ba       ..             ; Y=value of *SPOOL file handle
    beq close_spool_exec                                              ; 845e: f0 06       ..             ; Handle matches SPOOL -- close it
    lda #&18                                                          ; 8460: a9 18       ..             ; '-': offset into "E." string at &852D
    cpx fs_spool_handle                                               ; 8462: e4 ba       ..             ; X=value of *EXEC file handle
    bne dispatch_fs_error                                             ; 8464: d0 06       ..             ; No EXEC match -- skip close
; &8466 referenced 1 time by &845e
.close_spool_exec
    tax                                                               ; 8466: aa          .              ; X = string offset for OSCLI close
    ldy #&85                                                          ; 8467: a0 85       ..             ; Y=&85: high byte of OSCLI string in ROM
    jsr oscli                                                         ; 8469: 20 f7 ff     ..            ; Close SPOOL/EXEC via "*SP." or "*E."
; &846c referenced 1 time by &8464
.dispatch_fs_error
    lda #&e0                                                          ; 846c: a9 e0       ..             ; Reset CB pointer to error buffer at &0FE0
    sta txcb_start                                                    ; 846e: 85 c4       ..             ; Reset reply ptr to error buffer
    ldx fs_getb_buf                                                   ; 8470: ae dd 0f    ...            ; Reload reply byte for error dispatch
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
    stx fs_last_error                                                 ; 8473: 8e 09 0e    ...            ; Remember raw FS error code
    ldy #1                                                            ; 8476: a0 01       ..             ; Y=1: point to error number byte in reply
    cpx #&a8                                                          ; 8478: e0 a8       ..             ; Clamp FS errors below &A8 to standard &A8
    bcs error_code_clamped                                            ; 847a: b0 04       ..             ; Error >= &A8: keep original value
    lda #&a8                                                          ; 847c: a9 a8       ..             ; Error < &A8: override with standard &A8
    sta (txcb_start),y                                                ; 847e: 91 c4       ..             ; Write clamped error number to reply buffer
; &8480 referenced 1 time by &847a
.error_code_clamped
    ldy #&ff                                                          ; 8480: a0 ff       ..             ; Start scanning from offset &FF (will INY to 0)
; &8482 referenced 1 time by &848a
.copy_error_to_brk
    iny                                                               ; 8482: c8          .              ; Next byte in reply buffer
    lda (txcb_start),y                                                ; 8483: b1 c4       ..             ; Copy reply buffer to &0100 for BRK execution
    sta l0100,y                                                       ; 8485: 99 00 01    ...            ; Build BRK error block at &0100
    eor #&0d                                                          ; 8488: 49 0d       I.             ; Scan for CR terminator (&0D)
    bne copy_error_to_brk                                             ; 848a: d0 f6       ..             ; Continue until CR found
    sta l0100,y                                                       ; 848c: 99 00 01    ...            ; Replace CR with zero = BRK error block end
    beq execute_downloaded                                            ; 848f: f0 44       .D             ; Execute as BRK error block at &0100; ALWAYS; ALWAYS branch

; &8491 referenced 1 time by &8447
.update_sequence_return
    sta fs_sequence_nos                                               ; 8491: 8d 08 0e    ...            ; Save updated sequence number
    pla                                                               ; 8494: 68          h              ; Restore Y from stack
    tay                                                               ; 8495: a8          .              ; Transfer A to Y for indexing
    pla                                                               ; 8496: 68          h              ; Restore X from stack
    tax                                                               ; 8497: aa          .              ; Transfer to X for return
    pla                                                               ; 8498: 68          h              ; Restore A from stack
.return_remote_cmd
    rts                                                               ; 8499: 60          `              ; Return to caller

; ***************************************************************************************
; Remote boot/execute handler
; 
; Checks byte 4 of the RX control block (remote status flag).
; If zero (not currently remoted), falls through to remot1 to
; set up a new remote session. If non-zero (already remoted),
; jumps to clear_jsr_protection and returns.
; ***************************************************************************************
.lang_1_remote_boot
    ldy #4                                                            ; 849a: a0 04       ..             ; Y=4: remote status flag offset
    lda (net_rx_ptr),y                                                ; 849c: b1 9c       ..             ; Read remote status from RX CB
    beq remot1                                                        ; 849e: f0 03       ..             ; Zero: not remoted, set up session
; &84a0 referenced 1 time by &84e6
.rchex
    jmp clear_jsr_protection                                          ; 84a0: 4c eb 92    L..            ; Already remoted: clear and return

; &84a3 referenced 2 times by &849e, &84dc
.remot1
    ora #9                                                            ; 84a3: 09 09       ..             ; Set remote status: bits 0+3 (ORA #9)
    sta (net_rx_ptr),y                                                ; 84a5: 91 9c       ..             ; Store updated remote status
    ldx #&80                                                          ; 84a7: a2 80       ..             ; X=&80: RX data area offset
    ldy #&80                                                          ; 84a9: a0 80       ..             ; Y=&80: read source station low
    lda (net_rx_ptr),y                                                ; 84ab: b1 9c       ..             ; Read source station lo from RX data at &80
    pha                                                               ; 84ad: 48          H              ; Save source station low byte
    iny                                                               ; 84ae: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 84af: b1 9c       ..             ; Read source station hi from RX data at &81
    ldy #&0f                                                          ; 84b1: a0 0f       ..             ; Save controlling station to workspace &0E/&0F
    sta (nfs_workspace),y                                             ; 84b3: 91 9e       ..             ; Store station high to ws+&0F
    dey                                                               ; 84b5: 88          .              ; Y=&0E; Y=&0e
    pla                                                               ; 84b6: 68          h              ; Restore source station low
    sta (nfs_workspace),y                                             ; 84b7: 91 9e       ..             ; Store station low to ws+&0E
    jsr clear_osbyte_ce_cf                                            ; 84b9: 20 ce 81     ..            ; Clear OSBYTE &CE/&CF flags
    jsr ctrl_block_setup                                              ; 84bc: 20 7c 91     |.            ; Set up TX control block
    ldx #1                                                            ; 84bf: a2 01       ..             ; X=1: disable keyboard
    ldy #0                                                            ; 84c1: a0 00       ..             ; Y=0 for OSBYTE
    lda #osbyte_read_write_econet_keyboard_disable                    ; 84c3: a9 c9       ..             ; Disable keyboard for remote session
    jsr osbyte                                                        ; 84c5: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; ***************************************************************************************
; Execute code at &0100
; 
; Clears JSR protection, zeroes &0100-&0102 (creating a BRK
; instruction at &0100 as a safe default), then JMP &0100 to
; execute code received over the network. If no code was loaded,
; the BRK triggers an error handler.
; ***************************************************************************************
.lang_3_execute_at_0100
    jsr clear_jsr_protection                                          ; 84c8: 20 eb 92     ..            ; Allow JSR to page 1 (stack page)
    ldx #2                                                            ; 84cb: a2 02       ..             ; Zero bytes &0100-&0102
    lda #0                                                            ; 84cd: a9 00       ..             ; A=0: zero execution header bytes
; &84cf referenced 1 time by &84d3
.zero_exec_header
    sta l0100,x                                                       ; 84cf: 9d 00 01    ...            ; BRK at &0100 as safe default
    dex                                                               ; 84d2: ca          .              ; Next byte
    bpl zero_exec_header                                              ; 84d3: 10 fa       ..             ; Loop until all zeroed
; &84d5 referenced 2 times by &848f, &850e
.execute_downloaded
    jmp l0100                                                         ; 84d5: 4c 00 01    L..            ; Execute downloaded code

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
    ldy #4                                                            ; 84d8: a0 04       ..             ; Y=4: RX control block byte 4 (remote status)
    lda (net_rx_ptr),y                                                ; 84da: b1 9c       ..             ; Read remote status flag
    beq remot1                                                        ; 84dc: f0 c5       ..             ; Zero = not remoted; allow new session
    ldy #&80                                                          ; 84de: a0 80       ..             ; Read source station from RX data at &80
    lda (net_rx_ptr),y                                                ; 84e0: b1 9c       ..             ; A = source station number
    ldy #&0e                                                          ; 84e2: a0 0e       ..             ; Compare against controlling station at &0E
    cmp (nfs_workspace),y                                             ; 84e4: d1 9e       ..             ; Check if source matches controller
    bne rchex                                                         ; 84e6: d0 b8       ..             ; Reject: source != controlling station
; ***************************************************************************************
; Insert remote keypress
; 
; Reads a character from RX block offset &82 and inserts it into
; keyboard input buffer 0 via OSBYTE &99.
; ***************************************************************************************
.lang_0_insert_remote_key
    ldy #&82                                                          ; 84e8: a0 82       ..             ; Read keypress from RX data at &82
    lda (net_rx_ptr),y                                                ; 84ea: b1 9c       ..             ; Load character byte
    tay                                                               ; 84ec: a8          .              ; Y = character to insert
    ldx #0                                                            ; 84ed: a2 00       ..             ; X = buffer 0 (keyboard input)
    jsr clear_jsr_protection                                          ; 84ef: 20 eb 92     ..            ; Release JSR protection before inserting key
    lda #osbyte_insert_input_buffer                                   ; 84f2: a9 99       ..             ; OSBYTE &99: insert char into input buffer
    jmp osbyte                                                        ; 84f4: 4c f4 ff    L..            ; Tail call: insert character Y into buffer X; Insert character Y into input buffer X

; &84f7 referenced 1 time by &854a
.error_not_listening
    lda #8                                                            ; 84f7: a9 08       ..             ; Error code 8: "Not listening" error
    bne set_listen_offset                                             ; 84f9: d0 04       ..             ; ALWAYS branch to set_listen_offset; ALWAYS branch

; &84fb referenced 1 time by &86d0
.nlistn
    lda (net_tx_ptr,x)                                                ; 84fb: a1 9a       ..             ; Load TX status byte for error lookup
; &84fd referenced 2 times by &855a, &89fc
.nlisne
    and #7                                                            ; 84fd: 29 07       ).             ; Mask to 3-bit error code (0-7)
; &84ff referenced 1 time by &84f9
.set_listen_offset
    tax                                                               ; 84ff: aa          .              ; X = error code index
    ldy error_offsets,x                                               ; 8500: bc 18 80    ...            ; Look up error message offset from table
    ldx #0                                                            ; 8503: a2 00       ..             ; X=0: start writing at &0101
    stx l0100                                                         ; 8505: 8e 00 01    ...            ; Store BRK opcode at &0100
; &8508 referenced 1 time by &8512
.copy_error_message
    lda error_msg_table,y                                             ; 8508: b9 79 85    .y.            ; Load error message byte
    sta l0101,x                                                       ; 850b: 9d 01 01    ...            ; Build error message at &0101+
    beq execute_downloaded                                            ; 850e: f0 c5       ..             ; Zero byte = end of message; go execute BRK
    iny                                                               ; 8510: c8          .              ; Next source byte
    inx                                                               ; 8511: e8          .              ; Next dest byte
    bne copy_error_message                                            ; 8512: d0 f4       ..             ; Continue copying message
    equs "SP."                                                        ; 8514: 53 50 2e    SP.
    equb &0d, &45, &2e, &0d                                           ; 8517: 0d 45 2e... .E.

; &851b referenced 5 times by &83f3, &8779, &8864, &9031, &9296
.send_to_fs_star
    lda #&2a ; '*'                                                    ; 851b: a9 2a       .*             ; A=&2A: error ptr for FS send
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
    pha                                                               ; 851d: 48          H              ; Save function code on stack
    lda rx_flags                                                      ; 851e: ad 64 0d    .d.            ; Load current rx_flags
    pha                                                               ; 8521: 48          H              ; Save rx_flags on stack for restore
    ora #&80                                                          ; 8522: 09 80       ..             ; Set bit7: FS transaction in progress
    sta rx_flags                                                      ; 8524: 8d 64 0d    .d.            ; Write back updated rx_flags
.skip_rx_flag_set
    lda #0                                                            ; 8527: a9 00       ..             ; Push two zero bytes as timeout counters
    pha                                                               ; 8529: 48          H              ; First zero for timeout
    pha                                                               ; 852a: 48          H              ; Second zero for timeout
    tay                                                               ; 852b: a8          .              ; Y=0: index for flag byte check; Y=&00
    tsx                                                               ; 852c: ba          .              ; TSX: index stack-based timeout via X
; &852d referenced 3 times by &8537, &853c, &8541
.fs_reply_poll
    jsr check_escape_handler                                          ; 852d: 20 4d 85     M.            ; Check for user escape condition
.incpx
    lda (net_tx_ptr),y                                                ; 8530: b1 9a       ..             ; Read flag byte from TX control block
    bmi fs_wait_cleanup                                               ; 8532: 30 0f       0.             ; Bit 7 set = reply received
    dec l0101,x                                                       ; 8534: de 01 01    ...            ; Three-stage nested timeout: inner loop
    bne fs_reply_poll                                                 ; 8537: d0 f4       ..             ; Inner not expired: keep polling
    dec l0102,x                                                       ; 8539: de 02 01    ...            ; Middle timeout loop
    bne fs_reply_poll                                                 ; 853c: d0 ef       ..             ; Middle not expired: keep polling
    dec l0104,x                                                       ; 853e: de 04 01    ...            ; Outer timeout loop (slowest)
    bne fs_reply_poll                                                 ; 8541: d0 ea       ..             ; Outer not expired: keep polling
; &8543 referenced 1 time by &8532
.fs_wait_cleanup
    pla                                                               ; 8543: 68          h              ; Pop first timeout byte
    pla                                                               ; 8544: 68          h              ; Pop second timeout byte
    pla                                                               ; 8545: 68          h              ; Pop saved rx_flags into A
    sta rx_flags                                                      ; 8546: 8d 64 0d    .d.            ; Restore saved rx_flags from stack
    pla                                                               ; 8549: 68          h              ; Pop saved function code
    beq error_not_listening                                           ; 854a: f0 ab       ..             ; A=saved func code; zero would mean no reply
    rts                                                               ; 854c: 60          `              ; Return to caller

; ***************************************************************************************
; Test MOS escape flag and abort if pending
; 
; Tests MOS escape flag (&FF bit 7). If escape is pending:
; acknowledges via OSBYTE &7E, writes &3F (deleted marker) into
; the control block via (net_tx_ptr),Y, and branches to the
; NLISTN error path. If no escape, returns immediately.
; ***************************************************************************************
; &854d referenced 3 times by &80b0, &852d, &86b7
.check_escape_handler
    bit escape_flag                                                   ; 854d: 24 ff       $.             ; Test escape flag (bit 7)
    bpl return_4                                                      ; 854f: 10 27       .'             ; Bit 7 clear: no escape, return
    lda #osbyte_acknowledge_escape                                    ; 8551: a9 7e       .~             ; A=&7E: acknowledge escape OSBYTE
    jsr osbyte                                                        ; 8553: 20 f4 ff     ..            ; Clear escape condition and perform escape effects
    lsr a                                                             ; 8556: 4a          J              ; LSR: get escape result bit
    sta (net_tx_ptr),y                                                ; 8557: 91 9a       ..             ; Store escape result to TXCB
    asl a                                                             ; 8559: 0a          .              ; Restore A
    bne nlisne                                                        ; 855a: d0 a1       ..             ; Non-zero: report 'Not listening'
.bgetv_handler
    sec                                                               ; 855c: 38          8              ; C=1: flag for BGET mode
    jsr handle_bput_bget                                              ; 855d: 20 10 84     ..            ; Handle BGET via FS command; Handle BPUT/BGET file byte I/O
    sec                                                               ; 8560: 38          8              ; SEC: set carry for error check
    lda #&fe                                                          ; 8561: a9 fe       ..             ; A=&FE: mask for EOF check
    bit fs_error_flags                                                ; 8563: 2c df 0f    ,..            ; BIT l0fdf: test error flags
    bvs return_4                                                      ; 8566: 70 10       p.             ; V=1: error, return early
    clc                                                               ; 8568: 18          .              ; CLC: no error
    php                                                               ; 8569: 08          .              ; Save flags for EOF check
    lda fs_spool0                                                     ; 856a: a5 cf       ..             ; Load BGET result byte
    plp                                                               ; 856c: 28          (              ; Restore flags
    bmi bgetv_shared_jsr                                              ; 856d: 30 03       0.             ; Bit7 set: skip FS flag clear
    jsr clear_fs_flag                                                 ; 856f: 20 7e 86     ~.            ; Clear FS flag for handle
; &8572 referenced 1 time by &856d
.bgetv_shared_jsr
    jsr set_fs_flag                                                   ; 8572: 20 79 86     y.            ; Set EOF flag for this handle
.load_handle_mask
    lda fs_handle_mask                                                ; 8575: ad de 0f    ...            ; Load handle bitmask for caller
; &8578 referenced 2 times by &854f, &8566
.return_4
    rts                                                               ; 8578: 60          `              ; Return with handle mask in A

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
; &8579 referenced 1 time by &8508
.error_msg_table
    equb &a0                                                          ; 8579: a0          .
    equs "Line Jammed", 0                                             ; 857a: 4c 69 6e... Lin
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
; Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
; Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
; falls through to save_fscv_args to store A/X/Y in the FS
; workspace.
; ***************************************************************************************
; &85c8 referenced 3 times by &80d4, &8994, &8bd7
.save_fscv_args_with_ptrs
    stx os_text_ptr                                                   ; 85c8: 86 f2       ..             ; X to os_text_ptr (text ptr lo)
    sty os_text_ptr_hi                                                ; 85ca: 84 f3       ..             ; Y to os_text_ptr hi
    stx fs_cmd_ptr                                                    ; 85cc: 8e 10 0e    ...            ; X to FS command ptr lo
    sty l0e11                                                         ; 85cf: 8c 11 0e    ...            ; Y to FS command ptr hi
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
    sta fs_last_byte_flag                                             ; 85d2: 85 bd       ..             ; A = function code / command
    stx fs_options                                                    ; 85d4: 86 bb       ..             ; X = control block ptr lo
    sty fs_block_offset                                               ; 85d6: 84 bc       ..             ; Y = control block ptr hi
    stx fs_crc_lo                                                     ; 85d8: 86 be       ..             ; X dup for indexed access via (fs_crc)
    sty fs_crc_hi                                                     ; 85da: 84 bf       ..             ; Y dup for indexed access
    rts                                                               ; 85dc: 60          `              ; Return

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
    ldy #&0e                                                          ; 85dd: a0 0e       ..             ; Y=&0E: attribute byte offset in param block
    lda (fs_options),y                                                ; 85df: b1 bb       ..             ; Load FS attribute byte
    and #&3f ; '?'                                                    ; 85e1: 29 3f       )?             ; Mask to 6 bits (FS → BBC direction)
    ldx #4                                                            ; 85e3: a2 04       ..             ; X=4: skip first 4 table entries (BBC→FS half)
    bne attrib_shift_bits                                             ; 85e5: d0 04       ..             ; ALWAYS branch to shared bitmask builder; ALWAYS branch

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
    and #&1f                                                          ; 85e7: 29 1f       ).             ; Mask to 5 bits (BBC → FS direction)
    ldx #&ff                                                          ; 85e9: a2 ff       ..             ; X=&FF: INX makes 0; start from table index 0
; &85eb referenced 1 time by &85e5
.attrib_shift_bits
    sta fs_error_ptr                                                  ; 85eb: 85 b8       ..             ; Temp storage for source bitmask to shift out
    lda #0                                                            ; 85ed: a9 00       ..             ; A=0: accumulate destination bits here
; &85ef referenced 1 time by &85f7
.map_attrib_bits
    inx                                                               ; 85ef: e8          .              ; Next table entry
    lsr fs_error_ptr                                                  ; 85f0: 46 b8       F.             ; Shift out source bits one at a time
    bcc skip_set_attrib_bit                                           ; 85f2: 90 03       ..             ; Bit was 0: skip this destination bit
    ora access_bit_table,x                                            ; 85f4: 1d fa 85    ...            ; OR in destination bit from lookup table
; &85f7 referenced 1 time by &85f2
.skip_set_attrib_bit
    bne map_attrib_bits                                               ; 85f7: d0 f6       ..             ; Loop while source bits remain (A != 0)
    rts                                                               ; 85f9: 60          `              ; Return; A = converted attribute bitmask

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
    sta fs_load_addr                                                  ; 8606: 85 b0       ..             ; Store return addr low as string ptr
    pla                                                               ; 8608: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 8609: 85 b1       ..             ; Store return addr high as string ptr
    ldy #0                                                            ; 860b: a0 00       ..             ; Y=0: offset for indirect load
; &860d referenced 1 time by &861a
.print_inline_char
    inc fs_load_addr                                                  ; 860d: e6 b0       ..             ; Advance pointer past return address / to next char
    bne print_next_char                                               ; 860f: d0 02       ..             ; No page wrap: skip high byte inc
    inc fs_load_addr_hi                                               ; 8611: e6 b1       ..             ; Handle page crossing in pointer
; &8613 referenced 1 time by &860f
.print_next_char
    lda (fs_load_addr),y                                              ; 8613: b1 b0       ..             ; Load next byte from inline string
    bmi jump_via_addr                                                 ; 8615: 30 06       0.             ; Bit 7 set? Done — this byte is the next opcode
    jsr osasci                                                        ; 8617: 20 e3 ff     ..            ; Write character
    jmp print_inline_char                                             ; 861a: 4c 0d 86    L..            ; Continue printing next character

; &861d referenced 1 time by &8615
.jump_via_addr
    jmp (fs_load_addr)                                                ; 861d: 6c b0 00    l..            ; Jump to address of high-bit byte (resumes code after string)

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
; &8620 referenced 2 times by &808c, &8095
.parse_decimal
    lda #0                                                            ; 8620: a9 00       ..             ; Zero accumulator
    sta fs_load_addr_2                                                ; 8622: 85 b2       ..             ; Initialise accumulator to zero
; &8624 referenced 1 time by &863d
.scan_decimal_digit
    lda (fs_options),y                                                ; 8624: b1 bb       ..             ; Load next char from buffer
    cmp #&2e ; '.'                                                    ; 8626: c9 2e       ..             ; Dot separator?
    beq parse_decimal_rts                                             ; 8628: f0 16       ..             ; Yes: exit with C=1 (dot found)
    bcc no_dot_exit                                                   ; 862a: 90 13       ..             ; Control char or space: done
    and #&0f                                                          ; 862c: 29 0f       ).             ; Mask ASCII digit to 0-9
    sta fs_load_addr_3                                                ; 862e: 85 b3       ..             ; Save new digit
    asl fs_load_addr_2                                                ; 8630: 06 b2       ..             ; Running total * 2
    lda fs_load_addr_2                                                ; 8632: a5 b2       ..             ; A = running total * 2
    asl a                                                             ; 8634: 0a          .              ; A = running total * 4
    asl a                                                             ; 8635: 0a          .              ; A = running total * 8
    adc fs_load_addr_2                                                ; 8636: 65 b2       e.             ; + total*2 = total * 10
    adc fs_load_addr_3                                                ; 8638: 65 b3       e.             ; + digit = total*10 + digit
    sta fs_load_addr_2                                                ; 863a: 85 b2       ..             ; Store new running total
    iny                                                               ; 863c: c8          .              ; Advance to next char
    bne scan_decimal_digit                                            ; 863d: d0 e5       ..             ; Loop (always: Y won't wrap to 0)
; &863f referenced 1 time by &862a
.no_dot_exit
    clc                                                               ; 863f: 18          .              ; No dot found: C=0
; &8640 referenced 1 time by &8628
.parse_decimal_rts
    lda fs_load_addr_2                                                ; 8640: a5 b2       ..             ; Return result in A
    rts                                                               ; 8642: 60          `              ; Return with result in A

; ***************************************************************************************
; Convert handle in A to bitmask
; 
; Transfers A to Y via TAY, then falls through to
; handle_to_mask_clc to clear carry and convert.
; ***************************************************************************************
; &8643 referenced 3 times by &886b, &8a49, &8f53
.handle_to_mask_a
    tay                                                               ; 8643: a8          .              ; Handle number to Y for conversion
; ***************************************************************************************
; Convert handle to bitmask (carry cleared)
; 
; Clears carry to ensure handle_to_mask converts
; unconditionally. Falls through to handle_to_mask.
; ***************************************************************************************
; &8644 referenced 2 times by &841b, &892f
.handle_to_mask_clc
    clc                                                               ; 8644: 18          .              ; Force unconditional conversion
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
; &8645 referenced 1 time by &8998
.handle_to_mask
    pha                                                               ; 8645: 48          H              ; Save A (will be restored on exit)
    txa                                                               ; 8646: 8a          .              ; Save X (will be restored on exit)
    pha                                                               ; 8647: 48          H              ;   (second half of X save)
    tya                                                               ; 8648: 98          .              ; A = handle from Y
    bcc y2fsl5                                                        ; 8649: 90 02       ..             ; C=0: always convert
    beq handle_mask_exit                                              ; 864b: f0 0f       ..             ; C=1 and Y=0: skip (handle 0 = none)
; &864d referenced 1 time by &8649
.y2fsl5
    sec                                                               ; 864d: 38          8              ; C=1 and Y!=0: convert
    sbc #&1f                                                          ; 864e: e9 1f       ..             ; A = handle - &1F (1-based bit position)
    tax                                                               ; 8650: aa          .              ; X = shift count
    lda #1                                                            ; 8651: a9 01       ..             ; Start with bit 0 set
; &8653 referenced 1 time by &8655
.y2fsl2
    asl a                                                             ; 8653: 0a          .              ; Shift bit left
    dex                                                               ; 8654: ca          .              ; Count down
    bne y2fsl2                                                        ; 8655: d0 fc       ..             ; Loop until correct position
    ror a                                                             ; 8657: 6a          j              ; Undo final extra shift
    tay                                                               ; 8658: a8          .              ; Y = resulting bitmask
    bne handle_mask_exit                                              ; 8659: d0 01       ..             ; Non-zero: valid mask, skip to exit
    dey                                                               ; 865b: 88          .              ; Zero: invalid handle, set Y=&FF
; &865c referenced 2 times by &864b, &8659
.handle_mask_exit
    pla                                                               ; 865c: 68          h              ; Restore X
    tax                                                               ; 865d: aa          .              ; Transfer mask to X for return
    pla                                                               ; 865e: 68          h              ; Restore A
    rts                                                               ; 865f: 60          `              ; Return with mask in X

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
    ldx #&1f                                                          ; 8660: a2 1f       ..             ; X = &1F (handle base - 1)
; &8662 referenced 1 time by &8664
.fs2al1
    inx                                                               ; 8662: e8          .              ; Count this bit position
    lsr a                                                             ; 8663: 4a          J              ; Shift mask right; C=0 when done
    bne fs2al1                                                        ; 8664: d0 fc       ..             ; Loop until all bits shifted out
    txa                                                               ; 8666: 8a          .              ; A = X = &1F + bit position = handle
    rts                                                               ; 8667: 60          `              ; Return (identity: no conversion)

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
    ldx #4                                                            ; 8668: a2 04       ..             ; Compare 4 bytes (index 4,3,2,1)
; &866a referenced 1 time by &8671
.compare_addr_byte
    lda addr_work,x                                                   ; 866a: b5 af       ..             ; Load byte from first address
    eor fs_load_addr_3,x                                              ; 866c: 55 b3       U.             ; XOR with corresponding byte
    bne return_compare                                                ; 866e: d0 03       ..             ; Mismatch: Z=0, return unequal
    dex                                                               ; 8670: ca          .              ; Next byte
    bne compare_addr_byte                                             ; 8671: d0 f7       ..             ; Continue comparing
; &8673 referenced 1 time by &866e
.return_compare
    rts                                                               ; 8673: 60          `              ; Return with Z flag result

.fscv_7_read_handles
    ldx #&20 ; ' '                                                    ; 8674: a2 20       .              ; X=first handle (&20)
    ldy #&27 ; '''                                                    ; 8676: a0 27       .'             ; Y=last handle (&27)
.return_fscv_handles
    rts                                                               ; 8678: 60          `              ; Return (FSCV 7 read handles)

; ***************************************************************************************
; Set bit(s) in EOF hint flags (&0E07)
; 
; ORs A into fs_eof_flags then stores the result via
; store_fs_flag. Each bit represents one of up to 8 open file
; handles. When clear, the file is definitely NOT at EOF. When
; set, the fileserver must be queried to confirm EOF status.
; This negative-cache optimisation avoids expensive network
; round-trips for the common case. The hint is cleared when
; the file pointer is updated (since seeking away from EOF
; invalidates the hint) and set after BGET/OPEN/EOF operations
; that might have reached the end.
; ***************************************************************************************
; &8679 referenced 5 times by &8572, &896c, &89c3, &89e3, &8ac4
.set_fs_flag
    ora fs_eof_flags                                                  ; 8679: 0d 07 0e    ...            ; Merge new bits into flags
    bne store_fs_flag                                                 ; 867c: d0 05       ..             ; Store updated flags (always taken)
; ***************************************************************************************
; Clear bit(s) in FS flags (&0E07)
; 
; Inverts A (EOR #&FF), then ANDs the result into fs_eof_flags
; to clear the specified bits.
; ***************************************************************************************
; &867e referenced 3 times by &856f, &8886, &8ac1
.clear_fs_flag
    eor #&ff                                                          ; 867e: 49 ff       I.             ; Invert mask: set bits become clear bits
    and fs_eof_flags                                                  ; 8680: 2d 07 0e    -..            ; Clear specified bits in flags
; &8683 referenced 1 time by &867c
.store_fs_flag
    sta fs_eof_flags                                                  ; 8683: 8d 07 0e    ...            ; Write back updated flags
    rts                                                               ; 8686: 60          `              ; Return

; ***************************************************************************************
; Set up TX pointer to control block at &00C0
; 
; Points net_tx_ptr to &00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; ***************************************************************************************
; &8687 referenced 2 times by &83eb, &8855
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 8687: a2 c0       ..             ; X=&C0: TX control block at &00C0
    stx net_tx_ptr                                                    ; 8689: 86 9a       ..             ; Set TX pointer lo
    ldx #0                                                            ; 868b: a2 00       ..             ; X=0: page zero
    stx net_tx_ptr_hi                                                 ; 868d: 86 9b       ..             ; Set TX pointer hi
; ***************************************************************************************
; Transmit and poll for result (full retry)
; 
; Sets A=&FF (retry count) and Y=&60 (timeout parameter).
; Falls through to tx_poll_core.
; ***************************************************************************************
; &868f referenced 4 times by &901a, &9073, &90d0, &9274
.tx_poll_ff
    lda #&ff                                                          ; 868f: a9 ff       ..             ; A=&FF: full retry count
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
; Two entry points: setup_tx_ptr_c0 (&8687) always uses the
; standard TXCB; tx_poll_core (&8693) is general-purpose.
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
    pha                                                               ; 8693: 48          H              ; Save retry count on stack
    tya                                                               ; 8694: 98          .              ; Transfer timeout to A
    pha                                                               ; 8695: 48          H              ; Save timeout on stack
    ldx #0                                                            ; 8696: a2 00       ..             ; X=0 for (net_tx_ptr,X) indirect
    lda (net_tx_ptr,x)                                                ; 8698: a1 9a       ..             ; Load TXCB byte 0 (control/status)
; &869a referenced 1 time by &86cd
.tx_retry
    sta (net_tx_ptr,x)                                                ; 869a: 81 9a       ..             ; Write control byte to start TX
    pha                                                               ; 869c: 48          H              ; Save control byte for retry
; &869d referenced 1 time by &86a0
.tx_semaphore_spin
    asl tx_clear_flag                                                 ; 869d: 0e 62 0d    .b.            ; Test TX semaphore (C=1 when free)
    bcc tx_semaphore_spin                                             ; 86a0: 90 fb       ..             ; Spin until semaphore released
    lda net_tx_ptr                                                    ; 86a2: a5 9a       ..             ; Copy TX ptr lo to NMI block
    sta nmi_tx_block                                                  ; 86a4: 85 a0       ..             ; Store for NMI handler access
    lda net_tx_ptr_hi                                                 ; 86a6: a5 9b       ..             ; Copy TX ptr hi to NMI block
    sta nmi_tx_block_hi                                               ; 86a8: 85 a1       ..             ; Store for NMI handler access
    jsr trampoline_tx_setup                                           ; 86aa: 20 60 96     `.            ; Initiate ADLC TX via trampoline
; &86ad referenced 1 time by &86af
.l4
.tx_poll_status
    lda (net_tx_ptr,x)                                                ; 86ad: a1 9a       ..             ; Poll TXCB byte 0 for completion
    bmi l4                                                            ; 86af: 30 fc       0.             ; Bit 7 set: still busy, keep polling
    asl a                                                             ; 86b1: 0a          .              ; Shift bit 6 into bit 7 (error flag)
    bpl tx_success                                                    ; 86b2: 10 1f       ..             ; Bit 6 clear: success, clean return
    asl a                                                             ; 86b4: 0a          .              ; Shift bit 5 into carry
    beq tx_not_listening                                              ; 86b5: f0 18       ..             ; Zero: fatal error, no escape
    jsr check_escape_handler                                          ; 86b7: 20 4d 85     M.            ; Check for user escape condition
    pla                                                               ; 86ba: 68          h              ; Discard saved control byte
    tax                                                               ; 86bb: aa          .              ; Save to X for retry delay
    pla                                                               ; 86bc: 68          h              ; Restore timeout parameter
    tay                                                               ; 86bd: a8          .              ; Back to Y
    pla                                                               ; 86be: 68          h              ; Restore retry count
    beq tx_not_listening                                              ; 86bf: f0 0e       ..             ; No retries left: report error
    sbc #1                                                            ; 86c1: e9 01       ..             ; Decrement retry count
    pha                                                               ; 86c3: 48          H              ; Save updated retry count
    tya                                                               ; 86c4: 98          .              ; Timeout to A for delay
    pha                                                               ; 86c5: 48          H              ; Save timeout parameter
    txa                                                               ; 86c6: 8a          .              ; Control byte for delay duration
; &86c7 referenced 2 times by &86c8, &86cb
.msdely
    dex                                                               ; 86c7: ca          .              ; Inner delay loop
    bne msdely                                                        ; 86c8: d0 fd       ..             ; Spin until X=0
    dey                                                               ; 86ca: 88          .              ; Outer delay loop
    bne msdely                                                        ; 86cb: d0 fa       ..             ; Continue delay
    beq tx_retry                                                      ; 86cd: f0 cb       ..             ; ALWAYS branch

; &86cf referenced 2 times by &86b5, &86bf
.tx_not_listening
    tax                                                               ; 86cf: aa          .              ; Save error code in X
    jmp nlistn                                                        ; 86d0: 4c fb 84    L..            ; Report 'Not listening' error

; &86d3 referenced 1 time by &86b2
.tx_success
    pla                                                               ; 86d3: 68          h              ; Discard saved control byte
    pla                                                               ; 86d4: 68          h              ; Discard timeout parameter
    pla                                                               ; 86d5: 68          h              ; Discard retry count
    rts                                                               ; 86d6: 60          `              ; Return (success)

; ***************************************************************************************
; Copy filename pointer to os_text_ptr and parse
; 
; Copies the 2-byte filename pointer from (fs_options),Y into
; os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
; to parse the filename via GSINIT/GSREAD into the &0E30 buffer.
; ***************************************************************************************
; &86d7 referenced 1 time by &8708
.copy_filename_ptr
    ldy #1                                                            ; 86d7: a0 01       ..             ; Y=1: copy 2 bytes (high then low)
; &86d9 referenced 1 time by &86df
.file1
    lda (fs_options),y                                                ; 86d9: b1 bb       ..             ; Load filename ptr from control block
    sta os_text_ptr,y                                                 ; 86db: 99 f2 00    ...            ; Store to MOS text pointer (&F2/&F3)
    dey                                                               ; 86de: 88          .              ; Next byte (descending)
    bpl file1                                                         ; 86df: 10 f8       ..             ; Loop for both bytes
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
    ldy #0                                                            ; 86e1: a0 00       ..             ; Start from beginning of string
; ***************************************************************************************
; Parse filename via GSINIT/GSREAD from offset Y
; 
; Sub-entry of parse_filename_gs that accepts a non-zero Y offset
; into the (os_text_ptr) string. Initialises GSINIT, reads chars
; via GSREAD into &0E30, CR-terminates the result, and sets up
; fs_crc_lo/hi to point at the buffer.
; ***************************************************************************************
; &86e3 referenced 1 time by &8c32
.parse_filename_gs_y
    ldx #&ff                                                          ; 86e3: a2 ff       ..             ; X=&FF: INX will make X=0 (first char index)
    clc                                                               ; 86e5: 18          .              ; C=0 for GSINIT: parse from current position
    jsr gsinit                                                        ; 86e6: 20 c2 ff     ..            ; Initialise GS string parser
    beq terminate_filename                                            ; 86e9: f0 0b       ..             ; Empty string: skip to CR terminator
; &86eb referenced 1 time by &86f4
.quote1
    jsr gsread                                                        ; 86eb: 20 c5 ff     ..            ; Read next character via GSREAD
    bcs terminate_filename                                            ; 86ee: b0 06       ..             ; C=1 from GSREAD: end of string reached
    inx                                                               ; 86f0: e8          .              ; Advance buffer index
    sta fs_filename_buf,x                                             ; 86f1: 9d 30 0e    .0.            ; Store parsed character to &0E30+X
    bcc quote1                                                        ; 86f4: 90 f5       ..             ; ALWAYS loop (GSREAD clears C on success); ALWAYS branch

; &86f6 referenced 2 times by &86e9, &86ee
.terminate_filename
    inx                                                               ; 86f6: e8          .              ; Terminate parsed string with CR
    lda #&0d                                                          ; 86f7: a9 0d       ..             ; CR = &0D
    sta fs_filename_buf,x                                             ; 86f9: 9d 30 0e    .0.            ; Store CR terminator at end of string
    lda #&30 ; '0'                                                    ; 86fc: a9 30       .0             ; Point fs_crc_lo/hi at &0E30 parse buffer
    sta fs_crc_lo                                                     ; 86fe: 85 be       ..             ; fs_crc_lo = &30
    lda #&0e                                                          ; 8700: a9 0e       ..             ; fs_crc_hi = &0E → buffer at &0E30
    sta fs_crc_hi                                                     ; 8702: 85 bf       ..             ; Store high byte
    rts                                                               ; 8704: 60          `              ; Return; X = string length

; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Calls save_fscv_args (&85D2) to preserve A/X/Y, then JSR &86D7
; to copy the 2-byte filename pointer from the parameter block to
; os_text_ptr and fall through to parse_filename_gs (&86E1) which
; parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
; the parsed filename buffer.
; Dispatches by function code A:
;   A=&FF: load file (send_fs_examine at &871B)
;   A=&00: save file (filev_save at &878F)
;   A=&01-&06: attribute operations (filev_attrib_dispatch at &888D)
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
    jsr save_fscv_args                                                ; 8705: 20 d2 85     ..            ; Save A/X/Y in FS workspace
    jsr copy_filename_ptr                                             ; 8708: 20 d7 86     ..            ; Copy filename ptr from param block to os_text_ptr
    lda fs_last_byte_flag                                             ; 870b: a5 bd       ..             ; Recover function code from saved A
    bpl saveop                                                        ; 870d: 10 7b       .{             ; A >= 0: save (&00) or attribs (&01-&06)
    cmp #&ff                                                          ; 870f: c9 ff       ..             ; A=&FF? Only &FF is valid for load
    beq loadop                                                        ; 8711: f0 03       ..             ; A=&FF: branch to load path
    jmp restore_args_return                                           ; 8713: 4c 6f 89    Lo.            ; Unknown negative code: no-op return

; &8716 referenced 1 time by &8711
.loadop
    jsr infol2                                                        ; 8716: 20 75 8d     u.            ; Copy parsed filename to cmd buffer
    ldy #2                                                            ; 8719: a0 02       ..             ; Y=2: FS function code offset
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
    lda #&92                                                          ; 871b: a9 92       ..             ; Port &92 = PLDATA (data transfer port)
    sta fs_cmd_urd                                                    ; 871d: 8d 02 0f    ...            ; Overwrite URD field with data port number
    jsr prepare_cmd_clv                                               ; 8720: 20 b9 83     ..            ; Build FS header (V=1: CLV path)
    ldy #6                                                            ; 8723: a0 06       ..             ; Y=6: param block byte 6
    lda (fs_options),y                                                ; 8725: b1 bb       ..             ; Byte 6: use file's own load address?
    bne lodfil                                                        ; 8727: d0 08       ..             ; Non-zero: use FS reply address (lodfil)
    jsr copy_load_addr_from_params                                    ; 8729: 20 f0 87     ..            ; Zero: copy caller's load addr first
    jsr copy_reply_to_params                                          ; 872c: 20 02 88     ..            ; Then copy FS reply to param block
    bcc skip_lodfil                                                   ; 872f: 90 06       ..             ; Carry clear from prepare_cmd_clv: skip lodfil
; &8731 referenced 1 time by &8727
.lodfil
    jsr copy_reply_to_params                                          ; 8731: 20 02 88     ..            ; Copy FS reply addresses to param block
    jsr copy_load_addr_from_params                                    ; 8734: 20 f0 87     ..            ; Then copy load addr from param block
; &8737 referenced 1 time by &872f
.skip_lodfil
    ldy #4                                                            ; 8737: a0 04       ..             ; Compute end address = load + file length
; &8739 referenced 1 time by &8744
.copy_load_end_addr
    lda fs_load_addr,x                                                ; 8739: b5 b0       ..             ; Load address byte
    sta txcb_end,x                                                    ; 873b: 95 c8       ..             ; Store as current transfer position
    adc fs_file_len,x                                                 ; 873d: 7d 0d 0f    }..            ; Add file length byte
    sta fs_work_4,x                                                   ; 8740: 95 b4       ..             ; Store as end position
    inx                                                               ; 8742: e8          .              ; Next address byte
    dey                                                               ; 8743: 88          .              ; Decrement byte counter
    bne copy_load_end_addr                                            ; 8744: d0 f3       ..             ; Loop for all 4 address bytes
    sec                                                               ; 8746: 38          8              ; Adjust high byte for 3-byte length overflow
    sbc fs_file_len_3                                                 ; 8747: ed 10 0f    ...            ; Subtract 4th length byte from end addr
    sta fs_work_7                                                     ; 874a: 85 b7       ..             ; Store adjusted end address high byte
    jsr print_file_info                                               ; 874c: 20 24 8d     $.            ; Display file info after FS reply
    jsr send_data_blocks                                              ; 874f: 20 5f 87     _.            ; Transfer file data in &80-byte blocks
    ldx #2                                                            ; 8752: a2 02       ..             ; Copy 3-byte file length to FS reply cmd buffer
; &8754 referenced 1 time by &875b
.floop
    lda fs_file_len_3,x                                               ; 8754: bd 10 0f    ...            ; Load file length byte
    sta fs_cmd_data,x                                                 ; 8757: 9d 05 0f    ...            ; Store in FS command data buffer
    dex                                                               ; 875a: ca          .              ; Next byte (count down)
    bpl floop                                                         ; 875b: 10 f7       ..             ; Loop for 3 bytes (X=2,1,0)
    bmi send_fs_reply                                                 ; 875d: 30 74       0t             ; ALWAYS branch

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
    beq return_lodchk                                                 ; 8762: f0 25       .%             ; Addresses match: transfer complete
    lda #&92                                                          ; 8764: a9 92       ..             ; Port &92 for data block transfer
    sta txcb_port                                                     ; 8766: 85 c1       ..             ; Store port to TXCB command byte
; &8768 referenced 1 time by &8784
.send_block_loop
    ldx #3                                                            ; 8768: a2 03       ..             ; Set up next &80-byte block for transfer
; &876a referenced 1 time by &8773
.copy_block_addrs
    lda txcb_end,x                                                    ; 876a: b5 c8       ..             ; Swap: current addr -> source, end -> current
    sta txcb_start,x                                                  ; 876c: 95 c4       ..             ; Source addr = current position
    lda fs_work_4,x                                                   ; 876e: b5 b4       ..             ; Load end address byte
    sta txcb_end,x                                                    ; 8770: 95 c8       ..             ; Dest = end address (will be clamped)
    dex                                                               ; 8772: ca          .              ; Next address byte
    bpl copy_block_addrs                                              ; 8773: 10 f5       ..             ; Loop for all 4 bytes
    lda #&7f                                                          ; 8775: a9 7f       ..             ; Command &7F = data block transfer
    sta txcb_ctrl                                                     ; 8777: 85 c0       ..             ; Store to TXCB control byte
    jsr send_to_fs_star                                               ; 8779: 20 1b 85     ..            ; Send this block to the fileserver
    ldy #3                                                            ; 877c: a0 03       ..             ; Y=3: compare 4 bytes (3..0)
; &877e referenced 1 time by &8787
.lodchk
    lda txcb_end,y                                                    ; 877e: b9 c8 00    ...            ; Compare current vs end address (4 bytes)
    eor fs_work_4,y                                                   ; 8781: 59 b4 00    Y..            ; XOR with end address byte
    bne send_block_loop                                               ; 8784: d0 e2       ..             ; Not equal: more blocks to send
    dey                                                               ; 8786: 88          .              ; Next byte
    bpl lodchk                                                        ; 8787: 10 f5       ..             ; Loop for all 4 address bytes
; &8789 referenced 1 time by &8762
.return_lodchk
    rts                                                               ; 8789: 60          `              ; All equal: transfer complete

; &878a referenced 1 time by &870d
.saveop
    beq filev_save                                                    ; 878a: f0 03       ..             ; A=0: SAVE handler
    jmp filev_attrib_dispatch                                         ; 878c: 4c 8d 88    L..            ; A!=0: attribute dispatch (A=1-6)

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
    ldx #4                                                            ; 878f: a2 04       ..             ; Process 4 address bytes (load/exec/start/end)
    ldy #&0e                                                          ; 8791: a0 0e       ..             ; Y=&0E: start from end-address in param block
; &8793 referenced 1 time by &87ad
.savsiz
    lda (fs_options),y                                                ; 8793: b1 bb       ..             ; Read end-address byte from param block
    sta port_ws_offset,y                                              ; 8795: 99 a6 00    ...            ; Save to port workspace for transfer setup
    jsr sub_4_from_y                                                  ; 8798: 20 0f 88     ..            ; Y = Y-4: point to start-address byte
    sbc (fs_options),y                                                ; 879b: f1 bb       ..             ; end - start = transfer length byte
    sta fs_cmd_csd,y                                                  ; 879d: 99 03 0f    ...            ; Store length byte in FS command buffer
    pha                                                               ; 87a0: 48          H              ; Save length byte for param block restore
    lda (fs_options),y                                                ; 87a1: b1 bb       ..             ; Read corresponding start-address byte
    sta port_ws_offset,y                                              ; 87a3: 99 a6 00    ...            ; Save to port workspace
    pla                                                               ; 87a6: 68          h              ; Restore length byte from stack
    sta (fs_options),y                                                ; 87a7: 91 bb       ..             ; Replace param block entry with length
    jsr add_5_to_y                                                    ; 87a9: 20 fc 87     ..            ; Y = Y+5: advance to next address group
    dex                                                               ; 87ac: ca          .              ; Decrement address byte counter
    bne savsiz                                                        ; 87ad: d0 e4       ..             ; Loop for all 4 address bytes
    ldy #9                                                            ; 87af: a0 09       ..             ; Copy load/exec addresses to FS command buffer
; &87b1 referenced 1 time by &87b7
.copy_save_params
    lda (fs_options),y                                                ; 87b1: b1 bb       ..             ; Read load/exec address byte from params
    sta fs_cmd_csd,y                                                  ; 87b3: 99 03 0f    ...            ; Copy to FS command buffer
    dey                                                               ; 87b6: 88          .              ; Next byte (descending)
    bne copy_save_params                                              ; 87b7: d0 f8       ..             ; Loop for bytes 9..1
    lda #&91                                                          ; 87b9: a9 91       ..             ; Port &91 for save command
    sta fs_cmd_urd                                                    ; 87bb: 8d 02 0f    ...            ; Overwrite URD field with port number
    sta fs_error_ptr                                                  ; 87be: 85 b8       ..             ; Save port &91 for flow control ACK
    ldx #&0b                                                          ; 87c0: a2 0b       ..             ; Append filename at offset &0B in cmd buffer
    jsr copy_string_to_cmd                                            ; 87c2: 20 77 8d     w.            ; Append filename to cmd buffer at offset X
    ldy #1                                                            ; 87c5: a0 01       ..             ; Y=1: function code for save
    jsr prepare_cmd_clv                                               ; 87c7: 20 b9 83     ..            ; Build header and send FS save command
    jsr print_file_info                                               ; 87ca: 20 24 8d     $.            ; Display save info (addr/len)
    lda fs_cmd_data                                                   ; 87cd: ad 05 0f    ...            ; Load reply byte for transfer
    jsr transfer_file_blocks                                          ; 87d0: 20 14 88     ..            ; Print file length in hex
; &87d3 referenced 1 time by &875d
.send_fs_reply
    jsr send_fs_reply_cmd                                             ; 87d3: 20 ef 83     ..            ; Send FS reply acknowledgement
.skip_catalogue_msg
    stx fs_reply_cmd                                                  ; 87d6: 8e 08 0f    ...            ; Store reply command for attr decode
    ldy #&0e                                                          ; 87d9: a0 0e       ..             ; Y=&0E: access byte offset in param block
    lda fs_cmd_data                                                   ; 87db: ad 05 0f    ...            ; Load access byte from FS reply
    jsr decode_attribs_5bit                                           ; 87de: 20 e7 85     ..            ; Convert FS access to BBC attribute format
    beq direct_attr_copy                                              ; 87e1: f0 03       ..             ; Z=1: first byte, use A directly
; &87e3 referenced 1 time by &87eb
.copy_attr_loop
    lda fs_reply_data,y                                               ; 87e3: b9 f7 0e    ...            ; Load attribute byte from FS reply
; &87e6 referenced 1 time by &87e1
.direct_attr_copy
    sta (fs_options),y                                                ; 87e6: 91 bb       ..             ; Store decoded access in param block
    iny                                                               ; 87e8: c8          .              ; Next attribute byte
    cpy #&12                                                          ; 87e9: c0 12       ..             ; Copied all 4 bytes? (Y=&0E..&11)
    bne copy_attr_loop                                                ; 87eb: d0 f6       ..             ; Loop for 4 attribute bytes
    jmp restore_args_return                                           ; 87ed: 4c 6f 89    Lo.            ; Restore A/X/Y and return to caller

; ***************************************************************************************
; Copy load address from parameter block
; 
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to &AE-&B3 (local workspace).
; ***************************************************************************************
; &87f0 referenced 2 times by &8729, &8734
.copy_load_addr_from_params
    ldy #5                                                            ; 87f0: a0 05       ..             ; Start at offset 5 (top of 4-byte addr)
; &87f2 referenced 1 time by &87fa
.lodrl1
    lda (fs_options),y                                                ; 87f2: b1 bb       ..             ; Read from parameter block
    sta work_ae,y                                                     ; 87f4: 99 ae 00    ...            ; Store to local workspace
    dey                                                               ; 87f7: 88          .              ; Next byte (descending)
    cpy #2                                                            ; 87f8: c0 02       ..             ; Copy offsets 5,4,3,2 (4 bytes)
    bcs lodrl1                                                        ; 87fa: b0 f6       ..             ; Loop while Y >= 2
; &87fc referenced 1 time by &87a9
.add_5_to_y
    iny                                                               ; 87fc: c8          .              ; Y=3 after loop; add 5 to get Y=8
; &87fd referenced 1 time by &8a91
.add_4_to_y
    iny                                                               ; 87fd: c8          .              ; INY * 4 = add 4 to Y
    iny                                                               ; 87fe: c8          .              ; Add 1 (of 5) to Y
    iny                                                               ; 87ff: c8          .              ; Add 2 (of 5) to Y
    iny                                                               ; 8800: c8          .              ; Add 3 (of 5) to Y
    rts                                                               ; 8801: 60          `              ; Return

; ***************************************************************************************
; Copy FS reply data to parameter block
; 
; Copies bytes from the FS command reply buffer (&0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; ***************************************************************************************
; &8802 referenced 2 times by &872c, &8731
.copy_reply_to_params
    ldy #&0d                                                          ; 8802: a0 0d       ..             ; Start at offset &0D (top of range)
    txa                                                               ; 8804: 8a          .              ; First store uses X (attrib byte)
; &8805 referenced 1 time by &880d
.lodrl2
    sta (fs_options),y                                                ; 8805: 91 bb       ..             ; Write to parameter block
    lda fs_cmd_urd,y                                                  ; 8807: b9 02 0f    ...            ; Read next byte from reply buffer
    dey                                                               ; 880a: 88          .              ; Next byte (descending)
    cpy #2                                                            ; 880b: c0 02       ..             ; Copy offsets &0D down to 2
    bcs lodrl2                                                        ; 880d: b0 f6       ..             ; Loop until offset 2 reached
; &880f referenced 1 time by &8798
.sub_4_from_y
    dey                                                               ; 880f: 88          .              ; Y=1 after loop; sub 4 to get Y=&FD
; &8810 referenced 2 times by &88a5, &8a99
.sub_3_from_y
    dey                                                               ; 8810: 88          .              ; Subtract 1 (of 3) from Y
    dey                                                               ; 8811: 88          .              ; Subtract 2 (of 3) from Y
    dey                                                               ; 8812: 88          .              ; Subtract 3 (of 3) from Y
    rts                                                               ; 8813: 60          `              ; Return to caller

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
    pha                                                               ; 8814: 48          H              ; Save FS command byte on stack
    jsr compare_addresses                                             ; 8815: 20 68 86     h.            ; Compare two 4-byte addresses
    beq restore_ay_return                                             ; 8818: f0 6f       .o             ; Addresses equal: nothing to transfer
; &881a referenced 1 time by &8867
.next_block
    ldx #0                                                            ; 881a: a2 00       ..             ; X=0: clear hi bytes of block size
    ldy #4                                                            ; 881c: a0 04       ..             ; Y=4: process 4 address bytes
    stx fs_reply_cmd                                                  ; 881e: 8e 08 0f    ...            ; Clear block size hi byte 1
    stx fs_load_vector                                                ; 8821: 8e 09 0f    ...            ; Clear block size hi byte 2
    clc                                                               ; 8824: 18          .              ; CLC for ADC in loop
; &8825 referenced 1 time by &8832
.block_addr_loop
    lda fs_load_addr,x                                                ; 8825: b5 b0       ..             ; Source = current position
    sta txcb_start,x                                                  ; 8827: 95 c4       ..             ; Store source address byte
    adc fs_func_code,x                                                ; 8829: 7d 06 0f    }..            ; Add block size to current position
    sta txcb_end,x                                                    ; 882c: 95 c8       ..             ; Store dest address byte
    sta fs_load_addr,x                                                ; 882e: 95 b0       ..             ; Advance current position
    inx                                                               ; 8830: e8          .              ; Next address byte
    dey                                                               ; 8831: 88          .              ; Decrement byte counter
    bne block_addr_loop                                               ; 8832: d0 f1       ..             ; Loop for all 4 bytes
    bcs clamp_dest_setup                                              ; 8834: b0 0d       ..             ; Carry: address overflowed, clamp
    sec                                                               ; 8836: 38          8              ; SEC for SBC in overshoot check
; &8837 referenced 1 time by &883f
.savchk
    lda fs_load_addr,y                                                ; 8837: b9 b0 00    ...            ; Check if new pos overshot end addr
    sbc fs_work_4,y                                                   ; 883a: f9 b4 00    ...            ; Subtract end address byte
    iny                                                               ; 883d: c8          .              ; Next byte
    dex                                                               ; 883e: ca          .              ; Decrement counter
    bne savchk                                                        ; 883f: d0 f6       ..             ; Loop for 4-byte comparison
    bcc send_block                                                    ; 8841: 90 09       ..             ; C=0: no overshoot, proceed
; &8843 referenced 1 time by &8834
.clamp_dest_setup
    ldx #3                                                            ; 8843: a2 03       ..             ; Overshot: clamp dest to end address
; &8845 referenced 1 time by &884a
.clamp_dest_addr
    lda fs_work_4,x                                                   ; 8845: b5 b4       ..             ; Load end address byte
    sta txcb_end,x                                                    ; 8847: 95 c8       ..             ; Replace dest with end address
    dex                                                               ; 8849: ca          .              ; Next byte
    bpl clamp_dest_addr                                               ; 884a: 10 f9       ..             ; Loop for all 4 bytes
; &884c referenced 1 time by &8841
.send_block
    pla                                                               ; 884c: 68          h              ; Recover original FS command byte
    pha                                                               ; 884d: 48          H              ; Re-push for next iteration
    php                                                               ; 884e: 08          .              ; Save processor flags (C from cmp)
    sta txcb_port                                                     ; 884f: 85 c1       ..             ; Store command byte in TXCB
    lda #&80                                                          ; 8851: a9 80       ..             ; 128-byte block size for data transfer
    sta txcb_ctrl                                                     ; 8853: 85 c0       ..             ; Store size in TXCB control byte
    jsr setup_tx_ptr_c0                                               ; 8855: 20 87 86     ..            ; Point TX ptr to &00C0; transmit
    lda fs_error_ptr                                                  ; 8858: a5 b8       ..             ; ACK port for flow control
    jsr init_tx_ctrl_port                                             ; 885a: 20 85 83     ..            ; Set reply port for ACK receive
    plp                                                               ; 885d: 28          (              ; Restore flags (C=overshoot status)
    bcs restore_ay_return                                             ; 885e: b0 29       .)             ; C=1: all data sent (overshot), done
    lda #&91                                                          ; 8860: a9 91       ..             ; Command &91 = data block transfer
    sta txcb_port                                                     ; 8862: 85 c1       ..             ; Store command &91 in TXCB
    jsr send_to_fs_star                                               ; 8864: 20 1b 85     ..            ; Transmit block and wait (BRIANX)
    bne next_block                                                    ; 8867: d0 b1       ..             ; More blocks? Loop back
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
    pha                                                               ; 8869: 48          H              ; Save A (function code)
    txa                                                               ; 886a: 8a          .              ; X = file handle to check
    jsr handle_to_mask_a                                              ; 886b: 20 43 86     C.            ; Convert handle to bitmask in A
    tya                                                               ; 886e: 98          .              ; Y = handle bitmask from conversion
    and fs_eof_flags                                                  ; 886f: 2d 07 0e    -..            ; Local hint: is EOF possible for this handle?
    tax                                                               ; 8872: aa          .              ; X = result of AND (0 = not at EOF)
    beq restore_ay_return                                             ; 8873: f0 14       ..             ; Hint clear: definitely not at EOF
    pha                                                               ; 8875: 48          H              ; Save bitmask for clear_fs_flag
    sty fs_cmd_data                                                   ; 8876: 8c 05 0f    ...            ; Handle byte in FS command buffer
    ldy #&11                                                          ; 8879: a0 11       ..             ; Y=&11: FS function code FCEOF; Y=function code for HDRFN
    ldx #1                                                            ; 887b: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 887d: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    pla                                                               ; 8880: 68          h              ; Restore bitmask
    ldx fs_cmd_data                                                   ; 8881: ae 05 0f    ...            ; FS reply: non-zero = at EOF
    bne restore_ay_return                                             ; 8884: d0 03       ..             ; At EOF: skip flag clear
    jsr clear_fs_flag                                                 ; 8886: 20 7e 86     ~.            ; Not at EOF: clear the hint bit
; &8889 referenced 4 times by &8818, &885e, &8873, &8884
.restore_ay_return
    pla                                                               ; 8889: 68          h              ; Restore A
    ldy fs_block_offset                                               ; 888a: a4 bc       ..             ; Restore Y
    rts                                                               ; 888c: 60          `              ; Return; X=0 (not EOF) or X=&FF (EOF)

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
    sta fs_cmd_data                                                   ; 888d: 8d 05 0f    ...            ; Store function code in FS cmd buffer
    cmp #6                                                            ; 8890: c9 06       ..             ; A=6? (delete)
    beq cha6                                                          ; 8892: f0 3f       .?             ; Yes: jump to delete handler
    bcs check_attrib_result                                           ; 8894: b0 48       .H             ; A>=7: unsupported, fall through to return
    cmp #5                                                            ; 8896: c9 05       ..             ; A=5? (read catalogue info)
    beq cha5                                                          ; 8898: f0 52       .R             ; Yes: jump to read info handler
    cmp #4                                                            ; 889a: c9 04       ..             ; A=4? (write attributes only)
    beq cha4                                                          ; 889c: f0 44       .D             ; Yes: jump to write attrs handler
    cmp #1                                                            ; 889e: c9 01       ..             ; A=1? (write all catalogue info)
    beq get_file_protection                                           ; 88a0: f0 15       ..             ; Yes: jump to write-all handler
    asl a                                                             ; 88a2: 0a          .              ; A=2 or 3: convert to param block offset
    asl a                                                             ; 88a3: 0a          .              ; A*4: 2->8, 3->12
    tay                                                               ; 88a4: a8          .              ; Y = A*4
    jsr sub_3_from_y                                                  ; 88a5: 20 10 88     ..            ; Y = A*4 - 3 (load addr offset for A=2)
    ldx #3                                                            ; 88a8: a2 03       ..             ; X=3: copy 4 bytes
; &88aa referenced 1 time by &88b1
.chalp1
    lda (fs_options),y                                                ; 88aa: b1 bb       ..             ; Load address byte from param block
    sta fs_func_code,x                                                ; 88ac: 9d 06 0f    ...            ; Store to FS cmd data area
    dey                                                               ; 88af: 88          .              ; Next source byte (descending)
    dex                                                               ; 88b0: ca          .              ; Next dest byte
    bpl chalp1                                                        ; 88b1: 10 f7       ..             ; Loop for 4 bytes
    ldx #5                                                            ; 88b3: a2 05       ..             ; X=5: data extent for filename copy
    bne copy_filename_to_cmd                                          ; 88b5: d0 15       ..             ; ALWAYS branch

; &88b7 referenced 1 time by &88a0
.get_file_protection
    jsr decode_attribs_6bit                                           ; 88b7: 20 dd 85     ..            ; A=1: encode protection from param block
    sta fs_file_attrs                                                 ; 88ba: 8d 0e 0f    ...            ; Store encoded attrs at &0F0E
    ldy #9                                                            ; 88bd: a0 09       ..             ; Y=9: source offset in param block
    ldx #8                                                            ; 88bf: a2 08       ..             ; X=8: dest offset in cmd buffer
; &88c1 referenced 1 time by &88c8
.chalp2
    lda (fs_options),y                                                ; 88c1: b1 bb       ..             ; Load byte from param block
    sta fs_cmd_data,x                                                 ; 88c3: 9d 05 0f    ...            ; Store to FS cmd buffer
    dey                                                               ; 88c6: 88          .              ; Next source byte (descending)
    dex                                                               ; 88c7: ca          .              ; Next dest byte
    bne chalp2                                                        ; 88c8: d0 f7       ..             ; Loop until X=0 (8 bytes copied)
    ldx #&0a                                                          ; 88ca: a2 0a       ..             ; X=&0A: data extent past attrs+addrs
; &88cc referenced 2 times by &88b5, &88ea
.copy_filename_to_cmd
    jsr copy_string_to_cmd                                            ; 88cc: 20 77 8d     w.            ; Append filename to cmd buffer
    ldy #&13                                                          ; 88cf: a0 13       ..             ; Y=&13: fn code for FCSAVE (write attrs)
    bne send_fs_cmd_v1                                                ; 88d1: d0 05       ..             ; ALWAYS branch to send command; ALWAYS branch

; &88d3 referenced 1 time by &8892
.cha6
    jsr infol2                                                        ; 88d3: 20 75 8d     u.            ; A=6: copy filename (delete)
    ldy #&14                                                          ; 88d6: a0 14       ..             ; Y=&14: fn code for FCDEL (delete)
; &88d8 referenced 1 time by &88d1
.send_fs_cmd_v1
    bit tx_ctrl_upper                                                 ; 88d8: 2c af 83    ,..            ; Set V=1 (BIT trick: &B3 has bit 6 set)
    jsr init_tx_ctrl_data                                             ; 88db: 20 c4 83     ..            ; Send via prepare_fs_cmd_v (V=1 path)
; &88de referenced 1 time by &8894
.check_attrib_result
    bcs attrib_error_exit                                             ; 88de: b0 42       .B             ; C=1: &D6 not-found, skip to return
    bcc argsv_check_return                                            ; 88e0: 90 71       .q             ; C=0: success, copy reply to param block; ALWAYS branch

; &88e2 referenced 1 time by &889c
.cha4
    jsr decode_attribs_6bit                                           ; 88e2: 20 dd 85     ..            ; A=4: encode attrs from param block
    sta fs_func_code                                                  ; 88e5: 8d 06 0f    ...            ; Store encoded attrs at &0F06
    ldx #2                                                            ; 88e8: a2 02       ..             ; X=2: data extent (1 attr byte + fn)
    bne copy_filename_to_cmd                                          ; 88ea: d0 e0       ..             ; ALWAYS branch to append filename; ALWAYS branch

; &88ec referenced 1 time by &8898
.cha5
    ldx #1                                                            ; 88ec: a2 01       ..             ; A=5: X=1 (filename only, no data)
    jsr copy_string_to_cmd                                            ; 88ee: 20 77 8d     w.            ; Copy filename to cmd buffer
    ldy #&12                                                          ; 88f1: a0 12       ..             ; Y=&12: fn code for FCEXAM (read info); Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 88f3: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_obj_type                                                   ; 88f6: ad 11 0f    ...            ; Save object type from FS reply
    stx fs_obj_type                                                   ; 88f9: 8e 11 0f    ...            ; Clear reply byte (X=0 on success); X=0 on success, &D6 on not-found
    stx fs_len_clear                                                  ; 88fc: 8e 14 0f    ...            ; Clear length high byte in reply
    jsr decode_attribs_5bit                                           ; 88ff: 20 e7 85     ..            ; Decode 5-bit access byte from FS reply
    ldy #&0e                                                          ; 8902: a0 0e       ..             ; Y=&0E: attrs offset in param block
    sta (fs_options),y                                                ; 8904: 91 bb       ..             ; Store decoded attrs at param block +&0E
    dey                                                               ; 8906: 88          .              ; Y=&0D: start copy below attrs; Y=&0d
    ldx #&0c                                                          ; 8907: a2 0c       ..             ; X=&0C: copy from reply offset &0C down
; &8909 referenced 1 time by &8910
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 8909: bd 05 0f    ...            ; Load reply byte (load/exec/length)
    sta (fs_options),y                                                ; 890c: 91 bb       ..             ; Store to param block
    dey                                                               ; 890e: 88          .              ; Next dest byte (descending)
    dex                                                               ; 890f: ca          .              ; Next source byte
    bne copy_fs_reply_to_cb                                           ; 8910: d0 f7       ..             ; Loop until X=0 (12 bytes copied)
    inx                                                               ; 8912: e8          .              ; X=0 -> X=2 for length high copy
    inx                                                               ; 8913: e8          .              ; INX again: X=2
    ldy #&11                                                          ; 8914: a0 11       ..             ; Y=&11: length high dest in param block
; &8916 referenced 1 time by &891d
.cha5lp
    lda fs_access_level,x                                             ; 8916: bd 12 0f    ...            ; Load length high byte from reply
    sta (fs_options),y                                                ; 8919: 91 bb       ..             ; Store to param block
    dey                                                               ; 891b: 88          .              ; Next dest byte (descending)
    dex                                                               ; 891c: ca          .              ; Next source byte
    bpl cha5lp                                                        ; 891d: 10 f7       ..             ; Loop for 3 length-high bytes
    lda fs_cmd_data                                                   ; 891f: ad 05 0f    ...            ; Return object type in A
; &8922 referenced 1 time by &88de
.attrib_error_exit
    bpl restore_xy_return                                             ; 8922: 10 4d       .M             ; A>=0: branch to restore_args_return
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
    jsr save_fscv_args                                                ; 8924: 20 d2 85     ..            ; Save A/X/Y registers for later restore
    cmp #3                                                            ; 8927: c9 03       ..             ; Function >= 3?
    bcs restore_args_return                                           ; 8929: b0 44       .D             ; A>=3 (ensure/flush): no-op for NFS
    cpy #0                                                            ; 892b: c0 00       ..             ; Test file handle
    beq argsv_fs_query                                                ; 892d: f0 47       .G             ; Y=0: FS-level query, not per-file
    jsr handle_to_mask_clc                                            ; 892f: 20 44 86     D.            ; Convert handle to bitmask
    sty fs_cmd_data                                                   ; 8932: 8c 05 0f    ...            ; Store bitmask as first cmd data byte
    lsr a                                                             ; 8935: 4a          J              ; LSR splits A: C=1 means write (A=1)
    sta fs_func_code                                                  ; 8936: 8d 06 0f    ...            ; Store function code to cmd data byte 2
    bcs save_args_handle                                              ; 8939: b0 1a       ..             ; C=1: write path, copy ptr from caller
    ldy #&0c                                                          ; 893b: a0 0c       ..             ; Y=&0C: FCRDSE (read sequential pointer); Y=function code for HDRFN
    ldx #2                                                            ; 893d: a2 02       ..             ; X=2: 3 data bytes in command; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 893f: 20 c3 83     ..            ; Build and send FS command; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 8942: 85 bd       ..             ; Clear last-byte flag on success; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 8944: a6 bb       ..             ; X = saved control block ptr low
    ldy #2                                                            ; 8946: a0 02       ..             ; Y=2: copy 3 bytes of file pointer
    sta zp_work_3,x                                                   ; 8948: 95 03       ..             ; Zero high byte of 3-byte pointer
; &894a referenced 1 time by &8951
.copy_fileptr_reply
    lda fs_cmd_data,y                                                 ; 894a: b9 05 0f    ...            ; Read reply byte from FS cmd data
    sta zp_work_2,x                                                   ; 894d: 95 02       ..             ; Store to caller's control block
    dex                                                               ; 894f: ca          .              ; Next byte (descending)
    dey                                                               ; 8950: 88          .              ; Next source byte
    bpl copy_fileptr_reply                                            ; 8951: 10 f7       ..             ; Loop for all 3 bytes
; &8953 referenced 1 time by &88e0
.argsv_check_return
    bcc restore_args_return                                           ; 8953: 90 1a       ..             ; C=0 (read): return to caller
; &8955 referenced 1 time by &8939
.save_args_handle
    tya                                                               ; 8955: 98          .              ; Save bitmask for set_fs_flag later
    pha                                                               ; 8956: 48          H              ; Push bitmask
    ldy #3                                                            ; 8957: a0 03       ..             ; Y=3: copy 4 bytes of file pointer
; &8959 referenced 1 time by &8960
.copy_fileptr_to_cmd
    lda zp_work_3,x                                                   ; 8959: b5 03       ..             ; Read caller's pointer byte
    sta fs_data_count,y                                               ; 895b: 99 07 0f    ...            ; Store to FS command data area
    dex                                                               ; 895e: ca          .              ; Next source byte
    dey                                                               ; 895f: 88          .              ; Next destination byte
    bpl copy_fileptr_to_cmd                                           ; 8960: 10 f7       ..             ; Loop for all 4 bytes
    ldy #&0d                                                          ; 8962: a0 0d       ..             ; Y=&0D: FCWRSE (write sequential pointer); Y=function code for HDRFN
    ldx #5                                                            ; 8964: a2 05       ..             ; X=5: 6 data bytes in command; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8966: 20 c3 83     ..            ; Build and send FS command; Prepare FS command buffer (12 references)
    stx fs_last_byte_flag                                             ; 8969: 86 bd       ..             ; Save not-found status from X; X=0 on success, &D6 on not-found
    pla                                                               ; 896b: 68          h              ; Recover bitmask for EOF hint update
    jsr set_fs_flag                                                   ; 896c: 20 79 86     y.            ; Set EOF hint bit for this handle
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
    lda fs_last_byte_flag                                             ; 896f: a5 bd       ..             ; A = saved function code / command
; &8971 referenced 5 times by &8922, &8982, &8992, &89bd, &89ca
.restore_xy_return
    ldx fs_options                                                    ; 8971: a6 bb       ..             ; X = saved control block ptr low
    ldy fs_block_offset                                               ; 8973: a4 bc       ..             ; Y = saved control block ptr high
    rts                                                               ; 8975: 60          `              ; Return to MOS with registers restored

; &8976 referenced 1 time by &892d
.argsv_fs_query
    cmp #2                                                            ; 8976: c9 02       ..             ; A=0: *ARGS Y,0; A=1: *ARGS Y,1; A>=2: FS; Y=0: FS-level queries (no file handle)
    beq halve_args_a                                                  ; 8978: f0 07       ..             ; A=2: FS-level ensure (write extent)
    bcs return_a_zero                                                 ; 897a: b0 14       ..             ; A>=3: FS command (ARGSV write)
    tay                                                               ; 897c: a8          .              ; Y = A = byte count for copy loop
    bne osarg1                                                        ; 897d: d0 05       ..             ; A!=0: copy command context block
    lda #&0a                                                          ; 897f: a9 0a       ..             ; &0A >> 1 = 5 = NFS filing system number; FS number 5 (loaded as &0A, LSR'd)
; &8981 referenced 1 time by &8978
.halve_args_a
    lsr a                                                             ; 8981: 4a          J              ; Shared: halve A (A=0 or A=2 paths); Shared: A=0->&05, A=2->&01
    bne restore_xy_return                                             ; 8982: d0 ed       ..             ; Return with A = FS number or 1
; &8984 referenced 2 times by &897d, &898a
.osarg1
    lda fs_cmd_context,y                                              ; 8984: b9 0a 0e    ...            ; Read FS command context byte; Copy command context to caller's block
    sta (fs_options),y                                                ; 8987: 91 bb       ..             ; Store to caller's parameter block
    dey                                                               ; 8989: 88          .              ; Next byte (descending)
    bpl osarg1                                                        ; 898a: 10 f8       ..             ; Loop until all bytes copied
    sty zp_work_2,x                                                   ; 898c: 94 02       ..             ; Y=&FF after loop; fill high bytes
    sty zp_work_3,x                                                   ; 898e: 94 03       ..             ; Set 32-bit result bytes 2-3 to &FF
; ***************************************************************************************
; Return with A=0 via register restore
; 
; Loads A=0 and branches (always taken) to the common register
; restore exit at restore_args_return. Used as a shared exit
; point by ARGSV, FINDV, and GBPBV when an operation is
; unsupported or should return zero.
; ***************************************************************************************
; &8990 referenced 4 times by &897a, &89a0, &8ad5, &8b77
.return_a_zero
    lda #0                                                            ; 8990: a9 00       ..             ; A=operation (0=close, &40=read, &80=write, &C0=R/W)
    bpl restore_xy_return                                             ; 8992: 10 dd       ..             ; ALWAYS branch

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
    jsr save_fscv_args_with_ptrs                                      ; 8994: 20 c8 85     ..            ; Save A/X/Y and set up pointers
    sec                                                               ; 8997: 38          8              ; SEC distinguishes open (A>0) from close
    jsr handle_to_mask                                                ; 8998: 20 45 86     E.            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 899b: aa          .              ; A=preserved
    beq close_handle                                                  ; 899c: f0 2e       ..             ; A=0: close file(s)
    and #&3f ; '?'                                                    ; 899e: 29 3f       )?             ; Valid open modes: &40, &80, &C0 only
    bne return_a_zero                                                 ; 89a0: d0 ee       ..             ; Invalid mode bits: return
    txa                                                               ; 89a2: 8a          .              ; A = original mode byte
    eor #&80                                                          ; 89a3: 49 80       I.             ; Convert MOS mode to FS protocol flags
    asl a                                                             ; 89a5: 0a          .              ; ASL: shift mode bits left
    sta fs_cmd_data                                                   ; 89a6: 8d 05 0f    ...            ; Flag 1: read/write direction
    rol a                                                             ; 89a9: 2a          *              ; ROL: Flag 2 into bit 0
    sta fs_func_code                                                  ; 89aa: 8d 06 0f    ...            ; Flag 2: create vs existing file
    jsr parse_filename_gs                                             ; 89ad: 20 e1 86     ..            ; Parse filename from command line
    ldx #2                                                            ; 89b0: a2 02       ..             ; X=2: copy after 2-byte flags
    jsr copy_string_to_cmd                                            ; 89b2: 20 77 8d     w.            ; Copy filename to FS command buffer
    ldy #6                                                            ; 89b5: a0 06       ..             ; Y=6: FS function code FCOPEN
    bit tx_ctrl_upper                                                 ; 89b7: 2c af 83    ,..            ; Set V flag from l83b3 bit 6
    jsr init_tx_ctrl_data                                             ; 89ba: 20 c4 83     ..            ; Build and send FS open command
    bcs restore_xy_return                                             ; 89bd: b0 b2       ..             ; Error: restore and return
    lda fs_cmd_data                                                   ; 89bf: ad 05 0f    ...            ; Load reply handle from FS
    tax                                                               ; 89c2: aa          .              ; X = new file handle
    jsr set_fs_flag                                                   ; 89c3: 20 79 86     y.            ; Set EOF hint + sequence bits
; OR handle bit into fs_sequence_nos (&0E08) to prevent
; a newly opened file inheriting a stale sequence number
; from a previous file using the same handle.
    txa                                                               ; 89c6: 8a          .              ; A=handle bitmask for new file; A=single-bit bitmask
    jsr mask_to_handle                                                ; 89c7: 20 60 86     `.            ; Convert bitmask to handle number (FS2A)
    bne restore_xy_return                                             ; 89ca: d0 a5       ..             ; ALWAYS branch to restore and return
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
    tya                                                               ; 89cc: 98          .              ; A = handle (Y preserved in A); Y=preserved
    bne close_single_handle                                           ; 89cd: d0 07       ..             ; Y>0: close single file
    lda #osbyte_close_spool_exec                                      ; 89cf: a9 77       .w             ; Close SPOOL/EXEC before FS close-all
    jsr osbyte                                                        ; 89d1: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 89d4: a0 00       ..             ; Y=0: close all handles on server
; &89d6 referenced 1 time by &89cd
.close_single_handle
    sty fs_cmd_data                                                   ; 89d6: 8c 05 0f    ...            ; Handle byte in FS command buffer
    ldx #1                                                            ; 89d9: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 89db: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89dd: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 89e0: ad 05 0f    ...            ; Reply handle for flag update
    jsr set_fs_flag                                                   ; 89e3: 20 79 86     y.            ; Update EOF/sequence tracking bits
; &89e6 referenced 1 time by &8a0c
.close_opt_return
    bcc restore_args_return                                           ; 89e6: 90 87       ..             ; C=0: restore A/X/Y and return
.fscv_0_opt_entry
    beq set_messages_flag                                             ; 89e8: f0 0b       ..             ; Entry from fscv_0_opt (close-all path)
; ***************************************************************************************
; FSCV 0: *OPT handler (OPTION)
; 
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
; Other combinations generate error &CB (OPTER: "bad option").
; ***************************************************************************************
.fscv_0_opt
    cpx #4                                                            ; 89ea: e0 04       ..             ; Is it *OPT 4,Y?
    bne check_opt1                                                    ; 89ec: d0 04       ..             ; No: check for *OPT 1
    cpy #4                                                            ; 89ee: c0 04       ..             ; Y must be 0-3 for boot option
    bcc optl1                                                         ; 89f0: 90 0d       ..             ; Y < 4: valid boot option
; &89f2 referenced 1 time by &89ec
.check_opt1
    dex                                                               ; 89f2: ca          .              ; Not *OPT 4: check for *OPT 1
    bne opter1                                                        ; 89f3: d0 05       ..             ; Not *OPT 1 either: bad option
; &89f5 referenced 1 time by &89e8
.set_messages_flag
    sty fs_messages_flag                                              ; 89f5: 8c 06 0e    ...            ; Set local messages flag (*OPT 1,Y)
    bcc opt_return                                                    ; 89f8: 90 12       ..             ; Return via restore_args_return
; &89fa referenced 1 time by &89f3
.opter1
    lda #7                                                            ; 89fa: a9 07       ..             ; Error index 7 (Bad option)
    jmp nlisne                                                        ; 89fc: 4c fd 84    L..            ; Generate BRK error

; &89ff referenced 1 time by &89f0
.optl1
    sty fs_cmd_data                                                   ; 89ff: 8c 05 0f    ...            ; Boot option value in FS command
    ldy #&16                                                          ; 8a02: a0 16       ..             ; Y=&16: FS function code FCOPT; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8a04: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 8a07: a4 bc       ..             ; Restore Y from saved value
    sty fs_boot_option                                                ; 8a09: 8c 05 0e    ...            ; Cache boot option locally
; &8a0c referenced 1 time by &89f8
.opt_return
    bcc close_opt_return                                              ; 8a0c: 90 d8       ..             ; Return via restore_args_return
; &8a0e referenced 1 time by &8ac9
.adjust_addrs_9
    ldy #9                                                            ; 8a0e: a0 09       ..             ; Y=9: adjust 9 address bytes
    jsr adjust_addrs_clc                                              ; 8a10: 20 15 8a     ..            ; Adjust with carry clear
; &8a13 referenced 1 time by &8bbe
.adjust_addrs_1
    ldy #1                                                            ; 8a13: a0 01       ..             ; Y=1: adjust 1 address byte
; &8a15 referenced 1 time by &8a10
.adjust_addrs_clc
    clc                                                               ; 8a15: 18          .              ; C=0 for address adjustment
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
    ldx #&fc                                                          ; 8a16: a2 fc       ..             ; X=&FC: index into &0E06 area (wraps to 0)
; &8a18 referenced 1 time by &8a2b
.adjust_addr_byte
    lda (fs_options),y                                                ; 8a18: b1 bb       ..             ; Load byte from param block
    bit fs_load_addr_2                                                ; 8a1a: 24 b2       $.             ; Test sign of adjustment direction
    bmi subtract_adjust                                               ; 8a1c: 30 06       0.             ; Negative: subtract instead
    adc fs_cmd_context,x                                              ; 8a1e: 7d 0a 0e    }..            ; Add adjustment value
    jmp gbpbx                                                         ; 8a21: 4c 27 8a    L'.            ; Skip to store result

; &8a24 referenced 1 time by &8a1c
.subtract_adjust
    sbc fs_cmd_context,x                                              ; 8a24: fd 0a 0e    ...            ; Subtract adjustment value
; &8a27 referenced 1 time by &8a21
.gbpbx
    sta (fs_options),y                                                ; 8a27: 91 bb       ..             ; Store adjusted byte back
    iny                                                               ; 8a29: c8          .              ; Next param block byte
    inx                                                               ; 8a2a: e8          .              ; Next adjustment byte (X wraps &FC->&00)
    bne adjust_addr_byte                                              ; 8a2b: d0 eb       ..             ; Loop 4 times (X=&FC,&FD,&FE,&FF,done)
    rts                                                               ; 8a2d: 60          `              ; Return (unsupported function)

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
    jsr save_fscv_args                                                ; 8a2e: 20 d2 85     ..            ; Save A/X/Y to FS workspace
    tax                                                               ; 8a31: aa          .              ; X = call number for range check
    beq gbpb_invalid_exit                                             ; 8a32: f0 05       ..             ; A=0: invalid, restore and return
    dex                                                               ; 8a34: ca          .              ; Convert to 0-based (A=0..7)
    cpx #8                                                            ; 8a35: e0 08       ..             ; Range check: must be 0-7
    bcc gbpbx1                                                        ; 8a37: 90 03       ..             ; In range: continue to handler
; &8a39 referenced 1 time by &8a32
.gbpb_invalid_exit
    jmp restore_args_return                                           ; 8a39: 4c 6f 89    Lo.            ; Out of range: restore args and return

; &8a3c referenced 1 time by &8a37
.gbpbx1
    txa                                                               ; 8a3c: 8a          .              ; Recover 0-based function code
    ldy #0                                                            ; 8a3d: a0 00       ..             ; Y=0: param block byte 0 (file handle)
    pha                                                               ; 8a3f: 48          H              ; Save function code on stack
    cmp #4                                                            ; 8a40: c9 04       ..             ; A>=4: info queries, dispatch separately
    bcc gbpbe1                                                        ; 8a42: 90 03       ..             ; A<4: file read/write operations
    jmp osgbpb_info                                                   ; 8a44: 4c ed 8a    L..            ; Dispatch to OSGBPB 5-8 info handler

; &8a47 referenced 1 time by &8a42
.gbpbe1
    lda (fs_options),y                                                ; 8a47: b1 bb       ..             ; Get file handle from param block byte 0
    jsr handle_to_mask_a                                              ; 8a49: 20 43 86     C.            ; Convert handle to bitmask for EOF flags
    sty fs_cmd_data                                                   ; 8a4c: 8c 05 0f    ...            ; Store handle in FS command data
    ldy #&0b                                                          ; 8a4f: a0 0b       ..             ; Y=&0B: start at param block byte 11
    ldx #6                                                            ; 8a51: a2 06       ..             ; X=6: copy 6 bytes of transfer params
; &8a53 referenced 1 time by &8a5f
.gbpbf1
    lda (fs_options),y                                                ; 8a53: b1 bb       ..             ; Load param block byte
    sta fs_func_code,x                                                ; 8a55: 9d 06 0f    ...            ; Store to FS command buffer at &0F06+X
    dey                                                               ; 8a58: 88          .              ; Previous param block byte
    cpy #8                                                            ; 8a59: c0 08       ..             ; Skip param block offset 8 (the handle)
    bne gbpbx0                                                        ; 8a5b: d0 01       ..             ; Not at handle offset: continue
    dey                                                               ; 8a5d: 88          .              ; Extra DEY to skip handle byte
; &8a5e referenced 1 time by &8a5b
.gbpbx0
.gbpbf2
    dex                                                               ; 8a5e: ca          .              ; Decrement copy counter
    bne gbpbf1                                                        ; 8a5f: d0 f2       ..             ; Loop for all 6 bytes
    pla                                                               ; 8a61: 68          h              ; Recover function code from stack
    lsr a                                                             ; 8a62: 4a          J              ; LSR: odd=read (C=1), even=write (C=0)
    pha                                                               ; 8a63: 48          H              ; Save function code again (need C later)
    bcc gbpbl1                                                        ; 8a64: 90 01       ..             ; Even (write): X stays 0
    inx                                                               ; 8a66: e8          .              ; Odd (read): X=1
; &8a67 referenced 1 time by &8a64
.gbpbl1
    stx fs_func_code                                                  ; 8a67: 8e 06 0f    ...            ; Store FS direction flag
    ldy #&0b                                                          ; 8a6a: a0 0b       ..             ; Y=&0B: command data extent
    ldx #&91                                                          ; 8a6c: a2 91       ..             ; Command &91=put, &92=get
    pla                                                               ; 8a6e: 68          h              ; Recover function code
    pha                                                               ; 8a6f: 48          H              ; Save again for later direction check
    beq gbpb_write_path                                               ; 8a70: f0 03       ..             ; Even (write): keep &91 and Y=&0B
    ldx #&92                                                          ; 8a72: a2 92       ..             ; Odd (read): use &92 (get) instead
    dey                                                               ; 8a74: 88          .              ; Read: one fewer data byte in command; Y=&0a
; &8a75 referenced 1 time by &8a70
.gbpb_write_path
    stx fs_cmd_urd                                                    ; 8a75: 8e 02 0f    ...            ; Store port to FS command URD field
    stx fs_error_ptr                                                  ; 8a78: 86 b8       ..             ; Save port for error recovery
    ldx #8                                                            ; 8a7a: a2 08       ..             ; X=8: command data bytes
    lda fs_cmd_data                                                   ; 8a7c: ad 05 0f    ...            ; Load handle from FS command data
    jsr prepare_cmd_with_flag                                         ; 8a7f: 20 b5 83     ..            ; Build FS command with handle+flag
    lda fs_load_addr_3                                                ; 8a82: a5 b3       ..             ; Save seq# for byte-stream flow control
    sta fs_sequence_nos                                               ; 8a84: 8d 08 0e    ...            ; Store to FS sequence number workspace
    ldx #4                                                            ; 8a87: a2 04       ..             ; X=4: copy 4 address bytes
; &8a89 referenced 1 time by &8a9d
.gbpbl3
    lda (fs_options),y                                                ; 8a89: b1 bb       ..             ; Set up source/dest from param block
    sta addr_work,y                                                   ; 8a8b: 99 af 00    ...            ; Store as source address
    sta txcb_pos,y                                                    ; 8a8e: 99 c7 00    ...            ; Store as current transfer position
    jsr add_4_to_y                                                    ; 8a91: 20 fd 87     ..            ; Skip 4 bytes to reach transfer length
    adc (fs_options),y                                                ; 8a94: 71 bb       q.             ; Dest = source + length
    sta addr_work,y                                                   ; 8a96: 99 af 00    ...            ; Store as end address
    jsr sub_3_from_y                                                  ; 8a99: 20 10 88     ..            ; Back 3 to align for next iteration
    dex                                                               ; 8a9c: ca          .              ; Decrement byte counter
    bne gbpbl3                                                        ; 8a9d: d0 ea       ..             ; Loop for all 4 address bytes
    inx                                                               ; 8a9f: e8          .              ; X=1 after loop
; &8aa0 referenced 1 time by &8aa7
.gbpbf3
    lda fs_cmd_csd,x                                                  ; 8aa0: bd 03 0f    ...            ; Copy CSD data to command buffer
    sta fs_func_code,x                                                ; 8aa3: 9d 06 0f    ...            ; Store at &0F06+X
    dex                                                               ; 8aa6: ca          .              ; Decrement counter
    bpl gbpbf3                                                        ; 8aa7: 10 f7       ..             ; Loop for X=1,0
    pla                                                               ; 8aa9: 68          h              ; Odd (read): send data to FS first
    bne gbpb_read_path                                                ; 8aaa: d0 08       ..             ; Non-zero: skip write path
    lda fs_cmd_urd                                                    ; 8aac: ad 02 0f    ...            ; Load port for transfer setup
    jsr transfer_file_blocks                                          ; 8aaf: 20 14 88     ..            ; Transfer data blocks to fileserver
    bcs wait_fs_reply                                                 ; 8ab2: b0 03       ..             ; Carry set: transfer error
; &8ab4 referenced 1 time by &8aaa
.gbpb_read_path
    jsr send_data_blocks                                              ; 8ab4: 20 5f 87     _.            ; Read path: receive data blocks from FS
; &8ab7 referenced 1 time by &8ab2
.wait_fs_reply
    jsr send_fs_reply_cmd                                             ; 8ab7: 20 ef 83     ..            ; Wait for FS reply command
    lda (fs_options,x)                                                ; 8aba: a1 bb       ..             ; Load handle mask for EOF flag update
    bit fs_cmd_data                                                   ; 8abc: 2c 05 0f    ,..            ; Check FS reply: bit 7 = not at EOF
    bmi skip_clear_flag                                               ; 8abf: 30 03       0.             ; Bit 7 set: not EOF, skip clear
    jsr clear_fs_flag                                                 ; 8ac1: 20 7e 86     ~.            ; At EOF: clear EOF hint for this handle
; &8ac4 referenced 1 time by &8abf
.skip_clear_flag
    jsr set_fs_flag                                                   ; 8ac4: 20 79 86     y.            ; Set EOF hint flag (may be at EOF)
    stx fs_load_addr_2                                                ; 8ac7: 86 b2       ..             ; Direction=0: forward adjustment
    jsr adjust_addrs_9                                                ; 8ac9: 20 0e 8a     ..            ; Adjust param block addrs by +9 bytes
    dec fs_load_addr_2                                                ; 8acc: c6 b2       ..             ; Direction=&FF: reverse adjustment
    sec                                                               ; 8ace: 38          8              ; SEC for reverse subtraction
    jsr adjust_addrs                                                  ; 8acf: 20 16 8a     ..            ; Adjust param block addrs (reverse)
    asl fs_cmd_data                                                   ; 8ad2: 0e 05 0f    ...            ; Shift bit 7 into C for return flag
    jmp return_a_zero                                                 ; 8ad5: 4c 90 89    L..            ; Return via restore_args path

; &8ad8 referenced 1 time by &8b08
.get_disc_title
    ldy #&15                                                          ; 8ad8: a0 15       ..             ; Y=&15: function code for disc title; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8ada: 20 c3 83     ..            ; Build and send FS command; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8add: ad 05 0e    ...            ; Load boot option from FS workspace
    sta fs_boot_data                                                  ; 8ae0: 8d 16 0f    ...            ; Store boot option in reply area
    stx fs_load_addr                                                  ; 8ae3: 86 b0       ..             ; X=0: reply data start offset; X=0 on success, &D6 on not-found
    stx fs_load_addr_hi                                               ; 8ae5: 86 b1       ..             ; Clear reply buffer high byte
    lda #&12                                                          ; 8ae7: a9 12       ..             ; A=&12: 18 bytes of reply data
    sta fs_load_addr_2                                                ; 8ae9: 85 b2       ..             ; Store as byte count for copy
    bne copy_reply_to_caller                                          ; 8aeb: d0 4e       .N             ; ALWAYS branch to copy_reply_to_caller; ALWAYS branch

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
    ldy #4                                                            ; 8aed: a0 04       ..             ; Y=4: check param block byte 4
    lda tube_flag                                                     ; 8aef: ad 67 0d    .g.            ; Check if destination is in Tube space
    beq store_tube_flag                                               ; 8af2: f0 07       ..             ; No Tube: skip Tube address check
    cmp (fs_options),y                                                ; 8af4: d1 bb       ..             ; Compare Tube flag with addr byte 4
    bne store_tube_flag                                               ; 8af6: d0 03       ..             ; Mismatch: not Tube space
    dey                                                               ; 8af8: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8af9: f1 bb       ..             ; Y=3: subtract addr byte 3 from flag
; &8afb referenced 2 times by &8af2, &8af6
.store_tube_flag
    sta svc_state                                                     ; 8afb: 85 a9       ..             ; Non-zero = Tube transfer required
; &8afd referenced 1 time by &8b03
.info2
    lda (fs_options),y                                                ; 8afd: b1 bb       ..             ; Copy param block bytes 1-4 to workspace
    sta fs_last_byte_flag,y                                           ; 8aff: 99 bd 00    ...            ; Store to &BD+Y workspace area
    dey                                                               ; 8b02: 88          .              ; Previous byte
    bne info2                                                         ; 8b03: d0 f8       ..             ; Loop for bytes 3,2,1
    pla                                                               ; 8b05: 68          h              ; Sub-function: AND #3 of (original A - 4)
    and #3                                                            ; 8b06: 29 03       ).             ; Mask to 0-3 (OSGBPB 5-8 → 0-3)
    beq get_disc_title                                                ; 8b08: f0 ce       ..             ; A=0 (OSGBPB 5): read disc title
    lsr a                                                             ; 8b0a: 4a          J              ; LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)
    beq gbpb6_read_name                                               ; 8b0b: f0 02       ..             ; A=0 (OSGBPB 6): read CSD/LIB name
    bcs gbpb8_read_dir                                                ; 8b0d: b0 6b       .k             ; C=1 (OSGBPB 8): read filenames from dir
; &8b0f referenced 1 time by &8b0b
.gbpb6_read_name
    tay                                                               ; 8b0f: a8          .              ; Y=0 for CSD or carry for fn code select; Y=function code
    lda fs_csd_handle,y                                               ; 8b10: b9 03 0e    ...            ; Get CSD/LIB/URD handles for FS command
    sta fs_cmd_csd                                                    ; 8b13: 8d 03 0f    ...            ; Store CSD handle in command buffer
    lda fs_lib_handle                                                 ; 8b16: ad 04 0e    ...            ; Load LIB handle from workspace
    sta fs_cmd_lib                                                    ; 8b19: 8d 04 0f    ...            ; Store LIB handle in command buffer
    lda fs_urd_handle                                                 ; 8b1c: ad 02 0e    ...            ; Load URD handle from workspace
    sta fs_cmd_urd                                                    ; 8b1f: 8d 02 0f    ...            ; Store URD handle in command buffer
    ldx #&12                                                          ; 8b22: a2 12       ..             ; X=&12: buffer extent for command data; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8b24: 8e 01 0f    ...            ; Store X as function code in header
    lda #&0d                                                          ; 8b27: a9 0d       ..             ; &0D = 13 bytes of reply data expected
    sta fs_func_code                                                  ; 8b29: 8d 06 0f    ...            ; Store reply length in command buffer
    sta fs_load_addr_2                                                ; 8b2c: 85 b2       ..             ; Store as byte count for copy loop
    lsr a                                                             ; 8b2e: 4a          J              ; LSR: &0D >> 1 = 6; A=timeout period for FS reply
    sta fs_cmd_data                                                   ; 8b2f: 8d 05 0f    ...            ; Store as command data byte
    clc                                                               ; 8b32: 18          .              ; CLC for standard FS path
    jsr build_send_fs_cmd                                             ; 8b33: 20 d9 83     ..            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8b36: 86 b1       ..             ; X=0 on success, &D6 on not-found
    inx                                                               ; 8b38: e8          .              ; INX: X=1 after build_send_fs_cmd
    stx fs_load_addr                                                  ; 8b39: 86 b0       ..             ; Store X as reply start offset
; &8b3b referenced 2 times by &8aeb, &8bb3
.copy_reply_to_caller
    lda svc_state                                                     ; 8b3b: a5 a9       ..             ; Copy FS reply to caller's buffer
    bne tube_transfer                                                 ; 8b3d: d0 11       ..             ; Non-zero: use Tube transfer path
    ldx fs_load_addr                                                  ; 8b3f: a6 b0       ..             ; X = reply start offset
    ldy fs_load_addr_hi                                               ; 8b41: a4 b1       ..             ; Y = reply buffer high byte
; &8b43 referenced 1 time by &8b4c
.copy_reply_bytes
    lda fs_cmd_data,x                                                 ; 8b43: bd 05 0f    ...            ; Load reply data byte
    sta (fs_crc_lo),y                                                 ; 8b46: 91 be       ..             ; Store to caller's buffer
    inx                                                               ; 8b48: e8          .              ; Next source byte
    iny                                                               ; 8b49: c8          .              ; Next destination byte
    dec fs_load_addr_2                                                ; 8b4a: c6 b2       ..             ; Decrement remaining bytes
    bne copy_reply_bytes                                              ; 8b4c: d0 f5       ..             ; Loop until all bytes copied
    beq gbpb_done                                                     ; 8b4e: f0 27       .'             ; ALWAYS branch to exit; ALWAYS branch

; &8b50 referenced 1 time by &8b3d
.tube_transfer
    jsr tube_claim_loop                                               ; 8b50: 20 cf 8b     ..            ; Claim Tube transfer channel
    lda #1                                                            ; 8b53: a9 01       ..             ; A=1: Tube claim type 1 (write)
    ldx fs_options                                                    ; 8b55: a6 bb       ..             ; X = param block address low
    ldy fs_block_offset                                               ; 8b57: a4 bc       ..             ; Y = param block address high
    inx                                                               ; 8b59: e8          .              ; INX: advance past byte 0
    bne no_page_wrap                                                  ; 8b5a: d0 01       ..             ; No page wrap: keep Y
    iny                                                               ; 8b5c: c8          .              ; Page wrap: increment high byte
; &8b5d referenced 1 time by &8b5a
.no_page_wrap
    jsr tube_addr_claim                                               ; 8b5d: 20 06 04     ..            ; Claim Tube address for transfer
    ldx fs_load_addr                                                  ; 8b60: a6 b0       ..             ; X = reply data start offset
; &8b62 referenced 1 time by &8b70
.tbcop1
    lda fs_cmd_data,x                                                 ; 8b62: bd 05 0f    ...            ; Load reply data byte
    sta tube_data_register_3                                          ; 8b65: 8d e5 fe    ...            ; Send byte to Tube via R3
    inx                                                               ; 8b68: e8          .              ; Next source byte
    ldy #6                                                            ; 8b69: a0 06       ..             ; Delay loop for slow Tube co-processor
; &8b6b referenced 1 time by &8b6c
.wait_tube_delay
    dey                                                               ; 8b6b: 88          .              ; Decrement delay counter
    bne wait_tube_delay                                               ; 8b6c: d0 fd       ..             ; Loop until delay complete
    dec fs_load_addr_2                                                ; 8b6e: c6 b2       ..             ; Decrement remaining bytes
    bne tbcop1                                                        ; 8b70: d0 f0       ..             ; Loop until all bytes sent to Tube
    lda #&83                                                          ; 8b72: a9 83       ..             ; Release Tube after transfer complete
    jsr tube_addr_claim                                               ; 8b74: 20 06 04     ..            ; Release Tube address claim
; &8b77 referenced 2 times by &8b4e, &8bcd
.gbpb_done
    jmp return_a_zero                                                 ; 8b77: 4c 90 89    L..            ; Return via restore_args path

; &8b7a referenced 1 time by &8b0d
.gbpb8_read_dir
    ldy #9                                                            ; 8b7a: a0 09       ..             ; OSGBPB 8: read filenames from dir
    lda (fs_options),y                                                ; 8b7c: b1 bb       ..             ; Byte 9: number of entries to read
    sta fs_func_code                                                  ; 8b7e: 8d 06 0f    ...            ; Store as reply count in command buffer
    ldy #5                                                            ; 8b81: a0 05       ..             ; Y=5: byte 5 = starting entry number
    lda (fs_options),y                                                ; 8b83: b1 bb       ..             ; Load starting entry number
    sta fs_data_count                                                 ; 8b85: 8d 07 0f    ...            ; Store in command buffer
    ldx #&0d                                                          ; 8b88: a2 0d       ..             ; X=&0D: command data extent; X=preserved through header build
    stx fs_reply_cmd                                                  ; 8b8a: 8e 08 0f    ...            ; Store extent in command buffer
    ldy #2                                                            ; 8b8d: a0 02       ..             ; Y=2: function code for dir read
    sty fs_load_addr                                                  ; 8b8f: 84 b0       ..             ; Store 2 as reply data start offset
    sty fs_cmd_data                                                   ; 8b91: 8c 05 0f    ...            ; Store 2 as command data byte
    iny                                                               ; 8b94: c8          .              ; Y=3: function code for header read; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8b95: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8b98: 86 b1       ..             ; X=0 after FS command completes; X=0 on success, &D6 on not-found
    lda fs_func_code                                                  ; 8b9a: ad 06 0f    ...            ; Load reply entry count
    sta (fs_options,x)                                                ; 8b9d: 81 bb       ..             ; Store at param block byte 0 (X=0)
    lda fs_cmd_data                                                   ; 8b9f: ad 05 0f    ...            ; Load entries-read count from reply
    ldy #9                                                            ; 8ba2: a0 09       ..             ; Y=9: param block byte 9
    adc (fs_options),y                                                ; 8ba4: 71 bb       q.             ; Add to starting entry number
    sta (fs_options),y                                                ; 8ba6: 91 bb       ..             ; Update param block with new position
    lda txcb_end                                                      ; 8ba8: a5 c8       ..             ; Load total reply length
    sbc #7                                                            ; 8baa: e9 07       ..             ; Subtract header (7 bytes) from reply len
    sta fs_func_code                                                  ; 8bac: 8d 06 0f    ...            ; Store adjusted length in command buffer
    sta fs_load_addr_2                                                ; 8baf: 85 b2       ..             ; Store as byte count for copy loop
    beq skip_copy_reply                                               ; 8bb1: f0 03       ..             ; Zero bytes: skip copy
    jsr copy_reply_to_caller                                          ; 8bb3: 20 3b 8b     ;.            ; Copy reply data to caller's buffer
; &8bb6 referenced 1 time by &8bb1
.skip_copy_reply
    ldx #2                                                            ; 8bb6: a2 02       ..             ; X=2: clear 3 bytes
; &8bb8 referenced 1 time by &8bbc
.zero_cmd_bytes
    sta fs_data_count,x                                               ; 8bb8: 9d 07 0f    ...            ; Zero out &0F07+X area
    dex                                                               ; 8bbb: ca          .              ; Next byte
    bpl zero_cmd_bytes                                                ; 8bbc: 10 fa       ..             ; Loop for X=2,1,0
    jsr adjust_addrs_1                                                ; 8bbe: 20 13 8a     ..            ; Adjust pointer by +1 (one filename read)
    sec                                                               ; 8bc1: 38          8              ; SEC for reverse adjustment
    dec fs_load_addr_2                                                ; 8bc2: c6 b2       ..             ; Reverse adjustment for updated counter
    lda fs_cmd_data                                                   ; 8bc4: ad 05 0f    ...            ; Load entries-read count
    sta fs_func_code                                                  ; 8bc7: 8d 06 0f    ...            ; Store in command buffer
    jsr adjust_addrs                                                  ; 8bca: 20 16 8a     ..            ; Adjust param block addresses
    beq gbpb_done                                                     ; 8bcd: f0 a8       ..             ; Z=1: all done, exit
; &8bcf referenced 3 times by &8b50, &8bd4, &8e10
.tube_claim_loop
    lda #&c3                                                          ; 8bcf: a9 c3       ..             ; A=&C3: Tube claim with retry
    jsr tube_addr_claim                                               ; 8bd1: 20 06 04     ..            ; Request Tube address claim
    bcc tube_claim_loop                                               ; 8bd4: 90 f9       ..             ; C=0: claim failed, retry
    rts                                                               ; 8bd6: 60          `              ; Tube claimed successfully

; ***************************************************************************************
; FSCV 2/3/4: unrecognised * command handler (DECODE)
; 
; CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text
; against the table
; at &8C05 using case-insensitive comparison with abbreviation
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
.fscv_3_star_cmd
    jsr save_fscv_args_with_ptrs                                      ; 8bd7: 20 c8 85     ..            ; Save A/X/Y and set up command ptr
    ldx #&ff                                                          ; 8bda: a2 ff       ..             ; X=&FF: table index (pre-incremented)
    stx fs_crflag                                                     ; 8bdc: 86 b9       ..             ; Disable column formatting
; &8bde referenced 1 time by &8bf9
.scan_cmd_table
    ldy #&ff                                                          ; 8bde: a0 ff       ..             ; Y=&FF: input index (pre-incremented)
; &8be0 referenced 1 time by &8beb
.decfir
    iny                                                               ; 8be0: c8          .              ; Advance input pointer
    inx                                                               ; 8be1: e8          .              ; Advance table pointer
; &8be2 referenced 1 time by &8bfd
.decmor
    lda fs_cmd_match_table,x                                          ; 8be2: bd 05 8c    ...            ; Load table character
    bmi dispatch_cmd                                                  ; 8be5: 30 18       0.             ; Bit 7: end of name, dispatch
    eor (fs_crc_lo),y                                                 ; 8be7: 51 be       Q.             ; XOR input char with table char
    and #&df                                                          ; 8be9: 29 df       ).             ; Case-insensitive (clear bit 5)
    beq decfir                                                        ; 8beb: f0 f3       ..             ; Match: continue comparing
    dex                                                               ; 8bed: ca          .              ; Mismatch: back up table pointer
; &8bee referenced 1 time by &8bf2
.decmin
    inx                                                               ; 8bee: e8          .              ; Skip to end of table entry
    lda fs_cmd_match_table,x                                          ; 8bef: bd 05 8c    ...            ; Load table byte
    bpl decmin                                                        ; 8bf2: 10 fa       ..             ; Loop until bit 7 set (end marker)
    lda (fs_crc_lo),y                                                 ; 8bf4: b1 be       ..             ; Check input for '.' abbreviation
    inx                                                               ; 8bf6: e8          .              ; Skip past handler high byte
    cmp #&2e ; '.'                                                    ; 8bf7: c9 2e       ..             ; Is input '.' (abbreviation)?
    bne scan_cmd_table                                                ; 8bf9: d0 e3       ..             ; No: try next table entry
    iny                                                               ; 8bfb: c8          .              ; Yes: skip '.' in input
    dex                                                               ; 8bfc: ca          .              ; Back to handler high byte
    bcs decmor                                                        ; 8bfd: b0 e3       ..             ; ALWAYS branch; dispatch via BMI
; &8bff referenced 1 time by &8be5
.dispatch_cmd
    pha                                                               ; 8bff: 48          H              ; Push handler address high byte
    lda fs_cmd_dispatch_hi,x                                          ; 8c00: bd 06 8c    ...            ; Load handler address low byte
    pha                                                               ; 8c03: 48          H              ; Push handler address low byte
    rts                                                               ; 8c04: 60          `              ; Dispatch via RTS (addr-1 on stack)

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
;   "EX"     → &8C1B (ex_handler: embedded in table tail)
;   "BYE"\r  → &83BC (bye_handler: logoff)
;   <catch-all> → &80C1 (forward anything else to FS)
; ***************************************************************************************
; &8c05 referenced 2 times by &8be2, &8bef
.fs_cmd_match_table
fs_cmd_dispatch_hi = fs_cmd_match_table+1
    eor #&2e ; '.'                                                    ; 8c05: 49 2e       I.             ; Match last char against '.' for *I. abbreviation
; &8c06 referenced 1 time by &8c00
    equb &80, &c0                                                     ; 8c07: 80 c0       ..
    equs "I AM"                                                       ; 8c09: 49 20 41... I A
    equb &80, &81, &45, &58, &8c, &1a                                 ; 8c0d: 80 81 45... ..E
    equs "BYE"                                                        ; 8c13: 42 59 45    BYE
    equb &0d, &83, &bb, &80, &c0                                      ; 8c16: 0d 83 bb... ...

.ex_handler
    ldx #1                                                            ; 8c1b: a2 01       ..             ; X=1: *EX single-entry examine
    lda #3                                                            ; 8c1d: a9 03       ..             ; A=3: column count for *EX mode
    bne init_cat_params                                               ; 8c1f: d0 08       ..             ; ALWAYS branch

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
    ldx #3                                                            ; 8c21: a2 03       ..             ; X=3: column count for multi-column layout
    stx fs_crflag                                                     ; 8c23: 86 b9       ..             ; CRFLAG=3: first entry will trigger newline
    ldy #0                                                            ; 8c25: a0 00       ..             ; Y=&FF: mark as escapable
    lda #&0b                                                          ; 8c27: a9 0b       ..             ; A=&0B: examine argument count
; &8c29 referenced 1 time by &8c1f
.init_cat_params
    sta fs_work_5                                                     ; 8c29: 85 b5       ..             ; Store examine argument count
    stx fs_work_7                                                     ; 8c2b: 86 b7       ..             ; Store column count
    lda #6                                                            ; 8c2d: a9 06       ..             ; A=6: examine format type in command
    sta fs_cmd_data                                                   ; 8c2f: 8d 05 0f    ...            ; Store format type at &0F05
    jsr parse_filename_gs_y                                           ; 8c32: 20 e3 86     ..            ; Set up command parameter pointers
    ldx #1                                                            ; 8c35: a2 01       ..             ; X=1: copy dir name at cmd offset 1
    jsr copy_string_to_cmd                                            ; 8c37: 20 77 8d     w.            ; Copy directory name to command buffer
    ldy #&12                                                          ; 8c3a: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c3c: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c3f: a2 03       ..             ; X=3: start printing from reply offset 3
    jsr print_reply_bytes                                             ; 8c41: 20 fb 8c     ..            ; Print directory title (10 chars)
    jsr print_inline                                                  ; 8c44: 20 05 86     ..            ; Print '('
    equs "("                                                          ; 8c47: 28          (

    lda fs_reply_stn                                                  ; 8c48: ad 13 0f    ...            ; Load station number from FS reply
    jsr print_decimal                                                 ; 8c4b: 20 b0 8d     ..            ; Print station number as decimal
    jsr print_inline                                                  ; 8c4e: 20 05 86     ..            ; Print ')     '
    equs ")     "                                                     ; 8c51: 29 20 20... )

    ldx fs_access_level                                               ; 8c57: ae 12 0f    ...            ; Load access level from reply
    bne print_public                                                  ; 8c5a: d0 0b       ..             ; Non-zero: Public access
    jsr print_inline                                                  ; 8c5c: 20 05 86     ..            ; Print 'Owner' + CR
    equs "Owner", &0d                                                 ; 8c5f: 4f 77 6e... Own

    bne cat_check_access                                              ; 8c65: d0 0a       ..             ; ALWAYS branch past 'Owner'
; &8c67 referenced 1 time by &8c5a
.print_public
    jsr print_inline                                                  ; 8c67: 20 05 86     ..            ; Print 'Public' + CR
    equs "Public", &0d                                                ; 8c6a: 50 75 62... Pub

; &8c71 referenced 1 time by &8c65
.cat_check_access
    ldy #&15                                                          ; 8c71: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c73: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8c76: e8          .              ; X=1: past command code byte
    ldy #&10                                                          ; 8c77: a0 10       ..             ; Y=&10: print 16 characters
    jsr print_reply_counted                                           ; 8c79: 20 fd 8c     ..            ; Print disc/CSD name from reply
    jsr print_inline                                                  ; 8c7c: 20 05 86     ..            ; Print '    Option '
    equs "    Option "                                                ; 8c7f: 20 20 20...

    lda fs_boot_option                                                ; 8c8a: ad 05 0e    ...            ; Load boot option from reply
    tax                                                               ; 8c8d: aa          .              ; X = boot option for name table lookup
    jsr print_hex                                                     ; 8c8e: 20 e0 9f     ..            ; Print boot option as hex digit
    jsr print_inline                                                  ; 8c91: 20 05 86     ..            ; Print ' ('
    equs " ("                                                         ; 8c94: 20 28        (

    ldy boot_option_text,x                                            ; 8c96: bc 08 8d    ...            ; Y=string offset for this option
; &8c99 referenced 1 time by &8ca2
.cattxt
    lda boot_option_text,y                                            ; 8c99: b9 08 8d    ...            ; Load next char of option name
    bmi done_option_name                                              ; 8c9c: 30 06       0.             ; Bit 7 set: end of option name
    jsr osasci                                                        ; 8c9e: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8ca1: c8          .              ; Next character
    bne cattxt                                                        ; 8ca2: d0 f5       ..             ; Continue printing option name
; &8ca4 referenced 1 time by &8c9c
.done_option_name
    jsr print_inline                                                  ; 8ca4: 20 05 86     ..            ; Print ')' + CR + 'Dir. '
    equs ")", &0d, "Dir. "                                            ; 8ca7: 29 0d 44... ).D

    ldx #&11                                                          ; 8cae: a2 11       ..             ; X=&11: Dir. name offset in reply
    jsr print_reply_bytes                                             ; 8cb0: 20 fb 8c     ..            ; Print directory name (10 chars)
    jsr print_inline                                                  ; 8cb3: 20 05 86     ..            ; Print '     Lib. ' header
    equs "     Lib. "                                                 ; 8cb6: 20 20 20...

    ldx #&1b                                                          ; 8cc0: a2 1b       ..             ; X=&1B: Lib. name offset in reply
    jsr print_reply_bytes                                             ; 8cc2: 20 fb 8c     ..            ; Print library name
    jsr osnewl                                                        ; 8cc5: 20 e7 ff     ..            ; Print two CRs (blank line); Write newline (characters 10 and 13)
; &8cc8 referenced 1 time by &8cf9
.fetch_dir_batch
    sty fs_func_code                                                  ; 8cc8: 8c 06 0f    ...            ; Store entry start offset for request
    sty fs_work_4                                                     ; 8ccb: 84 b4       ..             ; Save start offset in zero page for loop
    ldx fs_work_5                                                     ; 8ccd: a6 b5       ..             ; Load examine arg count for batch size
    stx fs_data_count                                                 ; 8ccf: 8e 07 0f    ...            ; Store as request count at &0F07
.cat_examine_loop
    ldx fs_work_7                                                     ; 8cd2: a6 b7       ..             ; Load column count for display format
    stx fs_cmd_data                                                   ; 8cd4: 8e 05 0f    ...            ; Store column count in command data
    ldx #3                                                            ; 8cd7: a2 03       ..             ; X=3: copy directory name at offset 3
    jsr copy_string_to_cmd                                            ; 8cd9: 20 77 8d     w.            ; Append directory name to examine command
    ldy #3                                                            ; 8cdc: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cde: 20 c3 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8ce1: e8          .              ; X past command code byte in reply
    lda fs_cmd_data                                                   ; 8ce2: ad 05 0f    ...            ; Load entry count from reply
    beq print_newline                                                 ; 8ce5: f0 6e       .n             ; Zero entries: catalogue complete
.process_entries
    pha                                                               ; 8ce7: 48          H              ; Save entry count for batch processing
; &8ce8 referenced 1 time by &8cec
.scan_entry_terminator
    iny                                                               ; 8ce8: c8          .              ; Advance Y past entry data bytes
    lda fs_cmd_data,y                                                 ; 8ce9: b9 05 0f    ...            ; Read entry byte from reply buffer
    bpl scan_entry_terminator                                         ; 8cec: 10 fa       ..             ; Loop until high-bit terminator found
    sta fs_cmd_lib,y                                                  ; 8cee: 99 04 0f    ...            ; Store terminator as print boundary
    jsr cat_column_separator                                          ; 8cf1: 20 92 8d     ..            ; Print/format this directory entry
    pla                                                               ; 8cf4: 68          h              ; Restore entry count from stack
    clc                                                               ; 8cf5: 18          .              ; CLC for addition
    adc fs_work_4                                                     ; 8cf6: 65 b4       e.             ; Advance start offset by entry count
    tay                                                               ; 8cf8: a8          .              ; Y = new entry start offset
    bne fetch_dir_batch                                               ; 8cf9: d0 cd       ..             ; More entries: fetch next batch
; &8cfb referenced 3 times by &8c41, &8cb0, &8cc2
.print_reply_bytes
    ldy #&0a                                                          ; 8cfb: a0 0a       ..             ; Y=&0A: default print 10 characters
; &8cfd referenced 2 times by &8c79, &8d05
.print_reply_counted
    lda fs_cmd_data,x                                                 ; 8cfd: bd 05 0f    ...            ; Load reply byte at offset X
    jsr osasci                                                        ; 8d00: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8d03: e8          .              ; Next reply byte
    dey                                                               ; 8d04: 88          .              ; Decrement character count
    bne print_reply_counted                                           ; 8d05: d0 f6       ..             ; Loop for remaining characters
; Option name encoding: the boot option names ("Off",
; "Load", "Run", "Exec") are scattered through the code rather
; than stored as a contiguous table. They are addressed via
; base+offset from return_9 (&8CE0), whose first four bytes
; (starting with the RTS opcode &60) double as the offset table:
;   &60→&8D40 "Off", &73→&8D53 "Load",
;   &9B→&8D7B "Run", &18→&8CF8 "Exec"
; Each string is terminated by the next instruction's opcode
; having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).
.return_9
    rts                                                               ; 8d07: 60          `              ; Return from column separator

; &8d08 referenced 2 times by &8c96, &8c99
.boot_option_text
    equb &6a, &7d, &a5, &18                                           ; 8d08: 6a 7d a5... j}.
    equs "L.!"                                                        ; 8d0c: 4c 2e 21    L.!
; ***************************************************************************************
; Boot command strings for auto-boot
; 
; The four boot options use OSCLI strings at offsets within page &8D.
; The offset table at boot_option_offsets+1 (&8D1C) is indexed by
; the boot option value (0-3); each byte is the low byte of the
; string address, with the page high byte &8D loaded separately:
;   Option 0 (Off):  offset &1B → &8D1B = bare CR (empty command)
;   Option 1 (Load): offset &0C → &8D0C = "L.!BOOT" (the bytes
;       &4C='L', &2E='.', &21='!' precede "BOOT" + CR at &8D0F)
;   Option 2 (Run):  offset &0E → &8D0E = "!BOOT" (bare filename = *RUN)
;   Option 3 (Exec): offset &14 → &8D14 = "E.!BOOT"
; 
; This is a classic BBC ROM space optimisation: the string data
; overlaps with other byte sequences to save space. The &0D byte
; at &8D1B terminates "E.!BOOT" AND doubles as the bare-CR
; command for boot option 0.
; ***************************************************************************************
.boot_cmd_strings
    equs "BOOT"                                                       ; 8d0f: 42 4f 4f... BOO
    equb &0d                                                          ; 8d13: 0d          .
    equs "E.!BOOT"                                                    ; 8d14: 45 2e 21... E.!
; ***************************************************************************************
; Boot option → OSCLI string offset table
; 
; Five bytes: the first byte (&0D) is the bare-CR target for boot
; option 0; bytes 1-4 are the offset table indexed by boot option
; (0-3). Each offset is the low byte of a pointer into page &8D.
; The code reads from boot_option_offsets+1 (&8D1C) via
; LDX l8d1c,Y with Y=boot_option, then LDY #&8D, JMP oscli.
; See boot_cmd_strings for the target strings.
; ***************************************************************************************
.boot_option_offsets
    equb &0d                                                          ; 8d1b: 0d          .
; &8d1c referenced 1 time by &8e3d
.boot_oscli_offset
    equb &1b                                                          ; 8d1c: 1b          .
    equb &0c                                                          ; 8d1d: 0c          .
    equb &0e                                                          ; 8d1e: 0e          .
    equb &14                                                          ; 8d1f: 14          .
    equb &45                                                          ; 8d20: 45          E

    sei                                                               ; 8d21: 78          x              ; Data byte: boot_cmd_strings 'x'
    adc l0063                                                         ; 8d22: 65 63       ec             ; Data bytes: boot_cmd_strings 'ec'
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
    ldy fs_messages_flag                                              ; 8d24: ac 06 0e    ...            ; Check if messages enabled
    beq return_5                                                      ; 8d27: f0 5b       .[             ; Zero: no info to display, return
    ldy #0                                                            ; 8d29: a0 00       ..             ; Y=0: start of filename
    ldx fs_cmd_csd                                                    ; 8d2b: ae 03 0f    ...            ; Load current directory prefix flag
    beq next_filename_char                                            ; 8d2e: f0 05       ..             ; No prefix: skip directory display
    jsr print_dir_from_offset                                         ; 8d30: 20 8b 8d     ..            ; Print directory name prefix
    bmi print_hex_fields                                              ; 8d33: 30 18       0.             ; N=1: skip to hex fields after dir
; &8d35 referenced 2 times by &8d2e, &8d43
.next_filename_char
    lda (fs_crc_lo),y                                                 ; 8d35: b1 be       ..             ; Load next filename character
    cmp #&0d                                                          ; 8d37: c9 0d       ..             ; CR: end of filename
    beq pad_filename_spaces                                           ; 8d39: f0 0a       ..             ; CR found: pad remaining with spaces
    cmp #&20 ; ' '                                                    ; 8d3b: c9 20       .              ; Space: end of name field
    beq pad_filename_spaces                                           ; 8d3d: f0 06       ..             ; Space found: pad with spaces
    jsr osasci                                                        ; 8d3f: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8d42: c8          .              ; Advance to next character
    bne next_filename_char                                            ; 8d43: d0 f0       ..             ; Continue printing filename
; &8d45 referenced 3 times by &8d39, &8d3d, &8d4b
.pad_filename_spaces
    jsr print_space                                                   ; 8d45: 20 6e 8d     n.            ; Print space for padding
    iny                                                               ; 8d48: c8          .              ; Advance column counter
    cpy #&0c                                                          ; 8d49: c0 0c       ..             ; Reached 12 columns?
    bcc pad_filename_spaces                                           ; 8d4b: 90 f8       ..             ; No: continue padding
; &8d4d referenced 1 time by &8d33
.print_hex_fields
    ldy #5                                                            ; 8d4d: a0 05       ..             ; Y=5: load address offset (4 bytes)
    jsr print_hex_bytes                                               ; 8d4f: 20 63 8d     c.            ; Print load address
    jsr print_exec_and_len                                            ; 8d52: 20 58 8d     X.            ; Print exec address and file length
; &8d55 referenced 1 time by &8ce5
.print_newline
    jmp osnewl                                                        ; 8d55: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &8d58 referenced 1 time by &8d52
.print_exec_and_len
    ldy #9                                                            ; 8d58: a0 09       ..             ; Y=9: exec address offset (4 bytes)
    jsr print_hex_bytes                                               ; 8d5a: 20 63 8d     c.            ; Print exec address
    ldy #&0c                                                          ; 8d5d: a0 0c       ..             ; Y=&0C: file length offset
    ldx #3                                                            ; 8d5f: a2 03       ..             ; X=3: print 3 bytes (24-bit length)
    bne num01                                                         ; 8d61: d0 02       ..             ; ALWAYS branch

; &8d63 referenced 2 times by &8d4f, &8d5a
.print_hex_bytes
    ldx #4                                                            ; 8d63: a2 04       ..             ; X=4: print 4 hex bytes
; &8d65 referenced 2 times by &8d61, &8d6c
.num01
    lda (fs_options),y                                                ; 8d65: b1 bb       ..             ; Load byte from parameter block
    jsr print_hex                                                     ; 8d67: 20 e0 9f     ..            ; Print as two hex digits
    dey                                                               ; 8d6a: 88          .              ; Next byte (descending)
    dex                                                               ; 8d6b: ca          .              ; Count down
    bne num01                                                         ; 8d6c: d0 f7       ..             ; Loop until 4 bytes printed
; &8d6e referenced 1 time by &8d45
.print_space
    lda #&20 ; ' '                                                    ; 8d6e: a9 20       .              ; A=space character
    bne print_digit                                                   ; 8d70: d0 5a       .Z             ; ALWAYS branch

    equs "Off"                                                        ; 8d72: 4f 66 66    Off

; ***************************************************************************************
; Copy filename to FS command buffer
; 
; Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; ***************************************************************************************
; &8d75 referenced 5 times by &809d, &80c1, &8716, &88d3, &8dd2
.infol2
.copy_filename
    ldx #0                                                            ; 8d75: a2 00       ..             ; Start writing at &0F05 (after cmd header)
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
    ldy #0                                                            ; 8d77: a0 00       ..             ; Start copying from offset 0; Start source offset at 0
; &8d79 referenced 1 time by &8d82
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d79: b1 be       ..             ; Load next byte from source string; Load byte from source string
    sta fs_cmd_data,x                                                 ; 8d7b: 9d 05 0f    ...            ; Store to command buffer; Store to FS command buffer (&0F05+X)
    inx                                                               ; 8d7e: e8          .              ; Advance write position; Advance dest pointer
    iny                                                               ; 8d7f: c8          .              ; Advance read position; Advance source pointer
    eor #&0d                                                          ; 8d80: 49 0d       I.             ; XOR with CR: result=0 if byte was CR
    bne copy_string_from_offset                                       ; 8d82: d0 f5       ..             ; Loop until CR copied
; &8d84 referenced 2 times by &8d27, &8d8e
.return_5
    rts                                                               ; 8d84: 60          `              ; Return; X = next free position in buffer

    equs "Load"                                                       ; 8d85: 4c 6f 61... Loa

; ***************************************************************************************
; Print directory name from reply buffer
; 
; Prints characters from the FS reply buffer (&0F05+X onwards).
; Null bytes (&00) are replaced with CR (&0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by fscv_5_cat to display Dir. and Lib. paths.
; ***************************************************************************************
.fsreply_0_print_dir
    ldx #0                                                            ; 8d89: a2 00       ..             ; X=0: start from first reply byte
; &8d8b referenced 2 times by &8d30, &8dab
.print_dir_from_offset
    lda fs_cmd_data,x                                                 ; 8d8b: bd 05 0f    ...            ; Load byte from FS reply buffer
    bmi return_5                                                      ; 8d8e: 30 f4       0.             ; Bit 7 set: end of string, return
    bne dir_print_char                                                ; 8d90: d0 15       ..             ; Non-zero: print character
; ***************************************************************************************
; Print catalogue column separator or newline
; 
; Handles column formatting for *CAT display. On a null byte
; separator, advances the column counter modulo 4: prints a
; 2-space separator between columns, or a CR at column 0.
; Called from fsreply_0_print_dir.
; ***************************************************************************************
; &8d92 referenced 1 time by &8cf1
.cat_column_separator
    ldy fs_crflag                                                     ; 8d92: a4 b9       ..             ; Null byte: check column counter
    bmi dir_column_check                                              ; 8d94: 30 0f       0.             ; Negative: print CR (no columns)
    iny                                                               ; 8d96: c8          .              ; Advance column counter
    tya                                                               ; 8d97: 98          .              ; Transfer to A for modulo
    and #3                                                            ; 8d98: 29 03       ).             ; Modulo 4 columns
    sta fs_crflag                                                     ; 8d9a: 85 b9       ..             ; Update column counter
    beq dir_column_check                                              ; 8d9c: f0 07       ..             ; Column 0: start new line
    jsr print_inline                                                  ; 8d9e: 20 05 86     ..            ; Print 2-space column separator
    equs "  "                                                         ; 8da1: 20 20

    bne next_dir_entry                                                ; 8da3: d0 05       ..             ; More entries: skip final newline
; &8da5 referenced 2 times by &8d94, &8d9c
.dir_column_check
    lda #&0d                                                          ; 8da5: a9 0d       ..             ; A=CR: print newline separator
; &8da7 referenced 1 time by &8d90
.dir_print_char
    jsr osasci                                                        ; 8da7: 20 e3 ff     ..            ; Write character 13
; &8daa referenced 1 time by &8da3
.next_dir_entry
    inx                                                               ; 8daa: e8          .              ; Next byte in reply buffer
    bne print_dir_from_offset                                         ; 8dab: d0 de       ..             ; Loop until end of buffer
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
    tay                                                               ; 8db0: a8          .              ; Y = value to print
    lda #&64 ; 'd'                                                    ; 8db1: a9 64       .d             ; Divisor = 100 (hundreds digit)
    jsr print_decimal_digit                                           ; 8db3: 20 bd 8d     ..            ; Print hundreds digit
    lda #&0a                                                          ; 8db6: a9 0a       ..             ; Divisor = 10 (tens digit)
    jsr print_decimal_digit                                           ; 8db8: 20 bd 8d     ..            ; Print tens digit
    lda #1                                                            ; 8dbb: a9 01       ..             ; Divisor = 1; fall through to units
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
    sta fs_error_ptr                                                  ; 8dbd: 85 b8       ..             ; Save divisor to workspace
    tya                                                               ; 8dbf: 98          .              ; A = dividend (from Y)
    ldx #&2f ; '/'                                                    ; 8dc0: a2 2f       ./             ; X = &2F = ASCII '0' - 1
    sec                                                               ; 8dc2: 38          8              ; Prepare for subtraction
; &8dc3 referenced 1 time by &8dc6
.divide_subtract
    inx                                                               ; 8dc3: e8          .              ; Count one subtraction (next digit value)
    sbc fs_error_ptr                                                  ; 8dc4: e5 b8       ..             ; A = A - divisor
    bcs divide_subtract                                               ; 8dc6: b0 fb       ..             ; Loop while A >= 0 (borrow clear)
    adc fs_error_ptr                                                  ; 8dc8: 65 b8       e.             ; Undo last subtraction: A = remainder
    tay                                                               ; 8dca: a8          .              ; Y = remainder for caller
    txa                                                               ; 8dcb: 8a          .              ; A = X = ASCII digit character
; &8dcc referenced 1 time by &8d70
.print_digit
    jmp osasci                                                        ; 8dcc: 4c e3 ff    L..            ; Write character

; ***************************************************************************************
; FSCV 2/4: */ (run) and *RUN handler
; 
; Parses the filename via parse_filename_gs and calls infol2,
; then falls through to fsreply_4_notify_exec to set up and
; send the FS load-as-command request.
; ***************************************************************************************
.fscv_2_star_run
    jsr parse_filename_gs                                             ; 8dcf: 20 e1 86     ..            ; Parse filename from command line
    jsr infol2                                                        ; 8dd2: 20 75 8d     u.            ; Copy filename to FS command buffer
; ***************************************************************************************
; FS reply 4: send FS load-as-command and execute response
; 
; Initialises a GS reader to skip past the filename and
; calculate the command context address, then sets up an FS
; command with function code &05 (FCCMND: load as command)
; using send_fs_examine. If a Tube co-processor is present
; (tx_in_progress != 0), transfers the response data to the
; Tube via tube_addr_claim. Otherwise jumps via the indirect
; pointer at (&0F09) to execute at the load address.
; ***************************************************************************************
.fsreply_4_notify_exec
    ldy #0                                                            ; 8dd5: a0 00       ..             ; Y=0: start of text for GSINIT
    clc                                                               ; 8dd7: 18          .              ; CLC before GSINIT call
    jsr gsinit                                                        ; 8dd8: 20 c2 ff     ..            ; GSINIT/GSREAD: skip past the filename
; &8ddb referenced 1 time by &8dde
.skip_gs_filename
    jsr gsread                                                        ; 8ddb: 20 c5 ff     ..            ; Read next filename character
    bcc skip_gs_filename                                              ; 8dde: 90 fb       ..             ; C=0: more characters, keep reading
    jsr skip_spaces                                                   ; 8de0: 20 7a 83     z.            ; Skip spaces after filename
    clc                                                               ; 8de3: 18          .              ; Calculate context addr = text ptr + Y
    tya                                                               ; 8de4: 98          .              ; Y = offset past filename end
    adc os_text_ptr                                                   ; 8de5: 65 f2       e.             ; Add text pointer low byte
    sta fs_cmd_context                                                ; 8de7: 8d 0a 0e    ...            ; Store context address low byte
    lda os_text_ptr_hi                                                ; 8dea: a5 f3       ..             ; Load text pointer high byte
    adc #0                                                            ; 8dec: 69 00       i.             ; Add carry from low byte addition
    sta fs_context_hi                                                 ; 8dee: 8d 0b 0e    ...            ; Store context address high byte
    ldx #&0e                                                          ; 8df1: a2 0e       ..             ; X=&0E: FS command buffer offset
    stx fs_block_offset                                               ; 8df3: 86 bc       ..             ; Store block offset for FS command
    lda #&10                                                          ; 8df5: a9 10       ..             ; A=&10: 16 bytes of command data
    sta fs_options                                                    ; 8df7: 85 bb       ..             ; Store options byte
    sta fs_work_16                                                    ; 8df9: 8d 16 0e    ...            ; Store to FS workspace
    ldx #&4a ; 'J'                                                    ; 8dfc: a2 4a       .J             ; X=&4A: TXCB size for load command
    ldy #5                                                            ; 8dfe: a0 05       ..             ; Y=5: FCCMND (load as command)
    jsr send_fs_examine                                               ; 8e00: 20 1b 87     ..            ; Send FS examine/load command
    lda tube_flag                                                     ; 8e03: ad 67 0d    .g.            ; Check for Tube co-processor
    beq exec_at_load_addr                                             ; 8e06: f0 14       ..             ; No Tube: execute locally
    adc fs_load_upper                                                 ; 8e08: 6d 0b 0f    m..            ; Check load address upper bytes
    adc fs_addr_check                                                 ; 8e0b: 6d 0c 0f    m..            ; Continue address range check
    bcs exec_at_load_addr                                             ; 8e0e: b0 0c       ..             ; Carry set: not Tube space, exec locally
    jsr tube_claim_loop                                               ; 8e10: 20 cf 8b     ..            ; Claim Tube transfer channel
    ldx #9                                                            ; 8e13: a2 09       ..             ; X=9: source offset in FS reply
    ldy #&0f                                                          ; 8e15: a0 0f       ..             ; Y=&0F: page &0F (FS command buffer)
    lda #4                                                            ; 8e17: a9 04       ..             ; A=4: Tube transfer type 4 (256-byte)
    jmp tube_addr_claim                                               ; 8e19: 4c 06 04    L..            ; Transfer data to Tube co-processor

; &8e1c referenced 2 times by &8e06, &8e0e
.exec_at_load_addr
    jmp (fs_load_vector)                                              ; 8e1c: 6c 09 0f    l..            ; Execute at load address via indirect JMP

; ***************************************************************************************
; Set library handle
; 
; Stores Y into &0E04 (library directory handle in FS workspace).
; Falls through to JMP restore_args_return if Y is non-zero.
; ***************************************************************************************
.fsreply_5_set_lib
    sty fs_lib_handle                                                 ; 8e1f: 8c 04 0e    ...            ; Save library handle from FS reply
    bcc jmp_restore_args                                              ; 8e22: 90 03       ..             ; SDISC path: skip CSD, jump to return
; ***************************************************************************************
; Set CSD handle
; 
; Stores Y into &0E03 (current selected directory handle).
; Falls through to JMP restore_args_return.
; ***************************************************************************************
.fsreply_3_set_csd
    sty fs_csd_handle                                                 ; 8e24: 8c 03 0e    ...            ; Store CSD handle from FS reply
; &8e27 referenced 2 times by &8e22, &8e38
.jmp_restore_args
    jmp restore_args_return                                           ; 8e27: 4c 6f 89    Lo.            ; Restore A/X/Y and return to caller

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
    sec                                                               ; 8e2a: 38          8              ; Set carry: LOGIN path (copy + boot)
; ***************************************************************************************
; Copy FS reply handles to workspace (no boot)
; 
; CLC entry (SDISC): copies handles only, then jumps to
; restore_args_return via c8e27. Called when the FS reply contains
; updated handle values but no boot action is needed.
; ***************************************************************************************
.fsreply_2_copy_handles
    ldx #3                                                            ; 8e2b: a2 03       ..             ; Copy 4 bytes: boot option + 3 handles
    bcc copy_handles_loop                                             ; 8e2d: 90 06       ..             ; SDISC: skip boot option, copy handles only
; &8e2f referenced 1 time by &8e36
.logon2
    lda fs_cmd_data,x                                                 ; 8e2f: bd 05 0f    ...            ; Load from FS reply (&0F05+X)
    sta fs_urd_handle,x                                               ; 8e32: 9d 02 0e    ...            ; Store to handle workspace (&0E02+X)
; &8e35 referenced 1 time by &8e2d
.copy_handles_loop
    dex                                                               ; 8e35: ca          .              ; Next handle (descending)
    bpl logon2                                                        ; 8e36: 10 f7       ..             ; Loop while X >= 0
    bcc jmp_restore_args                                              ; 8e38: 90 ed       ..             ; SDISC: done, restore args and return
; ***************************************************************************************
; Execute boot command via OSCLI
; 
; Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
; path). Reads the boot option from fs_boot_option (&0E05),
; looks up the OSCLI command string offset from boot_option_offsets+1,
; and executes the boot command via JMP oscli with page &8D.
; ***************************************************************************************
.boot_cmd_execute
    ldy fs_boot_option                                                ; 8e3a: ac 05 0e    ...            ; Y = boot option from FS workspace
    ldx boot_oscli_offset,y                                           ; 8e3d: be 1c 8d    ...            ; X = command string offset from table
    ldy #&8d                                                          ; 8e40: a0 8d       ..             ; Y = &8D (high byte of command address)
    jmp oscli                                                         ; 8e42: 4c f7 ff    L..            ; Execute boot command string via OSCLI

; ***************************************************************************************
; Load handle from &F0 and calculate workspace offset
; 
; Loads the file handle byte from &F0, then falls through to
; calc_handle_offset which converts handle * 12 to a workspace
; byte offset. Validates offset < &48.
; ***************************************************************************************
; &8e45 referenced 2 times by &8e5f, &8e6f
.load_handle_calc_offset
    lda osword_pb_ptr                                                 ; 8e45: a5 f0       ..             ; Load handle from &F0
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
    asl a                                                             ; 8e47: 0a          .              ; A = handle * 2
    asl a                                                             ; 8e48: 0a          .              ; A = handle * 4
    pha                                                               ; 8e49: 48          H              ; Push handle*4 onto stack
    asl a                                                             ; 8e4a: 0a          .              ; A = handle * 8
    tsx                                                               ; 8e4b: ba          .              ; X = stack pointer
    adc l0101,x                                                       ; 8e4c: 7d 01 01    }..            ; A = handle*8 + handle*4 = handle*12
    tay                                                               ; 8e4f: a8          .              ; Y = offset into handle workspace
    pla                                                               ; 8e50: 68          h              ; Clean up stack (discard handle*4)
    cmp #&48 ; 'H'                                                    ; 8e51: c9 48       .H             ; Offset >= &48? (6 handles max)
    bcc return_6                                                      ; 8e53: 90 03       ..             ; Valid: return with C clear
    ldy #0                                                            ; 8e55: a0 00       ..             ; Invalid: Y = 0
    tya                                                               ; 8e57: 98          .              ; A = 0, C set (error); A=0, C set = error indicator; A=&00
; &8e58 referenced 1 time by &8e53
.return_6
.return_calc_handle
    rts                                                               ; 8e58: 60          `              ; Return after calculation

; *NET1: read file handle from received packet.
; Reads a byte from offset &6F of the RX buffer (net_rx_ptr)
; and falls through to net_2_read_handle_entry's common path.
.net_1_read_handle
    ldy #&6f ; 'o'                                                    ; 8e59: a0 6f       .o             ; Y=&6F: RX buffer handle offset
    lda (net_rx_ptr),y                                                ; 8e5b: b1 9c       ..             ; Read handle from RX packet
    bcc store_handle_return                                           ; 8e5d: 90 0d       ..             ; Valid handle: store and return
; ***************************************************************************************
; *NET2: read handle entry from workspace
; 
; Looks up the handle in &F0 via calc_handle_offset. If the
; workspace slot contains &3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears rom_svc_num on exit.
; ***************************************************************************************
.net_2_read_handle_entry
    jsr load_handle_calc_offset                                       ; 8e5f: 20 45 8e     E.            ; Look up handle &F0 in workspace
    bcs rxpol2                                                        ; 8e62: b0 06       ..             ; Invalid handle: return 0
    lda (nfs_workspace),y                                             ; 8e64: b1 9e       ..             ; Load stored handle value
    cmp #&3f ; '?'                                                    ; 8e66: c9 3f       .?             ; &3F = unused/closed slot marker
    bne store_handle_return                                           ; 8e68: d0 02       ..             ; Slot in use: return actual value
; &8e6a referenced 2 times by &8e62, &8e72
.rxpol2
    lda #0                                                            ; 8e6a: a9 00       ..             ; Return 0 for closed/invalid handle
; &8e6c referenced 2 times by &8e5d, &8e68
.store_handle_return
    sta osword_pb_ptr                                                 ; 8e6c: 85 f0       ..             ; Store result back to &F0
    rts                                                               ; 8e6e: 60          `              ; Return

; ***************************************************************************************
; *NET3: close handle (mark as unused)
; 
; Looks up the handle in &F0 via calc_handle_offset. Writes
; &3F ('?') to mark the handle slot as closed in the NFS
; workspace. Preserves the carry flag state across the write
; using ROL/ROR on rx_status_flags. Clears rom_svc_num on exit.
; ***************************************************************************************
.net_3_close_handle
    jsr load_handle_calc_offset                                       ; 8e6f: 20 45 8e     E.            ; Look up handle &F0 in workspace
    bcs rxpol2                                                        ; 8e72: b0 f6       ..             ; Invalid handle: return 0
    ror rx_flags                                                      ; 8e74: 6e 64 0d    nd.            ; Save carry via rotate
    lda #&3f ; '?'                                                    ; 8e77: a9 3f       .?             ; A=&3F: handle closed/unused marker
    sta (nfs_workspace),y                                             ; 8e79: 91 9e       ..             ; Write marker to handle slot
    rol rx_flags                                                      ; 8e7b: 2e 64 0d    .d.            ; Restore carry from rotate
    rts                                                               ; 8e7e: 60          `              ; Return

; ***************************************************************************************
; Filing system OSWORD entry
; 
; Subtracts &0F from the command code in &EF, giving a 0-4 index
; for OSWORD calls &0F-&13 (15-19). Falls through to the
; PHA/PHA/RTS dispatch at &8E80.
; ***************************************************************************************
.svc_8_osword
    lda osbyte_a_copy                                                 ; 8e7f: a5 ef       ..             ; Command code from &EF
    sbc #&0f                                                          ; 8e81: e9 0f       ..             ; Subtract &0F: OSWORD &0F-&13 become indices 0-4
    bmi return_7                                                      ; 8e83: 30 2a       0*             ; Outside our OSWORD range, exit
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
    cmp #5                                                            ; 8e85: c9 05       ..             ; Only OSWORDs &0F-&13 (index 0-4)
    bcs return_7                                                      ; 8e87: b0 26       .&             ; Index >= 5: not ours, return
    jsr fs_osword_dispatch                                            ; 8e89: 20 97 8e     ..            ; Dispatch via PHA/PHA/RTS table
    ldy #2                                                            ; 8e8c: a0 02       ..             ; Y=2: restore 3 bytes (&AA-&AC)
; &8e8e referenced 1 time by &8e94
.copy_param_ptr
    lda (net_rx_ptr),y                                                ; 8e8e: b1 9c       ..             ; Load saved param block byte
    sta osword_flag,y                                                 ; 8e90: 99 aa 00    ...            ; Restore to &AA-&AC
    dey                                                               ; 8e93: 88          .              ; Next byte (descending)
    bpl copy_param_ptr                                                ; 8e94: 10 f8       ..             ; Loop for all 3 bytes
    rts                                                               ; 8e96: 60          `              ; Return to service handler

; ***************************************************************************************
; PHA/PHA/RTS dispatch for filing system OSWORDs
; 
; X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
; at &8EB0 (low) / &8EB5 (high).
; ***************************************************************************************
; &8e97 referenced 1 time by &8e89
.fs_osword_dispatch
    tax                                                               ; 8e97: aa          .              ; X = sub-function code for table lookup
    lda fs_osword_tbl_hi,x                                            ; 8e98: bd b5 8e    ...            ; Load handler address high byte from table
    pha                                                               ; 8e9b: 48          H              ; Push high byte for RTS dispatch
    lda osword_handler_lo,x                                           ; 8e9c: bd b0 8e    ...            ; Load handler address low byte from table
.fs_osword_tbl_lo
    pha                                                               ; 8e9f: 48          H              ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
    ldy #2                                                            ; 8ea0: a0 02       ..             ; Y=2: save 3 bytes (&AA-&AC)
; &8ea2 referenced 1 time by &8ea8
.save1
    lda osword_flag,y                                                 ; 8ea2: b9 aa 00    ...            ; Load param block pointer byte
    sta (net_rx_ptr),y                                                ; 8ea5: 91 9c       ..             ; Save to NFS workspace via (net_rx_ptr)
    dey                                                               ; 8ea7: 88          .              ; Next byte (descending)
    bpl save1                                                         ; 8ea8: 10 f8       ..             ; Loop for all 3 bytes
    iny                                                               ; 8eaa: c8          .              ; Y=0 after BPL exit; INY makes Y=1
    lda (osword_pb_ptr),y                                             ; 8eab: b1 f0       ..             ; Read sub-function code from (&F0)+1
    sty svc_state                                                     ; 8ead: 84 a9       ..             ; Store Y=1 to &A9
; &8eaf referenced 2 times by &8e83, &8e87
.return_7
    rts                                                               ; 8eaf: 60          `              ; RTS dispatches to pushed handler address

; &8eb0 referenced 1 time by &8e9c
.osword_handler_lo
    equb <(osword_0f_handler-1)                                       ; 8eb0: b9          .
    equb <(osword_10_handler-1)                                       ; 8eb1: 73          s
    equb <(osword_11_handler-1)                                       ; 8eb2: d3          .
.copyl3
    equb <(rs-1)                                                      ; 8eb3: f8          .
    equb <(econet_tx_rx-1)                                            ; 8eb4: e7          .
; &8eb5 referenced 1 time by &8e98
.fs_osword_tbl_hi
    equb >(osword_0f_handler-1)                                       ; 8eb5: 8e          .              ; Dispatch table: high bytes for OSWORD &0F-&13 handlers
    equb >(osword_10_handler-1)                                       ; 8eb6: 8f          .
    equb >(osword_11_handler-1)                                       ; 8eb7: 8e          .
    equb >(rs-1)                                                      ; 8eb8: 8e          .
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
    asl tx_clear_flag                                                 ; 8eba: 0e 62 0d    .b.            ; Test TX semaphore (bit 7 to C)
    tya                                                               ; 8ebd: 98          .              ; Save Y for return value
    bcc readry                                                        ; 8ebe: 90 34       .4             ; C=0: TX busy, return error
    lda net_rx_ptr_hi                                                 ; 8ec0: a5 9d       ..             ; User TX CB in workspace page (high byte)
    sta ws_ptr_hi                                                     ; 8ec2: 85 ac       ..             ; Set param block high byte
    sta nmi_tx_block_hi                                               ; 8ec4: 85 a1       ..             ; Set LTXCBP high byte for low-level TX
    lda #&6f ; 'o'                                                    ; 8ec6: a9 6f       .o             ; &6F: offset into workspace for user TXCB
    sta ws_ptr_lo                                                     ; 8ec8: 85 ab       ..             ; Set param block low byte
    sta nmi_tx_block                                                  ; 8eca: 85 a0       ..             ; Set LTXCBP low byte for low-level TX
    ldx #&0f                                                          ; 8ecc: a2 0f       ..             ; X=15: copy 16 bytes (OSWORD param block)
    jsr copy_param_workspace                                          ; 8ece: 20 14 8f     ..            ; Copy param block to user TX control block
    jmp trampoline_tx_setup                                           ; 8ed1: 4c 60 96    L`.            ; Start user transmit via BRIANX

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
    lda net_rx_ptr_hi                                                 ; 8ed4: a5 9d       ..             ; Set source high byte from workspace page
    sta ws_ptr_hi                                                     ; 8ed6: 85 ac       ..             ; Store as copy source high byte in &AC
    ldy #&7f                                                          ; 8ed8: a0 7f       ..             ; JSRSIZ at workspace offset &7F
    lda (net_rx_ptr),y                                                ; 8eda: b1 9c       ..             ; Load buffer size from workspace
    iny                                                               ; 8edc: c8          .              ; Y=&80: start of JSR argument data; Y=&80
    sty ws_ptr_lo                                                     ; 8edd: 84 ab       ..             ; Store &80 as copy source low byte
    tax                                                               ; 8edf: aa          .              ; X = buffer size (loop counter)
    dex                                                               ; 8ee0: ca          .              ; X = size-1 (0-based count for copy)
    ldy #0                                                            ; 8ee1: a0 00       ..             ; Y=0: start of destination param block
    jsr copy_param_workspace                                          ; 8ee3: 20 14 8f     ..            ; Copy X+1 bytes from workspace to param
    jmp clear_jsr_protection                                          ; 8ee6: 4c eb 92    L..            ; Clear JSR protection status (CLRJSR)

; &8ee9 referenced 1 time by &8f44
.read_args_size
    ldy #&7f                                                          ; 8ee9: a0 7f       ..             ; Y=&7F: JSRSIZ offset (READRB entry)
    lda (net_rx_ptr),y                                                ; 8eeb: b1 9c       ..             ; Load buffer size from workspace
    ldy #1                                                            ; 8eed: a0 01       ..             ; Y=1: param block offset for size byte
    sta (osword_pb_ptr),y                                             ; 8eef: 91 f0       ..             ; Store buffer size to (&F0)+1
    iny                                                               ; 8ef1: c8          .              ; Y=2: param block offset for args size; Y=&02
    lda #&80                                                          ; 8ef2: a9 80       ..             ; A=&80: argument data starts at offset &80
; &8ef4 referenced 1 time by &8ebe
.readry
    sta (osword_pb_ptr),y                                             ; 8ef4: 91 f0       ..             ; Store args start offset to (&F0)+2
    rts                                                               ; 8ef6: 60          `              ; Return

; &8ef7 referenced 1 time by &8f0b
.osword_12_offsets
    equb &ff, 1                                                       ; 8ef7: ff 01       ..

.rs
    cmp #6                                                            ; 8ef9: c9 06       ..             ; Sub-function >= 6?
    bcs rsl1                                                          ; 8efb: b0 41       .A             ; Yes: jump to sub 6-9 handler
    cmp #4                                                            ; 8efd: c9 04       ..             ; Sub-function >= 4?
    bcs rssl1                                                         ; 8eff: b0 22       ."             ; Sub-function 4 or 5: read/set station
    lsr a                                                             ; 8f01: 4a          J              ; LSR: 0->0, 1->0, 2->1, 3->1
    ldx #&0d                                                          ; 8f02: a2 0d       ..             ; X=&0D: default to static workspace page
    tay                                                               ; 8f04: a8          .              ; Transfer LSR result to Y for indexing
    beq set_workspace_page                                            ; 8f05: f0 02       ..             ; Y=0 (sub 0-1): use page &0D
    ldx nfs_workspace_hi                                              ; 8f07: a6 9f       ..             ; Y=1 (sub 2-3): use dynamic workspace
; &8f09 referenced 1 time by &8f05
.set_workspace_page
    stx ws_ptr_hi                                                     ; 8f09: 86 ac       ..             ; Store workspace page in &AC (hi byte)
    lda osword_12_offsets,y                                           ; 8f0b: b9 f7 8e    ...            ; Load offset: &FF (sub 0-1) or &01 (sub 2-3)
    sta ws_ptr_lo                                                     ; 8f0e: 85 ab       ..             ; Store offset in &AB (lo byte)
    ldx #1                                                            ; 8f10: a2 01       ..             ; X=1: copy 2 bytes
    ldy #1                                                            ; 8f12: a0 01       ..             ; Y=1: start at param block offset 1
; &8f14 referenced 4 times by &8ece, &8ee3, &8f20, &8fb5
.copy_param_workspace
    bcc skip_param_write                                              ; 8f14: 90 04       ..             ; C=0: skip param-to-workspace copy
    lda (osword_pb_ptr),y                                             ; 8f16: b1 f0       ..             ; Load byte from param block; C=1: copy from param to workspace
    sta (ws_ptr_lo),y                                                 ; 8f18: 91 ab       ..             ; Store to workspace; Store param byte to workspace
; &8f1a referenced 1 time by &8f14
.skip_param_write
    lda (ws_ptr_lo),y                                                 ; 8f1a: b1 ab       ..             ; Load byte from workspace; Load workspace byte for return
; ***************************************************************************************
; Bidirectional block copy between OSWORD param block and workspace.
; 
; C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
; C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)
; ***************************************************************************************
.copy_param_block
    sta (osword_pb_ptr),y                                             ; 8f1c: 91 f0       ..             ; Store to param block (no-op if C=1)
    iny                                                               ; 8f1e: c8          .              ; Advance to next byte
    dex                                                               ; 8f1f: ca          .              ; Decrement byte counter; Decrement remaining count
    bpl copy_param_workspace                                          ; 8f20: 10 f2       ..             ; Loop while X >= 0; Loop while bytes remain
.logon3
.return_copy_param
    rts                                                               ; 8f22: 60          `              ; Return

; &8f23 referenced 1 time by &8eff
.rssl1
    lsr a                                                             ; 8f23: 4a          J              ; LSR A: test bit 0 of sub-function
    iny                                                               ; 8f24: c8          .              ; Y=1: offset for protection byte
    lda (osword_pb_ptr),y                                             ; 8f25: b1 f0       ..             ; Load protection byte from param block
    bcs rssl2                                                         ; 8f27: b0 05       ..             ; C=1 (odd sub): set protection
    lda prot_status                                                   ; 8f29: ad 63 0d    .c.            ; C=0 (even sub): read current status
    sta (osword_pb_ptr),y                                             ; 8f2c: 91 f0       ..             ; Return current value to param block
; &8f2e referenced 1 time by &8f27
.rssl2
    sta prot_status                                                   ; 8f2e: 8d 63 0d    .c.            ; Update protection status
    sta saved_jsr_mask                                                ; 8f31: 8d 65 0d    .e.            ; Also save as JSR mask backup
    rts                                                               ; 8f34: 60          `              ; Return

; &8f35 referenced 1 time by &8f40
.read_fs_handle
    ldy #&14                                                          ; 8f35: a0 14       ..             ; Y=&14: RX buffer offset for FS handle
    lda (net_rx_ptr),y                                                ; 8f37: b1 9c       ..             ; Read FS reply handle from RX data
    ldy #1                                                            ; 8f39: a0 01       ..             ; Y=1: param block byte 1
    sta (osword_pb_ptr),y                                             ; 8f3b: 91 f0       ..             ; Return handle to caller's param block
    rts                                                               ; 8f3d: 60          `              ; Return

; &8f3e referenced 1 time by &8efb
.rsl1
    cmp #8                                                            ; 8f3e: c9 08       ..             ; Sub-function 8: read FS handle
    beq read_fs_handle                                                ; 8f40: f0 f3       ..             ; Match: read handle from RX buffer
    cmp #9                                                            ; 8f42: c9 09       ..             ; Sub-function 9: read args size
    beq read_args_size                                                ; 8f44: f0 a3       ..             ; Match: read ARGS buffer info
    bpl return_last_error                                             ; 8f46: 10 19       ..             ; Sub >= 10 (bit 7 clear): read error
    ldy #3                                                            ; 8f48: a0 03       ..             ; Y=3: start from handle 3 (descending)
    lsr a                                                             ; 8f4a: 4a          J              ; LSR: test read/write bit
    bcc readc1                                                        ; 8f4b: 90 1b       ..             ; C=0: read handles from workspace
    sty ws_page                                                       ; 8f4d: 84 a8       ..             ; Init loop counter at Y=3
; &8f4f referenced 1 time by &8f5e
.copy_handles_to_ws
    ldy ws_page                                                       ; 8f4f: a4 a8       ..             ; Reload loop counter
    lda (osword_pb_ptr),y                                             ; 8f51: b1 f0       ..             ; Read handle from caller's param block
    jsr handle_to_mask_a                                              ; 8f53: 20 43 86     C.            ; Convert handle number to bitmask
    tya                                                               ; 8f56: 98          .              ; TYA: get bitmask result
    ldy ws_page                                                       ; 8f57: a4 a8       ..             ; Reload loop counter
    sta fs_server_net,y                                               ; 8f59: 99 01 0e    ...            ; Store bitmask to FS server table
    dec ws_page                                                       ; 8f5c: c6 a8       ..             ; Next handle (descending)
    bne copy_handles_to_ws                                            ; 8f5e: d0 ef       ..             ; Loop for handles 3,2,1
    rts                                                               ; 8f60: 60          `              ; Return

; &8f61 referenced 1 time by &8f46
.return_last_error
    iny                                                               ; 8f61: c8          .              ; Y=1 (post-INY): param block byte 1
    lda fs_last_error                                                 ; 8f62: ad 09 0e    ...            ; Read last FS error code
    sta (osword_pb_ptr),y                                             ; 8f65: 91 f0       ..             ; Return error to caller's param block
    rts                                                               ; 8f67: 60          `              ; Return

; &8f68 referenced 2 times by &8f4b, &8f71
.readc1
    lda fs_server_net,y                                               ; 8f68: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8f6b: 20 60 86     `.            ; Convert bitmask to handle number (FS2A)
    sta (osword_pb_ptr),y                                             ; 8f6e: 91 f0       ..             ; A=handle number (&20-&27); Y=preserved
    dey                                                               ; 8f70: 88          .              ; Next handle (descending)
    bne readc1                                                        ; 8f71: d0 f5       ..             ; Loop for handles 3,2,1
    rts                                                               ; 8f73: 60          `              ; Return

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
    ldx nfs_workspace_hi                                              ; 8f74: a6 9f       ..             ; Workspace page high byte
    stx ws_ptr_hi                                                     ; 8f76: 86 ac       ..             ; Set up pointer high byte in &AC
    sty ws_ptr_lo                                                     ; 8f78: 84 ab       ..             ; Save param block high byte in &AB
    ror rx_flags                                                      ; 8f7a: 6e 64 0d    nd.            ; Disable user RX during CB operation
    lda (osword_pb_ptr),y                                             ; 8f7d: b1 f0       ..             ; Read first byte of param block
    sta osword_flag                                                   ; 8f7f: 85 aa       ..             ; Load from ROM template (zero = use NMI workspace value); Save: 0=open new, non-zero=read RXCB
    bne read_rxcb                                                     ; 8f81: d0 1b       ..             ; Non-zero: read specified RXCB
    lda #3                                                            ; 8f83: a9 03       ..             ; Start scan from RXCB #3 (0-2 reserved)
; &8f85 referenced 1 time by &8f97
.scan0
    jsr calc_handle_offset                                            ; 8f85: 20 47 8e     G.            ; Convert RXCB number to workspace offset
    bcs openl4                                                        ; 8f88: b0 3d       .=             ; Invalid RXCB: return zero
    lsr a                                                             ; 8f8a: 4a          J              ; LSR twice: byte offset / 4
    lsr a                                                             ; 8f8b: 4a          J              ; Yields RXCB number from offset
    tax                                                               ; 8f8c: aa          .              ; X = RXCB number for iteration
    lda (ws_ptr_lo),y                                                 ; 8f8d: b1 ab       ..             ; Read flag byte from RXCB workspace
    beq openl4                                                        ; 8f8f: f0 36       .6             ; Zero = end of CB list
    cmp #&3f ; '?'                                                    ; 8f91: c9 3f       .?             ; &3F = deleted slot, free for reuse
    beq scan1                                                         ; 8f93: f0 04       ..             ; Found free slot
    inx                                                               ; 8f95: e8          .              ; Try next RXCB
    txa                                                               ; 8f96: 8a          .              ; A = next RXCB number
    bne scan0                                                         ; 8f97: d0 ec       ..             ; Continue scan (always branches)
; &8f99 referenced 1 time by &8f93
.scan1
    txa                                                               ; 8f99: 8a          .              ; A = free RXCB number
    ldx #0                                                            ; 8f9a: a2 00       ..             ; X=0 for indexed indirect store
    sta (osword_pb_ptr,x)                                             ; 8f9c: 81 f0       ..             ; Return RXCB number to caller's byte 0
; &8f9e referenced 1 time by &8f81
.read_rxcb
    jsr calc_handle_offset                                            ; 8f9e: 20 47 8e     G.            ; Convert RXCB number to workspace offset
    bcs openl4                                                        ; 8fa1: b0 24       .$             ; Invalid: write zero to param block
    dey                                                               ; 8fa3: 88          .              ; Y = offset-1: points to flag byte
    sty ws_ptr_lo                                                     ; 8fa4: 84 ab       ..             ; Set &AB = workspace ptr low byte
    lda #&c0                                                          ; 8fa6: a9 c0       ..             ; &C0: test mask for flag byte
    ldy #1                                                            ; 8fa8: a0 01       ..             ; Y=1: flag byte offset in RXCB
    ldx #&0b                                                          ; 8faa: a2 0b       ..             ; Enable interrupts before transmit; X=11: copy 12 bytes from RXCB
    cpy osword_flag                                                   ; 8fac: c4 aa       ..             ; Compare Y(1) with saved byte (open/read)
    adc (ws_ptr_lo),y                                                 ; 8fae: 71 ab       q.             ; ADC flag: test if slot is in use
    beq openl6                                                        ; 8fb0: f0 03       ..             ; Dest station = &FFFF (accept reply from any station); Zero: slot open, do copy
    bmi openl7                                                        ; 8fb2: 30 0e       0.             ; Negative: slot has received data
; &8fb4 referenced 1 time by &8fc4
.copy_rxcb_to_param
    clc                                                               ; 8fb4: 18          .              ; C=0: workspace-to-param direction
; &8fb5 referenced 1 time by &8fb0
.openl6
    jsr copy_param_workspace                                          ; 8fb5: 20 14 8f     ..            ; Copy RXCB data to param block
    bcs reenable_rx                                                   ; 8fb8: b0 0f       ..             ; Done: skip deletion on error
    lda #&3f ; '?'                                                    ; 8fba: a9 3f       .?             ; Mark CB as consumed (consume-once)
    ldy #1                                                            ; 8fbc: a0 01       ..             ; Y=1: flag byte offset
    sta (ws_ptr_lo),y                                                 ; 8fbe: 91 ab       ..             ; Write &3F to mark slot deleted
    bne reenable_rx                                                   ; 8fc0: d0 07       ..             ; Branch to exit (always taken); ALWAYS branch

; &8fc2 referenced 1 time by &8fb2
.openl7
    adc #1                                                            ; 8fc2: 69 01       i.             ; Initiate receive with timeout; Advance through multi-byte field
    bne copy_rxcb_to_param                                            ; 8fc4: d0 ee       ..             ; Loop until all bytes processed
    dey                                                               ; 8fc6: 88          .              ; Y=-1 → Y=0 after STA below
; &8fc7 referenced 3 times by &8f88, &8f8f, &8fa1
.openl4
    sta (osword_pb_ptr),y                                             ; 8fc7: 91 f0       ..             ; Return zero (no free RXCB found)
; &8fc9 referenced 2 times by &8fb8, &8fc0
.reenable_rx
    rol rx_flags                                                      ; 8fc9: 2e 64 0d    .d.            ; Re-enable user RX
    rts                                                               ; 8fcc: 60          `              ; Return

; ***************************************************************************************
; Set up RX buffer pointers in NFS workspace
; 
; Calculates the start address of the RX data area (&F0+1) and stores
; it at workspace offset &28. Also reads the data length from (&F0)+1
; and adds it to &F0 to compute the end address at offset &2C.
; ***************************************************************************************
; &8fcd referenced 1 time by &9000
.setup_rx_buffer_ptrs
    ldy #&1c                                                          ; 8fcd: a0 1c       ..             ; Workspace offset &1C = RX data start
    lda osword_pb_ptr                                                 ; 8fcf: a5 f0       ..             ; A = base address low byte
    adc #1                                                            ; 8fd1: 69 01       i.             ; A = base + 1 (skip length byte)
    jsr store_16bit_at_y                                              ; 8fd3: 20 de 8f     ..            ; Receive data blocks until command byte = &00 or &0D; Store 16-bit start addr at ws+&1C/&1D
    ldy #1                                                            ; 8fd6: a0 01       ..             ; Read data length from (&F0)+1
    lda (osword_pb_ptr),y                                             ; 8fd8: b1 f0       ..             ; A = data length byte
    ldy #&20 ; ' '                                                    ; 8fda: a0 20       .              ; Workspace offset &20 = RX data end
    adc osword_pb_ptr                                                 ; 8fdc: 65 f0       e.             ; A = base + length = end address low
; &8fde referenced 1 time by &8fd3
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8fde: 91 9e       ..             ; Store low byte of 16-bit address
    iny                                                               ; 8fe0: c8          .              ; Advance to high byte offset
    lda osword_pb_ptr_hi                                              ; 8fe1: a5 f1       ..             ; A = high byte of base address
    adc #0                                                            ; 8fe3: 69 00       i.             ; Add carry for 16-bit addition
    sta (nfs_workspace),y                                             ; 8fe5: 91 9e       ..             ; Store high byte
    rts                                                               ; 8fe7: 60          `              ; Return

; ***************************************************************************************
; Econet transmit/receive handler
; 
; A=0: Initialise TX control block from ROM template at &8391
;      (zero entries substituted from NMI workspace &0DDA), transmit
;      it, set up RX control block, and receive reply.
; A>=1: Handle transmit result (branch to cleanup at &9034).
; ***************************************************************************************
.econet_tx_rx
    cmp #1                                                            ; 8fe8: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs handle_tx_result                                              ; 8fea: b0 48       .H             ; A >= 1: handle TX result
    ldy #&23 ; '#'                                                    ; 8fec: a0 23       .#             ; Y=&23: start of template (descending)
; &8fee referenced 1 time by &8ffb
.dofs01
    lda init_tx_ctrl_block,y                                          ; 8fee: b9 91 83    ...            ; Load ROM template byte
    bne store_txcb_byte                                               ; 8ff1: d0 03       ..             ; Non-zero = use ROM template byte as-is
    lda nmi_sub_table,y                                               ; 8ff3: b9 e6 0d    ...            ; Zero = substitute from NMI workspace
; &8ff6 referenced 1 time by &8ff1
.store_txcb_byte
    sta (nfs_workspace),y                                             ; 8ff6: 91 9e       ..             ; Store to dynamic workspace
    dey                                                               ; 8ff8: 88          .              ; Descend through template
    cpy #&17                                                          ; 8ff9: c0 17       ..             ; Stop at offset &17
    bne dofs01                                                        ; 8ffb: d0 f1       ..             ; Loop until all bytes copied
    iny                                                               ; 8ffd: c8          .              ; Y=&18: TX block starts here
    sty net_tx_ptr                                                    ; 8ffe: 84 9a       ..             ; Point net_tx_ptr at workspace+&18
    jsr setup_rx_buffer_ptrs                                          ; 9000: 20 cd 8f     ..            ; Set up RX buffer start/end pointers
    ldy #2                                                            ; 9003: a0 02       ..             ; Y=2: port byte offset in RXCB
    lda #&90                                                          ; 9005: a9 90       ..             ; A=&90: FS reply port
    sta (osword_pb_ptr),y                                             ; 9007: 91 f0       ..             ; Store port &90 at (&F0)+2
    iny                                                               ; 9009: c8          .              ; Y=&03
    iny                                                               ; 900a: c8          .              ; Retrieve original A (function code) from stack; Y=&04
; &900b referenced 1 time by &9013
.copy_fs_addr
    lda fs_context_base,y                                             ; 900b: b9 fe 0d    ...            ; Copy FS station addr from workspace
    sta (osword_pb_ptr),y                                             ; 900e: 91 f0       ..             ; Store to RX param block
    iny                                                               ; 9010: c8          .              ; Next byte
    cpy #7                                                            ; 9011: c0 07       ..             ; Done 3 bytes (Y=4,5,6)?
    bne copy_fs_addr                                                  ; 9013: d0 f6       ..             ; No: continue copying
    lda nfs_workspace_hi                                              ; 9015: a5 9f       ..             ; High byte of workspace for TX ptr
    sta net_tx_ptr_hi                                                 ; 9017: 85 9b       ..             ; Store as TX pointer high byte
    cli                                                               ; 9019: 58          X              ; Enable interrupts before transmit
    jsr tx_poll_ff                                                    ; 901a: 20 8f 86     ..            ; Transmit with full retry
    ldy #&20 ; ' '                                                    ; 901d: a0 20       .              ; Y=&20: RX end address offset
    lda #&ff                                                          ; 901f: a9 ff       ..             ; Set RX end address to &FFFF (accept any length)
    sta (nfs_workspace),y                                             ; 9021: 91 9e       ..             ; Store end address low byte (&FF)
    iny                                                               ; 9023: c8          .              ; Y=&21
    sta (nfs_workspace),y                                             ; 9024: 91 9e       ..             ; Store end address high byte (&FF)
    ldy #&19                                                          ; 9026: a0 19       ..             ; Y=&19: port byte in workspace RXCB
    lda #&90                                                          ; 9028: a9 90       ..             ; A=&90: FS reply port
    sta (nfs_workspace),y                                             ; 902a: 91 9e       ..             ; Store port to workspace RXCB
    dey                                                               ; 902c: 88          .              ; Y=&18
    lda #&7f                                                          ; 902d: a9 7f       ..             ; A=&7F: flag byte = waiting for reply
    sta (nfs_workspace),y                                             ; 902f: 91 9e       ..             ; Store flag byte to workspace RXCB
    jmp send_to_fs_star                                               ; 9031: 4c 1b 85    L..            ; Jump to RX poll (BRIANX)

; &9034 referenced 1 time by &8fea
.handle_tx_result
    php                                                               ; 9034: 08          .              ; Save processor flags
    ldy #1                                                            ; 9035: a0 01       ..             ; Y=1: first data byte offset; Y=character to write
    lda (osword_pb_ptr),y                                             ; 9037: b1 f0       ..             ; Load first data byte from RX buffer
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
    tax                                                               ; 9039: aa          .              ; X = first data byte (command code)
    iny                                                               ; 903a: c8          .              ; ROR/ASL on stacked P: zeros carry to signal success; Advance to next data byte
    lda (osword_pb_ptr),y                                             ; 903b: b1 f0       ..             ; Load station address high byte
    iny                                                               ; 903d: c8          .              ; Advance past station addr
    sty ws_ptr_lo                                                     ; 903e: 84 ab       ..             ; Save Y as data index
    ldy #&72 ; 'r'                                                    ; 9040: a0 72       .r             ; Store station addr hi at (net_rx_ptr)+&72
    sta (net_rx_ptr),y                                                ; 9042: 91 9c       ..             ; Store to workspace
    dey                                                               ; 9044: 88          .              ; Y=&71
    txa                                                               ; 9045: 8a          .              ; A = command code (from X)
    sta (net_rx_ptr),y                                                ; 9046: 91 9c       ..             ; Store station addr lo at (net_rx_ptr)+&71
    plp                                                               ; 9048: 28          (              ; Restore flags from earlier PHP
    bne dofs2                                                         ; 9049: d0 1c       ..             ; First call: adjust data length
; &904b referenced 1 time by &9064
.send_data_bytes
    ldy ws_ptr_lo                                                     ; 904b: a4 ab       ..             ; Reload data index
    inc ws_ptr_lo                                                     ; 904d: e6 ab       ..             ; Advance data index for next iteration
    lda (osword_pb_ptr),y                                             ; 904f: b1 f0       ..             ; Load next data byte
    beq return_8                                                      ; 9051: f0 13       ..             ; Zero byte: end of data, return
    ldy #&7d ; '}'                                                    ; 9053: a0 7d       .}             ; Y=&7D: store byte for TX at offset &7D
    sta (net_rx_ptr),y                                                ; 9055: 91 9c       ..             ; Store data byte at (net_rx_ptr)+&7D for TX; Store data byte at (net_rx_ptr)+&7D for TX
    pha                                                               ; 9057: 48          H              ; Save data byte for &0D check after TX
    jsr ctrl_block_setup_alt                                          ; 9058: 20 73 91     s.            ; Set up TX control block
    jsr enable_irq_and_tx                                             ; 905b: 20 72 90     r.            ; Enable IRQs and transmit
; &905e referenced 1 time by &905f
.delay_between_tx
    dex                                                               ; 905e: ca          .              ; Short delay loop between TX packets
    bne delay_between_tx                                              ; 905f: d0 fd       ..             ; Spin until X reaches 0
    pla                                                               ; 9061: 68          h              ; Restore data byte for terminator check
    eor #&0d                                                          ; 9062: 49 0d       I.             ; Test for end-of-data marker (&0D)
    bne send_data_bytes                                               ; 9064: d0 e5       ..             ; Not &0D: continue with next byte
; &9066 referenced 1 time by &9051
.return_8
    rts                                                               ; 9066: 60          `              ; Return (data complete)

; &9067 referenced 1 time by &9049
.dofs2
    jsr ctrl_block_setup_alt                                          ; 9067: 20 73 91     s.            ; First-packet: set up control block
    ldy #&7b ; '{'                                                    ; 906a: a0 7b       .{             ; Y=&7B: data length offset
    lda (net_rx_ptr),y                                                ; 906c: b1 9c       ..             ; Load current data length
    adc #3                                                            ; 906e: 69 03       i.             ; Add 3 for header bytes; Adjust data length by 3 for header bytes
    sta (net_rx_ptr),y                                                ; 9070: 91 9c       ..             ; Store adjusted length
; ***************************************************************************************
; Enable interrupts and transmit via tx_poll_ff
; 
; CLI to enable interrupts, then JMP tx_poll_ff. A short
; tail-call wrapper used after building the TX control block.
; ***************************************************************************************
; &9072 referenced 1 time by &905b
.enable_irq_and_tx
    cli                                                               ; 9072: 58          X              ; Enable interrupts
    jmp tx_poll_ff                                                    ; 9073: 4c 8f 86    L..            ; Transmit via tx_poll_ff

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
    php                                                               ; 9076: 08          .              ; Save processor status
    pha                                                               ; 9077: 48          H              ; Save A (reason code)
    txa                                                               ; 9078: 8a          .              ; Save X
    pha                                                               ; 9079: 48          H              ; Push X to stack
    tya                                                               ; 907a: 98          .              ; Save Y
    pha                                                               ; 907b: 48          H              ; Push Y to stack
    tsx                                                               ; 907c: ba          .              ; Get stack pointer for indexed access
    lda l0103,x                                                       ; 907d: bd 03 01    ...            ; Retrieve original A (reason code) from stack
    cmp #9                                                            ; 9080: c9 09       ..             ; Reason codes 0-8 only
    bcs entry1                                                        ; 9082: b0 04       ..             ; Code >= 9: skip dispatch, restore regs
    tax                                                               ; 9084: aa          .              ; X = reason code for table lookup
    jsr osword_trampoline                                             ; 9085: 20 8f 90     ..            ; Dispatch to handler via trampoline
; &9088 referenced 1 time by &9082
.entry1
    pla                                                               ; 9088: 68          h              ; Restore Y
    tay                                                               ; 9089: a8          .              ; Transfer to Y register
    pla                                                               ; 908a: 68          h              ; Restore X
    tax                                                               ; 908b: aa          .              ; Transfer to X register
    pla                                                               ; 908c: 68          h              ; Restore A
    plp                                                               ; 908d: 28          (              ; Restore processor status flags
    rts                                                               ; 908e: 60          `              ; Return with all registers preserved

; &908f referenced 1 time by &9085
.osword_trampoline
    lda netvec_handler_hi,x                                           ; 908f: bd a3 90    ...            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 9092: 48          H              ; Push high byte of handler address
    lda osword_tbl_lo,x                                               ; 9093: bd 9a 90    ...            ; Load handler low byte from table
    pha                                                               ; 9096: 48          H              ; Push low byte of handler address
    lda osbyte_a_copy                                                 ; 9097: a5 ef       ..             ; Load workspace byte &EF for handler
    rts                                                               ; 9099: 60          `              ; RTS dispatches to pushed handler

; &909a referenced 1 time by &9093
.osword_tbl_lo
    equb <(return_1-1)                                                ; 909a: f5          .
    equb <(remote_print_handler-1)                                    ; 909b: de          .
    equb <(remote_print_handler-1)                                    ; 909c: de          .
    equb <(remote_print_handler-1)                                    ; 909d: de          .
    equb <(net_write_char_handler-1)                                  ; 909e: ab          .
    equb <(printer_select_handler-1)                                  ; 909f: ce          .
    equb <(return_1-1)                                                ; 90a0: f5          .
.osword_tbl_hi
    equb <(remote_cmd_dispatch-1)                                     ; 90a1: dd          .
    equb <(nword-1)                                                   ; 90a2: 47          G
; &90a3 referenced 1 time by &908f
.netvec_handler_hi
    equb >(return_1-1)                                                ; 90a3: 80          .
    equb >(remote_print_handler-1)                                    ; 90a4: 91          .
    equb >(remote_print_handler-1)                                    ; 90a5: 91          .
    equb >(remote_print_handler-1)                                    ; 90a6: 91          .
    equb >(net_write_char_handler-1)                                  ; 90a7: 90          .
    equb >(printer_select_handler-1)                                  ; 90a8: 91          .
    equb >(return_1-1)                                                ; 90a9: 80          .
    equb >(remote_cmd_dispatch-1)                                     ; 90aa: 90          .
    equb >(nword-1)                                                   ; 90ab: 91          .

.net_write_char_handler
    tsx                                                               ; 90ac: ba          .              ; Get stack pointer for P register access
    ror l0106,x                                                       ; 90ad: 7e 06 01    ~..            ; ROR/ASL on stacked P: zeros carry to signal success
    asl l0106,x                                                       ; 90b0: 1e 06 01    ...            ; ASL: restore P after ROR zeroed carry
    tya                                                               ; 90b3: 98          .              ; Y = character to write
    ldy #&da                                                          ; 90b4: a0 da       ..             ; Store character at workspace offset &DA
    sta (nfs_workspace),y                                             ; 90b6: 91 9e       ..             ; Store char at workspace offset &DA
    lda #0                                                            ; 90b8: a9 00       ..             ; A=0: command type for net write char
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
    ldy #&d9                                                          ; 90ba: a0 d9       ..             ; Y=&D9: command type offset
    sta (nfs_workspace),y                                             ; 90bc: 91 9e       ..             ; Store command type at ws+&D9
    lda #&80                                                          ; 90be: a9 80       ..             ; Mark TX control block as active (&80)
    ldy #&0c                                                          ; 90c0: a0 0c       ..             ; Y=&0C: TXCB start offset
    sta (nfs_workspace),y                                             ; 90c2: 91 9e       ..             ; Set TX active flag at ws+&0C
    lda net_tx_ptr                                                    ; 90c4: a5 9a       ..             ; Save net_tx_ptr; redirect to workspace TXCB
    pha                                                               ; 90c6: 48          H              ; Save net_tx_ptr low
    lda net_tx_ptr_hi                                                 ; 90c7: a5 9b       ..             ; Load net_tx_ptr high
    pha                                                               ; 90c9: 48          H              ; Save net_tx_ptr high
    sty net_tx_ptr                                                    ; 90ca: 84 9a       ..             ; Redirect net_tx_ptr low to workspace
    ldx nfs_workspace_hi                                              ; 90cc: a6 9f       ..             ; Load workspace page high byte
    stx net_tx_ptr_hi                                                 ; 90ce: 86 9b       ..             ; Complete ptr redirect
    jsr tx_poll_ff                                                    ; 90d0: 20 8f 86     ..            ; Transmit with full retry
    lda #&3f ; '?'                                                    ; 90d3: a9 3f       .?             ; Mark TXCB as deleted (&3F) after transmit
    sta (net_tx_ptr,x)                                                ; 90d5: 81 9a       ..             ; Write &3F to TXCB byte 0
    pla                                                               ; 90d7: 68          h              ; Restore net_tx_ptr high
    sta net_tx_ptr_hi                                                 ; 90d8: 85 9b       ..             ; Write back
    pla                                                               ; 90da: 68          h              ; Restore net_tx_ptr low
    sta net_tx_ptr                                                    ; 90db: 85 9a       ..             ; Write back
    rts                                                               ; 90dd: 60          `              ; Return

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
    ldy osword_pb_ptr_hi                                              ; 90de: a4 f1       ..             ; Load original Y (OSBYTE secondary param)
    cmp #&81                                                          ; 90e0: c9 81       ..             ; OSBYTE &81 (INKEY): always forward to terminal
    beq dispatch_remote_osbyte                                        ; 90e2: f0 13       ..             ; Forward &81 to terminal for keyboard read
    ldy #1                                                            ; 90e4: a0 01       ..             ; Y=1: search NCTBPL table (execute on both)
    ldx #7                                                            ; 90e6: a2 07       ..             ; X=9: 10-entry NCTBPL table size
    jsr match_osbyte_code                                             ; 90e8: 20 30 91     0.            ; Search for OSBYTE code in NCTBPL table
    beq dispatch_remote_osbyte                                        ; 90eb: f0 0a       ..             ; Match found: dispatch with Y=1 (both)
    dey                                                               ; 90ed: 88          .              ; Y=-1: search NCTBMI table (terminal only)
    dey                                                               ; 90ee: 88          .              ; Second DEY: Y=&FF (from 1 via 0)
    ldx #&0e                                                          ; 90ef: a2 0e       ..             ; X=&0E: 15-entry NCTBMI table size
    jsr match_osbyte_code                                             ; 90f1: 20 30 91     0.            ; Search for OSBYTE code in NCTBMI table
    beq dispatch_remote_osbyte                                        ; 90f4: f0 01       ..             ; Match found: dispatch with Y=&FF (terminal)
    iny                                                               ; 90f6: c8          .              ; Y=0: OSBYTE not recognised, ignore
; &90f7 referenced 3 times by &90e2, &90eb, &90f4
.dispatch_remote_osbyte
    ldx #2                                                            ; 90f7: a2 02       ..             ; X=2 bytes to copy (default for RBYTE)
    tya                                                               ; 90f9: 98          .              ; A=Y: check table match result
    beq return_nbyte                                                  ; 90fa: f0 33       .3             ; Y=0: not recognised, return unhandled
    php                                                               ; 90fc: 08          .              ; Y>0 (NCTBPL): send only, no result expected
    bpl nbyte6                                                        ; 90fd: 10 01       ..             ; Y>0 (NCTBPL): no result expected, skip RX
    inx                                                               ; 90ff: e8          .              ; Y<0 (NCTBMI): X=3 bytes (result + P flags); X=&03
; &9100 referenced 1 time by &90fd
.nbyte6
    ldy #&dc                                                          ; 9100: a0 dc       ..             ; Y=&DC: top of 3-byte stack frame region
; &9102 referenced 1 time by &910a
.nbyte1
    lda tube_claimed_id,y                                             ; 9102: b9 15 00    ...            ; Copy OSBYTE args from stack frame to workspace
    sta (nfs_workspace),y                                             ; 9105: 91 9e       ..             ; Store to NFS workspace for transmission
    dey                                                               ; 9107: 88          .              ; Next byte (descending)
    cpy #&da                                                          ; 9108: c0 da       ..             ; Copied all 3 bytes? (&DC, &DB, &DA)
    bpl nbyte1                                                        ; 910a: 10 f6       ..             ; Loop for remaining bytes
    txa                                                               ; 910c: 8a          .              ; A = byte count for setup_tx_and_send
    jsr setup_tx_and_send                                             ; 910d: 20 ba 90     ..            ; Build TXCB and transmit to terminal
    plp                                                               ; 9110: 28          (              ; Restore N flag from table match type
    bpl return_nbyte                                                  ; 9111: 10 1c       ..             ; Y was positive (NCTBPL): done, no result
    lda #&7f                                                          ; 9113: a9 7f       ..             ; Set up RX control block to wait for reply
    sta (net_tx_ptr,x)                                                ; 9115: 81 9a       ..             ; Write &7F to RXCB (wait for reply)
; &9117 referenced 1 time by &9119
.poll_rxcb_loop
    lda (net_tx_ptr,x)                                                ; 9117: a1 9a       ..             ; Poll RXCB for completion (bit7)
    bpl poll_rxcb_loop                                                ; 9119: 10 fc       ..             ; Bit7 clear: still waiting, poll again
    tsx                                                               ; 911b: ba          .              ; X = stack pointer for register restoration
    ldy #&dd                                                          ; 911c: a0 dd       ..             ; Y=&DD: saved P byte offset in workspace
    lda (nfs_workspace),y                                             ; 911e: b1 9e       ..             ; Load remote processor status from reply
    ora #&44 ; 'D'                                                    ; 9120: 09 44       .D             ; Force V=1 (claimed) and I=1 (no IRQ) in saved P
    bne nbyte5                                                        ; 9122: d0 04       ..             ; ALWAYS branch (ORA #&44 never zero); ALWAYS branch

; &9124 referenced 1 time by &912d
.nbyte4
    dey                                                               ; 9124: 88          .              ; Previous workspace offset
    dex                                                               ; 9125: ca          .              ; Previous stack register slot
    lda (nfs_workspace),y                                             ; 9126: b1 9e       ..             ; Load next result byte (X, then Y)
; &9128 referenced 1 time by &9122
.nbyte5
    sta l0106,x                                                       ; 9128: 9d 06 01    ...            ; Write result bytes to stacked registers
    cpy #&da                                                          ; 912b: c0 da       ..             ; Copied all result bytes? (P at &DA)
    bne nbyte4                                                        ; 912d: d0 f5       ..             ; Loop for remaining result bytes
; &912f referenced 2 times by &90fa, &9111
.return_nbyte
    rts                                                               ; 912f: 60          `              ; Return to OSBYTE dispatcher

; &9130 referenced 3 times by &90e8, &90f1, &9136
.match_osbyte_code
    cmp remote_osbyte_table,x                                         ; 9130: dd 39 91    .9.            ; Compare OSBYTE code with table entry
    beq return_match_osbyte                                           ; 9133: f0 03       ..             ; Match found: return with Z=1
    dex                                                               ; 9135: ca          .              ; Next table entry (descending)
    bpl match_osbyte_code                                             ; 9136: 10 f8       ..             ; Loop for remaining entries
; &9138 referenced 2 times by &9133, &9150
.return_match_osbyte
    rts                                                               ; 9138: 60          `              ; Return; Z=1 if match, Z=0 if not

; &9139 referenced 1 time by &9130
.remote_osbyte_table
    equb   4,   9, &0a, &14, &15, &9a, &9b, &e2, &0b, &0c, &0f, &79   ; 9139: 04 09 0a... ...
    equb &7a, &e3, &e4                                                ; 9145: 7a e3 e4    z..

.nword
    ldy #&0e                                                          ; 9148: a0 0e       ..             ; Y=14: max OSWORD parameter bytes
    cmp #7                                                            ; 914a: c9 07       ..             ; OSWORD 7 = make a sound
    beq copy_params_rword                                             ; 914c: f0 04       ..             ; OSWORD 7 (sound): handle via common path
    cmp #8                                                            ; 914e: c9 08       ..             ; OSWORD 8 = define an envelope
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
    bne return_match_osbyte                                           ; 9150: d0 e6       ..             ; Not OSWORD 7 or 8: ignore (BNE exits)
; &9152 referenced 1 time by &914c
.copy_params_rword
    ldx #&db                                                          ; 9152: a2 db       ..             ; Point workspace to offset &DB for params
    stx nfs_workspace                                                 ; 9154: 86 9e       ..             ; Store workspace ptr offset &DB
; &9156 referenced 1 time by &915b
.copy_osword_params
    lda (osword_pb_ptr),y                                             ; 9156: b1 f0       ..             ; Copy parameter bytes from RX buffer
    sta (nfs_workspace),y                                             ; 9158: 91 9e       ..             ; Write param byte to workspace
    dey                                                               ; 915a: 88          .              ; Next byte (descending)
    bpl copy_osword_params                                            ; 915b: 10 f9       ..             ; Loop for all parameter bytes
    iny                                                               ; 915d: c8          .              ; Y=0 after loop
    dec nfs_workspace                                                 ; 915e: c6 9e       ..             ; Point workspace to offset &DA
    lda osbyte_a_copy                                                 ; 9160: a5 ef       ..             ; Store original OSBYTE code at workspace+0
    sta (nfs_workspace),y                                             ; 9162: 91 9e       ..             ; Store OSBYTE code at ws+0
    sty nfs_workspace                                                 ; 9164: 84 9e       ..             ; Reset workspace ptr to base
    ldy #&14                                                          ; 9166: a0 14       ..             ; Y=&14: command type offset
    lda #&e9                                                          ; 9168: a9 e9       ..             ; Tag as RWORD (port &E9)
    sta (nfs_workspace),y                                             ; 916a: 91 9e       ..             ; Store port tag at ws+&14
    lda #1                                                            ; 916c: a9 01       ..             ; A=1: single-byte TX
    jsr setup_tx_and_send                                             ; 916e: 20 ba 90     ..            ; Load template byte from ctrl_block_template[X]; Transmit via workspace TXCB
    stx nfs_workspace                                                 ; 9171: 86 9e       ..             ; Restore workspace ptr
; ***************************************************************************************
; Alternate entry into control block setup
; 
; Sets X=&0D, Y=&7C. Tests bit 6 of &83AF to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; ***************************************************************************************
; &9173 referenced 2 times by &9058, &9067
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 9173: a2 0d       ..             ; X=&0D: template offset for alt entry
    ldy #&7c ; '|'                                                    ; 9175: a0 7c       .|             ; Y=&7C: target workspace offset for alt entry
    bit tx_ctrl_upper                                                 ; 9177: 2c af 83    ,..            ; BIT test: V flag = bit 6 of &83B3
    bvs cbset2                                                        ; 917a: 70 05       p.             ; V=1: store to (net_rx_ptr) instead
; ***************************************************************************************
; Control block setup — main entry
; 
; Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
; Reads the template table at &91A8 indexed by X, storing each
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
    ldy #&17                                                          ; 917c: a0 17       ..             ; Y=&17: workspace target offset (main entry)
    ldx #&1a                                                          ; 917e: a2 1a       ..             ; X=&1A: template table index (main entry)
; &9180 referenced 1 time by &9244
.ctrl_block_setup_clv
    clv                                                               ; 9180: b8          .              ; V=0: target is (nfs_workspace)
; &9181 referenced 1 time by &917a
.cbset2
    lda ctrl_block_template,x                                         ; 9181: bd a8 91    ...            ; Load template byte from ctrl_block_template[X]
    cmp #&fe                                                          ; 9184: c9 fe       ..             ; &FE = stop sentinel
    beq cb_template_tail                                              ; 9186: f0 1c       ..             ; End of template: jump to exit
    cmp #&fd                                                          ; 9188: c9 fd       ..             ; &FD = skip sentinel
    beq cb_template_main_start                                        ; 918a: f0 14       ..             ; Skip: don't store, just decrement Y
    cmp #&fc                                                          ; 918c: c9 fc       ..             ; &FC = page byte sentinel
    bne cbset3                                                        ; 918e: d0 08       ..             ; Not sentinel: store template value directly
    lda net_rx_ptr_hi                                                 ; 9190: a5 9d       ..             ; V=1: use (net_rx_ptr) page
    bvs rxcb_matched                                                  ; 9192: 70 02       p.             ; V=1: skip to net_rx_ptr page
    lda nfs_workspace_hi                                              ; 9194: a5 9f       ..             ; V=0: use (nfs_workspace) page
; &9196 referenced 1 time by &9192
.rxcb_matched
    sta net_tx_ptr_hi                                                 ; 9196: 85 9b       ..             ; PAGE byte → Y=&02 / Y=&74
; &9198 referenced 1 time by &918e
.cbset3
    bvs cbset4                                                        ; 9198: 70 04       p.             ; → Y=&04 / Y=&76
    sta (nfs_workspace),y                                             ; 919a: 91 9e       ..             ; PAGE byte → Y=&06 / Y=&78
    equb &50                                                          ; 919c: 50          P              ; → Y=&08 / Y=&7A
    equb 2                                                            ; 919d: 02          .
; &919e referenced 1 time by &9198
.cbset4
    equb &91                                                          ; 919e: 91          .              ; Alt-path only → Y=&70
    equb &9c                                                          ; 919f: 9c          .
; &91a0 referenced 1 time by &918a
.cb_template_main_start
    equb &88                                                          ; 91a0: 88          .              ; SKIP
    equb &ca                                                          ; 91a1: ca          .              ; → Y=&01 / Y=&73
    equb &10                                                          ; 91a2: 10          .
    equb &dd                                                          ; 91a3: dd          .
; &91a4 referenced 1 time by &9186
.cb_template_tail
    equb &c8                                                          ; 91a4: c8          .
    equb &84                                                          ; 91a5: 84          .
    equb &9a                                                          ; 91a6: 9a          .              ; PAGE byte → Y=&06 / Y=&78
    equb &60                                                          ; 91a7: 60          `              ; → Y=&07 / Y=&79
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
    equb &7d                                                          ; 91ac: 7d          }              ; → Y=&0C (main only)
    equb &fc                                                          ; 91ad: fc          .              ; PAGE byte → Y=&02 / Y=&74; → Y=&0D (main only)
    equb &ff                                                          ; 91ae: ff          .              ; → Y=&03 / Y=&75
    equb &ff                                                          ; 91af: ff          .              ; → Y=&04 / Y=&76; SKIP (main only)
    equb &7e                                                          ; 91b0: 7e          ~              ; → Y=&05 / Y=&77; → Y=&10 (main only)
    equb &fc                                                          ; 91b1: fc          .
    equb &ff                                                          ; 91b2: ff          .
    equb &ff                                                          ; 91b3: ff          .              ; → Y=&08 / Y=&7A
    equb 0                                                            ; 91b4: 00          .              ; → Y=&09 / Y=&7B
    equb 0                                                            ; 91b5: 00          .              ; → Y=&0A / Y=&7C; PAGE byte → Y=&15 (main only)
    equb &fe                                                          ; 91b6: fe          .              ; STOP — main-path boundary; → Y=&16 (main only)
    equb &80                                                          ; 91b7: 80          .
    equb &93, &fd, &fd, &d9, &fc, &ff, &ff, &de, &fc, &ff, &ff, &fe   ; 91b8: 93 fd fd... ...            ; SKIP (main only); PAGE byte → Y=&11 (main only); → Y=&12 (main only); → Y=&13 (main only); → Y=&14 (main only); → Y=&17 (main only)
    equb &d1, &fd, &fd, &1f, &fd, &ff, &ff, &fd, &fd, &ff, &ff        ; 91c4: d1 fd fd... ...

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
    dex                                                               ; 91cf: ca          .              ; X-1: convert 1-based buffer to 0-based
    cpx osword_pb_ptr                                                 ; 91d0: e4 f0       ..             ; Is this the network printer buffer?
    bne setup1                                                        ; 91d2: d0 07       ..             ; No: skip printer init
    lda #&1f                                                          ; 91d4: a9 1f       ..             ; &1F = initial buffer pointer offset
    sta printer_buf_ptr                                               ; 91d6: 8d 61 0d    .a.            ; Reset printer buffer write position
    lda #&41 ; 'A'                                                    ; 91d9: a9 41       .A             ; &41 = initial PFLAGS (bit 6 set, bit 0 set)
; &91db referenced 1 time by &91d2
.setup1
    sta l0d60                                                         ; 91db: 8d 60 0d    .`.            ; Store initial PFLAGS value
; &91de referenced 2 times by &91e1, &91f5
.return_printer_select
    rts                                                               ; 91de: 60          `              ; Return

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
    cpy #4                                                            ; 91df: c0 04       ..             ; Only handle buffer 4 (network printer)
    bne return_printer_select                                         ; 91e1: d0 fb       ..             ; Not buffer 4: ignore
    txa                                                               ; 91e3: 8a          .              ; A = reason code
    dex                                                               ; 91e4: ca          .              ; Reason 1? (DEX: 1->0)
    bne toggle_print_flag                                             ; 91e5: d0 26       .&             ; Not reason 1: handle Ctrl-B/C
    tsx                                                               ; 91e7: ba          .              ; Get stack pointer for P register
    ora l0106,x                                                       ; 91e8: 1d 06 01    ...            ; Force I flag in stacked P to block IRQs
    sta l0106,x                                                       ; 91eb: 9d 06 01    ...            ; Write back modified P register
; &91ee referenced 2 times by &91fd, &9202
.prlp1
    lda #osbyte_read_buffer                                           ; 91ee: a9 91       ..             ; OSBYTE &91: extract char from MOS buffer
    ldx #buffer_printer                                               ; 91f0: a2 03       ..             ; X=3: printer buffer number
    jsr osbyte                                                        ; 91f2: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_printer_select                                         ; 91f5: b0 e7       ..             ; Buffer empty: return
    tya                                                               ; 91f7: 98          .              ; Y = extracted character; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 91f8: 20 04 92     ..            ; Store char in output buffer
    cpy #&6e ; 'n'                                                    ; 91fb: c0 6e       .n             ; Buffer nearly full? (&6E = threshold)
    bcc prlp1                                                         ; 91fd: 90 ef       ..             ; Not full: get next char
    jsr flush_output_block                                            ; 91ff: 20 30 92     0.            ; Buffer full: flush to network
    bcc prlp1                                                         ; 9202: 90 ea       ..             ; Continue after flush
; ***************************************************************************************
; Store output byte to network buffer
; 
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; ***************************************************************************************
; &9204 referenced 2 times by &91f8, &9211
.store_output_byte
    ldy printer_buf_ptr                                               ; 9204: ac 61 0d    .a.            ; Load current buffer offset
    sta (net_rx_ptr),y                                                ; 9207: 91 9c       ..             ; Store byte at current position
    inc printer_buf_ptr                                               ; 9209: ee 61 0d    .a.            ; Advance buffer pointer
    rts                                                               ; 920c: 60          `              ; Return; Y = buffer offset

; &920d referenced 1 time by &91e5
.toggle_print_flag
    pha                                                               ; 920d: 48          H              ; Save reason code
    txa                                                               ; 920e: 8a          .              ; A = reason code
    eor #1                                                            ; 920f: 49 01       I.             ; EOR #1: toggle print-active flag (bit 0)
    jsr store_output_byte                                             ; 9211: 20 04 92     ..            ; Store toggled flag as output byte
    eor l0d60                                                         ; 9214: 4d 60 0d    M`.            ; XOR with current PFLAGS
    ror a                                                             ; 9217: 6a          j              ; Test if sequence changed (bit 7 mismatch)
    bcc pril1                                                         ; 9218: 90 07       ..             ; Sequence unchanged: skip flush
    rol a                                                             ; 921a: 2a          *              ; Undo ROR
    sta l0d60                                                         ; 921b: 8d 60 0d    .`.            ; Store toggled PFLAGS
    jsr flush_output_block                                            ; 921e: 20 30 92     0.            ; Flush current output block
; &9221 referenced 1 time by &9218
.pril1
    lda l0d60                                                         ; 9221: ad 60 0d    .`.            ; Reload current PFLAGS
    and #&f0                                                          ; 9224: 29 f0       ).             ; Extract upper nibble of PFLAGS
    ror a                                                             ; 9226: 6a          j              ; Shift for bit extraction
    tax                                                               ; 9227: aa          .              ; Save in X
    pla                                                               ; 9228: 68          h              ; Restore original reason code
    ror a                                                             ; 9229: 6a          j              ; Merge print-active bit from original A
    txa                                                               ; 922a: 8a          .              ; Retrieve shifted PFLAGS
    rol a                                                             ; 922b: 2a          *              ; Recombine into new PFLAGS value
    sta l0d60                                                         ; 922c: 8d 60 0d    .`.            ; Store recombined PFLAGS value
    rts                                                               ; 922f: 60          `              ; Return

; ***************************************************************************************
; Flush output block
; 
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; ***************************************************************************************
; &9230 referenced 2 times by &91ff, &921e
.flush_output_block
    ldy #8                                                            ; 9230: a0 08       ..             ; Store buffer length at workspace offset &08
    lda printer_buf_ptr                                               ; 9232: ad 61 0d    .a.            ; Current buffer fill position
    sta (nfs_workspace),y                                             ; 9235: 91 9e       ..             ; Write to workspace offset &08
    lda net_rx_ptr_hi                                                 ; 9237: a5 9d       ..             ; Store page high byte at offset &09
    iny                                                               ; 9239: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 923a: 91 9e       ..             ; Write page high byte at offset &09
    ldy #5                                                            ; 923c: a0 05       ..             ; Also store at offset &05
    sta (nfs_workspace),y                                             ; 923e: 91 9e       ..             ; (end address high byte)
    ldy #&0b                                                          ; 9240: a0 0b       ..             ; Y=&0B: flag byte offset
    ldx #&26 ; '&'                                                    ; 9242: a2 26       .&             ; X=&26: start from template entry &26
    jsr ctrl_block_setup_clv                                          ; 9244: 20 80 91     ..            ; Reuse ctrl_block_setup with CLV entry
    dey                                                               ; 9247: 88          .              ; Y=&0A: sequence flag byte offset
    lda l0d60                                                         ; 9248: ad 60 0d    .`.            ; Load current PFLAGS
    pha                                                               ; 924b: 48          H              ; Save current PFLAGS
    rol a                                                             ; 924c: 2a          *              ; Carry = current sequence (bit 7)
    pla                                                               ; 924d: 68          h              ; Restore original PFLAGS
    eor #&80                                                          ; 924e: 49 80       I.             ; Toggle sequence number (bit 7 of PFLAGS)
    sta l0d60                                                         ; 9250: 8d 60 0d    .`.            ; Store toggled sequence number
    rol a                                                             ; 9253: 2a          *              ; Old sequence bit into bit 0
    sta (nfs_workspace),y                                             ; 9254: 91 9e       ..             ; Store sequence flag at offset &0A
    ldy #&1f                                                          ; 9256: a0 1f       ..             ; Y=&1F: buffer start offset
    sty printer_buf_ptr                                               ; 9258: 8c 61 0d    .a.            ; Reset printer buffer to start (&1F)
    lda #0                                                            ; 925b: a9 00       ..             ; A=0: printer output flag
    tax                                                               ; 925d: aa          .              ; X=0: workspace low byte; X=&00
    ldy nfs_workspace_hi                                              ; 925e: a4 9f       ..             ; Y = workspace page high byte
    cli                                                               ; 9260: 58          X              ; Enable interrupts before TX
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
    stx net_tx_ptr                                                    ; 9261: 86 9a       ..             ; Set TX control block ptr low byte
    sty net_tx_ptr_hi                                                 ; 9263: 84 9b       ..             ; Set TX control block ptr high byte
    pha                                                               ; 9265: 48          H              ; Save A (handle bitmask) for later
    and fs_sequence_nos                                               ; 9266: 2d 08 0e    -..            ; Compute sequence bit from handle
    beq bsxl1                                                         ; 9269: f0 02       ..             ; Zero: no sequence bit set
    lda #1                                                            ; 926b: a9 01       ..             ; Non-zero: normalise to bit 0
; &926d referenced 1 time by &9269
.bsxl1
    ldy #0                                                            ; 926d: a0 00       ..             ; Y=0: flag byte offset in TXCB
    ora (net_tx_ptr),y                                                ; 926f: 11 9a       ..             ; Merge sequence into existing flag byte
    pha                                                               ; 9271: 48          H              ; Save merged flag byte
    sta (net_tx_ptr),y                                                ; 9272: 91 9a       ..             ; Write flag+sequence to TXCB byte 0
    jsr tx_poll_ff                                                    ; 9274: 20 8f 86     ..            ; Transmit with full retry
    lda #&ff                                                          ; 9277: a9 ff       ..             ; End address &FFFF = unlimited data length
    ldy #8                                                            ; 9279: a0 08       ..             ; Y=8: end address low offset in TXCB
    sta (net_tx_ptr),y                                                ; 927b: 91 9a       ..             ; Store &FF to end addr low
    iny                                                               ; 927d: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 927e: 91 9a       ..             ; Store &FF to end addr high (Y=9)
    pla                                                               ; 9280: 68          h              ; Recover merged flag byte
    tax                                                               ; 9281: aa          .              ; Save in X for sequence compare
    ldy #&d1                                                          ; 9282: a0 d1       ..             ; Y=&D1: printer port number
    pla                                                               ; 9284: 68          h              ; Recover saved handle bitmask
    pha                                                               ; 9285: 48          H              ; Re-save for later consumption
    beq bspsx                                                         ; 9286: f0 02       ..             ; A=0: port &D1 (print); A!=0: port &90 (FS)
    ldy #&90                                                          ; 9288: a0 90       ..             ; Y=&90: FS data port
; &928a referenced 1 time by &9286
.bspsx
    tya                                                               ; 928a: 98          .              ; A = selected port number
    ldy #1                                                            ; 928b: a0 01       ..             ; Y=1: port byte offset in TXCB
    sta (net_tx_ptr),y                                                ; 928d: 91 9a       ..             ; Write port to TXCB byte 1
    txa                                                               ; 928f: 8a          .              ; A = saved flag byte (expected sequence)
    dey                                                               ; 9290: 88          .              ; Y=&00
    pha                                                               ; 9291: 48          H              ; Push expected sequence for retry loop
; &9292 referenced 1 time by &929e
.bsxl0
    lda #&7f                                                          ; 9292: a9 7f       ..             ; Flag byte &7F = waiting for reply
    sta (net_tx_ptr),y                                                ; 9294: 91 9a       ..             ; Write to TXCB flag byte (Y=0)
    jsr send_to_fs_star                                               ; 9296: 20 1b 85     ..            ; Transmit and wait for reply (BRIANX)
    pla                                                               ; 9299: 68          h              ; Recover expected sequence
    pha                                                               ; 929a: 48          H              ; Keep on stack for next iteration
    eor (net_tx_ptr),y                                                ; 929b: 51 9a       Q.             ; Check if TX result matches expected sequence
    ror a                                                             ; 929d: 6a          j              ; Bit 0 to carry (sequence mismatch?)
    bcs bsxl0                                                         ; 929e: b0 f2       ..             ; C=1: mismatch, retry transmit
    pla                                                               ; 92a0: 68          h              ; Clean up: discard expected sequence
    pla                                                               ; 92a1: 68          h              ; Discard saved handle bitmask
    eor fs_sequence_nos                                               ; 92a2: 4d 08 0e    M..            ; Toggle sequence bit on success
.return_bspsx
    rts                                                               ; 92a5: 60          `              ; Return

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
; (OSBYTE &C3) using the 3-entry table at &9319.
; On completion, restores the JSR buffer protection bits (LSTAT)
; from OLDJSR to re-enable JSR reception, which was disabled during
; the screen data capture to prevent interference.
; ***************************************************************************************
.lang_2_save_palette_vdu
    lda table_idx                                                     ; 92a6: a5 ad       ..             ; Save current table index
    pha                                                               ; 92a8: 48          H              ; Push for later restore
    lda #&e9                                                          ; 92a9: a9 e9       ..             ; Point workspace to palette save area (&E9)
    sta nfs_workspace                                                 ; 92ab: 85 9e       ..             ; Set workspace low byte
    ldy #0                                                            ; 92ad: a0 00       ..             ; Y=0: first palette entry
    sty table_idx                                                     ; 92af: 84 ad       ..             ; Clear table index counter
    lda l0350                                                         ; 92b1: ad 50 03    .P.            ; Save current screen MODE to workspace
    sta (nfs_workspace),y                                             ; 92b4: 91 9e       ..             ; Store MODE at workspace[0]
    inc nfs_workspace                                                 ; 92b6: e6 9e       ..             ; Advance workspace pointer past MODE byte
    lda l0351                                                         ; 92b8: ad 51 03    .Q.            ; Read colour count (from &0351)
    pha                                                               ; 92bb: 48          H              ; Push for iteration count tracking
    tya                                                               ; 92bc: 98          .              ; A=0: logical colour number for OSWORD; A=&00
; &92bd referenced 1 time by &92dc
.save_palette_entry
    sta (nfs_workspace),y                                             ; 92bd: 91 9e       ..             ; Store logical colour at workspace[0]
    ldx nfs_workspace                                                 ; 92bf: a6 9e       ..             ; X = workspace ptr low (param block addr)
    ldy nfs_workspace_hi                                              ; 92c1: a4 9f       ..             ; Y = workspace ptr high
    lda #osword_read_palette                                          ; 92c3: a9 0b       ..             ; OSWORD &0B: read palette for logical colour
    jsr osword                                                        ; 92c5: 20 f1 ff     ..            ; Read palette
    pla                                                               ; 92c8: 68          h              ; Recover colour count
    ldy #0                                                            ; 92c9: a0 00       ..             ; Y=0: access workspace[0]
    sta (nfs_workspace),y                                             ; 92cb: 91 9e       ..             ; Write colour count back to workspace[0]
    iny                                                               ; 92cd: c8          .              ; Y=1: access workspace[1] (palette result); Y=&01
    lda (nfs_workspace),y                                             ; 92ce: b1 9e       ..             ; Read palette value returned by OSWORD
    pha                                                               ; 92d0: 48          H              ; Push palette value for next iteration
    ldx nfs_workspace                                                 ; 92d1: a6 9e       ..             ; X = current workspace ptr low
    inc nfs_workspace                                                 ; 92d3: e6 9e       ..             ; Advance workspace pointer
    inc table_idx                                                     ; 92d5: e6 ad       ..             ; Increment table index
    dey                                                               ; 92d7: 88          .              ; Y=0 for next store; Y=&00
    lda table_idx                                                     ; 92d8: a5 ad       ..             ; Load table index as logical colour
    cpx #&f9                                                          ; 92da: e0 f9       ..             ; Loop until workspace wraps past &F9
    bne save_palette_entry                                            ; 92dc: d0 df       ..             ; Continue for all 16 palette entries
    pla                                                               ; 92de: 68          h              ; Discard last palette value from stack
    sty table_idx                                                     ; 92df: 84 ad       ..             ; Reset table index to 0
    inc nfs_workspace                                                 ; 92e1: e6 9e       ..             ; Advance workspace past palette data
    jsr save_vdu_state                                                ; 92e3: 20 f2 92     ..            ; Save cursor pos and OSBYTE state values
    inc nfs_workspace                                                 ; 92e6: e6 9e       ..             ; Advance workspace past VDU state data
    pla                                                               ; 92e8: 68          h              ; Recover saved table index
    sta table_idx                                                     ; 92e9: 85 ad       ..             ; Restore table index
; &92eb referenced 4 times by &84a0, &84c8, &84ef, &8ee6
.clear_jsr_protection
    lda saved_jsr_mask                                                ; 92eb: ad 65 0d    .e.            ; Restore LSTAT from saved OLDJSR value
    sta prot_status                                                   ; 92ee: 8d 63 0d    .c.            ; Write to protection status
    rts                                                               ; 92f1: 60          `              ; Return

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
    lda l0355                                                         ; 92f2: ad 55 03    .U.            ; Read cursor editing state
    sta (nfs_workspace),y                                             ; 92f5: 91 9e       ..             ; Store to workspace[Y]
    tax                                                               ; 92f7: aa          .              ; Preserve in X for OSBYTE
    jsr read_vdu_osbyte                                               ; 92f8: 20 05 93     ..            ; OSBYTE &85: read cursor position
    inc nfs_workspace                                                 ; 92fb: e6 9e       ..             ; Advance workspace pointer
    tya                                                               ; 92fd: 98          .              ; Y result from OSBYTE &85
    sta (nfs_workspace,x)                                             ; 92fe: 81 9e       ..             ; Store Y pos to workspace (X=0)
    jsr read_vdu_osbyte_x0                                            ; 9300: 20 03 93     ..            ; Self-call trick: executes twice
; &9303 referenced 1 time by &9300
.read_vdu_osbyte_x0
    ldx #0                                                            ; 9303: a2 00       ..             ; X=0 for (zp,X) addressing
; &9305 referenced 1 time by &92f8
.read_vdu_osbyte
    ldy table_idx                                                     ; 9305: a4 ad       ..             ; Index into OSBYTE number table
    inc table_idx                                                     ; 9307: e6 ad       ..             ; Next table entry next time
    inc nfs_workspace                                                 ; 9309: e6 9e       ..             ; Advance workspace pointer
    lda vdu_osbyte_table,y                                            ; 930b: b9 19 93    ...            ; Read OSBYTE number from table
    ldy #&ff                                                          ; 930e: a0 ff       ..             ; Y=&FF: read current value
    jsr osbyte                                                        ; 9310: 20 f4 ff     ..            ; Call OSBYTE
    txa                                                               ; 9313: 8a          .              ; Result in X to A
    ldx #0                                                            ; 9314: a2 00       ..             ; X=0 for indexed indirect store
    sta (nfs_workspace,x)                                             ; 9316: 81 9e       ..             ; Store result to workspace
    rts                                                               ; 9318: 60          `              ; Return after storing result

; &9319 referenced 1 time by &930b
.vdu_osbyte_table
    equb &85, &c2, &c3                                                ; 9319: 85 c2 c3    ...            ; OSBYTE &85: read cursor position; OSBYTE &C3: read screen start address
; &931c referenced 1 time by &8175

    org &9656

    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff             ; 9656: ff ff ff... ...

; &9660 referenced 2 times by &86aa, &8ed1
.trampoline_tx_setup
    jmp tx_begin                                                      ; 9660: 4c c7 9b    L..            ; Trampoline: forward to tx_begin

; &9663 referenced 1 time by &8319
.trampoline_adlc_init
    jmp adlc_init                                                     ; 9663: 4c 6f 96    Lo.            ; Trampoline: forward to adlc_init

.svc_12_nmi_release
    jmp poll_nmi_ready                                                ; 9666: 4c b2 96    L..            ; Trampoline: forward to NMI release

.svc_11_nmi_claim
    jmp init_nmi_workspace                                            ; 9669: 4c 8d 96    L..            ; Trampoline: forward to NMI claim

.svc_5_unknown_irq
    jmp check_cb1_irq                                                 ; 966c: 4c 35 9b    L5.            ; Trampoline: forward to IRQ handler

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
    jsr adlc_full_reset                                               ; 9672: 20 d8 96     ..            ; Full ADLC hardware reset
    lda #osbyte_read_tube_presence                                    ; 9675: a9 ea       ..             ; OSBYTE &EA: check Tube co-processor
    ldx #0                                                            ; 9677: a2 00       ..             ; X=0 for OSBYTE
    stx econet_init_flag                                              ; 9679: 8e 66 0d    .f.            ; Clear Econet init flag before setup
    ldy #&ff                                                          ; 967c: a0 ff       ..             ; Y=&FF for OSBYTE
    jsr osbyte                                                        ; 967e: 20 f4 ff     ..            ; Read Tube present flag
    stx tube_flag                                                     ; 9681: 8e 67 0d    .g.            ; X=value of Tube present flag
    lda #osbyte_issue_service_request                                 ; 9684: a9 8f       ..             ; OSBYTE &8F: issue service request
    ldx #&0c                                                          ; 9686: a2 0c       ..             ; X=&0C: NMI claim service
    ldy #&ff                                                          ; 9688: a0 ff       ..             ; Y=&FF: pass to adlc_init_workspace
; ***************************************************************************************
; Initialise NMI workspace
; 
; Issues OSBYTE &8F with X=&0C (NMI claim service request) before
; copying the NMI shim. Sub-entry at &968A skips the service
; request for quick re-init. Then copies 32 bytes of
; NMI shim from ROM (&9FA8) to RAM (&0D00), patches the current
; ROM bank number into the shim's self-modifying code at &0D07,
; sets TX clear flag and econet_init_flag to &80, reads station ID
; from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
; and re-enables NMIs by reading &FE20 (INTON side effect).
; ***************************************************************************************
.adlc_init_workspace
    jsr osbyte                                                        ; 968a: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=12 - NMI claim
; ***************************************************************************************
; Initialise NMI workspace (skip service request)
; 
; Sub-entry of adlc_init_workspace that skips the OSBYTE &8F
; service request. Copies 32 bytes of NMI shim from ROM to
; &0D00, patches the ROM bank number, sets init flags, reads
; station ID, and re-enables NMIs.
; ***************************************************************************************
; &968d referenced 1 time by &9669
.init_nmi_workspace
    ldy #&20 ; ' '                                                    ; 968d: a0 20       .              ; Copy 32 bytes of NMI shim from ROM to &0D00
; &968f referenced 1 time by &9696
.copy_nmi_shim
    lda nmi_shim_rom_src,y                                            ; 968f: b9 a7 9f    ...            ; Read byte from NMI shim ROM source
    sta l0cff,y                                                       ; 9692: 99 ff 0c    ...            ; Write to NMI shim RAM at &0D00
    dey                                                               ; 9695: 88          .              ; Next byte (descending)
    bne copy_nmi_shim                                                 ; 9696: d0 f7       ..             ; Loop until all 32 bytes copied
    lda romsel_copy                                                   ; 9698: a5 f4       ..             ; Patch current ROM bank into NMI shim
    sta nmi_shim_07                                                   ; 969a: 8d 07 0d    ...            ; Self-modifying code: ROM bank at &0D07
    lda #&80                                                          ; 969d: a9 80       ..             ; &80 = Econet initialised
    sta tx_clear_flag                                                 ; 969f: 8d 62 0d    .b.            ; Mark TX as complete (ready)
    sta econet_init_flag                                              ; 96a2: 8d 66 0d    .f.            ; Mark Econet as initialised
    lda station_id_disable_net_nmis                                   ; 96a5: ad 18 fe    ...            ; Read station ID (&FE18 = INTOFF side effect)
    sta tx_src_stn                                                    ; 96a8: 8d 22 0d    .".            ; Store our station ID in TX scout
    sty tx_src_net                                                    ; 96ab: 8c 23 0d    .#.            ; Y=0 after copy loop: net = local
    bit video_ula_control                                             ; 96ae: 2c 20 fe    , .            ; BIT VULA: enable NMIs via latch
    rts                                                               ; 96b1: 60          `              ; Return from NMI workspace init

; &96b2 referenced 1 time by &9666
.poll_nmi_ready
    bit econet_init_flag                                              ; 96b2: 2c 66 0d    ,f.            ; Test Econet init complete flag
    bpl enter_rx_listen                                               ; 96b5: 10 1e       ..             ; Init done: enter RX listen mode
; &96b7 referenced 2 times by &96bc, &96c3
.nmi_vec_lo_match
    lda nmi_jmp_lo                                                    ; 96b7: ad 0c 0d    ...            ; Load NMI vector low byte
    cmp #&f2                                                          ; 96ba: c9 f2       ..             ; Check if low byte is expected value
    bne nmi_vec_lo_match                                              ; 96bc: d0 f9       ..             ; Mismatch: keep polling
    lda nmi_jmp_hi                                                    ; 96be: ad 0d 0d    ...            ; Load NMI vector high byte
    cmp #&96                                                          ; 96c1: c9 96       ..             ; Check if high byte is &97
    bne nmi_vec_lo_match                                              ; 96c3: d0 f2       ..             ; Mismatch: keep polling
    bit station_id_disable_net_nmis                                   ; 96c5: 2c 18 fe    ,..            ; BIT INTOFF: disable NMIs
; ***************************************************************************************
; Save Econet state to RX control block
; 
; Stores rx_status_flags, protection_mask, and tx_in_progress
; to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.
; ***************************************************************************************
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 96c8: 2c 18 fe    ,..            ; INTOFF: disable NMIs
    lda #0                                                            ; 96cb: a9 00       ..             ; A=0: clear TX and init flags
    sta tx_clear_flag                                                 ; 96cd: 8d 62 0d    .b.            ; Clear TX semaphore (allow new TX)
    sta econet_init_flag                                              ; 96d0: 8d 66 0d    .f.            ; Clear Econet init flag
    ldy #5                                                            ; 96d3: a0 05       ..             ; Y=5: status flags offset
; &96d5 referenced 1 time by &96b5
.enter_rx_listen
    jmp adlc_rx_listen                                                ; 96d5: 4c e7 96    L..            ; Re-enter idle RX listen mode

; ***************************************************************************************
; ADLC full reset
; 
; Aborts all activity and returns to idle RX listen mode.
; ***************************************************************************************
; &96d8 referenced 3 times by &9672, &973a, &987a
.adlc_full_reset
    lda #&c1                                                          ; 96d8: a9 c1       ..             ; CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 96da: 8d a0 fe    ...            ; Write CR1: full reset
    lda #&1e                                                          ; 96dd: a9 1e       ..             ; CR4=&1E: 8-bit word, abort ext, NRZ
    sta econet_data_terminate_frame                                   ; 96df: 8d a3 fe    ...            ; Write CR4 via ADLC reg 3 (AC=1)
    lda #0                                                            ; 96e2: a9 00       ..             ; CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 96e4: 8d a1 fe    ...            ; Write CR3=0: clear loop-back/AEX/DTR
; ***************************************************************************************
; Enter RX listen mode
; 
; TX held in reset, RX active with interrupts. Clears all status.
; ***************************************************************************************
; &96e7 referenced 2 times by &96d5, &9a3d
.adlc_rx_listen
    lda #&82                                                          ; 96e7: a9 82       ..             ; CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding; CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 96e9: 8d a0 fe    ...            ; Write CR1: RIE | TX_RESET
    lda #&67 ; 'g'                                                    ; 96ec: a9 67       .g             ; CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 96ee: 8d a1 fe    ...            ; Write CR2: listen mode config
    rts                                                               ; 96f1: 60          `              ; Return

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
    bit econet_control23_or_status2                                   ; 96f4: 2c a1 fe    ,..            ; BIT SR2: Z = A AND SR2 -- tests if AP is set
    beq scout_error                                                   ; 96f7: f0 3a       .:             ; AP not set, no incoming data -- check for errors
    lda econet_data_continue_frame                                    ; 96f9: ad a2 fe    ...            ; Read first RX byte (destination station address)
    cmp station_id_disable_net_nmis                                   ; 96fc: cd 18 fe    ...            ; Compare to our station ID (&FE18 read = INTOFF, disables NMIs)
    beq accept_frame                                                  ; 96ff: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 9701: c9 ff       ..             ; Check for broadcast address (&FF)
    bne scout_reject                                                  ; 9703: d0 1a       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 9705: a9 40       .@             ; Flag &40 = broadcast frame
    sta tx_flags                                                      ; 9707: 8d 4a 0d    .J.            ; Clear TX flags for new reception
; &970a referenced 1 time by &96ff
.accept_frame
    lda #&11                                                          ; 970a: a9 11       ..             ; Install next NMI handler at &9715 (RX scout second byte); Install next NMI handler at &96DC (RX scout net byte)
    ldy #&97                                                          ; 970c: a0 97       ..             ; High byte of scout net handler
    jmp set_nmi_vector                                                ; 970e: 4c 0e 0d    L..            ; Install next handler and RTI

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
    beq accept_local_net                                              ; 9719: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 971b: 49 ff       I.             ; EOR &FF: test if network = &FF (broadcast)
    beq accept_scout_net                                              ; 971d: f0 0b       ..             ; Broadcast network -- accept
; &971f referenced 1 time by &9703
.scout_reject
    lda #&a2                                                          ; 971f: a9 a2       ..             ; Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 9721: 8d a0 fe    ...            ; Write CR1 to discontinue RX
    jmp install_rx_scout_handler                                      ; 9724: 4c 40 9a    L@.            ; Return to idle scout listening

; &9727 referenced 1 time by &9719
.accept_local_net
    sta tx_flags                                                      ; 9727: 8d 4a 0d    .J.            ; Network = &FF broadcast: clear &0D4A; Network = 0 (local): clear tx_flags
; &972a referenced 1 time by &971d
.accept_scout_net
    sta port_buf_len                                                  ; 972a: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #&43 ; 'C'                                                    ; 972c: a9 43       .C             ; Install scout data reading loop at &9747; Install scout data reading loop at &970E
    ldy #&97                                                          ; 972e: a0 97       ..             ; High byte of scout data handler
    jmp set_nmi_vector                                                ; 9730: 4c 0e 0d    L..            ; Install scout data loop and RTI

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
; &9733 referenced 5 times by &96f7, &9714, &9748, &977c, &977e
.scout_error
    lda econet_control23_or_status2                                   ; 9733: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 9736: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 9738: f0 06       ..             ; Neither set -- clean end, discard via &9A40; Neither set -- clean end, discard via &99E8
    jsr adlc_full_reset                                               ; 973a: 20 d8 96     ..            ; Unexpected data/status: full ADLC reset
    jmp install_rx_scout_handler                                      ; 973d: 4c 40 9a    L@.            ; Discard and return to idle

; &9740 referenced 1 time by &9738
.scout_discard
    jmp discard_listen                                                ; 9740: 4c 3d 9a    L=.            ; Gentle discard: RX_DISCONTINUE

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
    bpl scout_error                                                   ; 9748: 10 e9       ..             ; No RDA -- error handler &9737; No RDA -- error handler &96FE
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
    cpy #&0c                                                          ; 975f: c0 0c       ..             ; Copied all 12 scout bytes?
    beq scout_complete                                                ; 9761: f0 0a       ..             ; Buffer full (Y=12) -- force completion
    sty port_buf_len                                                  ; 9763: 84 a2       ..             ; Save final buffer offset
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
    sta econet_control1_or_status1                                    ; 976f: 8d a0 fe    ...            ; Write CR1
    lda #&84                                                          ; 9772: a9 84       ..             ; CR2=&84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 9774: 8d a1 fe    ...            ; Write CR2
    lda #2                                                            ; 9777: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9779: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 977c: f0 b5       ..             ; No FV -- not a valid frame end, error
    bpl scout_error                                                   ; 977e: 10 b3       ..             ; FV set but no RDA -- missing last byte, error
    lda econet_data_continue_frame                                    ; 9780: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9783: 99 3d 0d    .=.            ; Store last byte at &0D3D+Y
    lda #&44 ; 'D'                                                    ; 9786: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 9788: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    lda rx_port                                                       ; 978b: ad 40 0d    .@.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 978e: d0 06       ..             ; Port non-zero -- look for matching receive block
    jmp immediate_op                                                  ; 9790: 4c 56 9a    LV.            ; Port = 0 -- immediate operation handler

; &9793 referenced 3 times by &97de, &97e3, &9801
.scout_no_match
    jmp nmi_error_dispatch                                            ; 9793: 4c 72 98    Lr.            ; Port = 0 -- immediate operation handler

; &9796 referenced 1 time by &978e
.scout_match_port
    bit tx_flags                                                      ; 9796: 2c 4a 0d    ,J.            ; Check if broadcast (bit6 of tx_flags)
    bvc scan_port_list                                                ; 9799: 50 05       P.             ; Not broadcast -- skip CR2 setup
    lda #7                                                            ; 979b: a9 07       ..             ; CR2=&07: broadcast prep
    sta econet_control23_or_status2                                   ; 979d: 8d a1 fe    ...            ; Write CR2: broadcast frame prep
; &97a0 referenced 1 time by &9799
.scan_port_list
    bit rx_flags                                                      ; 97a0: 2c 64 0d    ,d.            ; Check if RX port list active (bit7)
    bpl scout_network_match                                           ; 97a3: 10 3b       .;             ; No active ports -- try NFS workspace
    lda #&c0                                                          ; 97a5: a9 c0       ..             ; Start scanning port list at page &C0
.scan_nfs_port_list
    sta port_ws_offset                                                ; 97a7: 85 a6       ..             ; Store page to workspace pointer low
    lda #0                                                            ; 97a9: a9 00       ..             ; A=0: no NFS workspace offset yet
    sta rx_buf_offset                                                 ; 97ab: 85 a7       ..             ; Clear NFS workspace search flag
; &97ad referenced 1 time by &97da
.check_port_slot
    ldy #0                                                            ; 97ad: a0 00       ..             ; Y=0: read control byte from start of slot
; &97af referenced 1 time by &97ed
.scout_ctrl_check
    lda (port_ws_offset),y                                            ; 97af: b1 a6       ..             ; Read port control byte from slot
    beq scout_station_check                                           ; 97b1: f0 29       .)             ; Zero = end of port list, no match
    cmp #&7f                                                          ; 97b3: c9 7f       ..             ; &7F = any-port wildcard
    bne next_port_slot                                                ; 97b5: d0 1c       ..             ; Not wildcard -- check specific port match
    iny                                                               ; 97b7: c8          .              ; Y=1: advance to port byte in slot
    lda (port_ws_offset),y                                            ; 97b8: b1 a6       ..             ; Read port number from slot (offset 1)
    beq check_station_filter                                          ; 97ba: f0 05       ..             ; Zero port in slot = match any port
    cmp rx_port                                                       ; 97bc: cd 40 0d    .@.            ; Check if port matches this slot
    bne next_port_slot                                                ; 97bf: d0 12       ..             ; Port mismatch -- try next slot
; &97c1 referenced 1 time by &97ba
.check_station_filter
    iny                                                               ; 97c1: c8          .              ; Y=2: advance to station byte
    lda (port_ws_offset),y                                            ; 97c2: b1 a6       ..             ; Read station filter from slot (offset 2)
    beq scout_port_match                                              ; 97c4: f0 05       ..             ; Zero station = match any station, accept
    cmp rx_src_stn                                                    ; 97c6: cd 3d 0d    .=.            ; Check if source station matches
    bne next_port_slot                                                ; 97c9: d0 08       ..             ; Station mismatch -- try next slot
; &97cb referenced 1 time by &97c4
.scout_port_match
    iny                                                               ; 97cb: c8          .              ; Y=3: advance to network byte
    lda (port_ws_offset),y                                            ; 97cc: b1 a6       ..             ; Read network filter from slot (offset 3)
    cmp rx_src_net                                                    ; 97ce: cd 3e 0d    .>.            ; Check if source network matches
    beq scout_accept                                                  ; 97d1: f0 1c       ..             ; Network matches or zero = accept
; &97d3 referenced 3 times by &97b5, &97bf, &97c9
.next_port_slot
    lda port_ws_offset                                                ; 97d3: a5 a6       ..             ; Check if NFS workspace search pending
    clc                                                               ; 97d5: 18          .              ; CLC for 12-byte slot advance
    adc #&0c                                                          ; 97d6: 69 0c       i.             ; Advance to next 12-byte port slot
    sta port_ws_offset                                                ; 97d8: 85 a6       ..             ; Update workspace pointer to next slot
    bcc check_port_slot                                               ; 97da: 90 d1       ..             ; Always branches (page &C0 won't overflow)
; &97dc referenced 1 time by &97b1
.scout_station_check
    lda rx_buf_offset                                                 ; 97dc: a5 a7       ..             ; Check if NFS workspace already searched
    bne scout_no_match                                                ; 97de: d0 b3       ..             ; Already searched: no match found
; &97e0 referenced 1 time by &97a3
.scout_network_match
    bit rx_flags                                                      ; 97e0: 2c 64 0d    ,d.            ; Try NFS workspace if paged list exhausted
    bvc scout_no_match                                                ; 97e3: 50 ae       P.             ; No NFS workspace RX (bit6 clear) -- discard
    lda nfs_workspace_hi                                              ; 97e5: a5 9f       ..             ; Get NFS workspace page number
    sta rx_buf_offset                                                 ; 97e7: 85 a7       ..             ; Mark NFS workspace as search target
    ldy #0                                                            ; 97e9: a0 00       ..             ; Y=0: start at offset 0 in workspace
    sty port_ws_offset                                                ; 97eb: 84 a6       ..             ; Reset slot pointer to start
    beq scout_ctrl_check                                              ; 97ed: f0 c0       ..             ; ALWAYS branch

; &97ef referenced 1 time by &97d1
.scout_accept
    bit tx_flags                                                      ; 97ef: 2c 4a 0d    ,J.            ; Check broadcast flag (bit 6)
    bvc ack_scout_match                                               ; 97f2: 50 03       P.             ; Not broadcast: ACK and set up RX
    jmp copy_scout_fields                                             ; 97f4: 4c 47 9a    LG.            ; Broadcast: copy scout fields directly

; &97f7 referenced 2 times by &97f2, &9abb
.ack_scout_match
    lda #3                                                            ; 97f7: a9 03       ..             ; Match found: set scout_status = 3
    sta scout_status                                                  ; 97f9: 8d 5c 0d    .\.            ; Record match for completion handler
    jsr tx_calc_transfer                                              ; 97fc: 20 38 9f     8.            ; Calculate transfer parameters
    bcs send_data_rx_ack                                              ; 97ff: b0 03       ..             ; Transfer OK: send data ACK
    jmp scout_no_match                                                ; 9801: 4c 93 97    L..            ; Broadcast: different completion path

; &9804 referenced 2 times by &97ff, &9ab0
.send_data_rx_ack
    lda #&44 ; 'D'                                                    ; 9804: a9 44       .D             ; CR1=&44: RX_RESET | TIE
    sta econet_control1_or_status1                                    ; 9806: 8d a0 fe    ...            ; Write CR1: TX mode for ACK
    lda #&a7                                                          ; 9809: a9 a7       ..             ; CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE
    sta econet_control23_or_status2                                   ; 980b: 8d a1 fe    ...            ; Write CR2: enable TX with PSE
    lda #&15                                                          ; 980e: a9 15       ..             ; Install data_rx_setup at &97DC
    ldy #&98                                                          ; 9810: a0 98       ..             ; High byte of data_rx_setup handler
    jmp ack_tx_write_dest                                             ; 9812: 4c 5d 99    L].            ; Send ACK with data_rx_setup as next NMI

.data_rx_setup
    lda #&82                                                          ; 9815: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 9817: 8d a0 fe    ...            ; Write CR1: switch to RX for data frame
    lda #&21 ; '!'                                                    ; 981a: a9 21       .!             ; Install nmi_data_rx at &97E6
    ldy #&98                                                          ; 981c: a0 98       ..             ; High byte of nmi_data_rx handler
    jmp set_nmi_vector                                                ; 981e: 4c 0e 0d    L..            ; Install nmi_data_rx and return from NMI

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
    lda #1                                                            ; 9821: a9 01       ..             ; Read SR2 for AP check; A=&01: mask for AP (Address Present)
    bit econet_control23_or_status2                                   ; 9823: 2c a1 fe    ,..            ; BIT SR2: test AP bit
    beq nmi_error_dispatch                                            ; 9826: f0 4a       .J             ; No AP: wrong frame or error
    lda econet_data_continue_frame                                    ; 9828: ad a2 fe    ...            ; Read first byte (dest station)
    cmp station_id_disable_net_nmis                                   ; 982b: cd 18 fe    ...            ; Compare to our station ID (INTOFF)
    bne nmi_error_dispatch                                            ; 982e: d0 42       .B             ; Not for us: error path
    lda #&37 ; '7'                                                    ; 9830: a9 37       .7             ; Install net check handler at &97FA
    ldy #&98                                                          ; 9832: a0 98       ..             ; High byte of nmi_data_rx handler
    jmp set_nmi_vector                                                ; 9834: 4c 0e 0d    L..            ; Set NMI vector via RAM shim

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 9837: 2c a1 fe    ,..            ; Validate source network = 0
    bpl nmi_error_dispatch                                            ; 983a: 10 36       .6             ; SR2 bit7 clear: no data ready -- error
    lda econet_data_continue_frame                                    ; 983c: ad a2 fe    ...            ; Read dest network byte
    bne nmi_error_dispatch                                            ; 983f: d0 31       .1             ; Network != 0: wrong network -- error
    lda #&4d ; 'M'                                                    ; 9841: a9 4d       .M             ; Install skip handler at &9810
    ldy #&98                                                          ; 9843: a0 98       ..             ; High byte of &9810 handler
    bit econet_control1_or_status1                                    ; 9845: 2c a0 fe    ,..            ; SR1 bit7: IRQ, data already waiting
    bmi nmi_data_rx_skip                                              ; 9848: 30 03       0.             ; Data ready: skip directly, no RTI
    jmp set_nmi_vector                                                ; 984a: 4c 0e 0d    L..            ; Install handler and return via RTI

; &984d referenced 1 time by &9848
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 984d: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl nmi_error_dispatch                                            ; 9850: 10 20       .              ; SR2 bit7 clear: error
    lda econet_data_continue_frame                                    ; 9852: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 9855: ad a2 fe    ...            ; Discard port byte
; ***************************************************************************************
; Install data RX bulk or Tube handler
; 
; Selects either the normal bulk RX handler (&9843) or the Tube
; RX handler (&98A0) based on the Tube transfer flag in tx_flags,
; and installs the appropriate NMI handler.
; ***************************************************************************************
; &9858 referenced 1 time by &9f0c
.install_data_rx_handler
    lda #2                                                            ; 9858: a9 02       ..             ; A=2: Tube transfer flag mask
    bit tx_flags                                                      ; 985a: 2c 4a 0d    ,J.            ; Check if Tube transfer active
    bne install_tube_rx                                               ; 985d: d0 0c       ..             ; Tube active: use Tube RX path
    lda #&80                                                          ; 985f: a9 80       ..             ; Install bulk read at &9843
    ldy #&98                                                          ; 9861: a0 98       ..             ; High byte of &9843 handler
    bit econet_control1_or_status1                                    ; 9863: 2c a0 fe    ,..            ; SR1 bit7: more data already waiting?
    bmi nmi_data_rx_bulk                                              ; 9866: 30 18       0.             ; Yes: enter bulk read directly
    jmp set_nmi_vector                                                ; 9868: 4c 0e 0d    L..            ; No: install handler and RTI

; &986b referenced 1 time by &985d
.install_tube_rx
    lda #&dd                                                          ; 986b: a9 dd       ..             ; Tube: install Tube RX at &98A0
    ldy #&98                                                          ; 986d: a0 98       ..             ; High byte of &98A0 handler
    jmp set_nmi_vector                                                ; 986f: 4c 0e 0d    L..            ; Install Tube handler and RTI

; ***************************************************************************************
; NMI error handler dispatch
; 
; Common error/abort entry used by 12 call sites. Checks
; tx_flags bit 7: if clear, does a full ADLC reset and returns
; to idle listen (RX error path); if set, jumps to tx_result_fail
; (TX not-listening path).
; ***************************************************************************************
; &9872 referenced 12 times by &9793, &9826, &982e, &983a, &983f, &9850, &9893, &98c5, &98cb, &9916, &99a1, &9a82
.nmi_error_dispatch
    lda tx_flags                                                      ; 9872: ad 4a 0d    .J.            ; Check tx_flags for error path
    bpl rx_error                                                      ; 9875: 10 03       ..             ; Bit7 clear: RX error path
    jmp tx_result_fail                                                ; 9877: 4c 1a 9f    L..            ; Bit7 set: TX result = not listening

; &987a referenced 1 time by &9875
.rx_error
.rx_error_reset
    jsr adlc_full_reset                                               ; 987a: 20 d8 96     ..            ; Full ADLC reset on RX error
    jmp discard_reset_listen                                          ; 987d: 4c 2e 9a    L..            ; Discard and return to idle listen

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
.data_rx_loop
    bpl data_rx_complete                                              ; 9885: 10 2d       .-             ; SR2 bit7 clear: frame complete (FV)
    lda econet_data_continue_frame                                    ; 9887: ad a2 fe    ...            ; Read first byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 988a: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 988c: c8          .              ; Advance buffer offset
    bne read_sr2_between_pairs                                        ; 988d: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 988f: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 9891: c6 a3       ..             ; Decrement remaining page count
    beq nmi_error_dispatch                                            ; 9893: f0 dd       ..             ; No pages left: handle as complete
; &9895 referenced 1 time by &988d
.read_sr2_between_pairs
    lda econet_control23_or_status2                                   ; 9895: ad a1 fe    ...            ; Read SR2 between byte pairs
    bmi read_second_rx_byte                                           ; 9898: 30 02       0.             ; SR2 bit7 set: more data available
    bne data_rx_complete                                              ; 989a: d0 18       ..             ; SR2 non-zero, bit7 clear: frame done
; &989c referenced 1 time by &9898
.read_second_rx_byte
    lda econet_data_continue_frame                                    ; 989c: ad a2 fe    ...            ; Read second byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 989f: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 98a1: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 98a2: 84 a2       ..             ; Save updated buffer position
    bne check_sr2_loop_again                                          ; 98a4: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 98a6: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 98a8: c6 a3       ..             ; Decrement remaining page count
    beq data_rx_complete                                              ; 98aa: f0 08       ..             ; No pages left: frame complete
; &98ac referenced 1 time by &98a4
.check_sr2_loop_again
    lda econet_control23_or_status2                                   ; 98ac: ad a1 fe    ...            ; Read SR2 for next iteration
    bne data_rx_loop                                                  ; 98af: d0 d4       ..             ; SR2 non-zero: more data, loop back
    jmp nmi_rti                                                       ; 98b1: 4c 14 0d    L..            ; SR2=0: no more data yet, wait for NMI

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
    lda #0                                                            ; 98b4: a9 00       ..             ; CR1=&00: disable all interrupts; CR2=&84: disable PSE for individual bit testing
    sta econet_control1_or_status1                                    ; 98b6: 8d a0 fe    ...            ; Write CR2: disable PSE for bit testing
    lda #&84                                                          ; 98b9: a9 84       ..             ; CR2=&84: disable PSE for individual bit testing; CR1=&00: disable all interrupts
    sta econet_control23_or_status2                                   ; 98bb: 8d a1 fe    ...            ; Write CR1: disable all interrupts
    sty port_buf_len                                                  ; 98be: 84 a2       ..             ; Save Y (byte count from data RX loop)
    lda #2                                                            ; 98c0: a9 02       ..             ; A=&02: FV mask
    bit econet_control23_or_status2                                   ; 98c2: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq nmi_error_dispatch                                            ; 98c5: f0 ab       ..             ; No FV -- error
    bpl send_ack                                                      ; 98c7: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 98c9: a5 a3       ..             ; Check if buffer space remains
.read_last_rx_byte
    beq nmi_error_dispatch                                            ; 98cb: f0 a5       ..             ; No buffer space: error/discard frame
    lda econet_data_continue_frame                                    ; 98cd: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 98d0: a4 a2       ..             ; Y = current buffer write offset
    sta (open_port_buf),y                                             ; 98d2: 91 a4       ..             ; Store last byte in port receive buffer
    inc port_buf_len                                                  ; 98d4: e6 a2       ..             ; Advance buffer write offset
    bne send_ack                                                      ; 98d6: d0 02       ..             ; No page wrap: proceed to send ACK
    inc open_port_buf_hi                                              ; 98d8: e6 a5       ..             ; Page boundary: advance buffer page
; &98da referenced 2 times by &98c7, &98d6
.send_ack
    jmp ack_tx                                                        ; 98da: 4c 44 99    LD.            ; Send ACK frame to complete handshake

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 98dd: ad a1 fe    ...            ; Read SR2 for Tube data receive path
; &98e0 referenced 1 time by &9911
.rx_tube_data
    bpl data_rx_tube_complete                                         ; 98e0: 10 37       .7             ; RDA clear: no more data, frame complete
    lda econet_data_continue_frame                                    ; 98e2: ad a2 fe    ...            ; Read data byte from ADLC RX FIFO
    inc port_buf_len                                                  ; 98e5: e6 a2       ..             ; Advance Tube transfer byte count
    sta tube_data_register_3                                          ; 98e7: 8d e5 fe    ...            ; Send byte to Tube data register 3
    bne rx_update_buf                                                 ; 98ea: d0 0c       ..             ; No overflow: read second byte
    inc port_buf_len_hi                                               ; 98ec: e6 a3       ..             ; Carry to transfer count byte 2
    bne rx_update_buf                                                 ; 98ee: d0 08       ..             ; No overflow: read second byte
    inc open_port_buf                                                 ; 98f0: e6 a4       ..             ; Carry to transfer count byte 3
    bne rx_update_buf                                                 ; 98f2: d0 04       ..             ; No overflow: read second byte
    inc open_port_buf_hi                                              ; 98f4: e6 a5       ..             ; Carry to transfer count byte 4
    beq data_rx_tube_error                                            ; 98f6: f0 1e       ..             ; All bytes zero: overflow error
; &98f8 referenced 3 times by &98ea, &98ee, &98f2
.rx_update_buf
    lda econet_data_continue_frame                                    ; 98f8: ad a2 fe    ...            ; Read second data byte (paired transfer)
    sta tube_data_register_3                                          ; 98fb: 8d e5 fe    ...            ; Send second byte to Tube
    inc port_buf_len                                                  ; 98fe: e6 a2       ..             ; Advance count after second byte
    bne rx_check_error                                                ; 9900: d0 0c       ..             ; No overflow: check for more data
    inc port_buf_len_hi                                               ; 9902: e6 a3       ..             ; Carry to count byte 2
    bne rx_check_error                                                ; 9904: d0 08       ..             ; No overflow: check for more data
    inc open_port_buf                                                 ; 9906: e6 a4       ..             ; Carry to count byte 3
    bne rx_check_error                                                ; 9908: d0 04       ..             ; No overflow: check for more data
    inc open_port_buf_hi                                              ; 990a: e6 a5       ..             ; Carry to count byte 4
    beq data_rx_tube_complete                                         ; 990c: f0 0b       ..             ; Zero: Tube transfer complete
; &990e referenced 3 times by &9900, &9904, &9908
.rx_check_error
    lda econet_control23_or_status2                                   ; 990e: ad a1 fe    ...            ; Re-read SR2 for next byte pair
    bne rx_tube_data                                                  ; 9911: d0 cd       ..             ; More data available: continue loop
    jmp nmi_rti                                                       ; 9913: 4c 14 0d    L..            ; Return from NMI, wait for data

; &9916 referenced 3 times by &98f6, &9928, &9934
.data_rx_tube_error
    jmp nmi_error_dispatch                                            ; 9916: 4c 72 98    Lr.            ; Unexpected end: return from NMI

; &9919 referenced 2 times by &98e0, &990c
.data_rx_tube_complete
    lda #0                                                            ; 9919: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 991b: 8d a0 fe    ...            ; Write CR1 for individual bit testing
    lda #&84                                                          ; 991e: a9 84       ..             ; CR2=&84: disable PSE
    sta econet_control23_or_status2                                   ; 9920: 8d a1 fe    ...            ; Write CR2: same pattern as main path
    lda #2                                                            ; 9923: a9 02       ..             ; A=&02: FV mask for Tube completion
    bit econet_control23_or_status2                                   ; 9925: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq data_rx_tube_error                                            ; 9928: f0 ec       ..             ; No FV: incomplete frame, error
    bpl ack_tx                                                        ; 992a: 10 18       ..             ; FV set, no RDA: proceed to ACK
    lda port_buf_len                                                  ; 992c: a5 a2       ..             ; Check if any buffer was allocated
    ora port_buf_len_hi                                               ; 992e: 05 a3       ..             ; OR all 4 buffer pointer bytes together
    ora open_port_buf                                                 ; 9930: 05 a4       ..             ; Check buffer low byte
    ora open_port_buf_hi                                              ; 9932: 05 a5       ..             ; Check buffer high byte
    beq data_rx_tube_error                                            ; 9934: f0 e0       ..             ; All zero (null buffer): error
    lda econet_data_continue_frame                                    ; 9936: ad a2 fe    ...            ; Read extra trailing byte from FIFO
    sta rx_extra_byte                                                 ; 9939: 8d 5d 0d    .].            ; Save extra byte at &0D5D for later use
    lda #&20 ; ' '                                                    ; 993c: a9 20       .              ; Bit5 = extra data byte available flag
    ora tx_flags                                                      ; 993e: 0d 4a 0d    .J.            ; Set extra byte flag in tx_flags
    sta tx_flags                                                      ; 9941: 8d 4a 0d    .J.            ; Store updated flags
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
    lda tx_flags                                                      ; 9944: ad 4a 0d    .J.            ; Load TX flags to check ACK type
    bpl ack_tx_configure                                              ; 9947: 10 06       ..             ; Bit7 clear: normal scout ACK
    jsr advance_rx_buffer_ptr                                         ; 9949: 20 a4 99     ..            ; Final ACK: call completion handler
    jmp tx_result_ok                                                  ; 994c: 4c 16 9f    L..            ; Jump to TX success result

; &994f referenced 1 time by &9947
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 994f: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 9951: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    lda #&a7                                                          ; 9954: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9956: 8d a1 fe    ...            ; Write CR2: enable TX with status clear
    lda #&e8                                                          ; 9959: a9 e8       ..             ; Install saved next handler (&99BB for scout ACK); Save &9995 (post-ACK port check) in &0D4B/&0D4C
    ldy #&99                                                          ; 995b: a0 99       ..             ; High byte of post-ACK handler
; &995d referenced 2 times by &9812, &9af9
.ack_tx_write_dest
    sta nmi_next_lo                                                   ; 995d: 8d 4b 0d    .K.            ; Store next handler low byte
    sty nmi_next_hi                                                   ; 9960: 8c 4c 0d    .L.            ; Store next handler high byte
    lda rx_src_stn                                                    ; 9963: ad 3d 0d    .=.            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 9966: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc dispatch_nmi_error                                            ; 9969: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 996b: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda rx_src_net                                                    ; 996e: ad 3e 0d    .>.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9971: 8d a2 fe    ...            ; Write dest net byte to FIFO
    lda #&7b ; '{'                                                    ; 9974: a9 7b       .{             ; Install handler at &9992 (write src addr); Install nmi_ack_tx_src at &9925
    ldy #&99                                                          ; 9976: a0 99       ..             ; High byte of nmi_ack_tx_src
    jmp set_nmi_vector                                                ; 9978: 4c 0e 0d    L..            ; Set NMI vector to ack_tx_src handler

; ***************************************************************************************
; ACK TX continuation
; 
; Writes source station and network to TX FIFO, completing the 4-byte
; ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 997b: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 997e: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc dispatch_nmi_error                                            ; 9981: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9983: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9986: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 9988: 8d a2 fe    ...            ; Write network=0 (local) to TX FIFO
    lda tx_flags                                                      ; 998b: ad 4a 0d    .J.            ; Check tx_flags for data phase
    bmi start_data_tx                                                 ; 998e: 30 0e       0.             ; bit7 set: start data TX phase
    lda #&3f ; '?'                                                    ; 9990: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | PSE
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
    sta econet_control23_or_status2                                   ; 9992: 8d a1 fe    ...            ; Write CR2 to clear status after ACK TX
    lda nmi_next_lo                                                   ; 9995: ad 4b 0d    .K.            ; Install saved handler from &0D4B/&0D4C; Load saved next handler low byte
    ldy nmi_next_hi                                                   ; 9998: ac 4c 0d    .L.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 999b: 4c 0e 0d    L..            ; Install next NMI handler

; &999e referenced 1 time by &998e
.start_data_tx
    jmp data_tx_begin                                                 ; 999e: 4c 1a 9e    L..            ; Jump to start data TX phase

; &99a1 referenced 2 times by &9969, &9981
.dispatch_nmi_error
    jmp nmi_error_dispatch                                            ; 99a1: 4c 72 98    Lr.            ; Jump to error handler

; ***************************************************************************************
; Advance RX buffer pointer after transfer
; 
; Adds the transfer count to the RXCB buffer pointer (4-byte
; addition). If a Tube transfer is active, re-claims the Tube
; address and sends the extra RX byte via R3, incrementing the
; Tube pointer by 1.
; ***************************************************************************************
; &99a4 referenced 2 times by &9949, &99f7
.advance_rx_buffer_ptr
    lda #2                                                            ; 99a4: a9 02       ..             ; A=2: test bit1 of tx_flags
    bit tx_flags                                                      ; 99a6: 2c 4a 0d    ,J.            ; BIT tx_flags: check data transfer bit
    beq return_10                                                     ; 99a9: f0 3c       .<             ; Bit1 clear: no transfer -- return
    clc                                                               ; 99ab: 18          .              ; CLC: init carry for 4-byte add
    php                                                               ; 99ac: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 99ad: a0 08       ..             ; Y=8: RXCB high pointer offset
; &99af referenced 1 time by &99bb
.add_rxcb_ptr
    lda (port_ws_offset),y                                            ; 99af: b1 a6       ..             ; Load RXCB[Y] (buffer pointer byte)
    plp                                                               ; 99b1: 28          (              ; Restore carry from stack
    adc net_tx_ptr,y                                                  ; 99b2: 79 9a 00    y..            ; Add transfer count byte
    sta (port_ws_offset),y                                            ; 99b5: 91 a6       ..             ; Store updated pointer back to RXCB
    iny                                                               ; 99b7: c8          .              ; Next byte
    php                                                               ; 99b8: 08          .              ; Save carry for next iteration
    cpy #&0c                                                          ; 99b9: c0 0c       ..             ; Done 4 bytes? (Y reaches &0C)
    bcc add_rxcb_ptr                                                  ; 99bb: 90 f2       ..             ; No: continue adding
    plp                                                               ; 99bd: 28          (              ; Discard final carry
    lda #&20 ; ' '                                                    ; 99be: a9 20       .              ; A=&20: test bit5 of tx_flags
    bit tx_flags                                                      ; 99c0: 2c 4a 0d    ,J.            ; BIT tx_flags: check Tube bit
    beq skip_tube_update                                              ; 99c3: f0 20       .              ; No Tube: skip Tube update
    txa                                                               ; 99c5: 8a          .              ; Save X on stack
    pha                                                               ; 99c6: 48          H              ; Push X
    lda #8                                                            ; 99c7: a9 08       ..             ; A=8: offset for Tube address
    clc                                                               ; 99c9: 18          .              ; CLC for address calculation
    adc port_ws_offset                                                ; 99ca: 65 a6       e.             ; Add workspace base offset
    tax                                                               ; 99cc: aa          .              ; X = address low for Tube claim
    ldy rx_buf_offset                                                 ; 99cd: a4 a7       ..             ; Y = address high for Tube claim
    lda #1                                                            ; 99cf: a9 01       ..             ; A=1: Tube claim type (read)
    jsr tube_addr_claim                                               ; 99d1: 20 06 04     ..            ; Claim Tube address for transfer
    lda rx_extra_byte                                                 ; 99d4: ad 5d 0d    .].            ; Load extra RX data byte
    sta tube_data_register_3                                          ; 99d7: 8d e5 fe    ...            ; Send to Tube via R3
    pla                                                               ; 99da: 68          h              ; Restore X from stack
    tax                                                               ; 99db: aa          .              ; Transfer to X register
    ldy #8                                                            ; 99dc: a0 08       ..             ; Y=8: RXCB buffer ptr offset
    lda (port_ws_offset),y                                            ; 99de: b1 a6       ..             ; Load current RXCB buffer ptr lo
    sec                                                               ; 99e0: 38          8              ; SEC for ADC #0 = add carry
    adc #0                                                            ; 99e1: 69 00       i.             ; Increment by 1 (Tube extra byte)
    sta (port_ws_offset),y                                            ; 99e3: 91 a6       ..             ; Store updated ptr back to RXCB
; &99e5 referenced 1 time by &99c3
.skip_tube_update
    lda #&ff                                                          ; 99e5: a9 ff       ..             ; A=&FF: return value (transfer done)
; &99e7 referenced 1 time by &99a9
.return_10
    rts                                                               ; 99e7: 60          `              ; Return

    lda rx_port                                                       ; 99e8: ad 40 0d    .@.            ; Load received port byte
    bne rx_complete_update_rxcb                                       ; 99eb: d0 0a       ..             ; Port != 0: data transfer frame
    ldy rx_ctrl                                                       ; 99ed: ac 3f 0d    .?.            ; Port=0: load control byte
    cpy #&82                                                          ; 99f0: c0 82       ..             ; Ctrl = &82 (POKE)?
    beq rx_complete_update_rxcb                                       ; 99f2: f0 03       ..             ; Yes: POKE also needs data transfer
    jmp imm_op_build_reply                                            ; 99f4: 4c fc 9a    L..            ; Other port-0 ops: immediate dispatch

; &99f7 referenced 2 times by &99eb, &99f2
.rx_complete_update_rxcb
    jsr advance_rx_buffer_ptr                                         ; 99f7: 20 a4 99     ..            ; Update buffer pointer and check for Tube
    bne skip_buf_ptr_update                                           ; 99fa: d0 12       ..             ; Transfer not done: skip buffer update
.add_buf_to_base
    lda port_buf_len                                                  ; 99fc: a5 a2       ..             ; Load buffer bytes remaining
    clc                                                               ; 99fe: 18          .              ; CLC for address add
    adc open_port_buf                                                 ; 99ff: 65 a4       e.             ; Add to buffer base address
    bcc store_buf_ptr_lo                                              ; 9a01: 90 02       ..             ; No carry: skip high byte increment
.inc_rxcb_buf_hi
imm_dispatch_lo = inc_rxcb_buf_hi+1
    inc open_port_buf_hi                                              ; 9a03: e6 a5       ..             ; Carry: increment buffer high byte
; &9a04 referenced 1 time by &9a7d
; &9a05 referenced 1 time by &9a01
.store_buf_ptr_lo
    ldy #8                                                            ; 9a05: a0 08       ..             ; Y=8: store updated buffer position
.store_rxcb_buf_ptr
    sta (port_ws_offset),y                                            ; 9a07: 91 a6       ..             ; Store updated low byte to RXCB
    iny                                                               ; 9a09: c8          .              ; Y=9: buffer high byte offset
    lda open_port_buf_hi                                              ; 9a0a: a5 a5       ..             ; Load updated buffer high byte
; &9a0c referenced 1 time by &9a79
.store_rxcb_buf_hi
    sta (port_ws_offset),y                                            ; 9a0c: 91 a6       ..             ; Store high byte to RXCB
; &9a0e referenced 2 times by &99fa, &9a53
.skip_buf_ptr_update
    lda rx_port                                                       ; 9a0e: ad 40 0d    .@.            ; Check port byte again
    beq discard_reset_listen                                          ; 9a11: f0 1b       ..             ; Port=0: immediate op, discard+listen
    lda rx_src_net                                                    ; 9a13: ad 3e 0d    .>.            ; Load source network from scout buffer
    ldy #3                                                            ; 9a16: a0 03       ..             ; Y=3: RXCB source network offset
    sta (port_ws_offset),y                                            ; 9a18: 91 a6       ..             ; Store source network to RXCB
    dey                                                               ; 9a1a: 88          .              ; Y=2: source station offset; Y=&02
    lda rx_src_stn                                                    ; 9a1b: ad 3d 0d    .=.            ; Load source station from scout buffer
    sta (port_ws_offset),y                                            ; 9a1e: 91 a6       ..             ; Store source station to RXCB
    dey                                                               ; 9a20: 88          .              ; Y=1: port byte offset; Y=&01
    lda rx_port                                                       ; 9a21: ad 40 0d    .@.            ; Load port byte
    sta (port_ws_offset),y                                            ; 9a24: 91 a6       ..             ; Store port to RXCB
    dey                                                               ; 9a26: 88          .              ; Y=0: control/flag byte offset; Y=&00
    lda rx_ctrl                                                       ; 9a27: ad 3f 0d    .?.            ; Load control byte from scout
    ora #&80                                                          ; 9a2a: 09 80       ..             ; Set bit7 = reception complete flag
    sta (port_ws_offset),y                                            ; 9a2c: 91 a6       ..             ; Store to RXCB (marks CB as complete)
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
    lda #2                                                            ; 9a2e: a9 02       ..             ; Tube flag bit 1 AND tx_flags bit 1
    and tube_flag                                                     ; 9a30: 2d 67 0d    -g.            ; Check if Tube transfer active
    bit tx_flags                                                      ; 9a33: 2c 4a 0d    ,J.            ; Test tx_flags for Tube transfer
    beq discard_listen                                                ; 9a36: f0 05       ..             ; No Tube transfer active -- skip release
    lda #&82                                                          ; 9a38: a9 82       ..             ; A=&82: Tube release claim type
    jsr tube_addr_claim                                               ; 9a3a: 20 06 04     ..            ; Release Tube claim before discarding
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
    jsr adlc_rx_listen                                                ; 9a3d: 20 e7 96     ..            ; Re-enter idle RX listen mode
; ***************************************************************************************
; Install RX scout NMI handler
; 
; Installs nmi_rx_scout (&96BF) as the NMI handler via
; set_nmi_vector, without first calling adlc_rx_listen.
; Used when the ADLC is already in the correct RX mode.
; ***************************************************************************************
; &9a40 referenced 2 times by &9724, &973d
.install_rx_scout_handler
    lda #&f2                                                          ; 9a40: a9 f2       ..             ; Install nmi_rx_scout (&96BF) as NMI handler
    ldy #&96                                                          ; 9a42: a0 96       ..             ; High byte of nmi_rx_scout
    jmp set_nmi_vector                                                ; 9a44: 4c 0e 0d    L..            ; Set NMI vector and return

; &9a47 referenced 1 time by &97f4
.copy_scout_fields
    ldy #4                                                            ; 9a47: a0 04       ..             ; Y=4: start at RX CB offset 4
; &9a49 referenced 1 time by &9a51
.copy_scout_loop
    lda rx_src_stn,y                                                  ; 9a49: b9 3d 0d    .=.            ; Load scout field (stn/net/ctrl/port)
    sta (port_ws_offset),y                                            ; 9a4c: 91 a6       ..             ; Store to port workspace buffer; Store to port buffer
    iny                                                               ; 9a4e: c8          .              ; Next field; Advance buffer pointer
    cpy #&0c                                                          ; 9a4f: c0 0c       ..             ; All 8 fields copied?
    bne copy_scout_loop                                               ; 9a51: d0 f6       ..             ; No: continue copy loop; No page crossing
    jmp skip_buf_ptr_update                                           ; 9a53: 4c 0e 9a    L..            ; Skip buffer pointer update; Jump to completion handler

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
    ldy rx_ctrl                                                       ; 9a56: ac 3f 0d    .?.            ; Control byte &81-&88 range check
    cpy #&81                                                          ; 9a59: c0 81       ..             ; Below &81: not an immediate op
    bcc imm_op_out_of_range                                           ; 9a5b: 90 25       .%             ; Out of range low: jump to discard
    cpy #&89                                                          ; 9a5d: c0 89       ..             ; Above &88: not an immediate op
    bcs imm_op_out_of_range                                           ; 9a5f: b0 21       .!             ; Out of range high: jump to discard
    cpy #&87                                                          ; 9a61: c0 87       ..             ; HALT(&87)/CONTINUE(&88) skip protection
    bcs imm_op_dispatch                                               ; 9a63: b0 11       ..             ; Ctrl >= &87: dispatch without mask check
    tya                                                               ; 9a65: 98          .              ; Convert ctrl byte to 0-based index for mask
    sec                                                               ; 9a66: 38          8              ; SEC for subtract
    sbc #&81                                                          ; 9a67: e9 81       ..             ; A = ctrl - &81 (0-based operation index)
    tay                                                               ; 9a69: a8          .              ; Y = index for mask rotation count
    lda prot_status                                                   ; 9a6a: ad 63 0d    .c.            ; Load protection mask from LSTAT
; &9a6d referenced 1 time by &9a6f
.rotate_prot_mask
    ror a                                                             ; 9a6d: 6a          j              ; Rotate mask right by control byte index
    dey                                                               ; 9a6e: 88          .              ; Decrement rotation counter
    bpl rotate_prot_mask                                              ; 9a6f: 10 fc       ..             ; Loop until bit aligned
    bcc imm_op_dispatch                                               ; 9a71: 90 03       ..             ; Carry clear: operation permitted
    jmp imm_op_discard                                                ; 9a73: 4c 32 9b    L2.            ; Operation blocked by LSTAT mask

; &9a76 referenced 2 times by &9a63, &9a71
.imm_op_dispatch
    ldy rx_ctrl                                                       ; 9a76: ac 3f 0d    .?.            ; Reload ctrl byte for dispatch table
    lda store_rxcb_buf_hi,y                                           ; 9a79: b9 0c 9a    ...            ; Look up handler address high byte
    pha                                                               ; 9a7c: 48          H              ; Push &9A as dispatch high byte; Push handler address high
    lda imm_dispatch_lo,y                                             ; 9a7d: b9 04 9a    ...            ; Load handler low byte from jump table; Look up handler address low byte
    pha                                                               ; 9a80: 48          H              ; Push handler low byte; Push handler address low
    rts                                                               ; 9a81: 60          `              ; RTS dispatches to handler; RTS dispatch to handler

; &9a82 referenced 2 times by &9a5b, &9a5f
.imm_op_out_of_range
    jmp nmi_error_dispatch                                            ; 9a82: 4c 72 98    Lr.            ; Jump to discard handler

    equb <(rx_imm_peek-1)                                             ; 9a85: d0          .
    equb <(rx_imm_poke-1)                                             ; 9a86: b2          .
    equb <(rx_imm_exec-1)                                             ; 9a87: 94          .
    equb <(rx_imm_exec-1)                                             ; 9a88: 94          .
    equb <(rx_imm_exec-1)                                             ; 9a89: 94          .
    equb <(rx_imm_halt_cont-1)                                        ; 9a8a: ea          .
    equb <(rx_imm_halt_cont-1)                                        ; 9a8b: ea          .
    equb <(rx_imm_machine_type-1)                                     ; 9a8c: bd          .
    equb >(rx_imm_peek-1)                                             ; 9a8d: 9a          .
    equb >(rx_imm_poke-1)                                             ; 9a8e: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a8f: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a90: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a91: 9a          .
    equb >(rx_imm_halt_cont-1)                                        ; 9a92: 9a          .
    equb >(rx_imm_halt_cont-1)                                        ; 9a93: 9a          .
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
    lda #0                                                            ; 9a95: a9 00       ..             ; Buffer start lo = &00
    sta open_port_buf                                                 ; 9a97: 85 a4       ..             ; Set port buffer lo
    lda #&82                                                          ; 9a99: a9 82       ..             ; Buffer length lo = &82
    sta port_buf_len                                                  ; 9a9b: 85 a2       ..             ; Set buffer length lo
    lda #1                                                            ; 9a9d: a9 01       ..             ; Buffer length hi = 1
    sta port_buf_len_hi                                               ; 9a9f: 85 a3       ..             ; Set buffer length hi
    lda net_rx_ptr_hi                                                 ; 9aa1: a5 9d       ..             ; Load RX page hi for buffer
    sta open_port_buf_hi                                              ; 9aa3: 85 a5       ..             ; Set port buffer hi
    ldy #3                                                            ; 9aa5: a0 03       ..             ; Y=3: copy 4 bytes (3 down to 0)
; &9aa7 referenced 1 time by &9aae
.copy_addr_loop
    lda rx_remote_addr,y                                              ; 9aa7: b9 41 0d    .A.            ; Load remote address byte
    sta l0d58,y                                                       ; 9aaa: 99 58 0d    .X.            ; Store to exec address workspace
    dey                                                               ; 9aad: 88          .              ; Next byte (descending)
    bpl copy_addr_loop                                                ; 9aae: 10 f7       ..             ; Loop until all 4 bytes copied
    jmp send_data_rx_ack                                              ; 9ab0: 4c 04 98    L..            ; Enter common data-receive path

; ***************************************************************************************
; RX immediate: POKE setup
; 
; Sets up workspace offsets for receiving POKE data.
; port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
; the common data-receive path at c9805.
; ***************************************************************************************
.rx_imm_poke
    lda #&3d ; '='                                                    ; 9ab3: a9 3d       .=             ; Port workspace offset = &3D
    sta port_ws_offset                                                ; 9ab5: 85 a6       ..             ; Store workspace offset lo
    lda #&0d                                                          ; 9ab7: a9 0d       ..             ; RX buffer page = &0D
    sta rx_buf_offset                                                 ; 9ab9: 85 a7       ..             ; Store workspace offset hi
    jmp ack_scout_match                                               ; 9abb: 4c f7 97    L..            ; Enter POKE data-receive path

; ***************************************************************************************
; RX immediate: machine type query
; 
; Sets up a buffer at &7F21 (length #&01FC) for the machine
; type query response, then jumps to the query handler at
; c9b0f. Returns system identification data to the remote
; station.
; ***************************************************************************************
.rx_imm_machine_type
    lda #1                                                            ; 9abe: a9 01       ..             ; Buffer length hi = 1
    sta port_buf_len_hi                                               ; 9ac0: 85 a3       ..             ; Set buffer length hi
    lda #&fc                                                          ; 9ac2: a9 fc       ..             ; Buffer length lo = &FC
    sta port_buf_len                                                  ; 9ac4: 85 a2       ..             ; Set buffer length lo
    lda #&25 ; '%'                                                    ; 9ac6: a9 25       .%             ; Buffer start lo = &25
    sta open_port_buf                                                 ; 9ac8: 85 a4       ..             ; Set port buffer lo
    lda #&7f                                                          ; 9aca: a9 7f       ..             ; Buffer hi = &7F (below screen)
    sta open_port_buf_hi                                              ; 9acc: 85 a5       ..             ; Set port buffer hi
    jmp set_tx_reply_flag                                             ; 9ace: 4c e3 9a    L..            ; Enter reply build path

; ***************************************************************************************
; RX immediate: PEEK setup
; 
; Writes &0D3D to port_ws_offset/rx_buf_offset, sets
; scout_status=2, then calls tx_calc_transfer to send the
; PEEK response data back to the requesting station.
; Uses workspace offsets (&A6/&A7) for nmi_tx_block.
; ***************************************************************************************
.rx_imm_peek
    lda #&3d ; '='                                                    ; 9ad1: a9 3d       .=             ; Port workspace offset = &3D
    sta port_ws_offset                                                ; 9ad3: 85 a6       ..             ; Store workspace offset lo
    lda #&0d                                                          ; 9ad5: a9 0d       ..             ; RX buffer page = &0D
    sta rx_buf_offset                                                 ; 9ad7: 85 a7       ..             ; Store workspace offset hi
    lda #2                                                            ; 9ad9: a9 02       ..             ; Scout status = 2 (PEEK response)
    sta scout_status                                                  ; 9adb: 8d 5c 0d    .\.            ; Store scout status
    jsr tx_calc_transfer                                              ; 9ade: 20 38 9f     8.            ; Calculate transfer size for response
    bcc imm_op_discard                                                ; 9ae1: 90 4f       .O             ; C=0: transfer not set up, discard
; &9ae3 referenced 1 time by &9ace
.set_tx_reply_flag
    lda tx_flags                                                      ; 9ae3: ad 4a 0d    .J.            ; Mark TX flags bit 7 (reply pending)
    ora #&80                                                          ; 9ae6: 09 80       ..             ; Set reply pending flag
    sta tx_flags                                                      ; 9ae8: 8d 4a 0d    .J.            ; Store updated TX flags
.rx_imm_halt_cont
    lda #&44 ; 'D'                                                    ; 9aeb: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    sta econet_control1_or_status1                                    ; 9aed: 8d a0 fe    ...            ; Write CR1: enable TX interrupts
.tx_cr2_setup
tx_done_handler_lo = tx_cr2_setup+1
    lda #&a7                                                          ; 9af0: a9 a7       ..             ; NMI handler hi byte (self-modifying)
; &9af1 referenced 1 time by &9b6f
    sta econet_control23_or_status2                                   ; 9af2: 8d a1 fe    ...            ; Write CR2 for TX setup
.tx_nmi_setup
tx_done_handler_hi = tx_nmi_setup+1
    lda #&12                                                          ; 9af5: a9 12       ..             ; NMI handler lo byte (self-modifying)
; &9af6 referenced 1 time by &9b6b
    ldy #&9b                                                          ; 9af7: a0 9b       ..             ; Y=&9B: dispatch table page
    jmp ack_tx_write_dest                                             ; 9af9: 4c 5d 99    L].            ; Acknowledge and write TX dest

; ***************************************************************************************
; Build immediate operation reply header
; 
; Stores data length, source station/network, and control byte
; into the RX buffer header area for port-0 immediate operations.
; Then disables CB1 interrupts and configures the VIA shift
; register for outgoing shift-out mode before returning to
; idle listen.
; ***************************************************************************************
; &9afc referenced 1 time by &99f4
.imm_op_build_reply
    lda port_buf_len                                                  ; 9afc: a5 a2       ..             ; Get buffer position for reply header
    clc                                                               ; 9afe: 18          .              ; Clear carry for offset addition
    adc #&80                                                          ; 9aff: 69 80       i.             ; Data offset = buf_len + &80 (past header)
    ldy #&7f                                                          ; 9b01: a0 7f       ..             ; Y=&7F: reply data length slot
    sta (net_rx_ptr),y                                                ; 9b03: 91 9c       ..             ; Store reply data length in RX buffer
    ldy #&80                                                          ; 9b05: a0 80       ..             ; Y=&80: source station slot
    lda rx_src_stn                                                    ; 9b07: ad 3d 0d    .=.            ; Load requesting station number
    sta (net_rx_ptr),y                                                ; 9b0a: 91 9c       ..             ; Store source station in reply header
    iny                                                               ; 9b0c: c8          .              ; Y=&81
    lda rx_src_net                                                    ; 9b0d: ad 3e 0d    .>.            ; Load requesting network number
    sta (net_rx_ptr),y                                                ; 9b10: 91 9c       ..             ; Store source network in reply header
    lda rx_ctrl                                                       ; 9b12: ad 3f 0d    .?.            ; Load control byte from received frame
    sta tx_work_57                                                    ; 9b15: 8d 57 0d    .W.            ; Save ctrl byte for TX response
    lda #&84                                                          ; 9b18: a9 84       ..             ; IER bit 2: disable CB1 interrupt
    sta system_via_ier                                                ; 9b1a: 8d 4e fe    .N.            ; Write IER to disable CB1
    lda system_via_acr                                                ; 9b1d: ad 4b fe    .K.            ; Read ACR for shift register config
    and #&1c                                                          ; 9b20: 29 1c       ).             ; Isolate shift register mode bits (2-4)
    sta tx_work_51                                                    ; 9b22: 8d 51 0d    .Q.            ; Save original SR mode for later restore
    lda system_via_acr                                                ; 9b25: ad 4b fe    .K.            ; Reload ACR for modification
    and #&e3                                                          ; 9b28: 29 e3       ).             ; Clear SR mode bits (keep other bits)
    ora #8                                                            ; 9b2a: 09 08       ..             ; SR mode 4: shift out under CB1 control
    sta system_via_acr                                                ; 9b2c: 8d 4b fe    .K.            ; Apply new shift register mode
    bit system_via_sr                                                 ; 9b2f: 2c 4a fe    ,J.            ; Read SR to clear pending interrupt
; &9b32 referenced 2 times by &9a73, &9ae1
.imm_op_discard
    jmp discard_listen                                                ; 9b32: 4c 3d 9a    L=.            ; Return to idle listen mode

; &9b35 referenced 1 time by &966c
.check_cb1_irq
    lda #4                                                            ; 9b35: a9 04       ..             ; A=&04: IFR bit 2 (CB1) mask
    bit system_via_ifr                                                ; 9b37: 2c 4d fe    ,M.            ; Test CB1 interrupt pending
    bne tx_done_error                                                 ; 9b3a: d0 03       ..             ; CB1 fired: handle TX completion
    lda #5                                                            ; 9b3c: a9 05       ..             ; A=5: no CB1, return status 5
    rts                                                               ; 9b3e: 60          `              ; Return (no CB1 interrupt)

; &9b3f referenced 1 time by &9b3a
.tx_done_error
    txa                                                               ; 9b3f: 8a          .              ; Save X
    pha                                                               ; 9b40: 48          H              ; Push X
    tya                                                               ; 9b41: 98          .              ; Save Y
    pha                                                               ; 9b42: 48          H              ; Push Y
    lda system_via_acr                                                ; 9b43: ad 4b fe    .K.            ; Read ACR for shift register mode
    and #&e3                                                          ; 9b46: 29 e3       ).             ; Clear SR mode bits (2-4)
    ora tx_work_51                                                    ; 9b48: 0d 51 0d    .Q.            ; Restore original SR mode
    sta system_via_acr                                                ; 9b4b: 8d 4b fe    .K.            ; Write updated ACR
    lda system_via_sr                                                 ; 9b4e: ad 4a fe    .J.            ; Read SR to clear pending interrupt
    lda #4                                                            ; 9b51: a9 04       ..             ; A=&04: CB1 bit mask
    sta system_via_ifr                                                ; 9b53: 8d 4d fe    .M.            ; Clear CB1 in IFR
    sta system_via_ier                                                ; 9b56: 8d 4e fe    .N.            ; Disable CB1 in IER
    ldy tx_work_57                                                    ; 9b59: ac 57 0d    .W.            ; Load ctrl byte for dispatch
    cpy #&86                                                          ; 9b5c: c0 86       ..             ; Ctrl >= &86? (HALT/CONTINUE)
    bcs tx_done_classify                                              ; 9b5e: b0 0b       ..             ; Yes: skip protection mask save
    lda prot_status                                                   ; 9b60: ad 63 0d    .c.            ; Load current protection mask
    sta saved_jsr_mask                                                ; 9b63: 8d 65 0d    .e.            ; Save mask before JSR modification
    ora #&1c                                                          ; 9b66: 09 1c       ..             ; Enable bits 2-4 (allow JSR ops)
    sta prot_status                                                   ; 9b68: 8d 63 0d    .c.            ; Store modified protection mask
; &9b6b referenced 1 time by &9b5e
.tx_done_classify
    lda tx_done_handler_hi,y                                          ; 9b6b: b9 f6 9a    ...            ; Load handler addr hi from table
    pha                                                               ; 9b6e: 48          H              ; Push handler hi
    lda tx_done_handler_lo,y                                          ; 9b6f: b9 f1 9a    ...            ; Load handler addr lo from table
    pha                                                               ; 9b72: 48          H              ; Push handler lo
    rts                                                               ; 9b73: 60          `              ; Dispatch via RTS (addr-1 on stack)

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
    lda #&9b                                                          ; 9b7e: a9 9b       ..             ; Push hi of (tx_done_exit-1)
    pha                                                               ; 9b80: 48          H              ; Push hi byte on stack
    lda #&bf                                                          ; 9b81: a9 bf       ..             ; Push lo of (tx_done_exit-1)
    pha                                                               ; 9b83: 48          H              ; Push lo byte on stack
    jmp (l0d58)                                                       ; 9b84: 6c 58 0d    lX.            ; Call remote JSR; RTS to tx_done_exit

; ***************************************************************************************
; TX done: UserProc event
; 
; Generates a network event (event 8) via OSEVEN with
; X=l0d58, A=l0d59 (the remote address). This notifies
; the user program that a UserProc operation has completed.
; ***************************************************************************************
.tx_done_user_proc
    ldy #event_network_error                                          ; 9b87: a0 08       ..             ; Y=8: network event type
    ldx l0d58                                                         ; 9b89: ae 58 0d    .X.            ; X = remote address lo
    lda l0d59                                                         ; 9b8c: ad 59 0d    .Y.            ; A = remote address hi
    jsr oseven                                                        ; 9b8f: 20 bf ff     ..            ; Generate event Y='Network error'
    jmp tx_done_exit                                                  ; 9b92: 4c c0 9b    L..            ; Exit TX done handler

; ***************************************************************************************
; TX done: OSProc call
; 
; Calls the ROM entry point at &8000 (rom_header) with
; X=l0d58, Y=l0d59. This invokes an OS-level procedure
; on behalf of the remote station.
; ***************************************************************************************
.tx_done_os_proc
    ldx l0d58                                                         ; 9b95: ae 58 0d    .X.            ; X = remote address lo
    ldy l0d59                                                         ; 9b98: ac 59 0d    .Y.            ; Y = remote address hi
    jsr rom_header                                                    ; 9b9b: 20 00 80     ..            ; Call ROM entry point at &8000
    jmp tx_done_exit                                                  ; 9b9e: 4c c0 9b    L..            ; Exit TX done handler

; ***************************************************************************************
; TX done: HALT
; 
; Sets bit 2 of rx_flags (&0D64), enables interrupts, and
; spin-waits until bit 2 is cleared (by a CONTINUE from the
; remote station). If bit 2 is already set, skips to exit.
; ***************************************************************************************
.tx_done_halt
    lda #4                                                            ; 9ba1: a9 04       ..             ; A=&04: bit 2 mask for rx_flags
    bit rx_flags                                                      ; 9ba3: 2c 64 0d    ,d.            ; Test if already halted
    bne tx_done_exit                                                  ; 9ba6: d0 18       ..             ; Already halted: skip to exit
    ora rx_flags                                                      ; 9ba8: 0d 64 0d    .d.            ; Set bit 2 in rx_flags
    sta rx_flags                                                      ; 9bab: 8d 64 0d    .d.            ; Store halt flag
    lda #4                                                            ; 9bae: a9 04       ..             ; A=4: re-load halt bit mask
    cli                                                               ; 9bb0: 58          X              ; Enable interrupts during halt wait
; &9bb1 referenced 1 time by &9bb4
.halt_spin_loop
    bit rx_flags                                                      ; 9bb1: 2c 64 0d    ,d.            ; Test halt flag
    bne halt_spin_loop                                                ; 9bb4: d0 fb       ..             ; Still halted: keep spinning
    beq tx_done_exit                                                  ; 9bb6: f0 08       ..             ; ALWAYS branch

; ***************************************************************************************
; TX done: CONTINUE
; 
; Clears bit 2 of rx_flags (&0D64), releasing any station
; that is halted and spinning in tx_done_halt.
; ***************************************************************************************
.tx_done_continue
    lda rx_flags                                                      ; 9bb8: ad 64 0d    .d.            ; Load current RX flags
    and #&fb                                                          ; 9bbb: 29 fb       ).             ; Clear bit 2: release halted station
    sta rx_flags                                                      ; 9bbd: 8d 64 0d    .d.            ; Store updated flags
; &9bc0 referenced 4 times by &9b92, &9b9e, &9ba6, &9bb6
.tx_done_exit
    pla                                                               ; 9bc0: 68          h              ; Restore Y from stack
    tay                                                               ; 9bc1: a8          .              ; Transfer to Y register
    pla                                                               ; 9bc2: 68          h              ; Restore X from stack
    tax                                                               ; 9bc3: aa          .              ; Transfer to X register
    lda #0                                                            ; 9bc4: a9 00       ..             ; A=0: success status
    rts                                                               ; 9bc6: 60          `              ; Return with A=0 (success)

; ***************************************************************************************
; Begin TX operation
; 
; Main TX initiation entry point (called via trampoline at &06CE).
; Copies dest station/network from the TXCB to the scout buffer,
; dispatches to immediate op setup (ctrl >= &81) or normal data
; transfer, calculates transfer sizes, copies extra parameters,
; then enters the INACTIVE polling loop.
; ***************************************************************************************
; &9bc7 referenced 1 time by &9660
.tx_begin
    txa                                                               ; 9bc7: 8a          .              ; Save X on stack
    pha                                                               ; 9bc8: 48          H              ; Push X
    ldy #2                                                            ; 9bc9: a0 02       ..             ; Y=2: TXCB offset for dest station
    lda (nmi_tx_block),y                                              ; 9bcb: b1 a0       ..             ; Load dest station from TX control block
    sta tx_dst_stn                                                    ; 9bcd: 8d 20 0d    . .            ; Store to TX scout buffer
    iny                                                               ; 9bd0: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 9bd1: b1 a0       ..             ; Load dest network from TX control block
    sta tx_dst_net                                                    ; 9bd3: 8d 21 0d    .!.            ; Store to TX scout buffer
    ldy #0                                                            ; 9bd6: a0 00       ..             ; Y=0: first byte of TX control block
    lda (nmi_tx_block),y                                              ; 9bd8: b1 a0       ..             ; Load control/flag byte
    bmi tx_imm_op_setup                                               ; 9bda: 30 03       0.             ; Bit7 set: immediate operation ctrl byte
    jmp tx_active_start                                               ; 9bdc: 4c 6b 9c    Lk.            ; Bit7 clear: normal data transfer

; &9bdf referenced 1 time by &9bda
.tx_imm_op_setup
    sta tx_ctrl_byte                                                  ; 9bdf: 8d 24 0d    .$.            ; Store control byte to TX scout buffer
    tax                                                               ; 9be2: aa          .              ; X = control byte for range checks
    iny                                                               ; 9be3: c8          .              ; Y=1: port byte offset
    lda (nmi_tx_block),y                                              ; 9be4: b1 a0       ..             ; Load port byte from TX control block
    sta tx_port                                                       ; 9be6: 8d 25 0d    .%.            ; Store port byte to TX scout buffer
    bne tx_line_idle_check                                            ; 9be9: d0 33       .3             ; Port != 0: skip immediate op setup
    cpx #&83                                                          ; 9beb: e0 83       ..             ; Ctrl < &83: PEEK/POKE need address calc
    bcs tx_ctrl_range_check                                           ; 9bed: b0 1b       ..             ; Ctrl >= &83: skip to range check
    sec                                                               ; 9bef: 38          8              ; SEC: init borrow for 4-byte subtract
    php                                                               ; 9bf0: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 9bf1: a0 08       ..             ; Y=8: high pointer offset in TXCB
; &9bf3 referenced 1 time by &9c07
.calc_peek_poke_size
    lda (nmi_tx_block),y                                              ; 9bf3: b1 a0       ..             ; Load TXCB[Y] (end addr byte)
    dey                                                               ; 9bf5: 88          .              ; Y -= 4: back to start addr offset
    dey                                                               ; 9bf6: 88          .              ; (Y -= 4: reach start addr offset)
    dey                                                               ; 9bf7: 88          .              ; (continued)
    dey                                                               ; 9bf8: 88          .              ; (continued)
    plp                                                               ; 9bf9: 28          (              ; Restore borrow from stack
    sbc (nmi_tx_block),y                                              ; 9bfa: f1 a0       ..             ; end - start = transfer size byte
    sta tx_data_start,y                                               ; 9bfc: 99 26 0d    .&.            ; Store result to tx_data_start
    iny                                                               ; 9bff: c8          .              ; (Y += 5: advance to next end byte)
    iny                                                               ; 9c00: c8          .              ; (continued)
    iny                                                               ; 9c01: c8          .              ; (continued)
    iny                                                               ; 9c02: c8          .              ; (continued)
    iny                                                               ; 9c03: c8          .              ; (continued)
    php                                                               ; 9c04: 08          .              ; Save borrow for next byte
    cpy #&0c                                                          ; 9c05: c0 0c       ..             ; Done all 4 bytes? (Y reaches &0C)
    bcc calc_peek_poke_size                                           ; 9c07: 90 ea       ..             ; No: next byte pair
    plp                                                               ; 9c09: 28          (              ; Discard final borrow
; &9c0a referenced 1 time by &9bed
.tx_ctrl_range_check
    cpx #&81                                                          ; 9c0a: e0 81       ..             ; Ctrl < &81: not an immediate op
    bcc tx_active_start                                               ; 9c0c: 90 5d       .]             ; Below range: normal data transfer
.check_imm_range
    cpx #&89                                                          ; 9c0e: e0 89       ..             ; Ctrl >= &89: out of immediate range
    bcs tx_active_start                                               ; 9c10: b0 59       .Y             ; Above range: normal data transfer
    ldy #&0c                                                          ; 9c12: a0 0c       ..             ; Y=&0C: start of extra data in TXCB
; &9c14 referenced 1 time by &9c1c
.copy_imm_params
    lda (nmi_tx_block),y                                              ; 9c14: b1 a0       ..             ; Load extra parameter byte from TXCB
    sta nmi_shim_1a,y                                                 ; 9c16: 99 1a 0d    ...            ; Copy to NMI shim workspace at &0D1A+Y
    iny                                                               ; 9c19: c8          .              ; Next byte
    cpy #&10                                                          ; 9c1a: c0 10       ..             ; Done 4 bytes? (Y reaches &10)
    bcc copy_imm_params                                               ; 9c1c: 90 f6       ..             ; No: continue copying
; &9c1e referenced 1 time by &9be9
.tx_line_idle_check
    lda #&20 ; ' '                                                    ; 9c1e: a9 20       .              ; A=&20: mask for SR2 INACTIVE bit
    bit econet_control23_or_status2                                   ; 9c20: 2c a1 fe    ,..            ; BIT SR2: test if line is idle
    bne tx_no_clock_error                                             ; 9c23: d0 56       .V             ; Line not idle: handle as line jammed
    lda #&fd                                                          ; 9c25: a9 fd       ..             ; A=&FD: high byte of timeout counter
    pha                                                               ; 9c27: 48          H              ; Push timeout high byte to stack
    lda #6                                                            ; 9c28: a9 06       ..             ; Scout frame = 6 address+ctrl bytes
    sta tx_length                                                     ; 9c2a: 8d 50 0d    .P.            ; Store scout frame length
    lda #0                                                            ; 9c2d: a9 00       ..             ; A=0: init low byte of timeout counter
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
    sta tx_index                                                      ; 9c2f: 8d 4f 0d    .O.            ; Save TX index
    pha                                                               ; 9c32: 48          H              ; Push timeout byte 1 on stack
    pha                                                               ; 9c33: 48          H              ; Push timeout byte 2 on stack
    ldy #&e7                                                          ; 9c34: a0 e7       ..             ; Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &9c36 referenced 3 times by &9c5c, &9c61, &9c66
.test_inactive_retry
    lda #4                                                            ; 9c36: a9 04       ..             ; A=&04: INACTIVE mask for SR2 bit2
    php                                                               ; 9c38: 08          .              ; Save interrupt state
    sei                                                               ; 9c39: 78          x              ; Disable interrupts for ADLC access
; ***************************************************************************************
; Disable NMIs and test INACTIVE
; 
; Mid-instruction label within the INACTIVE polling loop. The
; address &9BE2 is referenced as a constant for self-modifying
; code. Disables NMIs twice (belt-and-braces) then tests SR2
; for INACTIVE before proceeding with TX.
; ***************************************************************************************
; &9c3a referenced 1 time by &9cb6
.intoff_test_inactive
    bit station_id_disable_net_nmis                                   ; 9c3a: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
    bit station_id_disable_net_nmis                                   ; 9c3d: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
.test_line_idle
sr2_idle_status = test_line_idle+2
    bit econet_control23_or_status2                                   ; 9c40: 2c a1 fe    ,..            ; BIT SR2: Z = &04 AND SR2 -- tests INACTIVE
; &9c42 referenced 1 time by &9cb2
    beq inactive_retry                                                ; 9c43: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 9c45: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 9c48: a9 67       .g             ; CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9c4a: 8d a1 fe    ...            ; Write CR2: clear status, prepare TX
    lda #&10                                                          ; 9c4d: a9 10       ..             ; A=&10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 9c4f: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 9c52: d0 35       .5             ; CTS set -- clock hardware detected, start TX
; &9c54 referenced 1 time by &9c43
.inactive_retry
    bit video_ula_control                                             ; 9c54: 2c 20 fe    , .            ; INTON -- re-enable NMIs (&FE20 read)
    plp                                                               ; 9c57: 28          (              ; Restore interrupt state
    tsx                                                               ; 9c58: ba          .              ; 3-byte timeout counter on stack
    inc l0101,x                                                       ; 9c59: fe 01 01    ...            ; Increment timeout counter byte 1
    bne test_inactive_retry                                           ; 9c5c: d0 d8       ..             ; Not overflowed: retry INACTIVE test
    inc l0102,x                                                       ; 9c5e: fe 02 01    ...            ; Increment timeout counter byte 2
    bne test_inactive_retry                                           ; 9c61: d0 d3       ..             ; Not overflowed: retry INACTIVE test
    inc l0103,x                                                       ; 9c63: fe 03 01    ...            ; Increment timeout counter byte 3
    bne test_inactive_retry                                           ; 9c66: d0 ce       ..             ; Not overflowed: retry INACTIVE test
    jmp tx_line_jammed                                                ; 9c68: 4c 6f 9c    Lo.            ; All 3 bytes overflowed: line jammed

; TX_ACTIVE branch (A=&44 = CR1 value for TX active)
; &9c6b referenced 3 times by &9bdc, &9c0c, &9c10
.tx_active_start
    lda #&44 ; 'D'                                                    ; 9c6b: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    bne store_tx_error                                                ; 9c6d: d0 0e       ..             ; ALWAYS branch

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
    sta econet_control23_or_status2                                   ; 9c71: 8d a1 fe    ...            ; Write CR2 to abort TX
    pla                                                               ; 9c74: 68          h              ; Clean 3 bytes of timeout loop state
    pla                                                               ; 9c75: 68          h              ; Pop saved register
    pla                                                               ; 9c76: 68          h              ; Pop saved register
    lda #&40 ; '@'                                                    ; 9c77: a9 40       .@             ; Error &40 = 'Line Jammed'
    bne store_tx_error                                                ; 9c79: d0 02       ..             ; ALWAYS branch to shared error handler; ALWAYS branch

; &9c7b referenced 1 time by &9c23
.tx_no_clock_error
    lda #&43 ; 'C'                                                    ; 9c7b: a9 43       .C             ; Error &43 = 'No Clock'
; &9c7d referenced 2 times by &9c6d, &9c79
.store_tx_error
    ldy #0                                                            ; 9c7d: a0 00       ..             ; Offset 0 = error byte in TX control block
    sta (nmi_tx_block),y                                              ; 9c7f: 91 a0       ..             ; Store error code in TX CB byte 0
    lda #&80                                                          ; 9c81: a9 80       ..             ; &80 = TX complete flag
    sta tx_clear_flag                                                 ; 9c83: 8d 62 0d    .b.            ; Signal TX operation complete
    pla                                                               ; 9c86: 68          h              ; Restore X saved by caller
    tax                                                               ; 9c87: aa          .              ; Move to X register
    rts                                                               ; 9c88: 60          `              ; Return to TX caller

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
    stx econet_control1_or_status1                                    ; 9c8e: 8e a0 fe    ...            ; Write to ADLC CR1
    ldx #&2d ; '-'                                                    ; 9c91: a2 2d       .-             ; Install NMI handler at &9D4C (TX data handler); Install NMI handler at &9CCC (nmi_tx_data)
    ldy #&9d                                                          ; 9c93: a0 9d       ..             ; High byte of NMI handler address
    stx nmi_jmp_lo                                                    ; 9c95: 8e 0c 0d    ...            ; Write NMI vector low byte directly
    sty nmi_jmp_hi                                                    ; 9c98: 8c 0d 0d    ...            ; Write NMI vector high byte directly
    bit video_ula_control                                             ; 9c9b: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA (&FE20 read)
    lda tx_port                                                       ; 9c9e: ad 25 0d    .%.            ; Load destination port number
    bne setup_data_xfer                                               ; 9ca1: d0 4c       .L             ; Port != 0: standard data transfer
    ldy tx_ctrl_byte                                                  ; 9ca3: ac 24 0d    .$.            ; Port 0: load control byte for table lookup
    lda tube_tx_count_4,y                                             ; 9ca6: b9 af 9e    ...            ; Look up tx_flags from table
    sta tx_flags                                                      ; 9ca9: 8d 4a 0d    .J.            ; Store operation flags
    lda tube_tx_count_2,y                                             ; 9cac: b9 a7 9e    ...            ; Look up tx_length from table
    sta tx_length                                                     ; 9caf: 8d 50 0d    .P.            ; Store expected transfer length
    lda sr2_idle_status,y                                             ; 9cb2: b9 42 9c    .B.            ; Load handler from dispatch table
    pha                                                               ; 9cb5: 48          H              ; Push high byte for PHA/PHA/RTS dispatch
    lda intoff_test_inactive,y                                        ; 9cb6: b9 3a 9c    .:.            ; Look up handler address low from table
    pha                                                               ; 9cb9: 48          H              ; Push low byte for PHA/PHA/RTS dispatch
    rts                                                               ; 9cba: 60          `              ; RTS dispatches to control-byte handler

    equb <(tx_ctrl_peek-1)                                            ; 9cbb: ce          .
    equb <(tx_ctrl_poke-1)                                            ; 9cbc: d2          .
    equb <(proc_op_status2-1)                                         ; 9cbd: 15          .
    equb <(proc_op_status2-1)                                         ; 9cbe: 15          .
    equb <(proc_op_status2-1)                                         ; 9cbf: 15          .
    equb <(tx_ctrl_exit-1)                                            ; 9cc0: 25          %
    equb <(tx_ctrl_exit-1)                                            ; 9cc1: 25          %
    equb <(imm_op_status3-1)                                          ; 9cc2: ca          .
    equb >(tx_ctrl_peek-1)                                            ; 9cc3: 9c          .
    equb >(tx_ctrl_poke-1)                                            ; 9cc4: 9c          .
    equb >(proc_op_status2-1)                                         ; 9cc5: 9d          .
    equb >(proc_op_status2-1)                                         ; 9cc6: 9d          .
    equb >(proc_op_status2-1)                                         ; 9cc7: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cc8: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cc9: 9d          .
    equb >(imm_op_status3-1)                                          ; 9cca: 9c          .

.imm_op_status3
    lda #3                                                            ; 9ccb: a9 03       ..             ; A=3: scout_status for POKE
    bne store_status_copy_ptr                                         ; 9ccd: d0 49       .I             ; ALWAYS branch

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
    lda #3                                                            ; 9ccf: a9 03       ..             ; A=3: scout_status for PEEK op
    bne store_status_add4                                             ; 9cd1: d0 02       ..             ; ALWAYS branch

; ***************************************************************************************
; TX ctrl: POKE transfer setup
; 
; Sets scout_status=2 and shares the 4-byte addition and
; transfer calculation path with tx_ctrl_peek.
; ***************************************************************************************
.tx_ctrl_poke
    lda #2                                                            ; 9cd3: a9 02       ..             ; Scout status = 2 (POKE transfer)
; &9cd5 referenced 1 time by &9cd1
.store_status_add4
    sta scout_status                                                  ; 9cd5: 8d 5c 0d    .\.            ; Store scout status
    clc                                                               ; 9cd8: 18          .              ; Clear carry for 4-byte addition
    php                                                               ; 9cd9: 08          .              ; Save carry on stack
    ldy #&0c                                                          ; 9cda: a0 0c       ..             ; Y=&0C: start at offset 12
; &9cdc referenced 1 time by &9ce9
.add_bytes_loop
    lda l0d1e,y                                                       ; 9cdc: b9 1e 0d    ...            ; Load workspace address byte
    plp                                                               ; 9cdf: 28          (              ; Restore carry from previous byte
    adc (nmi_tx_block),y                                              ; 9ce0: 71 a0       q.             ; Add TXCB address byte
    sta l0d1e,y                                                       ; 9ce2: 99 1e 0d    ...            ; Store updated address byte
    iny                                                               ; 9ce5: c8          .              ; Next byte
    php                                                               ; 9ce6: 08          .              ; Save carry for next addition
; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_proc
    cpy #&10                                                          ; 9ce7: c0 10       ..             ; Compare Y with 16-byte boundary
    bcc add_bytes_loop                                                ; 9ce9: 90 f1       ..             ; Below boundary: continue addition
    plp                                                               ; 9ceb: 28          (              ; Restore processor flags
    jmp skip_buf_setup                                                ; 9cec: 4c 1b 9d    L..            ; Exit TX ctrl setup

; &9cef referenced 1 time by &9ca1
.setup_data_xfer
    lda tx_dst_stn                                                    ; 9cef: ad 20 0d    . .            ; Load dest station for broadcast check
    and tx_dst_net                                                    ; 9cf2: 2d 21 0d    -!.            ; AND with dest network
    cmp #&ff                                                          ; 9cf5: c9 ff       ..             ; Both &FF = broadcast address?
    bne setup_unicast_xfer                                            ; 9cf7: d0 18       ..             ; Not broadcast: unicast path
    lda #&0e                                                          ; 9cf9: a9 0e       ..             ; Broadcast scout: 14 bytes total
    sta tx_length                                                     ; 9cfb: 8d 50 0d    .P.            ; Store broadcast scout length
    lda #&40 ; '@'                                                    ; 9cfe: a9 40       .@             ; A=&40: broadcast flag
    sta tx_flags                                                      ; 9d00: 8d 4a 0d    .J.            ; Set broadcast flag in tx_flags
    ldy #4                                                            ; 9d03: a0 04       ..             ; Y=4: start of address data in TXCB
; &9d05 referenced 1 time by &9d0d
.copy_bcast_addr
    lda (nmi_tx_block),y                                              ; 9d05: b1 a0       ..             ; Copy TXCB address bytes to scout buffer
    sta tx_src_stn,y                                                  ; 9d07: 99 22 0d    .".            ; Store to TX source/data area
    iny                                                               ; 9d0a: c8          .              ; Next byte
    cpy #&0c                                                          ; 9d0b: c0 0c       ..             ; Done 8 bytes? (Y reaches &0C)
    bcc copy_bcast_addr                                               ; 9d0d: 90 f6       ..             ; No: continue copying
    bcs tx_ctrl_exit                                                  ; 9d0f: b0 15       ..             ; ALWAYS branch

; &9d11 referenced 1 time by &9cf7
.setup_unicast_xfer
    lda #0                                                            ; 9d11: a9 00       ..             ; A=0: clear flags for unicast
    sta tx_flags                                                      ; 9d13: 8d 4a 0d    .J.            ; Clear tx_flags
.proc_op_status2
    lda #2                                                            ; 9d16: a9 02       ..             ; scout_status=2: data transfer pending
; &9d18 referenced 1 time by &9ccd
.store_status_copy_ptr
    sta scout_status                                                  ; 9d18: 8d 5c 0d    .\.            ; Store scout status
; &9d1b referenced 1 time by &9cec
.skip_buf_setup
    lda nmi_tx_block                                                  ; 9d1b: a5 a0       ..             ; Copy TX block pointer to workspace ptr
    sta port_ws_offset                                                ; 9d1d: 85 a6       ..             ; Store low byte
    lda nmi_tx_block_hi                                               ; 9d1f: a5 a1       ..             ; Copy TX block pointer high byte
    sta rx_buf_offset                                                 ; 9d21: 85 a7       ..             ; Store high byte
    jsr tx_calc_transfer                                              ; 9d23: 20 38 9f     8.            ; Calculate transfer size from RXCB
; &9d26 referenced 1 time by &9d0f
.tx_ctrl_exit
    plp                                                               ; 9d26: 28          (              ; Restore processor status from stack
    pla                                                               ; 9d27: 68          h              ; Restore stacked registers (4 PLAs)
    pla                                                               ; 9d28: 68          h              ; Second PLA
    pla                                                               ; 9d29: 68          h              ; Third PLA
    pla                                                               ; 9d2a: 68          h              ; Fourth PLA
    tax                                                               ; 9d2b: aa          .              ; Restore X from A
    rts                                                               ; 9d2c: 60          `              ; Return to caller

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
.tx_fifo_write
    bvc tx_fifo_not_ready                                             ; 9d33: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 9d35: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 9d38: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 9d3b: c8          .              ; Next TX buffer byte
    lda tx_dst_stn,y                                                  ; 9d3c: b9 20 0d    . .            ; Load second byte from TX buffer
    iny                                                               ; 9d3f: c8          .              ; Advance TX index past second byte
    sty tx_index                                                      ; 9d40: 8c 4f 0d    .O.            ; Save updated TX buffer index
    sta econet_data_continue_frame                                    ; 9d43: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy tx_length                                                     ; 9d46: cc 50 0d    .P.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 9d49: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA
    bit econet_control1_or_status1                                    ; 9d4b: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi tx_fifo_write                                                 ; 9d4e: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 9d50: 4c 14 0d    L..            ; RTI -- wait for next NMI

; TX error path
; &9d53 referenced 1 time by &9d98
.tx_error
    lda #&42 ; 'B'                                                    ; 9d53: a9 42       .B             ; Error &42
    bne tx_store_error                                                ; 9d55: d0 07       ..             ; ALWAYS branch

; &9d57 referenced 1 time by &9d33
.tx_fifo_not_ready
    lda #&67 ; 'g'                                                    ; 9d57: a9 67       .g             ; CR2=&67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 9d59: 8d a1 fe    ...            ; Write CR2: clear status, idle listen
    lda #&41 ; 'A'                                                    ; 9d5c: a9 41       .A             ; Error &41 (TDRA not ready)
; &9d5e referenced 1 time by &9d55
.tx_store_error
    ldy station_id_disable_net_nmis                                   ; 9d5e: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &9d61 referenced 1 time by &9d64
.delay_nmi_disable
    pha                                                               ; 9d61: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 9d62: 68          h              ; PHA/PLA delay (~7 cycles each)
    iny                                                               ; 9d63: c8          .              ; Increment delay counter
    bne delay_nmi_disable                                             ; 9d64: d0 fb       ..             ; Loop 256 times for NMI disable
    jmp tx_store_result                                               ; 9d66: 4c 1c 9f    L..            ; Store error and return to idle

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
    sta econet_control23_or_status2                                   ; 9d6b: 8d a1 fe    ...            ; Write to ADLC CR2
    lda #&75 ; 'u'                                                    ; 9d6e: a9 75       .u             ; Install NMI handler at &9D94 (TX completion); Install NMI handler at &9D14 (nmi_tx_complete)
    ldy #&9d                                                          ; 9d70: a0 9d       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9d72: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

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
    sta econet_control1_or_status1                                    ; 9d77: 8d a0 fe    ...            ; Write CR1 to switch from TX to RX
    bit tx_flags                                                      ; 9d7a: 2c 4a 0d    ,J.            ; Test workspace flags
    bvc check_handshake_bit                                           ; 9d7d: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 9d7f: 4c 16 9f    L..            ; bit6 set -- TX completion

; &9d82 referenced 1 time by &9d7d
.check_handshake_bit
    lda #1                                                            ; 9d82: a9 01       ..             ; A=1: mask for bit0 test
    bit tx_flags                                                      ; 9d84: 2c 4a 0d    ,J.            ; Test tx_flags bit0 (handshake)
    beq install_reply_scout                                           ; 9d87: f0 03       ..             ; bit0 clear: install reply handler
    jmp handshake_await_ack                                           ; 9d89: 4c ba 9e    L..            ; bit0 set -- four-way handshake data phase

; &9d8c referenced 1 time by &9d87
.install_reply_scout
    lda #&93                                                          ; 9d8c: a9 93       ..             ; Install RX reply handler at &9DB2; Install nmi_reply_scout at &9D30
    ldy #&9d                                                          ; 9d8e: a0 9d       ..             ; High byte of nmi_reply_scout addr
    jmp set_nmi_vector                                                ; 9d90: 4c 0e 0d    L..            ; Install handler and RTI

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
    lda econet_data_continue_frame                                    ; 9d9a: ad a2 fe    ...            ; Read first RX byte (destination station)
    cmp station_id_disable_net_nmis                                   ; 9d9d: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne reject_reply                                                  ; 9da0: d0 1d       ..             ; Not our station -- error/reject
    lda #&a9                                                          ; 9da2: a9 a9       ..             ; Install next handler at &9DC8 (reply continuation); Install nmi_reply_cont at &9D44
    ldy #&9d                                                          ; 9da4: a0 9d       ..             ; High byte of nmi_reply_cont
    jmp set_nmi_vector                                                ; 9da6: 4c 0e 0d    L..            ; Install continuation handler

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
    bpl reject_reply                                                  ; 9dac: 10 11       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9dae: ad a2 fe    ...            ; Read destination network byte
    bne reject_reply                                                  ; 9db1: d0 0c       ..             ; Non-zero -- network mismatch, error
    lda #&c2                                                          ; 9db3: a9 c2       ..             ; Install next handler at &9DE3 (reply validation); Install nmi_reply_validate at &9D5B
    ldy #&9d                                                          ; 9db5: a0 9d       ..             ; High byte of nmi_reply_validate
    bit econet_control1_or_status1                                    ; 9db7: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 9dba: 30 06       0.             ; IRQ set -- fall through to &9DE3 without RTI; IRQ set -- fall through to &9D5B without RTI
    jmp set_nmi_vector                                                ; 9dbc: 4c 0e 0d    L..            ; IRQ not set -- install handler and RTI

; &9dbf referenced 7 times by &9da0, &9dac, &9db1, &9dc5, &9dcd, &9dd5, &9ddc
.reject_reply
    jmp tx_result_fail                                                ; 9dbf: 4c 1a 9f    L..            ; Store error and return to idle

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
    bpl reject_reply                                                  ; 9dc5: 10 f8       ..             ; No RDA -- error (FV masking RDA via PSE would cause this)
    lda econet_data_continue_frame                                    ; 9dc7: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9dca: cd 20 0d    . .            ; Compare to original TX destination station (&0D20)
    bne reject_reply                                                  ; 9dcd: d0 f0       ..             ; Mismatch -- not the expected reply, error
    lda econet_data_continue_frame                                    ; 9dcf: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9dd2: cd 21 0d    .!.            ; Compare to original TX destination network (&0D21)
    bne reject_reply                                                  ; 9dd5: d0 e8       ..             ; Mismatch -- error
    lda #2                                                            ; 9dd7: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9dd9: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq reject_reply                                                  ; 9ddc: f0 e1       ..             ; No FV -- incomplete frame, error
    lda #&a7                                                          ; 9dde: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)
    sta econet_control23_or_status2                                   ; 9de0: 8d a1 fe    ...            ; Write CR2: enable RTS for TX handshake
    lda #&44 ; 'D'                                                    ; 9de3: a9 44       .D             ; CR1=&44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 9de5: 8d a0 fe    ...            ; Write CR1: reset RX, enable TX interrupt
    lda #&ba                                                          ; 9de8: a9 ba       ..             ; Install next handler at &9EDD (four-way data phase) into &0D4B/&0D4C; Save handshake_await_ack (&9E50) in &0D4B/&0D4C
    ldy #&9e                                                          ; 9dea: a0 9e       ..             ; High byte &9E of next handler address
    sta nmi_next_lo                                                   ; 9dec: 8d 4b 0d    .K.            ; Store low byte to nmi_next_lo
    sty nmi_next_hi                                                   ; 9def: 8c 4c 0d    .L.            ; Store high byte to nmi_next_hi
    lda tx_dst_stn                                                    ; 9df2: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 9df5: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc data_tx_error                                                 ; 9df8: 50 73       Ps             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9dfa: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 9dfd: ad 21 0d    .!.            ; Write dest network to TX FIFO; Load dest network for scout ACK TX
    sta econet_data_continue_frame                                    ; 9e00: 8d a2 fe    ...            ; Write dest network to TX FIFO
    lda #&0a                                                          ; 9e03: a9 0a       ..             ; Install handler at &9E2B (write src addr for scout ACK); Install nmi_scout_ack_src at &9DA3
    ldy #&9e                                                          ; 9e05: a0 9e       ..             ; High byte &9D of handler address
    jmp set_nmi_vector                                                ; 9e07: 4c 0e 0d    L..            ; Set NMI vector and return

; ***************************************************************************************
; TX scout ACK: write source address
; 
; Writes our station ID and network=0 to TX FIFO, completing the
; 4-byte scout ACK frame. Then proceeds to send the data frame.
; ***************************************************************************************
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 9e0a: ad 18 fe    ...            ; Load our station ID (also INTOFF); Read our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9e0d: 2c a0 fe    ,..            ; BIT SR1: test TDRA; BIT SR1: check TDRA before writing
    bvc data_tx_error                                                 ; 9e10: 50 5b       P[             ; TDRA not ready -- error; TDRA not ready: TX error
    sta econet_data_continue_frame                                    ; 9e12: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9e15: a9 00       ..             ; Write network=0 to TX FIFO; Network = 0 (local network)
    sta econet_data_continue_frame                                    ; 9e17: 8d a2 fe    ...            ; Write network byte to TX FIFO
; &9e1a referenced 1 time by &999e
.data_tx_begin
    lda #2                                                            ; 9e1a: a9 02       ..             ; Test bit 1 of tx_flags
    bit tx_flags                                                      ; 9e1c: 2c 4a 0d    ,J.            ; Check if immediate-op or data-transfer
    bne install_imm_data_nmi                                          ; 9e1f: d0 07       ..             ; Bit 1 set: immediate op, use alt handler
    lda #&2f ; '/'                                                    ; 9e21: a9 2f       ./             ; Install nmi_data_tx at &9DC8
    ldy #&9e                                                          ; 9e23: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9e25: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; &9e28 referenced 1 time by &9e1f
.install_imm_data_nmi
    lda #&81                                                          ; 9e28: a9 81       ..             ; Install nmi_imm_data at &9E0F
    ldy #&9e                                                          ; 9e2a: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9e2c: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

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
.data_tx_check_fifo
    bvc data_tx_error                                                 ; 9e34: 50 37       P7             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 9e36: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 9e38: 8d a2 fe    ...            ; Write first byte of pair to FIFO
    iny                                                               ; 9e3b: c8          .              ; Advance buffer offset
    bne write_second_tx_byte                                          ; 9e3c: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 9e3e: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 9e40: f0 1a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 9e42: e6 a5       ..             ; Increment buffer high byte
; &9e44 referenced 1 time by &9e3c
.write_second_tx_byte
    lda (open_port_buf),y                                             ; 9e44: b1 a4       ..             ; Load second byte of pair
    sta econet_data_continue_frame                                    ; 9e46: 8d a2 fe    ...            ; Write second byte to FIFO
    iny                                                               ; 9e49: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 9e4a: 84 a2       ..             ; Save updated buffer position
    bne check_irq_loop                                                ; 9e4c: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 9e4e: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 9e50: f0 0a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 9e52: e6 a5       ..             ; Increment buffer high byte
; &9e54 referenced 1 time by &9e4c
.check_irq_loop
    bit econet_control1_or_status1                                    ; 9e54: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) for tight loop
    bmi data_tx_check_fifo                                            ; 9e57: 30 db       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 9e59: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; &9e5c referenced 4 times by &9e40, &9e50, &9e9a, &9eb0
.data_tx_last
    lda #&3f ; '?'                                                    ; 9e5c: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 9e5e: 8d a1 fe    ...            ; Write CR2 to close frame
    lda tx_flags                                                      ; 9e61: ad 4a 0d    .J.            ; Check tx_flags for next action
    bpl install_saved_handler                                         ; 9e64: 10 12       ..             ; Bit7 clear: error, install saved handler
    lda #&2e ; '.'                                                    ; 9e66: a9 2e       ..             ; Install discard_reset_listen at &99DB
    ldy #&9a                                                          ; 9e68: a0 9a       ..             ; High byte of &99DB handler
    jmp set_nmi_vector                                                ; 9e6a: 4c 0e 0d    L..            ; Set NMI vector and return

; &9e6d referenced 4 times by &9df8, &9e10, &9e34, &9e84
.data_tx_error
    lda tx_flags                                                      ; 9e6d: ad 4a 0d    .J.            ; Load saved next handler low byte
    bpl jmp_tx_result_fail                                            ; 9e70: 10 03       ..             ; bit7 clear: error path
    jmp discard_reset_listen                                          ; 9e72: 4c 2e 9a    L..            ; ADLC reset and return to idle

; &9e75 referenced 1 time by &9e70
.jmp_tx_result_fail
    jmp tx_result_fail                                                ; 9e75: 4c 1a 9f    L..            ; Store result and return to idle

; &9e78 referenced 1 time by &9e64
.install_saved_handler
    lda nmi_next_lo                                                   ; 9e78: ad 4b 0d    .K.            ; Load saved handler low byte
    ldy nmi_next_hi                                                   ; 9e7b: ac 4c 0d    .L.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 9e7e: 4c 0e 0d    L..            ; Install saved handler and return

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 9e81: 2c a0 fe    ,..            ; Tube TX: BIT SR1 test TDRA
; &9e84 referenced 1 time by &9eb5
.tube_tx_fifo_write
    bvc data_tx_error                                                 ; 9e84: 50 e7       P.             ; TDRA not ready -- error
    lda tube_data_register_3                                          ; 9e86: ad e5 fe    ...            ; Read byte from Tube R3
    sta econet_data_continue_frame                                    ; 9e89: 8d a2 fe    ...            ; Write to TX FIFO
    inc port_buf_len                                                  ; 9e8c: e6 a2       ..             ; Increment 4-byte buffer counter
    bne write_second_tube_byte                                        ; 9e8e: d0 0c       ..             ; Low byte didn't wrap
    inc port_buf_len_hi                                               ; 9e90: e6 a3       ..             ; Carry into second byte
    bne write_second_tube_byte                                        ; 9e92: d0 08       ..             ; No further carry
    inc open_port_buf                                                 ; 9e94: e6 a4       ..             ; Carry into third byte
    bne write_second_tube_byte                                        ; 9e96: d0 04       ..             ; No further carry
    inc open_port_buf_hi                                              ; 9e98: e6 a5       ..             ; Carry into fourth byte
    beq data_tx_last                                                  ; 9e9a: f0 c0       ..             ; Counter wrapped to zero: last data
; &9e9c referenced 3 times by &9e8e, &9e92, &9e96
.write_second_tube_byte
    lda tube_data_register_3                                          ; 9e9c: ad e5 fe    ...            ; Read second Tube byte from R3
    sta econet_data_continue_frame                                    ; 9e9f: 8d a2 fe    ...            ; Write second byte to TX FIFO
    inc port_buf_len                                                  ; 9ea2: e6 a2       ..             ; Increment 4-byte counter (second byte)
    bne check_tube_irq_loop                                           ; 9ea4: d0 0c       ..             ; Low byte didn't wrap
.tube_tx_inc_byte2
tube_tx_count_2 = tube_tx_inc_byte2+1
    inc port_buf_len_hi                                               ; 9ea6: e6 a3       ..             ; Carry into second byte
; &9ea7 referenced 1 time by &9cac
    bne check_tube_irq_loop                                           ; 9ea8: d0 08       ..             ; No further carry
.tube_tx_inc_byte3
    inc open_port_buf                                                 ; 9eaa: e6 a4       ..             ; Carry into third byte
    bne check_tube_irq_loop                                           ; 9eac: d0 04       ..             ; No further carry
.tube_tx_inc_byte4
tube_tx_count_4 = tube_tx_inc_byte4+1
    inc open_port_buf_hi                                              ; 9eae: e6 a5       ..             ; Carry into fourth byte
; &9eaf referenced 1 time by &9ca6
    beq data_tx_last                                                  ; 9eb0: f0 aa       ..             ; Counter wrapped to zero: last data
; &9eb2 referenced 3 times by &9ea4, &9ea8, &9eac
.check_tube_irq_loop
    bit econet_control1_or_status1                                    ; 9eb2: 2c a0 fe    ,..            ; BIT SR1: test IRQ for tight loop
    bmi tube_tx_fifo_write                                            ; 9eb5: 30 cd       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 9eb7: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; ***************************************************************************************
; Four-way handshake: switch to RX for final ACK
; 
; After the data frame TX completes, switches to RX mode (CR1=&82)
; and installs &9EF8 to receive the final ACK from the remote station.
; ***************************************************************************************
; &9eba referenced 1 time by &9d89
.handshake_await_ack
    lda #&82                                                          ; 9eba: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 9ebc: 8d a0 fe    ...            ; Write to ADLC CR1
    lda #&c6                                                          ; 9ebf: a9 c6       ..             ; Install handler at &9EE9 (RX final ACK); Install nmi_final_ack at &9E5C
    ldy #&9e                                                          ; 9ec1: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9ec3: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

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
    lda #&dc                                                          ; 9ed5: a9 dc       ..             ; Install handler at &9EFF (final ACK continuation); Install nmi_final_ack_net at &9E70
    ldy #&9e                                                          ; 9ed7: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9ed9: 4c 0e 0d    L..            ; Install continuation handler

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 9edc: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9edf: 10 39       .9             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9ee1: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 9ee4: d0 34       .4             ; Non-zero -- network mismatch, error
    lda #&f2                                                          ; 9ee6: a9 f2       ..             ; Install handler at &9F15 (final ACK validation); Install nmi_final_ack_validate at &9E84
    ldy #&9e                                                          ; 9ee8: a0 9e       ..             ; High byte of handler address
    bit econet_control1_or_status1                                    ; 9eea: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 9eed: 30 03       0.             ; IRQ set -- fall through to &9F15 without RTI; IRQ set -- fall through to &9E84 without RTI
    jmp set_nmi_vector                                                ; 9eef: 4c 0e 0d    L..            ; Install handler and RTI

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
    lda tx_flags                                                      ; 9f07: ad 4a 0d    .J.            ; Load TX flags for next action
    bpl check_fv_final_ack                                            ; 9f0a: 10 03       ..             ; bit7 clear: no data phase
    jmp install_data_rx_handler                                       ; 9f0c: 4c 58 98    LX.            ; Install data RX handler

; &9f0f referenced 1 time by &9f0a
.check_fv_final_ack
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

; ***************************************************************************************
; TX failure: not listening
; 
; Loads error code &41 (not listening) and falls through to
; tx_store_result. The most common TX error path — reached from
; 11 sites across the final-ACK validation chain when the remote
; station doesn't respond or the frame is malformed.
; ***************************************************************************************
; &9f1a referenced 11 times by &9877, &9dbf, &9e75, &9ecb, &9ed3, &9edf, &9ee4, &9ef5, &9efd, &9f05, &9f14
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 9f1a: a9 41       .A             ; A=&41: not listening error code
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
    ldy #6                                                            ; 9f38: a0 06       ..             ; Load RXCB[6] (buffer addr byte 2)
    lda (port_ws_offset),y                                            ; 9f3a: b1 a6       ..             ; Load workspace byte at offset Y
    iny                                                               ; 9f3c: c8          .              ; Y=&07
    and (port_ws_offset),y                                            ; 9f3d: 31 a6       1.             ; AND with RXCB[7] (byte 3)
    cmp #&ff                                                          ; 9f3f: c9 ff       ..             ; Both &FF = no buffer?
    beq fallback_calc_transfer                                        ; 9f41: f0 41       .A             ; Yes: fallback path
    lda tube_flag                                                     ; 9f43: ad 67 0d    .g.            ; Tube transfer in progress?; Transmit in progress?
    beq fallback_calc_transfer                                        ; 9f46: f0 3c       .<             ; No: fallback path
    lda tx_flags                                                      ; 9f48: ad 4a 0d    .J.            ; Load TX flags for transfer setup
    ora #2                                                            ; 9f4b: 09 02       ..             ; Set bit 1 (transfer complete)
    sta tx_flags                                                      ; 9f4d: 8d 4a 0d    .J.            ; Store with bit 1 set (Tube xfer)
    sec                                                               ; 9f50: 38          8              ; Init borrow for 4-byte subtract
    php                                                               ; 9f51: 08          .              ; Save carry on stack
    ldy #4                                                            ; 9f52: a0 04       ..             ; Y=4: start at RXCB offset 4
; &9f54 referenced 1 time by &9f66
.calc_transfer_size
    lda (port_ws_offset),y                                            ; 9f54: b1 a6       ..             ; Load RXCB[Y] (current ptr byte)
    iny                                                               ; 9f56: c8          .              ; Y += 4: advance to RXCB[Y+4]
    iny                                                               ; 9f57: c8          .              ; Y += 4: advance to high ptr offset
    iny                                                               ; 9f58: c8          .              ; (continued)
    iny                                                               ; 9f59: c8          .              ; (continued)
    plp                                                               ; 9f5a: 28          (              ; Restore borrow from previous byte
    sbc (port_ws_offset),y                                            ; 9f5b: f1 a6       ..             ; Subtract RXCB[Y+4] (start ptr byte)
    sta net_tx_ptr,y                                                  ; 9f5d: 99 9a 00    ...            ; Store result byte
    dey                                                               ; 9f60: 88          .              ; Y -= 3: next source byte
    dey                                                               ; 9f61: 88          .              ; Y -= 3: back to next low ptr byte
    dey                                                               ; 9f62: 88          .              ; (continued)
    php                                                               ; 9f63: 08          .              ; Save borrow for next byte
    cpy #8                                                            ; 9f64: c0 08       ..             ; Done all 4 bytes?
    bcc calc_transfer_size                                            ; 9f66: 90 ec       ..             ; No: next byte pair
    plp                                                               ; 9f68: 28          (              ; Discard final borrow
    txa                                                               ; 9f69: 8a          .              ; A = saved X; Save X
    pha                                                               ; 9f6a: 48          H              ; Save X
    lda #4                                                            ; 9f6b: a9 04       ..             ; Compute address of RXCB+4
    clc                                                               ; 9f6d: 18          .              ; CLC for base pointer addition
    adc port_ws_offset                                                ; 9f6e: 65 a6       e.             ; Add RXCB base to get RXCB+4 addr
    tax                                                               ; 9f70: aa          .              ; X = low byte of RXCB+4
    ldy rx_buf_offset                                                 ; 9f71: a4 a7       ..             ; Y = high byte of RXCB ptr
    lda #&c2                                                          ; 9f73: a9 c2       ..             ; Tube claim type &C2
    jsr tube_addr_claim                                               ; 9f75: 20 06 04     ..            ; Claim Tube transfer address
    bcc restore_x_and_return                                          ; 9f78: 90 07       ..             ; No Tube: skip reclaim
    lda scout_status                                                  ; 9f7a: ad 5c 0d    .\.            ; Tube: reclaim with scout status
    jsr tube_addr_claim                                               ; 9f7d: 20 06 04     ..            ; Reclaim with scout status type
    sec                                                               ; 9f80: 38          8              ; C=1: Tube address claimed
; &9f81 referenced 1 time by &9f78
.restore_x_and_return
    pla                                                               ; 9f81: 68          h              ; Restore X
    tax                                                               ; 9f82: aa          .              ; Restore X from stack
    rts                                                               ; 9f83: 60          `              ; Return with C = transfer status

; &9f84 referenced 2 times by &9f41, &9f46
.fallback_calc_transfer
    ldy #4                                                            ; 9f84: a0 04       ..             ; Y=4: RXCB current pointer offset
    lda (port_ws_offset),y                                            ; 9f86: b1 a6       ..             ; Load RXCB[4] (current ptr lo)
    ldy #8                                                            ; 9f88: a0 08       ..             ; Y=8: RXCB start address offset
    sec                                                               ; 9f8a: 38          8              ; Set carry for subtraction
    sbc (port_ws_offset),y                                            ; 9f8b: f1 a6       ..             ; Subtract RXCB[8] (start ptr lo)
    sta port_buf_len                                                  ; 9f8d: 85 a2       ..             ; Store transfer size lo
    ldy #5                                                            ; 9f8f: a0 05       ..             ; Y=5: current ptr hi offset
    lda (port_ws_offset),y                                            ; 9f91: b1 a6       ..             ; Load RXCB[5] (current ptr hi)
    sbc #0                                                            ; 9f93: e9 00       ..             ; Propagate borrow only; Propagate borrow from lo subtraction
    sta open_port_buf_hi                                              ; 9f95: 85 a5       ..             ; Temp store of adjusted hi byte; Temp store adjusted current ptr hi
    ldy #8                                                            ; 9f97: a0 08       ..             ; Y=8: start address lo offset
    lda (port_ws_offset),y                                            ; 9f99: b1 a6       ..             ; Copy RXCB[8] to open port buffer lo; Load RXCB[8] (start ptr lo)
    sta open_port_buf                                                 ; 9f9b: 85 a4       ..             ; Store to scratch (side effect)
    ldy #9                                                            ; 9f9d: a0 09       ..             ; Y=9: start address hi offset
    lda (port_ws_offset),y                                            ; 9f9f: b1 a6       ..             ; Load RXCB[9]; Load RXCB[9] (start ptr hi)
    sec                                                               ; 9fa1: 38          8              ; Set carry for subtraction
    sbc open_port_buf_hi                                              ; 9fa2: e5 a5       ..             ; Subtract adjusted hi byte; start_hi - adjusted current_hi
    sta port_buf_len_hi                                               ; 9fa4: 85 a3       ..             ; Store transfer size hi
    sec                                                               ; 9fa6: 38          8              ; Return with C=1
; &9fa7 referenced 1 time by &968f
.nmi_shim_rom_src
    rts                                                               ; 9fa7: 60          `              ; Return with C=1 (success)

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
    bit station_id_disable_net_nmis                                   ; 9fa8: 2c 18 fe    ,..            ; INTOFF: disable NMIs while switching ROM
    pha                                                               ; 9fab: 48          H              ; Save A
    tya                                                               ; 9fac: 98          .              ; Transfer Y to A
    pha                                                               ; 9fad: 48          H              ; Save Y (via A)
    lda #0                                                            ; 9fae: a9 00       ..             ; ROM bank 0 (patched during init for actual bank)
    sta romsel                                                        ; 9fb0: 8d 30 fe    .0.            ; Select Econet ROM bank via ROMSEL
    jmp nmi_rx_scout                                                  ; 9fb3: 4c f2 96    L..            ; Jump to scout handler in ROM

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
    sty nmi_jmp_hi                                                    ; 9fb6: 8c 0d 0d    ...            ; Store handler high byte at &0D0D
    sta nmi_jmp_lo                                                    ; 9fb9: 8d 0c 0d    ...            ; Store handler low byte at &0D0C
    lda romsel_copy                                                   ; 9fbc: a5 f4       ..             ; Restore NFS ROM bank
    sta romsel                                                        ; 9fbe: 8d 30 fe    .0.            ; Page in via hardware latch
    pla                                                               ; 9fc1: 68          h              ; Restore Y from stack
    tay                                                               ; 9fc2: a8          .              ; Transfer ROM bank to Y
    pla                                                               ; 9fc3: 68          h              ; Restore A from stack
    bit video_ula_control                                             ; 9fc4: 2c 20 fe    , .            ; INTON: re-enable NMIs
    rti                                                               ; 9fc7: 40          @              ; Return from interrupt

    equs "Brian,Hugo,Jes and Roger"                                   ; 9fc8: 42 72 69... Bri

; ***************************************************************************************
; Print byte as two hex digits
; 
; Prints the high nibble first (via 4x LSR), then the low
; nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
; and output via OSASCI. Returns with carry set.
; ***************************************************************************************
; &9fe0 referenced 2 times by &8c8e, &8d67
.print_hex
    pha                                                               ; 9fe0: 48          H              ; Save original byte for low nibble
    lsr a                                                             ; 9fe1: 4a          J              ; Shift high nibble right (4x LSR)
    lsr a                                                             ; 9fe2: 4a          J              ; Shift high nibble to low
    lsr a                                                             ; 9fe3: 4a          J              ; Shift high nibble to low
    lsr a                                                             ; 9fe4: 4a          J              ; Shift high nibble to low
    jsr print_hex_nibble                                              ; 9fe5: 20 e9 9f     ..            ; Print high nibble as hex
    pla                                                               ; 9fe8: 68          h              ; Restore byte; fall through for low nibble
; ***************************************************************************************
; Print single hex nibble
; 
; Converts the low nibble of A to ASCII hex ('0'-'9' or 'A'-'F')
; and prints via OSASCI. Returns with carry set.
; ***************************************************************************************
; &9fe9 referenced 1 time by &9fe5
.print_hex_nibble
    and #&0f                                                          ; 9fe9: 29 0f       ).             ; Mask to low nibble (0-F)
    cmp #&0a                                                          ; 9feb: c9 0a       ..             ; Digit A-F?
    bcc add_ascii_base                                                ; 9fed: 90 02       ..             ; No: skip letter offset
    adc #6                                                            ; 9fef: 69 06       i.             ; A-F: ADC #6 + ADC #&30 + C = &41-&46
; &9ff1 referenced 1 time by &9fed
.add_ascii_base
    adc #&30 ; '0'                                                    ; 9ff1: 69 30       i0             ; Add ASCII '0' base (with carry)
    jsr osasci                                                        ; 9ff3: 20 e3 ff     ..            ; Write character
    sec                                                               ; 9ff6: 38          8              ; C=1: callers use SEC as sentinel
    rts                                                               ; 9ff7: 60          `              ; Return

    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff                       ; 9ff8: ff ff ff... ...
.pydis_end

    assert <(dispatch_net_cmd-1) == &6e
    assert <(econet_tx_rx-1) == &e7
    assert <(fscv_0_opt_entry-1) == &e7
    assert <(fscv_1_eof-1) == &68
    assert <(fscv_2_star_run-1) == &ce
    assert <(fscv_3_star_cmd-1) == &d6
    assert <(fscv_5_cat-1) == &20
    assert <(fscv_6_shutdown-1) == &4c
    assert <(fscv_7_read_handles-1) == &73
    assert <(fsreply_0_print_dir-1) == &88
    assert <(fsreply_1_copy_handles_boot-1) == &29
    assert <(fsreply_2_copy_handles-1) == &2a
    assert <(fsreply_3_set_csd-1) == &23
    assert <(fsreply_4_notify_exec-1) == &d4
    assert <(fsreply_5_set_lib-1) == &1e
    assert <(imm_op_status3-1) == &ca
    assert <(l0128) == &28
    assert <(lang_0_insert_remote_key-1) == &e7
    assert <(lang_1_remote_boot-1) == &99
    assert <(lang_2_save_palette_vdu-1) == &a5
    assert <(lang_3_execute_at_0100-1) == &c7
    assert <(lang_4_remote_validated-1) == &d7
    assert <(net_1_read_handle-1) == &58
    assert <(net_2_read_handle_entry-1) == &5e
    assert <(net_3_close_handle-1) == &6e
    assert <(net_4_resume_remote-1) == &b7
    assert <(net_write_char_handler-1) == &ab
    assert <(nword-1) == &47
    assert <(osword_0f_handler-1) == &b9
    assert <(osword_10_handler-1) == &73
    assert <(osword_11_handler-1) == &d3
    assert <(printer_select_handler-1) == &ce
    assert <(proc_op_status2-1) == &15
    assert <(remote_cmd_dispatch-1) == &dd
    assert <(remote_print_handler-1) == &de
    assert <(return_1-1) == &f5
    assert <(rs-1) == &f8
    assert <(rx_imm_exec-1) == &94
    assert <(rx_imm_halt_cont-1) == &ea
    assert <(rx_imm_machine_type-1) == &bd
    assert <(rx_imm_peek-1) == &d0
    assert <(rx_imm_poke-1) == &b2
    assert <(svc_11_nmi_claim-1) == &68
    assert <(svc_12_nmi_release-1) == &65
    assert <(svc_13_select_nfs-1) == &ec
    assert <(svc_1_abs_workspace-1) == &b7
    assert <(svc_2_private_workspace-1) == &c0
    assert <(svc_3_autoboot-1) == &18
    assert <(svc_4_star_command-1) == &b0
    assert <(svc_5_unknown_irq-1) == &6b
    assert <(svc_8_osword-1) == &7e
    assert <(svc_9_help-1) == &03
    assert <(tx_ctrl_exit-1) == &25
    assert <(tx_ctrl_peek-1) == &ce
    assert <(tx_ctrl_poke-1) == &d2
    assert <(tx_done_continue-1) == &b7
    assert <(tx_done_halt-1) == &a0
    assert <(tx_done_jsr-1) == &7d
    assert <(tx_done_os_proc-1) == &94
    assert <(tx_done_user_proc-1) == &86
    assert >(dispatch_net_cmd-1) == &80
    assert >(econet_tx_rx-1) == &8f
    assert >(fscv_0_opt_entry-1) == &89
    assert >(fscv_1_eof-1) == &88
    assert >(fscv_2_star_run-1) == &8d
    assert >(fscv_3_star_cmd-1) == &8b
    assert >(fscv_5_cat-1) == &8c
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
    assert >(net_write_char_handler-1) == &90
    assert >(nword-1) == &91
    assert >(osword_0f_handler-1) == &8e
    assert >(osword_10_handler-1) == &8f
    assert >(osword_11_handler-1) == &8e
    assert >(printer_select_handler-1) == &91
    assert >(proc_op_status2-1) == &9d
    assert >(remote_cmd_dispatch-1) == &90
    assert >(remote_print_handler-1) == &91
    assert >(return_1-1) == &80
    assert >(rs-1) == &8e
    assert >(rx_imm_exec-1) == &9a
    assert >(rx_imm_halt_cont-1) == &9a
    assert >(rx_imm_machine_type-1) == &9a
    assert >(rx_imm_peek-1) == &9a
    assert >(rx_imm_poke-1) == &9a
    assert >(svc_11_nmi_claim-1) == &96
    assert >(svc_12_nmi_release-1) == &96
    assert >(svc_13_select_nfs-1) == &81
    assert >(svc_1_abs_workspace-1) == &82
    assert >(svc_2_private_workspace-1) == &82
    assert >(svc_3_autoboot-1) == &82
    assert >(svc_4_star_command-1) == &81
    assert >(svc_5_unknown_irq-1) == &96
    assert >(svc_8_osword-1) == &8e
    assert >(svc_9_help-1) == &82
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
;     econet_control23_or_status2:             45
;     fs_options:                              41
;     econet_data_continue_frame:              37
;     fs_cmd_data:                             37
;     port_ws_offset:                          35
;     net_rx_ptr:                              32
;     econet_control1_or_status1:              31
;     osword_pb_ptr:                           26
;     tx_flags:                                26
;     net_tx_ptr:                              25
;     osbyte:                                  23
;     set_nmi_vector:                          22
;     port_buf_len:                            20
;     tube_read_r2:                            20
;     station_id_disable_net_nmis:             17
;     open_port_buf_hi:                        16
;     rx_flags:                                16
;     fs_load_addr_2:                          15
;     fs_func_code:                            14
;     nmi_tx_block:                            14
;     open_port_buf:                           14
;     ws_page:                                 14
;     fs_load_addr:                            13
;     port_buf_len_hi:                         13
;     print_inline:                            13
;     tube_send_r2:                            13
;     ws_ptr_lo:                               13
;     nmi_error_dispatch:                      12
;     prepare_fs_cmd:                          12
;     tube_data_register_2:                    11
;     tx_result_fail:                          11
;     nfs_workspace_hi:                        10
;     svc_state:                               10
;     tube_addr_claim:                         10
;     tube_status_register_2:                  10
;     tube_data_register_3:                     9
;     txcb_end:                                 9
;     fs_error_ptr:                             8
;     net_tx_ptr_hi:                            8
;     rx_buf_offset:                            8
;     rx_src_stn:                               8
;     table_idx:                                8
;     tube_send_r4:                             8
;     tube_status_1_and_tube_control:           8
;     txcb_start:                               8
;     fs_cmd_csd:                               7
;     fs_cmd_urd:                               7
;     fs_crc_lo:                                7
;     fs_work_4:                                7
;     l0d60:                                    7
;     osasci:                                   7
;     prot_status:                              7
;     reject_reply:                             7
;     restore_args_return:                      7
;     tx_clear_flag:                            7
;     tx_dst_stn:                               7
;     copy_string_to_cmd:                       6
;     fs_block_offset:                          6
;     fs_last_byte_flag:                        6
;     fs_load_addr_hi:                          6
;     net_rx_ptr_hi:                            6
;     nmi_rti:                                  6
;     tube_claimed_id:                          6
;     tube_main_loop:                           6
;     zp_ptr_hi:                                6
;     zp_ptr_lo:                                6
;     copy_filename:                            5
;     dispatch:                                 5
;     fs_boot_option:                           5
;     fs_load_addr_3:                           5
;     infol2:                                   5
;     l0100:                                    5
;     l0106:                                    5
;     os_text_ptr:                              5
;     printer_buf_ptr:                          5
;     restore_xy_return:                        5
;     rx_ctrl:                                  5
;     rx_port:                                  5
;     scout_error:                              5
;     scout_status:                             5
;     send_to_fs_star:                          5
;     set_fs_flag:                              5
;     system_via_acr:                           5
;     tube_flag:                                5
;     tube_send_r1:                             5
;     tx_dst_net:                               5
;     clear_jsr_protection:                     4
;     copy_param_workspace:                     4
;     data_tx_error:                            4
;     data_tx_last:                             4
;     discard_reset_listen:                     4
;     econet_init_flag:                         4
;     escape_flag:                              4
;     fs_cmd_context:                           4
;     fs_crflag:                                4
;     fs_data_count:                            4
;     fs_eof_flags:                             4
;     fs_sequence_nos:                          4
;     fs_server_net:                            4
;     init_tx_ctrl_block:                       4
;     l0101:                                    4
;     l0d58:                                    4
;     nmi_next_hi:                              4
;     nmi_next_lo:                              4
;     osbyte_a_copy:                            4
;     osrdsc_ptr:                               4
;     osword_flag:                              4
;     restore_ay_return:                        4
;     return_a_zero:                            4
;     romsel_copy:                              4
;     rx_src_net:                               4
;     tube_reply_byte:                          4
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
;     check_escape_handler:                     3
;     check_tube_irq_loop:                      3
;     clear_fs_flag:                            3
;     data_rx_complete:                         3
;     data_rx_tube_error:                       3
;     discard_listen:                           3
;     dispatch_remote_osbyte:                   3
;     fs_csd_handle:                            3
;     fs_getb_buf:                              3
;     fs_messages_flag:                         3
;     fs_reply_cmd:                             3
;     fs_reply_poll:                            3
;     fs_server_stn:                            3
;     fs_spool0:                                3
;     fs_spool_handle:                          3
;     fs_urd_handle:                            3
;     fs_work_7:                                3
;     handle_to_mask_a:                         3
;     language_entry:                           3
;     match_osbyte_code:                        3
;     next_port_slot:                           3
;     nmi_jmp_hi:                               3
;     nmi_jmp_lo:                               3
;     nmi_tx_block_hi:                          3
;     openl4:                                   3
;     oscli:                                    3
;     osnewl:                                   3
;     osword:                                   3
;     oswrch:                                   3
;     pad_filename_spaces:                      3
;     print_reply_bytes:                        3
;     pydis_start:                              3
;     return_1:                                 3
;     rom_header:                               3
;     rom_ws_table:                             3
;     rx_check_error:                           3
;     rx_update_buf:                            3
;     save_fscv_args:                           3
;     save_fscv_args_with_ptrs:                 3
;     saved_jsr_mask:                           3
;     scout_no_match:                           3
;     setup_tx_and_send:                        3
;     test_inactive_retry:                      3
;     tube_claim_loop:                          3
;     tube_data_register_1:                     3
;     tube_read_string:                         3
;     tube_reply_ack:                           3
;     tube_xfer_page:                           3
;     tx_active_start:                          3
;     tx_calc_transfer:                         3
;     tx_ctrl_upper:                            3
;     tx_index:                                 3
;     write_second_tube_byte:                   3
;     zp_work_3:                                3
;     ack_scout_match:                          2
;     ack_tx:                                   2
;     ack_tx_write_dest:                        2
;     adjust_addrs:                             2
;     adlc_detect_done:                         2
;     adlc_rx_listen:                           2
;     advance_rx_buffer_ptr:                    2
;     binary_version:                           2
;     boot_option_text:                         2
;     brk_ptr:                                  2
;     call_fscv_shutdown:                       2
;     check_rom_end:                            2
;     check_svc_12:                             2
;     claim_addr_ff:                            2
;     compare_addresses:                        2
;     copy_filename_to_cmd:                     2
;     copy_load_addr_from_params:               2
;     copy_reply_to_caller:                     2
;     copy_reply_to_params:                     2
;     ctrl_block_setup_alt:                     2
;     data_rx_tube_complete:                    2
;     decode_attribs_5bit:                      2
;     decode_attribs_6bit:                      2
;     dir_column_check:                         2
;     dispatch_nmi_error:                       2
;     econet_tx_retry:                          2
;     exec_at_load_addr:                        2
;     execute_downloaded:                       2
;     fallback_calc_transfer:                   2
;     flush_output_block:                       2
;     fs_access_level:                          2
;     fs_cmd_lib:                               2
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
;     fs_work_5:                                2
;     gbpb_done:                                2
;     gsinit:                                   2
;     gsread:                                   2
;     handle_mask_exit:                         2
;     handle_to_mask_clc:                       2
;     imm_op_discard:                           2
;     imm_op_dispatch:                          2
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
;     load_handle_calc_offset:                  2
;     mask_to_handle:                           2
;     match_rom_string:                         2
;     msdely:                                   2
;     next_filename_char:                       2
;     nlisne:                                   2
;     nmi_vec_lo_match:                         2
;     not_svc_12_nfs:                           2
;     num01:                                    2
;     os_text_ptr_hi:                           2
;     osarg1:                                   2
;     osfind:                                   2
;     osrdch:                                   2
;     osword_pb_ptr_hi:                         2
;     parse_decimal:                            2
;     parse_filename_gs:                        2
;     poll_tube_ready:                          2
;     prepare_cmd_clv:                          2
;     prepare_fs_cmd_v:                         2
;     print_decimal:                            2
;     print_decimal_digit:                      2
;     print_dir_from_offset:                    2
;     print_file_info:                          2
;     print_hex:                                2
;     print_hex_bytes:                          2
;     print_reply_counted:                      2
;     prlp1:                                    2
;     read_station_id:                          2
;     readc1:                                   2
;     reenable_rx:                              2
;     remot1:                                   2
;     return_3:                                 2
;     return_4:                                 2
;     return_5:                                 2
;     return_7:                                 2
;     return_match_osbyte:                      2
;     return_nbyte:                             2
;     return_printer_select:                    2
;     return_service:                           2
;     return_tube_init:                         2
;     romsel:                                   2
;     run_fscv_cmd:                             2
;     rx_complete_update_rxcb:                  2
;     rx_extra_byte:                            2
;     rxpol2:                                   2
;     scan_for_colon:                           2
;     scout_complete:                           2
;     send_ack:                                 2
;     send_data_blocks:                         2
;     send_data_rx_ack:                         2
;     send_fs_reply_cmd:                        2
;     setup_tx_ptr_c0:                          2
;     skip_addr_carry:                          2
;     skip_buf_ptr_update:                      2
;     skip_nmi_release:                         2
;     skip_space_next:                          2
;     skip_spaces:                              2
;     skip_stn_parse:                           2
;     store_handle_return:                      2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     store_tube_flag:                          2
;     store_tx_error:                           2
;     sub_3_from_y:                             2
;     system_via_ier:                           2
;     system_via_ifr:                           2
;     system_via_sr:                            2
;     terminate_filename:                       2
;     trampoline_tx_setup:                      2
;     transfer_file_blocks:                     2
;     tube_claim_flag:                          2
;     tube_data_ptr:                            2
;     tube_dispatch_table:                      2
;     tube_init_reloc:                          2
;     tube_osword_read_lp:                      2
;     tube_rdch_reply:                          2
;     tube_status_register_4_and_cpu_control:   2
;     tube_transfer_addr:                       2
;     tube_xfer_addr_2:                         2
;     tube_xfer_addr_3:                         2
;     tx_ctrl_byte:                             2
;     tx_not_listening:                         2
;     tx_port:                                  2
;     tx_result_ok:                             2
;     tx_src_stn:                               2
;     tx_store_result:                          2
;     tx_work_51:                               2
;     tx_work_57:                               2
;     zp_work_2:                                2
;     accept_frame:                             1
;     accept_local_net:                         1
;     accept_new_claim:                         1
;     accept_scout_net:                         1
;     access_bit_table:                         1
;     ack_tx_configure:                         1
;     add_4_to_y:                               1
;     add_5_to_y:                               1
;     add_ascii_base:                           1
;     add_bytes_loop:                           1
;     add_rxcb_ptr:                             1
;     addr_claim_external:                      1
;     adjust_addr_byte:                         1
;     adjust_addrs_1:                           1
;     adjust_addrs_9:                           1
;     adjust_addrs_clc:                         1
;     adlc_init:                                1
;     argsv_check_return:                       1
;     argsv_fs_query:                           1
;     argsw:                                    1
;     attrib_error_exit:                        1
;     attrib_shift_bits:                        1
;     bgetv_shared_jsr:                         1
;     block_addr_loop:                          1
;     boot_oscli_offset:                        1
;     brkv:                                     1
;     bspsx:                                    1
;     bsxl0:                                    1
;     bsxl1:                                    1
;     build_send_fs_cmd:                        1
;     bytex:                                    1
;     calc_peek_poke_size:                      1
;     calc_transfer_size:                       1
;     cat_check_access:                         1
;     cat_column_separator:                     1
;     cattxt:                                   1
;     cb_template_main_start:                   1
;     cb_template_tail:                         1
;     cbset2:                                   1
;     cbset3:                                   1
;     cbset4:                                   1
;     cha4:                                     1
;     cha5:                                     1
;     cha5lp:                                   1
;     cha6:                                     1
;     chalp1:                                   1
;     chalp2:                                   1
;     check_attrib_result:                      1
;     check_break_type:                         1
;     check_cb1_irq:                            1
;     check_fs_error:                           1
;     check_fv_final_ack:                       1
;     check_handshake_bit:                      1
;     check_irq_loop:                           1
;     check_opt1:                               1
;     check_port_slot:                          1
;     check_sr2_loop_again:                     1
;     check_station_filter:                     1
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
;     copy_param_ptr:                           1
;     copy_params_rword:                        1
;     copy_reply_bytes:                         1
;     copy_rxcb_to_param:                       1
;     copy_save_params:                         1
;     copy_scout_fields:                        1
;     copy_scout_loop:                          1
;     copy_string_from_offset:                  1
;     copy_vectors_loop:                        1
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
;     dir_print_char:                           1
;     direct_attr_copy:                         1
;     discard_after_reset:                      1
;     dispatch_0_hi-1:                          1
;     dispatch_0_lo-1:                          1
;     dispatch_cmd:                             1
;     dispatch_fs_error:                        1
;     divide_subtract:                          1
;     do_svc_dispatch:                          1
;     dofs01:                                   1
;     dofs2:                                    1
;     dofsl5:                                   1
;     dofsl7:                                   1
;     done_option_name:                         1
;     econet_data_terminate_frame:              1
;     enable_irq_and_tx:                        1
;     enter_rx_listen:                          1
;     entry1:                                   1
;     error1:                                   1
;     error_code_clamped:                       1
;     error_msg_table:                          1
;     error_not_listening:                      1
;     error_offsets:                            1
;     evntv:                                    1
;     fetch_dir_batch:                          1
;     file1:                                    1
;     filev:                                    1
;     filev_attrib_dispatch:                    1
;     filev_save:                               1
;     floop:                                    1
;     flush_r3_nmi_check:                       1
;     fs2al1:                                   1
;     fs_addr_check:                            1
;     fs_boot_data:                             1
;     fs_cmd_dispatch_hi:                       1
;     fs_cmd_ptr:                               1
;     fs_cmd_type:                              1
;     fs_context_base:                          1
;     fs_context_hi:                            1
;     fs_error_buf:                             1
;     fs_file_attrs:                            1
;     fs_file_len:                              1
;     fs_len_clear:                             1
;     fs_load_upper:                            1
;     fs_osword_dispatch:                       1
;     fs_osword_tbl_hi:                         1
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
;     got_station_num:                          1
;     halt_spin_loop:                           1
;     halve_args_a:                             1
;     handle_bput_bget:                         1
;     handle_to_mask:                           1
;     handle_tx_result:                         1
;     handshake_await_ack:                      1
;     imm_dispatch_lo:                          1
;     imm_op_build_reply:                       1
;     immediate_op:                             1
;     inactive_retry:                           1
;     info2:                                    1
;     init_cat_params:                          1
;     init_fs_vectors:                          1
;     init_nmi_workspace:                       1
;     init_rxcb_entries:                        1
;     init_tx_ctrl_port:                        1
;     init_tx_reply_port:                       1
;     init_vectors_and_copy:                    1
;     initl:                                    1
;     install_data_rx_handler:                  1
;     install_imm_data_nmi:                     1
;     install_reply_scout:                      1
;     install_saved_handler:                    1
;     install_tube_rx:                          1
;     intoff_test_inactive:                     1
;     issue_vectors_claimed:                    1
;     jmp_tx_result_fail:                       1
;     jump_via_addr:                            1
;     l0006:                                    1
;     l0063:                                    1
;     l0104:                                    1
;     l0350:                                    1
;     l0351:                                    1
;     l0355:                                    1
;     l0cff:                                    1
;     l0e11:                                    1
;     l4:                                       1
;     l9556:                                    1
;     lang_entry_hi:                            1
;     lang_entry_lo:                            1
;     language_handler:                         1
;     loadop:                                   1
;     lodchk:                                   1
;     lodfil:                                   1
;     lodrl1:                                   1
;     lodrl2:                                   1
;     logon2:                                   1
;     map_attrib_bits:                          1
;     match_cmd_chars:                          1
;     match_net_cmd:                            1
;     mj:                                       1
;     nbyte1:                                   1
;     nbyte4:                                   1
;     nbyte5:                                   1
;     nbyte6:                                   1
;     netv:                                     1
;     netvec_handler_hi:                        1
;     next_block:                               1
;     next_dir_entry:                           1
;     next_rom_page:                            1
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
;     nmi_workspace_start:                      1
;     no_adlc_found:                            1
;     no_dot_exit:                              1
;     no_page_wrap:                             1
;     openl6:                                   1
;     openl7:                                   1
;     opt_return:                               1
;     opter1:                                   1
;     optl1:                                    1
;     osargs:                                   1
;     osbget:                                   1
;     osbput:                                   1
;     oseven:                                   1
;     osfile:                                   1
;     osgbpb:                                   1
;     osgbpb_info:                              1
;     osrdsc_ptr_hi:                            1
;     osword_12_offsets:                        1
;     osword_handler_lo:                        1
;     osword_tbl_lo:                            1
;     osword_trampoline:                        1
;     parse_decimal_rts:                        1
;     parse_filename_gs_y:                      1
;     poll_nmi_ready:                           1
;     poll_r2_osword_result:                    1
;     poll_r4_copro_ack:                        1
;     poll_rxcb_loop:                           1
;     prepare_cmd_dispatch:                     1
;     prepare_cmd_with_flag:                    1
;     pril1:                                    1
;     print_digit:                              1
;     print_exec_and_len:                       1
;     print_hex_fields:                         1
;     print_hex_nibble:                         1
;     print_inline_char:                        1
;     print_newline:                            1
;     print_next_char:                          1
;     print_public:                             1
;     print_space:                              1
;     print_station_info:                       1
;     quote1:                                   1
;     r2_cmd_table:                             1
;     rchex:                                    1
;     read_args_size:                           1
;     read_fs_handle:                           1
;     read_osargs_params:                       1
;     read_osgbpb_ctrl_blk:                     1
;     read_rdln_ctrl_block:                     1
;     read_remote_cmd_line:                     1
;     read_rxcb:                                1
;     read_second_rx_byte:                      1
;     read_sr2_between_pairs:                   1
;     read_vdu_osbyte:                          1
;     read_vdu_osbyte_x0:                       1
;     readry:                                   1
;     reloc_p4_src:                             1
;     reloc_p5_src:                             1
;     reloc_zp_src:                             1
;     remote_osbyte_table:                      1
;     restore_x_and_return:                     1
;     return_10:                                1
;     return_2:                                 1
;     return_6:                                 1
;     return_8:                                 1
;     return_calc_handle:                       1
;     return_compare:                           1
;     return_dofsl7:                            1
;     return_last_error:                        1
;     return_lodchk:                            1
;     rom_type:                                 1
;     rotate_prot_mask:                         1
;     rsl1:                                     1
;     rssl1:                                    1
;     rssl2:                                    1
;     rx_error:                                 1
;     rx_error_reset:                           1
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
;     scan_entry_terminator:                    1
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
;     send_block:                               1
;     send_block_loop:                          1
;     send_data_bytes:                          1
;     send_fs_cmd_v1:                           1
;     send_fs_examine:                          1
;     send_fs_reply:                            1
;     send_osargs_result:                       1
;     send_osfile_ctrl_blk:                     1
;     send_osgbpb_result:                       1
;     send_rom_page_bytes:                      1
;     send_xfer_addr_bytes:                     1
;     service_entry:                            1
;     service_handler:                          1
;     set_listen_offset:                        1
;     set_messages_flag:                        1
;     set_tx_reply_flag:                        1
;     set_workspace_page:                       1
;     setup1:                                   1
;     setup_data_xfer:                          1
;     setup_rom_ptrs_netv:                      1
;     setup_rx_buffer_ptrs:                     1
;     setup_unicast_xfer:                       1
;     skip_buf_setup:                           1
;     skip_clear_flag:                          1
;     skip_cmd_spaces:                          1
;     skip_copy_reply:                          1
;     skip_gs_filename:                         1
;     skip_kbd_reenable:                        1
;     skip_lodfil:                              1
;     skip_no_clock_msg:                        1
;     skip_param_read:                          1
;     skip_param_write:                         1
;     skip_set_attrib_bit:                      1
;     skip_tube_update:                         1
;     sr2_idle_status:                          1
;     start_data_tx:                            1
;     store_16bit_at_y:                         1
;     store_buf_ptr_lo:                         1
;     store_fs_error:                           1
;     store_fs_flag:                            1
;     store_fs_hdr_clc:                         1
;     store_fs_hdr_fn:                          1
;     store_retry_count:                        1
;     store_rxcb_buf_hi:                        1
;     store_status_add4:                        1
;     store_status_copy_ptr:                    1
;     store_txcb_byte:                          1
;     store_xfer_end_addr:                      1
;     string_buf_done:                          1
;     strnh:                                    1
;     sub_4_from_y:                             1
;     subtract_adjust:                          1
;     svc_dispatch_range:                       1
;     svc_entry_lo:                             1
;     svc_unhandled_return:                     1
;     tbcop1:                                   1
;     toggle_print_flag:                        1
;     trampoline_adlc_init:                     1
;     tube_begin:                               1
;     tube_brk_handler:                         1
;     tube_brk_send_loop:                       1
;     tube_chars_done:                          1
;     tube_claim_default:                       1
;     tube_code_page4:                          1
;     tube_data_ptr_hi:                         1
;     tube_data_register_4:                     1
;     tube_escape_check:                        1
;     tube_handle_wrch:                         1
;     tube_jmp_target:                          1
;     tube_osbyte_send_y:                       1
;     tube_osfind_close:                        1
;     tube_osword_read:                         1
;     tube_osword_write:                        1
;     tube_osword_write_lp:                     1
;     tube_page6_start:                         1
;     tube_poll_r2:                             1
;     tube_poll_r2_result:                      1
;     tube_post_init:                           1
;     tube_rdln_send_line:                      1
;     tube_rdln_send_loop:                      1
;     tube_reset_stack:                         1
;     tube_return_main:                         1
;     tube_send_error_byte:                     1
;     tube_send_release:                        1
;     tube_send_zero_r2:                        1
;     tube_sendw_complete:                      1
;     tube_transfer:                            1
;     tube_transfer_setup:                      1
;     tube_tx_count_2:                          1
;     tube_tx_count_4:                          1
;     tube_tx_fifo_write:                       1
;     tx_begin:                                 1
;     tx_ctrl_exit:                             1
;     tx_ctrl_range_check:                      1
;     tx_ctrl_template:                         1
;     tx_data_start:                            1
;     tx_done_classify:                         1
;     tx_done_error:                            1
;     tx_done_handler_hi:                       1
;     tx_done_handler_lo:                       1
;     tx_error:                                 1
;     tx_fifo_not_ready:                        1
;     tx_fifo_write:                            1
;     tx_imm_op_setup:                          1
;     tx_last_data:                             1
;     tx_line_idle_check:                       1
;     tx_line_jammed:                           1
;     tx_no_clock_error:                        1
;     tx_poll_status:                           1
;     tx_prepare:                               1
;     tx_retry:                                 1
;     tx_semaphore_spin:                        1
;     tx_src_net:                               1
;     tx_store_error:                           1
;     tx_success:                               1
;     txcb_dest:                                1
;     txcb_pos:                                 1
;     update_sequence_return:                   1
;     vdu_osbyte_table:                         1
;     wait_fs_reply:                            1
;     wait_tube_delay:                          1
;     work_ae:                                  1
;     write_second_tx_byte:                     1
;     y2fsl2:                                   1
;     y2fsl5:                                   1
;     zero_cmd_bytes:                           1
;     zero_exec_header:                         1

; Automatically generated labels:
;     l0006
;     l0063
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
;     l9556

; Stats:
;     Total size (Code + Data) = 8192 bytes
;     Code                     = 7501 bytes (92%)
;     Data                     = 691 bytes (8%)
;
;     Number of instructions   = 3616
;     Number of data bytes     = 448 bytes
;     Number of data words     = 0 bytes
;     Number of string bytes   = 243 bytes
;     Number of strings        = 34
