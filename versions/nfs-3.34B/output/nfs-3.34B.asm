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
osbyte_read_write_last_break_type           = 253
osbyte_read_write_spool_file_handle         = 199
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
l00b6                                   = &00b6
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
l0130                                   = &0130
brkv                                    = &0202
wrchv                                   = &020e
rdchv                                   = &0210
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
l0dda                                   = &0dda
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
l0e0c                                   = &0e0c
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
l0fc5                                   = &0fc5
l0fc6                                   = &0fc6
fs_putb_buf                             = &0fdc
fs_getb_buf                             = &0fdd
fs_handle_mask                          = &0fde
fs_error_flags                          = &0fdf
fs_error_buf                            = &0fe0
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
osasci                                  = &ffe3
osnewl                                  = &ffe7
osword                                  = &fff1
osbyte                                  = &fff4
oscli                                   = &fff7

    org &9308

.reloc_zp_src

; Move 1: &9308 to &16 for length 69
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
; The main loop continuously polls R4 for WRCH requests (forwarded
; to OSWRITCH &FFCB) and R2 for command bytes (dispatched via the
; 14-entry table at &0500). The R2 command byte is stored at &55
; before dispatch via JMP (&0500).
; ***************************************************************************************
; &9308 referenced 1 time by &8116
.nmi_workspace_start
.tube_brk_handler
    lda #&ff                                                          ; 9308: a9 ff       ..  :0016[1]   ; A=&FF: signal error to co-processor via R4
    jsr tube_send_r4                                                  ; 930a: 20 d9 06     .. :0018[1]   ; Send &FF error signal to Tube R4
    lda tube_data_register_2                                          ; 930d: ad e3 fe    ... :001b[1]   ; Flush any pending R2 byte
    lda #0                                                            ; 9310: a9 00       ..  :001e[1]   ; A=0: send zero prefix to R2
.tube_send_zero_r2
    jsr tube_send_r2                                                  ; 9312: 20 d0 06     .. :0020[1]   ; Send zero prefix byte via R2
    tay                                                               ; 9315: a8          .   :0023[1]   ; Y=0: start of error block at (&FD)
    lda (brk_ptr),y                                                   ; 9316: b1 fd       ..  :0024[1]   ; Load error number from (&FD),0
    jsr tube_send_r2                                                  ; 9318: 20 d0 06     .. :0026[1]   ; Send error number via R2
; &931b referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 931b: c8          .   :0029[1]   ; Advance to next error string byte
.tube_send_error_byte
    lda (brk_ptr),y                                                   ; 931c: b1 fd       ..  :002a[1]   ; Load next error string byte
    jsr tube_send_r2                                                  ; 931e: 20 d0 06     .. :002c[1]   ; Send error string byte via R2
    tax                                                               ; 9321: aa          .   :002f[1]   ; Zero byte = end of error string
    bne tube_brk_send_loop                                            ; 9322: d0 f7       ..  :0030[1]   ; Loop until zero terminator sent
.tube_reset_stack
    ldx #&ff                                                          ; 9324: a2 ff       ..  :0032[1]   ; Reset stack pointer to top
    txs                                                               ; 9326: 9a          .   :0034[1]   ; TXS: set stack pointer from X
    cli                                                               ; 9327: 58          X   :0035[1]   ; Enable interrupts for main loop
; ***************************************************************************************
; Save registers and enter Tube polling loop
; 
; Saves X and Y to zp_temp_11/zp_temp_10, then falls through
; to tube_main_loop which polls Tube R1 (WRCH) and R2 (command)
; registers in an infinite loop. Called from tube_init_reloc
; after ROM relocation and from tube_dispatch_table handlers
; that need to restart the main loop.
; ***************************************************************************************
; &9328 referenced 2 times by &04ec[2], &053a[3]
.tube_enter_main_loop
    stx zp_temp_11                                                    ; 9328: 86 11       ..  :0036[1]   ; Save X to temporary
    sty zp_temp_10                                                    ; 932a: 84 10       ..  :0038[1]   ; Save Y to temporary
; &932c referenced 7 times by &0048[1], &05ae[3], &05d5[3], &0623[4], &0638[4], &06a0[4], &06cd[4]
.tube_main_loop
    bit tube_status_register_4_and_cpu_control                        ; 932c: 2c e6 fe    ,.. :003a[1]   ; BIT R4 status: check WRCH request
    bpl tube_poll_r2                                                  ; 932f: 10 06       ..  :003d[1]   ; R1 not ready: check R2 instead
; &9331 referenced 1 time by &004d[1]
.tube_handle_wrch
    lda tube_data_register_4                                          ; 9331: ad e7 fe    ... :003f[1]   ; Read character from Tube R4 data
    jsr nvwrch                                                        ; 9334: 20 cb ff     .. :0042[1]   ; Write character
; &9337 referenced 1 time by &003d[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 9337: 2c e2 fe    ,.. :0045[1]   ; BIT R2 status: check command byte
    bpl tube_main_loop                                                ; 933a: 10 f0       ..  :0048[1]   ; R2 not ready: loop back to R1 check
    bit tube_status_register_4_and_cpu_control                        ; 933c: 2c e6 fe    ,.. :004a[1]   ; Re-check R4: WRCH has priority over R2
    bmi tube_handle_wrch                                              ; 933f: 30 f0       0.  :004d[1]   ; R1 ready: handle WRCH first
    ldx tube_data_register_2                                          ; 9341: ae e3 fe    ... :004f[1]   ; Read command byte from Tube R2 data
    stx tube_dispatch_ptr_lo                                          ; 9344: 86 55       .U  :0052[1]   ; Self-modify JMP low byte for dispatch
.tube_dispatch_cmd
tube_dispatch_ptr_lo = tube_dispatch_cmd+1
    jmp (tube_dispatch_table)                                         ; 9346: 6c 00 05    l.. :0054[1]   ; Dispatch to handler via indirect JMP

; &9347 referenced 1 time by &0052[1]
; &9349 referenced 2 times by &0478[2], &0493[2]
.tube_transfer_addr
    equb 0                                                            ; 9349: 00          .   :0057[1]
; &934a referenced 2 times by &047c[2], &0498[2]
.tube_xfer_page
    equb &80                                                          ; 934a: 80          .   :0058[1]
; &934b referenced 1 time by &04a2[2]
.tube_xfer_addr_2
    equb 0                                                            ; 934b: 00          .   :0059[1]
; &934c referenced 1 time by &04a0[2]
.tube_xfer_addr_3
    equb 0                                                            ; 934c: 00          .   :005a[1]

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

; Move 2: &934d to &0400 for length 256
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
; &934d referenced 1 time by &80fc
.tube_code_page4
    jmp tube_begin                                                    ; 934d: 4c 73 04    Ls. :0400[2]   ; JMP to BEGIN startup entry

.tube_escape_entry
    jmp tube_escape_check                                             ; 9350: 4c e2 06    L.. :0403[2]   ; JMP to tube_escape_check (&06A7)

; &9353 referenced 10 times by &04bc[2], &04e4[2], &8b1e, &8b30, &8b8d, &8daa, &99f0, &9a3d, &9f98, &9fa0
.tube_addr_claim
    cmp #&80                                                          ; 9353: c9 80       ..  :0406[2]   ; A>=&80: address claim; A<&80: data transfer
    bcc setup_data_transfer                                           ; 9355: 90 1c       ..  :0408[2]   ; A<&80: data transfer setup (SENDW)
    cmp #&c0                                                          ; 9357: c9 c0       ..  :040a[2]   ; A>=&C0: new address claim from another host
    bcs addr_claim_external                                           ; 9359: b0 0b       ..  :040c[2]   ; C=1: external claim, check ownership
    ora #&40 ; '@'                                                    ; 935b: 09 40       .@  :040e[2]   ; Map &80-&BF range to &C0-&FF for comparison
    cmp tube_claimed_id                                               ; 935d: c5 15       ..  :0410[2]   ; Is this for our currently-claimed address?
    bne return_tube_init                                              ; 935f: d0 11       ..  :0412[2]   ; Not our address: return
; &9361 referenced 1 time by &810e
.tube_post_init
    lda #&80                                                          ; 9361: a9 80       ..  :0414[2]   ; &80 sentinel: clear address claim
    sta tube_claim_flag                                               ; 9363: 85 14       ..  :0416[2]   ; Store to claim-in-progress flag
    rts                                                               ; 9365: 60          `   :0418[2]   ; Return from tube_post_init

; &9366 referenced 1 time by &040c[2]
.addr_claim_external
    asl tube_claim_flag                                               ; 9366: 06 14       ..  :0419[2]   ; Another host claiming; check if we're owner
    bcs accept_new_claim                                              ; 9368: b0 06       ..  :041b[2]   ; C=1: we have an active claim
    cmp tube_claimed_id                                               ; 936a: c5 15       ..  :041d[2]   ; Compare with our claimed address
    beq return_tube_init                                              ; 936c: f0 04       ..  :041f[2]   ; Match: return (we already have it)
    clc                                                               ; 936e: 18          .   :0421[2]   ; Not ours: CLC = we don't own this address
    rts                                                               ; 936f: 60          `   :0422[2]   ; Return with C=0 (claim denied)

; &9370 referenced 1 time by &041b[2]
.accept_new_claim
    sta tube_claimed_id                                               ; 9370: 85 15       ..  :0423[2]   ; Accept new claim: update our address
; &9372 referenced 2 times by &0412[2], &041f[2]
.return_tube_init
    rts                                                               ; 9372: 60          `   :0425[2]   ; Return with address updated

; &9373 referenced 1 time by &0408[2]
.setup_data_transfer
    sty tube_data_ptr_hi                                              ; 9373: 84 13       ..  :0426[2]   ; Save 16-bit transfer address from (X,Y)
    stx tube_data_ptr                                                 ; 9375: 86 12       ..  :0428[2]   ; Store address pointer low byte
    jsr tube_send_r4                                                  ; 9377: 20 d9 06     .. :042a[2]   ; Send transfer type byte to co-processor
    tax                                                               ; 937a: aa          .   :042d[2]   ; X = transfer type for table lookup
    ldy #3                                                            ; 937b: a0 03       ..  :042e[2]   ; Y=3: send 4 bytes (address + claimed addr)
; &937d referenced 1 time by &0436[2]
.send_xfer_addr_bytes
    lda (tube_data_ptr),y                                             ; 937d: b1 12       ..  :0430[2]   ; Load transfer address byte from (X,Y)
    jsr tube_send_r4                                                  ; 937f: 20 d9 06     .. :0432[2]   ; Send address byte to co-processor via R4
    dey                                                               ; 9382: 88          .   :0435[2]   ; Previous byte (big-endian: 3,2,1,0)
    bpl send_xfer_addr_bytes                                          ; 9383: 10 f8       ..  :0436[2]   ; Loop for all 4 address bytes
    ldy #8                                                            ; 9385: a0 08       ..  :0438[2]   ; Y=8: write to Tube control register
    sty tube_status_1_and_tube_control                                ; 9387: 8c e0 fe    ... :043a[2]   ; Configure Tube for data transfer
    ldy #&10                                                          ; 938a: a0 10       ..  :043d[2]   ; Y=&10: data transfer control value
    cpx #2                                                            ; 938c: e0 02       ..  :043f[2]   ; Check transfer type (X=2?)
    bcc tube_ctrl_write_2                                             ; 938e: 90 02       ..  :0441[2]   ; X<2: skip alternate control
    ldy #&90                                                          ; 9390: a0 90       ..  :0443[2]   ; Y=&90: alternate control for X>=2
; &9392 referenced 1 time by &0441[2]
.tube_ctrl_write_2
    sty tube_status_1_and_tube_control                                ; 9392: 8c e0 fe    ... :0445[2]   ; Write transfer control to Tube
    jsr tube_send_r4                                                  ; 9395: 20 d9 06     .. :0448[2]   ; Send data byte via Tube R4
    ldy #&88                                                          ; 9398: a0 88       ..  :044b[2]   ; Y=&88: post-transfer control value
    txa                                                               ; 939a: 8a          .   :044d[2]   ; Transfer type to A for comparison
    beq flush_r3_nmi_check                                            ; 939b: f0 14       ..  :044e[2]   ; Type 0: go to NMI flush check
    cmp #2                                                            ; 939d: c9 02       ..  :0450[2]   ; Check if type 2
    beq flush_r3_nmi_check                                            ; 939f: f0 10       ..  :0452[2]   ; Type 2: go to NMI flush check
    sty tube_status_1_and_tube_control                                ; 93a1: 8c e0 fe    ... :0454[2]   ; Write post-transfer control
    cmp #4                                                            ; 93a4: c9 04       ..  :0457[2]   ; Check if type 4 (SENDW)
    bne return_tube_xfer                                              ; 93a6: d0 17       ..  :0459[2]   ; Not SENDW type: skip release path
    pla                                                               ; 93a8: 68          h   :045b[2]   ; Discard return address (low byte)
    pla                                                               ; 93a9: 68          h   :045c[2]   ; Discard return address (high byte)
; &93aa referenced 1 time by &04b8[2]
.release_claim_restart
    lda #&80                                                          ; 93aa: a9 80       ..  :045d[2]   ; A=&80: reset claim flag sentinel
    sta tube_claim_flag                                               ; 93ac: 85 14       ..  :045f[2]   ; Clear claim-in-progress flag
    jmp tube_reply_byte                                               ; 93ae: 4c cd 05    L.. :0461[2]   ; Restart Tube main loop

; &93b1 referenced 3 times by &044e[2], &0452[2], &0467[2]
.flush_r3_nmi_check
    bit tube_status_register_4_and_cpu_control                        ; 93b1: 2c e6 fe    ,.. :0464[2]   ; Poll R4 status: wait for transfer ready
    bvc flush_r3_nmi_check                                            ; 93b4: 50 fb       P.  :0467[2]   ; V=0: not ready, poll again
    bit tube_data_register_3                                          ; 93b6: 2c e5 fe    ,.. :0469[2]   ; Flush Tube R3 data register
    bit tube_data_register_3                                          ; 93b9: 2c e5 fe    ,.. :046c[2]   ; Flush Tube R3 again
    sty tube_status_1_and_tube_control                                ; 93bc: 8c e0 fe    ... :046f[2]   ; Write final control value
; &93bf referenced 1 time by &0459[2]
.return_tube_xfer
    rts                                                               ; 93bf: 60          `   :0472[2]   ; Return from Tube data setup

; &93c0 referenced 1 time by &0400[2]
.tube_begin
    cli                                                               ; 93c0: 58          X   :0473[2]   ; BEGIN: enable interrupts for Tube host code
    php                                                               ; 93c1: 08          .   :0474[2]   ; Save processor status
    pha                                                               ; 93c2: 48          H   :0475[2]   ; Save A on stack
    ldy #0                                                            ; 93c3: a0 00       ..  :0476[2]   ; Y=0: start at beginning of page
    sty tube_transfer_addr                                            ; 93c5: 84 57       .W  :0478[2]   ; Store to zero page pointer low byte
; ***************************************************************************************
; Initialise relocation address for ROM transfer
; 
; Sets source page to &8000 and page counter to &80. Checks
; ROM type bit 5 for a relocation address in the ROM header;
; if present, extracts the 4-byte address from after the
; copyright string. Otherwise uses default &8000 start.
; ***************************************************************************************
.tube_init_reloc
    lda #&80                                                          ; 93c7: a9 80       ..  :047a[2]   ; Init: start sending from &8000
    sta tube_xfer_page                                                ; 93c9: 85 58       .X  :047c[2]   ; Store &80 as source page high byte
    sta zp_ptr_hi                                                     ; 93cb: 85 01       ..  :047e[2]   ; Store &80 as page counter initial value
    lda #&20 ; ' '                                                    ; 93cd: a9 20       .   :0480[2]   ; A=&20: bit 5 mask for ROM type check
    and rom_type                                                      ; 93cf: 2d 06 80    -.. :0482[2]   ; ROM type bit 5: reloc address in header?
    beq store_xfer_end_addr                                           ; 93d2: f0 19       ..  :0485[2]   ; No reloc addr: use defaults
    ldx copyright_offset                                              ; 93d4: ae 07 80    ... :0487[2]   ; Skip past copyright string to find reloc addr
; &93d7 referenced 1 time by &048e[2]
.scan_copyright_end
    inx                                                               ; 93d7: e8          .   :048a[2]   ; Skip past null-terminated copyright string
    lda rom_header,x                                                  ; 93d8: bd 00 80    ... :048b[2]   ; Load next byte from ROM header
    bne scan_copyright_end                                            ; 93db: d0 fa       ..  :048e[2]   ; Loop until null terminator found
    lda lang_entry_lo,x                                               ; 93dd: bd 01 80    ... :0490[2]   ; Read 4-byte reloc address from ROM header
    sta tube_transfer_addr                                            ; 93e0: 85 57       .W  :0493[2]   ; Store reloc addr byte 1 as transfer addr
    lda lang_entry_hi,x                                               ; 93e2: bd 02 80    ... :0495[2]   ; Load reloc addr byte 2
    sta tube_xfer_page                                                ; 93e5: 85 58       .X  :0498[2]   ; Store as source page start
    ldy service_entry,x                                               ; 93e7: bc 03 80    ... :049a[2]   ; Load reloc addr byte 3
    lda svc_entry_lo,x                                                ; 93ea: bd 04 80    ... :049d[2]   ; Load reloc addr byte 4 (highest)
; &93ed referenced 1 time by &0485[2]
.store_xfer_end_addr
    sta tube_xfer_addr_3                                              ; 93ed: 85 5a       .Z  :04a0[2]   ; Store high byte of end address
    sty tube_xfer_addr_2                                              ; 93ef: 84 59       .Y  :04a2[2]   ; Store byte 3 of end address
    pla                                                               ; 93f1: 68          h   :04a4[2]   ; Restore A from stack
    plp                                                               ; 93f2: 28          (   :04a5[2]   ; Restore processor status
    bcs beginr                                                        ; 93f3: b0 12       ..  :04a6[2]   ; Carry set: language entry (claim Tube)
    tax                                                               ; 93f5: aa          .   :04a8[2]   ; X = A (preserved from entry)
    bne begink                                                        ; 93f6: d0 03       ..  :04a9[2]   ; Non-zero: check break type
    jmp tube_reply_ack                                                ; 93f8: 4c cb 05    L.. :04ab[2]   ; A=0: acknowledge and return

; &93fb referenced 1 time by &04a9[2]
.begink
    ldx #0                                                            ; 93fb: a2 00       ..  :04ae[2]   ; X=0 for OSBYTE read
    ldy #&ff                                                          ; 93fd: a0 ff       ..  :04b0[2]   ; Y=&FF for OSBYTE read
    lda #osbyte_read_write_last_break_type                            ; 93ff: a9 fd       ..  :04b2[2]   ; OSBYTE &FD: read last break type
    jsr osbyte                                                        ; 9401: 20 f4 ff     .. :04b4[2]   ; Read type of last reset
    txa                                                               ; 9404: 8a          .   :04b7[2]   ; X=value of type of last reset
    beq release_claim_restart                                         ; 9405: f0 a3       ..  :04b8[2]   ; Soft break (0): skip ROM transfer
; &9407 referenced 2 times by &04a6[2], &04bf[2]
.beginr
    lda #&ff                                                          ; 9407: a9 ff       ..  :04ba[2]   ; A=&FF: claim Tube for all operations
    jsr tube_addr_claim                                               ; 9409: 20 06 04     .. :04bc[2]   ; Claim Tube address via R4
    bcc beginr                                                        ; 940c: 90 f9       ..  :04bf[2]   ; Not claimed: retry until claimed
    lda #1                                                            ; 940e: a9 01       ..  :04c1[2]   ; Transfer type 1 (parasite to host)
    jsr tube_setup_transfer                                           ; 9410: 20 e0 04     .. :04c3[2]   ; Set up Tube transfer parameters
    ldy #0                                                            ; 9413: a0 00       ..  :04c6[2]   ; Y=0: start at page boundary
    sty zp_ptr_lo                                                     ; 9415: 84 00       ..  :04c8[2]   ; Source ptr low = 0
    ldx #&40 ; '@'                                                    ; 9417: a2 40       .@  :04ca[2]   ; X=&40: 64 pages (16KB) to transfer
; &9419 referenced 2 times by &04d7[2], &04dc[2]
.send_rom_byte
    lda (zp_ptr_lo),y                                                 ; 9419: b1 00       ..  :04cc[2]   ; Read byte from source address
    sta tube_data_register_3                                          ; 941b: 8d e5 fe    ... :04ce[2]   ; Send byte to Tube via R3
; &941e referenced 1 time by &04d4[2]
.poll_r3_ready
    bit tube_status_register_3                                        ; 941e: 2c e4 fe    ,.. :04d1[2]   ; Check R3 status
    bvc poll_r3_ready                                                 ; 9421: 50 fb       P.  :04d4[2]   ; Not ready: wait for Tube
    iny                                                               ; 9423: c8          .   :04d6[2]   ; Next byte in page
    bne send_rom_byte                                                 ; 9424: d0 f3       ..  :04d7[2]   ; More bytes in page: continue
    inc zp_ptr_hi                                                     ; 9426: e6 01       ..  :04d9[2]   ; Next source page
    dex                                                               ; 9428: ca          .   :04db[2]   ; Decrement page counter
    bne send_rom_byte                                                 ; 9429: d0 ee       ..  :04dc[2]   ; More pages: continue transfer
    lda #4                                                            ; 942b: a9 04       ..  :04de[2]   ; Transfer type 4 (host to parasite burst)
; &942d referenced 1 time by &04c3[2]
.tube_setup_transfer
    ldy #0                                                            ; 942d: a0 00       ..  :04e0[2]   ; Y=0: low byte of param block ptr
    ldx #&57 ; 'W'                                                    ; 942f: a2 57       .W  :04e2[2]   ; X=&57: param block at &0057
    jmp tube_addr_claim                                               ; 9431: 4c 06 04    L.. :04e4[2]   ; Claim Tube and start transfer

.tube_rdch_handler
    lda #1                                                            ; 9434: a9 01       ..  :04e7[2]   ; R2 command: OSRDCH request
    jsr tube_send_r2                                                  ; 9436: 20 d0 06     .. :04e9[2]   ; Send OSRDCH request to host
    jmp tube_enter_main_loop                                          ; 9439: 4c 36 00    L6. :04ec[2]   ; Jump to RDCH completion handler

.tube_restore_regs
    ldy zp_temp_10                                                    ; 943c: a4 10       ..  :04ef[2]   ; Restore saved Y register
    ldx zp_temp_11                                                    ; 943e: a6 11       ..  :04f1[2]   ; Restore X from saved value
    jsr tube_read_r2                                                  ; 9440: 20 f7 04     .. :04f3[2]   ; Read result byte from R2
    asl a                                                             ; 9443: 0a          .   :04f6[2]   ; Shift carry into C flag
; &9444 referenced 22 times by &04f3[2], &04fa[2], &0543[3], &0547[3], &0550[3], &0569[3], &0580[3], &058c[3], &0592[3], &059b[3], &05b5[3], &05da[3], &05eb[3], &0604[4], &060c[4], &0626[4], &062a[4], &063b[4], &063f[4], &0643[4], &065d[4], &06a5[4]
.tube_read_r2
    bit tube_status_register_2                                        ; 9444: 2c e2 fe    ,.. :04f7[2]   ; Poll R2 status register
    bpl tube_read_r2                                                  ; 9447: 10 fb       ..  :04fa[2]   ; Bit 7 clear: R2 not ready, wait
    lda tube_data_register_2                                          ; 9449: ad e3 fe    ... :04fc[2]   ; Read byte from R2 data register
    rts                                                               ; 944c: 60          `   :04ff[2]   ; Return with pointers initialised


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, reloc_p4_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &0500

    ; Set the program counter to the next position in the binary file.
    org reloc_p4_src + (* - tube_code_page4)

.l944d

; Move 3: &944d to &0500 for length 256
    org &0500
; ***************************************************************************************
; Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)
; 
; Copied from ROM at &944D during init. Contains:
;   &0500: tube_dispatch_table — 14-entry handler address table
;   &051C: tube_wrch_handler — WRCHV target
;   &051F: tube_send_and_poll — send byte via R2, poll for reply
;   &0527: tube_poll_r4_wrch — service R4 WRCH while waiting for R2
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
; &944d referenced 2 times by &0054[1], &8102
.tube_dispatch_table
    equw tube_osrdch                                                  ; 944d: 5b 05       [.  :0500[3]   ; cmd 0: OSRDCH
    equw tube_oscli                                                   ; 944f: c5 05       ..  :0502[3]   ; cmd 1: OSCLI
    equw tube_osbyte_short                                            ; 9451: 26 06       &.  :0504[3]   ; cmd 2: OSBYTE (2-param)
    equw tube_osbyte_long                                             ; 9453: 3b 06       ;.  :0506[3]   ; cmd 3: OSBYTE (3-param)
    equw tube_osword                                                  ; 9455: 5d 06       ].  :0508[3]   ; cmd 4: OSWORD
    equw tube_osword_rdln                                             ; 9457: a3 06       ..  :050a[3]   ; cmd 5: OSWORD 0 (read line)
    equw tube_restore_regs                                            ; 9459: ef 04       ..  :050c[3]   ; cmd 6: release/restore regs
    equw tube_release_return                                          ; 945b: 3d 05       =.  :050e[3]   ; cmd 7: restore regs, RTS
    equw tube_osargs                                                  ; 945d: 8c 05       ..  :0510[3]   ; cmd 8: OSARGS
    equw tube_osbget                                                  ; 945f: 50 05       P.  :0512[3]   ; cmd 9: OSBGET
    equw tube_osbput                                                  ; 9461: 43 05       C.  :0514[3]   ; cmd 10: OSBPUT
    equw tube_osfind                                                  ; 9463: 69 05       i.  :0516[3]   ; cmd 11: OSFIND
    equw tube_osfile                                                  ; 9465: d8 05       ..  :0518[3]   ; cmd 12: OSFILE
    equw tube_osgbpb                                                  ; 9467: 02 06       ..  :051a[3]   ; cmd 13: OSGBPB

.tube_wrch_handler
    pha                                                               ; 9469: 48          H   :051c[3]   ; Save character for WRCH echo
    lda #0                                                            ; 946a: a9 00       ..  :051d[3]   ; A=0: send null prefix via R2
.tube_send_and_poll
    jsr tube_send_r2                                                  ; 946c: 20 d0 06     .. :051f[3]   ; Send prefix byte to co-processor
; &946f referenced 2 times by &052a[3], &0532[3]
.poll_r2_reply
    bit tube_status_register_2                                        ; 946f: 2c e2 fe    ,.. :0522[3]   ; Poll R2 for co-processor reply
    bvs wrch_echo_reply                                               ; 9472: 70 0e       p.  :0525[3]   ; R2 ready: go process reply
.tube_poll_r4_wrch
    bit tube_status_register_4_and_cpu_control                        ; 9474: 2c e6 fe    ,.. :0527[3]   ; Check R4 for pending WRCH request
    bpl poll_r2_reply                                                 ; 9477: 10 f6       ..  :052a[3]   ; No R4 data: back to polling R2
    lda tube_data_register_4                                          ; 9479: ad e7 fe    ... :052c[3]   ; Read WRCH character from R4
    jsr nvwrch                                                        ; 947c: 20 cb ff     .. :052f[3]   ; Write character
.tube_resume_poll
    jmp poll_r2_reply                                                 ; 947f: 4c 22 05    L". :0532[3]   ; Resume R2 polling after servicing

; &9482 referenced 1 time by &0525[3]
.wrch_echo_reply
    pla                                                               ; 9482: 68          h   :0535[3]   ; Recover original character
    sta tube_data_register_2                                          ; 9483: 8d e3 fe    ... :0536[3]   ; Echo character back via R2
    pha                                                               ; 9486: 48          H   :0539[3]   ; Push for dispatch loop re-entry
    jmp tube_enter_main_loop                                          ; 9487: 4c 36 00    L6. :053a[3]   ; Enter main dispatch loop

.tube_release_return
    ldx zp_temp_11                                                    ; 948a: a6 11       ..  :053d[3]   ; Restore saved X
    ldy zp_temp_10                                                    ; 948c: a4 10       ..  :053f[3]   ; Restore saved Y from temporary
    pla                                                               ; 948e: 68          h   :0541[3]   ; Restore saved A
    rts                                                               ; 948f: 60          `   :0542[3]   ; Return to caller

.tube_osbput
    jsr tube_read_r2                                                  ; 9490: 20 f7 04     .. :0543[3]   ; Read file handle from R2
    tay                                                               ; 9493: a8          .   :0546[3]   ; Y=channel handle from R2
    jsr tube_read_r2                                                  ; 9494: 20 f7 04     .. :0547[3]   ; Read data byte from R2 for BPUT
.tube_poll_r1_wrch
    jsr osbput                                                        ; 9497: 20 d4 ff     .. :054a[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 949a: 4c cb 05    L.. :054d[3]   ; BPUT done: send acknowledge, return

.tube_osbget
    jsr tube_read_r2                                                  ; 949d: 20 f7 04     .. :0550[3]   ; Read file handle from R2
    tay                                                               ; 94a0: a8          .   :0553[3]   ; Y=channel handle for OSBGET; Y=file handle
    jsr osbget                                                        ; 94a1: 20 d7 ff     .. :0554[3]   ; Read a single byte from an open file Y
    pha                                                               ; 94a4: 48          H   :0557[3]   ; Save byte read from file
    jmp send_reply_ok                                                 ; 94a5: 4c 5f 05    L_. :0558[3]   ; Send carry+byte reply (BGET result)

.tube_osrdch
    jsr nvrdch                                                        ; 94a8: 20 c8 ff     .. :055b[3]   ; Read a character from the current input stream
    pha                                                               ; 94ab: 48          H   :055e[3]   ; A=character read
; &94ac referenced 1 time by &0558[3]
.send_reply_ok
    ora #&80                                                          ; 94ac: 09 80       ..  :055f[3]   ; Set bit 7 (no-error flag)
.tube_rdch_reply
    ror a                                                             ; 94ae: 6a          j   :0561[3]   ; ROR A: encode carry (error flag) into bit 7
    jsr tube_send_r2                                                  ; 94af: 20 d0 06     .. :0562[3]   ; = JSR tube_send_r2 (overlaps &053D entry)
    pla                                                               ; 94b2: 68          h   :0565[3]   ; Restore read character/byte
    jmp tube_reply_byte                                               ; 94b3: 4c cd 05    L.. :0566[3]   ; Return to Tube main loop

.tube_osfind
    jsr tube_read_r2                                                  ; 94b6: 20 f7 04     .. :0569[3]   ; Read open mode from R2
    beq tube_osfind_close                                             ; 94b9: f0 12       ..  :056c[3]   ; A=0: close file, else open with filename
    pha                                                               ; 94bb: 48          H   :056e[3]   ; Save open mode while reading filename
    jsr tube_read_string                                              ; 94bc: 20 b1 05     .. :056f[3]   ; Read filename string from R2 into &0700
    pla                                                               ; 94bf: 68          h   :0572[3]   ; Recover open mode from stack
    jsr osfind                                                        ; 94c0: 20 ce ff     .. :0573[3]   ; Open or close file(s)
    pha                                                               ; 94c3: 48          H   :0576[3]   ; Save file handle result
    lda #&ff                                                          ; 94c4: a9 ff       ..  :0577[3]   ; A=&FF: success marker
    jsr tube_send_r2                                                  ; 94c6: 20 d0 06     .. :0579[3]   ; Send success marker via R2
    pla                                                               ; 94c9: 68          h   :057c[3]   ; Restore file handle
    jmp tube_reply_byte                                               ; 94ca: 4c cd 05    L.. :057d[3]   ; Send file handle result to co-processor

; &94cd referenced 1 time by &056c[3]
.tube_osfind_close
    jsr tube_read_r2                                                  ; 94cd: 20 f7 04     .. :0580[3]   ; OSFIND close: read handle from R2
    tay                                                               ; 94d0: a8          .   :0583[3]   ; Y=handle to close
    lda #osfind_close                                                 ; 94d1: a9 00       ..  :0584[3]   ; A=0: close command for OSFIND
    jsr osfind                                                        ; 94d3: 20 ce ff     .. :0586[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94d6: 4c cb 05    L.. :0589[3]   ; Close done: send acknowledge, return

.tube_osargs
    jsr tube_read_r2                                                  ; 94d9: 20 f7 04     .. :058c[3]   ; Read file handle from R2
    tay                                                               ; 94dc: a8          .   :058f[3]   ; Y=file handle for OSARGS
.tube_read_params
    ldx #3                                                            ; 94dd: a2 03       ..  :0590[3]   ; Read 4-byte arg + reason from R2 into ZP
; &94df referenced 1 time by &0598[3]
.read_osargs_params
    jsr tube_read_r2                                                  ; 94df: 20 f7 04     .. :0592[3]   ; Read next param byte from R2
    sta zp_ptr_lo,x                                                   ; 94e2: 95 00       ..  :0595[3]   ; Params stored at &00-&03 (little-endian)
    dex                                                               ; 94e4: ca          .   :0597[3]   ; Decrement byte counter
    bpl read_osargs_params                                            ; 94e5: 10 f8       ..  :0598[3]   ; Loop until all 4 bytes read
    inx                                                               ; 94e7: e8          .   :059a[3]   ; X=0: reset index after loop
    jsr tube_read_r2                                                  ; 94e8: 20 f7 04     .. :059b[3]   ; Read OSARGS reason code from R2
    jsr osargs                                                        ; 94eb: 20 da ff     .. :059e[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 94ee: 20 d0 06     .. :05a1[3]   ; Send result A back to co-processor
    ldx #3                                                            ; 94f1: a2 03       ..  :05a4[3]   ; Return 4-byte result from ZP &00-&03
; &94f3 referenced 1 time by &05ac[3]
.send_osargs_result
    lda zp_ptr_lo,x                                                   ; 94f3: b5 00       ..  :05a6[3]   ; Load result byte from zero page
    jsr tube_send_r2                                                  ; 94f5: 20 d0 06     .. :05a8[3]   ; Send byte to co-processor via R2
    dex                                                               ; 94f8: ca          .   :05ab[3]   ; Previous byte (count down)
    bpl send_osargs_result                                            ; 94f9: 10 f8       ..  :05ac[3]   ; Loop for all 4 bytes
    jmp tube_main_loop                                                ; 94fb: 4c 3a 00    L:. :05ae[3]   ; Return to Tube main loop

; &94fe referenced 3 times by &056f[3], &05c5[3], &05e2[3]
.tube_read_string
    ldx #0                                                            ; 94fe: a2 00       ..  :05b1[3]   ; X=0: initialise string buffer index
    ldy #0                                                            ; 9500: a0 00       ..  :05b3[3]   ; Y=0: string buffer offset 0
; &9502 referenced 1 time by &05c0[3]
.strnh
    jsr tube_read_r2                                                  ; 9502: 20 f7 04     .. :05b5[3]   ; Read next string byte from R2
    sta l0700,y                                                       ; 9505: 99 00 07    ... :05b8[3]   ; Store byte in string buffer at &0700+Y
    iny                                                               ; 9508: c8          .   :05bb[3]   ; Next buffer position
    beq string_buf_done                                               ; 9509: f0 04       ..  :05bc[3]   ; Y overflow: string too long, truncate
    cmp #&0d                                                          ; 950b: c9 0d       ..  :05be[3]   ; Check for CR terminator
    bne strnh                                                         ; 950d: d0 f3       ..  :05c0[3]   ; Not CR: continue reading string
; &950f referenced 1 time by &05bc[3]
.string_buf_done
    ldy #7                                                            ; 950f: a0 07       ..  :05c2[3]   ; Y=7: set XY=&0700 for OSCLI/OSFIND
    rts                                                               ; 9511: 60          `   :05c4[3]   ; Return with XY pointing to &0700

.tube_oscli
    jsr tube_read_string                                              ; 9512: 20 b1 05     .. :05c5[3]   ; Read command string into &0700
    jsr oscli                                                         ; 9515: 20 f7 ff     .. :05c8[3]   ; Execute * command via OSCLI
; &9518 referenced 3 times by &04ab[2], &054d[3], &0589[3]
.tube_reply_ack
    lda #&7f                                                          ; 9518: a9 7f       ..  :05cb[3]   ; &7F = success acknowledgement
; &951a referenced 5 times by &0461[2], &0566[3], &057d[3], &05d0[3], &06b8[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 951a: 2c e2 fe    ,.. :05cd[3]   ; Poll R2 status until ready
    bvc tube_reply_byte                                               ; 951d: 50 fb       P.  :05d0[3]   ; Bit 6 clear: not ready, loop
    sta tube_data_register_2                                          ; 951f: 8d e3 fe    ... :05d2[3]   ; Write byte to R2 data register
; &9522 referenced 1 time by &0600[4]
.mj
    jmp tube_main_loop                                                ; 9522: 4c 3a 00    L:. :05d5[3]   ; Return to Tube main loop

.tube_osfile
    ldx #&10                                                          ; 9525: a2 10       ..  :05d8[3]   ; X=&10: read 16-byte control block
; &9527 referenced 1 time by &05e0[3]
.argsw
    jsr tube_read_r2                                                  ; 9527: 20 f7 04     .. :05da[3]   ; Read next control block byte from R2
    sta zp_ptr_hi,x                                                   ; 952a: 95 01       ..  :05dd[3]   ; Store at &01+X (descending)
    dex                                                               ; 952c: ca          .   :05df[3]   ; Decrement byte counter
    bne argsw                                                         ; 952d: d0 f8       ..  :05e0[3]   ; Loop for all 16 bytes
    jsr tube_read_string                                              ; 952f: 20 b1 05     .. :05e2[3]   ; Read filename string from R2 into &0700
    stx zp_ptr_lo                                                     ; 9532: 86 00       ..  :05e5[3]   ; XY=&0700: filename pointer for OSFILE
    sty zp_ptr_hi                                                     ; 9534: 84 01       ..  :05e7[3]   ; Store Y=7 as pointer high byte
    ldy #0                                                            ; 9536: a0 00       ..  :05e9[3]   ; Y=0 for OSFILE control block offset
    jsr tube_read_r2                                                  ; 9538: 20 f7 04     .. :05eb[3]   ; Read OSFILE reason code from R2
    jsr osfile                                                        ; 953b: 20 dd ff     .. :05ee[3]   ; Execute OSFILE operation
    ora #&80                                                          ; 953e: 09 80       ..  :05f1[3]   ; Set bit 7: mark result as present
    jsr tube_send_r2                                                  ; 9540: 20 d0 06     .. :05f3[3]   ; Send result A (object type) to co-processor
    ldx #&10                                                          ; 9543: a2 10       ..  :05f6[3]   ; Return 16-byte control block to co-processor
; &9545 referenced 1 time by &05fe[3]
.send_osfile_ctrl_blk
    lda zp_ptr_hi,x                                                   ; 9545: b5 01       ..  :05f8[3]   ; Load control block byte
    jsr tube_send_r2                                                  ; 9547: 20 d0 06     .. :05fa[3]   ; Send byte to co-processor via R2
    dex                                                               ; 954a: ca          .   :05fd[3]   ; Decrement byte counter
    bne send_osfile_ctrl_blk                                          ; 954b: d0 f8       ..  :05fe[3]   ; Loop for all 16 bytes

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_dispatch_table, *, l944d

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_dispatch_table, &0600

    ; Set the program counter to the next position in the binary file.
    org l944d + (* - tube_dispatch_table)

.c954d

; Move 4: &954d to &0600 for length 256
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
; &954d referenced 1 time by &8108
.tube_code_page6
    beq mj                                                            ; 954d: f0 d3       ..  :0600[4]   ; OSGBPB done: return to main loop
.tube_osgbpb
    ldx #&0c                                                          ; 954f: a2 0c       ..  :0602[4]   ; X=&0C: read 13-byte param block
; &9551 referenced 1 time by &060a[4]
.read_gbpb_params
    jsr tube_read_r2                                                  ; 9551: 20 f7 04     .. :0604[4]   ; Read param byte from Tube R2
    sta zp_ptr_lo,x                                                   ; 9554: 95 00       ..  :0607[4]   ; Store in zero page param block
    dex                                                               ; 9556: ca          .   :0609[4]   ; Next byte (descending)
    bpl read_gbpb_params                                              ; 9557: 10 f8       ..  :060a[4]   ; Loop until all 13 bytes read
    jsr tube_read_r2                                                  ; 9559: 20 f7 04     .. :060c[4]   ; Read A (OSGBPB function code)
    inx                                                               ; 955c: e8          .   :060f[4]   ; X=0 after loop
    ldy #0                                                            ; 955d: a0 00       ..  :0610[4]   ; Y=0 for OSGBPB call
    jsr osgbpb                                                        ; 955f: 20 d1 ff     .. :0612[4]   ; Read or write multiple bytes to an open file
    ror a                                                             ; 9562: 6a          j   :0615[4]   ; Encode carry into result bit 7
    jsr tube_send_r2                                                  ; 9563: 20 d0 06     .. :0616[4]   ; Send carry+result byte via R2
    ldx #&0c                                                          ; 9566: a2 0c       ..  :0619[4]   ; X=12: send 13 updated param bytes
; &9568 referenced 1 time by &0621[4]
.send_gbpb_params
    lda zp_ptr_lo,x                                                   ; 9568: b5 00       ..  :061b[4]   ; Load updated param byte
    jsr tube_send_r2                                                  ; 956a: 20 d0 06     .. :061d[4]   ; Send param byte via R2
    dex                                                               ; 956d: ca          .   :0620[4]   ; Next byte (descending)
    bpl send_gbpb_params                                              ; 956e: 10 f8       ..  :0621[4]   ; Loop until all 13 bytes sent
    jmp tube_main_loop                                                ; 9570: 4c 3a 00    L:. :0623[4]   ; Return to main event loop

.tube_osbyte_short
    jsr tube_read_r2                                                  ; 9573: 20 f7 04     .. :0626[4]   ; Read X parameter from R2
    tax                                                               ; 9576: aa          .   :0629[4]   ; Save in X
    jsr tube_read_r2                                                  ; 9577: 20 f7 04     .. :062a[4]   ; Read A (OSBYTE function code)
    jsr osbyte                                                        ; 957a: 20 f4 ff     .. :062d[4]   ; Execute OSBYTE A,X
; &957d referenced 2 times by &0633[4], &065b[4]
.tube_osbyte_send_x
    bit tube_status_register_2                                        ; 957d: 2c e2 fe    ,.. :0630[4]   ; Poll R2 status (bit 6 = ready)
    bvc tube_osbyte_send_x                                            ; 9580: 50 fb       P.  :0633[4]   ; Not ready: keep polling
    stx tube_data_register_2                                          ; 9582: 8e e3 fe    ... :0635[4]   ; Send X result for 2-param OSBYTE
; &9585 referenced 1 time by &064b[4]
.bytex
    jmp tube_main_loop                                                ; 9585: 4c 3a 00    L:. :0638[4]   ; Return to main event loop

.tube_osbyte_long
    jsr tube_read_r2                                                  ; 9588: 20 f7 04     .. :063b[4]   ; Read X parameter from R2
    tax                                                               ; 958b: aa          .   :063e[4]   ; Save in X
    jsr tube_read_r2                                                  ; 958c: 20 f7 04     .. :063f[4]   ; Read Y parameter from co-processor
    tay                                                               ; 958f: a8          .   :0642[4]   ; Save in Y
    jsr tube_read_r2                                                  ; 9590: 20 f7 04     .. :0643[4]   ; Read A (OSBYTE function code)
    jsr osbyte                                                        ; 9593: 20 f4 ff     .. :0646[4]   ; Execute OSBYTE A,X,Y
    eor #&9d                                                          ; 9596: 49 9d       I.  :0649[4]   ; Test for OSBYTE &9D (fast Tube BPUT)
    beq bytex                                                         ; 9598: f0 eb       ..  :064b[4]   ; OSBYTE &9D (fast Tube BPUT): no result needed
    lda #&40 ; '@'                                                    ; 959a: a9 40       .@  :064d[4]   ; A=&40: high bit will hold carry
    ror a                                                             ; 959c: 6a          j   :064f[4]   ; Encode carry (error flag) into bit 7
    jsr tube_send_r2                                                  ; 959d: 20 d0 06     .. :0650[4]   ; Send carry+status byte via R2
; &95a0 referenced 1 time by &0656[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 95a0: 2c e2 fe    ,.. :0653[4]   ; Poll R2 status for ready
    bvc tube_osbyte_send_y                                            ; 95a3: 50 fb       P.  :0656[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; 95a5: 8c e3 fe    ... :0658[4]   ; Send Y result, then fall through to send X
    bvs tube_osbyte_send_x                                            ; 95a8: 70 d3       p.  :065b[4]   ; ALWAYS branch

.tube_osword
    jsr tube_read_r2                                                  ; 95aa: 20 f7 04     .. :065d[4]   ; Read OSWORD number from R2
    tay                                                               ; 95ad: a8          .   :0660[4]   ; Save OSWORD number in Y
; &95ae referenced 1 time by &0664[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 95ae: 2c e2 fe    ,.. :0661[4]   ; Poll R2 status for data ready
    bpl tube_osword_read                                              ; 95b1: 10 fb       ..  :0664[4]   ; Not ready: keep polling
    ldx tube_data_register_2                                          ; 95b3: ae e3 fe    ... :0666[4]   ; Read param block length from R2
    dex                                                               ; 95b6: ca          .   :0669[4]   ; DEX: length 0 means no params to read
    bmi skip_param_read                                               ; 95b7: 30 0f       0.  :066a[4]   ; No params (length=0): skip read loop
; &95b9 referenced 2 times by &066f[4], &0678[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 95b9: 2c e2 fe    ,.. :066c[4]   ; Poll R2 status for data ready
    bpl tube_osword_read_lp                                           ; 95bc: 10 fb       ..  :066f[4]   ; Not ready: keep polling
    lda tube_data_register_2                                          ; 95be: ad e3 fe    ... :0671[4]   ; Read param byte from R2
    sta l0130,x                                                       ; 95c1: 9d 30 01    .0. :0674[4]   ; Store param bytes into block at &0130
    dex                                                               ; 95c4: ca          .   :0677[4]   ; Next param byte (descending)
    bpl tube_osword_read_lp                                           ; 95c5: 10 f2       ..  :0678[4]   ; Loop until all params read
    tya                                                               ; 95c7: 98          .   :067a[4]   ; Restore OSWORD number from Y
; &95c8 referenced 1 time by &066a[4]
.skip_param_read
    ldx #<(l0130)                                                     ; 95c8: a2 30       .0  :067b[4]   ; XY=&0130: param block address for OSWORD
    ldy #>(l0130)                                                     ; 95ca: a0 01       ..  :067d[4]   ; Y=&01: param block at &0130
    jsr osword                                                        ; 95cc: 20 f1 ff     .. :067f[4]   ; Execute OSWORD with XY=&0130
    lda #&ff                                                          ; 95cf: a9 ff       ..  :0682[4]   ; A=&FF: result marker for co-processor
    jsr tube_send_r2                                                  ; 95d1: 20 d0 06     .. :0684[4]   ; Send result marker via R2
; &95d4 referenced 1 time by &068a[4]
.poll_r2_osword_result
    bit tube_status_register_2                                        ; 95d4: 2c e2 fe    ,.. :0687[4]   ; Poll R2 status for ready
    bpl poll_r2_osword_result                                         ; 95d7: 10 fb       ..  :068a[4]   ; Not ready: keep polling
    ldx tube_data_register_2                                          ; 95d9: ae e3 fe    ... :068c[4]   ; Read result block length from R2
    dex                                                               ; 95dc: ca          .   :068f[4]   ; Decrement result byte counter
    bmi tube_return_main                                              ; 95dd: 30 0e       0.  :0690[4]   ; No results to send: return to main loop
; &95df referenced 1 time by &069e[4]
.tube_osword_write
    ldy l0130,x                                                       ; 95df: bc 30 01    .0. :0692[4]   ; Send result block bytes from &0128 via R2
; &95e2 referenced 1 time by &0698[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95e2: 2c e2 fe    ,.. :0695[4]   ; Poll R2 status for ready
    bvc tube_osword_write_lp                                          ; 95e5: 50 fb       P.  :0698[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; 95e7: 8c e3 fe    ... :069a[4]   ; Send result byte via R2
    dex                                                               ; 95ea: ca          .   :069d[4]   ; Next result byte (descending)
    bpl tube_osword_write                                             ; 95eb: 10 f2       ..  :069e[4]   ; Loop until all results sent
; &95ed referenced 1 time by &0690[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95ed: 4c 3a 00    L:. :06a0[4]   ; Return to main event loop

.tube_osword_rdln
    ldx #4                                                            ; 95f0: a2 04       ..  :06a3[4]   ; X=4: read 5-byte RDLN ctrl block
; &95f2 referenced 1 time by &06ab[4]
.read_rdln_ctrl_block
    jsr tube_read_r2                                                  ; 95f2: 20 f7 04     .. :06a5[4]   ; Read control block byte from R2
    sta zp_ptr_lo,x                                                   ; 95f5: 95 00       ..  :06a8[4]   ; Store in zero page params
    dex                                                               ; 95f7: ca          .   :06aa[4]   ; Next byte (descending)
    bpl read_rdln_ctrl_block                                          ; 95f8: 10 f8       ..  :06ab[4]   ; Loop until all 5 bytes read
    inx                                                               ; 95fa: e8          .   :06ad[4]   ; X=0 after loop, A=0 for OSWORD 0 (read line)
    ldy #0                                                            ; 95fb: a0 00       ..  :06ae[4]   ; Y=0 for OSWORD 0
    txa                                                               ; 95fd: 8a          .   :06b0[4]   ; A=0: OSWORD 0 (read line)
    jsr osword                                                        ; 95fe: 20 f1 ff     .. :06b1[4]   ; Read input line from keyboard
    bcc tube_rdln_send_line                                           ; 9601: 90 05       ..  :06b4[4]   ; C=0: line read OK; C=1: escape pressed
    lda #&ff                                                          ; 9603: a9 ff       ..  :06b6[4]   ; &FF = escape/error signal to co-processor
    jmp tube_reply_byte                                               ; 9605: 4c cd 05    L.. :06b8[4]   ; Escape: send &FF error to co-processor

; &9608 referenced 1 time by &06b4[4]
.tube_rdln_send_line
    ldx #0                                                            ; 9608: a2 00       ..  :06bb[4]   ; X=0: start of input buffer at &0700
    lda #&7f                                                          ; 960a: a9 7f       ..  :06bd[4]   ; &7F = line read successfully
    jsr tube_send_r2                                                  ; 960c: 20 d0 06     .. :06bf[4]   ; Send &7F (success) to co-processor
; &960f referenced 1 time by &06cb[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 960f: bd 00 07    ... :06c2[4]   ; Load char from input buffer
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 9612: 20 d0 06     .. :06c5[4]   ; Send char to co-processor
    inx                                                               ; 9615: e8          .   :06c8[4]   ; Next character
    cmp #&0d                                                          ; 9616: c9 0d       ..  :06c9[4]   ; Check for CR terminator
    bne tube_rdln_send_loop                                           ; 9618: d0 f5       ..  :06cb[4]   ; Loop until CR terminator sent
    jmp tube_main_loop                                                ; 961a: 4c 3a 00    L:. :06cd[4]   ; Return to main event loop

; &961d referenced 18 times by &0020[1], &0026[1], &002c[1], &04e9[2], &051f[3], &0562[3], &0579[3], &05a1[3], &05a8[3], &05f3[3], &05fa[3], &0616[4], &061d[4], &0650[4], &0684[4], &06bf[4], &06c5[4], &06d3[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 961d: 2c e2 fe    ,.. :06d0[4]   ; Poll R2 status (bit 6 = ready)
    bvc tube_send_r2                                                  ; 9620: 50 fb       P.  :06d3[4]   ; Not ready: keep polling
    sta tube_data_register_2                                          ; 9622: 8d e3 fe    ... :06d5[4]   ; Write A to Tube R2 data register
    rts                                                               ; 9625: 60          `   :06d8[4]   ; Return to caller

; &9626 referenced 5 times by &0018[1], &042a[2], &0432[2], &0448[2], &06dc[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 9626: 2c e6 fe    ,.. :06d9[4]   ; Poll R4 status (bit 6 = ready)
    bvc tube_send_r4                                                  ; 9629: 50 fb       P.  :06dc[4]   ; Not ready: keep polling
    sta tube_data_register_4                                          ; 962b: 8d e7 fe    ... :06de[4]   ; Write A to Tube R4 data register
    rts                                                               ; 962e: 60          `   :06e1[4]   ; Return to caller

; &962f referenced 1 time by &0403[2]
.tube_escape_check
    lda escape_flag                                                   ; 962f: a5 ff       ..  :06e2[4]   ; Check OS escape flag at &FF
    sec                                                               ; 9631: 38          8   :06e4[4]   ; SEC+ROR: put bit 7 of &FF into carry+bit 7
    ror a                                                             ; 9632: 6a          j   :06e5[4]   ; ROR: shift escape bit 7 to carry
    bmi tube_send_r1                                                  ; 9633: 30 0f       0.  :06e6[4]   ; Escape set: forward to co-processor via R1
.tube_event_handler
    pha                                                               ; 9635: 48          H   :06e8[4]   ; EVNTV: forward event A, Y, X to co-processor
    lda #0                                                            ; 9636: a9 00       ..  :06e9[4]   ; Send &00 prefix (event notification)
    jsr tube_send_r1                                                  ; 9638: 20 f7 06     .. :06eb[4]   ; Send zero prefix via R1
    tya                                                               ; 963b: 98          .   :06ee[4]   ; Y value for event
    jsr tube_send_r1                                                  ; 963c: 20 f7 06     .. :06ef[4]   ; Send Y via R1
    txa                                                               ; 963f: 8a          .   :06f2[4]   ; X value for event
    jsr tube_send_r1                                                  ; 9640: 20 f7 06     .. :06f3[4]   ; Send X via R1
    pla                                                               ; 9643: 68          h   :06f6[4]   ; Restore A (event type)
; &9644 referenced 5 times by &06e6[4], &06eb[4], &06ef[4], &06f3[4], &06fa[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 9644: 2c e0 fe    ,.. :06f7[4]   ; Poll R1 status (bit 6 = ready)
    bvc tube_send_r1                                                  ; 9647: 50 fb       P.  :06fa[4]   ; Not ready: keep polling
    sta tube_data_register_1                                          ; 9649: 8d e1 fe    ... :06fc[4]   ; Write A to Tube R1 data register
    rts                                                               ; 964c: 60          `   :06ff[4]   ; Return to caller


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page6, *, c954d

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page6, &0700

    ; Set the program counter to the next position in the binary file.
    org c954d + (* - tube_code_page6)


    org &8000

; Sideways ROM header
; NFS ROM 3.34B disassembly (Acorn Econet filing system)
; =====================================================
; &8000 referenced 2 times by &048b[2], &9bb8
.pydis_start
.rom_header
.language_entry
lang_entry_lo = rom_header+1
lang_entry_hi = rom_header+2
    jmp language_handler                                              ; 8000: 4c 99 80    L..            ; JMP language_handler

; &8001 referenced 1 time by &0490[2]
; &8002 referenced 1 time by &0495[2]
; &8003 referenced 1 time by &049a[2]
.service_entry
svc_entry_lo = service_entry+1
    jmp service_handler                                               ; 8003: 4c af 80    L..            ; JMP service_handler

; &8004 referenced 1 time by &049d[2]
; &8006 referenced 1 time by &0482[2]
.rom_type
    equb &82                                                          ; 8006: 82          .
; &8007 referenced 1 time by &0487[2]
.copyright_offset
    equb copyright - rom_header                                       ; 8007: 0c          .
; &8008 referenced 2 times by &81a3, &81ac
.binary_version
    equb 3                                                            ; 8008: 03          .
.title
    equs "NET"                                                        ; 8009: 4e 45 54    NET
.copyright
    equb 0                                                            ; 800c: 00          .
; The 'ROFF' suffix at &8010 is reused by the *ROFF
; command matcher (svc_4_star_command) — a space-saving
; trick that shares ROM bytes between the copyright
; string and the star command table.
.copyright_string
    equs "(C)ROFF"                                                    ; 800d: 28 43 29... (C)
; Error message offset table (9 entries).
; Each byte is a Y offset into error_msg_table.
; Entry 0 (Y=0, "Line Jammed") doubles as the
; copyright string null terminator.
; Indexed by TXCB status (AND #7), or hardcoded 8.
; &8014 referenced 1 time by &842e
.error_offsets
    equb 0                                                            ; 8014: 00          .              ; "Line Jammed"
    equb &0d                                                          ; 8015: 0d          .              ; "Net Error"
    equb &18                                                          ; 8016: 18          .              ; "Not listening"
    equb &27                                                          ; 8017: 27          '              ; "No Clock"
    equb &31                                                          ; 8018: 31          1              ; "Bad Txcb"
    equb &3b                                                          ; 8019: 3b          ;              ; "Escape"
    equb &3b                                                          ; 801a: 3b          ;              ; "Escape"
    equb &43                                                          ; 801b: 43          C              ; "Bad Option"
    equb &4f                                                          ; 801c: 4f          O              ; "No reply"
; Four bytes with unknown purpose.
    equb 1                                                            ; 801d: 01          .              ; Purpose unknown
    equb 0                                                            ; 801e: 00          .              ; Purpose unknown
    equb &3b                                                          ; 801f: 3b          ;              ; Purpose unknown
; &8020 referenced 1 time by &80a8
    equb 3                                                            ; 8020: 03          .              ; Purpose unknown
; Dispatch table: low bytes of (handler_address - 1)
; Each entry stores the low byte of a handler address minus 1,
; for use with the PHA/PHA/RTS dispatch trick at &809F.
; See dispatch_0_hi (&8045) for the corresponding high bytes.
; 
; Five callers share this table via different Y base offsets:
;   Y=&00  Service calls 0-12       (indices 1-13)
;   Y=&0D  Language entry reasons    (indices 14-18)
;   Y=&12  FSCV codes 0-7           (indices 19-26)
;   Y=&16  FS reply handlers        (indices 27-32)
;   Y=&20  *NET1-4 sub-commands     (indices 33-36)
.dispatch_0_lo
    equb <(return_2-1)                                                ; 8021: 44          D              ; lo - Svc 0: already claimed (no-op)
    equb <(svc_1_abs_workspace-1)                                     ; 8022: 6f          o              ; lo - Svc 1: absolute workspace
    equb <(svc_2_private_workspace-1)                                 ; 8023: 78          x              ; lo - Svc 2: private workspace
    equb <(svc_3_autoboot-1)                                          ; 8024: d1          .              ; lo - Svc 3: auto-boot
    equb <(svc_4_star_command-1)                                      ; 8025: 71          q              ; lo - Svc 4: unrecognised star command
    equb <(svc_5_unknown_irq-1)                                       ; 8026: 6b          k              ; lo - Svc 5: unrecognised interrupt
    equb <(return_2-1)                                                ; 8027: 44          D              ; lo - Svc 6: BRK (no-op)
    equb <(dispatch_net_cmd-1)                                        ; 8028: 68          h              ; lo - Svc 7: unrecognised OSBYTE
    equb <(svc_8_osword-1)                                            ; 8029: f7          .              ; lo - Svc 8: unrecognised OSWORD
    equb <(svc_9_help-1)                                              ; 802a: bb          .              ; lo - Svc 9: *HELP
    equb <(return_2-1)                                                ; 802b: 44          D              ; lo - Svc 10: static workspace (no-op)
    equb <(svc_11_nmi_claim-1)                                        ; 802c: 68          h              ; lo - Svc 11: NMI release (reclaim NMIs)
    equb <(svc_12_nmi_release-1)                                      ; 802d: 65          e              ; lo - Svc 12: NMI claim (save NMI state)
    equb <(lang_0_insert_remote_key-1)                                ; 802e: 4a          J              ; lo - Lang 0: no language / Tube
    equb <(lang_1_remote_boot-1)                                      ; 802f: fc          .              ; lo - Lang 1: normal startup
    equb <(lang_2_save_palette_vdu-1)                                 ; 8030: 91          .              ; lo - Lang 2: softkey byte (Electron)
    equb <(lang_3_execute_at_0100-1)                                  ; 8031: 2a          *              ; lo - Lang 3: softkey length (Electron)
    equb <(lang_4_remote_validated-1)                                 ; 8032: 3a          :              ; lo - Lang 4: remote validated
    equb <(fscv_0_opt-1)                                              ; 8033: a1          .              ; lo - FSCV 0: *OPT
    equb <(fscv_1_eof-1)                                              ; 8034: 1f          .              ; lo - FSCV 1: EOF check
    equb <(fscv_3_star_cmd-1)                                         ; 8035: 92          .              ; lo - FSCV 2: */ (run)
    equb <(fscv_3_star_cmd-1)                                         ; 8036: 92          .              ; lo - FSCV 3: unrecognised star command
    equb <(fscv_3_star_cmd-1)                                         ; 8037: 92          .              ; lo - FSCV 4: *RUN
    equb <(fscv_5_cat-1)                                              ; 8038: fd          .              ; lo - FSCV 5: *CAT
    equb <(fscv_6_shutdown-1)                                         ; 8039: fd          .              ; lo - FSCV 6: shutdown
    equb <(fscv_7_read_handles-1)                                     ; 803a: da          .              ; lo - FSCV 7: read handle range
    equb <(fsreply_0_print_dir-1)                                     ; 803b: 73          s              ; lo - FS reply: print directory name
    equb <(fsreply_1_copy_handles_boot-1)                             ; 803c: 1f          .              ; lo - FS reply: copy handles + boot
    equb <(fsreply_2_copy_handles-1)                                  ; 803d: 20                         ; lo - FS reply: copy handles
    equb <(fsreply_3_set_csd-1)                                       ; 803e: fc          .              ; lo - FS reply: set CSD handle
    equb <(fsreply_4_notify_exec-1)                                   ; 803f: 84          .              ; lo - FS reply: notify + execute
    equb <(fsreply_5_set_lib-1)                                       ; 8040: f7          .              ; lo - FS reply: set library handle
    equb <(net_1_read_handle-1)                                       ; 8041: af          .              ; lo - *NET1: read handle from packet
    equb <(net_2_read_handle_entry-1)                                 ; 8042: c9          .              ; lo - *NET2: read handle from workspace
    equb <(net_3_close_handle-1)                                      ; 8043: df          .              ; lo - *NET3: close handle
; &8044 referenced 1 time by &80a4
    equb <(net_4_resume_remote-1)                                     ; 8044: f2          .              ; lo - *NET4: resume remote
; Dispatch table: high bytes of (handler_address - 1)
; Paired with dispatch_0_lo (&8021). Together they form a table
; of 37 handler addresses, used via the PHA/PHA/RTS trick at
; &809F.
.dispatch_0_hi
    equb >(return_2-1)                                                ; 8045: 81          .              ; hi - Svc 0: already claimed (no-op)
    equb >(svc_1_abs_workspace-1)                                     ; 8046: 82          .              ; hi - Svc 1: absolute workspace
    equb >(svc_2_private_workspace-1)                                 ; 8047: 82          .              ; hi - Svc 2: private workspace
    equb >(svc_3_autoboot-1)                                          ; 8048: 81          .              ; hi - Svc 3: auto-boot
    equb >(svc_4_star_command-1)                                      ; 8049: 81          .              ; hi - Svc 4: unrecognised star command
    equb >(svc_5_unknown_irq-1)                                       ; 804a: 96          .              ; hi - Svc 5: unrecognised interrupt
    equb >(return_2-1)                                                ; 804b: 81          .              ; hi - Svc 6: BRK (no-op)
    equb >(dispatch_net_cmd-1)                                        ; 804c: 80          .              ; hi - Svc 7: unrecognised OSBYTE
    equb >(svc_8_osword-1)                                            ; 804d: 8d          .              ; hi - Svc 8: unrecognised OSWORD
    equb >(svc_9_help-1)                                              ; 804e: 81          .              ; hi - Svc 9: *HELP
    equb >(return_2-1)                                                ; 804f: 81          .              ; hi - Svc 10: static workspace (no-op)
    equb >(svc_11_nmi_claim-1)                                        ; 8050: 96          .              ; hi - Svc 11: NMI release (reclaim NMIs)
    equb >(svc_12_nmi_release-1)                                      ; 8051: 96          .              ; hi - Svc 12: NMI claim (save NMI state)
    equb >(lang_0_insert_remote_key-1)                                ; 8052: 91          .              ; hi - Lang 0: no language / Tube
    equb >(lang_1_remote_boot-1)                                      ; 8053: 90          .              ; hi - Lang 1: normal startup
    equb >(lang_2_save_palette_vdu-1)                                 ; 8054: 92          .              ; hi - Lang 2: softkey byte (Electron)
    equb >(lang_3_execute_at_0100-1)                                  ; 8055: 91          .              ; hi - Lang 3: softkey length (Electron)
    equb >(lang_4_remote_validated-1)                                 ; 8056: 91          .              ; hi - Lang 4: remote validated
    equb >(fscv_0_opt-1)                                              ; 8057: 89          .              ; hi - FSCV 0: *OPT
    equb >(fscv_1_eof-1)                                              ; 8058: 88          .              ; hi - FSCV 1: EOF check
    equb >(fscv_3_star_cmd-1)                                         ; 8059: 8b          .              ; hi - FSCV 2: */ (run)
    equb >(fscv_3_star_cmd-1)                                         ; 805a: 8b          .              ; hi - FSCV 3: unrecognised star command
    equb >(fscv_3_star_cmd-1)                                         ; 805b: 8b          .              ; hi - FSCV 4: *RUN
    equb >(fscv_5_cat-1)                                              ; 805c: 8b          .              ; hi - FSCV 5: *CAT
    equb >(fscv_6_shutdown-1)                                         ; 805d: 82          .              ; hi - FSCV 6: shutdown
    equb >(fscv_7_read_handles-1)                                     ; 805e: 85          .              ; hi - FSCV 7: read handle range
    equb >(fsreply_0_print_dir-1)                                     ; 805f: 8d          .              ; hi - FS reply: print directory name
    equb >(fsreply_1_copy_handles_boot-1)                             ; 8060: 8d          .              ; hi - FS reply: copy handles + boot
    equb >(fsreply_2_copy_handles-1)                                  ; 8061: 8d          .              ; hi - FS reply: copy handles
    equb >(fsreply_3_set_csd-1)                                       ; 8062: 8c          .              ; hi - FS reply: set CSD handle
    equb >(fsreply_4_notify_exec-1)                                   ; 8063: 8d          .              ; hi - FS reply: notify + execute
    equb >(fsreply_5_set_lib-1)                                       ; 8064: 8c          .              ; hi - FS reply: set library handle
    equb >(net_1_read_handle-1)                                       ; 8065: 8d          .              ; hi - *NET1: read handle from packet
    equb >(net_2_read_handle_entry-1)                                 ; 8066: 8d          .              ; hi - *NET2: read handle from workspace
    equb >(net_3_close_handle-1)                                      ; 8067: 8d          .              ; hi - *NET3: close handle
    equb >(net_4_resume_remote-1)                                     ; 8068: 8d          .              ; hi - *NET4: resume remote

; ***************************************************************************************
; *NET command dispatcher
; 
; Parses the character after *NET as '1'-'4', maps to table
; indices 33-36 via base offset Y=&20, and dispatches via &809F.
; Characters outside '1'-'4' fall through to return_1 (RTS).
; 
; These are internal sub-commands used only by the ROM itself,
; not user-accessible star commands. The MOS command parser
; requires a space or terminator after 'NET', so *NET1 typed
; at the command line does not match; these are reached only
; via OSCLI calls within the ROM.
; 
; *NET1 (&8DB0): read file handle from received
; packet (net_1_read_handle)
; 
; *NET2 (&8DCA): read handle entry from workspace
; (net_2_read_handle_entry)
; 
; *NET3 (&8DE0): close handle / mark as unused
; (net_3_close_handle)
; 
; *NET4 (&8DF3): resume after remote operation
; (net_4_resume_remote)
; ***************************************************************************************
.dispatch_net_cmd
    lda osbyte_a_copy                                                 ; 8069: a5 ef       ..             ; Read command character following *NET
    sbc #&31 ; '1'                                                    ; 806b: e9 31       .1             ; Subtract ASCII '1' to get 0-based command index
    bmi return_1                                                      ; 806d: 30 3f       0?             ; Negative: not a net command, exit
    cmp #4                                                            ; 806f: c9 04       ..             ; Command index >= 4: invalid *NET sub-command
    bcs return_1                                                      ; 8071: b0 3b       .;             ; Out of range: return via c80e3/RTS
    tax                                                               ; 8073: aa          .              ; X = command index (0-3)
    tya                                                               ; 8074: 98          .              ; Transfer Y to A for dispatch
    ldy #&20 ; ' '                                                    ; 8075: a0 20       .              ; Y=&20: base offset for *NET commands (index 33+)
    bne dispatch                                                      ; 8077: d0 26       .&             ; ALWAYS branch

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
; &8079 referenced 1 time by &8d1d
.forward_star_cmd
    jsr copy_filename                                                 ; 8079: 20 64 8d     d.            ; Copy command text to FS buffer
    tay                                                               ; 807c: a8          .              ; Y=function code for HDRFN
.prepare_cmd_dispatch
    jsr prepare_fs_cmd                                                ; 807d: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    ldx fs_cmd_csd                                                    ; 8080: ae 03 0f    ...            ; X=depends on function
    beq return_1                                                      ; 8083: f0 29       .)             ; CSD handle zero: not logged in
    lda fs_cmd_data                                                   ; 8085: ad 05 0f    ...            ; A=function code (0-7)
    ldy #&16                                                          ; 8088: a0 16       ..             ; Y=depends on function
    bne dispatch                                                      ; 808a: d0 13       ..             ; ALWAYS branch

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
    jsr save_fscv_args                                                ; 808c: 20 09 85     ..            ; Store A/X/Y in FS workspace
    cmp #8                                                            ; 808f: c9 08       ..             ; Function code >= 8? Return (unsupported)
    bcs return_1                                                      ; 8091: b0 1b       ..             ; Function code >= 8? Return (unsupported)
    tax                                                               ; 8093: aa          .              ; X = function code for dispatch
    tya                                                               ; 8094: 98          .              ; Save Y (command text ptr hi)
    ldy #&12                                                          ; 8095: a0 12       ..             ; Y=&12: base offset for FSCV dispatch (indices 19+)
    bne dispatch                                                      ; 8097: d0 06       ..             ; ALWAYS branch

; ***************************************************************************************
; Language entry dispatcher
; 
; Called when the NFS ROM is entered as a language. Although rom_type
; (&82) does not set the language bit, the MOS enters this point
; after NFS claims service &FE (Tube post-init). X = reason code
; (0-4). Dispatches via table indices 14-18 (base offset Y=&0D).
; ***************************************************************************************
; &8099 referenced 1 time by &8000
.language_handler
.lang_entry_dispatch
    cpx #5                                                            ; 8099: e0 05       ..             ; X >= 5: invalid reason code, return
.svc_dispatch_range
    bcs return_1                                                      ; 809b: b0 11       ..             ; Out of range: return via RTS
    ldy #&0d                                                          ; 809d: a0 0d       ..             ; Y=&0D: base offset for language handlers (index 14+)
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
; &809f referenced 5 times by &8077, &808a, &8097, &80a1, &8139
.dispatch
    inx                                                               ; 809f: e8          .              ; Add base offset Y to index X (loop: X += Y+1)
    dey                                                               ; 80a0: 88          .              ; Decrement base offset counter
    bpl dispatch                                                      ; 80a1: 10 fc       ..             ; Loop until Y exhausted
    tay                                                               ; 80a3: a8          .              ; Y=&FF (no further use)
    lda dispatch_0_hi-1,x                                             ; 80a4: bd 44 80    .D.            ; Load high byte of (handler - 1) from table
    pha                                                               ; 80a7: 48          H              ; Push high byte onto stack
    lda dispatch_0_lo-1,x                                             ; 80a8: bd 20 80    . .            ; Load low byte of (handler - 1) from table
    pha                                                               ; 80ab: 48          H              ; Push low byte onto stack
    ldx fs_options                                                    ; 80ac: a6 bb       ..             ; Restore X (fileserver options) for use by handler
; &80ae referenced 6 times by &806d, &8071, &8083, &8091, &809b, &80b7
.return_1
    rts                                                               ; 80ae: 60          `              ; RTS pops address, adds 1, jumps to handler

; ***************************************************************************************
; Service handler entry
; 
; Intercepts three special service calls before normal dispatch:
;   &FE: Tube init — explode character definitions (OSBYTE &14, X=6)
;   &FF: Full init — set up WRCHV/RDCHV/BRKV/EVNTV, copy NMI handler
;        code from ROM to RAM pages &04-&06, copy workspace init to
;        &0016-&0076, then fall through to select NFS.
;   &12 with Y=5: Select NFS as active filing system.
; All other service calls dispatch via dispatch_service (&8127).
; ***************************************************************************************
; &80af referenced 1 time by &8003
.service_handler
.service_handler_entry
.check_svc_high
    cmp #&fe                                                          ; 80af: c9 fe       ..             ; Service >= &FE?
    bcc check_svc_12                                                  ; 80b1: 90 6c       .l             ; Service < &FE: skip to &12/dispatch check
    bne init_vectors_and_copy                                         ; 80b3: d0 13       ..             ; Service &FF: full init (vectors + RAM copy)
    cpy #0                                                            ; 80b5: c0 00       ..             ; Service &FE: Y=0?
    beq return_1                                                      ; 80b7: f0 f5       ..             ; Y=0: no Tube data, skip to &12 check
    stx zp_temp_11                                                    ; 80b9: 86 11       ..             ; Save ROM number across OSBYTE
    sty zp_temp_10                                                    ; 80bb: 84 10       ..             ; Save Tube address across OSBYTE
    ldx #6                                                            ; 80bd: a2 06       ..             ; X=6 extra pages for char definitions
    lda #osbyte_explode_chars                                         ; 80bf: a9 14       ..             ; OSBYTE &14: explode character RAM
    jsr osbyte                                                        ; 80c1: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
    ldx zp_temp_11                                                    ; 80c4: a6 11       ..             ; Restore ROM number
    bne restore_y_check_svc                                           ; 80c6: d0 53       .S             ; Continue to vector setup
; ***************************************************************************************
; NFS initialisation (service &FF: full reset)
; 
; Sets up OS vectors for Tube co-processor support:
;   WRCHV = &051C (page 5 — WRCH handler)
;   RDCHV = &04E7 (page 4 — RDCH handler)
;   BRKV  = &0016 (workspace — BRK/error handler)
;   EVNTV = &06E8 (page 6 — event handler)
; Writes &8E to Tube control register (&FEE0).
; Then copies 3 pages of Tube host code from ROM (&934D/&944D/&954D)
; to RAM (&0400/&0500/&0600), calls tube_post_init (&0414), and copies
; 97 bytes of workspace init from ROM (&9308) to &0016-&0076.
; ***************************************************************************************
; &80c8 referenced 1 time by &80b3
.init_vectors_and_copy
    lda #&1c                                                          ; 80c8: a9 1c       ..             ; Set WRCHV = &051C (Tube WRCH handler)
    sta wrchv                                                         ; 80ca: 8d 0e 02    ...            ; Set WRCHV low byte
    lda #5                                                            ; 80cd: a9 05       ..             ; A=5: WRCHV high byte
    sta wrchv+1                                                       ; 80cf: 8d 0f 02    ...            ; Set WRCHV high byte
    lda #&e7                                                          ; 80d2: a9 e7       ..             ; Set RDCHV = &04E7 (Tube RDCH handler)
    sta rdchv                                                         ; 80d4: 8d 10 02    ...            ; Set RDCHV low byte
    lda #4                                                            ; 80d7: a9 04       ..             ; A=4: RDCHV high byte
    sta rdchv+1                                                       ; 80d9: 8d 11 02    ...            ; Set RDCHV high byte
    lda #&16                                                          ; 80dc: a9 16       ..             ; Set BRKV = &0016 (BRK handler in workspace)
    sta brkv                                                          ; 80de: 8d 02 02    ...            ; Set BRKV low byte
    lda #0                                                            ; 80e1: a9 00       ..             ; A=0: BRKV high byte (page zero)
    sta brkv+1                                                        ; 80e3: 8d 03 02    ...            ; Set BRKV high byte
    lda #&e8                                                          ; 80e6: a9 e8       ..             ; Set EVNTV = &06E8 (event handler in page 6)
    sta evntv                                                         ; 80e8: 8d 20 02    . .            ; Set EVNTV low byte
    lda #6                                                            ; 80eb: a9 06       ..             ; A=6: EVNTV high byte
    sta evntv+1                                                       ; 80ed: 8d 21 02    .!.            ; Set EVNTV high byte
    lda #&8e                                                          ; 80f0: a9 8e       ..             ; Write &8E to Tube control register
    sta tube_status_1_and_tube_control                                ; 80f2: 8d e0 fe    ...            ; Write &8E to Tube control register
    sty zp_temp_10                                                    ; 80f5: 84 10       ..             ; Save Y to temporary
    ldy #0                                                            ; 80f7: a0 00       ..             ; Y=0: start ROM-to-RAM copy loop
; Copy NMI handler code from ROM to RAM pages &04-&06
; &80f9 referenced 1 time by &810c
.cloop
    lda reloc_p4_src,y                                                ; 80f9: b9 4d 93    .M.            ; Load ROM byte from page &93
    sta tube_code_page4,y                                             ; 80fc: 99 00 04    ...            ; Store to page &04 (Tube code)
    lda l944d,y                                                       ; 80ff: b9 4d 94    .M.            ; Load ROM byte from page &94
    sta tube_dispatch_table,y                                         ; 8102: 99 00 05    ...            ; Store to page &05 (dispatch table)
    lda c954d,y                                                       ; 8105: b9 4d 95    .M.            ; Load ROM byte from page &95
    sta tube_code_page6,y                                             ; 8108: 99 00 06    ...            ; Store to page &06
    dey                                                               ; 810b: 88          .              ; DEY wraps 0 -> &FF on first iteration
    bne cloop                                                         ; 810c: d0 eb       ..             ; Loop until 256 bytes copied per page
    jsr tube_post_init                                                ; 810e: 20 14 04     ..            ; Run post-init routine in copied code
    ldx #&60 ; '`'                                                    ; 8111: a2 60       .`             ; X=&60: copy 97 bytes (&60..&00)
; Copy NMI workspace initialiser from ROM to &0016-&0076
; &8113 referenced 1 time by &8119
.copy_nmi_workspace
    lda reloc_zp_src,x                                                ; 8113: bd 08 93    ...            ; Load NMI workspace init byte from ROM
    sta nmi_workspace_start,x                                         ; 8116: 95 16       ..             ; Store to zero page &16+X
    dex                                                               ; 8118: ca          .              ; Next byte
    bpl copy_nmi_workspace                                            ; 8119: 10 f8       ..             ; Loop until all workspace bytes copied
; &811b referenced 1 time by &80c6
.restore_y_check_svc
    ldy zp_temp_10                                                    ; 811b: a4 10       ..             ; Restore Y (ROM number)
.tube_chars_done
    lda #0                                                            ; 811d: a9 00       ..             ; A=0: fall through to service &12 check
; &811f referenced 1 time by &80b1
.check_svc_12
    cmp #&12                                                          ; 811f: c9 12       ..             ; Is this service &12 (select FS)?
    bne dispatch_service                                              ; 8121: d0 04       ..             ; No: check if service < &0D
    cpy #5                                                            ; 8123: c0 05       ..             ; Service &12: Y=5 (NFS)?
    beq select_nfs                                                    ; 8125: f0 5d       .]             ; Y=5: select NFS
; ***************************************************************************************
; Service call dispatcher
; 
; Dispatches MOS service calls 0-12 via the shared dispatch table.
; Uses base offset Y=0, so table index = service number + 1.
; Service numbers >= 13 are ignored (branch to return_2).
; Called via JSR &809F rather than fall-through, so it returns
; to &813C to restore saved registers.
; ***************************************************************************************
; &8127 referenced 1 time by &8121
.dispatch_service
.not_svc_12_nfs
    cmp #&0d                                                          ; 8127: c9 0d       ..             ; Service >= &0D?
.svc_unhandled_return
    bcs return_2                                                      ; 8129: b0 1a       ..             ; Service >= &0D: not handled, return
.do_svc_dispatch
    tax                                                               ; 812b: aa          .              ; X = service number (dispatch index)
    lda rom_svc_num                                                   ; 812c: a5 ce       ..             ; Save &A9 (current service state)
    pha                                                               ; 812e: 48          H              ; Push saved &A9
    lda nfs_temp                                                      ; 812f: a5 cd       ..             ; Save &A8 (workspace page number)
    pha                                                               ; 8131: 48          H              ; Push saved &A8
    stx rom_svc_num                                                   ; 8132: 86 ce       ..             ; Store service number to &A9
    sty nfs_temp                                                      ; 8134: 84 cd       ..             ; Store Y (page number) to &A8
    tya                                                               ; 8136: 98          .              ; A = Y for dispatch table offset
    ldy #0                                                            ; 8137: a0 00       ..             ; Y=0: base offset for service dispatch
    jsr dispatch                                                      ; 8139: 20 9f 80     ..            ; JSR to dispatcher (returns here after handler completes)
    ldx rom_svc_num                                                   ; 813c: a6 ce       ..             ; Recover service claim status from &A9
    pla                                                               ; 813e: 68          h              ; Restore saved &A8 from stack
    sta nfs_temp                                                      ; 813f: 85 cd       ..             ; Write back &A8
; ***************************************************************************************
; Service dispatch epilogue
; 
; Common return path for all dispatched service handlers.
; Restores rom_svc_num from the stack (pushed by dispatch_service),
; transfers X (ROM number) to A, then returns via RTS.
; ***************************************************************************************
.svc_dispatch_epilogue
    pla                                                               ; 8141: 68          h              ; Restore saved A from service dispatch
    sta rom_svc_num                                                   ; 8142: 85 ce       ..             ; Save to workspace &A9
    txa                                                               ; 8144: 8a          .              ; Return ROM number in A
; &8145 referenced 2 times by &8129, &814a
.return_2
    rts                                                               ; 8145: 60          `              ; Return (not our command)

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
; &8146 referenced 2 times by &817b, &8df3
.resume_after_remote
    ldy #4                                                            ; 8146: a0 04       ..             ; Y=4: offset of keyboard disable flag
    lda (net_rx_ptr),y                                                ; 8148: b1 9c       ..             ; Read flag from RX buffer
    beq return_2                                                      ; 814a: f0 f9       ..             ; Zero: keyboard not disabled, skip
    lda #0                                                            ; 814c: a9 00       ..             ; A=0: value to clear flag and re-enable
    tax                                                               ; 814e: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 814f: 91 9c       ..             ; Clear keyboard disable flag in buffer
    tay                                                               ; 8151: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 8152: a9 c9       ..             ; OSBYTE &C9: Econet keyboard disable
    jsr osbyte                                                        ; 8154: 20 f4 ff     ..            ; Re-enable keyboard (X=0, Y=0); Enable keyboard (for Econet)
    lda #&0a                                                          ; 8157: a9 0a       ..             ; Function &0A: remote operation complete
    jsr setup_tx_and_send                                             ; 8159: 20 4c 90     L.            ; Send notification to controlling station
; &815c referenced 1 time by &911c
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 815c: 86 9e       ..             ; Save X (return value from TX)
    lda #&ce                                                          ; 815e: a9 ce       ..             ; OSBYTE &CE: first system mask to reset
; &8160 referenced 1 time by &816b
.clear_osbyte_masks
    ldx nfs_workspace                                                 ; 8160: a6 9e       ..             ; Restore X for OSBYTE call
    ldy #&7f                                                          ; 8162: a0 7f       ..             ; Y=&7F: AND mask (clear bit 7)
    jsr osbyte                                                        ; 8164: 20 f4 ff     ..            ; Reset system mask byte
    adc #1                                                            ; 8167: 69 01       i.             ; Advance to next OSBYTE (&CE -> &CF)
    cmp #&d0                                                          ; 8169: c9 d0       ..             ; Reached &D0? (past &CF)
    beq clear_osbyte_masks                                            ; 816b: f0 f3       ..             ; No: reset &CF too
.skip_kbd_reenable
    lda #0                                                            ; 816d: a9 00       ..             ; A=0: clear remote state
    sta nfs_workspace                                                 ; 816f: 85 9e       ..             ; Clear &A9 (service dispatch state)
    rts                                                               ; 8171: 60          `              ; Return from workspace reset

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
.svc_4_star_command
    ldx #8                                                            ; 8172: a2 08       ..             ; X=8: ROM offset for *ROFF match
    jsr match_rom_string                                              ; 8174: 20 9b 81     ..            ; Match command against ROM string
    bne match_net_cmd                                                 ; 8177: d0 04       ..             ; No match: try *NET command
    sta rom_svc_num                                                   ; 8179: 85 ce       ..             ; Match found: claim service (A=0)
    beq resume_after_remote                                           ; 817b: f0 c9       ..             ; ALWAYS branch

; &817d referenced 1 time by &8177
.match_net_cmd
    ldx #1                                                            ; 817d: a2 01       ..             ; X=1: ROM offset for "NET" match
    jsr match_rom_string                                              ; 817f: 20 9b 81     ..            ; Try matching *NET command
    bne restore_y_return                                              ; 8182: d0 46       .F             ; No match: return unclaimed
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
; &8184 referenced 1 time by &8125
.select_nfs
    jsr call_fscv_shutdown                                            ; 8184: 20 cd 81     ..            ; Notify current FS of shutdown (FSCV A=6)
    sec                                                               ; 8187: 38          8              ; C=1 for ROR
    ror nfs_temp                                                      ; 8188: 66 cd       f.             ; Set bit 7 of l00a8 (inhibit auto-boot)
    jsr issue_vectors_claimed                                         ; 818a: 20 2f 82     /.            ; Claim OS vectors, issue service &0F
    ldy #&1d                                                          ; 818d: a0 1d       ..             ; Y=&1D: top of FS state range
; &818f referenced 1 time by &8197
.initl
    lda (net_rx_ptr),y                                                ; 818f: b1 9c       ..             ; Copy FS state from RX buffer...
    sta fs_state_deb,y                                                ; 8191: 99 eb 0d    ...            ; ...to workspace (offsets &15-&1D)
    dey                                                               ; 8194: 88          .              ; Next byte (descending)
    cpy #&14                                                          ; 8195: c0 14       ..             ; Loop until offset &14 done
    bne initl                                                         ; 8197: d0 f6       ..             ; Continue loop
    beq init_fs_vectors                                               ; 8199: f0 7d       .}             ; ALWAYS branch to init_fs_vectors; ALWAYS branch

; ***************************************************************************************
; Match command text against ROM string table
; 
; Compares characters from (os_text_ptr)+Y against bytes starting
; at binary_version+X (&8008+X). Input is uppercased via AND &DF.
; Returns with Z=1 if the ROM string's NUL terminator was reached
; (match), or Z=0 if a mismatch was found. On match, Y points
; past the matched text; on return, skips trailing spaces.
; ***************************************************************************************
; &819b referenced 2 times by &8174, &817f
.match_rom_string
    ldy nfs_temp                                                      ; 819b: a4 cd       ..             ; Y = saved text pointer offset
; &819d referenced 1 time by &81aa
.match_next_char
    lda (os_text_ptr),y                                               ; 819d: b1 f2       ..             ; Load next input character
    and #&df                                                          ; 819f: 29 df       ).             ; Force uppercase (clear bit 5)
    beq cmd_name_matched                                              ; 81a1: f0 09       ..             ; Input char is NUL/space: check ROM byte
    cmp binary_version,x                                              ; 81a3: dd 08 80    ...            ; Compare with ROM string byte
    bne cmd_name_matched                                              ; 81a6: d0 04       ..             ; Mismatch: check if ROM string ended
    iny                                                               ; 81a8: c8          .              ; Advance input pointer
    inx                                                               ; 81a9: e8          .              ; Advance ROM string pointer
    bne match_next_char                                               ; 81aa: d0 f1       ..             ; Continue matching (always taken)
; &81ac referenced 2 times by &81a1, &81a6
.cmd_name_matched
    lda binary_version,x                                              ; 81ac: bd 08 80    ...            ; Load ROM string byte at match point
    beq skip_cmd_spaces                                               ; 81af: f0 02       ..             ; Zero = end of ROM string = full match
    rts                                                               ; 81b1: 60          `              ; Non-zero = partial/no match; Z=0

; &81b2 referenced 1 time by &81b7
.skpspi
    iny                                                               ; 81b2: c8          .              ; Skip this space
; &81b3 referenced 1 time by &81af
.skip_cmd_spaces
    lda (os_text_ptr),y                                               ; 81b3: b1 f2       ..             ; Load next input character
    cmp #&20 ; ' '                                                    ; 81b5: c9 20       .              ; Is it a space?
    beq skpspi                                                        ; 81b7: f0 f9       ..             ; Yes: keep skipping
    eor #&0d                                                          ; 81b9: 49 0d       I.             ; XOR with CR: Z=1 if end of line
    rts                                                               ; 81bb: 60          `              ; Return (not our service call)

; ***************************************************************************************
; Service 9: *HELP
; 
; Prints the ROM identification string using print_inline.
; ***************************************************************************************
.svc_9_help
    jsr print_inline                                                  ; 81bc: 20 3c 85     <.            ; Print inline ROM identification string
    equs &0d, "NFS 3.34B", &0d                                        ; 81bf: 0d 4e 46... .NF

; &81ca referenced 2 times by &8182, &81df
.restore_y_return
    ldy nfs_temp                                                      ; 81ca: a4 cd       ..             ; Restore Y from temporary
    rts                                                               ; 81cc: 60          `              ; Return (service not claimed)

; ***************************************************************************************
; Notify filing system of shutdown
; 
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; ***************************************************************************************
; &81cd referenced 2 times by &8184, &81d2
.call_fscv_shutdown
    lda #6                                                            ; 81cd: a9 06       ..             ; FSCV reason 6 = FS shutdown
    jmp (fscv)                                                        ; 81cf: 6c 1e 02    l..            ; Tail-call via filing system control vector

; ***************************************************************************************
; Service 3: auto-boot
; 
; Notifies current FS of shutdown via FSCV A=6. Scans keyboard
; (OSBYTE &7A): if the 'N' key is pressed (matrix address &55),
; the keypress is forgotten via OSBYTE &78 and auto-boot proceeds.
; Any other key causes the auto-boot to be declined. If no key is
; pressed, auto-boot proceeds directly. Falls through to
; print_station_info, then init_fs_vectors.
; ***************************************************************************************
.svc_3_autoboot
    jsr call_fscv_shutdown                                            ; 81d2: 20 cd 81     ..            ; Notify current FS of shutdown
    lda #osbyte_scan_keyboard_from_16                                 ; 81d5: a9 7a       .z             ; OSBYTE &7A: scan keyboard
    jsr osbyte                                                        ; 81d7: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 81da: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi print_station_info                                            ; 81db: 30 0a       0.             ; No key pressed: proceed with auto-boot
; ***************************************************************************************
; Check boot key
; 
; Checks if the pressed key (in A) is 'N' (matrix address &55). If
; not 'N', returns to the MOS without claiming the service call
; (another ROM may boot instead). If 'N', forgets the keypress via
; OSBYTE &78 and falls through to print_station_info.
; ***************************************************************************************
.check_boot_key
    eor #&55 ; 'U'                                                    ; 81dd: 49 55       IU             ; XOR with &55: result=0 if key is 'N'
    bne restore_y_return                                              ; 81df: d0 e9       ..             ; Not 'N': return without claiming
    tay                                                               ; 81e1: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 81e2: a9 78       .x             ; OSBYTE &78: clear key-pressed state
    jsr osbyte                                                        ; 81e4: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; ***************************************************************************************
; Print station identification
; 
; Prints "Econet Station <n>" using the station number from the net
; receive buffer, then tests ADLC SR2 for the network clock signal —
; prints " No Clock" if absent. Falls through to init_fs_vectors.
; ***************************************************************************************
; &81e7 referenced 1 time by &81db
.print_station_info
    jsr print_inline                                                  ; 81e7: 20 3c 85     <.            ; Print 'Econet Station ' banner
    equs "Econet Station "                                            ; 81ea: 45 63 6f... Eco

    lda tx_clear_flag                                                 ; 81f9: ad 62 0d    .b.            ; Load local station number
    jsr print_decimal                                                 ; 81fc: 20 b0 85     ..            ; Print station number as decimal
    lda #&20 ; ' '                                                    ; 81ff: a9 20       .              ; A=&20: test bit 5 of SR2 (clock)
    bit econet_control23_or_status2                                   ; 8201: 2c a1 fe    ,..            ; Test ADLC SR2 for network clock
    beq skip_no_clock_msg                                             ; 8204: f0 0d       ..             ; Clock present: skip warning msg
    jsr print_inline                                                  ; 8206: 20 3c 85     <.            ; Print ' No Clock' warning
    equs " No Clock"                                                  ; 8209: 20 4e 6f...  No

    nop                                                               ; 8212: ea          .              ; NOP (padding after inline string)
; &8213 referenced 1 time by &8204
.skip_no_clock_msg
    jsr print_inline                                                  ; 8213: 20 3c 85     <.            ; Print two CRs (blank line)
    equs &0d, &0d                                                     ; 8216: 0d 0d       ..

; ***************************************************************************************
; Initialise filing system vectors
; 
; Copies 14 bytes from fs_vector_addrs (&824E) into FILEV-FSCV (&0212),
; setting all 7 filing system vectors to the extended vector dispatch
; addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
; ROM pointer table entries with the actual NFS handler addresses. Also
; reached directly from select_nfs, bypassing the station display.
; Falls through to issue_vectors_claimed.
; ***************************************************************************************
; &8218 referenced 1 time by &8199
.init_fs_vectors
    ldy #&0d                                                          ; 8218: a0 0d       ..             ; Copy 14 bytes: FS vector addresses → FILEV-FSCV
; &821a referenced 1 time by &8221
.dofsl1
    lda fs_vector_addrs,y                                             ; 821a: b9 4e 82    .N.            ; Load vector address from ROM table
    sta filev,y                                                       ; 821d: 99 12 02    ...            ; Write to FILEV-FSCV vector table
    dey                                                               ; 8220: 88          .              ; Next byte (descending)
    bpl dofsl1                                                        ; 8221: 10 f7       ..             ; Loop until all 14 bytes copied
    jsr setup_rom_ptrs_netv                                           ; 8223: 20 d2 82     ..            ; Read ROM ptr table addr, install NETV
    ldy #&1b                                                          ; 8226: a0 1b       ..             ; Install 7 handler entries in ROM ptr table
    ldx #7                                                            ; 8228: a2 07       ..             ; 7 FS vectors to install
    jsr store_rom_ptr_pair                                            ; 822a: 20 e6 82     ..            ; Install each 3-byte vector entry
    stx rom_svc_num                                                   ; 822d: 86 ce       ..             ; X=0 after loop; store as workspace offset
; ***************************************************************************************
; Issue 'vectors claimed' service and optionally auto-boot
; 
; Issues service &0F (vectors claimed) via OSBYTE &8F, then
; service &0A. If nfs_temp is zero (auto-boot not inhibited),
; sets up the command string "I .BOOT" at &8246 and jumps to
; the FSCV 3 unrecognised-command handler (which matches against
; the command table at &8BD7). The "I." prefix triggers the
; catch-all entry which forwards the command to the fileserver.
; Falls through to run_fscv_cmd.
; ***************************************************************************************
; &822f referenced 1 time by &818a
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 822f: a9 8f       ..             ; A=&8F: issue service request
    ldx #&0f                                                          ; 8231: a2 0f       ..             ; X=&0F: 'vectors claimed' service
    jsr osbyte                                                        ; 8233: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 8236: a2 0a       ..             ; X=&0A: service &0A
    jsr osbyte                                                        ; 8238: 20 f4 ff     ..            ; Issue service &0A
    ldx nfs_temp                                                      ; 823b: a6 cd       ..             ; Non-zero after hard reset: skip auto-boot
    bne return_3                                                      ; 823d: d0 37       .7             ; Non-zero: skip auto-boot
    ldx #&46 ; 'F'                                                    ; 823f: a2 46       .F             ; X = lo byte of auto-boot string at &8292
; ***************************************************************************************
; Run FSCV command from ROM
; 
; Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
; to execute the command string at (X, Y). X is pre-loaded by the
; caller with the low byte of the string address. Also used as a
; data base address by store_rom_ptr_pair for Y-indexed access to
; the handler address table.
; ***************************************************************************************
; &8241 referenced 2 times by &82e6, &82ec
.run_fscv_cmd
    ldy #&82                                                          ; 8241: a0 82       ..             ; Y=&82: ROM page high byte
    jmp fscv_3_star_cmd                                               ; 8243: 4c 93 8b    L..            ; Execute command string at (X, Y)

; Synthetic auto-boot command string. "I " does not match any
; entry in NFS's local command table — "I." requires a dot, and
; "I AM" requires 'A' after the space — so fscv_3_star_cmd
; forwards the entire string to the fileserver, which executes
; the .BOOT file.
    equs "I .BOOT", &0d                                               ; 8246: 49 20 2e... I .            ; Auto-boot string tail / NETV handler data
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
; overwritten with the current ROM bank number at runtime. The
; last entry (FSCV) has no padding byte.
; ***************************************************************************************
; &824e referenced 1 time by &821a
.fs_vector_addrs
    equb &1b                                                          ; 824e: 1b          .              ; FILEV dispatch lo
    equb &ff                                                          ; 824f: ff          .              ; FILEV dispatch hi
    equb &1e                                                          ; 8250: 1e          .              ; ARGSV dispatch lo
    equb &ff                                                          ; 8251: ff          .              ; ARGSV dispatch hi
    equb &21                                                          ; 8252: 21          !              ; BGETV dispatch lo
    equb &ff                                                          ; 8253: ff          .              ; BGETV dispatch hi
    equb &24                                                          ; 8254: 24          $              ; BPUTV dispatch lo
    equb &ff                                                          ; 8255: ff          .              ; BPUTV dispatch hi
    equb &27                                                          ; 8256: 27          '              ; GBPBV dispatch lo
    equb &ff                                                          ; 8257: ff          .              ; GBPBV dispatch hi
    equb &2a                                                          ; 8258: 2a          *              ; FINDV dispatch lo
    equb &ff                                                          ; 8259: ff          .              ; FINDV dispatch hi
    equb &2d                                                          ; 825a: 2d          -              ; FSCV dispatch lo
    equb &ff                                                          ; 825b: ff          .              ; FSCV dispatch hi
    equb &95                                                          ; 825c: 95          .              ; FILEV handler lo (&8695)
    equb &86                                                          ; 825d: 86          .              ; FILEV handler hi
    equb 0                                                            ; 825e: 00          .              ; (ROM bank — overwritten)
    equb &e2                                                          ; 825f: e2          .              ; ARGSV handler lo (&88E2)
    equb &88                                                          ; 8260: 88          .              ; ARGSV handler hi
    equb 0                                                            ; 8261: 00          .              ; (ROM bank — overwritten)
    equb &86                                                          ; 8262: 86          .              ; BGETV handler lo (&8486)
    equb &84                                                          ; 8263: 84          .              ; BGETV handler hi
    equb 0                                                            ; 8264: 00          .              ; (ROM bank — overwritten)
    equb &a3                                                          ; 8265: a3          .              ; BPUTV handler lo (&83A3)
    equb &83                                                          ; 8266: 83          .              ; BPUTV handler hi
    equb 0                                                            ; 8267: 00          .              ; (ROM bank — overwritten)
    equb &eb                                                          ; 8268: eb          .              ; GBPBV handler lo (&89EB)
    equb &89                                                          ; 8269: 89          .              ; GBPBV handler hi
    equb 0                                                            ; 826a: 00          .              ; (ROM bank — overwritten)
    equb &4a                                                          ; 826b: 4a          J              ; FINDV handler lo (&894A)
    equb &89                                                          ; 826c: 89          .              ; FINDV handler hi
    equb 0                                                            ; 826d: 00          .              ; (ROM bank — overwritten)
    equb &8c                                                          ; 826e: 8c          .              ; FSCV handler lo (&808C)
    equb &80                                                          ; 826f: 80          .              ; FSCV handler hi

; ***************************************************************************************
; Service 1: claim absolute workspace
; 
; Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
; and FS command buffer (&0F). If Y >= &10, workspace already
; allocated — returns unchanged.
; 
; On Entry:
;     Y: current top of absolute workspace
; 
; On Exit:
;     Y: updated top of absolute workspace (max of input and &10)
; ***************************************************************************************
.svc_1_abs_workspace
    cpy #&10                                                          ; 8270: c0 10       ..             ; Compare Y against workspace boundary
    bcs return_3                                                      ; 8272: b0 02       ..             ; Y>=&10: already allocated, return
    ldy #&10                                                          ; 8274: a0 10       ..             ; Claim workspace up to page &10
; &8276 referenced 2 times by &823d, &8272
.return_3
    rts                                                               ; 8276: 60          `              ; Return to caller

    equb 8, &90                                                       ; 8277: 08 90       ..

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
; 
; On Entry:
;     Y: next available workspace page
; 
; On Exit:
;     Y: next available workspace page after NFS (input + 2)
; ***************************************************************************************
.svc_2_private_workspace
    sty net_rx_ptr_hi                                                 ; 8279: 84 9d       ..             ; Store RX buffer page pointer
    iny                                                               ; 827b: c8          .              ; Advance to next page
    sty nfs_workspace_hi                                              ; 827c: 84 9f       ..             ; Store workspace page pointer
    lda #0                                                            ; 827e: a9 00       ..             ; A=0 for clearing workspace
    ldy #4                                                            ; 8280: a0 04       ..             ; Y=4: remote status offset
    sta (net_rx_ptr),y                                                ; 8282: 91 9c       ..             ; Clear status byte in net receive buffer
    ldy #&ff                                                          ; 8284: a0 ff       ..             ; Y=&FF: used for later iteration
    sta net_rx_ptr                                                    ; 8286: 85 9c       ..             ; Clear RX ptr low byte
    sta nfs_workspace                                                 ; 8288: 85 9e       ..             ; Clear workspace ptr low byte
    sta nfs_temp                                                      ; 828a: 85 cd       ..             ; Clear RXCB iteration counter
    sta tx_ctrl_status                                                ; 828c: 8d 3a 0d    .:.            ; Clear TX semaphore (no TX in progress)
    tax                                                               ; 828f: aa          .              ; X=0 for OSBYTE; X=&00
    lda #osbyte_read_write_last_break_type                            ; 8290: a9 fd       ..             ; OSBYTE &FD: read type of last reset
    jsr osbyte                                                        ; 8292: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 8295: 8a          .              ; X = break type from OSBYTE result; X=value of type of last reset
    beq read_station_id                                               ; 8296: f0 2c       .,             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 8298: a0 15       ..             ; Y=&15: printer station offset in RX buffer
    lda #&fe                                                          ; 829a: a9 fe       ..             ; &FE = no server selected
    sta fs_server_stn                                                 ; 829c: 8d 00 0e    ...            ; Station &FE = no server selected
    sta (net_rx_ptr),y                                                ; 829f: 91 9c       ..             ; Store &FE at printer station offset
    ldy #2                                                            ; 82a1: a0 02       ..             ; Y=2: printer server offset
    lda #&eb                                                          ; 82a3: a9 eb       ..             ; A=&EB: default printer server
    sta (nfs_workspace),y                                             ; 82a5: 91 9e       ..             ; Store printer server at offset 2
    iny                                                               ; 82a7: c8          .              ; Y=&03
    lda #0                                                            ; 82a8: a9 00       ..             ; A=0: clear remaining fields
    sta fs_server_net                                                 ; 82aa: 8d 01 0e    ...            ; Clear FS server network number
    sta (nfs_workspace),y                                             ; 82ad: 91 9e       ..             ; Clear workspace byte at offset 3
    sta prot_status                                                   ; 82af: 8d 63 0d    .c.            ; Clear protection status mask
    sta fs_messages_flag                                              ; 82b2: 8d 06 0e    ...            ; Clear FS messages flag
; &82b5 referenced 1 time by &82c2
.init_rxcb_entries
    lda nfs_temp                                                      ; 82b5: a5 cd       ..             ; Load RXCB counter
    jsr calc_handle_offset                                            ; 82b7: 20 b8 8d     ..            ; Convert to workspace byte offset
    bcs read_station_id                                               ; 82ba: b0 08       ..             ; C=1: past max handles, done
    lda #&3f ; '?'                                                    ; 82bc: a9 3f       .?             ; Mark RXCB as available
    sta (nfs_workspace),y                                             ; 82be: 91 9e       ..             ; Write &3F flag to workspace
    inc nfs_temp                                                      ; 82c0: e6 cd       ..             ; Next RXCB number
    bne init_rxcb_entries                                             ; 82c2: d0 f1       ..             ; Loop for all RXCBs
; &82c4 referenced 2 times by &8296, &82ba
.read_station_id
    lda station_id_disable_net_nmis                                   ; 82c4: ad 18 fe    ...            ; Read station ID (also INTOFF)
    sta tx_clear_flag                                                 ; 82c7: 8d 62 0d    .b.            ; Store station ID for TX scout
    jsr trampoline_adlc_init                                          ; 82ca: 20 63 96     c.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 82cd: a9 40       .@             ; Enable user-level RX (LFLAG=&40)
    sta rx_status_flags                                               ; 82cf: 8d 38 0d    .8.            ; Store to rx_flags
; ***************************************************************************************
; Set up ROM pointer table and NETV
; 
; Reads the ROM pointer table base address via OSBYTE &A8, stores
; it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
; one 3-byte extended vector entry (addr=&9008, rom=current) into
; the ROM pointer table at offset &36, installing osword_dispatch
; as the NETV handler.
; ***************************************************************************************
; &82d2 referenced 1 time by &8223
.setup_rom_ptrs_netv
    lda #osbyte_read_rom_ptr_table_low                                ; 82d2: a9 a8       ..             ; OSBYTE &A8: read ROM pointer table address
    ldx #0                                                            ; 82d4: a2 00       ..             ; X=0: read low byte
    ldy #&ff                                                          ; 82d6: a0 ff       ..             ; Y=&FF: read high byte
    jsr osbyte                                                        ; 82d8: 20 f4 ff     ..            ; Returns table address in X (lo) Y (hi); Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 82db: 86 f6       ..             ; Store table base address low byte; X=value of address of ROM pointer table (low byte)
    sty osrdsc_ptr_hi                                                 ; 82dd: 84 f7       ..             ; Store table base address high byte; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 82df: a0 36       .6             ; NETV extended vector offset in ROM ptr table
    sty netv                                                          ; 82e1: 8c 24 02    .$.            ; Set NETV low byte = &36 (vector dispatch)
    ldx #1                                                            ; 82e4: a2 01       ..             ; Install 1 entry (NETV) in ROM ptr table
; &82e6 referenced 2 times by &822a, &82f8
.store_rom_ptr_pair
    lda run_fscv_cmd,y                                                ; 82e6: b9 41 82    .A.            ; Load handler address low byte from table
    sta (osrdsc_ptr),y                                                ; 82e9: 91 f6       ..             ; Store to ROM pointer table
    iny                                                               ; 82eb: c8          .              ; Next byte
    lda run_fscv_cmd,y                                                ; 82ec: b9 41 82    .A.            ; Load handler address high byte from table
    sta (osrdsc_ptr),y                                                ; 82ef: 91 f6       ..             ; Store to ROM pointer table
    iny                                                               ; 82f1: c8          .              ; Next byte
    lda romsel_copy                                                   ; 82f2: a5 f4       ..             ; Write current ROM bank number
    sta (osrdsc_ptr),y                                                ; 82f4: 91 f6       ..             ; Store ROM number to ROM pointer table
    iny                                                               ; 82f6: c8          .              ; Advance to next entry position
    dex                                                               ; 82f7: ca          .              ; Count down entries
    bne store_rom_ptr_pair                                            ; 82f8: d0 ec       ..             ; Loop until all entries installed
    ldy nfs_workspace_hi                                              ; 82fa: a4 9f       ..             ; Y = workspace high byte + 1 = next free page
    iny                                                               ; 82fc: c8          .              ; Advance past workspace page
    rts                                                               ; 82fd: 60          `              ; Return; Y = page after NFS workspace

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
    ldy #&1d                                                          ; 82fe: a0 1d       ..             ; Copy 10 bytes: FS state to workspace backup
; &8300 referenced 1 time by &8308
.fsdiel
    lda fs_state_deb,y                                                ; 8300: b9 eb 0d    ...            ; Load FS state byte at offset Y
    sta (net_rx_ptr),y                                                ; 8303: 91 9c       ..             ; Store to workspace backup area
    dey                                                               ; 8305: 88          .              ; Next byte down
    cpy #&14                                                          ; 8306: c0 14       ..             ; Offsets &15-&1D: server, handles, OPT, etc.
    bne fsdiel                                                        ; 8308: d0 f6       ..             ; Loop for offsets &1D..&15
    lda #osbyte_printer_driver_going_dormant                          ; 830a: a9 7b       .{             ; A=&7B: printer driver going dormant
    jmp osbyte                                                        ; 830c: 4c f4 ff    L..            ; Printer driver going dormant

; ***************************************************************************************
; Initialise TX control block for FS reply on port &90
; 
; Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
; up the TX control block, stores the port and control bytes, then
; decrements the control flag. Used by send_fs_reply_cmd to prepare
; for receiving the fileserver's reply.
; ***************************************************************************************
; &830f referenced 1 time by &8382
.init_tx_ctrl_data
.init_tx_reply_port
    lda #&90                                                          ; 830f: a9 90       ..             ; A=&90: FS reply port (PREPLY)
; &8311 referenced 2 times by &880f, &8f79
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 8311: 20 1d 83     ..            ; Init TXCB from template
    sta txcb_port                                                     ; 8314: 85 c1       ..             ; Store port number in TXCB
    lda #3                                                            ; 8316: a9 03       ..             ; Control byte: 3 = transmit
    sta txcb_start                                                    ; 8318: 85 c4       ..             ; Store control byte in TXCB
    dec txcb_ctrl                                                     ; 831a: c6 c0       ..             ; Decrement TXCB flag to arm TX
    rts                                                               ; 831c: 60          `              ; Return after port setup

; ***************************************************************************************
; Initialise TX control block at &00C0 from template
; 
; Copies 12 bytes from tx_ctrl_template (&8335) to &00C0.
; For the first 2 bytes (Y=0,1), also copies the fileserver
; station/network from &0E00/&0E01 to &00C2/&00C3.
; The template sets up: control=&80, port=&99 (FS command port),
; command data length=&0F, plus padding bytes.
; ***************************************************************************************
; &831d referenced 3 times by &8311, &8371, &83ba
.init_tx_ctrl_block
    pha                                                               ; 831d: 48          H              ; Preserve A across call
    ldy #&0b                                                          ; 831e: a0 0b       ..             ; Copy 12 bytes (Y=11..0)
; &8320 referenced 1 time by &8331
.fstxl1
    lda tx_ctrl_template,y                                            ; 8320: b9 35 83    .5.            ; Load template byte
    sta txcb_ctrl,y                                                   ; 8323: 99 c0 00    ...            ; Store to TX control block at &00C0
    cpy #2                                                            ; 8326: c0 02       ..             ; Y < 2: also copy FS server station/network
    bpl fstxl2                                                        ; 8328: 10 06       ..             ; Skip station/network copy for Y >= 2
    lda fs_server_stn,y                                               ; 832a: b9 00 0e    ...            ; Load FS server station (Y=0) or network (Y=1)
    sta txcb_dest,y                                                   ; 832d: 99 c2 00    ...            ; Store to dest station/network at &00C2
; &8330 referenced 1 time by &8328
.fstxl2
    dey                                                               ; 8330: 88          .              ; Next byte (descending)
    bpl fstxl1                                                        ; 8331: 10 ed       ..             ; Loop until all 12 bytes copied
    pla                                                               ; 8333: 68          h              ; Restore A
    rts                                                               ; 8334: 60          `              ; Return

; ***************************************************************************************
; TX control block template (TXTAB, 12 bytes)
; 
; 12-byte template copied to &00C0 by init_tx_ctrl. Defines the
; TX control block for FS commands: control flag, port, station/
; network, and data buffer pointers (&0F00-&0FFF). The 4-byte
; Econet addresses use only the low 2 bytes; upper bytes are &FF.
; ***************************************************************************************
; &8335 referenced 1 time by &8320
.tx_ctrl_template
    equb &80                                                          ; 8335: 80          .              ; Control flag
    equb &99                                                          ; 8336: 99          .              ; Port (FS command = &99)
    equb 0                                                            ; 8337: 00          .              ; Station (filled at runtime)
    equb 0                                                            ; 8338: 00          .              ; Network (filled at runtime)
    equb 0                                                            ; 8339: 00          .              ; Buffer start low
    equb &0f                                                          ; 833a: 0f          .              ; Buffer start high (page &0F)
; &833b referenced 3 times by &8890, &896a, &915e
.tx_ctrl_upper
    equb &ff                                                          ; 833b: ff          .              ; Buffer start pad (4-byte Econet addr)
    equb &ff                                                          ; 833c: ff          .              ; Buffer start pad
    equb &ff                                                          ; 833d: ff          .              ; Buffer end low
    equb &0f                                                          ; 833e: 0f          .              ; Buffer end high (page &0F)
    equb &ff                                                          ; 833f: ff          .              ; Buffer end pad
    equb &ff                                                          ; 8340: ff          .              ; Buffer end pad

; ***************************************************************************************
; Prepare FS command with carry set
; 
; Alternate entry to prepare_fs_cmd that pushes A, loads &2A
; into fs_error_ptr, and enters with carry set (SEC). The carry
; flag is later tested by build_send_fs_cmd to select the
; byte-stream (BSXMIT) transmission path.
; 
; On Entry:
;     A: flag byte to include in FS command
;     Y: function code for FS header
; ***************************************************************************************
; &8341 referenced 1 time by &8a3c
.prepare_cmd_with_flag
    pha                                                               ; 8341: 48          H              ; Save flag byte for command
    lda #&2a ; '*'                                                    ; 8342: a9 2a       .*             ; A=&2A: error ptr for retry
    sec                                                               ; 8344: 38          8              ; C=1: include flag in FS command
    bcs store_fs_hdr_fn                                               ; 8345: b0 14       ..             ; ALWAYS branch to prepare_fs_cmd; ALWAYS branch

; &8347 referenced 2 times by &86d8, &8781
.prepare_cmd_clv
    clv                                                               ; 8347: b8          .              ; V=0: command has no flag byte
    bvc store_fs_hdr_clc                                              ; 8348: 50 10       P.             ; ALWAYS branch to prepare_fs_cmd; ALWAYS branch

; ***************************************************************************************
; *BYE handler (logoff)
; 
; Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
; Dispatched from the command match table at &8BD7 for "BYE".
; ***************************************************************************************
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 834a: a9 77       .w             ; A=&77: OSBYTE close spool/exec
    jsr osbyte                                                        ; 834c: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #&17                                                          ; 834f: a0 17       ..             ; Y=function code for HDRFN
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
; &8351 referenced 12 times by &807d, &8835, &88ab, &88fd, &8924, &8997, &89c1, &8a9b, &8b51, &8c19, &8c50, &8cc9
.prepare_fs_cmd
    clv                                                               ; 8351: b8          .              ; V=0: standard FS command path
; &8352 referenced 2 times by &8893, &896d
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 8352: ad 02 0e    ...            ; Copy URD handle from workspace to buffer
    sta fs_cmd_urd                                                    ; 8355: 8d 02 0f    ...            ; Store URD at &0F02
    lda #&2a ; '*'                                                    ; 8358: a9 2a       .*             ; A=&2A: error ptr for retry
; &835a referenced 1 time by &8348
.store_fs_hdr_clc
    clc                                                               ; 835a: 18          .              ; CLC: no byte-stream path
; &835b referenced 1 time by &8345
.store_fs_hdr_fn
    sty fs_cmd_y_param                                                ; 835b: 8c 01 0f    ...            ; Store function code at &0F01
    sta fs_error_ptr                                                  ; 835e: 85 b8       ..             ; Store error ptr for TX poll
    ldy #1                                                            ; 8360: a0 01       ..             ; Y=1: copy CSD (offset 1) then LIB (offset 0)
; &8362 referenced 1 time by &8369
.copy_dir_handles
    lda fs_csd_handle,y                                               ; 8362: b9 03 0e    ...            ; Copy CSD and LIB handles to command buffer; A=timeout period for FS reply
    sta fs_cmd_csd,y                                                  ; 8365: 99 03 0f    ...            ; Store at &0F03 (CSD) and &0F04 (LIB)
    dey                                                               ; 8368: 88          .              ; Y=function code
    bpl copy_dir_handles                                              ; 8369: 10 f7       ..             ; Loop for both handles
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
; command code to read the return code. Error &D6 ("not found",
;     on_entry={"x": "buffer extent (command-specific data bytes)", "y": "function
; code", "a": "timeout period for FS reply", "c": "0 for standard FS path, 1 for byte-
; stream (BSXMIT)"},
;     on_exit={"a": "0 on success", "x": "0 on success, &D6 on not-found", "y": "1
; (offset past command code in reply)"})
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
; &836b referenced 1 time by &8af4
.build_send_fs_cmd
    php                                                               ; 836b: 08          .              ; Save carry (FS path vs byte-stream)
    lda #&90                                                          ; 836c: a9 90       ..             ; Reply port &90 (PREPLY)
    sta fs_cmd_type                                                   ; 836e: 8d 00 0f    ...            ; Store at &0F00 (HDRREP)
    jsr init_tx_ctrl_block                                            ; 8371: 20 1d 83     ..            ; Copy TX template to &00C0
    txa                                                               ; 8374: 8a          .              ; A = X (buffer extent)
    adc #5                                                            ; 8375: 69 05       i.             ; HPTR = header (5) + data (X) bytes to send
    sta txcb_end                                                      ; 8377: 85 c8       ..             ; Store to TXCB end-pointer low
    plp                                                               ; 8379: 28          (              ; Restore carry flag
    bcs dofsl5                                                        ; 837a: b0 1c       ..             ; C=1: byte-stream path (BSXMIT)
    php                                                               ; 837c: 08          .              ; Save flags for send_fs_reply_cmd
    jsr setup_tx_ptr_c0                                               ; 837d: 20 45 86     E.            ; Point net_tx_ptr to &00C0; transmit
    plp                                                               ; 8380: 28          (              ; Restore flags
; &8381 referenced 2 times by &8791, &8a78
.send_fs_reply_cmd
    php                                                               ; 8381: 08          .              ; Save flags (V flag state)
    jsr init_tx_ctrl_data                                             ; 8382: 20 0f 83     ..            ; Set up RX wait for FS reply
    lda fs_error_ptr                                                  ; 8385: a5 b8       ..             ; Load error ptr for TX retry
    jsr send_to_fs                                                    ; 8387: 20 4b 84     K.            ; Transmit and wait (BRIANX)
    plp                                                               ; 838a: 28          (              ; Restore flags
; &838b referenced 1 time by &83a1
.dofsl7
    iny                                                               ; 838b: c8          .              ; Y=1: skip past command code byte
    lda (txcb_start),y                                                ; 838c: b1 c4       ..             ; Load return code from FS reply
    tax                                                               ; 838e: aa          .              ; X = return code
    beq return_dofsl7                                                 ; 838f: f0 06       ..             ; Zero: success, return
    bvc check_fs_error                                                ; 8391: 50 02       P.             ; V=0: standard path, error is fatal
    adc #&2a ; '*'                                                    ; 8393: 69 2a       i*             ; ADC #&2A: test for &D6 (not found)
; &8395 referenced 1 time by &8391
.check_fs_error
    bne store_fs_error                                                ; 8395: d0 6c       .l             ; Non-zero: hard error, go to FSERR
; &8397 referenced 1 time by &838f
.return_dofsl7
    rts                                                               ; 8397: 60          `              ; Return (success or soft &D6 error)

; &8398 referenced 1 time by &837a
.dofsl5
    pla                                                               ; 8398: 68          h              ; Discard saved flags from stack
    ldx #&c0                                                          ; 8399: a2 c0       ..             ; X=&C0: TXCB address for byte-stream TX
    iny                                                               ; 839b: c8          .              ; Y++ past command code
    jsr econet_tx_retry                                               ; 839c: 20 49 92     I.            ; Byte-stream transmit with retry
    sta fs_load_addr_3                                                ; 839f: 85 b3       ..             ; Store result to &B3
    bcc dofsl7                                                        ; 83a1: 90 e8       ..             ; C=0: success, check reply code
.bputv_handler
    clc                                                               ; 83a3: 18          .              ; CLC for address addition
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
; &83a4 referenced 1 time by &8487
.handle_bput_bget
    pha                                                               ; 83a4: 48          H              ; Save A (BPUT byte) on stack
    sta fs_error_flags                                                ; 83a5: 8d df 0f    ...            ; Also save byte at &0FDF for BSXMIT
    txa                                                               ; 83a8: 8a          .              ; Transfer X for stack save
    pha                                                               ; 83a9: 48          H              ; Save X on stack
    tya                                                               ; 83aa: 98          .              ; Transfer Y (handle) for stack save
    pha                                                               ; 83ab: 48          H              ; Save Y (handle) on stack
    php                                                               ; 83ac: 08          .              ; Save P (C = BPUT/BGET selector) on stack
    jsr handle_to_mask_clc                                            ; 83ad: 20 8a 85     ..            ; Convert handle Y to single-bit mask
    sty fs_handle_mask                                                ; 83b0: 8c de 0f    ...            ; Store handle bitmask at &0FDE
    sty fs_spool0                                                     ; 83b3: 84 cf       ..             ; Store handle bitmask for sequence tracking
    ldy #&90                                                          ; 83b5: a0 90       ..             ; &90 = data port (PREPLY)
    sty fs_putb_buf                                                   ; 83b7: 8c dc 0f    ...            ; Store reply port in command buffer
    jsr init_tx_ctrl_block                                            ; 83ba: 20 1d 83     ..            ; Set up 12-byte TXCB from template
    lda #&dc                                                          ; 83bd: a9 dc       ..             ; CB reply buffer at &0FDC
    sta txcb_start                                                    ; 83bf: 85 c4       ..             ; Store reply buffer ptr low in TXCB
    lda #&e0                                                          ; 83c1: a9 e0       ..             ; Error buffer at &0FE0
    sta txcb_end                                                      ; 83c3: 85 c8       ..             ; Store error buffer ptr low in TXCB
    iny                                                               ; 83c5: c8          .              ; Y=1 (from init_tx_ctrl_block exit)
    ldx #9                                                            ; 83c6: a2 09       ..             ; X=9: BPUT function code
    plp                                                               ; 83c8: 28          (              ; Restore C: selects BPUT (0) vs BGET (1)
    bcc store_retry_count                                             ; 83c9: 90 01       ..             ; C=0 (BPUT): keep X=9
    dex                                                               ; 83cb: ca          .              ; X=&08
; &83cc referenced 1 time by &83c9
.store_retry_count
    stx fs_getb_buf                                                   ; 83cc: 8e dd 0f    ...            ; Store function code at &0FDD
    lda fs_handle_mask                                                ; 83cf: ad de 0f    ...            ; Load handle bitmask for BPUT/BGET
    ldx #&c0                                                          ; 83d2: a2 c0       ..             ; X=&C0: TXCB address for econet_tx_retry
    jsr econet_tx_retry                                               ; 83d4: 20 49 92     I.            ; Transmit via byte-stream protocol
    ldx fs_getb_buf                                                   ; 83d7: ae dd 0f    ...            ; Load reply byte from buffer
    beq update_sequence_return                                        ; 83da: f0 40       .@             ; Zero reply = success, skip error handling
    ldy #&1f                                                          ; 83dc: a0 1f       ..             ; Copy 32-byte reply to error buffer at &0FE0
; &83de referenced 1 time by &83e5
.error1
    lda fs_putb_buf,y                                                 ; 83de: b9 dc 0f    ...            ; Load reply byte at offset Y
    sta fs_error_buf,y                                                ; 83e1: 99 e0 0f    ...            ; Store to error buffer at &0FE0+Y
    dey                                                               ; 83e4: 88          .              ; Next byte (descending)
    bpl error1                                                        ; 83e5: 10 f7       ..             ; Loop until all 32 bytes copied
    tax                                                               ; 83e7: aa          .              ; X=File handle
    lda #osbyte_read_write_spool_file_handle                          ; 83e8: a9 c7       ..             ; A=&C7: read *SPOOL file handle
    jsr osbyte                                                        ; 83ea: 20 f4 ff     ..            ; Read/Write *SPOOL file handle
    txa                                                               ; 83ed: 8a          .              ; X=value of *SPOOL file handle
    jsr handle_to_mask_a                                              ; 83ee: 20 89 85     ..            ; Convert SPOOL handle to bitmask
    cpy fs_spool0                                                     ; 83f1: c4 cf       ..             ; Compare SPOOL mask with file mask
    bne dispatch_fs_error                                             ; 83f3: d0 07       ..             ; Not SPOOL file: dispatch FS error
    ldx #<(sp_dot_string)                                             ; 83f5: a2 45       .E             ; Load '*SP.' command string low
    ldy #>(sp_dot_string)                                             ; 83f7: a0 84       ..             ; Y=&85: high byte of OSCLI string in ROM
    jsr oscli                                                         ; 83f9: 20 f7 ff     ..            ; Close SPOOL/EXEC via "*SP." or "*E."
; &83fc referenced 1 time by &83f3
.dispatch_fs_error
    lda #&e0                                                          ; 83fc: a9 e0       ..             ; Reset CB pointer to error buffer at &0FE0
    sta txcb_start                                                    ; 83fe: 85 c4       ..             ; Reset reply ptr to error buffer
    ldx fs_getb_buf                                                   ; 8400: ae dd 0f    ...            ; Reload reply byte for error dispatch
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
; &8403 referenced 1 time by &8395
.store_fs_error
    stx fs_last_error                                                 ; 8403: 8e 09 0e    ...            ; Remember raw FS error code
    ldy #1                                                            ; 8406: a0 01       ..             ; Y=1: point to error number byte in reply
    cpx #&a8                                                          ; 8408: e0 a8       ..             ; Clamp FS errors below &A8 to standard &A8
    bcs find_cr_terminator                                            ; 840a: b0 04       ..             ; Error >= &A8: keep original value
    lda #&a8                                                          ; 840c: a9 a8       ..             ; Error < &A8: override with standard &A8
    sta (txcb_start),y                                                ; 840e: 91 c4       ..             ; Write clamped error number to reply buffer
; &8410 referenced 2 times by &840a, &8415
.find_cr_terminator
    iny                                                               ; 8410: c8          .              ; Advance to next reply buffer byte
    lda #&0d                                                          ; 8411: a9 0d       ..             ; A=CR: terminator to search for
    eor (txcb_start),y                                                ; 8413: 51 c4       Q.             ; XOR with buffer byte (0 when CR)
    bne find_cr_terminator                                            ; 8415: d0 f9       ..             ; Not CR: continue scanning
    sta (txcb_start),y                                                ; 8417: 91 c4       ..             ; Store 0 (from XOR) to replace CR
    jmp (txcb_start)                                                  ; 8419: 6c c4 00    l..            ; Execute error via JMP indirect

; &841c referenced 1 time by &83da
.update_sequence_return
    sta fs_sequence_nos                                               ; 841c: 8d 08 0e    ...            ; Save updated sequence number
    pla                                                               ; 841f: 68          h              ; Restore Y from stack
    tay                                                               ; 8420: a8          .              ; Transfer A to Y for indexing
    pla                                                               ; 8421: 68          h              ; Restore X from stack
    tax                                                               ; 8422: aa          .              ; Transfer to X for return
    pla                                                               ; 8423: 68          h              ; Restore A from stack
    rts                                                               ; 8424: 60          `              ; Return to caller

; &8425 referenced 1 time by &8478
.error_not_listening
    lda #8                                                            ; 8425: a9 08       ..             ; Error code 8: "Not listening" error
    bne set_listen_offset                                             ; 8427: d0 04       ..             ; ALWAYS branch to set_listen_offset; ALWAYS branch

; &8429 referenced 1 time by &868e
.nlistn
    lda (net_tx_ptr,x)                                                ; 8429: a1 9a       ..             ; Load TX status byte for error lookup
; &842b referenced 2 times by &8484, &89b9
.nlisne
    and #7                                                            ; 842b: 29 07       ).             ; Mask to 3-bit error code (0-7)
; &842d referenced 1 time by &8427
.set_listen_offset
    tax                                                               ; 842d: aa          .              ; X = error code index
    ldy error_offsets,x                                               ; 842e: bc 14 80    ...            ; Look up error message offset from table
    ldx #0                                                            ; 8431: a2 00       ..             ; X=0: start writing at &0101
    stx l0100                                                         ; 8433: 8e 00 01    ...            ; Store BRK opcode at &0100
; &8436 referenced 1 time by &8440
.copy_error_message
    lda error_msg_table,y                                             ; 8436: b9 b0 84    ...            ; Load error message byte
    sta l0101,x                                                       ; 8439: 9d 01 01    ...            ; Build error message at &0101+
    beq execute_brk_error                                             ; 843c: f0 04       ..             ; Zero byte = end of message; go execute BRK
    inx                                                               ; 843e: e8          .              ; Advance output buffer position
    iny                                                               ; 843f: c8          .              ; Advance source string pointer
    bne copy_error_message                                            ; 8440: d0 f4       ..             ; Continue copying message bytes
; &8442 referenced 1 time by &843c
.execute_brk_error
    jmp l0100                                                         ; 8442: 4c 00 01    L..            ; Execute constructed BRK error

.sp_dot_string
    equs "SP."                                                        ; 8445: 53 50 2e    SP.
    equb &0d                                                          ; 8448: 0d          .

; &8449 referenced 3 times by &8731, &8fbc, &927e
.send_to_fs_star
    lda #&2a ; '*'                                                    ; 8449: a9 2a       .*             ; A=&2A: error ptr for FS retry
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
; &844b referenced 2 times by &8387, &881b
.send_to_fs
    pha                                                               ; 844b: 48          H              ; Save function code on stack
    lda rx_status_flags                                               ; 844c: ad 38 0d    .8.            ; Load current rx_flags
    pha                                                               ; 844f: 48          H              ; Save rx_flags on stack for restore
    ora #&80                                                          ; 8450: 09 80       ..             ; Set bit7: FS transaction in progress
    sta rx_status_flags                                               ; 8452: 8d 38 0d    .8.            ; Write back updated rx_flags
.skip_rx_flag_set
    lda #0                                                            ; 8455: a9 00       ..             ; Push two zero bytes as timeout counters
    pha                                                               ; 8457: 48          H              ; First zero for timeout
    pha                                                               ; 8458: 48          H              ; Second zero for timeout
    tay                                                               ; 8459: a8          .              ; Y=0: index for flag byte check; Y=&00
    tsx                                                               ; 845a: ba          .              ; TSX: index stack-based timeout via X
; &845b referenced 3 times by &8465, &846a, &846f
.incpx
    lda (net_tx_ptr),y                                                ; 845b: b1 9a       ..             ; Load TX flag byte from ctrl block
    bmi fs_wait_cleanup                                               ; 845d: 30 12       0.             ; Bit 7 set: TX complete, clean up
    jsr check_escape                                                  ; 845f: 20 7b 84     {.            ; Check for Escape during TX wait
    dec l0101,x                                                       ; 8462: de 01 01    ...            ; Three-stage nested timeout: inner loop
    bne incpx                                                         ; 8465: d0 f4       ..             ; Inner not expired: keep polling
    dec l0102,x                                                       ; 8467: de 02 01    ...            ; Middle timeout loop
    bne incpx                                                         ; 846a: d0 ef       ..             ; Middle not expired: keep polling
    dec l0104,x                                                       ; 846c: de 04 01    ...            ; Outer timeout loop (slowest)
    bne incpx                                                         ; 846f: d0 ea       ..             ; Outer not expired: keep polling
; &8471 referenced 1 time by &845d
.fs_wait_cleanup
    pla                                                               ; 8471: 68          h              ; Pop first timeout byte
    pla                                                               ; 8472: 68          h              ; Pop second timeout byte
    pla                                                               ; 8473: 68          h              ; Pop saved rx_flags into A
    sta rx_status_flags                                               ; 8474: 8d 38 0d    .8.            ; Restore saved rx_flags from stack
    pla                                                               ; 8477: 68          h              ; Pop saved function code
    beq error_not_listening                                           ; 8478: f0 ab       ..             ; A=saved func code; zero would mean no reply
    rts                                                               ; 847a: 60          `              ; Return to caller

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
; &847b referenced 2 times by &845f, &8675
.check_escape
    lda #&7e ; '~'                                                    ; 847b: a9 7e       .~             ; A=&7E: OSBYTE acknowledge escape
; ***************************************************************************************
; Test MOS escape flag and abort if pending
; 
; Tests MOS escape flag (&FF bit 7). If escape is pending:
; acknowledges via OSBYTE &7E, writes &3F (deleted marker) into
; the control block via (net_tx_ptr),Y, and branches to the
; NLISTN error path. If no escape, returns immediately.
; ***************************************************************************************
.check_escape_handler
    bit escape_flag                                                   ; 847d: 24 ff       $.             ; Test escape flag (bit 7)
    bpl return_bget                                                   ; 847f: 10 23       .#             ; Bit 7 clear: no escape, return
    jsr osbyte                                                        ; 8481: 20 f4 ff     ..            ; Acknowledge escape via OSBYTE &7E
    bne nlisne                                                        ; 8484: d0 a5       ..             ; Non-zero: report 'Not listening'
.bgetv_handler
    sec                                                               ; 8486: 38          8              ; C=1: flag for BGET mode
    jsr handle_bput_bget                                              ; 8487: 20 a4 83     ..            ; Handle BGET via FS command; Handle BPUT/BGET file byte I/O
    sec                                                               ; 848a: 38          8              ; SEC: set carry for error check
    lda #&fe                                                          ; 848b: a9 fe       ..             ; A=&FE: mask for EOF check
    bit fs_error_flags                                                ; 848d: 2c df 0f    ,..            ; BIT l0fdf: test error flags
    bvs return_bget                                                   ; 8490: 70 12       p.             ; V=1: error, return early
    clc                                                               ; 8492: 18          .              ; CLC: no error
    bmi tx_flow_control                                               ; 8493: 30 07       0.             ; Bit 7 set: set EOF hint flag
    lda fs_spool0                                                     ; 8495: a5 cf       ..             ; Load handle bitmask for flag op
    jsr clear_fs_flag                                                 ; 8497: 20 e0 85     ..            ; Clear EOF hint flag for this handle
    bcc tx_error_classify                                             ; 849a: 90 05       ..             ; Flag cleared: load handle mask
; &849c referenced 1 time by &8493
.tx_flow_control
    lda fs_spool0                                                     ; 849c: a5 cf       ..             ; Load handle bitmask for flow control
    jsr set_fs_flag                                                   ; 849e: 20 e5 85     ..            ; Set EOF hint flag for this handle
; &84a1 referenced 1 time by &849a
.tx_error_classify
    lda fs_handle_mask                                                ; 84a1: ad de 0f    ...            ; Load handle mask for return value
; &84a4 referenced 2 times by &847f, &8490
.return_bget
    rts                                                               ; 84a4: 60          `              ; Return with handle mask in A

; &84a5 referenced 1 time by &8761
.add_5_to_y
    iny                                                               ; 84a5: c8          .              ; Y += 5 (entry point); Y += 5 (entry point)
; &84a6 referenced 1 time by &8a4e
.add_4_to_y
    iny                                                               ; 84a6: c8          .              ; Y += 4 (entry point)
    iny                                                               ; 84a7: c8          .              ; Y += 3
    iny                                                               ; 84a8: c8          .              ; Y += 2
    iny                                                               ; 84a9: c8          .              ; Y += 1
    rts                                                               ; 84aa: 60          `              ; Return with Y adjusted

; &84ab referenced 1 time by &8750
.sub_4_from_y
    dey                                                               ; 84ab: 88          .              ; Y -= 4 (entry point)
; &84ac referenced 2 times by &885d, &8a56
.sub_3_from_y
    dey                                                               ; 84ac: 88          .              ; Y -= 3 (entry point)
    dey                                                               ; 84ad: 88          .              ; Y -= 2
    dey                                                               ; 84ae: 88          .              ; Y -= 1
.return_4
    rts                                                               ; 84af: 60          `              ; Return with handle mask in A

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
; &84b0 referenced 1 time by &8436
.error_msg_table
    equb &a0                                                          ; 84b0: a0          .
    equs "Line Jammed", 0                                             ; 84b1: 4c 69 6e... Lin
    equb &a1                                                          ; 84bd: a1          .
    equs "Net Error", 0                                               ; 84be: 4e 65 74... Net
    equb &a2                                                          ; 84c8: a2          .
    equs "Not listening", 0                                           ; 84c9: 4e 6f 74... Not
    equb &a3                                                          ; 84d7: a3          .
    equs "No Clock", 0                                                ; 84d8: 4e 6f 20... No
    equb &a4                                                          ; 84e1: a4          .
    equs "Bad Txcb", 0                                                ; 84e2: 42 61 64... Bad
    equb &11                                                          ; 84eb: 11          .
    equs "Escape", 0                                                  ; 84ec: 45 73 63... Esc
    equb &cb                                                          ; 84f3: cb          .
    equs "Bad Option", 0                                              ; 84f4: 42 61 64... Bad
    equb &a5                                                          ; 84ff: a5          .
    equs "No reply", 0                                                ; 8500: 4e 6f 20... No

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
; 
; On Entry:
;     A: function code
;     X: control block pointer low
;     Y: control block pointer high
; ***************************************************************************************
; &8509 referenced 6 times by &808c, &8695, &88e2, &894a, &89eb, &8b93
.save_fscv_args
    sta fs_last_byte_flag                                             ; 8509: 85 bd       ..             ; A = function code / command
    stx fs_options                                                    ; 850b: 86 bb       ..             ; X = control block ptr lo
    sty fs_block_offset                                               ; 850d: 84 bc       ..             ; Y = control block ptr hi
    stx fs_crc_lo                                                     ; 850f: 86 be       ..             ; X dup for indexed access via (fs_crc)
    sty fs_crc_hi                                                     ; 8511: 84 bf       ..             ; Y dup for indexed access
    rts                                                               ; 8513: 60          `              ; Return

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
; &8514 referenced 2 times by &886f, &889a
.decode_attribs_6bit
    ldy #&0e                                                          ; 8514: a0 0e       ..             ; Y=&0E: attribute byte offset in param block
    lda (fs_options),y                                                ; 8516: b1 bb       ..             ; Load FS attribute byte
    and #&3f ; '?'                                                    ; 8518: 29 3f       )?             ; Mask to 6 bits (FS → BBC direction)
    ldx #4                                                            ; 851a: a2 04       ..             ; X=4: skip first 4 table entries (BBC→FS half)
    bne attrib_shift_bits                                             ; 851c: d0 04       ..             ; ALWAYS branch to shared bitmask builder; ALWAYS branch

; ***************************************************************************************
; Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)
; 
; Masks A to 5 bits and builds an access bitmask via the
; lookup table at &8531. Each input bit position maps to a
; different output bit via the table. The conversion is done
; by iterating through the source bits and OR-ing in the
; corresponding destination bits from the table, translating
; between BBC (8-bit) and fileserver (5-bit) protection formats.
; 
; On Entry:
;     A: BBC attribute byte (bits 0-4 used)
; 
; On Exit:
;     A: FS attribute bitmask (5-bit)
;     X: corrupted
; ***************************************************************************************
; &851e referenced 2 times by &879c, &88b7
.decode_attribs_5bit
    and #&1f                                                          ; 851e: 29 1f       ).             ; Mask to 5 bits (BBC → FS direction)
    ldx #&ff                                                          ; 8520: a2 ff       ..             ; X=&FF: INX makes 0; start from table index 0
; &8522 referenced 1 time by &851c
.attrib_shift_bits
    sta fs_error_ptr                                                  ; 8522: 85 b8       ..             ; Temp storage for source bitmask to shift out
    lda #0                                                            ; 8524: a9 00       ..             ; A=0: accumulate destination bits here
; &8526 referenced 1 time by &852e
.map_attrib_bits
    inx                                                               ; 8526: e8          .              ; Next table entry
    lsr fs_error_ptr                                                  ; 8527: 46 b8       F.             ; Shift out source bits one at a time
    bcc skip_set_attrib_bit                                           ; 8529: 90 03       ..             ; Bit was 0: skip this destination bit
    ora access_bit_table,x                                            ; 852b: 1d 31 85    .1.            ; OR in destination bit from lookup table
; &852e referenced 1 time by &8529
.skip_set_attrib_bit
    bne map_attrib_bits                                               ; 852e: d0 f6       ..             ; Loop while source bits remain (A != 0)
    rts                                                               ; 8530: 60          `              ; Return; A = converted attribute bitmask

; &8531 referenced 1 time by &852b
.access_bit_table
    equb &50, &20, 5, 2, &88, 4, 8, &80, &10, 1, 2                    ; 8531: 50 20 05... P .

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
; &853c referenced 13 times by &81bc, &81e7, &8206, &8213, &8c21, &8c2b, &8c39, &8c44, &8c5e, &8c6f, &8c82, &8c96, &8ca3
.print_inline
    pla                                                               ; 853c: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 853d: 85 b0       ..             ; Store return addr low as string ptr
    pla                                                               ; 853f: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 8540: 85 b1       ..             ; Store return addr high as string ptr
    ldy #0                                                            ; 8542: a0 00       ..             ; Y=0: offset for indirect load
; &8544 referenced 1 time by &8551
.print_inline_char
    inc fs_load_addr                                                  ; 8544: e6 b0       ..             ; Advance pointer past return address / to next char
    bne print_next_char                                               ; 8546: d0 02       ..             ; No page wrap: skip high byte inc
    inc fs_load_addr_hi                                               ; 8548: e6 b1       ..             ; Handle page crossing in pointer
; &854a referenced 1 time by &8546
.print_next_char
    lda (fs_load_addr),y                                              ; 854a: b1 b0       ..             ; Load next byte from inline string
    bmi filev_attrib_code_check                                       ; 854c: 30 05       0.             ; Bit 7 set? Done — this byte is the next opcode
    jsr osasci                                                        ; 854e: 20 e3 ff     ..            ; Write character
    bne print_inline_char                                             ; 8551: d0 f1       ..             ; Continue printing loop
; &8553 referenced 1 time by &854c
.filev_attrib_code_check
    jmp (fs_load_addr)                                                ; 8553: 6c b0 00    l..            ; Jump to address of high-bit byte (resumes code after string)

; ***************************************************************************************
; Skip leading spaces in parameter block
; 
; Advances Y past space characters in (fs_options),Y.
; Returns with the first non-space character in A.
; Sets carry if the character is >= 'A' (alphabetic).
; ***************************************************************************************
; &8556 referenced 3 times by &855b, &8c0d, &8d07
.skip_spaces
    lda (fs_options),y                                                ; 8556: b1 bb       ..             ; Load character from parameter string
    iny                                                               ; 8558: c8          .              ; Advance to next character
    cmp #&20 ; ' '                                                    ; 8559: c9 20       .              ; Compare against space (ASCII &20)
    beq skip_spaces                                                   ; 855b: f0 f9       ..             ; Space found: keep scanning
    dey                                                               ; 855d: 88          .              ; Back up one (first non-space char)
    cmp #&41 ; 'A'                                                    ; 855e: c9 41       .A             ; Compare against 'A' for case flag
    rts                                                               ; 8560: 60          `              ; Return: A=char, C set if >= 'A'

; ***************************************************************************************
; Parse decimal number from (fs_options),Y (DECIN)
; 
; Reads ASCII digits and accumulates in &B2 (fs_load_addr_2).
; Multiplication by 10 uses the identity: n*10 = n*8 + n*2,
; computed as ASL &B2 (x2), then A = &B2*4 via two ASLs,
; then ADC &B2 gives x10.
; Terminates on "." (pathname separator), control chars, or space.
; The delimiter handling was revised to support dot-separated path
; components (e.g. "1.$.PROG",
;     on_entry={"y": "offset into (fs_options) buffer"},
;     on_exit={"a": "parsed value (accumulated in &B2)", "x": "initial A value (saved
; by TAX)", "y": "offset past last digit parsed"})
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
; &8561 referenced 2 times by &8d0e, &8d14
.parse_decimal
    tax                                                               ; 8561: aa          .              ; Save A in X for caller
    lda #0                                                            ; 8562: a9 00       ..             ; Zero accumulator
    sta fs_load_addr_2                                                ; 8564: 85 b2       ..             ; Clear accumulator workspace
; &8566 referenced 1 time by &8583
.scan_decimal_digit
    lda (fs_options),y                                                ; 8566: b1 bb       ..             ; Load next char from buffer
    cmp #&40 ; '@'                                                    ; 8568: c9 40       .@             ; Letter or above?
    bcs no_dot_exit                                                   ; 856a: b0 19       ..             ; Yes: not a digit, done
    cmp #&2e ; '.'                                                    ; 856c: c9 2e       ..             ; Dot separator?
    beq parse_decimal_rts                                             ; 856e: f0 16       ..             ; Yes: exit with C=1 (dot found)
    bmi no_dot_exit                                                   ; 8570: 30 13       0.             ; Control char or space: done
    and #&0f                                                          ; 8572: 29 0f       ).             ; Mask ASCII digit to 0-9
    sta fs_load_addr_3                                                ; 8574: 85 b3       ..             ; Save new digit
    asl fs_load_addr_2                                                ; 8576: 06 b2       ..             ; Running total * 2
    lda fs_load_addr_2                                                ; 8578: a5 b2       ..             ; A = running total * 2
    asl a                                                             ; 857a: 0a          .              ; A = running total * 4
    asl a                                                             ; 857b: 0a          .              ; A = running total * 8
    adc fs_load_addr_2                                                ; 857c: 65 b2       e.             ; + total*2 = total * 10
    adc fs_load_addr_3                                                ; 857e: 65 b3       e.             ; + digit = total*10 + digit
    sta fs_load_addr_2                                                ; 8580: 85 b2       ..             ; Store new running total
    iny                                                               ; 8582: c8          .              ; Advance to next char
    bne scan_decimal_digit                                            ; 8583: d0 e1       ..             ; Loop (always: Y won't wrap to 0)
; &8585 referenced 2 times by &856a, &8570
.no_dot_exit
    clc                                                               ; 8585: 18          .              ; No dot found: C=0
; &8586 referenced 1 time by &856e
.parse_decimal_rts
    lda fs_load_addr_2                                                ; 8586: a5 b2       ..             ; Return result in A
    rts                                                               ; 8588: 60          `              ; Return with result in A

; ***************************************************************************************
; Convert handle in A to bitmask
; 
; Transfers A to Y via TAY, then falls through to
; handle_to_mask_clc to clear carry and convert.
; 
; On Entry:
;     A: file handle number (&20-&27, or 0)
; 
; On Exit:
;     A: preserved
;     X: preserved
;     Y: bitmask (single bit set) or &FF if invalid
; ***************************************************************************************
; &8589 referenced 3 times by &83ee, &8a06, &8ecd
.handle_to_mask_a
    tay                                                               ; 8589: a8          .              ; Handle number to Y for conversion
; ***************************************************************************************
; Convert handle to bitmask (carry cleared)
; 
; Clears carry to ensure handle_to_mask converts
; unconditionally. Falls through to handle_to_mask.
; 
; On Entry:
;     Y: file handle number (&20-&27, or 0)
; 
; On Exit:
;     A: preserved
;     X: preserved
;     Y: bitmask (single bit set) or &FF if invalid
; ***************************************************************************************
; &858a referenced 3 times by &83ad, &8823, &88ed
.handle_to_mask_clc
    clc                                                               ; 858a: 18          .              ; Force unconditional conversion
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
; through unchanged (means "no file",
;     on_entry={"y": "handle number", "c": "0: convert, 1 with Y=0: skip, 1 with Y!=0:
; convert"},
;     on_exit={"a": "preserved", "x": "preserved", "y": "bitmask (single bit set) or
; &FF if handle invalid"})
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
; &858b referenced 1 time by &894e
.handle_to_mask
    pha                                                               ; 858b: 48          H              ; Save A (will be restored on exit)
    txa                                                               ; 858c: 8a          .              ; Save X (will be restored on exit)
    pha                                                               ; 858d: 48          H              ;   (second half of X save)
    tya                                                               ; 858e: 98          .              ; A = handle from Y
    bcc y2fsl5                                                        ; 858f: 90 02       ..             ; C=0: always convert
    beq handle_mask_exit                                              ; 8591: f0 0f       ..             ; C=1 and Y=0: skip (handle 0 = none)
; &8593 referenced 1 time by &858f
.y2fsl5
    sec                                                               ; 8593: 38          8              ; C=1 and Y!=0: convert
    sbc #&1f                                                          ; 8594: e9 1f       ..             ; A = handle - &1F (1-based bit position)
    tax                                                               ; 8596: aa          .              ; X = shift count
    lda #1                                                            ; 8597: a9 01       ..             ; Start with bit 0 set
; &8599 referenced 1 time by &859b
.y2fsl2
    asl a                                                             ; 8599: 0a          .              ; Shift bit left
    dex                                                               ; 859a: ca          .              ; Count down
    bne y2fsl2                                                        ; 859b: d0 fc       ..             ; Loop until correct position
    ror a                                                             ; 859d: 6a          j              ; Undo final extra shift
    tay                                                               ; 859e: a8          .              ; Y = resulting bitmask
    bne handle_mask_exit                                              ; 859f: d0 01       ..             ; Non-zero: valid mask, skip to exit
    dey                                                               ; 85a1: 88          .              ; Zero: invalid handle, set Y=&FF
; &85a2 referenced 2 times by &8591, &859f
.handle_mask_exit
    pla                                                               ; 85a2: 68          h              ; Restore X
    tax                                                               ; 85a3: aa          .              ; Restore X from stack
    pla                                                               ; 85a4: 68          h              ; Restore A
    rts                                                               ; 85a5: 60          `              ; Return with mask in X

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
; &85a6 referenced 2 times by &8981, &8ee7
.mask_to_handle
    ldx #0                                                            ; 85a6: a2 00       ..             ; X = 0 (bit position counter)
; &85a8 referenced 1 time by &85aa
.fs2al1
    inx                                                               ; 85a8: e8          .              ; Count this bit position
    lsr a                                                             ; 85a9: 4a          J              ; Shift mask right; C=0 when done
    bne fs2al1                                                        ; 85aa: d0 fc       ..             ; Loop until all bits shifted out
    txa                                                               ; 85ac: 8a          .              ; A = X = &1F + bit position = handle
    adc #&1e                                                          ; 85ad: 69 1e       i.             ; Add &1E+C(=0) = &1E; handle=&1F+pos
    rts                                                               ; 85af: 60          `              ; Return with A=handle number

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
; &85b0 referenced 2 times by &81fc, &8c28
.print_decimal
    tay                                                               ; 85b0: a8          .              ; Y=dividend, A=100: hundreds digit
    lda #&64 ; 'd'                                                    ; 85b1: a9 64       .d             ; Print hundreds digit
    jsr print_decimal_digit                                           ; 85b3: 20 bd 85     ..            ; A=10: tens divisor
    lda #&0a                                                          ; 85b6: a9 0a       ..             ; Print tens digit
    jsr print_decimal_digit                                           ; 85b8: 20 bd 85     ..            ; Transfer remainder to A
    lda #1                                                            ; 85bb: a9 01       ..             ; Convert to ASCII and print
; ***************************************************************************************
; Print one decimal digit by repeated subtraction
; 
; Divides Y by A using repeated subtraction. Prints the
; quotient as an ASCII digit ('0'-'9'). Returns with the
; remainder in Y. X starts at &2F ('0'-1) and increments
; once per subtraction, giving the ASCII digit directly.
; 
; On Entry:
;     A: divisor (stored to &B8)
;     Y: dividend
; 
; On Exit:
;     Y: remainder
; ***************************************************************************************
; &85bd referenced 2 times by &85b3, &85b8
.print_decimal_digit
    sta fs_error_ptr                                                  ; 85bd: 85 b8       ..             ; Store divisor in temporary
    tya                                                               ; 85bf: 98          .              ; Transfer dividend (Y) to A
    ldx #&2f ; '/'                                                    ; 85c0: a2 2f       ./             ; X=&2F: ASCII '0'-1 (loop init)
    sec                                                               ; 85c2: 38          8              ; Set carry for subtraction
; &85c3 referenced 1 time by &85c6
.decimal_divide_loop
    inx                                                               ; 85c3: e8          .              ; Increment digit (ASCII '0'..'9')
    sbc fs_error_ptr                                                  ; 85c4: e5 b8       ..             ; Subtract divisor from remainder
    bcs decimal_divide_loop                                           ; 85c6: b0 fb       ..             ; Carry set: subtract again
    adc fs_error_ptr                                                  ; 85c8: 65 b8       e.             ; Add back divisor (undo last SBC)
    tay                                                               ; 85ca: a8          .              ; Remainder to Y for next digit
    txa                                                               ; 85cb: 8a          .              ; Quotient digit (X) to A for print
; &85cc referenced 1 time by &85ff
.print_via_osasci
    jmp osasci                                                        ; 85cc: 4c e3 ff    L..            ; Write character

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
; &85cf referenced 2 times by &8717, &87ca
.compare_addresses
    ldx #4                                                            ; 85cf: a2 04       ..             ; Compare 4 bytes (index 4,3,2,1)
; &85d1 referenced 1 time by &85d8
.compare_addr_byte
    lda addr_work,x                                                   ; 85d1: b5 af       ..             ; Load byte from first address
    eor fs_load_addr_3,x                                              ; 85d3: 55 b3       U.             ; XOR with corresponding byte
    bne return_compare                                                ; 85d5: d0 03       ..             ; Mismatch: Z=0, return unequal
    dex                                                               ; 85d7: ca          .              ; Next byte
    bne compare_addr_byte                                             ; 85d8: d0 f7       ..             ; Continue comparing
; &85da referenced 1 time by &85d5
.return_compare
    rts                                                               ; 85da: 60          `              ; Return with Z flag result

.fscv_7_read_handles
    ldx #&20 ; ' '                                                    ; 85db: a2 20       .              ; X=first handle (&20)
    ldy #&27 ; '''                                                    ; 85dd: a0 27       .'             ; Y=last handle (&27)
; &85df referenced 1 time by &8604
.return_fscv_handles
    rts                                                               ; 85df: 60          `              ; Return (FSCV 7 read handles)

; ***************************************************************************************
; Clear bit(s) in FS flags (&0E07)
; 
; Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
; the specified bits. Falls through to set_fs_flag to store.
; 
; On Entry:
;     A: bitmask of bits to clear
; 
; On Exit:
;     A: updated fs_eof_flags value
; ***************************************************************************************
; &85e0 referenced 3 times by &8497, &883e, &8a82
.clear_fs_flag
    eor #&ff                                                          ; 85e0: 49 ff       I.             ; Invert A (NOT mask)
    and fs_eof_flags                                                  ; 85e2: 2d 07 0e    -..            ; AND inverted mask to clear bits
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
; 
; On Entry:
;     A: bitmask of bits to set
; 
; On Exit:
;     A: updated fs_eof_flags value
; ***************************************************************************************
; &85e5 referenced 5 times by &849e, &892a, &8976, &899d, &8a85
.set_fs_flag
    ora fs_eof_flags                                                  ; 85e5: 0d 07 0e    ...            ; OR mask into EOF flags
    sta fs_eof_flags                                                  ; 85e8: 8d 07 0e    ...            ; Store updated EOF flags
    rts                                                               ; 85eb: 60          `              ; Return to caller

; ***************************************************************************************
; Print byte as two hex digits
; 
; Prints the high nibble first (via 4× LSR), then the low
; nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
; and output via OSASCI.
; 
; On Entry:
;     A: byte to print as two hex digits
; 
; On Exit:
;     A: preserved (original byte)
;     X: corrupted (by OSASCI)
; ***************************************************************************************
; &85ec referenced 2 times by &863a, &8c6c
.print_hex
    pha                                                               ; 85ec: 48          H              ; Save full byte on stack
    lsr a                                                             ; 85ed: 4a          J              ; Shift high nibble to low position
    lsr a                                                             ; 85ee: 4a          J              ; Continue shift (4 LSRs total)
    lsr a                                                             ; 85ef: 4a          J              ; Continue shift
    lsr a                                                             ; 85f0: 4a          J              ; High nibble now in bits 0-3
    jsr print_hex_nibble                                              ; 85f1: 20 f7 85     ..            ; Print high nibble as hex
    pla                                                               ; 85f4: 68          h              ; Restore original byte
    and #&0f                                                          ; 85f5: 29 0f       ).             ; Mask to low nibble
; &85f7 referenced 1 time by &85f1
.print_hex_nibble
    ora #&30 ; '0'                                                    ; 85f7: 09 30       .0             ; Convert to ASCII digit ('0'-'9')
    cmp #&3a ; ':'                                                    ; 85f9: c9 3a       .:             ; Compare against ':' (past '9'?)
    bcc print_hex_digit                                               ; 85fb: 90 02       ..             ; Digit 0-9: skip A-F adjustment
    adc #6                                                            ; 85fd: 69 06       i.             ; Add 7 to get ASCII 'A'-'F'
; &85ff referenced 2 times by &85fb, &8643
.print_hex_digit
    bne print_via_osasci                                              ; 85ff: d0 cb       ..             ; ALWAYS branch to print character
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
; &8601 referenced 2 times by &8704, &8784
.print_file_info
    ldy fs_messages_flag                                              ; 8601: ac 06 0e    ...            ; Check if file info available
    beq return_fscv_handles                                           ; 8604: f0 d9       ..             ; No info available: return
    ldy #0                                                            ; 8606: a0 00       ..             ; Y=0: start of filename string
; &8608 referenced 1 time by &8616
.print_filename_loop
    lda (fs_crc_lo),y                                                 ; 8608: b1 be       ..             ; Load filename character
    cmp #&0d                                                          ; 860a: c9 0d       ..             ; CR: end of filename
    beq pad_filename_spaces                                           ; 860c: f0 0a       ..             ; CR: pad rest of filename field
    cmp #&20 ; ' '                                                    ; 860e: c9 20       .              ; Also end name on space character
    beq pad_filename_spaces                                           ; 8610: f0 06       ..             ; Space: also ends filename
    jsr osasci                                                        ; 8612: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8615: c8          .              ; Advance to next filename byte
    bne print_filename_loop                                           ; 8616: d0 f0       ..             ; Loop until all chars printed
; &8618 referenced 3 times by &860c, &8610, &861e
.pad_filename_spaces
    jsr print_space                                                   ; 8618: 20 41 86     A.            ; Print padding space
    iny                                                               ; 861b: c8          .              ; Advance past filename position
    cpy #&0c                                                          ; 861c: c0 0c       ..             ; Pad to 12 chars wide
    bcc pad_filename_spaces                                           ; 861e: 90 f8       ..             ; Continue padding if < 12 chars
    ldy #5                                                            ; 8620: a0 05       ..             ; Y=5: high byte of load address
    jsr print_hex_bytes                                               ; 8622: 20 36 86     6.            ; Print load address as 2 hex bytes; Print load address as 2 hex bytes
    jsr print_exec_and_len                                            ; 8625: 20 2b 86     +.            ; Print exec address and length
    jmp osnewl                                                        ; 8628: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &862b referenced 1 time by &8625
.print_exec_and_len
    ldy #9                                                            ; 862b: a0 09       ..             ; Y=9: exec address offset
    jsr print_hex_bytes                                               ; 862d: 20 36 86     6.            ; Print exec address bytes
    ldy #&0c                                                          ; 8630: a0 0c       ..             ; Y=&0C: file length offset
    ldx #3                                                            ; 8632: a2 03       ..             ; X=3: print 3 bytes for file length
    bne num01                                                         ; 8634: d0 02       ..             ; ALWAYS branch

; &8636 referenced 2 times by &8622, &862d
.print_hex_bytes
    ldx #4                                                            ; 8636: a2 04       ..             ; X=4: print 4 bytes for address
; &8638 referenced 2 times by &8634, &863f
.num01
    lda (fs_options),y                                                ; 8638: b1 bb       ..             ; Load address/length byte
    jsr print_hex                                                     ; 863a: 20 ec 85     ..            ; Print as 2 hex digits
    dey                                                               ; 863d: 88          .              ; Move to next lower address byte
    dex                                                               ; 863e: ca          .              ; Decrement byte counter
    bne num01                                                         ; 863f: d0 f7       ..             ; Loop for remaining hex bytes
; &8641 referenced 2 times by &8618, &8d5d
.print_space
    lda #&20 ; ' '                                                    ; 8641: a9 20       .              ; A=space: separator character
    bne print_hex_digit                                               ; 8643: d0 ba       ..             ; ALWAYS branch

; ***************************************************************************************
; Set up TX pointer to control block at &00C0
; 
; Points net_tx_ptr to &00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; ***************************************************************************************
; &8645 referenced 2 times by &837d, &880a
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 8645: a2 c0       ..             ; X=&C0: TX control block at &00C0
    stx net_tx_ptr                                                    ; 8647: 86 9a       ..             ; Set TX pointer lo
    ldx #0                                                            ; 8649: a2 00       ..             ; X=0: page zero
    stx net_tx_ptr_hi                                                 ; 864b: 86 9b       ..             ; Set TX pointer hi byte to page 0
; ***************************************************************************************
; Transmit and poll for result (full retry)
; 
; Sets A=&FF (retry count) and Y=&60 (timeout parameter).
; Falls through to tx_poll_core.
; ***************************************************************************************
; &864d referenced 3 times by &9002, &905c, &925c
.tx_poll_ff
    lda #&ff                                                          ; 864d: a9 ff       ..             ; A=&FF: full retry count
; &864f referenced 1 time by &8fa5
.tx_poll_timeout
    ldy #&60 ; '`'                                                    ; 864f: a0 60       .`             ; Y=timeout parameter (&60 = standard)
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
; &8651 referenced 1 time by &8fe7
.tx_poll_core
    pha                                                               ; 8651: 48          H              ; Save retry count on stack
    tya                                                               ; 8652: 98          .              ; Transfer timeout to A
    pha                                                               ; 8653: 48          H              ; Save timeout on stack
    ldx #0                                                            ; 8654: a2 00       ..             ; X=0 for (net_tx_ptr,X) indirect
    lda (net_tx_ptr,x)                                                ; 8656: a1 9a       ..             ; Load TXCB byte 0 (control/status)
; &8658 referenced 1 time by &868b
.tx_retry
    sta (net_tx_ptr,x)                                                ; 8658: 81 9a       ..             ; Write control byte to start TX
    pha                                                               ; 865a: 48          H              ; Save control byte for retry
; &865b referenced 1 time by &865e
.tx_semaphore_spin
    asl tx_ctrl_status                                                ; 865b: 0e 3a 0d    .:.            ; Test TX semaphore (C=1 when free)
    bcc tx_semaphore_spin                                             ; 865e: 90 fb       ..             ; Spin until semaphore released
    lda net_tx_ptr                                                    ; 8660: a5 9a       ..             ; Copy TX ptr lo to NMI block
    sta nmi_tx_block                                                  ; 8662: 85 a0       ..             ; Store for NMI handler access
    lda net_tx_ptr_hi                                                 ; 8664: a5 9b       ..             ; Copy TX ptr hi to NMI block
    sta nmi_tx_block_hi                                               ; 8666: 85 a1       ..             ; Store for NMI handler access
    jsr trampoline_tx_setup                                           ; 8668: 20 60 96     `.            ; Initiate ADLC TX via trampoline
; &866b referenced 1 time by &866d
.poll_txcb_status
    lda (net_tx_ptr,x)                                                ; 866b: a1 9a       ..             ; Poll TXCB byte 0 for completion
    bmi poll_txcb_status                                              ; 866d: 30 fc       0.             ; Bit 7 set: still busy, keep polling
    asl a                                                             ; 866f: 0a          .              ; Shift bit 6 into bit 7 (error flag)
    bpl tx_success                                                    ; 8670: 10 1f       ..             ; Bit 6 clear: success, clean return
    asl a                                                             ; 8672: 0a          .              ; Shift bit 5 into carry
    beq tx_not_listening                                              ; 8673: f0 18       ..             ; Zero: fatal error, no escape
    jsr check_escape                                                  ; 8675: 20 7b 84     {.            ; Check for user escape condition
    pla                                                               ; 8678: 68          h              ; Discard saved control byte
    tax                                                               ; 8679: aa          .              ; Save to X for retry delay
    pla                                                               ; 867a: 68          h              ; Restore timeout parameter
    tay                                                               ; 867b: a8          .              ; Back to Y
    pla                                                               ; 867c: 68          h              ; Restore retry count
    beq tx_not_listening                                              ; 867d: f0 0e       ..             ; No retries left: report error
    sbc #1                                                            ; 867f: e9 01       ..             ; Decrement retry count
    pha                                                               ; 8681: 48          H              ; Save updated retry count
    tya                                                               ; 8682: 98          .              ; Timeout to A for delay
    pha                                                               ; 8683: 48          H              ; Save timeout parameter
    txa                                                               ; 8684: 8a          .              ; Control byte for delay duration
; &8685 referenced 2 times by &8686, &8689
.delay_1ms
    dex                                                               ; 8685: ca          .              ; Inner delay loop
    bne delay_1ms                                                     ; 8686: d0 fd       ..             ; Spin until X=0
    dey                                                               ; 8688: 88          .              ; Outer delay loop
    bne delay_1ms                                                     ; 8689: d0 fa       ..             ; Continue delay
    beq tx_retry                                                      ; 868b: f0 cb       ..             ; ALWAYS branch

; &868d referenced 2 times by &8673, &867d
.tx_not_listening
    tax                                                               ; 868d: aa          .              ; Save error code in X
    jmp nlistn                                                        ; 868e: 4c 29 84    L).            ; Report 'Not listening' error

; &8691 referenced 1 time by &8670
.tx_success
    pla                                                               ; 8691: 68          h              ; Discard saved control byte
    pla                                                               ; 8692: 68          h              ; Discard timeout parameter
    pla                                                               ; 8693: 68          h              ; Discard retry count
    rts                                                               ; 8694: 60          `              ; Return (success)

; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Saves A/X/Y, copies the filename pointer from the parameter block
; to os_text_ptr, then uses GSINIT/GSREAD to parse the filename into
; &0FC5+. Sets fs_crc_lo/hi to point at the parsed filename buffer.
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
    jsr save_fscv_args                                                ; 8695: 20 09 85     ..            ; Load FILEV function code from A
; ***************************************************************************************
; Copy filename pointer to os_text_ptr and parse
; 
; Copies the 2-byte filename pointer from (fs_options),Y into
; os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
; to parse the filename via GSINIT/GSREAD into the &0E30 buffer.
; ***************************************************************************************
.copy_filename_ptr
    ldy #1                                                            ; 8698: a0 01       ..             ; Y=1: copy 2 bytes (high then low)
; &869a referenced 1 time by &86a0
.file1
    lda (fs_options),y                                                ; 869a: b1 bb       ..             ; Load filename ptr from control block
    sta os_text_ptr,y                                                 ; 869c: 99 f2 00    ...            ; Store to MOS text pointer (&F2/&F3)
    dey                                                               ; 869f: 88          .              ; Next byte (descending)
    bpl file1                                                         ; 86a0: 10 f8       ..             ; Loop for both bytes
    iny                                                               ; 86a2: c8          .              ; Y=1: offset past filename pointer
    ldx #&ff                                                          ; 86a3: a2 ff       ..             ; X=&FF: parse all characters
    clc                                                               ; 86a5: 18          .              ; C=0: normal string parse entry
    jsr gsinit                                                        ; 86a6: 20 c2 ff     ..            ; Init string parsing via GSINIT
; &86a9 referenced 1 time by &86b2
.quote1
    jsr gsread                                                        ; 86a9: 20 c5 ff     ..            ; Read next character via GSREAD
    bcs tx_result_check                                               ; 86ac: b0 06       ..             ; C=1 from GSREAD: end of string reached
    inx                                                               ; 86ae: e8          .              ; Advance buffer index
    sta l0fc5,x                                                       ; 86af: 9d c5 0f    ...            ; Store parsed character to &0E30+X
    bcc quote1                                                        ; 86b2: 90 f5       ..             ; ALWAYS loop (GSREAD clears C on success); ALWAYS branch

; &86b4 referenced 1 time by &86ac
.tx_result_check
    lda #&0d                                                          ; 86b4: a9 0d       ..             ; CR = &0D
    sta l0fc6,x                                                       ; 86b6: 9d c6 0f    ...            ; Store CR terminator at end of string
    lda #&c5                                                          ; 86b9: a9 c5       ..             ; Point fs_crc_lo/hi at &0E30 parse buffer
    sta fs_crc_lo                                                     ; 86bb: 85 be       ..             ; fs_crc_lo = &30
    lda #&0f                                                          ; 86bd: a9 0f       ..             ; fs_crc_hi = &0E → buffer at &0E30
    sta fs_crc_hi                                                     ; 86bf: 85 bf       ..             ; Store high byte
    lda fs_last_byte_flag                                             ; 86c1: a5 bd       ..             ; Recover function code from saved A
    bpl saveop                                                        ; 86c3: 10 7d       .}             ; A >= 0: save (&00) or attribs (&01-&06)
    cmp #&ff                                                          ; 86c5: c9 ff       ..             ; A=&FF? Only &FF is valid for load
    beq loadop                                                        ; 86c7: f0 03       ..             ; A=&FF: branch to load path
    jmp restore_args_return                                           ; 86c9: 4c 2d 89    L-.            ; Unknown negative code: no-op return

; &86cc referenced 1 time by &86c7
.loadop
    jsr copy_filename                                                 ; 86cc: 20 64 8d     d.            ; Copy parsed filename to cmd buffer
    ldy #2                                                            ; 86cf: a0 02       ..             ; Y=2: FS function code offset
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
; 
; On Entry:
;     Y: FS function code (2=load, 5=examine)
;     X: TX buffer extent
; ***************************************************************************************
; &86d1 referenced 1 time by &8d91
.send_fs_examine
    lda #&92                                                          ; 86d1: a9 92       ..             ; Port &92 = PLDATA (data transfer port)
    sta fs_cmd_urd                                                    ; 86d3: 8d 02 0f    ...            ; Overwrite URD field with data port number
    lda #&2a ; '*'                                                    ; 86d6: a9 2a       .*             ; A=&2A: error ptr for retry
    jsr prepare_cmd_clv                                               ; 86d8: 20 47 83     G.            ; Build FS header (V=1: CLV path)
    ldy #6                                                            ; 86db: a0 06       ..             ; Y=6: param block byte 6
    lda (fs_options),y                                                ; 86dd: b1 bb       ..             ; Byte 6: use file's own load address?
    bne lodfil                                                        ; 86df: d0 08       ..             ; Non-zero: use FS reply address (lodfil)
    jsr copy_load_addr_from_params                                    ; 86e1: 20 ae 87     ..            ; Zero: copy caller's load addr first
    jsr copy_reply_to_params                                          ; 86e4: 20 bb 87     ..            ; Then copy FS reply to param block
    bcc skip_lodfil                                                   ; 86e7: 90 06       ..             ; Carry clear from prepare_cmd_clv: skip lodfil
; &86e9 referenced 1 time by &86df
.lodfil
    jsr copy_reply_to_params                                          ; 86e9: 20 bb 87     ..            ; Copy FS reply addresses to param block
    jsr copy_load_addr_from_params                                    ; 86ec: 20 ae 87     ..            ; Then copy load addr from param block
; &86ef referenced 1 time by &86e7
.skip_lodfil
    ldy #4                                                            ; 86ef: a0 04       ..             ; Compute end address = load + file length
; &86f1 referenced 1 time by &86fc
.copy_load_end_addr
    lda fs_load_addr,x                                                ; 86f1: b5 b0       ..             ; Load address byte
    sta txcb_end,x                                                    ; 86f3: 95 c8       ..             ; Store as current transfer position
    adc fs_file_len,x                                                 ; 86f5: 7d 0d 0f    }..            ; Add file length byte
    sta fs_work_4,x                                                   ; 86f8: 95 b4       ..             ; Store as end position
    inx                                                               ; 86fa: e8          .              ; Next address byte
    dey                                                               ; 86fb: 88          .              ; Decrement byte counter
    bne copy_load_end_addr                                            ; 86fc: d0 f3       ..             ; Loop for all 4 address bytes
    sec                                                               ; 86fe: 38          8              ; Adjust high byte for 3-byte length overflow
    sbc fs_file_len_3                                                 ; 86ff: ed 10 0f    ...            ; Subtract 4th length byte from end addr
    sta fs_work_7                                                     ; 8702: 85 b7       ..             ; Store adjusted end address high byte
    jsr print_file_info                                               ; 8704: 20 01 86     ..            ; Display file info after FS reply
    jsr send_data_blocks                                              ; 8707: 20 17 87     ..            ; Transfer file data in &80-byte blocks
    ldx #2                                                            ; 870a: a2 02       ..             ; Copy 3-byte file length to FS reply cmd buffer
; &870c referenced 1 time by &8713
.floop
    lda fs_file_len_3,x                                               ; 870c: bd 10 0f    ...            ; Load file length byte
    sta fs_cmd_data,x                                                 ; 870f: 9d 05 0f    ...            ; Store in FS command data buffer
    dex                                                               ; 8712: ca          .              ; Next byte (count down)
    bpl floop                                                         ; 8713: 10 f7       ..             ; Loop for 3 bytes (X=2,1,0)
    bmi set_star_reply_port                                           ; 8715: 30 76       0v             ; ALWAYS branch

; ***************************************************************************************
; Send file data in multi-block chunks
; 
; Repeatedly sends &80-byte (128-byte) blocks of file data to the
; fileserver using command &7F. Compares current address (&C8-&CB)
; against end address (&B4-&B7) via compare_addresses, and loops
; until the entire file has been transferred. Each block is sent
; via send_to_fs_star.
; ***************************************************************************************
; &8717 referenced 2 times by &8707, &8a71
.send_data_blocks
    jsr compare_addresses                                             ; 8717: 20 cf 85     ..            ; Compare two 4-byte addresses
    beq return_lodchk                                                 ; 871a: f0 25       .%             ; Addresses match: transfer complete
    lda #&92                                                          ; 871c: a9 92       ..             ; Port &92 for data block transfer
    sta txcb_port                                                     ; 871e: 85 c1       ..             ; Store port to TXCB command byte
; &8720 referenced 1 time by &873c
.send_block_loop
    ldx #3                                                            ; 8720: a2 03       ..             ; Set up next &80-byte block for transfer
; &8722 referenced 1 time by &872b
.copy_block_addrs
    lda txcb_end,x                                                    ; 8722: b5 c8       ..             ; Swap: current addr -> source, end -> current
    sta txcb_start,x                                                  ; 8724: 95 c4       ..             ; Source addr = current position
    lda fs_work_4,x                                                   ; 8726: b5 b4       ..             ; Load end address byte
    sta txcb_end,x                                                    ; 8728: 95 c8       ..             ; Dest = end address (will be clamped)
    dex                                                               ; 872a: ca          .              ; Next address byte
    bpl copy_block_addrs                                              ; 872b: 10 f5       ..             ; Loop for all 4 bytes
    lda #&7f                                                          ; 872d: a9 7f       ..             ; Command &7F = data block transfer
    sta txcb_ctrl                                                     ; 872f: 85 c0       ..             ; Store to TXCB control byte
    jsr send_to_fs_star                                               ; 8731: 20 49 84     I.            ; Send this block to the fileserver
    ldy #3                                                            ; 8734: a0 03       ..             ; Y=3: compare 4 bytes (3..0)
; &8736 referenced 1 time by &873f
.lodchk
    lda txcb_end,y                                                    ; 8736: b9 c8 00    ...            ; Compare current vs end address (4 bytes)
    eor fs_work_4,y                                                   ; 8739: 59 b4 00    Y..            ; XOR with end address byte
    bne send_block_loop                                               ; 873c: d0 e2       ..             ; Not equal: more blocks to send
    dey                                                               ; 873e: 88          .              ; Next byte
    bpl lodchk                                                        ; 873f: 10 f5       ..             ; Loop for all 4 address bytes
; &8741 referenced 1 time by &871a
.return_lodchk
    rts                                                               ; 8741: 60          `              ; All equal: transfer complete

; &8742 referenced 1 time by &86c3
.saveop
    beq filev_save                                                    ; 8742: f0 03       ..             ; A=0: SAVE handler
    jmp filev_attrib_dispatch                                         ; 8744: 4c 45 88    LE.            ; A!=0: attribute dispatch (A=1-6)

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
; &8747 referenced 1 time by &8742
.filev_save
    ldx #4                                                            ; 8747: a2 04       ..             ; Process 4 address bytes (load/exec/start/end)
    ldy #&0e                                                          ; 8749: a0 0e       ..             ; Y=&0E: start from end-address in param block
; &874b referenced 1 time by &8765
.savsiz
    lda (fs_options),y                                                ; 874b: b1 bb       ..             ; Read end-address byte from param block
    sta port_ws_offset,y                                              ; 874d: 99 a6 00    ...            ; Save to port workspace for transfer setup
    jsr sub_4_from_y                                                  ; 8750: 20 ab 84     ..            ; Y = Y-4: point to start-address byte
    sbc (fs_options),y                                                ; 8753: f1 bb       ..             ; end - start = transfer length byte
    sta fs_cmd_csd,y                                                  ; 8755: 99 03 0f    ...            ; Store length byte in FS command buffer
    pha                                                               ; 8758: 48          H              ; Save length byte for param block restore
    lda (fs_options),y                                                ; 8759: b1 bb       ..             ; Read corresponding start-address byte
    sta port_ws_offset,y                                              ; 875b: 99 a6 00    ...            ; Save to port workspace
    pla                                                               ; 875e: 68          h              ; Restore length byte from stack
    sta (fs_options),y                                                ; 875f: 91 bb       ..             ; Replace param block entry with length
    jsr add_5_to_y                                                    ; 8761: 20 a5 84     ..            ; Y = Y+5: advance to next address group
    dex                                                               ; 8764: ca          .              ; Decrement address byte counter
    bne savsiz                                                        ; 8765: d0 e4       ..             ; Loop for all 4 address bytes
    ldy #9                                                            ; 8767: a0 09       ..             ; Copy load/exec addresses to FS command buffer
; &8769 referenced 1 time by &876f
.copy_save_params
    lda (fs_options),y                                                ; 8769: b1 bb       ..             ; Read load/exec address byte from params
    sta fs_cmd_csd,y                                                  ; 876b: 99 03 0f    ...            ; Copy to FS command buffer
    dey                                                               ; 876e: 88          .              ; Next byte (descending)
    bne copy_save_params                                              ; 876f: d0 f8       ..             ; Loop for bytes 9..1
    lda #&91                                                          ; 8771: a9 91       ..             ; Port &91 for save command
    sta fs_cmd_urd                                                    ; 8773: 8d 02 0f    ...            ; Overwrite URD field with port number
    sta fs_error_ptr                                                  ; 8776: 85 b8       ..             ; Save port &91 for flow control ACK
    ldx #&0b                                                          ; 8778: a2 0b       ..             ; Append filename at offset &0B in cmd buffer
    jsr copy_string_to_cmd                                            ; 877a: 20 66 8d     f.            ; Append filename to cmd buffer at offset X
    ldy #1                                                            ; 877d: a0 01       ..             ; Y=1: function code for save
    lda #&14                                                          ; 877f: a9 14       ..             ; A=&14: FS function code for SAVE
    jsr prepare_cmd_clv                                               ; 8781: 20 47 83     G.            ; Build header and send FS save command
    jsr print_file_info                                               ; 8784: 20 01 86     ..            ; Display filename being saved
.save_csd_display
    lda fs_cmd_data                                                   ; 8787: ad 05 0f    ...            ; Load CSD from FS reply
    jsr transfer_file_blocks                                          ; 878a: 20 c9 87     ..            ; Transfer file data blocks to server
; &878d referenced 1 time by &8715
.set_star_reply_port
    lda #&2a ; '*'                                                    ; 878d: a9 2a       .*             ; A=&2A: error ptr for FS retry
    sta fs_error_ptr                                                  ; 878f: 85 b8       ..             ; Store error ptr for TX poll
.send_fs_reply
    jsr send_fs_reply_cmd                                             ; 8791: 20 81 83     ..            ; Send FS reply acknowledgement
.skip_catalogue_msg
    stx fs_reply_cmd                                                  ; 8794: 8e 08 0f    ...            ; Store reply command for attr decode
    ldy #&0e                                                          ; 8797: a0 0e       ..             ; Y=&0E: access byte offset in param block
    lda fs_cmd_data                                                   ; 8799: ad 05 0f    ...            ; Load access byte from FS reply
    jsr decode_attribs_5bit                                           ; 879c: 20 1e 85     ..            ; Convert FS access to BBC attribute format
    beq direct_attr_copy                                              ; 879f: f0 03       ..             ; Z=1: first byte, use A directly
; &87a1 referenced 1 time by &87a9
.copy_attr_loop
    lda fs_reply_data,y                                               ; 87a1: b9 f7 0e    ...            ; Load attribute byte from FS reply
; &87a4 referenced 1 time by &879f
.direct_attr_copy
    sta (fs_options),y                                                ; 87a4: 91 bb       ..             ; Store decoded access in param block
    iny                                                               ; 87a6: c8          .              ; Next attribute byte
    cpy #&12                                                          ; 87a7: c0 12       ..             ; Copied all 4 bytes? (Y=&0E..&11)
    bne copy_attr_loop                                                ; 87a9: d0 f6       ..             ; Loop for 4 attribute bytes
    jmp restore_args_return                                           ; 87ab: 4c 2d 89    L-.            ; Restore A/X/Y and return to caller

; ***************************************************************************************
; Copy load address from parameter block
; 
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to &AE-&B3 (local workspace).
; ***************************************************************************************
; &87ae referenced 2 times by &86e1, &86ec
.copy_load_addr_from_params
    ldy #5                                                            ; 87ae: a0 05       ..             ; Start at offset 5 (top of 4-byte addr)
; &87b0 referenced 1 time by &87b8
.lodrl1
    lda (fs_options),y                                                ; 87b0: b1 bb       ..             ; Read from parameter block
    sta work_ae,y                                                     ; 87b2: 99 ae 00    ...            ; Store to local workspace
    dey                                                               ; 87b5: 88          .              ; Next byte (descending)
    cpy #2                                                            ; 87b6: c0 02       ..             ; Copy offsets 5,4,3,2 (4 bytes)
    bcs lodrl1                                                        ; 87b8: b0 f6       ..             ; Loop while Y >= 2
    rts                                                               ; 87ba: 60          `              ; Return

; ***************************************************************************************
; Copy FS reply data to parameter block
; 
; Copies bytes from the FS command reply buffer (&0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; 
; On Entry:
;     X: attribute byte (stored first at offset &0D)
; ***************************************************************************************
; &87bb referenced 2 times by &86e4, &86e9
.copy_reply_to_params
    ldy #&0d                                                          ; 87bb: a0 0d       ..             ; Start at offset &0D (top of range)
    txa                                                               ; 87bd: 8a          .              ; First store uses X (attrib byte)
; &87be referenced 1 time by &87c6
.lodrl2
    sta (fs_options),y                                                ; 87be: 91 bb       ..             ; Write to parameter block
    lda fs_cmd_urd,y                                                  ; 87c0: b9 02 0f    ...            ; Read next byte from reply buffer
    dey                                                               ; 87c3: 88          .              ; Next byte (descending)
    cpy #2                                                            ; 87c4: c0 02       ..             ; Copy offsets &0D down to 2
    bcs lodrl2                                                        ; 87c6: b0 f6       ..             ; Loop until offset 2 reached
    rts                                                               ; 87c8: 60          `              ; Return to caller

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
; &87c9 referenced 2 times by &878a, &8a6c
.transfer_file_blocks
    pha                                                               ; 87c9: 48          H              ; Save FS command byte on stack
    jsr compare_addresses                                             ; 87ca: 20 cf 85     ..            ; Compare two 4-byte addresses
    beq restore_ay_return                                             ; 87cd: f0 72       .r             ; Addresses equal: nothing to transfer
; &87cf referenced 1 time by &881e
.next_block
    ldx #0                                                            ; 87cf: a2 00       ..             ; X=0: clear hi bytes of block size
    ldy #4                                                            ; 87d1: a0 04       ..             ; Y=4: process 4 address bytes
    stx fs_reply_cmd                                                  ; 87d3: 8e 08 0f    ...            ; Clear block size hi byte 1
    stx fs_load_vector                                                ; 87d6: 8e 09 0f    ...            ; Clear block size hi byte 2
    clc                                                               ; 87d9: 18          .              ; CLC for ADC in loop
; &87da referenced 1 time by &87e7
.block_addr_loop
    lda fs_load_addr,x                                                ; 87da: b5 b0       ..             ; Source = current position
    sta txcb_start,x                                                  ; 87dc: 95 c4       ..             ; Store source address byte
    adc fs_func_code,x                                                ; 87de: 7d 06 0f    }..            ; Add block size to current position
    sta txcb_end,x                                                    ; 87e1: 95 c8       ..             ; Store dest address byte
    sta fs_load_addr,x                                                ; 87e3: 95 b0       ..             ; Advance current position
    inx                                                               ; 87e5: e8          .              ; Next address byte
    dey                                                               ; 87e6: 88          .              ; Decrement byte counter
    bne block_addr_loop                                               ; 87e7: d0 f1       ..             ; Loop for all 4 bytes
    bcs clamp_dest_setup                                              ; 87e9: b0 0d       ..             ; Carry: address overflowed, clamp
    sec                                                               ; 87eb: 38          8              ; SEC for SBC in overshoot check
; &87ec referenced 1 time by &87f4
.savchk
    lda fs_load_addr,y                                                ; 87ec: b9 b0 00    ...            ; Check if new pos overshot end addr
    sbc fs_work_4,y                                                   ; 87ef: f9 b4 00    ...            ; Subtract end address byte
    iny                                                               ; 87f2: c8          .              ; Next byte
    dex                                                               ; 87f3: ca          .              ; Decrement counter
    bne savchk                                                        ; 87f4: d0 f6       ..             ; Loop for 4-byte comparison
    bcc send_block                                                    ; 87f6: 90 09       ..             ; C=0: no overshoot, proceed
; &87f8 referenced 1 time by &87e9
.clamp_dest_setup
    ldx #3                                                            ; 87f8: a2 03       ..             ; Overshot: clamp dest to end address
; &87fa referenced 1 time by &87ff
.clamp_dest_addr
    lda fs_work_4,x                                                   ; 87fa: b5 b4       ..             ; Load end address byte
    sta txcb_end,x                                                    ; 87fc: 95 c8       ..             ; Replace dest with end address
    dex                                                               ; 87fe: ca          .              ; Next byte
    bpl clamp_dest_addr                                               ; 87ff: 10 f9       ..             ; Loop for all 4 bytes
; &8801 referenced 1 time by &87f6
.send_block
    pla                                                               ; 8801: 68          h              ; Recover original FS command byte
    pha                                                               ; 8802: 48          H              ; Re-push for next iteration
    php                                                               ; 8803: 08          .              ; Save processor flags (C from cmp)
    sta txcb_port                                                     ; 8804: 85 c1       ..             ; Store command byte in TXCB
    lda #&80                                                          ; 8806: a9 80       ..             ; 128-byte block size for data transfer
    sta txcb_ctrl                                                     ; 8808: 85 c0       ..             ; Store size in TXCB control byte
    jsr setup_tx_ptr_c0                                               ; 880a: 20 45 86     E.            ; Point TX ptr to &00C0; transmit
    lda fs_error_ptr                                                  ; 880d: a5 b8       ..             ; ACK port for flow control
    jsr init_tx_ctrl_port                                             ; 880f: 20 11 83     ..            ; Set reply port for ACK receive
    plp                                                               ; 8812: 28          (              ; Restore flags (C=overshoot status)
    bcs restore_ay_return                                             ; 8813: b0 2c       .,             ; C=1: all data sent (overshot), done
    lda #&91                                                          ; 8815: a9 91       ..             ; Command &91 = data block transfer
    sta txcb_port                                                     ; 8817: 85 c1       ..             ; Store command &91 in TXCB
    lda #&2a ; '*'                                                    ; 8819: a9 2a       .*             ; A=&2A: error ptr for retry
    jsr send_to_fs                                                    ; 881b: 20 4b 84     K.            ; Transmit block and wait (BRIANX)
    bne next_block                                                    ; 881e: d0 af       ..             ; More blocks? Loop back
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
; 
; On Entry:
;     X: file handle to check
; 
; On Exit:
;     X: &FF if at EOF, &00 if not
; ***************************************************************************************
.fscv_1_eof
    pha                                                               ; 8820: 48          H              ; Save A (function code)
    sty fs_block_offset                                               ; 8821: 84 bc       ..             ; Save handle for EOF check
    jsr handle_to_mask_clc                                            ; 8823: 20 8a 85     ..            ; Convert handle to bitmask in A
    tya                                                               ; 8826: 98          .              ; Y = handle bitmask from conversion
    and fs_eof_flags                                                  ; 8827: 2d 07 0e    -..            ; Local hint: is EOF possible for this handle?
    tax                                                               ; 882a: aa          .              ; X = result of AND (0 = not at EOF)
    beq restore_ay_return                                             ; 882b: f0 14       ..             ; Hint clear: definitely not at EOF
    pha                                                               ; 882d: 48          H              ; Save bitmask for clear_fs_flag
    sty fs_cmd_data                                                   ; 882e: 8c 05 0f    ...            ; Handle byte in FS command buffer
    ldy #&11                                                          ; 8831: a0 11       ..             ; Y=&11: FS function code FCEOF; Y=function code for HDRFN
    ldx #1                                                            ; 8833: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8835: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    pla                                                               ; 8838: 68          h              ; Restore bitmask
    ldx fs_cmd_data                                                   ; 8839: ae 05 0f    ...            ; FS reply: non-zero = at EOF
    bne restore_ay_return                                             ; 883c: d0 03       ..             ; At EOF: skip flag clear
    jsr clear_fs_flag                                                 ; 883e: 20 e0 85     ..            ; Not at EOF: clear the hint bit
; &8841 referenced 4 times by &87cd, &8813, &882b, &883c
.restore_ay_return
    pla                                                               ; 8841: 68          h              ; Restore A
    ldy fs_block_offset                                               ; 8842: a4 bc       ..             ; Restore Y
    rts                                                               ; 8844: 60          `              ; Return; X=0 (not EOF) or X=&FF (EOF)

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
; 
; On Entry:
;     A: function code (1-6)
; 
; On Exit:
;     A: object type (A=5 read info) or restored
; ***************************************************************************************
; &8845 referenced 1 time by &8744
.filev_attrib_dispatch
    sta fs_cmd_data                                                   ; 8845: 8d 05 0f    ...            ; Store function code in FS cmd buffer
    cmp #6                                                            ; 8848: c9 06       ..             ; A=6? (delete)
    beq cha6                                                          ; 884a: f0 3f       .?             ; Yes: jump to delete handler
    bcs check_attrib_result                                           ; 884c: b0 48       .H             ; A>=7: unsupported, fall through to return
    cmp #5                                                            ; 884e: c9 05       ..             ; A=5? (read catalogue info)
    beq cha5                                                          ; 8850: f0 52       .R             ; Yes: jump to read info handler
    cmp #4                                                            ; 8852: c9 04       ..             ; A=4? (write attributes only)
    beq cha4                                                          ; 8854: f0 44       .D             ; Yes: jump to write attrs handler
    cmp #1                                                            ; 8856: c9 01       ..             ; A=1? (write all catalogue info)
    beq get_file_protection                                           ; 8858: f0 15       ..             ; Yes: jump to write-all handler
    asl a                                                             ; 885a: 0a          .              ; A=2 or 3: convert to param block offset
    asl a                                                             ; 885b: 0a          .              ; A*4: 2->8, 3->12
    tay                                                               ; 885c: a8          .              ; Y = A*4
    jsr sub_3_from_y                                                  ; 885d: 20 ac 84     ..            ; Y = A*4 - 3 (load addr offset for A=2)
    ldx #3                                                            ; 8860: a2 03       ..             ; X=3: copy 4 bytes
; &8862 referenced 1 time by &8869
.chalp1
    lda (fs_options),y                                                ; 8862: b1 bb       ..             ; Load address byte from param block
    sta fs_func_code,x                                                ; 8864: 9d 06 0f    ...            ; Store to FS cmd data area
    dey                                                               ; 8867: 88          .              ; Next source byte (descending)
    dex                                                               ; 8868: ca          .              ; Next dest byte
    bpl chalp1                                                        ; 8869: 10 f7       ..             ; Loop for 4 bytes
    ldx #5                                                            ; 886b: a2 05       ..             ; X=5: data extent for filename copy
    bne copy_filename_to_cmd                                          ; 886d: d0 15       ..             ; ALWAYS branch

; &886f referenced 1 time by &8858
.get_file_protection
    jsr decode_attribs_6bit                                           ; 886f: 20 14 85     ..            ; A=1: encode protection from param block
    sta fs_file_attrs                                                 ; 8872: 8d 0e 0f    ...            ; Store encoded attrs at &0F0E
    ldy #9                                                            ; 8875: a0 09       ..             ; Y=9: source offset in param block
    ldx #8                                                            ; 8877: a2 08       ..             ; X=8: dest offset in cmd buffer
; &8879 referenced 1 time by &8880
.chalp2
    lda (fs_options),y                                                ; 8879: b1 bb       ..             ; Load byte from param block
    sta fs_cmd_data,x                                                 ; 887b: 9d 05 0f    ...            ; Store to FS cmd buffer
    dey                                                               ; 887e: 88          .              ; Next source byte (descending)
    dex                                                               ; 887f: ca          .              ; Next dest byte
    bne chalp2                                                        ; 8880: d0 f7       ..             ; Loop until X=0 (8 bytes copied)
    ldx #&0a                                                          ; 8882: a2 0a       ..             ; X=&0A: data extent past attrs+addrs
; &8884 referenced 2 times by &886d, &88a2
.copy_filename_to_cmd
    jsr copy_string_to_cmd                                            ; 8884: 20 66 8d     f.            ; Append filename to cmd buffer
    ldy #&13                                                          ; 8887: a0 13       ..             ; Y=&13: fn code for FCSAVE (write attrs)
    bne send_fs_cmd_v1                                                ; 8889: d0 05       ..             ; ALWAYS branch to send command; ALWAYS branch

; &888b referenced 1 time by &884a
.cha6
    jsr copy_filename                                                 ; 888b: 20 64 8d     d.            ; A=6: copy filename (delete)
    ldy #&14                                                          ; 888e: a0 14       ..             ; Y=&14: fn code for FCDEL (delete)
; &8890 referenced 1 time by &8889
.send_fs_cmd_v1
    bit tx_ctrl_upper                                                 ; 8890: 2c 3b 83    ,;.            ; Set V=1 (BIT trick: &B3 has bit 6 set)
    jsr prepare_fs_cmd_v                                              ; 8893: 20 52 83     R.            ; Send via prepare_fs_cmd_v (V=1 path)
; &8896 referenced 1 time by &884c
.check_attrib_result
    bcs attrib_error_exit                                             ; 8896: b0 48       .H             ; C=1: &D6 not-found, skip to return
    bcc argsv_check_return                                            ; 8898: 90 77       .w             ; C=0: success, copy reply to param block; ALWAYS branch

; &889a referenced 1 time by &8854
.cha4
    jsr decode_attribs_6bit                                           ; 889a: 20 14 85     ..            ; A=4: encode attrs from param block
    sta fs_func_code                                                  ; 889d: 8d 06 0f    ...            ; Store encoded attrs at &0F06
    ldx #2                                                            ; 88a0: a2 02       ..             ; X=2: data extent (1 attr byte + fn)
    bne copy_filename_to_cmd                                          ; 88a2: d0 e0       ..             ; ALWAYS branch to append filename; ALWAYS branch

; &88a4 referenced 1 time by &8850
.cha5
    ldx #1                                                            ; 88a4: a2 01       ..             ; X=1: filename only, no data extent
    jsr copy_string_to_cmd                                            ; 88a6: 20 66 8d     f.            ; Copy filename to cmd buffer
    ldy #&12                                                          ; 88a9: a0 12       ..             ; Y=&12: fn code for FCEXAM (read info); Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 88ab: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    lda fs_obj_type                                                   ; 88ae: ad 11 0f    ...            ; Save object type from FS reply
    stx fs_obj_type                                                   ; 88b1: 8e 11 0f    ...            ; Clear reply byte (X=0 on success); X=0 on success, &D6 on not-found
    stx fs_len_clear                                                  ; 88b4: 8e 14 0f    ...            ; Clear length high byte in reply
    jsr decode_attribs_5bit                                           ; 88b7: 20 1e 85     ..            ; Decode 5-bit access byte from FS reply
    ldx fs_cmd_data                                                   ; 88ba: ae 05 0f    ...            ; Load FS command code from reply
    beq argsv_zero_length                                             ; 88bd: f0 20       .              ; Zero: no attribute data returned
    ldy #&0e                                                          ; 88bf: a0 0e       ..             ; Y=&0E: attrs offset in param block
    sta (fs_options),y                                                ; 88c1: 91 bb       ..             ; Store decoded attrs at param block +&0E
    dey                                                               ; 88c3: 88          .              ; Y=&0D: start copy below attrs; Y=&0d
    ldx #&0c                                                          ; 88c4: a2 0c       ..             ; X=&0C: copy from reply offset &0C down
; &88c6 referenced 1 time by &88cd
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 88c6: bd 05 0f    ...            ; Load reply byte (load/exec/length)
    sta (fs_options),y                                                ; 88c9: 91 bb       ..             ; Store to param block
    dey                                                               ; 88cb: 88          .              ; Next dest byte (descending)
    dex                                                               ; 88cc: ca          .              ; Next source byte
    bne copy_fs_reply_to_cb                                           ; 88cd: d0 f7       ..             ; Loop until X=0 (12 bytes copied)
    inx                                                               ; 88cf: e8          .              ; X=0 -> X=2 for length high copy
    inx                                                               ; 88d0: e8          .              ; INX again: X=2
    ldy #&11                                                          ; 88d1: a0 11       ..             ; Y=&11: length high dest in param block
; &88d3 referenced 1 time by &88da
.cha5lp
    lda fs_access_level,x                                             ; 88d3: bd 12 0f    ...            ; Load length high byte from reply
    sta (fs_options),y                                                ; 88d6: 91 bb       ..             ; Store to param block
    dey                                                               ; 88d8: 88          .              ; Next dest byte (descending)
    dex                                                               ; 88d9: ca          .              ; Next source byte
    bpl cha5lp                                                        ; 88da: 10 f7       ..             ; Loop for 3 length-high bytes
    ldx fs_cmd_data                                                   ; 88dc: ae 05 0f    ...            ; Reload FS command code
; &88df referenced 1 time by &88bd
.argsv_zero_length
    txa                                                               ; 88df: 8a          .              ; A = command code for exit test
; &88e0 referenced 1 time by &8896
.attrib_error_exit
    bpl restore_xy_return                                             ; 88e0: 10 4d       .M             ; A>=0: branch to restore_args_return
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
    jsr save_fscv_args                                                ; 88e2: 20 09 85     ..            ; Save A/X/Y registers for later restore
    cmp #3                                                            ; 88e5: c9 03       ..             ; Function >= 3?
    bcs restore_args_return                                           ; 88e7: b0 44       .D             ; A>=3 (ensure/flush): no-op for NFS
    cpy #0                                                            ; 88e9: c0 00       ..             ; Test file handle
    beq argsv_dispatch_a                                              ; 88eb: f0 47       .G             ; Y=0: FS-level query, not per-file
    jsr handle_to_mask_clc                                            ; 88ed: 20 8a 85     ..            ; Convert handle to bitmask
    sty fs_cmd_data                                                   ; 88f0: 8c 05 0f    ...            ; Store bitmask as first cmd data byte
    lsr a                                                             ; 88f3: 4a          J              ; LSR splits A: C=1 means write (A=1)
    sta fs_func_code                                                  ; 88f4: 8d 06 0f    ...            ; Store function code to cmd data byte 2
    bcs save_args_handle                                              ; 88f7: b0 1a       ..             ; C=1: write path, copy ptr from caller
    ldy #&0c                                                          ; 88f9: a0 0c       ..             ; Y=&0C: FCRDSE (read sequential pointer); Y=function code for HDRFN
    ldx #2                                                            ; 88fb: a2 02       ..             ; X=2: 3 data bytes in command; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 88fd: 20 51 83     Q.            ; Build and send FS command; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 8900: 85 bd       ..             ; Clear last-byte flag on success; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 8902: a6 bb       ..             ; X = saved control block ptr low
    ldy #2                                                            ; 8904: a0 02       ..             ; Y=2: copy 3 bytes of file pointer
    sta zp_work_3,x                                                   ; 8906: 95 03       ..             ; Zero high byte of 3-byte pointer
; &8908 referenced 1 time by &890f
.copy_fileptr_reply
    lda fs_cmd_data,y                                                 ; 8908: b9 05 0f    ...            ; Read reply byte from FS cmd data
    sta zp_work_2,x                                                   ; 890b: 95 02       ..             ; Store to caller's control block
    dex                                                               ; 890d: ca          .              ; Next byte (descending)
    dey                                                               ; 890e: 88          .              ; Next source byte
    bpl copy_fileptr_reply                                            ; 890f: 10 f7       ..             ; Loop for all 3 bytes
; &8911 referenced 1 time by &8898
.argsv_check_return
    bcc restore_args_return                                           ; 8911: 90 1a       ..             ; C=0 (read): return to caller
; &8913 referenced 1 time by &88f7
.save_args_handle
    tya                                                               ; 8913: 98          .              ; Save bitmask for set_fs_flag later
    pha                                                               ; 8914: 48          H              ; Push bitmask
    ldy #3                                                            ; 8915: a0 03       ..             ; Y=3: copy 4 bytes of file pointer
; &8917 referenced 1 time by &891e
.copy_fileptr_to_cmd
    lda zp_work_3,x                                                   ; 8917: b5 03       ..             ; Read caller's pointer byte
    sta fs_data_count,y                                               ; 8919: 99 07 0f    ...            ; Store to FS command data area
    dex                                                               ; 891c: ca          .              ; Next source byte
    dey                                                               ; 891d: 88          .              ; Next destination byte
    bpl copy_fileptr_to_cmd                                           ; 891e: 10 f7       ..             ; Loop for all 4 bytes
    ldy #&0d                                                          ; 8920: a0 0d       ..             ; Y=&0D: FCWRSE (write sequential pointer); Y=function code for HDRFN
    ldx #5                                                            ; 8922: a2 05       ..             ; X=5: 6 data bytes in command; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8924: 20 51 83     Q.            ; Build and send FS command; Prepare FS command buffer (12 references)
    stx fs_last_byte_flag                                             ; 8927: 86 bd       ..             ; Save not-found status from X; X=0 on success, &D6 on not-found
    pla                                                               ; 8929: 68          h              ; Recover bitmask for EOF hint update
    jsr set_fs_flag                                                   ; 892a: 20 e5 85     ..            ; Set EOF hint bit for this handle
; ***************************************************************************************
; Restore arguments and return
; 
; Common exit point for FS vector handlers. Reloads A from
; fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
; fs_block_offset (&BC) — the values saved at entry by
; save_fscv_args — and returns to the caller.
; ***************************************************************************************
; &892d referenced 8 times by &86c9, &87ab, &88e7, &8911, &893c, &89a0, &89f6, &8d00
.restore_args_return
    lda fs_last_byte_flag                                             ; 892d: a5 bd       ..             ; A = saved function code / command
; &892f referenced 5 times by &88e0, &8939, &8948, &8970, &8984
.restore_xy_return
    ldx fs_options                                                    ; 892f: a6 bb       ..             ; X = saved control block ptr low
    ldy fs_block_offset                                               ; 8931: a4 bc       ..             ; Y = saved control block ptr high
    rts                                                               ; 8933: 60          `              ; Return to MOS with registers restored

; &8934 referenced 1 time by &88eb
.argsv_dispatch_a
    tay                                                               ; 8934: a8          .              ; Transfer A to Y for test
    bne halve_args_a                                                  ; 8935: d0 04       ..             ; Non-zero: halve A
    lda #5                                                            ; 8937: a9 05       ..             ; A=5: default FS number
    bne restore_xy_return                                             ; 8939: d0 f4       ..             ; ALWAYS branch

; &893b referenced 1 time by &8935
.halve_args_a
    lsr a                                                             ; 893b: 4a          J              ; Shared: halve A (A=0 or A=2 paths)
    bne restore_args_return                                           ; 893c: d0 ef       ..             ; Return with A = FS number or 1
; &893e referenced 1 time by &8944
.osarg1
    lda fs_context_hi,y                                               ; 893e: b9 0b 0e    ...            ; Copy command context to caller's block
    sta (fs_options),y                                                ; 8941: 91 bb       ..             ; Store to caller's parameter block
    dey                                                               ; 8943: 88          .              ; Next byte (descending)
    bpl osarg1                                                        ; 8944: 10 f8       ..             ; Loop until all bytes copied
; ***************************************************************************************
; Return with A=0 via register restore
; 
; Loads A=0 and branches (always taken) to the common register
; restore exit at restore_args_return. Used as a shared exit
; point by ARGSV, FINDV, and GBPBV when an operation is
; unsupported or should return zero.
; ***************************************************************************************
; &8946 referenced 3 times by &8956, &8a96, &8b33
.return_a_zero
    lda #0                                                            ; 8946: a9 00       ..             ; A=operation (0=close, &40=read, &80=write, &C0=R/W)
    bpl restore_xy_return                                             ; 8948: 10 e5       ..             ; ALWAYS branch

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
; "might be at EOF, query the server",
;     on_entry={"a": "operation (0=close, &40=read, &80=write, &C0=R/W)", "x":
; "filename pointer low (open)", "y": "file handle (close) or filename pointer high
; (open)"},
;     on_exit={"a": "handle on open, 0 on close-all, restored on close-one", "x":
; "restored", "y": "restored"})
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
    jsr save_fscv_args                                                ; 894a: 20 09 85     ..            ; Save A/X/Y and set up pointers
    sec                                                               ; 894d: 38          8              ; SEC distinguishes open (A>0) from close
    jsr handle_to_mask                                                ; 894e: 20 8b 85     ..            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 8951: aa          .              ; A=preserved
    beq close_handle                                                  ; 8952: f0 32       .2             ; A=0: close file(s)
    and #&3f ; '?'                                                    ; 8954: 29 3f       )?             ; Valid open modes: &40, &80, &C0 only
    bne return_a_zero                                                 ; 8956: d0 ee       ..             ; Invalid mode bits: return
    txa                                                               ; 8958: 8a          .              ; A = original mode byte
    eor #&80                                                          ; 8959: 49 80       I.             ; Convert MOS mode to FS protocol flags
    asl a                                                             ; 895b: 0a          .              ; ASL: shift mode bits left
    sta fs_cmd_data                                                   ; 895c: 8d 05 0f    ...            ; Flag 1: read/write direction
    rol a                                                             ; 895f: 2a          *              ; ROL: Flag 2 into bit 0
    sta fs_func_code                                                  ; 8960: 8d 06 0f    ...            ; Flag 2: create vs existing file
    ldx #2                                                            ; 8963: a2 02       ..             ; X=2: copy after 2-byte flags
    jsr copy_string_to_cmd                                            ; 8965: 20 66 8d     f.            ; Copy filename to FS command buffer
    ldy #6                                                            ; 8968: a0 06       ..             ; Y=6: FS function code FCOPEN
    bit tx_ctrl_upper                                                 ; 896a: 2c 3b 83    ,;.            ; Set V flag from l83b3 bit 6
    jsr prepare_fs_cmd_v                                              ; 896d: 20 52 83     R.            ; Build and send FS open command
    bcs restore_xy_return                                             ; 8970: b0 bd       ..             ; Error: restore and return
    lda fs_cmd_data                                                   ; 8972: ad 05 0f    ...            ; Load reply handle from FS
    tax                                                               ; 8975: aa          .              ; X = new file handle
    jsr set_fs_flag                                                   ; 8976: 20 e5 85     ..            ; Set EOF hint + sequence bits
    txa                                                               ; 8979: 8a          .              ; A = handle bitmask from set_fs_flag
    ora fs_sequence_nos                                               ; 897a: 0d 08 0e    ...            ; Merge handle into sequence tracking
    sta fs_sequence_nos                                               ; 897d: 8d 08 0e    ...            ; Store updated sequence tracking
    txa                                                               ; 8980: 8a          .              ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8981: 20 a6 85     ..            ; Convert bitmask to handle number (FS2A)
    bne restore_xy_return                                             ; 8984: d0 a9       ..             ; ALWAYS branch to restore and return
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
; 
; On Entry:
;     Y: file handle (0=close all, >0=close single)
; ***************************************************************************************
; &8986 referenced 1 time by &8952
.close_handle
    tya                                                               ; 8986: 98          .              ; A = handle (Y preserved in A); Y=preserved
    bne close_single_handle                                           ; 8987: d0 07       ..             ; Y>0: close single file
    lda #osbyte_close_spool_exec                                      ; 8989: a9 77       .w             ; Close SPOOL/EXEC before FS close-all
    jsr osbyte                                                        ; 898b: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 898e: a0 00       ..             ; Y=0: close all handles on server
; &8990 referenced 1 time by &8987
.close_single_handle
    sty fs_cmd_data                                                   ; 8990: 8c 05 0f    ...            ; Handle byte in FS command buffer
    ldx #1                                                            ; 8993: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 8995: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8997: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 899a: ad 05 0f    ...            ; Reply handle for flag update
    jsr set_fs_flag                                                   ; 899d: 20 e5 85     ..            ; Update EOF/sequence tracking bits
; &89a0 referenced 1 time by &89c9
.close_opt_return
    bcc restore_args_return                                           ; 89a0: 90 8b       ..             ; C=0: restore A/X/Y and return
; ***************************************************************************************
; FSCV 0: *OPT handler (OPTION)
; 
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
; Other combinations generate error &CB (OPTER: "bad option").
; 
; On Entry:
;     X: option number (1 or 4)
;     Y: option value
; ***************************************************************************************
.fscv_0_opt
    cpx #4                                                            ; 89a2: e0 04       ..             ; Is it *OPT 4,Y?
    bne gbpbv_func_dispatch                                           ; 89a4: d0 04       ..             ; No: check for *OPT 1
    cpy #4                                                            ; 89a6: c0 04       ..             ; Y must be 0-3 for boot option
    bcc optl1                                                         ; 89a8: 90 12       ..             ; Y < 4: valid boot option
; &89aa referenced 1 time by &89a4
.gbpbv_func_dispatch
    cpx #1                                                            ; 89aa: e0 01       ..             ; X=1? (*OPT 1: set messaging)
    bne opter1                                                        ; 89ac: d0 09       ..             ; Not *OPT 1: bad option error
    cpy #2                                                            ; 89ae: c0 02       ..             ; Y < 2? (valid: 0=off, 1=on)
    bcs opter1                                                        ; 89b0: b0 05       ..             ; Y >= 2: bad option value error
.set_messages_flag
    sty fs_messages_flag                                              ; 89b2: 8c 06 0e    ...            ; Set local messages flag (*OPT 1,Y)
    bcc opt_return                                                    ; 89b5: 90 12       ..             ; Return via restore_args_return
; &89b7 referenced 2 times by &89ac, &89b0
.opter1
    lda #7                                                            ; 89b7: a9 07       ..             ; Error index 7 (Bad option)
    jmp nlisne                                                        ; 89b9: 4c 2b 84    L+.            ; Generate BRK error

; &89bc referenced 1 time by &89a8
.optl1
    sty fs_cmd_data                                                   ; 89bc: 8c 05 0f    ...            ; Boot option value in FS command
    ldy #&16                                                          ; 89bf: a0 16       ..             ; Y=&16: FS function code FCOPT; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89c1: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 89c4: a4 bc       ..             ; Restore Y from saved value
    sty fs_boot_option                                                ; 89c6: 8c 05 0e    ...            ; Cache boot option locally
; &89c9 referenced 1 time by &89b5
.opt_return
    bcc close_opt_return                                              ; 89c9: 90 d5       ..             ; Return via restore_args_return
; &89cb referenced 1 time by &8a8a
.adjust_addrs_9
    ldy #9                                                            ; 89cb: a0 09       ..             ; Y=9: adjust 9 address bytes
    jsr adjust_addrs_clc                                              ; 89cd: 20 d2 89     ..            ; Adjust with carry clear
; &89d0 referenced 1 time by &8b7a
.adjust_addrs_1
    ldy #1                                                            ; 89d0: a0 01       ..             ; Y=1: adjust 1 address byte
; &89d2 referenced 1 time by &89cd
.adjust_addrs_clc
    clc                                                               ; 89d2: 18          .              ; C=0 for address adjustment
; ***************************************************************************************
; Bidirectional 4-byte address adjustment
; 
; Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
;   If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
;   If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
; Starting offset X=&FC means it reads from &0E06-&0E09 area.
; Used to convert between absolute and relative file positions.
; 
; On Entry:
;     Y: starting offset into (fs_options) parameter block
; 
; On Exit:
;     A: corrupted (last adjusted byte)
;     X: 0
;     Y: entry Y + 4
; ***************************************************************************************
; &89d3 referenced 2 times by &8a90, &8b86
.adjust_addrs
    ldx #&fc                                                          ; 89d3: a2 fc       ..             ; X=&FC: index into &0E06 area (wraps to 0)
; &89d5 referenced 1 time by &89e8
.adjust_addr_byte
    lda (fs_options),y                                                ; 89d5: b1 bb       ..             ; Load byte from param block
    bit fs_load_addr_2                                                ; 89d7: 24 b2       $.             ; Test sign of adjustment direction
    bmi subtract_adjust                                               ; 89d9: 30 06       0.             ; Negative: subtract instead
    adc fs_cmd_context,x                                              ; 89db: 7d 0a 0e    }..            ; Add adjustment value
    jmp gbpbx                                                         ; 89de: 4c e4 89    L..            ; Skip to store result

; &89e1 referenced 1 time by &89d9
.subtract_adjust
    sbc fs_cmd_context,x                                              ; 89e1: fd 0a 0e    ...            ; Subtract adjustment value
; &89e4 referenced 1 time by &89de
.gbpbx
    sta (fs_options),y                                                ; 89e4: 91 bb       ..             ; Store adjusted byte back
    iny                                                               ; 89e6: c8          .              ; Next param block byte
    inx                                                               ; 89e7: e8          .              ; Next adjustment byte (X wraps &FC->&00)
    bne adjust_addr_byte                                              ; 89e8: d0 eb       ..             ; Loop 4 times (X=&FC,&FD,&FE,&FF,done)
    rts                                                               ; 89ea: 60          `              ; Return (unsupported function)

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
    jsr save_fscv_args                                                ; 89eb: 20 09 85     ..            ; Save A/X/Y to FS workspace
    tax                                                               ; 89ee: aa          .              ; X = call number for range check
    beq gbpbx0                                                        ; 89ef: f0 05       ..             ; A=0: invalid, restore and return
    dex                                                               ; 89f1: ca          .              ; Convert to 0-based (A=0..7)
    cpx #8                                                            ; 89f2: e0 08       ..             ; Range check: must be 0-7
    bcc gbpbx1                                                        ; 89f4: 90 03       ..             ; In range: continue to handler
; &89f6 referenced 1 time by &89ef
.gbpbx0
    jmp restore_args_return                                           ; 89f6: 4c 2d 89    L-.            ; Out of range: restore args and return

; &89f9 referenced 1 time by &89f4
.gbpbx1
    txa                                                               ; 89f9: 8a          .              ; Recover 0-based function code
    ldy #0                                                            ; 89fa: a0 00       ..             ; Y=0: param block byte 0 (file handle)
    pha                                                               ; 89fc: 48          H              ; Save function code on stack
    cmp #4                                                            ; 89fd: c9 04       ..             ; A>=4: info queries, dispatch separately
    bcc gbpbe1                                                        ; 89ff: 90 03       ..             ; A<4: file read/write operations
    jmp osgbpb_info                                                   ; 8a01: 4c ae 8a    L..            ; Dispatch to OSGBPB 5-8 info handler

; &8a04 referenced 1 time by &89ff
.gbpbe1
    lda (fs_options),y                                                ; 8a04: b1 bb       ..             ; Get file handle from param block byte 0
    jsr handle_to_mask_a                                              ; 8a06: 20 89 85     ..            ; Convert handle to bitmask for EOF flags
    sty fs_cmd_data                                                   ; 8a09: 8c 05 0f    ...            ; Store handle in FS command data
    ldy #&0b                                                          ; 8a0c: a0 0b       ..             ; Y=&0B: start at param block byte 11
    ldx #6                                                            ; 8a0e: a2 06       ..             ; X=6: copy 6 bytes of transfer params
; &8a10 referenced 1 time by &8a1c
.gbpbf1
    lda (fs_options),y                                                ; 8a10: b1 bb       ..             ; Load param block byte
    sta fs_func_code,x                                                ; 8a12: 9d 06 0f    ...            ; Store to FS command buffer at &0F06+X
    dey                                                               ; 8a15: 88          .              ; Previous param block byte
    cpy #8                                                            ; 8a16: c0 08       ..             ; Skip param block offset 8 (the handle)
    bne gbpbf2                                                        ; 8a18: d0 01       ..             ; Not at handle offset: continue
    dey                                                               ; 8a1a: 88          .              ; Extra DEY to skip handle byte
; &8a1b referenced 1 time by &8a18
.gbpbf2
    dex                                                               ; 8a1b: ca          .              ; Decrement copy counter
    bne gbpbf1                                                        ; 8a1c: d0 f2       ..             ; Loop for all 6 bytes
    pla                                                               ; 8a1e: 68          h              ; Recover function code from stack
    lsr a                                                             ; 8a1f: 4a          J              ; LSR: odd=read (C=1), even=write (C=0)
    pha                                                               ; 8a20: 48          H              ; Save function code again (need C later)
    bcc gbpbl1                                                        ; 8a21: 90 01       ..             ; Even (write): X stays 0
    inx                                                               ; 8a23: e8          .              ; Odd (read): X=1
; &8a24 referenced 1 time by &8a21
.gbpbl1
    stx fs_func_code                                                  ; 8a24: 8e 06 0f    ...            ; Store FS direction flag
    ldy #&0b                                                          ; 8a27: a0 0b       ..             ; Y=&0B: command data extent
    ldx #&91                                                          ; 8a29: a2 91       ..             ; Command &91=put, &92=get
    pla                                                               ; 8a2b: 68          h              ; Recover function code
    pha                                                               ; 8a2c: 48          H              ; Save again for later direction check
    beq gbpb_write_path                                               ; 8a2d: f0 03       ..             ; Even (write): keep &91 and Y=&0B
    ldx #&92                                                          ; 8a2f: a2 92       ..             ; Odd (read): use &92 (get) instead
    dey                                                               ; 8a31: 88          .              ; Read: one fewer data byte in command; Y=&0a
; &8a32 referenced 1 time by &8a2d
.gbpb_write_path
    stx fs_cmd_urd                                                    ; 8a32: 8e 02 0f    ...            ; Store port to FS command URD field
    stx fs_error_ptr                                                  ; 8a35: 86 b8       ..             ; Save port for error recovery
    ldx #8                                                            ; 8a37: a2 08       ..             ; X=8: command data bytes
    lda fs_cmd_data                                                   ; 8a39: ad 05 0f    ...            ; Load handle from FS command data
    jsr prepare_cmd_with_flag                                         ; 8a3c: 20 41 83     A.            ; Build FS command with handle+flag
    lda fs_load_addr_3                                                ; 8a3f: a5 b3       ..             ; Save seq# for byte-stream flow control
    sta fs_sequence_nos                                               ; 8a41: 8d 08 0e    ...            ; Store to FS sequence number workspace
    ldx #4                                                            ; 8a44: a2 04       ..             ; X=4: copy 4 address bytes
; &8a46 referenced 1 time by &8a5a
.gbpbl3
    lda (fs_options),y                                                ; 8a46: b1 bb       ..             ; Set up source/dest from param block
    sta addr_work,y                                                   ; 8a48: 99 af 00    ...            ; Store as source address
    sta txcb_pos,y                                                    ; 8a4b: 99 c7 00    ...            ; Store as current transfer position
    jsr add_4_to_y                                                    ; 8a4e: 20 a6 84     ..            ; Skip 4 bytes to reach transfer length
    adc (fs_options),y                                                ; 8a51: 71 bb       q.             ; Dest = source + length
    sta addr_work,y                                                   ; 8a53: 99 af 00    ...            ; Store as end address
    jsr sub_3_from_y                                                  ; 8a56: 20 ac 84     ..            ; Back 3 to align for next iteration
    dex                                                               ; 8a59: ca          .              ; Decrement byte counter
    bne gbpbl3                                                        ; 8a5a: d0 ea       ..             ; Loop for all 4 address bytes
    inx                                                               ; 8a5c: e8          .              ; X=1 after loop
; &8a5d referenced 1 time by &8a64
.gbpbf3
    lda fs_cmd_csd,x                                                  ; 8a5d: bd 03 0f    ...            ; Copy CSD data to command buffer
    sta fs_func_code,x                                                ; 8a60: 9d 06 0f    ...            ; Store at &0F06+X
    dex                                                               ; 8a63: ca          .              ; Decrement counter
    bpl gbpbf3                                                        ; 8a64: 10 f7       ..             ; Loop for X=1,0
    pla                                                               ; 8a66: 68          h              ; Odd (read): send data to FS first
    bne gbpb_read_path                                                ; 8a67: d0 08       ..             ; Non-zero: skip write path
    lda fs_cmd_urd                                                    ; 8a69: ad 02 0f    ...            ; Load port for transfer setup
    jsr transfer_file_blocks                                          ; 8a6c: 20 c9 87     ..            ; Transfer data blocks to fileserver
    bne findv_eof_check                                               ; 8a6f: d0 03       ..             ; Non-zero: branch past error ptr
; &8a71 referenced 1 time by &8a67
.gbpb_read_path
    jsr send_data_blocks                                              ; 8a71: 20 17 87     ..            ; Read path: receive data blocks from FS
; &8a74 referenced 1 time by &8a6f
.findv_eof_check
    lda #&2a ; '*'                                                    ; 8a74: a9 2a       .*             ; A=&2A: error ptr for FS retry
    sta fs_error_ptr                                                  ; 8a76: 85 b8       ..             ; Store error ptr for TX poll
.wait_fs_reply
    jsr send_fs_reply_cmd                                             ; 8a78: 20 81 83     ..            ; Wait for FS reply command
    lda (fs_options,x)                                                ; 8a7b: a1 bb       ..             ; Load handle mask for EOF flag update
    bit fs_cmd_data                                                   ; 8a7d: 2c 05 0f    ,..            ; Check FS reply: bit 7 = not at EOF
    bmi skip_clear_flag                                               ; 8a80: 30 03       0.             ; Bit 7 set: not EOF, skip clear
    jsr clear_fs_flag                                                 ; 8a82: 20 e0 85     ..            ; At EOF: clear EOF hint for this handle
; &8a85 referenced 1 time by &8a80
.skip_clear_flag
    jsr set_fs_flag                                                   ; 8a85: 20 e5 85     ..            ; Set EOF hint flag (may be at EOF)
    stx fs_load_addr_2                                                ; 8a88: 86 b2       ..             ; Direction=0: forward adjustment
    jsr adjust_addrs_9                                                ; 8a8a: 20 cb 89     ..            ; Adjust param block addrs by +9 bytes
    dec fs_load_addr_2                                                ; 8a8d: c6 b2       ..             ; Direction=&FF: reverse adjustment
    sec                                                               ; 8a8f: 38          8              ; SEC for reverse subtraction
    jsr adjust_addrs                                                  ; 8a90: 20 d3 89     ..            ; Adjust param block addrs (reverse)
    asl fs_cmd_data                                                   ; 8a93: 0e 05 0f    ...            ; Shift bit 7 into C for return flag
    jmp return_a_zero                                                 ; 8a96: 4c 46 89    LF.            ; Return via restore_args path

; &8a99 referenced 1 time by &8ac9
.get_disc_title
    ldy #&15                                                          ; 8a99: a0 15       ..             ; Y=&15: function code for disc title; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8a9b: 20 51 83     Q.            ; Build and send FS command; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8a9e: ad 05 0e    ...            ; Load boot option from FS workspace
    sta fs_boot_data                                                  ; 8aa1: 8d 16 0f    ...            ; Store boot option in reply area
    stx fs_load_addr                                                  ; 8aa4: 86 b0       ..             ; X=0: reply data start offset; X=0 on success, &D6 on not-found
    stx fs_load_addr_hi                                               ; 8aa6: 86 b1       ..             ; Clear reply buffer high byte
    lda #&12                                                          ; 8aa8: a9 12       ..             ; A=&12: 18 bytes of reply data
    sta fs_load_addr_2                                                ; 8aaa: 85 b2       ..             ; Store as byte count for copy
    bne copy_reply_to_caller                                          ; 8aac: d0 4e       .N             ; ALWAYS branch to copy_reply_to_caller; ALWAYS branch

; ***************************************************************************************
; OSGBPB 5-8 info handler (OSINFO)
; 
; Handles the "messy interface tacked onto OSGBPB" (original source).
; Checks whether the destination address is in Tube space by comparing
; the high bytes against TBFLAG. If in Tube space, data must be
; copied via the Tube FIFO registers (with delays to accommodate the
; slow 16032 co-processor) instead of direct memory access.
; ***************************************************************************************
; &8aae referenced 1 time by &8a01
.osgbpb_info
    ldy #4                                                            ; 8aae: a0 04       ..             ; Y=4: check param block byte 4
    lda tx_in_progress                                                ; 8ab0: ad 52 0d    .R.            ; Check if destination is in Tube space
    beq store_tube_flag                                               ; 8ab3: f0 07       ..             ; No Tube: skip Tube address check
    cmp (fs_options),y                                                ; 8ab5: d1 bb       ..             ; Compare Tube flag with addr byte 4
    bne store_tube_flag                                               ; 8ab7: d0 03       ..             ; Mismatch: not Tube space
    dey                                                               ; 8ab9: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8aba: f1 bb       ..             ; Y=3: subtract addr byte 3 from flag
; &8abc referenced 2 times by &8ab3, &8ab7
.store_tube_flag
    sta rom_svc_num                                                   ; 8abc: 85 ce       ..             ; Non-zero = Tube transfer required
; &8abe referenced 1 time by &8ac4
.info2
    lda (fs_options),y                                                ; 8abe: b1 bb       ..             ; Copy param block bytes 1-4 to workspace
    sta fs_last_byte_flag,y                                           ; 8ac0: 99 bd 00    ...            ; Store to &BD+Y workspace area
    dey                                                               ; 8ac3: 88          .              ; Previous byte
    bne info2                                                         ; 8ac4: d0 f8       ..             ; Loop for bytes 3,2,1
    pla                                                               ; 8ac6: 68          h              ; Sub-function: AND #3 of (original A - 4)
    and #3                                                            ; 8ac7: 29 03       ).             ; Mask to 0-3 (OSGBPB 5-8 → 0-3)
    beq get_disc_title                                                ; 8ac9: f0 ce       ..             ; A=0 (OSGBPB 5): read disc title
    lsr a                                                             ; 8acb: 4a          J              ; LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)
    beq gbpb6_read_name                                               ; 8acc: f0 02       ..             ; A=0 (OSGBPB 6): read CSD/LIB name
    bcs gbpb8_read_dir                                                ; 8ace: b0 66       .f             ; C=1 (OSGBPB 8): read filenames from dir
; &8ad0 referenced 1 time by &8acc
.gbpb6_read_name
    tay                                                               ; 8ad0: a8          .              ; Y=0 for CSD or carry for fn code select; Y=function code
    lda fs_csd_handle,y                                               ; 8ad1: b9 03 0e    ...            ; Get CSD/LIB/URD handles for FS command
    sta fs_cmd_csd                                                    ; 8ad4: 8d 03 0f    ...            ; Store CSD handle in command buffer
    lda fs_lib_handle                                                 ; 8ad7: ad 04 0e    ...            ; Load LIB handle from workspace
    sta fs_cmd_lib                                                    ; 8ada: 8d 04 0f    ...            ; Store LIB handle in command buffer
    lda fs_urd_handle                                                 ; 8add: ad 02 0e    ...            ; Load URD handle from workspace
    sta fs_cmd_urd                                                    ; 8ae0: 8d 02 0f    ...            ; Store URD handle in command buffer
    ldx #&12                                                          ; 8ae3: a2 12       ..             ; X=&12: buffer extent for command data; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8ae5: 8e 01 0f    ...            ; Store X as function code in header
    lda #&0d                                                          ; 8ae8: a9 0d       ..             ; &0D = 13 bytes of reply data expected
    sta fs_func_code                                                  ; 8aea: 8d 06 0f    ...            ; Store reply length in command buffer
    sta fs_load_addr_2                                                ; 8aed: 85 b2       ..             ; Store as byte count for copy loop
    lsr a                                                             ; 8aef: 4a          J              ; LSR: &0D >> 1 = 6; A=timeout period for FS reply
    sta fs_cmd_data                                                   ; 8af0: 8d 05 0f    ...            ; Store as command data byte
    clc                                                               ; 8af3: 18          .              ; CLC for standard FS path
    jsr build_send_fs_cmd                                             ; 8af4: 20 6b 83     k.            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8af7: 86 b1       ..             ; X=0 on success, &D6 on not-found
    inx                                                               ; 8af9: e8          .              ; INX: X=1 after build_send_fs_cmd
    stx fs_load_addr                                                  ; 8afa: 86 b0       ..             ; Store X as reply start offset
; &8afc referenced 2 times by &8aac, &8b6f
.copy_reply_to_caller
    lda rom_svc_num                                                   ; 8afc: a5 ce       ..             ; Copy FS reply to caller's buffer
    bne tube_transfer                                                 ; 8afe: d0 11       ..             ; Non-zero: use Tube transfer path
    ldx fs_load_addr                                                  ; 8b00: a6 b0       ..             ; X = reply start offset
    ldy fs_load_addr_hi                                               ; 8b02: a4 b1       ..             ; Y = reply buffer high byte
; &8b04 referenced 1 time by &8b0d
.copy_reply_bytes
    lda fs_cmd_data,x                                                 ; 8b04: bd 05 0f    ...            ; Load reply data byte
    sta (fs_crc_lo),y                                                 ; 8b07: 91 be       ..             ; Store to caller's buffer
    inx                                                               ; 8b09: e8          .              ; Next source byte
    iny                                                               ; 8b0a: c8          .              ; Next destination byte
    dec fs_load_addr_2                                                ; 8b0b: c6 b2       ..             ; Decrement remaining bytes
    bne copy_reply_bytes                                              ; 8b0d: d0 f5       ..             ; Loop until all bytes copied
    beq gbpb_done                                                     ; 8b0f: f0 22       ."             ; ALWAYS branch to exit; ALWAYS branch

; &8b11 referenced 1 time by &8afe
.tube_transfer
    jsr tube_claim_loop                                               ; 8b11: 20 8b 8b     ..            ; Claim Tube transfer channel
    lda #1                                                            ; 8b14: a9 01       ..             ; A=1: Tube claim type 1 (write)
    ldx fs_options                                                    ; 8b16: a6 bb       ..             ; X = param block address low
    ldy fs_block_offset                                               ; 8b18: a4 bc       ..             ; Y = param block address high
    inx                                                               ; 8b1a: e8          .              ; INX: advance past byte 0
    bne no_page_wrap                                                  ; 8b1b: d0 01       ..             ; No page wrap: keep Y
    iny                                                               ; 8b1d: c8          .              ; Page wrap: increment high byte
; &8b1e referenced 1 time by &8b1b
.no_page_wrap
    jsr tube_addr_claim                                               ; 8b1e: 20 06 04     ..            ; Claim Tube address for transfer
    ldx fs_load_addr                                                  ; 8b21: a6 b0       ..             ; X = reply data start offset
; &8b23 referenced 1 time by &8b2c
.tbcop1
    lda fs_cmd_data,x                                                 ; 8b23: bd 05 0f    ...            ; Load reply data byte
    sta tube_data_register_3                                          ; 8b26: 8d e5 fe    ...            ; Send byte to Tube via R3
    inx                                                               ; 8b29: e8          .              ; Next source byte
    dec fs_load_addr_2                                                ; 8b2a: c6 b2       ..             ; Decrement remaining bytes
    bne tbcop1                                                        ; 8b2c: d0 f5       ..             ; Loop until all bytes sent to Tube
    lda #&83                                                          ; 8b2e: a9 83       ..             ; Release Tube after transfer complete
    jsr tube_addr_claim                                               ; 8b30: 20 06 04     ..            ; Release Tube address claim
; &8b33 referenced 2 times by &8b0f, &8b89
.gbpb_done
    jmp return_a_zero                                                 ; 8b33: 4c 46 89    LF.            ; Return via restore_args path

; &8b36 referenced 1 time by &8ace
.gbpb8_read_dir
    ldy #9                                                            ; 8b36: a0 09       ..             ; OSGBPB 8: read filenames from dir
    lda (fs_options),y                                                ; 8b38: b1 bb       ..             ; Byte 9: number of entries to read
    sta fs_func_code                                                  ; 8b3a: 8d 06 0f    ...            ; Store as reply count in command buffer
    ldy #5                                                            ; 8b3d: a0 05       ..             ; Y=5: byte 5 = starting entry number
    lda (fs_options),y                                                ; 8b3f: b1 bb       ..             ; Load starting entry number
    sta fs_data_count                                                 ; 8b41: 8d 07 0f    ...            ; Store in command buffer
    ldx #&0d                                                          ; 8b44: a2 0d       ..             ; X=&0D: command data extent; X=preserved through header build
    stx fs_reply_cmd                                                  ; 8b46: 8e 08 0f    ...            ; Store extent in command buffer
    ldy #2                                                            ; 8b49: a0 02       ..             ; Y=2: function code for dir read
    sty fs_load_addr                                                  ; 8b4b: 84 b0       ..             ; Store 2 as reply data start offset
    sty fs_cmd_data                                                   ; 8b4d: 8c 05 0f    ...            ; Store 2 as command data byte
    iny                                                               ; 8b50: c8          .              ; Y=3: function code for header read; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8b51: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8b54: 86 b1       ..             ; X=0 after FS command completes; X=0 on success, &D6 on not-found
    lda fs_func_code                                                  ; 8b56: ad 06 0f    ...            ; Load reply entry count
    sta (fs_options,x)                                                ; 8b59: 81 bb       ..             ; Store at param block byte 0 (X=0)
    lda fs_cmd_data                                                   ; 8b5b: ad 05 0f    ...            ; Load entries-read count from reply
    ldy #9                                                            ; 8b5e: a0 09       ..             ; Y=9: param block byte 9
    adc (fs_options),y                                                ; 8b60: 71 bb       q.             ; Add to starting entry number
    sta (fs_options),y                                                ; 8b62: 91 bb       ..             ; Update param block with new position
    lda txcb_end                                                      ; 8b64: a5 c8       ..             ; Load total reply length
    sbc #7                                                            ; 8b66: e9 07       ..             ; Subtract header (7 bytes) from reply len
    sta fs_func_code                                                  ; 8b68: 8d 06 0f    ...            ; Store adjusted length in command buffer
    sta fs_load_addr_2                                                ; 8b6b: 85 b2       ..             ; Store as byte count for copy loop
    beq skip_copy_reply                                               ; 8b6d: f0 03       ..             ; Zero bytes: skip copy
    jsr copy_reply_to_caller                                          ; 8b6f: 20 fc 8a     ..            ; Copy reply data to caller's buffer
; &8b72 referenced 1 time by &8b6d
.skip_copy_reply
    ldx #2                                                            ; 8b72: a2 02       ..             ; X=2: clear 3 bytes
; &8b74 referenced 1 time by &8b78
.zero_cmd_bytes
    sta fs_data_count,x                                               ; 8b74: 9d 07 0f    ...            ; Zero out &0F07+X area
    dex                                                               ; 8b77: ca          .              ; Next byte
    bpl zero_cmd_bytes                                                ; 8b78: 10 fa       ..             ; Loop for X=2,1,0
    jsr adjust_addrs_1                                                ; 8b7a: 20 d0 89     ..            ; Adjust pointer by +1 (one filename read)
    sec                                                               ; 8b7d: 38          8              ; SEC for reverse adjustment
    dec fs_load_addr_2                                                ; 8b7e: c6 b2       ..             ; Reverse adjustment for updated counter
    lda fs_cmd_data                                                   ; 8b80: ad 05 0f    ...            ; Load entries-read count
    sta fs_func_code                                                  ; 8b83: 8d 06 0f    ...            ; Store in command buffer
    jsr adjust_addrs                                                  ; 8b86: 20 d3 89     ..            ; Adjust param block addresses
    beq gbpb_done                                                     ; 8b89: f0 a8       ..             ; Z=1: all done, exit
; &8b8b referenced 3 times by &8b11, &8b90, &8da1
.tube_claim_loop
    lda #&c3                                                          ; 8b8b: a9 c3       ..             ; A=&C3: Tube claim with retry
    jsr tube_addr_claim                                               ; 8b8d: 20 06 04     ..            ; Request Tube address claim
    bcc tube_claim_loop                                               ; 8b90: 90 f9       ..             ; C=0: claim failed, retry
    rts                                                               ; 8b92: 60          `              ; Tube claimed successfully

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
; &8b93 referenced 1 time by &8243
.fscv_3_star_cmd
    jsr save_fscv_args                                                ; 8b93: 20 09 85     ..            ; Save A/X/Y and set up command ptr
    ldx #&ff                                                          ; 8b96: a2 ff       ..             ; X=&FF: table index (pre-incremented)
; &8b98 referenced 1 time by &8bb3
.scan_cmd_table
    ldy #&ff                                                          ; 8b98: a0 ff       ..             ; Y=&FF: input index (pre-incremented)
; &8b9a referenced 1 time by &8ba5
.decfir
    iny                                                               ; 8b9a: c8          .              ; Advance input pointer
    inx                                                               ; 8b9b: e8          .              ; Advance table pointer
; &8b9c referenced 1 time by &8bb7
.decmor
    lda fs_cmd_match_table,x                                          ; 8b9c: bd d7 8b    ...            ; Load table character
    bmi dispatch_cmd                                                  ; 8b9f: 30 18       0.             ; Bit 7: end of name, dispatch
    eor (fs_crc_lo),y                                                 ; 8ba1: 51 be       Q.             ; XOR input char with table char
    and #&df                                                          ; 8ba3: 29 df       ).             ; Case-insensitive (clear bit 5)
    beq decfir                                                        ; 8ba5: f0 f3       ..             ; Match: continue comparing
    dex                                                               ; 8ba7: ca          .              ; Mismatch: back up table pointer
; &8ba8 referenced 1 time by &8bac
.decmin
    inx                                                               ; 8ba8: e8          .              ; Skip to end of table entry
    lda fs_cmd_match_table,x                                          ; 8ba9: bd d7 8b    ...            ; Load table byte
    bpl decmin                                                        ; 8bac: 10 fa       ..             ; Loop until bit 7 set (end marker)
    lda (fs_crc_lo),y                                                 ; 8bae: b1 be       ..             ; Check input for '.' abbreviation
    inx                                                               ; 8bb0: e8          .              ; Skip past handler high byte
    cmp #&2e ; '.'                                                    ; 8bb1: c9 2e       ..             ; Is input '.' (abbreviation)?
    bne scan_cmd_table                                                ; 8bb3: d0 e3       ..             ; No: try next table entry
    iny                                                               ; 8bb5: c8          .              ; Yes: skip '.' in input
    dex                                                               ; 8bb6: ca          .              ; Back to handler high byte
    bcs decmor                                                        ; 8bb7: b0 e3       ..             ; ALWAYS branch; dispatch via BMI
; &8bb9 referenced 1 time by &8b9f
.dispatch_cmd
    pha                                                               ; 8bb9: 48          H              ; Push handler address high byte
    lda cmd_table_entry_1,x                                           ; 8bba: bd d8 8b    ...            ; Load handler address low byte
    pha                                                               ; 8bbd: 48          H              ; Push handler address low byte
    clc                                                               ; 8bbe: 18          .              ; CLC for pointer calculation
    tya                                                               ; 8bbf: 98          .              ; A = chars consumed from input
    ldx fs_crc_hi                                                     ; 8bc0: a6 bf       ..             ; X = command text pointer high
    adc fs_crc_lo                                                     ; 8bc2: 65 be       e.             ; Add chars consumed to pointer low
    sta fs_context_hi                                                 ; 8bc4: 8d 0b 0e    ...            ; Store adjusted text pointer low
    sta fs_cmd_ptr                                                    ; 8bc7: 8d 10 0e    ...            ; Duplicate to second pointer copy
    bcc cmd_match_retry                                               ; 8bca: 90 01       ..             ; No page overflow: skip INX
    inx                                                               ; 8bcc: e8          .              ; Adjust high byte for page crossing
; &8bcd referenced 1 time by &8bca
.cmd_match_retry
    stx l0e0c                                                         ; 8bcd: 8e 0c 0e    ...            ; Store high byte to context ptr 1
    stx l0e11                                                         ; 8bd0: 8e 11 0e    ...            ; Store high byte to context ptr 2
    stx fs_work_16                                                    ; 8bd3: 8e 16 0e    ...            ; Store high byte to context ptr 3
    rts                                                               ; 8bd6: 60          `              ; Dispatch via PHA/PHA/RTS

; ***************************************************************************************
; FS command match table (COMTAB)
; 
; Format: command letters (bit 7 clear), then dispatch address
; as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
; adds 1 to the stored (address-1). Matching is case-insensitive
; (AND &DF) and supports '.' abbreviation (standard Acorn pattern).
; 
; Entries:
;   "I."     → &8079 (forward_star_cmd) — placed first as a fudge
;              to catch *I. abbreviation before matching *I AM
;   "I AM"   → &8D07 (i_am_handler: parse station.net, logon)
;   "EX "    → &8BF3 (ex_handler: extended catalogue)
;   "EX"\r   → &8BF3 (same, exact match at end of line)
;   "BYE"\r  → &834A (bye_handler: logoff)
;   <catch-all> → &8079 (forward anything else to FS)
; ***************************************************************************************
; &8bd7 referenced 2 times by &8b9c, &8ba9
.fs_cmd_match_table
cmd_table_entry_1 = fs_cmd_match_table+1
    eor #&2e ; '.'                                                    ; 8bd7: 49 2e       I.             ; XOR with '.' (abbreviation check)
; &8bd8 referenced 1 time by &8bba
    equb &80                                                          ; 8bd9: 80          .
    equs "xI AM"                                                      ; 8bda: 78 49 20... xI
    equb &8d, 6                                                       ; 8bdf: 8d 06       ..
    equs "EX "                                                        ; 8be1: 45 58 20    EX
    equb &8b, &f2, &45, &58, &0d, &8b, &f2                            ; 8be4: 8b f2 45... ..E
    equs "BYE"                                                        ; 8beb: 42 59 45    BYE
    equb &0d, &83, &49, &80, &78                                      ; 8bee: 0d 83 49... ..I

; ***************************************************************************************
; *EX handler (extended catalogue)
; 
; Sets column width &B6=&50 (80 columns, one file per line with
; full details) and &B7=&01, then branches into fscv_5_cat at
; &8C08, bypassing fscv_5_cat's default 20-column setup.
; ***************************************************************************************
.ex_handler
    dey                                                               ; 8bf3: 88          .              ; Pre-decrement Y for parameter
    ldx #1                                                            ; 8bf4: a2 01       ..             ; X=1: boot option display field
    stx fs_work_7                                                     ; 8bf6: 86 b7       ..             ; Store to fs_work_7 (&B7)
    ldx #&50 ; 'P'                                                    ; 8bf8: a2 50       .P             ; X=&50: 80-column display width
    stx l00b6                                                         ; 8bfa: 86 b6       ..             ; Store column width at &B6
    bne cat_init_display                                              ; 8bfc: d0 0a       ..             ; ALWAYS branch

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
    ldx #&14                                                          ; 8bfe: a2 14       ..             ; X=&14 (20): column width for display
    stx l00b6                                                         ; 8c00: 86 b6       ..             ; Store column width for batch calc
    ldx #3                                                            ; 8c02: a2 03       ..             ; X=3: column count for examine request
    stx fs_work_7                                                     ; 8c04: 86 b7       ..             ; Store column count
    ldy #0                                                            ; 8c06: a0 00       ..             ; Y=0: initial entry start offset
; &8c08 referenced 1 time by &8bfc
.cat_init_display
    lda #6                                                            ; 8c08: a9 06       ..             ; A=6: examine format type in command
    sta fs_cmd_data                                                   ; 8c0a: 8d 05 0f    ...            ; Store format type at &0F05
    jsr skip_spaces                                                   ; 8c0d: 20 56 85     V.            ; Skip spaces in dir name argument
    sty fs_load_addr_3                                                ; 8c10: 84 b3       ..             ; Save parameter offset after spaces
    ldx #1                                                            ; 8c12: a2 01       ..             ; X=1: copy dir name at cmd offset 1
    jsr copy_string_from_offset                                       ; 8c14: 20 68 8d     h.            ; Copy directory name to command buffer
    ldy #&12                                                          ; 8c17: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c19: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c1c: a2 03       ..             ; X=3: start printing from reply offset 3
    jsr print_reply_bytes                                             ; 8c1e: 20 50 8d     P.            ; Print directory title (10 chars)
    jsr print_inline                                                  ; 8c21: 20 3c 85     <.            ; Print '('
    equs "("                                                          ; 8c24: 28          (

    lda fs_reply_stn                                                  ; 8c25: ad 13 0f    ...            ; Load station number from FS reply
    jsr print_decimal                                                 ; 8c28: 20 b0 85     ..            ; Print station number as decimal
    jsr print_inline                                                  ; 8c2b: 20 3c 85     <.            ; Print ')     '
    equs ")"                                                          ; 8c2e: 29          )

    ldx #5                                                            ; 8c2f: a2 05       ..             ; X=5: space padding count
    jsr print_spaces                                                  ; 8c31: 20 5d 8d     ].            ; Print 5 spaces for alignment
    ldx fs_access_level                                               ; 8c34: ae 12 0f    ...            ; Access: 0=Owner, non-zero=Public
    bne print_public                                                  ; 8c37: d0 0b       ..             ; Non-zero: Public access
    jsr print_inline                                                  ; 8c39: 20 3c 85     <.            ; Print 'Owner' + CR
    equs "Owner", &0d                                                 ; 8c3c: 4f 77 6e... Own

    bne cat_access_setup                                              ; 8c42: d0 0a       ..             ; Always taken (high-bit term. str)
; &8c44 referenced 1 time by &8c37
.print_public
    jsr print_inline                                                  ; 8c44: 20 3c 85     <.            ; Print 'Public' + CR
    equs "Public", &0d                                                ; 8c47: 50 75 62... Pub

; &8c4e referenced 1 time by &8c42
.cat_access_setup
    ldy #&15                                                          ; 8c4e: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c50: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8c53: e8          .              ; X=1: past command code byte
    ldy #&10                                                          ; 8c54: a0 10       ..             ; Y=&10: print 16 characters
    jsr print_reply_counted                                           ; 8c56: 20 52 8d     R.            ; Print disc/CSD name from reply
    ldx #4                                                            ; 8c59: a2 04       ..             ; X=4: space padding count
    jsr print_spaces                                                  ; 8c5b: 20 5d 8d     ].            ; Print 4 spaces for alignment
    jsr print_inline                                                  ; 8c5e: 20 3c 85     <.            ; Print 'Option ' label
    equs "Option "                                                    ; 8c61: 4f 70 74... Opt

    lda fs_boot_option                                                ; 8c68: ad 05 0e    ...            ; Load boot option from workspace
    tax                                                               ; 8c6b: aa          .              ; X = boot option for name table lookup
    jsr print_hex                                                     ; 8c6c: 20 ec 85     ..            ; Print boot option as hex digit
    jsr print_inline                                                  ; 8c6f: 20 3c 85     <.            ; Print ' ('
    equs " ("                                                         ; 8c72: 20 28        (

    ldy option_name_offsets,x                                         ; 8c74: bc 4c 8d    .L.            ; Load string offset for option name
; &8c77 referenced 1 time by &8c80
.print_option_char
    lda option_name_strings,y                                         ; 8c77: b9 3b 8d    .;.            ; Load char from option name string
    beq done_option_name                                              ; 8c7a: f0 06       ..             ; Zero terminator: name complete
    jsr osasci                                                        ; 8c7c: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8c7f: c8          .              ; Next character
    bne print_option_char                                             ; 8c80: d0 f5       ..             ; Continue printing option name
; &8c82 referenced 1 time by &8c7a
.done_option_name
    jsr print_inline                                                  ; 8c82: 20 3c 85     <.            ; Print ')' + CR + 'Dir. '
    equs ")", &0d, "Dir. "                                            ; 8c85: 29 0d 44... ).D

    ldx #&11                                                          ; 8c8c: a2 11       ..             ; X=&11: CSD name offset in reply
    jsr print_reply_bytes                                             ; 8c8e: 20 50 8d     P.            ; Print current directory name
    ldx #5                                                            ; 8c91: a2 05       ..             ; X=5: space padding count
    jsr print_spaces                                                  ; 8c93: 20 5d 8d     ].            ; Print 5 spaces for alignment
    jsr print_inline                                                  ; 8c96: 20 3c 85     <.            ; Print 'Lib. ' label
    equs "Lib. "                                                      ; 8c99: 4c 69 62... Lib

    ldx #&1b                                                          ; 8c9e: a2 1b       ..             ; X=&1B: library name offset in reply
    jsr print_reply_bytes                                             ; 8ca0: 20 50 8d     P.            ; Print library name
    jsr print_inline                                                  ; 8ca3: 20 3c 85     <.            ; Print two CRs (blank line)
    equs &0d, &0d                                                     ; 8ca6: 0d 0d       ..

    sty fs_func_code                                                  ; 8ca8: 8c 06 0f    ...            ; Y=0: initial examine start position
    sty fs_work_4                                                     ; 8cab: 84 b4       ..             ; Save start offset in zero page for loop
    txa                                                               ; 8cad: 8a          .              ; A = reply buffer bytes consumed
    eor #&ff                                                          ; 8cae: 49 ff       I.             ; Complement for divide-by-subtraction
; &8cb0 referenced 1 time by &8cb4
.count_columns_loop
    sec                                                               ; 8cb0: 38          8              ; SEC for subtraction
    sbc l00b6                                                         ; 8cb1: e5 b6       ..             ; Subtract one column width (20)
    iny                                                               ; 8cb3: c8          .              ; Count another entry that fits
    bcs count_columns_loop                                            ; 8cb4: b0 fa       ..             ; Loop while space remains
    sty fs_data_count                                                 ; 8cb6: 8c 07 0f    ...            ; Store entries per examine batch
    sty fs_work_5                                                     ; 8cb9: 84 b5       ..             ; Save batch size for loop reset
; &8cbb referenced 1 time by &8ce6
.cat_examine_continue
    ldy fs_load_addr_3                                                ; 8cbb: a4 b3       ..             ; Reload dir name offset for examine
.cat_examine_loop
    ldx fs_work_7                                                     ; 8cbd: a6 b7       ..             ; Load column count for display format
    stx fs_cmd_data                                                   ; 8cbf: 8e 05 0f    ...            ; Store column count in command data
    ldx #3                                                            ; 8cc2: a2 03       ..             ; X=3: copy directory name at offset 3
    jsr copy_string_from_offset                                       ; 8cc4: 20 68 8d     h.            ; Append directory name to examine command
    ldy #3                                                            ; 8cc7: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cc9: 20 51 83     Q.            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 8ccc: ad 05 0f    ...            ; Load entry count from reply
    beq set_handle_return                                             ; 8ccf: f0 2f       ./             ; Zero entries returned: catalogue done
    ldx #2                                                            ; 8cd1: a2 02       ..             ; X=2: first entry offset in reply
    jsr print_dir_from_offset                                         ; 8cd3: 20 76 8d     v.            ; Print/format this directory entry
    clc                                                               ; 8cd6: 18          .              ; CLC for addition
    lda fs_work_4                                                     ; 8cd7: a5 b4       ..             ; Load current examine start offset
    adc fs_cmd_data                                                   ; 8cd9: 6d 05 0f    m..            ; Add entries returned this batch
    sta fs_func_code                                                  ; 8cdc: 8d 06 0f    ...            ; Update next examine start offset
    sta fs_work_4                                                     ; 8cdf: 85 b4       ..             ; Save updated start offset
    lda fs_work_5                                                     ; 8ce1: a5 b5       ..             ; Reload batch size for next request
    sta fs_data_count                                                 ; 8ce3: 8d 07 0f    ...            ; Store batch size in command buffer
    bne cat_examine_continue                                          ; 8ce6: d0 d3       ..             ; Loop for remaining characters
    jmp l212e                                                         ; 8ce8: 4c 2e 21    L.!            ; Fallthrough (also boot string 'L.!')

; ***************************************************************************************
; Boot command strings for auto-boot
; 
; The four boot options use OSCLI strings at offsets within page &8C:
;   Option 0 (Off):  offset &F7 → &8CF7 = bare CR (empty command)
;   Option 1 (Load): offset &E8 → &8CE8 = "L.!BOOT" (dual-purpose:
;       the JMP &212E instruction at &8CE8 has opcode &4C='L' and
;       operand bytes &2E='.' &21='!', forming the string "L.!")
;   Option 2 (Run):  offset &EA → &8CEA = "!BOOT" (bare filename = *RUN)
;   Option 3 (Exec): offset &F0 → &8CF0 = "E.!BOOT"
; 
; This is a classic BBC ROM space optimisation: the JMP instruction's
; bytes serve double duty as both executable code and ASCII text.
; ***************************************************************************************
.boot_cmd_strings
    equs "BOOT"                                                       ; 8ceb: 42 4f 4f... BOO
    equb &0d                                                          ; 8cef: 0d          .
    equs "E.!BOOT"                                                    ; 8cf0: 45 2e 21... E.!
    equb &0d                                                          ; 8cf7: 0d          .

; ***************************************************************************************
; Set library handle
; 
; Stores Y into &0E04 (library directory handle in FS workspace).
; Falls through to set_handle_return (JMP restore_args_return) if Y is non-zero.
; 
; On Entry:
;     Y: library handle from FS reply
; ***************************************************************************************
.fsreply_5_set_lib
    sty fs_lib_handle                                                 ; 8cf8: 8c 04 0e    ...            ; Store Y (library handle) to &0E04
    bne set_handle_return                                             ; 8cfb: d0 03       ..             ; Non-zero: continue to set handle
; ***************************************************************************************
; Set CSD handle
; 
; Stores Y into &0E03 (current selected directory handle).
; Falls through to set_handle_return (JMP restore_args_return).
; 
; On Entry:
;     Y: CSD handle from FS reply
; ***************************************************************************************
.fsreply_3_set_csd
    sty fs_csd_handle                                                 ; 8cfd: 8c 03 0e    ...            ; Store Y (CSD handle) to &0E03
; &8d00 referenced 3 times by &8ccf, &8cfb, &8d2e
.set_handle_return
    jmp restore_args_return                                           ; 8d00: 4c 2d 89    L-.            ; Jump to restore_args_return

; ***************************************************************************************
; Boot option → OSCLI string offset table
; 
; Four bytes indexed by the boot option value (0-3). Each byte
; is the low byte of a pointer into page &8C, where the OSCLI
; command string for that boot option lives. See boot_cmd_strings.
; ***************************************************************************************
; &8d03 referenced 1 time by &8d33
.boot_option_offsets
    equb &f7                                                          ; 8d03: f7          .              ; Opt 0 (Off): bare CR
    equb &e8                                                          ; 8d04: e8          .              ; Opt 1 (Load): L.!BOOT
    equb &ea                                                          ; 8d05: ea          .              ; Opt 2 (Run): !BOOT
    equb &f0                                                          ; 8d06: f0          .              ; Opt 3 (Exec): E.!BOOT

; ***************************************************************************************
; "I AM" command handler
; 
; Dispatched from the command match table when the user types
; "*I AM <station>" or "*I AM <network>.<station>".
; Skips leading spaces via skip_spaces, then calls parse_decimal
; twice if a dot separator is present. The first number becomes the
; network (&0E01, via TAX pass-through in parse_decimal) and the
; second becomes the station (&0E00). With a single number, it is
; stored as the station and the network defaults to 0 (local).
; Then forwards the command to the fileserver via forward_star_cmd.
; ***************************************************************************************
.i_am_handler
    jsr skip_spaces                                                   ; 8d07: 20 56 85     V.            ; Skip spaces before station number
    bcs jmp_restore_args                                              ; 8d0a: b0 11       ..             ; C=1: alphabetic, forward to FS
    lda #0                                                            ; 8d0c: a9 00       ..             ; A=0: default network (local)
    jsr parse_decimal                                                 ; 8d0e: 20 61 85     a.            ; Parse decimal number from (fs_options),Y (DECIN)
    bcc fsreply_handle_copy                                           ; 8d11: 90 04       ..             ; C=0: no dot, single number only
    iny                                                               ; 8d13: c8          .              ; Y=offset into (fs_options) buffer
    jsr parse_decimal                                                 ; 8d14: 20 61 85     a.            ; Parse decimal number from (fs_options),Y (DECIN)
; &8d17 referenced 1 time by &8d11
.fsreply_handle_copy
    sta fs_server_stn                                                 ; 8d17: 8d 00 0e    ...            ; A=parsed value (accumulated in &B2)
    stx fs_server_net                                                 ; 8d1a: 8e 01 0e    ...            ; X=initial A value (saved by TAX)
; &8d1d referenced 1 time by &8d0a
.jmp_restore_args
    jmp forward_star_cmd                                              ; 8d1d: 4c 79 80    Ly.            ; Restore A/X/Y and return to caller

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
    sec                                                               ; 8d20: 38          8              ; Set carry: LOGIN path (copy + boot)
; ***************************************************************************************
; Copy FS reply handles to workspace (no boot)
; 
; CLC entry (SDISC): copies handles only, then jumps to set_handle_return.
; Called when the FS reply contains updated handle values
; but no boot action is needed.
; ***************************************************************************************
.fsreply_2_copy_handles
    ldx #3                                                            ; 8d21: a2 03       ..             ; Copy 4 bytes: boot option + 3 handles
    bcc logon3                                                        ; 8d23: 90 06       ..             ; SDISC: skip boot option, copy handles only
; &8d25 referenced 1 time by &8d2c
.logon2
    lda fs_cmd_data,x                                                 ; 8d25: bd 05 0f    ...            ; Load from FS reply (&0F05+X)
    sta fs_urd_handle,x                                               ; 8d28: 9d 02 0e    ...            ; Store to handle workspace (&0E02+X)
; &8d2b referenced 1 time by &8d23
.logon3
    dex                                                               ; 8d2b: ca          .              ; Next handle (descending)
    bpl logon2                                                        ; 8d2c: 10 f7       ..             ; Loop while X >= 0
    bcc set_handle_return                                             ; 8d2e: 90 d0       ..             ; SDISC: done, restore args and return
; ***************************************************************************************
; Execute boot command via OSCLI
; 
; Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
; path). Reads the boot option from fs_boot_option (&0E05),
; looks up the OSCLI command string offset from boot_option_offsets+1,
; and executes the boot command via JMP oscli with page &8D.
; ***************************************************************************************
.boot_cmd_execute
    ldy fs_boot_option                                                ; 8d30: ac 05 0e    ...            ; Y = boot option from FS workspace
    ldx boot_option_offsets,y                                         ; 8d33: be 03 8d    ...            ; X = command string offset from table
    ldy #&8c                                                          ; 8d36: a0 8c       ..             ; Y = &8D (high byte of command address)
    jmp oscli                                                         ; 8d38: 4c f7 ff    L..            ; Execute boot command string via OSCLI

; ***************************************************************************************
; Option name strings
; 
; Null-terminated strings for the four boot option names:
;   "Off", "Load", "Run", "Exec"
; Used by fscv_5_cat to display the current boot option setting.
; ***************************************************************************************
; &8d3b referenced 1 time by &8c77
.option_name_strings
    equs "Off"                                                        ; 8d3b: 4f 66 66    Off
    equb 0                                                            ; 8d3e: 00          .
    equs "Load"                                                       ; 8d3f: 4c 6f 61... Loa
    equb 0                                                            ; 8d43: 00          .
    equs "Run"                                                        ; 8d44: 52 75 6e    Run
    equb 0                                                            ; 8d47: 00          .
    equs "Exec"                                                       ; 8d48: 45 78 65... Exe

; ***************************************************************************************
; Option name offsets
; 
; Four-byte table of offsets into option_name_strings:
;   0, 4, 9, &0D — one per boot option value (0-3).
; ***************************************************************************************
; &8d4c referenced 1 time by &8c74
.option_name_offsets
    brk                                                               ; 8d4c: 00          .              ; Offset 0 (BRK opcode as zero byte)

    equb 4, 9, &0d                                                    ; 8d4d: 04 09 0d    ...

; ***************************************************************************************
; Print reply buffer bytes
; 
; Prints Y characters from the FS reply buffer (&0F05+X) to
; the screen via OSASCI. X = starting offset, Y = count.
; Used by fscv_5_cat to display directory and library names.
; ***************************************************************************************
; &8d50 referenced 3 times by &8c1e, &8c8e, &8ca0
.print_reply_bytes
    ldy #&0a                                                          ; 8d50: a0 0a       ..             ; Y=10: default character count
; &8d52 referenced 2 times by &8c56, &8d5a
.print_reply_counted
    lda fs_cmd_data,x                                                 ; 8d52: bd 05 0f    ...            ; Load character from reply buffer
    jsr osasci                                                        ; 8d55: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8d58: e8          .              ; Advance to next character
    dey                                                               ; 8d59: 88          .              ; Decrement remaining count
    bne print_reply_counted                                           ; 8d5a: d0 f6       ..             ; Loop until count exhausted
    rts                                                               ; 8d5c: 60          `              ; Return to caller

; ***************************************************************************************
; Print spaces
; 
; Prints X space characters via print_space. Used by fscv_5_cat
; to align columns in the directory listing.
; ***************************************************************************************
; &8d5d referenced 4 times by &8c31, &8c5b, &8c93, &8d61
.print_spaces
    jsr print_space                                                   ; 8d5d: 20 41 86     A.            ; Print one space character
    dex                                                               ; 8d60: ca          .              ; Decrement space count
    bne print_spaces                                                  ; 8d61: d0 fa       ..             ; Loop until all spaces printed
    rts                                                               ; 8d63: 60          `              ; Return to caller

; ***************************************************************************************
; Copy filename to FS command buffer
; 
; Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; ***************************************************************************************
; &8d64 referenced 3 times by &8079, &86cc, &888b
.copy_filename
    ldx #0                                                            ; 8d64: a2 00       ..             ; X=0: start of output buffer
; ***************************************************************************************
; Copy string to FS command buffer
; 
; Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
; to &0F05+X, stopping when a CR (&0D) is encountered. The CR
; itself is also copied. Returns with X pointing past the last
; byte written.
; 
; On Entry:
;     X: destination offset in fs_cmd_data (&0F05+X)
; 
; On Exit:
;     X: next free position past CR
;     Y: string length (incl CR)
;     A: 0 (from EOR &0D with final CR)
; ***************************************************************************************
; &8d66 referenced 4 times by &877a, &8884, &88a6, &8965
.copy_string_to_cmd
    ldy #0                                                            ; 8d66: a0 00       ..             ; Start copying from offset 0
; &8d68 referenced 3 times by &8c14, &8cc4, &8d71
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d68: b1 be       ..             ; Load next byte from source string
    sta fs_cmd_data,x                                                 ; 8d6a: 9d 05 0f    ...            ; Store to command buffer
    inx                                                               ; 8d6d: e8          .              ; Advance write position
    iny                                                               ; 8d6e: c8          .              ; Advance read position
    eor #&0d                                                          ; 8d6f: 49 0d       I.             ; XOR with CR: result=0 if byte was CR
    bne copy_string_from_offset                                       ; 8d71: d0 f5       ..             ; Loop until CR copied
; &8d73 referenced 1 time by &8d79
.return_copy_string
    rts                                                               ; 8d73: 60          `              ; Return to caller

; ***************************************************************************************
; Print directory name from reply buffer
; 
; Prints characters from the FS reply buffer (&0F05+X onwards).
; Null bytes (&00) are replaced with CR (&0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by fscv_5_cat to display Dir. and Lib. paths.
; ***************************************************************************************
.fsreply_0_print_dir
    ldx #0                                                            ; 8d74: a2 00       ..             ; X=0: start of reply buffer
; &8d76 referenced 2 times by &8cd3, &8d83
.print_dir_from_offset
    lda fs_cmd_data,x                                                 ; 8d76: bd 05 0f    ...            ; Load character from reply
    bmi return_copy_string                                            ; 8d79: 30 f8       0.             ; Bit 7 set: end of string
    bne infol2                                                        ; 8d7b: d0 02       ..             ; Non-zero: printable character
    lda #&0d                                                          ; 8d7d: a9 0d       ..             ; Replace null with CR
; &8d7f referenced 1 time by &8d7b
.infol2
    jsr osasci                                                        ; 8d7f: 20 e3 ff     ..            ; Write character 13
    inx                                                               ; 8d82: e8          .              ; Advance to next character
    bne print_dir_from_offset                                         ; 8d83: d0 f1       ..             ; Continue printing directory path
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
    ldx #&0e                                                          ; 8d85: a2 0e       ..             ; X=&0E: OSWORD &10 parameter block size
    stx fs_block_offset                                               ; 8d87: 86 bc       ..             ; Y=0: param block offset
    lda #&10                                                          ; 8d89: a9 10       ..             ; A=&10: OSWORD &10 (open RXCB)
    sta fs_options                                                    ; 8d8b: 85 bb       ..             ; Issue OSWORD &10 to open RXCB
    ldx #&4a ; 'J'                                                    ; 8d8d: a2 4a       .J             ; Load RXCB number from result
    ldy #5                                                            ; 8d8f: a0 05       ..             ; Zero: no free RXCB, skip
    jsr send_fs_examine                                               ; 8d91: 20 d1 86     ..            ; Store RXCB number in exec context
    lda tx_in_progress                                                ; 8d94: ad 52 0d    .R.            ; Y=&70: FS workspace offset; Load reply byte from workspace
    beq net_handle_validate                                           ; 8d97: f0 14       ..             ; Store to exec param area
    adc fs_load_upper                                                 ; 8d99: 6d 0b 0f    m..            ; Advance to next param byte; Compare against boundary
    adc fs_addr_check                                                 ; 8d9c: 6d 0c 0f    m..            ; Loop for all exec parameters
    bcs net_handle_validate                                           ; 8d9f: b0 0c       ..             ; Store final byte
    jsr tube_claim_loop                                               ; 8da1: 20 8b 8b     ..            ; X=&16: OSBYTE param; A=&C7: OSBYTE read/write flag
    ldx #9                                                            ; 8da4: a2 09       ..             ; Enable exec notification via OSBYTE
    ldy #&0f                                                          ; 8da6: a0 0f       ..             ; Y=&0F: workspace offset for params
    lda #4                                                            ; 8da8: a9 04       ..             ; A=4: Tube claim type (multi-byte transfer)
    jmp tube_addr_claim                                               ; 8daa: 4c 06 04    L..            ; Claim Tube for address transfer

; &8dad referenced 2 times by &8d97, &8d9f
.net_handle_validate
    jmp (fs_load_vector)                                              ; 8dad: 6c 09 0f    l..            ; Execute at load address

; ***************************************************************************************
; *NET1: read file handle from received packet
; 
; Reads a file handle byte from offset &6F in the RX buffer
; (net_rx_ptr), stores it in &F0, then falls through to the
; common handle workspace cleanup at clear_svc_return.
; ***************************************************************************************
.net_1_read_handle
    ldy #&6f ; 'o'                                                    ; 8db0: a0 6f       .o             ; Y=&6F: handle offset in RX buffer
    lda (net_rx_ptr),y                                                ; 8db2: b1 9c       ..             ; Load handle byte from RX data
    sta osword_pb_ptr                                                 ; 8db4: 85 f0       ..             ; Store handle to &F0
    bcc clear_svc_return                                              ; 8db6: 90 23       .#             ; Branch to cleanup path
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
; 
; On Entry:
;     A: file handle number
; 
; On Exit:
;     A: handle*12 or 0 if invalid
;     Y: workspace offset or 0 if invalid
;     C: clear if valid, set if invalid
; ***************************************************************************************
; &8db8 referenced 5 times by &82b7, &8dcc, &8de2, &8f02, &8f1b
.calc_handle_offset
    asl a                                                             ; 8db8: 0a          .              ; A = handle * 2
    asl a                                                             ; 8db9: 0a          .              ; A = handle * 4
    pha                                                               ; 8dba: 48          H              ; Push handle*4 onto stack
    asl a                                                             ; 8dbb: 0a          .              ; A = handle * 8
    tsx                                                               ; 8dbc: ba          .              ; X = stack pointer
    adc l0101,x                                                       ; 8dbd: 7d 01 01    }..            ; A = handle*8 + handle*4 = handle*12
    tay                                                               ; 8dc0: a8          .              ; Y = offset into handle workspace
    pla                                                               ; 8dc1: 68          h              ; Clean up stack (discard handle*4)
    cmp #&48 ; 'H'                                                    ; 8dc2: c9 48       .H             ; Offset >= &48? (6 handles max)
    bcc return_calc_handle                                            ; 8dc4: 90 03       ..             ; Valid: return with C clear
    ldy #0                                                            ; 8dc6: a0 00       ..             ; Invalid: Y = 0
    tya                                                               ; 8dc8: 98          .              ; A = 0, C set (error); A=&00
; &8dc9 referenced 1 time by &8dc4
.return_calc_handle
    rts                                                               ; 8dc9: 60          `              ; Return after calculation

; ***************************************************************************************
; *NET2: read handle entry from workspace
; 
; Looks up the handle in &F0 via calc_handle_offset. If the
; workspace slot contains &3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears rom_svc_num on exit.
; ***************************************************************************************
.net_2_read_handle_entry
    lda osword_pb_ptr                                                 ; 8dca: a5 f0       ..             ; Load handle number from &F0
    jsr calc_handle_offset                                            ; 8dcc: 20 b8 8d     ..            ; Look up handle &F0 in workspace
    bcs rxpol2                                                        ; 8dcf: b0 06       ..             ; Invalid handle: return 0
    lda (nfs_workspace),y                                             ; 8dd1: b1 9e       ..             ; Load stored handle value
    cmp #&3f ; '?'                                                    ; 8dd3: c9 3f       .?             ; &3F = unused/closed slot marker
    bne store_handle_return                                           ; 8dd5: d0 02       ..             ; Slot in use: return actual value
; &8dd7 referenced 2 times by &8dcf, &8de5
.rxpol2
    lda #0                                                            ; 8dd7: a9 00       ..             ; Return 0 for closed/invalid handle
; &8dd9 referenced 1 time by &8dd5
.store_handle_return
    sta osword_pb_ptr                                                 ; 8dd9: 85 f0       ..             ; Store result back to &F0
; &8ddb referenced 3 times by &8db6, &8df1, &8df6
.clear_svc_return
    lda #0                                                            ; 8ddb: a9 00       ..             ; A=0: clear service claim
    sta rom_svc_num                                                   ; 8ddd: 85 ce       ..             ; Release ROM service number
    rts                                                               ; 8ddf: 60          `              ; Return to caller

; ***************************************************************************************
; *NET3: close handle (mark as unused)
; 
; Looks up the handle in &F0 via calc_handle_offset. Writes
; &3F ('?') to mark the handle slot as closed in the NFS
; workspace. Preserves the carry flag state across the write
; using ROL/ROR on rx_status_flags. Clears rom_svc_num on exit.
; ***************************************************************************************
.net_3_close_handle
    lda osword_pb_ptr                                                 ; 8de0: a5 f0       ..             ; Load handle number from &F0
    jsr calc_handle_offset                                            ; 8de2: 20 b8 8d     ..            ; Look up handle &F0 in workspace
    bcs rxpol2                                                        ; 8de5: b0 f0       ..             ; Invalid handle: return 0
    rol rx_status_flags                                               ; 8de7: 2e 38 0d    .8.            ; Preserve carry via ROL
    lda #&3f ; '?'                                                    ; 8dea: a9 3f       .?             ; A=&3F: handle closed/unused marker
    sta (nfs_workspace),y                                             ; 8dec: 91 9e       ..             ; Mark handle as closed in workspace
; ***************************************************************************************
; Restore RX flags after close handle
; 
; Performs ROR on rx_flags to restore the carry flag state
; that was preserved by the matching ROL in net_3_close_handle.
; Falls through to osword_12_handler (clearing fs_temp_ce).
; ***************************************************************************************
.restore_rx_flags
    ror rx_status_flags                                               ; 8dee: 6e 38 0d    n8.            ; Restore carry via ROR
    bcc clear_svc_return                                              ; 8df1: 90 e8       ..             ; C=0: branch to cleanup exit
; ***************************************************************************************
; *NET4: resume after remote operation
; 
; Calls resume_after_remote (&8146) to re-enable the keyboard
; and send a completion notification. The BVC always branches
; to clear_svc_return since resume_after_remote
; returns with V clear (from CLV in prepare_cmd_clv).
; ***************************************************************************************
.net_4_resume_remote
    jsr resume_after_remote                                           ; 8df3: 20 46 81     F.            ; Jump to clear_svc_restore_args
    bvc clear_svc_return                                              ; 8df6: 50 e3       P.             ; V always clear: branch to cleanup exit
; ***************************************************************************************
; Filing system OSWORD entry
; 
; Subtracts &0F from the command code in &EF, giving a 0-4 index
; for OSWORD calls &0F-&13 (15-19). Falls through to the
; PHA/PHA/RTS dispatch at &8E02.
; ***************************************************************************************
.svc_8_osword
    lda osbyte_a_copy                                                 ; 8df8: a5 ef       ..             ; Command code from &EF
    sbc #&0f                                                          ; 8dfa: e9 0f       ..             ; Subtract &0F: OSWORD &0F-&13 become indices 0-4
    bmi return_copy_param                                             ; 8dfc: 30 35       05             ; Outside our OSWORD range, exit
    cmp #5                                                            ; 8dfe: c9 05       ..             ; Only OSWORDs &0F-&13 (index 0-4)
    bcs return_copy_param                                             ; 8e00: b0 31       .1             ; Index >= 5: not ours, return
; ***************************************************************************************
; PHA/PHA/RTS dispatch for filing system OSWORDs
; 
; X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
; at &8E19 (low) / &8E1E (high).
; ***************************************************************************************
.fs_osword_dispatch
    tax                                                               ; 8e02: aa          .              ; X = sub-function code for table lookup
    lda fs_osword_tbl_hi,x                                            ; 8e03: bd 1e 8e    ...            ; Load handler address high byte from table
    pha                                                               ; 8e06: 48          H              ; Push high byte for RTS dispatch
    lda fs_osword_tbl_lo,x                                            ; 8e07: bd 19 8e    ...            ; Load handler address low byte from table
    pha                                                               ; 8e0a: 48          H              ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
    ldy #2                                                            ; 8e0b: a0 02       ..             ; Y=2: save 3 bytes (&AA-&AC)
; &8e0d referenced 1 time by &8e13
.save1
    lda fs_last_byte_flag,y                                           ; 8e0d: b9 bd 00    ...            ; Load param block pointer byte
    sta (net_rx_ptr),y                                                ; 8e10: 91 9c       ..             ; Save to NFS workspace via (net_rx_ptr)
    dey                                                               ; 8e12: 88          .              ; Next byte (descending)
    bpl save1                                                         ; 8e13: 10 f8       ..             ; Loop for all 3 bytes
    iny                                                               ; 8e15: c8          .              ; Y=0 after BPL exit; INY makes Y=1
    lda (osword_pb_ptr),y                                             ; 8e16: b1 f0       ..             ; Read sub-function code from (&F0)+1
    rts                                                               ; 8e18: 60          `              ; RTS dispatches to pushed handler

; &8e19 referenced 1 time by &8e07
.fs_osword_tbl_lo
    equb <(osword_0f_handler-1)                                       ; 8e19: 33          3              ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
    equb <(osword_10_handler-1)                                       ; 8e1a: f0          .
    equb <(osword_11_handler-1)                                       ; 8e1b: 53          S
    equb <(osword_12_handler-1)                                       ; 8e1c: 7b          {
    equb <(econet_tx_rx-1)                                            ; 8e1d: 72          r
; &8e1e referenced 1 time by &8e03
.fs_osword_tbl_hi
    equb >(osword_0f_handler-1)                                       ; 8e1e: 8e          .              ; Dispatch table: high bytes for OSWORD &0F-&13 handlers
    equb >(osword_10_handler-1)                                       ; 8e1f: 8e          .
    equb >(osword_11_handler-1)                                       ; 8e20: 8e          .
    equb >(osword_12_handler-1)                                       ; 8e21: 8e          .
    equb >(econet_tx_rx-1)                                            ; 8e22: 8f          .

; ***************************************************************************************
; Bidirectional block copy between OSWORD param block and workspace.
; 
; C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
; C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)
; ***************************************************************************************
; &8e23 referenced 5 times by &8e31, &8e47, &8e63, &8e97, &8f32
.copy_param_block
    bcc load_workspace_byte                                           ; 8e23: 90 06       ..             ; C=0: workspace to param direction
    lda (osword_pb_ptr),y                                             ; 8e25: b1 f0       ..             ; Load byte from param block
    sta (fs_crc_lo),y                                                 ; 8e27: 91 be       ..             ; Store to workspace
    bcs copyl3                                                        ; 8e29: b0 04       ..             ; Always taken (C still set); ALWAYS branch

; &8e2b referenced 1 time by &8e23
.load_workspace_byte
    lda (fs_crc_lo),y                                                 ; 8e2b: b1 be       ..             ; Load byte from workspace
    sta (osword_pb_ptr),y                                             ; 8e2d: 91 f0       ..             ; Store to param block (no-op if C=1)
; &8e2f referenced 1 time by &8e29
.copyl3
    iny                                                               ; 8e2f: c8          .              ; Advance to next byte
    dex                                                               ; 8e30: ca          .              ; Decrement byte counter
    bpl copy_param_block                                              ; 8e31: 10 f0       ..             ; Loop while X >= 0
; &8e33 referenced 2 times by &8dfc, &8e00
.return_copy_param
    rts                                                               ; 8e33: 60          `              ; Return after copy

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
    asl tx_ctrl_status                                                ; 8e34: 0e 3a 0d    .:.            ; ASL: set C if TX in progress
    bcc osword_12_subfunc                                             ; 8e37: 90 17       ..             ; C=0: read path
    lda net_rx_ptr_hi                                                 ; 8e39: a5 9d       ..             ; User TX CB in workspace page (high byte)
    sta fs_crc_hi                                                     ; 8e3b: 85 bf       ..             ; Set param block high byte
    sta nmi_tx_block_hi                                               ; 8e3d: 85 a1       ..             ; Set LTXCBP high byte for low-level TX
    lda #&6f ; 'o'                                                    ; 8e3f: a9 6f       .o             ; &6F: offset into workspace for user TXCB
    sta fs_crc_lo                                                     ; 8e41: 85 be       ..             ; Set param block low byte
    sta nmi_tx_block                                                  ; 8e43: 85 a0       ..             ; Set LTXCBP low byte for low-level TX
    ldx #&0f                                                          ; 8e45: a2 0f       ..             ; X=15: copy 16 bytes (OSWORD param block)
    jsr copy_param_block                                              ; 8e47: 20 23 8e     #.            ; Copy param block to user TX control block
    jsr trampoline_tx_setup                                           ; 8e4a: 20 60 96     `.            ; Set up and start low-level transmit
    jmp clear_svc_restore_args                                        ; 8e4d: 4c 49 8f    LI.            ; Exit: release service claim

; &8e50 referenced 1 time by &8e37
.osword_12_subfunc
    sec                                                               ; 8e50: 38          8              ; SEC: alternate entry for OSWORD &11
    tya                                                               ; 8e51: 98          .              ; A = param block high for branch
    bcs readry                                                        ; 8e52: b0 22       ."             ; ALWAYS branch

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
    lda net_rx_ptr_hi                                                 ; 8e54: a5 9d       ..             ; Set source high byte from workspace page
    sta fs_crc_hi                                                     ; 8e56: 85 bf       ..             ; Store as copy source high byte in &BF
    ldy #&7f                                                          ; 8e58: a0 7f       ..             ; JSRSIZ at workspace offset &7F
    lda (net_rx_ptr),y                                                ; 8e5a: b1 9c       ..             ; Load buffer size from workspace
    iny                                                               ; 8e5c: c8          .              ; Y=&80: start of JSR argument data; Y=&80
    sty fs_crc_lo                                                     ; 8e5d: 84 be       ..             ; Store &80 as copy source low byte
    tax                                                               ; 8e5f: aa          .              ; X = buffer size (loop counter)
    dex                                                               ; 8e60: ca          .              ; X = size-1 (0-based count for copy)
    ldy #0                                                            ; 8e61: a0 00       ..             ; Y=0: start of destination param block
    jsr copy_param_block                                              ; 8e63: 20 23 8e     #.            ; Copy X+1 bytes from workspace to param
    jsr clear_jsr_protection                                          ; 8e66: 20 d7 92     ..            ; Reset JSR protection status
    bcc set_carry_dispatch                                            ; 8e69: 90 42       .B             ; Branch to set carry and dispatch
; &8e6b referenced 1 time by &8ebe
.read_args_size
    ldy #&7f                                                          ; 8e6b: a0 7f       ..             ; Y=&7F: JSRSIZ offset (READRB entry)
    lda (net_rx_ptr),y                                                ; 8e6d: b1 9c       ..             ; Load buffer size from workspace
    ldy #1                                                            ; 8e6f: a0 01       ..             ; Y=1: param block offset for size byte
    sta (osword_pb_ptr),y                                             ; 8e71: 91 f0       ..             ; Store buffer size to (&F0)+1
    iny                                                               ; 8e73: c8          .              ; Y=2: param block offset for args size; Y=&02
    lda #&80                                                          ; 8e74: a9 80       ..             ; A=&80: argument data starts at offset &80
; &8e76 referenced 1 time by &8e52
.readry
    sta (osword_pb_ptr),y                                             ; 8e76: 91 f0       ..             ; Store args start offset to (&F0)+2
    bcs carry_exit_or_read                                            ; 8e78: b0 68       .h             ; Always taken (SEC set above)
; &8e7a referenced 1 time by &8e8e
.osword_12_ws_offsets
    equb &ff, 1                                                       ; 8e7a: ff 01       ..

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
.osword_12_handler
    cmp #6                                                            ; 8e7c: c9 06       ..             ; Sub-function >= 6? (handle ops)
    bcs rsl1                                                          ; 8e7e: b0 38       .8             ; Sub >= 6: handle/station/error
    cmp #4                                                            ; 8e80: c9 04       ..             ; Sub-function >= 4? (protection)
    bcs rssl1                                                         ; 8e82: b0 18       ..             ; Sub-function 4 or 5: read/set protection
    lsr a                                                             ; 8e84: 4a          J              ; LSR: 0->0, 1->0, 2->1, 3->1
    ldx #&0d                                                          ; 8e85: a2 0d       ..             ; X=&0D: default to static workspace page
    tay                                                               ; 8e87: a8          .              ; Transfer LSR result to Y for indexing
    beq set_workspace_page                                            ; 8e88: f0 02       ..             ; Y=0 (sub 0-1): use page &0D
    ldx nfs_workspace_hi                                              ; 8e8a: a6 9f       ..             ; Y=1 (sub 2-3): use dynamic workspace
; &8e8c referenced 1 time by &8e88
.set_workspace_page
    stx fs_crc_hi                                                     ; 8e8c: 86 bf       ..             ; Store workspace page in &BF (hi byte)
    lda osword_12_ws_offsets,y                                        ; 8e8e: b9 7a 8e    .z.            ; Load offset: &FF (sub 0-1) or &01 (sub 2-3)
    sta fs_crc_lo                                                     ; 8e91: 85 be       ..             ; Store offset in &BE (lo byte)
    ldx #1                                                            ; 8e93: a2 01       ..             ; X=1: copy 2 bytes
    ldy #1                                                            ; 8e95: a0 01       ..             ; Y=1: start at param block offset 1
    jsr copy_param_block                                              ; 8e97: 20 23 8e     #.            ; Copy station bytes to/from workspace
    bne set_carry_dispatch                                            ; 8e9a: d0 11       ..             ; Always taken (Y=2 after copy)
; &8e9c referenced 1 time by &8e82
.rssl1
    lsr a                                                             ; 8e9c: 4a          J              ; LSR A: test bit 0 of sub-function
    iny                                                               ; 8e9d: c8          .              ; Y=1: offset for protection byte
    lda (osword_pb_ptr),y                                             ; 8e9e: b1 f0       ..             ; Load protection byte from param block
    bcs rssl2                                                         ; 8ea0: b0 05       ..             ; C=1 (odd sub): set protection
    lda prot_status                                                   ; 8ea2: ad 63 0d    .c.            ; C=0 (even sub): read current status
    sta (osword_pb_ptr),y                                             ; 8ea5: 91 f0       ..             ; Return current value to param block
; &8ea7 referenced 1 time by &8ea0
.rssl2
    sta prot_status                                                   ; 8ea7: 8d 63 0d    .c.            ; Update protection status
    sta rx_ctrl_copy                                                  ; 8eaa: 8d 3b 0d    .;.            ; Also save as JSR mask backup
; &8ead referenced 2 times by &8e69, &8e9a
.set_carry_dispatch
    sec                                                               ; 8ead: 38          8              ; SEC: set carry for exit
    bcs carry_exit_or_read                                            ; 8eae: b0 32       .2             ; ALWAYS branch

; &8eb0 referenced 1 time by &8eba
.read_local_station
    lda tx_clear_flag                                                 ; 8eb0: ad 62 0d    .b.            ; Load local station number
    iny                                                               ; 8eb3: c8          .              ; Y=1: param block offset for result
    sta (osword_pb_ptr),y                                             ; 8eb4: 91 f0       ..             ; Return station number to caller
    bcs carry_exit_or_read                                            ; 8eb6: b0 2a       .*             ; Always taken (C set above)
; &8eb8 referenced 1 time by &8e7e
.rsl1
    cmp #8                                                            ; 8eb8: c9 08       ..             ; Sub-function 8: read FS handle
    beq read_local_station                                            ; 8eba: f0 f4       ..             ; Match: read handle from RX buffer
    cmp #9                                                            ; 8ebc: c9 09       ..             ; Sub-function 9: read args size
    beq read_args_size                                                ; 8ebe: f0 ab       ..             ; Match: read ARGS buffer info
    bpl osword_12_error                                               ; 8ec0: 10 1a       ..             ; Sub >= 10 (bit 7 clear): read error
    ldy #3                                                            ; 8ec2: a0 03       ..             ; Y=3: start from handle 3 (descending)
    lsr a                                                             ; 8ec4: 4a          J              ; LSR: test read/write bit
    bcc readc1                                                        ; 8ec5: 90 1d       ..             ; C=0: read handles from workspace
    sty nfs_temp                                                      ; 8ec7: 84 cd       ..             ; Init loop counter at Y=3
; &8ec9 referenced 1 time by &8ed8
.copy_handles_to_ws
    ldy nfs_temp                                                      ; 8ec9: a4 cd       ..             ; Reload loop counter
    lda (osword_pb_ptr),y                                             ; 8ecb: b1 f0       ..             ; Read handle from caller's param block
    jsr handle_to_mask_a                                              ; 8ecd: 20 89 85     ..            ; Convert handle number to bitmask
    tya                                                               ; 8ed0: 98          .              ; TYA: get bitmask result
    ldy nfs_temp                                                      ; 8ed1: a4 cd       ..             ; Reload loop counter
    sta fs_server_net,y                                               ; 8ed3: 99 01 0e    ...            ; Store bitmask to FS server table
    dec nfs_temp                                                      ; 8ed6: c6 cd       ..             ; Next handle (descending)
    bne copy_handles_to_ws                                            ; 8ed8: d0 ef       ..             ; Loop for handles 3,2,1
    beq clear_svc_restore_args                                        ; 8eda: f0 6d       .m             ; ALWAYS branch

; &8edc referenced 1 time by &8ec0
.osword_12_error
    iny                                                               ; 8edc: c8          .              ; Y=1: param block offset for error
    lda fs_last_error                                                 ; 8edd: ad 09 0e    ...            ; Load last FS error number
    sta (osword_pb_ptr),y                                             ; 8ee0: 91 f0       ..             ; Return error code to caller
; &8ee2 referenced 3 times by &8e78, &8eae, &8eb6
.carry_exit_or_read
    bcs clear_svc_restore_args                                        ; 8ee2: b0 65       .e             ; Exit with carry set
; &8ee4 referenced 2 times by &8ec5, &8eed
.readc1
    lda fs_server_net,y                                               ; 8ee4: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8ee7: 20 a6 85     ..            ; Convert bitmask to handle number (FS2A)
    sta (osword_pb_ptr),y                                             ; 8eea: 91 f0       ..             ; A=handle number (&20-&27); Y=preserved
    dey                                                               ; 8eec: 88          .              ; Next handle (descending); Y=parameter block address high byte
    bne readc1                                                        ; 8eed: d0 f5       ..             ; Loop for handles 3,2,1
    beq clear_svc_restore_args                                        ; 8eef: f0 58       .X             ; ALWAYS branch

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
    ldx nfs_workspace_hi                                              ; 8ef1: a6 9f       ..             ; Workspace page high byte
    stx fs_crc_hi                                                     ; 8ef3: 86 bf       ..             ; Set up pointer high byte in &AC
    sty fs_crc_lo                                                     ; 8ef5: 84 be       ..             ; Save param block high byte in &AB
    ror rx_status_flags                                               ; 8ef7: 6e 38 0d    n8.            ; Disable user RX during CB operation
    lda (osword_pb_ptr),y                                             ; 8efa: b1 f0       ..             ; Read first byte of param block
    sta fs_last_byte_flag                                             ; 8efc: 85 bd       ..             ; Save: 0=open new, non-zero=read RXCB
.scan_or_read_rxcb
post_reply_check = scan_or_read_rxcb+1
    bne read_rxcb                                                     ; 8efe: d0 1b       ..             ; Non-zero: read specified RXCB
    lda #3                                                            ; 8f00: a9 03       ..             ; Start scan from RXCB #3 (0-2 reserved)
; &8f02 referenced 1 time by &8f14
.scan0
    jsr calc_handle_offset                                            ; 8f02: 20 b8 8d     ..            ; Convert RXCB number to workspace offset
    bcs openl4                                                        ; 8f05: b0 3d       .=             ; Invalid RXCB: return zero
    lsr a                                                             ; 8f07: 4a          J              ; LSR twice: byte offset / 4
    lsr a                                                             ; 8f08: 4a          J              ; Yields RXCB number from offset
    tax                                                               ; 8f09: aa          .              ; X = RXCB number for iteration
    lda (fs_crc_lo),y                                                 ; 8f0a: b1 be       ..             ; Read flag byte from RXCB workspace
    beq openl4                                                        ; 8f0c: f0 36       .6             ; Zero = end of CB list
    cmp #&3f ; '?'                                                    ; 8f0e: c9 3f       .?             ; &3F = deleted slot, free for reuse
    beq scan1                                                         ; 8f10: f0 04       ..             ; Found free slot
    inx                                                               ; 8f12: e8          .              ; Try next RXCB
    txa                                                               ; 8f13: 8a          .              ; A = next RXCB number
    bne scan0                                                         ; 8f14: d0 ec       ..             ; Continue scan (always branches)
; &8f16 referenced 1 time by &8f10
.scan1
    txa                                                               ; 8f16: 8a          .              ; A = free RXCB number
    ldx #0                                                            ; 8f17: a2 00       ..             ; X=0 for indexed indirect store
    sta (osword_pb_ptr,x)                                             ; 8f19: 81 f0       ..             ; Return RXCB number to caller's byte 0
; &8f1b referenced 1 time by &8efe
.read_rxcb
    jsr calc_handle_offset                                            ; 8f1b: 20 b8 8d     ..            ; Convert RXCB number to workspace offset
    bcs openl4                                                        ; 8f1e: b0 24       .$             ; Invalid: write zero to param block
    dey                                                               ; 8f20: 88          .              ; Y = offset-1: points to flag byte
    sty fs_crc_lo                                                     ; 8f21: 84 be       ..             ; Set &AB = workspace ptr low byte
    lda #&c0                                                          ; 8f23: a9 c0       ..             ; &C0: test mask for flag byte
    ldy #1                                                            ; 8f25: a0 01       ..             ; Y=1: flag byte offset in RXCB
    ldx #&0b                                                          ; 8f27: a2 0b       ..             ; Enable interrupts before transmit
    cpy fs_last_byte_flag                                             ; 8f29: c4 bd       ..             ; Compare Y(1) with saved byte (open/read)
    adc (fs_crc_lo),y                                                 ; 8f2b: 71 be       q.             ; ADC flag: test if slot is in use
    beq openl6                                                        ; 8f2d: f0 03       ..             ; Dest station = &FFFF (accept reply from any station)
    bmi openl7                                                        ; 8f2f: 30 0e       0.             ; Negative: slot has received data
; &8f31 referenced 1 time by &8f41
.copy_rxcb_to_param
    clc                                                               ; 8f31: 18          .              ; C=0: workspace-to-param direction
; &8f32 referenced 1 time by &8f2d
.openl6
    jsr copy_param_block                                              ; 8f32: 20 23 8e     #.            ; Copy RXCB data to param block
    bcs reenable_rx                                                   ; 8f35: b0 0f       ..             ; Done: skip deletion on error
    lda #&3f ; '?'                                                    ; 8f37: a9 3f       .?             ; Mark CB as consumed (consume-once)
    ldy #1                                                            ; 8f39: a0 01       ..             ; Y=1: flag byte offset
    sta (fs_crc_lo),y                                                 ; 8f3b: 91 be       ..             ; Write &3F to mark slot deleted
    bne reenable_rx                                                   ; 8f3d: d0 07       ..             ; Branch to exit (always taken); ALWAYS branch

; &8f3f referenced 1 time by &8f2f
.openl7
    adc #1                                                            ; 8f3f: 69 01       i.             ; Advance through multi-byte field
    bne copy_rxcb_to_param                                            ; 8f41: d0 ee       ..             ; Loop until all bytes processed
    dey                                                               ; 8f43: 88          .              ; Y=-1 → Y=0 after STA below
; &8f44 referenced 3 times by &8f05, &8f0c, &8f1e
.openl4
    sta (osword_pb_ptr),y                                             ; 8f44: 91 f0       ..             ; Return zero (no free RXCB found)
; &8f46 referenced 2 times by &8f35, &8f3d
.reenable_rx
    rol rx_status_flags                                               ; 8f46: 2e 38 0d    .8.            ; Re-enable user RX
; ***************************************************************************************
; Clear service number and restore OSWORD args
; 
; Shared exit for OSWORD handlers. Zeros rom_svc_num to
; release the service claim, then copies 3 bytes from
; (net_rx_ptr) back to the fs_last_byte_flag area,
; restoring the OSWORD argument state saved at entry.
; ***************************************************************************************
; &8f49 referenced 6 times by &8e4d, &8eda, &8ee2, &8eef, &8fbf, &9005
.clear_svc_restore_args
    ldy #0                                                            ; 8f49: a0 00       ..             ; Y=0: clear service claim
    sty rom_svc_num                                                   ; 8f4b: 84 ce       ..             ; Release ROM service number
    ldy #2                                                            ; 8f4d: a0 02       ..             ; Y=2: copy 3 bytes (indices 2,1,0)
; &8f4f referenced 1 time by &8f55
.rest1
    lda (net_rx_ptr),y                                                ; 8f4f: b1 9c       ..             ; Load saved arg from (net_rx_ptr)+Y
    sta fs_last_byte_flag,y                                           ; 8f51: 99 bd 00    ...            ; Restore saved OSWORD argument byte
    dey                                                               ; 8f54: 88          .              ; Decrement byte counter
    bpl rest1                                                         ; 8f55: 10 f8       ..             ; Loop for bytes 2,1,0
    rts                                                               ; 8f57: 60          `              ; Return to caller

; ***************************************************************************************
; Set up RX buffer pointers in NFS workspace
; 
; Calculates the start address of the RX data area (&F0+1) and stores
; it at workspace offset &28. Also reads the data length from (&F0)+1
; and adds it to &F0 to compute the end address at offset &2C.
; 
; On Entry:
;     C: clear for ADC
; ***************************************************************************************
; &8f58 referenced 1 time by &8f8b
.setup_rx_buffer_ptrs
    ldy #&28 ; '('                                                    ; 8f58: a0 28       .(             ; Y=&28: RXCB template offset
    lda osword_pb_ptr                                                 ; 8f5a: a5 f0       ..             ; A = base address low byte
    adc #1                                                            ; 8f5c: 69 01       i.             ; A = base + 1 (skip length byte)
    jsr store_16bit_at_y                                              ; 8f5e: 20 69 8f     i.            ; Receive data blocks until command byte = &00 or &0D
    ldy #1                                                            ; 8f61: a0 01       ..             ; Read data length from (&F0)+1
    lda (osword_pb_ptr),y                                             ; 8f63: b1 f0       ..             ; A = data length byte
    ldy #&2c ; ','                                                    ; 8f65: a0 2c       .,             ; Workspace offset &20 = RX data end
    adc osword_pb_ptr                                                 ; 8f67: 65 f0       e.             ; A = base + length = end address low
; &8f69 referenced 1 time by &8f5e
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8f69: 91 9e       ..             ; Store low byte of 16-bit address
    iny                                                               ; 8f6b: c8          .              ; Advance to high byte offset
    lda osword_pb_ptr_hi                                              ; 8f6c: a5 f1       ..             ; A = high byte of base address
    adc #0                                                            ; 8f6e: 69 00       i.             ; Add carry for 16-bit addition
    sta (nfs_workspace),y                                             ; 8f70: 91 9e       ..             ; Store high byte
    rts                                                               ; 8f72: 60          `              ; Return

; ***************************************************************************************
; Econet transmit/receive handler
; 
; A=0: Initialise TX control block from ROM template at &8311
;      (zero entries substituted from NMI workspace &0DDA), transmit
;      it, set up RX control block, and receive reply.
; A>=1: Handle transmit result (branch to cleanup at &8F49).
; 
; On Entry:
;     A: 0=set up and transmit, >=1=handle TX result
; ***************************************************************************************
.econet_tx_rx
    cmp #1                                                            ; 8f73: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs handle_tx_result                                              ; 8f75: b0 4a       .J             ; A >= 1: handle TX result
    ldy #&2f ; '/'                                                    ; 8f77: a0 2f       ./             ; Y=&2F: start of template (descending)
; &8f79 referenced 1 time by &8f86
.dofs01
    lda init_tx_ctrl_port,y                                           ; 8f79: b9 11 83    ...            ; Load from ROM template (zero = use NMI workspace value)
    bne store_txcb_byte                                               ; 8f7c: d0 03       ..             ; Non-zero = use ROM template byte as-is
    lda l0dda,y                                                       ; 8f7e: b9 da 0d    ...            ; Zero = substitute from NMI workspace
; &8f81 referenced 1 time by &8f7c
.store_txcb_byte
    sta (nfs_workspace),y                                             ; 8f81: 91 9e       ..             ; Store to dynamic workspace
    dey                                                               ; 8f83: 88          .              ; Descend through template
    cpy #&23 ; '#'                                                    ; 8f84: c0 23       .#             ; Stop at offset &17
    bne dofs01                                                        ; 8f86: d0 f1       ..             ; Loop until all bytes copied
    iny                                                               ; 8f88: c8          .              ; Y=&18: TX block starts here
    sty net_tx_ptr                                                    ; 8f89: 84 9a       ..             ; Point net_tx_ptr at workspace+&18
    jsr setup_rx_buffer_ptrs                                          ; 8f8b: 20 58 8f     X.            ; Set up RX buffer start/end pointers
    ldy #2                                                            ; 8f8e: a0 02       ..             ; Y=2: port byte offset in RXCB
    lda #&90                                                          ; 8f90: a9 90       ..             ; A=&90: FS reply port
    sta (osword_pb_ptr),y                                             ; 8f92: 91 f0       ..             ; Store port &90 at (&F0)+2
    iny                                                               ; 8f94: c8          .              ; Y=&03
    iny                                                               ; 8f95: c8          .              ; Y=&04: advance to station address; Y=&04
; &8f96 referenced 1 time by &8f9e
.copy_fs_addr
    lda fs_context_base,y                                             ; 8f96: b9 fe 0d    ...            ; Copy FS station addr from workspace
    sta (osword_pb_ptr),y                                             ; 8f99: 91 f0       ..             ; Store to RX param block
    iny                                                               ; 8f9b: c8          .              ; Next byte
    cpy #7                                                            ; 8f9c: c0 07       ..             ; Done 3 bytes (Y=4,5,6)?
    bne copy_fs_addr                                                  ; 8f9e: d0 f6       ..             ; No: continue copying
    lda nfs_workspace_hi                                              ; 8fa0: a5 9f       ..             ; High byte of workspace for TX ptr
    sta net_tx_ptr_hi                                                 ; 8fa2: 85 9b       ..             ; Store as TX pointer high byte
    cli                                                               ; 8fa4: 58          X              ; Enable interrupts before transmit
    jsr tx_poll_timeout                                               ; 8fa5: 20 4f 86     O.            ; Transmit with full retry
    ldy #&2c ; ','                                                    ; 8fa8: a0 2c       .,             ; Y=&2C: RX end address offset
    lda #&ff                                                          ; 8faa: a9 ff       ..             ; Dest station = &FFFF (accept reply from any station)
    sta (nfs_workspace),y                                             ; 8fac: 91 9e       ..             ; Store end address low byte (&FF)
    iny                                                               ; 8fae: c8          .              ; Y=&2d
    sta (nfs_workspace),y                                             ; 8faf: 91 9e       ..             ; Store end address high byte (&FF)
    ldy #&25 ; '%'                                                    ; 8fb1: a0 25       .%             ; Y=&25: port byte in workspace RXCB
    lda #&90                                                          ; 8fb3: a9 90       ..             ; A=&90: FS reply port
    sta (nfs_workspace),y                                             ; 8fb5: 91 9e       ..             ; Store port to workspace RXCB
    dey                                                               ; 8fb7: 88          .              ; Y=&24
    lda #&7f                                                          ; 8fb8: a9 7f       ..             ; A=&7F: flag byte = waiting for reply
    sta (nfs_workspace),y                                             ; 8fba: 91 9e       ..             ; Store flag byte to workspace RXCB
    jsr send_to_fs_star                                               ; 8fbc: 20 49 84     I.            ; Initiate receive with timeout
    bne clear_svc_restore_args                                        ; 8fbf: d0 88       ..             ; Non-zero = error/timeout: jump to cleanup
; &8fc1 referenced 1 time by &8f75
.handle_tx_result
    php                                                               ; 8fc1: 08          .              ; Save processor flags
    ldy #1                                                            ; 8fc2: a0 01       ..             ; Y=1: first data byte offset
    lda (osword_pb_ptr),y                                             ; 8fc4: b1 f0       ..             ; Load first data byte from RX buffer
    tax                                                               ; 8fc6: aa          .              ; X = first data byte (command code)
    iny                                                               ; 8fc7: c8          .              ; Advance to next data byte; Y=&02
    lda (osword_pb_ptr),y                                             ; 8fc8: b1 f0       ..             ; Load station address high byte
    iny                                                               ; 8fca: c8          .              ; Advance past station addr; Y=&03
    sty fs_crc_lo                                                     ; 8fcb: 84 be       ..             ; Save Y as data index
    ldy #&72 ; 'r'                                                    ; 8fcd: a0 72       .r             ; Store station addr hi at (net_rx_ptr)+&72
    sta (net_rx_ptr),y                                                ; 8fcf: 91 9c       ..             ; Store to workspace
    dey                                                               ; 8fd1: 88          .              ; Y=&71
    txa                                                               ; 8fd2: 8a          .              ; A = command code (from X)
    sta (net_rx_ptr),y                                                ; 8fd3: 91 9c       ..             ; Store station addr lo at (net_rx_ptr)+&71
    plp                                                               ; 8fd5: 28          (              ; Restore flags from earlier PHP
    bne dofs2                                                         ; 8fd6: d0 1e       ..             ; First call: adjust data length
; &8fd8 referenced 1 time by &8ff2
.send_data_bytes
    ldy fs_crc_lo                                                     ; 8fd8: a4 be       ..             ; Receive data blocks until command byte = &00 or &0D
    inc fs_crc_lo                                                     ; 8fda: e6 be       ..             ; Advance data index for next iteration
    lda (osword_pb_ptr),y                                             ; 8fdc: b1 f0       ..             ; Load next data byte
    ldy #&7d ; '}'                                                    ; 8fde: a0 7d       .}             ; Y=&7D: store byte for TX at offset &7D
    sta (net_rx_ptr),y                                                ; 8fe0: 91 9c       ..             ; Store data byte at (net_rx_ptr)+&7D for TX
    pha                                                               ; 8fe2: 48          H              ; Save data byte for &0D check after TX
    jsr ctrl_block_setup_alt                                          ; 8fe3: 20 5a 91     Z.            ; Set up TX control block
    cli                                                               ; 8fe6: 58          X              ; Enable interrupts for TX
    jsr tx_poll_core                                                  ; 8fe7: 20 51 86     Q.            ; Enable IRQs and transmit; Core transmit and poll routine (XMIT)
; &8fea referenced 1 time by &8feb
.delay_between_tx
    dex                                                               ; 8fea: ca          .              ; Short delay loop between TX packets
    bne delay_between_tx                                              ; 8feb: d0 fd       ..             ; Spin until X reaches 0
    pla                                                               ; 8fed: 68          h              ; Restore data byte for terminator check
    beq rx_first_packet                                               ; 8fee: f0 04       ..             ; Z=1: not intercepted, pass through
    eor #&0d                                                          ; 8ff0: 49 0d       I.             ; Test for end-of-data marker (&0D)
    bne send_data_bytes                                               ; 8ff2: d0 e4       ..             ; Not &0D: continue with next byte
; &8ff4 referenced 1 time by &8fee
.rx_first_packet
    beq jmp_clear_svc_restore                                         ; 8ff4: f0 0f       ..             ; First packet: exit handler
; &8ff6 referenced 1 time by &8fd6
.dofs2
    jsr ctrl_block_setup_alt                                          ; 8ff6: 20 5a 91     Z.            ; First-packet: set up control block
    ldy #&7b ; '{'                                                    ; 8ff9: a0 7b       .{             ; Y=&7B: data length offset
    lda (net_rx_ptr),y                                                ; 8ffb: b1 9c       ..             ; Load current data length
    adc #3                                                            ; 8ffd: 69 03       i.             ; Adjust data length by 3 for header bytes
    sta (net_rx_ptr),y                                                ; 8fff: 91 9c       ..             ; Store adjusted length
; ***************************************************************************************
; Enable interrupts and transmit via tx_poll_ff
; 
; CLI to enable interrupts, then JMP tx_poll_ff. A short
; tail-call wrapper used after building the TX control block.
; ***************************************************************************************
.enable_irq_and_tx
    cli                                                               ; 9001: 58          X              ; Enable interrupts
    jsr tx_poll_ff                                                    ; 9002: 20 4d 86     M.            ; Poll TX until complete
; &9005 referenced 1 time by &8ff4
.jmp_clear_svc_restore
    jmp clear_svc_restore_args                                        ; 9005: 4c 49 8f    LI.            ; Transmit via tx_poll_ff

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
    php                                                               ; 9008: 08          .              ; Save processor status
    pha                                                               ; 9009: 48          H              ; Save A (reason code)
    txa                                                               ; 900a: 8a          .              ; Save X
    pha                                                               ; 900b: 48          H              ; Push X to stack
    tya                                                               ; 900c: 98          .              ; Save Y
    pha                                                               ; 900d: 48          H              ; Push Y to stack
    tsx                                                               ; 900e: ba          .              ; Get stack pointer for indexed access
    lda l0103,x                                                       ; 900f: bd 03 01    ...            ; Retrieve original A (function code) from stack
    cmp #9                                                            ; 9012: c9 09       ..             ; Reason codes 0-8 only
    bcs entry1                                                        ; 9014: b0 04       ..             ; Code >= 9: skip dispatch, restore regs
    tax                                                               ; 9016: aa          .              ; X = reason code for table lookup
    jsr osword_trampoline                                             ; 9017: 20 21 90     !.            ; Dispatch to handler via trampoline
; &901a referenced 1 time by &9014
.entry1
    pla                                                               ; 901a: 68          h              ; Restore Y
    tay                                                               ; 901b: a8          .              ; Transfer to Y register
    pla                                                               ; 901c: 68          h              ; Restore X
    tax                                                               ; 901d: aa          .              ; Transfer to X register
    pla                                                               ; 901e: 68          h              ; Restore A
    plp                                                               ; 901f: 28          (              ; Restore processor status flags
    rts                                                               ; 9020: 60          `              ; Return with all registers preserved

; &9021 referenced 1 time by &9017
.osword_trampoline
    lda osword_tbl_hi,x                                               ; 9021: bd 35 90    .5.            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 9024: 48          H              ; Push high byte of handler address
    lda osword_tbl_lo,x                                               ; 9025: bd 2c 90    .,.            ; Load handler low byte from table
    pha                                                               ; 9028: 48          H              ; Push low byte of handler address
    lda osbyte_a_copy                                                 ; 9029: a5 ef       ..             ; Load workspace byte &EF for handler
    rts                                                               ; 902b: 60          `              ; RTS dispatches to pushed handler

; &902c referenced 1 time by &9025
.osword_tbl_lo
    equb <(return_2-1)                                                ; 902c: 44          D
    equb <(remote_print_handler-1)                                    ; 902d: c7          .
    equb <(remote_print_handler-1)                                    ; 902e: c7          .
    equb <(remote_print_handler-1)                                    ; 902f: c7          .
    equb <(net_write_char-1)                                          ; 9030: 3d          =
    equb <(printer_select_handler-1)                                  ; 9031: b5          .
    equb <(return_2-1)                                                ; 9032: 44          D
    equb <(remote_cmd_dispatch-1)                                     ; 9033: 63          c
    equb <(remote_cmd_data-1)                                         ; 9034: cd          .
; &9035 referenced 1 time by &9021
.osword_tbl_hi
    equb >(return_2-1)                                                ; 9035: 81          .
    equb >(remote_print_handler-1)                                    ; 9036: 91          .
    equb >(remote_print_handler-1)                                    ; 9037: 91          .
    equb >(remote_print_handler-1)                                    ; 9038: 91          .
    equb >(net_write_char-1)                                          ; 9039: 90          .
    equb >(printer_select_handler-1)                                  ; 903a: 91          .
    equb >(return_2-1)                                                ; 903b: 81          .
    equb >(remote_cmd_dispatch-1)                                     ; 903c: 90          .
    equb >(remote_cmd_data-1)                                         ; 903d: 90          .

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
    tsx                                                               ; 903e: ba          .              ; Get stack pointer for flag access
    ror l0106,x                                                       ; 903f: 7e 06 01    ~..            ; ROR/ASL on stacked P: zeros carry to signal success
    asl l0106,x                                                       ; 9042: 1e 06 01    ...            ; ASL: restore P after ROR zeroed carry
    tya                                                               ; 9045: 98          .              ; Y = character to write
    ldy #&da                                                          ; 9046: a0 da       ..             ; Store character at workspace offset &DA
    sta (nfs_workspace),y                                             ; 9048: 91 9e       ..             ; Store char at workspace offset &DA
    lda #0                                                            ; 904a: a9 00       ..             ; A=0: command type for net write char
; ***************************************************************************************
; Set up TX control block and send
; 
; Builds a TX control block at (nfs_workspace)+&0C from the current
; workspace state, then initiates transmission via the ADLC TX path.
; This is the common send routine used after command data has been
; prepared. The exact control block layout and field mapping need
; further analysis.
; 
; On Entry:
;     A: command type byte
; ***************************************************************************************
; &904c referenced 3 times by &8159, &9093, &90f4
.setup_tx_and_send
    ldy #&d9                                                          ; 904c: a0 d9       ..             ; Y=&D9: command type offset
    sta (nfs_workspace),y                                             ; 904e: 91 9e       ..             ; Store command type at ws+&D9
    lda #&80                                                          ; 9050: a9 80       ..             ; Mark TX control block as active (&80)
    ldy #&0c                                                          ; 9052: a0 0c       ..             ; Y=&0C: TXCB start offset
    sta (nfs_workspace),y                                             ; 9054: 91 9e       ..             ; Set TX active flag at ws+&0C
    sty net_tx_ptr                                                    ; 9056: 84 9a       ..             ; Redirect net_tx_ptr low to workspace
    ldx nfs_workspace_hi                                              ; 9058: a6 9f       ..             ; Load workspace page high byte
    stx net_tx_ptr_hi                                                 ; 905a: 86 9b       ..             ; Complete ptr redirect
    jsr tx_poll_ff                                                    ; 905c: 20 4d 86     M.            ; Transmit with full retry
    lda #&3f ; '?'                                                    ; 905f: a9 3f       .?             ; Mark TXCB as deleted (&3F) after transmit
    sta (net_tx_ptr,x)                                                ; 9061: 81 9a       ..             ; Write &3F to TXCB byte 0
    rts                                                               ; 9063: 60          `              ; Return

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
    ldy osword_pb_ptr_hi                                              ; 9064: a4 f1       ..             ; Load original Y (OSBYTE secondary param)
    cmp #&81                                                          ; 9066: c9 81       ..             ; OSBYTE &81 (INKEY): always forward to terminal
    beq dispatch_remote_osbyte                                        ; 9068: f0 13       ..             ; Forward &81 to terminal for keyboard read
    ldy #1                                                            ; 906a: a0 01       ..             ; Y=1: search NCTBPL table (execute on both)
    ldx #7                                                            ; 906c: a2 07       ..             ; X=7: 8-entry NCTBPL table size
    jsr match_osbyte_code                                             ; 906e: 20 b6 90     ..            ; Search for OSBYTE code in NCTBPL table
    beq dispatch_remote_osbyte                                        ; 9071: f0 0a       ..             ; Match found: dispatch with Y=1 (both)
    dey                                                               ; 9073: 88          .              ; Y=-1: search NCTBMI table (terminal only)
    dey                                                               ; 9074: 88          .              ; Second DEY: Y=&FF (from 1 via 0)
    ldx #&0e                                                          ; 9075: a2 0e       ..             ; X=&0E: 15-entry NCTBMI table size
    jsr match_osbyte_code                                             ; 9077: 20 b6 90     ..            ; Search for OSBYTE code in NCTBMI table
    beq dispatch_remote_osbyte                                        ; 907a: f0 01       ..             ; Match found: dispatch with Y=&FF (terminal)
    iny                                                               ; 907c: c8          .              ; Y=0: OSBYTE not recognised, ignore
; &907d referenced 3 times by &9068, &9071, &907a
.dispatch_remote_osbyte
    ldx #2                                                            ; 907d: a2 02       ..             ; X=2 bytes to copy (default for RBYTE)
    tya                                                               ; 907f: 98          .              ; A=Y: check table match result
    beq return_nbyte                                                  ; 9080: f0 33       .3             ; Y=0: not recognised, return unhandled
    php                                                               ; 9082: 08          .              ; Y>0 (NCTBPL): send only, no result expected
    bpl nbyte6                                                        ; 9083: 10 01       ..             ; Y>0 (NCTBPL): no result expected, skip RX
    inx                                                               ; 9085: e8          .              ; Y<0 (NCTBMI): X=3 bytes (result + P flags); X=&03
; &9086 referenced 1 time by &9083
.nbyte6
    ldy #&dc                                                          ; 9086: a0 dc       ..             ; Y=&DC: top of 3-byte stack frame region
; &9088 referenced 1 time by &9090
.nbyte1
    lda tube_claimed_id,y                                             ; 9088: b9 15 00    ...            ; Copy OSBYTE args from stack frame to workspace
    sta (nfs_workspace),y                                             ; 908b: 91 9e       ..             ; Store to NFS workspace for transmission
    dey                                                               ; 908d: 88          .              ; Next byte (descending)
    cpy #&da                                                          ; 908e: c0 da       ..             ; Copied all 3 bytes? (&DC, &DB, &DA)
    bpl nbyte1                                                        ; 9090: 10 f6       ..             ; Loop for remaining bytes
    txa                                                               ; 9092: 8a          .              ; A = byte count for setup_tx_and_send
    jsr setup_tx_and_send                                             ; 9093: 20 4c 90     L.            ; Build TXCB and transmit to terminal
    plp                                                               ; 9096: 28          (              ; Restore N flag from table match type
    bpl return_nbyte                                                  ; 9097: 10 1c       ..             ; Y was positive (NCTBPL): done, no result
    lda #&7f                                                          ; 9099: a9 7f       ..             ; Set up RX control block to wait for reply
    sta (net_tx_ptr,x)                                                ; 909b: 81 9a       ..             ; Write &7F to RXCB (wait for reply)
; &909d referenced 1 time by &909f
.poll_rxcb_loop
    lda (net_tx_ptr,x)                                                ; 909d: a1 9a       ..             ; Poll RXCB for completion (bit7)
    bpl poll_rxcb_loop                                                ; 909f: 10 fc       ..             ; Bit7 clear: still waiting, poll again
    tsx                                                               ; 90a1: ba          .              ; X = stack pointer for register restoration
    ldy #&dd                                                          ; 90a2: a0 dd       ..             ; Y=&DD: saved P byte offset in workspace
    lda (nfs_workspace),y                                             ; 90a4: b1 9e       ..             ; Load remote processor status from reply
    ora #&44 ; 'D'                                                    ; 90a6: 09 44       .D             ; Force V=1 (claimed) and I=1 (no IRQ) in saved P
    bne nbyte5                                                        ; 90a8: d0 04       ..             ; ALWAYS branch (ORA #&44 never zero); ALWAYS branch

; &90aa referenced 1 time by &90b3
.nbyte4
    dey                                                               ; 90aa: 88          .              ; Previous workspace offset
    dex                                                               ; 90ab: ca          .              ; Previous stack register slot
    lda (nfs_workspace),y                                             ; 90ac: b1 9e       ..             ; Load next result byte (X, then Y)
; &90ae referenced 1 time by &90a8
.nbyte5
    sta l0106,x                                                       ; 90ae: 9d 06 01    ...            ; Write result bytes to stacked registers
    cpy #&da                                                          ; 90b1: c0 da       ..             ; Copied all result bytes? (P at &DA)
    bne nbyte4                                                        ; 90b3: d0 f5       ..             ; Loop for remaining result bytes
; &90b5 referenced 2 times by &9080, &9097
.return_nbyte
    rts                                                               ; 90b5: 60          `              ; Return to OSBYTE dispatcher

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
; &90b6 referenced 3 times by &906e, &9077, &90bc
.match_osbyte_code
    cmp remote_osbyte_table,x                                         ; 90b6: dd bf 90    ...            ; Compare OSBYTE code with table entry
    beq return_match_osbyte                                           ; 90b9: f0 03       ..             ; Match found: return with Z=1
    dex                                                               ; 90bb: ca          .              ; Next table entry (descending)
    bpl match_osbyte_code                                             ; 90bc: 10 f8       ..             ; Loop for remaining entries
; &90be referenced 1 time by &90b9
.return_match_osbyte
    rts                                                               ; 90be: 60          `              ; Return; Z=1 if match, Z=0 if not

; &90bf referenced 1 time by &90b6
.remote_osbyte_table
    equb 4                                                            ; 90bf: 04          .              ; OSBYTE &04: cursor key status
    equb 9                                                            ; 90c0: 09          .              ; OSBYTE &09: flash duration (1st colour)
    equb &0a                                                          ; 90c1: 0a          .              ; OSBYTE &0A: flash duration (2nd colour)
    equb &14                                                          ; 90c2: 14          .              ; OSBYTE &14: explode soft character RAM
    equb &9a                                                          ; 90c3: 9a          .              ; OSBYTE &9A: video ULA control register
    equb &9b                                                          ; 90c4: 9b          .              ; OSBYTE &9B: video ULA palette
    equb &9c                                                          ; 90c5: 9c          .              ; OSBYTE &9C: ACIA control register
    equb &e2                                                          ; 90c6: e2          .              ; OSBYTE &E2: function key &D0-&DF
    equb &0b                                                          ; 90c7: 0b          .              ; OSBYTE &0B: auto-repeat delay
    equb &0c                                                          ; 90c8: 0c          .              ; OSBYTE &0C: auto-repeat rate
    equb &0f                                                          ; 90c9: 0f          .              ; OSBYTE &0F: flush buffer class
    equb &79                                                          ; 90ca: 79          y              ; OSBYTE &79: keyboard scan from X
    equb &7a                                                          ; 90cb: 7a          z              ; OSBYTE &7A: keyboard scan from &10
    equb &e3                                                          ; 90cc: e3          .              ; OSBYTE &E3: function key &E0-&EF
    equb &e4                                                          ; 90cd: e4          .              ; OSBYTE &E4: function key &F0-&FF

; ***************************************************************************************
; Fn 8: remote OSWORD handler (NWORD)
; 
; Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
; envelope). Unlike NBYTE which returns results, NWORD is entirely
; fire-and-forget — no return path is implemented. The developer
; explicitly noted this was acceptable since sound/envelope commands
; don't return meaningful results. Copies up to 14 parameter bytes
; from the RX buffer to workspace, tags the message as RWORD, and
; transmits.
; ***************************************************************************************
.remote_cmd_data
    ldy #&0e                                                          ; 90ce: a0 0e       ..             ; Y=&0E: 14-byte parameter block
    cmp #7                                                            ; 90d0: c9 07       ..             ; OSWORD 7? (make sound)
    beq copy_params_rword                                             ; 90d2: f0 04       ..             ; OSWORD 7 (sound): handle via common path
    cmp #8                                                            ; 90d4: c9 08       ..             ; OSWORD 8 = define an envelope
    bne return_remote_cmd                                             ; 90d6: d0 24       .$             ; Not OSWORD 7 or 8: ignore (BNE exits)
; &90d8 referenced 1 time by &90d2
.copy_params_rword
    ldx #&db                                                          ; 90d8: a2 db       ..             ; Point workspace to offset &DB for params
    stx nfs_workspace                                                 ; 90da: 86 9e       ..             ; Store workspace ptr offset &DB
; &90dc referenced 1 time by &90e1
.copy_osword_params
    lda (osword_pb_ptr),y                                             ; 90dc: b1 f0       ..             ; Load param byte from OSWORD param block
    sta (nfs_workspace),y                                             ; 90de: 91 9e       ..             ; Write param byte to workspace
    dey                                                               ; 90e0: 88          .              ; Next byte (descending)
    bpl copy_osword_params                                            ; 90e1: 10 f9       ..             ; Loop for all parameter bytes
    iny                                                               ; 90e3: c8          .              ; Y=0 after loop
    dec nfs_workspace                                                 ; 90e4: c6 9e       ..             ; Point workspace to offset &DA
    lda osbyte_a_copy                                                 ; 90e6: a5 ef       ..             ; Load original OSWORD code
    sta (nfs_workspace),y                                             ; 90e8: 91 9e       ..             ; Store OSWORD code at ws+0
    sty nfs_workspace                                                 ; 90ea: 84 9e       ..             ; Reset workspace ptr to base
    ldy #&14                                                          ; 90ec: a0 14       ..             ; Y=&14: command type offset
    lda #&e9                                                          ; 90ee: a9 e9       ..             ; Tag as RWORD (port &E9)
    sta (nfs_workspace),y                                             ; 90f0: 91 9e       ..             ; Store port tag at ws+&14
    lda #1                                                            ; 90f2: a9 01       ..             ; A=1: single-byte TX
    jsr setup_tx_and_send                                             ; 90f4: 20 4c 90     L.            ; Set up TX and send RWORD packet
    stx nfs_workspace                                                 ; 90f7: 86 9e       ..             ; Restore workspace ptr
    jsr ctrl_block_setup_alt                                          ; 90f9: 20 5a 91     Z.            ; Set up control block for reply
; &90fc referenced 1 time by &90d6
.return_remote_cmd
    rts                                                               ; 90fc: 60          `              ; Return from remote command handler

; ***************************************************************************************
; Remote boot/execute handler
; 
; Validates byte 4 of the RX control block (must be zero), copies the
; 2-byte execution address from RX offsets &80/&81 into NFS workspace,
; sets up a control block, disables keyboard (OSBYTE &C9), then falls
; through to lang_3_execute_at_0100.
; ***************************************************************************************
.lang_1_remote_boot
    ldy #4                                                            ; 90fd: a0 04       ..             ; Y=4: RX control block byte 4
    lda (net_rx_ptr),y                                                ; 90ff: b1 9c       ..             ; Load first data byte from RX
    beq remot1                                                        ; 9101: f0 03       ..             ; Zero: standard boot, skip code
; &9103 referenced 1 time by &9149
.rchex
    jmp clear_jsr_protection                                          ; 9103: 4c d7 92    L..            ; Load language ROM number

; &9106 referenced 2 times by &9101, &913f
.remot1
    ora #9                                                            ; 9106: 09 09       ..             ; OR with 9: set remote boot bits
    sta (net_rx_ptr),y                                                ; 9108: 91 9c       ..             ; Store modified control byte
    ldx #&80                                                          ; 910a: a2 80       ..             ; X=&80: exec address offset lo
    ldy #&80                                                          ; 910c: a0 80       ..             ; Y=&80: exec address offset hi
    lda (net_rx_ptr),y                                                ; 910e: b1 9c       ..             ; Load exec address low byte
    pha                                                               ; 9110: 48          H              ; Save boot type on stack
    iny                                                               ; 9111: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 9112: b1 9c       ..             ; Load exec address high byte
    ldy #&0f                                                          ; 9114: a0 0f       ..             ; Y=&0F: workspace offset for hi
    sta (nfs_workspace),y                                             ; 9116: 91 9e       ..             ; Store filename offset at ws+&0F
    dey                                                               ; 9118: 88          .              ; Y=&0e
    pla                                                               ; 9119: 68          h              ; Restore boot type from stack
    sta (nfs_workspace),y                                             ; 911a: 91 9e       ..             ; Copy command to &0100 area
    jsr clear_osbyte_ce_cf                                            ; 911c: 20 5c 81     \.            ; Initialize OSBYTE vectors
    jsr ctrl_block_setup                                              ; 911f: 20 63 91     c.            ; Set up control block for boot
    ldx #1                                                            ; 9122: a2 01       ..             ; X=1: enable parameter
    ldy #0                                                            ; 9124: a0 00       ..             ; Y=0: second argument for OSBYTE
    lda #osbyte_read_write_econet_keyboard_disable                    ; 9126: a9 c9       ..             ; A=&C9: disable keyboard for boot
    jsr osbyte                                                        ; 9128: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; ***************************************************************************************
; Execute downloaded code at &0100
; 
; Zeroes &0100-&0102 (safe BRK default), restores the protection mask,
; and JMP &0100 to execute code received over the network.
; ***************************************************************************************
.lang_3_execute_at_0100
    ldx #2                                                            ; 912b: a2 02       ..             ; X=2: zero 3 bytes (offsets 2,1,0)
    lda #0                                                            ; 912d: a9 00       ..             ; A=0: zero / BRK opcode
; &912f referenced 1 time by &9133
.zero_0100_loop
    sta l0100,x                                                       ; 912f: 9d 00 01    ...            ; Store zero at &0100+X
    dex                                                               ; 9132: ca          .              ; Decrement byte counter
    bpl zero_0100_loop                                                ; 9133: 10 fa       ..             ; Loop until 3 bytes zeroed
    jsr clear_jsr_protection                                          ; 9135: 20 d7 92     ..            ; Release JSR protection mask
    jmp l0100                                                         ; 9138: 4c 00 01    L..            ; Execute downloaded code at &0100

; ***************************************************************************************
; Remote operation with source validation (REMOT)
; 
; Validates that the source station/network in the received packet
; matches the controlling station stored in the remote RXCB. This
; ensures that only the station that initiated the remote session
; can send commands — characters from other stations are rejected.
; Full init sequence: 1) disable keyboard, 2) set workspace ptr,
; 3) set status busy, 4) set R/W/byte/word masks, 5) set up CB,
; 6) set MODE 7 (the only mode guaranteed for terminal emulation),
; 7) set auto repeat rates, 8) enter current language. This is
; essentially a "thin terminal" setup — the local machine becomes
; a remote display/keyboard for the controlling station.
; Bit 0 of the status byte disallows further remote takeover
; attempts (preventing re-entrant remote control), while bit 3
; marks the machine as currently remoted.
; ***************************************************************************************
.lang_4_remote_validated
    ldy #4                                                            ; 913b: a0 04       ..             ; Y=4: validation byte offset
    lda (net_rx_ptr),y                                                ; 913d: b1 9c       ..             ; Load validation byte from RX data
    beq remot1                                                        ; 913f: f0 c5       ..             ; Zero: validation passed, continue
    ldy #&80                                                          ; 9141: a0 80       ..             ; Y=&80: source station offset
    lda (net_rx_ptr),y                                                ; 9143: b1 9c       ..             ; Load source station from RX buffer
    ldy #&0e                                                          ; 9145: a0 0e       ..             ; Y=&0E: controlling station offset
    cmp (nfs_workspace),y                                             ; 9147: d1 9e       ..             ; Compare with controlling station
    bne rchex                                                         ; 9149: d0 b8       ..             ; Mismatch: reject remote command
; ***************************************************************************************
; Insert remote keypress
; 
; Reads a character from RX block offset &82 and inserts it into
; keyboard input buffer 0 via OSBYTE &99.
; ***************************************************************************************
.lang_0_insert_remote_key
    ldy #&82                                                          ; 914b: a0 82       ..             ; Y=&82: character offset in RX data
    lda (net_rx_ptr),y                                                ; 914d: b1 9c       ..             ; Load remote keypress character
    tay                                                               ; 914f: a8          .              ; Transfer character to Y
    ldx #0                                                            ; 9150: a2 00       ..             ; X=0: keyboard input buffer
    jsr clear_jsr_protection                                          ; 9152: 20 d7 92     ..            ; Release JSR protection before call
    lda #osbyte_insert_input_buffer                                   ; 9155: a9 99       ..             ; A=&99: OSBYTE insert into buffer
    jmp osbyte                                                        ; 9157: 4c f4 ff    L..            ; Insert character Y into input buffer X

; ***************************************************************************************
; Alternate entry into control block setup
; 
; Sets X=&0D, Y=&7C. Tests bit 6 of &833B to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; ***************************************************************************************
; &915a referenced 3 times by &8fe3, &8ff6, &90f9
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 915a: a2 0d       ..             ; X=&0D: template offset for alt entry
    ldy #&7c ; '|'                                                    ; 915c: a0 7c       .|             ; Y=&7C: target workspace offset for alt entry
    bit tx_ctrl_upper                                                 ; 915e: 2c 3b 83    ,;.            ; BIT test: V flag = bit 6 of &83B3
    bvs cbset2                                                        ; 9161: 70 05       p.             ; V=1: store to (net_rx_ptr) instead
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
; &9163 referenced 1 time by &911f
.ctrl_block_setup
    ldy #&17                                                          ; 9163: a0 17       ..             ; Y=&17: workspace target offset (main entry)
    ldx #&1a                                                          ; 9165: a2 1a       ..             ; X=&1A: template table index (main entry)
; &9167 referenced 1 time by &922c
.ctrl_block_setup_clv
    clv                                                               ; 9167: b8          .              ; V=0: target is (nfs_workspace)
; &9168 referenced 2 times by &9161, &9189
.cbset2
    lda ctrl_block_template,x                                         ; 9168: bd 8f 91    ...            ; Load template byte from ctrl_block_template[X]
    cmp #&fe                                                          ; 916b: c9 fe       ..             ; &FE = stop sentinel
    beq cb_template_tail                                              ; 916d: f0 1c       ..             ; End of template: jump to exit
    cmp #&fd                                                          ; 916f: c9 fd       ..             ; &FD = skip sentinel
    beq cb_template_main_start                                        ; 9171: f0 14       ..             ; Skip: don't store, just decrement Y
    cmp #&fc                                                          ; 9173: c9 fc       ..             ; &FC = page byte sentinel
    bne cbset3                                                        ; 9175: d0 08       ..             ; Not sentinel: store template value directly
    lda net_rx_ptr_hi                                                 ; 9177: a5 9d       ..             ; V=1: use (net_rx_ptr) page
    bvs rxcb_matched                                                  ; 9179: 70 02       p.             ; V=1: skip to net_rx_ptr page
    lda nfs_workspace_hi                                              ; 917b: a5 9f       ..             ; V=0: use (nfs_workspace) page
; &917d referenced 1 time by &9179
.rxcb_matched
    sta net_tx_ptr_hi                                                 ; 917d: 85 9b       ..             ; PAGE byte → Y=&02 / Y=&74
; &917f referenced 1 time by &9175
.cbset3
    bvs cbset4                                                        ; 917f: 70 04       p.             ; → Y=&04 / Y=&76
    sta (nfs_workspace),y                                             ; 9181: 91 9e       ..             ; PAGE byte → Y=&06 / Y=&78
    bvc cb_template_main_start                                        ; 9183: 50 02       P.             ; → Y=&08 / Y=&7A; ALWAYS branch

; &9185 referenced 1 time by &917f
.cbset4
    sta (net_rx_ptr),y                                                ; 9185: 91 9c       ..             ; Alt-path only → Y=&70
; &9187 referenced 2 times by &9171, &9183
.cb_template_main_start
    dey                                                               ; 9187: 88          .              ; → Y=&0C (main only)
    dex                                                               ; 9188: ca          .              ; → Y=&0D (main only)
    bpl cbset2                                                        ; 9189: 10 dd       ..             ; Loop until all template bytes done
; &918b referenced 1 time by &916d
.cb_template_tail
    iny                                                               ; 918b: c8          .              ; → Y=&10 (main only)
    sty net_tx_ptr                                                    ; 918c: 84 9a       ..             ; Store final offset as net_tx_ptr
    rts                                                               ; 918e: 60          `              ; → Y=&07 / Y=&79

; ***************************************************************************************
; Control block initialisation template
; 
; Read by the loop at &9168, indexed by X from a starting value
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
; &918f referenced 1 time by &9168
.ctrl_block_template
    equb &85                                                          ; 918f: 85          .              ; Alt-path only → Y=&6F
    equb 0                                                            ; 9190: 00          .              ; Alt-path only → Y=&70
    equb &fd                                                          ; 9191: fd          .              ; SKIP
    equb &fd                                                          ; 9192: fd          .              ; SKIP
    equb &7d                                                          ; 9193: 7d          }              ; → Y=&01 / Y=&73
    equb &fc                                                          ; 9194: fc          .              ; PAGE byte → Y=&02 / Y=&74
    equb &ff                                                          ; 9195: ff          .              ; → Y=&03 / Y=&75
    equb &ff                                                          ; 9196: ff          .              ; → Y=&04 / Y=&76
    equb &7e                                                          ; 9197: 7e          ~              ; → Y=&05 / Y=&77
    equb &fc                                                          ; 9198: fc          .              ; PAGE byte → Y=&06 / Y=&78
    equb &ff                                                          ; 9199: ff          .              ; → Y=&07 / Y=&79
    equb &ff                                                          ; 919a: ff          .              ; → Y=&08 / Y=&7A
    equb 0                                                            ; 919b: 00          .              ; → Y=&09 / Y=&7B
    equb 0                                                            ; 919c: 00          .              ; → Y=&0A / Y=&7C
    equb &fe                                                          ; 919d: fe          .              ; STOP — main-path boundary
    equb &80                                                          ; 919e: 80          .              ; → Y=&0C (main only)
    equb &93                                                          ; 919f: 93          .              ; → Y=&0D (main only)
    equb &fd                                                          ; 91a0: fd          .              ; SKIP (main only)
    equb &fd                                                          ; 91a1: fd          .              ; SKIP (main only)
    equb &d9                                                          ; 91a2: d9          .              ; → Y=&10 (main only)
    equb &fc                                                          ; 91a3: fc          .              ; PAGE byte → Y=&11 (main only)
    equb &ff                                                          ; 91a4: ff          .              ; → Y=&12 (main only)
    equb &ff                                                          ; 91a5: ff          .              ; → Y=&13 (main only)
    equb &de                                                          ; 91a6: de          .              ; → Y=&14 (main only)
    equb &fc                                                          ; 91a7: fc          .              ; PAGE byte → Y=&15 (main only)
    equb &ff                                                          ; 91a8: ff          .              ; → Y=&16 (main only)
    equb &ff                                                          ; 91a9: ff          .              ; → Y=&17 (main only)
    equb &fe, &d1, &fd, &fd, &1f, &fd, &ff, &ff, &fd, &fd, &ff, &ff   ; 91aa: fe d1 fd... ...

; ***************************************************************************************
; Fn 5: printer selection changed (SELECT)
; 
; Called when the printer selection changes. Compares the new
; selection (in PARMX) against the network printer (buffer 4).
; If it matches, initialises the printer buffer pointer (PBUFFP)
; and sets the initial flag byte (&41). Otherwise just updates
; the printer status flags (PFLAGS).
; 
; On Entry:
;     X: 1-based buffer number
; ***************************************************************************************
.printer_select_handler
    lda #0                                                            ; 91b6: a9 00       ..             ; A=0: clear printer buffer state
    dex                                                               ; 91b8: ca          .              ; X-1: convert 1-based buffer to 0-based
    cpx osword_pb_ptr                                                 ; 91b9: e4 f0       ..             ; Is this the network printer buffer?
    bne setup1                                                        ; 91bb: d0 07       ..             ; No: skip printer init
    lda #&1f                                                          ; 91bd: a9 1f       ..             ; &1F = initial buffer pointer offset
    sta printer_buf_ptr                                               ; 91bf: 8d 61 0d    .a.            ; Reset printer buffer write position
    lda #&43 ; 'C'                                                    ; 91c2: a9 43       .C             ; &41 = initial PFLAGS (bit 6 set, bit 0 set)
; &91c4 referenced 1 time by &91bb
.setup1
    sta l0d60                                                         ; 91c4: 8d 60 0d    .`.            ; Store initial PFLAGS value
; &91c7 referenced 2 times by &91ca, &91de
.return_printer_select
    rts                                                               ; 91c7: 60          `              ; Return

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
; 
; On Entry:
;     X: reason code (1=chars, 2=Ctrl-B, 3=Ctrl-C)
;     Y: buffer number (must be 4 for network printer)
; ***************************************************************************************
.remote_print_handler
    cpy #4                                                            ; 91c8: c0 04       ..             ; Only handle buffer 4 (network printer)
    bne return_printer_select                                         ; 91ca: d0 fb       ..             ; Not buffer 4: ignore
    txa                                                               ; 91cc: 8a          .              ; A = reason code
    dex                                                               ; 91cd: ca          .              ; Reason 1? (DEX: 1->0)
    bne toggle_print_flag                                             ; 91ce: d0 26       .&             ; Not reason 1: handle Ctrl-B/C
    tsx                                                               ; 91d0: ba          .              ; Get stack pointer for P register
    ora l0106,x                                                       ; 91d1: 1d 06 01    ...            ; Force I flag in stacked P to block IRQs
    sta l0106,x                                                       ; 91d4: 9d 06 01    ...            ; Write back modified P register
; &91d7 referenced 2 times by &91e6, &91eb
.prlp1
    lda #osbyte_read_buffer                                           ; 91d7: a9 91       ..             ; OSBYTE &91: extract char from MOS buffer
    ldx #buffer_printer                                               ; 91d9: a2 03       ..             ; X=3: printer buffer number
    jsr osbyte                                                        ; 91db: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_printer_select                                         ; 91de: b0 e7       ..             ; Buffer empty: return
    tya                                                               ; 91e0: 98          .              ; Y = extracted character; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 91e1: 20 ed 91     ..            ; Store char in output buffer
    cpy #&6e ; 'n'                                                    ; 91e4: c0 6e       .n             ; Buffer nearly full? (&6E = threshold)
    bcc prlp1                                                         ; 91e6: 90 ef       ..             ; Not full: get next char
    jsr flush_output_block                                            ; 91e8: 20 18 92     ..            ; Buffer full: flush to network
    bne prlp1                                                         ; 91eb: d0 ea       ..             ; Flush done: continue loop
; ***************************************************************************************
; Store output byte to network buffer
; 
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; 
; On Entry:
;     A: byte to store
; 
; On Exit:
;     Y: buffer offset before store
; ***************************************************************************************
; &91ed referenced 2 times by &91e1, &91f7
.store_output_byte
    ldy printer_buf_ptr                                               ; 91ed: ac 61 0d    .a.            ; Load current buffer offset
    sta (net_rx_ptr),y                                                ; 91f0: 91 9c       ..             ; Store byte at current position
    inc printer_buf_ptr                                               ; 91f2: ee 61 0d    .a.            ; Advance buffer pointer
    rts                                                               ; 91f5: 60          `              ; Return; Y = buffer offset

; &91f6 referenced 1 time by &91ce
.toggle_print_flag
    pha                                                               ; 91f6: 48          H              ; Save reason code
    jsr store_output_byte                                             ; 91f7: 20 ed 91     ..            ; Decrement transfer count low byte
    eor l0d60                                                         ; 91fa: 4d 60 0d    M`.            ; XOR with transfer count flags
    ror a                                                             ; 91fd: 6a          j              ; Shift bit 0 into carry
    bcc rx_data_phase                                                 ; 91fe: 90 0f       ..             ; Data phase active: continue
    lda l0d60                                                         ; 9200: ad 60 0d    .`.            ; Load transfer count flags
    ror a                                                             ; 9203: 6a          j              ; Shift bit 0 into carry
    bcc rx_imm_discard                                                ; 9204: 90 06       ..             ; Bit 0=0 (active): just flush
    rol a                                                             ; 9206: 2a          *              ; Rotate carry back
    and #&7f                                                          ; 9207: 29 7f       ).             ; Mask off control bits
    sta l0d60                                                         ; 9209: 8d 60 0d    .`.            ; Store updated flags
; &920c referenced 1 time by &9204
.rx_imm_discard
    jsr flush_output_block                                            ; 920c: 20 18 92     ..            ; Flush accumulated output to network
; &920f referenced 1 time by &91fe
.rx_data_phase
    ror l0d60                                                         ; 920f: 6e 60 0d    n`.            ; Save PFLAGS bit 0 via carry
    pla                                                               ; 9212: 68          h              ; Restore original reason code
    ror a                                                             ; 9213: 6a          j              ; Old PFLAGS bit 0 to A bit 7
    rol l0d60                                                         ; 9214: 2e 60 0d    .`.            ; Reason bit 0 into PFLAGS bit 0
    rts                                                               ; 9217: 60          `              ; Return

; ***************************************************************************************
; Flush output block
; 
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; ***************************************************************************************
; &9218 referenced 2 times by &91e8, &920c
.flush_output_block
    ldy #8                                                            ; 9218: a0 08       ..             ; Store buffer length at workspace offset &08
    lda printer_buf_ptr                                               ; 921a: ad 61 0d    .a.            ; Current buffer fill position
    sta (nfs_workspace),y                                             ; 921d: 91 9e       ..             ; Write to workspace offset &08
    lda net_rx_ptr_hi                                                 ; 921f: a5 9d       ..             ; Store page high byte at offset &09
    iny                                                               ; 9221: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 9222: 91 9e       ..             ; Write page high byte at offset &09
    ldy #5                                                            ; 9224: a0 05       ..             ; Also store at offset &05
    sta (nfs_workspace),y                                             ; 9226: 91 9e       ..             ; (end address high byte)
    ldy #&0b                                                          ; 9228: a0 0b       ..             ; Y=&0B: flag byte offset
    ldx #&26 ; '&'                                                    ; 922a: a2 26       .&             ; X=&26: start from template entry &26
    jsr ctrl_block_setup_clv                                          ; 922c: 20 67 91     g.            ; Reuse ctrl_block_setup with CLV entry
    dey                                                               ; 922f: 88          .              ; Y=&0A: sequence flag byte offset
    lda l0d60                                                         ; 9230: ad 60 0d    .`.            ; Load current PFLAGS
    pha                                                               ; 9233: 48          H              ; Save current PFLAGS
    rol a                                                             ; 9234: 2a          *              ; Carry = current sequence (bit 7)
    pla                                                               ; 9235: 68          h              ; Restore original PFLAGS
    eor #&80                                                          ; 9236: 49 80       I.             ; Toggle sequence number (bit 7 of PFLAGS)
    sta l0d60                                                         ; 9238: 8d 60 0d    .`.            ; Store toggled sequence number
    rol a                                                             ; 923b: 2a          *              ; Old sequence bit into bit 0
    sta (nfs_workspace),y                                             ; 923c: 91 9e       ..             ; Store sequence flag at offset &0A
    ldy #&1f                                                          ; 923e: a0 1f       ..             ; Y=&1F: buffer start offset
    sty printer_buf_ptr                                               ; 9240: 8c 61 0d    .a.            ; Reset printer buffer to start (&1F)
    lda #0                                                            ; 9243: a9 00       ..             ; A=0: printer output flag
    tax                                                               ; 9245: aa          .              ; X=0: workspace low byte; X=&00
    ldy nfs_workspace_hi                                              ; 9246: a4 9f       ..             ; Y = workspace page high byte
    cli                                                               ; 9248: 58          X              ; Enable interrupts before TX
; ***************************************************************************************
; Transmit with retry loop (XMITFS/XMITFY)
; 
; Calls the low-level transmit routine (BRIANX) with FSTRY (&FF = 255)
; retries and FSDELY (&60 = 96) ms delay between attempts. On each
; iteration, checks the result code: zero means success, non-zero
; means retry. After all retries exhausted, reports a 'Net error'.
; Entry point XMITFY allows a custom delay in Y.
; 
; On Entry:
;     A: handle bitmask (0=printer, non-zero=file)
;     X: TX control block address low
;     Y: TX control block address high
; ***************************************************************************************
; &9249 referenced 2 times by &839c, &83d4
.econet_tx_retry
    stx net_tx_ptr                                                    ; 9249: 86 9a       ..             ; Set TX control block ptr low byte
    sty net_tx_ptr_hi                                                 ; 924b: 84 9b       ..             ; Set TX control block ptr high byte
    pha                                                               ; 924d: 48          H              ; Save A (handle bitmask) for later
    and fs_sequence_nos                                               ; 924e: 2d 08 0e    -..            ; Compute sequence bit from handle
    beq bsxl1                                                         ; 9251: f0 02       ..             ; Zero: no sequence bit set
    lda #1                                                            ; 9253: a9 01       ..             ; Non-zero: normalise to bit 0
; &9255 referenced 1 time by &9251
.bsxl1
    ldy #0                                                            ; 9255: a0 00       ..             ; Y=0: flag byte offset in TXCB
    ora (net_tx_ptr),y                                                ; 9257: 11 9a       ..             ; Merge sequence into existing flag byte
    pha                                                               ; 9259: 48          H              ; Save merged flag byte
    sta (net_tx_ptr),y                                                ; 925a: 91 9a       ..             ; Write flag+sequence to TXCB byte 0
    jsr tx_poll_ff                                                    ; 925c: 20 4d 86     M.            ; Transmit with full retry
    lda #&ff                                                          ; 925f: a9 ff       ..             ; End address &FFFF = unlimited data length
    ldy #8                                                            ; 9261: a0 08       ..             ; Y=8: end address low offset in TXCB
    sta (net_tx_ptr),y                                                ; 9263: 91 9a       ..             ; Store &FF to end addr low
    iny                                                               ; 9265: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 9266: 91 9a       ..             ; Store &FF to end addr high (Y=9)
    pla                                                               ; 9268: 68          h              ; Recover merged flag byte
    tax                                                               ; 9269: aa          .              ; Save in X for sequence compare
    ldy #&d1                                                          ; 926a: a0 d1       ..             ; Y=&D1: printer port number
    pla                                                               ; 926c: 68          h              ; Recover saved handle bitmask
    pha                                                               ; 926d: 48          H              ; Re-save for later consumption
    beq bspsx                                                         ; 926e: f0 02       ..             ; A=0: port &D1 (print); A!=0: port &90 (FS)
    ldy #&90                                                          ; 9270: a0 90       ..             ; Y=&90: FS data port
; &9272 referenced 1 time by &926e
.bspsx
    tya                                                               ; 9272: 98          .              ; A = selected port number
    ldy #1                                                            ; 9273: a0 01       ..             ; Y=1: port byte offset in TXCB
    sta (net_tx_ptr),y                                                ; 9275: 91 9a       ..             ; Write port to TXCB byte 1
    txa                                                               ; 9277: 8a          .              ; A = saved flag byte (expected sequence)
    dey                                                               ; 9278: 88          .              ; Y=&00
    pha                                                               ; 9279: 48          H              ; Push expected sequence for retry loop
; &927a referenced 1 time by &9286
.bsxl0
    lda #&7f                                                          ; 927a: a9 7f       ..             ; Flag byte &7F = waiting for reply
    sta (net_tx_ptr),y                                                ; 927c: 91 9a       ..             ; Write to TXCB flag byte (Y=0)
    jsr send_to_fs_star                                               ; 927e: 20 49 84     I.            ; Transmit and wait for reply (BRIANX)
    pla                                                               ; 9281: 68          h              ; Recover expected sequence
    pha                                                               ; 9282: 48          H              ; Keep on stack for next iteration
    eor (net_tx_ptr),y                                                ; 9283: 51 9a       Q.             ; Check if TX result matches expected sequence
    ror a                                                             ; 9285: 6a          j              ; Bit 0 to carry (sequence mismatch?)
    bcs bsxl0                                                         ; 9286: b0 f2       ..             ; C=1: mismatch, retry transmit
    pla                                                               ; 9288: 68          h              ; Clean up: discard expected sequence
    pla                                                               ; 9289: 68          h              ; Discard saved handle bitmask
    tax                                                               ; 928a: aa          .              ; Transfer count to X
    inx                                                               ; 928b: e8          .              ; Test for retry exhaustion
    beq return_bspsx                                                  ; 928c: f0 03       ..             ; X wrapped to 0: retries exhausted
    eor fs_sequence_nos                                               ; 928e: 4d 08 0e    M..            ; Toggle sequence bit on success
; &9291 referenced 1 time by &928c
.return_bspsx
    rts                                                               ; 9291: 60          `              ; Return

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
    lda fs_load_addr_2                                                ; 9292: a5 b2       ..             ; Save current table index
    pha                                                               ; 9294: 48          H              ; Push for later restore
    lda #&e9                                                          ; 9295: a9 e9       ..             ; Point workspace to palette save area (&E9)
    sta nfs_workspace                                                 ; 9297: 85 9e       ..             ; Set workspace low byte
    ldy #0                                                            ; 9299: a0 00       ..             ; Y=0: first palette entry
    sty fs_load_addr_2                                                ; 929b: 84 b2       ..             ; Clear table index counter
    lda l0350                                                         ; 929d: ad 50 03    .P.            ; Save current screen MODE to workspace
    sta (nfs_workspace),y                                             ; 92a0: 91 9e       ..             ; Store MODE at workspace[0]
    inc nfs_workspace                                                 ; 92a2: e6 9e       ..             ; Advance workspace pointer past MODE byte
    lda l0351                                                         ; 92a4: ad 51 03    .Q.            ; Read colour count (from &0351)
    pha                                                               ; 92a7: 48          H              ; Push for iteration count tracking
    tya                                                               ; 92a8: 98          .              ; A=0: logical colour number for OSWORD; A=&00
; &92a9 referenced 1 time by &92c8
.save_palette_entry
    sta (nfs_workspace),y                                             ; 92a9: 91 9e       ..             ; Store logical colour at workspace[0]
    ldx nfs_workspace                                                 ; 92ab: a6 9e       ..             ; X = workspace ptr low (param block addr)
    ldy nfs_workspace_hi                                              ; 92ad: a4 9f       ..             ; Y = workspace ptr high
    lda #osword_read_palette                                          ; 92af: a9 0b       ..             ; OSWORD &0B: read palette for logical colour
    jsr osword                                                        ; 92b1: 20 f1 ff     ..            ; Read palette
    pla                                                               ; 92b4: 68          h              ; Recover colour count
    ldy #0                                                            ; 92b5: a0 00       ..             ; Y=0: access workspace[0]
    sta (nfs_workspace),y                                             ; 92b7: 91 9e       ..             ; Write colour count back to workspace[0]
    iny                                                               ; 92b9: c8          .              ; Y=1: access workspace[1] (palette result); Y=&01
    lda (nfs_workspace),y                                             ; 92ba: b1 9e       ..             ; Read palette value returned by OSWORD
    pha                                                               ; 92bc: 48          H              ; Push palette value for next iteration
    ldx nfs_workspace                                                 ; 92bd: a6 9e       ..             ; X = current workspace ptr low
    inc nfs_workspace                                                 ; 92bf: e6 9e       ..             ; Advance workspace pointer
    inc fs_load_addr_2                                                ; 92c1: e6 b2       ..             ; Increment table index
    dey                                                               ; 92c3: 88          .              ; Y=0 for next store; Y=&00
    lda fs_load_addr_2                                                ; 92c4: a5 b2       ..             ; Load table index as logical colour
    cpx #&f9                                                          ; 92c6: e0 f9       ..             ; Loop until workspace wraps past &F9
    bne save_palette_entry                                            ; 92c8: d0 df       ..             ; Continue for all 16 palette entries
    pla                                                               ; 92ca: 68          h              ; Discard last palette value from stack
    sty fs_load_addr_2                                                ; 92cb: 84 b2       ..             ; Reset table index to 0
    inc nfs_workspace                                                 ; 92cd: e6 9e       ..             ; Advance workspace past palette data
    jsr save_vdu_state                                                ; 92cf: 20 de 92     ..            ; Save cursor pos and OSBYTE state values
    inc nfs_workspace                                                 ; 92d2: e6 9e       ..             ; Advance workspace past VDU state data
    pla                                                               ; 92d4: 68          h              ; Recover saved table index
    sta fs_load_addr_2                                                ; 92d5: 85 b2       ..             ; Restore table index
; &92d7 referenced 4 times by &8e66, &9103, &9135, &9152
.clear_jsr_protection
    lda rx_ctrl_copy                                                  ; 92d7: ad 3b 0d    .;.            ; Restore LSTAT from saved OLDJSR value
    sta prot_status                                                   ; 92da: 8d 63 0d    .c.            ; Write to protection status
    rts                                                               ; 92dd: 60          `              ; Return

; ***************************************************************************************
; Save VDU workspace state
; 
; Stores the cursor position value from &0355 into NFS workspace,
; then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
; and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
; each result into consecutive workspace bytes.
; ***************************************************************************************
; &92de referenced 1 time by &92cf
.save_vdu_state
    lda l0355                                                         ; 92de: ad 55 03    .U.            ; Read cursor editing state
    sta (nfs_workspace),y                                             ; 92e1: 91 9e       ..             ; Store to workspace[Y]
    tax                                                               ; 92e3: aa          .              ; Preserve in X for OSBYTE
    jsr read_vdu_osbyte                                               ; 92e4: 20 f1 92     ..            ; OSBYTE &85: read cursor position
    inc nfs_workspace                                                 ; 92e7: e6 9e       ..             ; Advance workspace pointer
    tya                                                               ; 92e9: 98          .              ; Y result from OSBYTE &85
    sta (nfs_workspace,x)                                             ; 92ea: 81 9e       ..             ; Store Y pos to workspace (X=0)
    jsr read_vdu_osbyte_x0                                            ; 92ec: 20 ef 92     ..            ; Self-call trick: executes twice
; &92ef referenced 1 time by &92ec
.read_vdu_osbyte_x0
    ldx #0                                                            ; 92ef: a2 00       ..             ; X=0 for (zp,X) addressing
; &92f1 referenced 1 time by &92e4
.read_vdu_osbyte
    ldy fs_load_addr_2                                                ; 92f1: a4 b2       ..             ; Index into OSBYTE number table
    inc fs_load_addr_2                                                ; 92f3: e6 b2       ..             ; Next table entry next time
    inc nfs_workspace                                                 ; 92f5: e6 9e       ..             ; Advance workspace pointer
    lda osbyte_vdu_table,y                                            ; 92f7: b9 05 93    ...            ; Read OSBYTE number from table
    ldy #&ff                                                          ; 92fa: a0 ff       ..             ; Y=&FF: read current value
    jsr osbyte                                                        ; 92fc: 20 f4 ff     ..            ; Call OSBYTE
    txa                                                               ; 92ff: 8a          .              ; Result in X to A
    ldx #0                                                            ; 9300: a2 00       ..             ; X=0 for indexed indirect store
    sta (nfs_workspace,x)                                             ; 9302: 81 9e       ..             ; Store result to workspace
    rts                                                               ; 9304: 60          `              ; Return after storing result

; 3-entry OSBYTE table for lang_2_save_palette_vdu (&9292)
; &9305 referenced 1 time by &92f7
.osbyte_vdu_table
    equb &85                                                          ; 9305: 85          .              ; OSBYTE &85: read cursor position
    equb &c2                                                          ; 9306: c2          .              ; OSBYTE &C2: read shadow RAM allocation
    equb &c3                                                          ; 9307: c3          .              ; OSBYTE &C3: read screen start address
; &9308 referenced 1 time by &8113

    org &964d

    equb &ff, &42, &ff, 0, &ff, &77, &ff, &ff, &ff, &df, &ff, 0       ; 964d: ff 42 ff... .B.
    equb &ff,   0, &ff, 0, &ff,   4, &ff                              ; 9659: ff 00 ff... ...

; &9660 referenced 2 times by &8668, &8e4a
.trampoline_tx_setup
    jmp tx_begin                                                      ; 9660: 4c e4 9b    L..            ; Trampoline: forward to tx_begin

; &9663 referenced 1 time by &82ca
.trampoline_adlc_init
    jmp adlc_init                                                     ; 9663: 4c 6f 96    Lo.            ; Trampoline: forward to adlc_init

.svc_12_nmi_release
    jmp save_econet_state                                             ; 9666: 4c 9d 96    L..            ; Trampoline: forward to NMI release

.svc_11_nmi_claim
    jmp restore_econet_state                                          ; 9669: 4c b4 96    L..            ; Trampoline: forward to NMI claim

.svc_5_unknown_irq
    jmp check_sr_irq                                                  ; 966c: 4c 52 9b    LR.            ; Trampoline: forward to IRQ handler

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
    jsr adlc_full_reset                                               ; 9672: 20 dc 96     ..            ; Full ADLC hardware reset
    lda #osbyte_read_tube_presence                                    ; 9675: a9 ea       ..             ; OSBYTE &EA: check Tube co-processor
    ldx #0                                                            ; 9677: a2 00       ..             ; X=0 for OSBYTE
    ldy #&ff                                                          ; 9679: a0 ff       ..             ; Y=&FF for OSBYTE
    jsr osbyte                                                        ; 967b: 20 f4 ff     ..            ; Read Tube present flag
    stx tx_in_progress                                                ; 967e: 8e 52 0d    .R.            ; X=value of Tube present flag
; ***************************************************************************************
; Initialise NMI workspace
; 
; Copies NMI shim from ROM to &0D00, stores current ROM bank number
; into shim self-modifying code, sets TX status to &80 (idle/complete),
; saves station ID from &FE18 into TX scout buffer, re-enables NMIs
; by reading &FE20.
; ***************************************************************************************
; &9681 referenced 1 time by &96ca
.adlc_init_workspace
    jsr install_nmi_shim                                              ; 9681: 20 cd 96     ..            ; Copy NMI shim from ROM to &0D00
    lda romsel_copy                                                   ; 9684: a5 f4       ..             ; Load current ROM bank number
    sta nmi_shim_07                                                   ; 9686: 8d 07 0d    ...            ; Patch ROM bank into NMI shim
    lda #&80                                                          ; 9689: a9 80       ..             ; A=&80: TX idle/complete status
    sta tx_ctrl_status                                                ; 968b: 8d 3a 0d    .:.            ; Mark Econet as initialised
    lda station_id_disable_net_nmis                                   ; 968e: ad 18 fe    ...            ; Read station ID (&FE18 = INTOFF side effect)
    sta tx_src_stn                                                    ; 9691: 8d 22 0d    .".            ; Store our station ID in TX scout
    lda #0                                                            ; 9694: a9 00       ..             ; A=0: clear source network
    sta tx_src_net                                                    ; 9696: 8d 23 0d    .#.            ; Clear TX source network byte
    bit video_ula_control                                             ; 9699: 2c 20 fe    , .            ; INTON: re-enable NMIs (&FE20 read side effect)
    rts                                                               ; 969c: 60          `              ; Return to caller

; ***************************************************************************************
; Save Econet state to RX control block
; 
; Stores rx_status_flags, protection_mask, and tx_in_progress
; to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.
; ***************************************************************************************
; &969d referenced 1 time by &9666
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 969d: 2c 18 fe    ,..            ; INTOFF: disable NMIs for state save
    ldy #8                                                            ; 96a0: a0 08       ..             ; Y=8: RXCB offset for rx_status_flags
    lda rx_status_flags                                               ; 96a2: ad 38 0d    .8.            ; Load rx_status_flags
    sta (net_rx_ptr),y                                                ; 96a5: 91 9c       ..             ; Store to RXCB offset 8
    iny                                                               ; 96a7: c8          .              ; Y=&09
    lda prot_status                                                   ; 96a8: ad 63 0d    .c.            ; Load prot_status
    sta (net_rx_ptr),y                                                ; 96ab: 91 9c       ..             ; Store to RXCB offset 9
    iny                                                               ; 96ad: c8          .              ; Y=&0a
    lda tx_in_progress                                                ; 96ae: ad 52 0d    .R.            ; Load TX in-progress flag
    sta (net_rx_ptr),y                                                ; 96b1: 91 9c       ..             ; Store tx_in_progress to offset &0A
    rts                                                               ; 96b3: 60          `              ; Return to caller

; ***************************************************************************************
; Restore Econet state from RX control block
; 
; Loads rx_status_flags, protection_mask, and tx_in_progress
; from (net_rx_ptr) at offsets 8-10, then reinitialises via
; adlc_init_workspace.
; ***************************************************************************************
; &96b4 referenced 1 time by &9669
.restore_econet_state
    bit station_id_disable_net_nmis                                   ; 96b4: 2c 18 fe    ,..            ; INTOFF: disable NMIs for state restore
    ldy #8                                                            ; 96b7: a0 08       ..             ; Y=8: workspace offset for flags
    lda (net_rx_ptr),y                                                ; 96b9: b1 9c       ..             ; Load saved rx_status_flags
    sta rx_status_flags                                               ; 96bb: 8d 38 0d    .8.            ; Restore rx_status_flags
    iny                                                               ; 96be: c8          .              ; Y=&09
    lda (net_rx_ptr),y                                                ; 96bf: b1 9c       ..             ; Load saved protection mask
    sta prot_status                                                   ; 96c1: 8d 63 0d    .c.            ; Restore prot_status
    iny                                                               ; 96c4: c8          .              ; Y=&0a
    lda (net_rx_ptr),y                                                ; 96c5: b1 9c       ..             ; Load saved tx_in_progress
    sta tx_in_progress                                                ; 96c7: 8d 52 0d    .R.            ; Restore TX state
    jmp adlc_init_workspace                                           ; 96ca: 4c 81 96    L..            ; Reinitialise NMI workspace

; ***************************************************************************************
; Copy NMI shim from ROM (&9FCA) to RAM (&0D00)
; 
; Copies 32 bytes. Interrupts are enabled during the copy.
; ***************************************************************************************
; &96cd referenced 1 time by &9681
.install_nmi_shim
    php                                                               ; 96cd: 08          .              ; Save interrupt state on stack
    cli                                                               ; 96ce: 58          X              ; Enable interrupts during copy
    ldy #&20 ; ' '                                                    ; 96cf: a0 20       .              ; Y=&20: copy 32 bytes
; &96d1 referenced 1 time by &96d8
.copy_nmi_shim_loop
    lda nmi_shim_rom_src,y                                            ; 96d1: b9 ca 9f    ...            ; Load NMI shim byte from ROM
    sta l0cff,y                                                       ; 96d4: 99 ff 0c    ...            ; Store to NMI area at &0D00+Y
    dey                                                               ; 96d7: 88          .              ; Decrement byte counter
    bne copy_nmi_shim_loop                                            ; 96d8: d0 f7       ..             ; Loop until all bytes copied
    plp                                                               ; 96da: 28          (              ; Restore interrupt state
    rts                                                               ; 96db: 60          `              ; Return from shim installation

; ***************************************************************************************
; ADLC full reset
; 
; Aborts all activity and returns to idle RX listen mode.
; ***************************************************************************************
; &96dc referenced 3 times by &9672, &973e, &9894
.adlc_full_reset
    lda #&c1                                                          ; 96dc: a9 c1       ..             ; CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 96de: 8d a0 fe    ...            ; Write CR1: full reset
    lda #&1e                                                          ; 96e1: a9 1e       ..             ; CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding
    sta econet_data_terminate_frame                                   ; 96e3: 8d a3 fe    ...            ; Write CR4 via ADLC reg 3 (AC=1)
    lda #0                                                            ; 96e6: a9 00       ..             ; CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 96e8: 8d a1 fe    ...            ; Write CR3=0: clear loop-back/AEX/DTR
; ***************************************************************************************
; Enter RX listen mode
; 
; TX held in reset, RX active with interrupts. Clears all status.
; ***************************************************************************************
; &96eb referenced 1 time by &9a40
.adlc_rx_listen
    lda #&82                                                          ; 96eb: a9 82       ..             ; CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 96ed: 8d a0 fe    ...            ; Write CR1: RIE | TX_RESET
    lda #&67 ; 'g'                                                    ; 96f0: a9 67       .g             ; CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 96f2: 8d a1 fe    ...            ; Write CR2: listen mode config
    rts                                                               ; 96f5: 60          `              ; Return

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
; &96f6 referenced 1 time by &9fd6
.nmi_rx_scout
    lda #1                                                            ; 96f6: a9 01       ..             ; A=&01: mask for SR2 bit0 (AP = Address Present)
    bit econet_control23_or_status2                                   ; 96f8: 2c a1 fe    ,..            ; BIT SR2: Z = A AND SR2 -- tests if AP is set
    beq scout_error                                                   ; 96fb: f0 3a       .:             ; AP not set, no incoming data -- check for errors
    lda econet_data_continue_frame                                    ; 96fd: ad a2 fe    ...            ; Read first RX byte (destination station address)
    cmp station_id_disable_net_nmis                                   ; 9700: cd 18 fe    ...            ; Compare to our station ID (&FE18 read = INTOFF, disables NMIs)
    beq accept_frame                                                  ; 9703: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 9705: c9 ff       ..             ; Check for broadcast address (&FF)
    bne scout_reject                                                  ; 9707: d0 1a       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 9709: a9 40       .@             ; Flag &40 = broadcast frame
    sta tx_flags                                                      ; 970b: 8d 4a 0d    .J.            ; Store broadcast flag in TX flags
; &970e referenced 1 time by &9703
.accept_frame
    lda #&15                                                          ; 970e: a9 15       ..             ; Install next NMI handler at &9715 (RX scout second byte)
    ldy #&97                                                          ; 9710: a0 97       ..             ; High byte of scout net handler
    jmp set_nmi_vector                                                ; 9712: 4c 0e 0d    L..            ; Install next handler and RTI

; ***************************************************************************************
; RX scout second byte handler
; 
; Reads the second byte of an incoming scout (destination network).
; Checks for network match: 0 = local network (accept), &FF = broadcast
; (accept and flag), anything else = reject.
; Installs the scout data reading loop handler at &9747.
; ***************************************************************************************
.nmi_rx_scout_net
    bit econet_control23_or_status2                                   ; 9715: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl scout_error                                                   ; 9718: 10 1d       ..             ; No RDA -- check errors
    lda econet_data_continue_frame                                    ; 971a: ad a2 fe    ...            ; Read destination network byte
    beq accept_local_net                                              ; 971d: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 971f: 49 ff       I.             ; EOR &FF: test if network = &FF (broadcast)
    beq accept_scout_net                                              ; 9721: f0 0b       ..             ; Broadcast network -- accept
; &9723 referenced 1 time by &9707
.scout_reject
    lda #&a2                                                          ; 9723: a9 a2       ..             ; Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 9725: 8d a0 fe    ...            ; Write CR1 to discontinue RX
    jmp discard_after_reset                                           ; 9728: 4c 43 9a    LC.            ; Return to idle scout listening

; &972b referenced 1 time by &971d
.accept_local_net
    sta tx_flags                                                      ; 972b: 8d 4a 0d    .J.            ; Network = 0 (local): clear tx_flags
; &972e referenced 1 time by &9721
.accept_scout_net
    sta port_buf_len                                                  ; 972e: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #&47 ; 'G'                                                    ; 9730: a9 47       .G             ; Install scout data reading loop at &9747
    ldy #&97                                                          ; 9732: a0 97       ..             ; High byte of scout data handler
    jmp set_nmi_vector                                                ; 9734: 4c 0e 0d    L..            ; Install scout data loop and RTI

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
; &9737 referenced 5 times by &96fb, &9718, &974c, &9780, &9782
.scout_error
    lda econet_control23_or_status2                                   ; 9737: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 973a: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 973c: f0 06       ..             ; Neither set -- clean end, discard via &9744
    jsr adlc_full_reset                                               ; 973e: 20 dc 96     ..            ; Unexpected data/status: full ADLC reset
    jmp discard_after_reset                                           ; 9741: 4c 43 9a    LC.            ; Discard and return to idle

; &9744 referenced 1 time by &973c
.scout_discard
    jmp discard_listen                                                ; 9744: 4c 40 9a    L@.            ; Gentle discard: RX_DISCONTINUE

; ***************************************************************************************
; Scout data reading loop
; 
; Reads the body of a scout frame, two bytes per iteration. Stores
; bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
; Between each pair it checks SR2:
;   - At entry (&9749): LDA SR2, BPL tests RDA (bit7)
;     - No RDA (BPL) -> error (&9737)
;     - RDA set (BMI) -> read byte
;   - After first byte (&9755): LDA SR2
;     - RDA set (BMI) -> read second byte
;     - SR2 non-zero (BNE) -> scout completion (&9771)
;       This is the FV detection point: when FV is set (by inline refill
;       of the last byte during the preceding RX FIFO read), SR2 is
;       non-zero and the branch is taken.
;     - SR2 = 0 -> RTI, wait for next NMI
;   - After second byte (&9769): LDA SR2
;     - SR2 non-zero (BNE) -> loop back to &974C
;     - SR2 = 0 -> RTI, wait for next NMI
; The loop ends at Y=&0C (12 bytes max in scout buffer).
; ***************************************************************************************
.scout_data_loop
    ldy port_buf_len                                                  ; 9747: a4 a2       ..             ; Y = buffer offset
    lda econet_control23_or_status2                                   ; 9749: ad a1 fe    ...            ; Read SR2
; &974c referenced 1 time by &976c
.scout_loop_rda
    bpl scout_error                                                   ; 974c: 10 e9       ..             ; No RDA -- error handler &9737
    lda econet_data_continue_frame                                    ; 974e: ad a2 fe    ...            ; Read data byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9751: 99 3d 0d    .=.            ; Store at &0D3D+Y (scout buffer)
    iny                                                               ; 9754: c8          .              ; Advance buffer index
    lda econet_control23_or_status2                                   ; 9755: ad a1 fe    ...            ; Read SR2 again (FV detection point)
    bmi scout_loop_second                                             ; 9758: 30 02       0.             ; RDA set -- more data, read second byte
    bne scout_complete                                                ; 975a: d0 15       ..             ; SR2 non-zero (FV or other) -- scout completion
; &975c referenced 1 time by &9758
.scout_loop_second
    lda econet_data_continue_frame                                    ; 975c: ad a2 fe    ...            ; Read second byte of pair
    sta rx_src_stn,y                                                  ; 975f: 99 3d 0d    .=.            ; Store at &0D3D+Y
    iny                                                               ; 9762: c8          .              ; Advance and check buffer limit
    cpy #&0c                                                          ; 9763: c0 0c       ..             ; Copied all 12 scout bytes?
    beq scout_complete                                                ; 9765: f0 0a       ..             ; Buffer full (Y=12) -- force completion
    sty port_buf_len                                                  ; 9767: 84 a2       ..             ; Save Y for next iteration
    lda econet_control23_or_status2                                   ; 9769: ad a1 fe    ...            ; Read SR2 for next pair
    bne scout_loop_rda                                                ; 976c: d0 de       ..             ; SR2 non-zero -- loop back for more bytes
    jmp nmi_rti                                                       ; 976e: 4c 14 0d    L..            ; SR2 = 0 -- RTI, wait for next NMI

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
; &9771 referenced 2 times by &975a, &9765
.scout_complete
    lda #0                                                            ; 9771: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 9773: 8d a0 fe    ...            ; Write CR1
    lda #&84                                                          ; 9776: a9 84       ..             ; CR2=&84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 9778: 8d a1 fe    ...            ; Write CR2
    lda #2                                                            ; 977b: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 977d: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 9780: f0 b5       ..             ; No FV -- not a valid frame end, error
    bpl scout_error                                                   ; 9782: 10 b3       ..             ; FV set but no RDA -- missing last byte, error
    lda econet_data_continue_frame                                    ; 9784: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9787: 99 3d 0d    .=.            ; Store last byte at &0D3D+Y
    lda #&44 ; 'D'                                                    ; 978a: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 978c: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    lda rx_port                                                       ; 978f: ad 40 0d    .@.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 9792: d0 06       ..             ; Port non-zero -- look for matching receive block
    jmp immediate_op                                                  ; 9794: 4c 59 9a    LY.            ; Port = 0 -- immediate operation handler

; &9797 referenced 3 times by &97e2, &97e7, &9819
.scout_no_match
    jmp rx_error                                                      ; 9797: 4c 8a 98    L..            ; Port = 0 -- immediate operation handler

; &979a referenced 1 time by &9792
.scout_match_port
    bit tx_flags                                                      ; 979a: 2c 4a 0d    ,J.            ; Check if broadcast (bit6 of tx_flags)
    bvc scan_port_list                                                ; 979d: 50 05       P.             ; Not broadcast -- skip CR2 setup
    lda #7                                                            ; 979f: a9 07       ..             ; CR2=&07: broadcast prep
    sta econet_control23_or_status2                                   ; 97a1: 8d a1 fe    ...            ; Write CR2: broadcast frame prep
; &97a4 referenced 1 time by &979d
.scan_port_list
    bit rx_status_flags                                               ; 97a4: 2c 38 0d    ,8.            ; Check if RX port list active (bit7)
    bpl scout_network_match                                           ; 97a7: 10 3b       .;             ; No active ports -- try NFS workspace
    lda #&c0                                                          ; 97a9: a9 c0       ..             ; Start scanning port list at page &C0
.scan_nfs_port_list
    sta port_ws_offset                                                ; 97ab: 85 a6       ..             ; Store page to workspace pointer low
    lda #0                                                            ; 97ad: a9 00       ..             ; A=0: no NFS workspace offset yet
    sta rx_buf_offset                                                 ; 97af: 85 a7       ..             ; Clear NFS workspace search flag
; &97b1 referenced 1 time by &97de
.check_port_slot
    ldy #0                                                            ; 97b1: a0 00       ..             ; Y=0: read control byte from start of slot
; &97b3 referenced 1 time by &97f1
.scout_ctrl_check
    lda (port_ws_offset),y                                            ; 97b3: b1 a6       ..             ; Read port control byte from slot
    beq scout_station_check                                           ; 97b5: f0 29       .)             ; Zero = end of port list, no match
    cmp #&7f                                                          ; 97b7: c9 7f       ..             ; &7F = any-port wildcard
    bne next_port_slot                                                ; 97b9: d0 1c       ..             ; Not wildcard -- check specific port match
    iny                                                               ; 97bb: c8          .              ; Y=1: advance to port byte in slot
    lda (port_ws_offset),y                                            ; 97bc: b1 a6       ..             ; Read port number from slot (offset 1)
    beq check_station_filter                                          ; 97be: f0 05       ..             ; Zero port in slot = match any port
    cmp rx_port                                                       ; 97c0: cd 40 0d    .@.            ; Check if port matches this slot
    bne next_port_slot                                                ; 97c3: d0 12       ..             ; Port mismatch -- try next slot
; &97c5 referenced 1 time by &97be
.check_station_filter
    iny                                                               ; 97c5: c8          .              ; Y=2: advance to station byte
    lda (port_ws_offset),y                                            ; 97c6: b1 a6       ..             ; Read station filter from slot (offset 2)
    beq scout_port_match                                              ; 97c8: f0 05       ..             ; Zero station = match any station, accept
    cmp rx_src_stn                                                    ; 97ca: cd 3d 0d    .=.            ; Check if source station matches
    bne next_port_slot                                                ; 97cd: d0 08       ..             ; Station mismatch -- try next slot
; &97cf referenced 1 time by &97c8
.scout_port_match
    iny                                                               ; 97cf: c8          .              ; Y=3: advance to network byte
    lda (port_ws_offset),y                                            ; 97d0: b1 a6       ..             ; Read network filter from slot (offset 3)
    cmp rx_src_net                                                    ; 97d2: cd 3e 0d    .>.            ; Check if source network matches
    beq scout_accept                                                  ; 97d5: f0 1c       ..             ; Network matches or zero = accept
; &97d7 referenced 3 times by &97b9, &97c3, &97cd
.next_port_slot
    lda port_ws_offset                                                ; 97d7: a5 a6       ..             ; Check if NFS workspace search pending
    clc                                                               ; 97d9: 18          .              ; CLC for 12-byte slot advance
    adc #&0c                                                          ; 97da: 69 0c       i.             ; Advance to next 12-byte port slot
    sta port_ws_offset                                                ; 97dc: 85 a6       ..             ; Update workspace pointer to next slot
    bcc check_port_slot                                               ; 97de: 90 d1       ..             ; Always branches (page &C0 won't overflow)
; &97e0 referenced 1 time by &97b5
.scout_station_check
    lda rx_buf_offset                                                 ; 97e0: a5 a7       ..             ; Check if NFS workspace already searched
    bne scout_no_match                                                ; 97e2: d0 b3       ..             ; Already searched: no match found
; &97e4 referenced 1 time by &97a7
.scout_network_match
    bit rx_status_flags                                               ; 97e4: 2c 38 0d    ,8.            ; Try NFS workspace if paged list exhausted
    bvc scout_no_match                                                ; 97e7: 50 ae       P.             ; No NFS workspace RX (bit6 clear) -- discard
    lda nfs_workspace_hi                                              ; 97e9: a5 9f       ..             ; Get NFS workspace page number
    sta rx_buf_offset                                                 ; 97eb: 85 a7       ..             ; Mark NFS workspace as search target
    ldy #0                                                            ; 97ed: a0 00       ..             ; Y=0: start at offset 0 in workspace
    sty port_ws_offset                                                ; 97ef: 84 a6       ..             ; Reset slot pointer to start
    beq scout_ctrl_check                                              ; 97f1: f0 c0       ..             ; ALWAYS branch

; &97f3 referenced 1 time by &97d5
.scout_accept
    bit tx_flags                                                      ; 97f3: 2c 4a 0d    ,J.            ; Check broadcast flag (bit 6)
    bvc ack_scout_match                                               ; 97f6: 50 03       P.             ; Not broadcast: ACK and set up RX
    jmp copy_scout_fields                                             ; 97f8: 4c 4a 9a    LJ.            ; Broadcast: copy scout fields directly

; &97fb referenced 2 times by &97f6, &9ac5
.ack_scout_match
    lda #3                                                            ; 97fb: a9 03       ..             ; Match found: set scout_status = 3
    sta scout_status                                                  ; 97fd: 8d 5c 0d    .\.            ; Record match for completion handler
    lda nmi_tx_block                                                  ; 9800: a5 a0       ..             ; Save current TX block ptr (low)
    pha                                                               ; 9802: 48          H              ; Push TX block low on stack
    lda nmi_tx_block_hi                                               ; 9803: a5 a1       ..             ; Save current TX block ptr (high)
    pha                                                               ; 9805: 48          H              ; Push TX block high on stack
    lda port_ws_offset                                                ; 9806: a5 a6       ..             ; Use port slot as temp RXCB ptr (lo)
    sta nmi_tx_block                                                  ; 9808: 85 a0       ..             ; Set RXCB low for tx_calc_transfer
    lda rx_buf_offset                                                 ; 980a: a5 a7       ..             ; Use workspace page as temp RXCB (hi)
    sta nmi_tx_block_hi                                               ; 980c: 85 a1       ..             ; Set RXCB high for tx_calc_transfer
    jsr tx_calc_transfer                                              ; 980e: 20 5b 9f     [.            ; Calculate transfer parameters
    pla                                                               ; 9811: 68          h              ; Restore original TX block (high)
    sta nmi_tx_block_hi                                               ; 9812: 85 a1       ..             ; Restore TX block ptr (high)
    pla                                                               ; 9814: 68          h              ; Restore original TX block (low)
    sta nmi_tx_block                                                  ; 9815: 85 a0       ..             ; Restore TX block ptr (low)
    bcs send_data_rx_ack                                              ; 9817: b0 03       ..             ; Transfer OK: send data ACK
    jmp scout_no_match                                                ; 9819: 4c 97 97    L..            ; Broadcast: different completion path

; &981c referenced 2 times by &9817, &9aba
.send_data_rx_ack
    lda #&44 ; 'D'                                                    ; 981c: a9 44       .D             ; CR1=&44: RX_RESET | TIE
    sta econet_control1_or_status1                                    ; 981e: 8d a0 fe    ...            ; Write CR1: TX mode for ACK
    lda #&a7                                                          ; 9821: a9 a7       ..             ; CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE
    sta econet_control23_or_status2                                   ; 9823: 8d a1 fe    ...            ; Write CR2: enable TX with PSE
    lda #&2d ; '-'                                                    ; 9826: a9 2d       .-             ; Install data_rx_setup at &982D
    ldy #&98                                                          ; 9828: a0 98       ..             ; High byte of data_rx_setup handler
    jmp ack_tx_write_dest                                             ; 982a: 4c 74 99    Lt.            ; Send ACK with data_rx_setup as next NMI

.data_rx_setup
    lda #&82                                                          ; 982d: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 982f: 8d a0 fe    ...            ; Write CR1: switch to RX for data frame
    lda #&39 ; '9'                                                    ; 9832: a9 39       .9             ; Install nmi_data_rx at &9839
    ldy #&98                                                          ; 9834: a0 98       ..             ; High byte of nmi_data_rx handler
    jmp set_nmi_vector                                                ; 9836: 4c 0e 0d    L..            ; Install nmi_data_rx and return from NMI

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
    lda #1                                                            ; 9839: a9 01       ..             ; A=&01: mask for AP (Address Present)
    bit econet_control23_or_status2                                   ; 983b: 2c a1 fe    ,..            ; BIT SR2: test AP bit
    beq rx_error                                                      ; 983e: f0 4a       .J             ; No AP: wrong frame or error
    lda econet_data_continue_frame                                    ; 9840: ad a2 fe    ...            ; Read first byte (dest station)
    cmp station_id_disable_net_nmis                                   ; 9843: cd 18 fe    ...            ; Compare to our station ID (INTOFF)
    bne rx_error                                                      ; 9846: d0 42       .B             ; Not for us: error path
    lda #&4f ; 'O'                                                    ; 9848: a9 4f       .O             ; Install net check handler at &984F
    ldy #&98                                                          ; 984a: a0 98       ..             ; High byte of nmi_data_rx_net handler
    jmp set_nmi_vector                                                ; 984c: 4c 0e 0d    L..            ; Set NMI vector via RAM shim

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 984f: 2c a1 fe    ,..            ; Validate source network = 0
    bpl rx_error                                                      ; 9852: 10 36       .6             ; SR2 bit7 clear: no data ready -- error
    lda econet_data_continue_frame                                    ; 9854: ad a2 fe    ...            ; Read dest network byte
    bne rx_error                                                      ; 9857: d0 31       .1             ; Network != 0: wrong network -- error
    lda #&65 ; 'e'                                                    ; 9859: a9 65       .e             ; Install skip handler at &9865
    ldy #&98                                                          ; 985b: a0 98       ..             ; High byte of &9865 handler
    bit econet_control1_or_status1                                    ; 985d: 2c a0 fe    ,..            ; SR1 bit7: IRQ, data already waiting
    bmi nmi_data_rx_skip                                              ; 9860: 30 03       0.             ; Data ready: skip directly, no RTI
    jmp set_nmi_vector                                                ; 9862: 4c 0e 0d    L..            ; Install handler and return via RTI

; &9865 referenced 1 time by &9860
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 9865: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl rx_error                                                      ; 9868: 10 20       .              ; SR2 bit7 clear: error
    lda econet_data_continue_frame                                    ; 986a: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 986d: ad a2 fe    ...            ; Discard port byte
; ***************************************************************************************
; Install data RX bulk or Tube handler
; 
; Selects either the normal bulk RX handler (&989A) or the Tube
; RX handler (&98F7) based on the Tube transfer flag in tx_flags,
; and installs the appropriate NMI handler.
; ***************************************************************************************
; &9870 referenced 1 time by &9f2f
.install_data_rx_handler
    lda #2                                                            ; 9870: a9 02       ..             ; A=2: Tube transfer flag mask
    bit tx_flags                                                      ; 9872: 2c 4a 0d    ,J.            ; Check if Tube transfer active
    bne install_tube_rx                                               ; 9875: d0 0c       ..             ; Tube active: use Tube RX path
    lda #&9a                                                          ; 9877: a9 9a       ..             ; Install bulk read at &989A
    ldy #&98                                                          ; 9879: a0 98       ..             ; High byte of &989A handler
    bit econet_control1_or_status1                                    ; 987b: 2c a0 fe    ,..            ; SR1 bit7: more data already waiting?
    bmi nmi_data_rx_bulk                                              ; 987e: 30 1a       0.             ; Yes: enter bulk read directly
    jmp set_nmi_vector                                                ; 9880: 4c 0e 0d    L..            ; No: install handler and RTI

; &9883 referenced 1 time by &9875
.install_tube_rx
    lda #&f7                                                          ; 9883: a9 f7       ..             ; Tube: install Tube RX at &98F7
    ldy #&98                                                          ; 9885: a0 98       ..             ; High byte of &98F7 handler
    jmp set_nmi_vector                                                ; 9887: 4c 0e 0d    L..            ; Install Tube handler and RTI

; ***************************************************************************************
; NMI error handler dispatch
; 
; Common error/abort entry used by 12 call sites. Checks
; tx_flags bit 7: if clear, does a full ADLC reset and returns
; to idle listen (RX error path); if set, jumps to tx_result_fail
; (TX not-listening path).
; ***************************************************************************************
; &988a referenced 12 times by &9797, &983e, &9846, &9852, &9857, &9868, &98ad, &98df, &98e5, &9930, &99b8, &9a8c
.rx_error
.nmi_error_dispatch
    lda tx_flags                                                      ; 988a: ad 4a 0d    .J.            ; Check tx_flags for error path
    bpl rx_error_reset                                                ; 988d: 10 05       ..             ; Bit7 clear: RX error path
    lda #&41 ; 'A'                                                    ; 988f: a9 41       .A             ; A=&41: 'not listening' error
    jmp tx_store_result                                               ; 9891: 4c 3f 9f    L?.            ; Bit7 set: TX result = not listening

; &9894 referenced 1 time by &988d
.rx_error_reset
    jsr adlc_full_reset                                               ; 9894: 20 dc 96     ..            ; Full ADLC reset on RX error
    jmp discard_reset_listen                                          ; 9897: 4c 34 9a    L4.            ; Discard and return to idle listen

; ***************************************************************************************
; Data frame bulk read loop
; 
; Reads data payload bytes from the RX FIFO and stores them into
; the open port buffer at (open_port_buf),Y. Reads bytes in pairs
; (like the scout data loop), checking SR2 between each pair.
; SR2 non-zero (FV or other) -> frame completion at &98CE.
; SR2 = 0 -> RTI, wait for next NMI to continue.
; ***************************************************************************************
; &989a referenced 1 time by &987e
.nmi_data_rx_bulk
    ldy port_buf_len                                                  ; 989a: a4 a2       ..             ; Y = buffer offset, resume from last position
    lda econet_control23_or_status2                                   ; 989c: ad a1 fe    ...            ; Read SR2 for next pair
; &989f referenced 1 time by &98c9
.data_rx_loop
    bpl data_rx_complete                                              ; 989f: 10 2d       .-             ; SR2 bit7 clear: frame complete (FV)
    lda econet_data_continue_frame                                    ; 98a1: ad a2 fe    ...            ; Read first byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 98a4: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 98a6: c8          .              ; Advance buffer offset
    bne read_sr2_between_pairs                                        ; 98a7: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 98a9: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 98ab: c6 a3       ..             ; Decrement remaining page count
    beq rx_error                                                      ; 98ad: f0 db       ..             ; No pages left: handle as complete
; &98af referenced 1 time by &98a7
.read_sr2_between_pairs
    lda econet_control23_or_status2                                   ; 98af: ad a1 fe    ...            ; Read SR2 between byte pairs
    bmi read_second_rx_byte                                           ; 98b2: 30 02       0.             ; SR2 bit7 set: more data available
    bne data_rx_complete                                              ; 98b4: d0 18       ..             ; SR2 non-zero, bit7 clear: frame done
; &98b6 referenced 1 time by &98b2
.read_second_rx_byte
    lda econet_data_continue_frame                                    ; 98b6: ad a2 fe    ...            ; Read second byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 98b9: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 98bb: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 98bc: 84 a2       ..             ; Save updated buffer position
    bne check_sr2_loop_again                                          ; 98be: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 98c0: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 98c2: c6 a3       ..             ; Decrement remaining page count
    beq data_rx_complete                                              ; 98c4: f0 08       ..             ; No pages left: frame complete
; &98c6 referenced 1 time by &98be
.check_sr2_loop_again
    lda econet_control23_or_status2                                   ; 98c6: ad a1 fe    ...            ; Read SR2 for next iteration
    bne data_rx_loop                                                  ; 98c9: d0 d4       ..             ; SR2 non-zero: more data, loop back
    jmp nmi_rti                                                       ; 98cb: 4c 14 0d    L..            ; SR2=0: no more data yet, wait for NMI

; ***************************************************************************************
; Data frame completion
; 
; Reached when SR2 non-zero during data RX (FV detected).
; Same pattern as scout completion (&9771): disables PSE (CR1=&00,
; CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
; If extra data available and buffer space remains, stores it.
; Proceeds to send the final ACK via &995E.
; ***************************************************************************************
; &98ce referenced 3 times by &989f, &98b4, &98c4
.data_rx_complete
    lda #0                                                            ; 98ce: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 98d0: 8d a0 fe    ...            ; Write CR1
    lda #&84                                                          ; 98d3: a9 84       ..             ; CR2=&84: disable PSE for individual bit testing
    sta econet_control23_or_status2                                   ; 98d5: 8d a1 fe    ...            ; Write CR2
    sty port_buf_len                                                  ; 98d8: 84 a2       ..             ; Save Y (byte count from data RX loop)
    lda #2                                                            ; 98da: a9 02       ..             ; A=&02: FV mask
    bit econet_control23_or_status2                                   ; 98dc: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq rx_error                                                      ; 98df: f0 a9       ..             ; No FV -- error
    bpl send_ack                                                      ; 98e1: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 98e3: a5 a3       ..             ; Check if buffer space remains
.read_last_rx_byte
    beq rx_error                                                      ; 98e5: f0 a3       ..             ; No buffer space: error/discard frame
    lda econet_data_continue_frame                                    ; 98e7: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 98ea: a4 a2       ..             ; Y = current buffer write offset
    sta (open_port_buf),y                                             ; 98ec: 91 a4       ..             ; Store last byte in port receive buffer
    inc port_buf_len                                                  ; 98ee: e6 a2       ..             ; Advance buffer write offset
    bne send_ack                                                      ; 98f0: d0 02       ..             ; No page wrap: proceed to send ACK
    inc open_port_buf_hi                                              ; 98f2: e6 a5       ..             ; Page boundary: advance buffer page
; &98f4 referenced 2 times by &98e1, &98f0
.send_ack
    jmp ack_tx                                                        ; 98f4: 4c 5e 99    L^.            ; Send ACK frame to complete handshake

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 98f7: ad a1 fe    ...            ; Read SR2 for Tube data receive path
; &98fa referenced 1 time by &992b
.rx_tube_data
    bpl data_rx_tube_complete                                         ; 98fa: 10 37       .7             ; RDA clear: no more data, frame complete
    lda econet_data_continue_frame                                    ; 98fc: ad a2 fe    ...            ; Read data byte from ADLC RX FIFO
    inc port_buf_len                                                  ; 98ff: e6 a2       ..             ; Advance Tube transfer byte count
    sta tube_data_register_3                                          ; 9901: 8d e5 fe    ...            ; Send byte to Tube data register 3
    bne rx_update_buf                                                 ; 9904: d0 0c       ..             ; No overflow: read second byte
    inc port_buf_len_hi                                               ; 9906: e6 a3       ..             ; Carry to transfer count byte 2
    bne rx_update_buf                                                 ; 9908: d0 08       ..             ; No overflow: read second byte
    inc open_port_buf                                                 ; 990a: e6 a4       ..             ; Carry to transfer count byte 3
    bne rx_update_buf                                                 ; 990c: d0 04       ..             ; No overflow: read second byte
    inc open_port_buf_hi                                              ; 990e: e6 a5       ..             ; Carry to transfer count byte 4
    beq data_rx_tube_error                                            ; 9910: f0 1e       ..             ; All bytes zero: overflow error
; &9912 referenced 3 times by &9904, &9908, &990c
.rx_update_buf
    lda econet_data_continue_frame                                    ; 9912: ad a2 fe    ...            ; Read second data byte (paired transfer)
    sta tube_data_register_3                                          ; 9915: 8d e5 fe    ...            ; Send second byte to Tube
    inc port_buf_len                                                  ; 9918: e6 a2       ..             ; Advance count after second byte
    bne rx_check_error                                                ; 991a: d0 0c       ..             ; No overflow: check for more data
    inc port_buf_len_hi                                               ; 991c: e6 a3       ..             ; Carry to count byte 2
    bne rx_check_error                                                ; 991e: d0 08       ..             ; No overflow: check for more data
    inc open_port_buf                                                 ; 9920: e6 a4       ..             ; Carry to count byte 3
    bne rx_check_error                                                ; 9922: d0 04       ..             ; No overflow: check for more data
    inc open_port_buf_hi                                              ; 9924: e6 a5       ..             ; Carry to count byte 4
    beq data_rx_tube_complete                                         ; 9926: f0 0b       ..             ; Zero: Tube transfer complete
; &9928 referenced 3 times by &991a, &991e, &9922
.rx_check_error
    lda econet_control23_or_status2                                   ; 9928: ad a1 fe    ...            ; Re-read SR2 for next byte pair
    bne rx_tube_data                                                  ; 992b: d0 cd       ..             ; More data available: continue loop
    jmp nmi_rti                                                       ; 992d: 4c 14 0d    L..            ; Return from NMI, wait for data

; &9930 referenced 3 times by &9910, &9942, &994e
.data_rx_tube_error
    jmp rx_error                                                      ; 9930: 4c 8a 98    L..            ; Unexpected end: return from NMI

; &9933 referenced 2 times by &98fa, &9926
.data_rx_tube_complete
    lda #0                                                            ; 9933: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 9935: 8d a0 fe    ...            ; Write CR1 for individual bit testing
    lda #&84                                                          ; 9938: a9 84       ..             ; CR2=&84: disable PSE
    sta econet_control23_or_status2                                   ; 993a: 8d a1 fe    ...            ; Write CR2: same pattern as main path
    lda #2                                                            ; 993d: a9 02       ..             ; A=&02: FV mask for Tube completion
    bit econet_control23_or_status2                                   ; 993f: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq data_rx_tube_error                                            ; 9942: f0 ec       ..             ; No FV: incomplete frame, error
    bpl ack_tx                                                        ; 9944: 10 18       ..             ; FV set, no RDA: proceed to ACK
    lda port_buf_len                                                  ; 9946: a5 a2       ..             ; Check if any buffer was allocated
    ora port_buf_len_hi                                               ; 9948: 05 a3       ..             ; OR all 4 buffer pointer bytes together
    ora open_port_buf                                                 ; 994a: 05 a4       ..             ; Check buffer low byte
    ora open_port_buf_hi                                              ; 994c: 05 a5       ..             ; Check buffer high byte
    beq data_rx_tube_error                                            ; 994e: f0 e0       ..             ; All zero (null buffer): error
    lda econet_data_continue_frame                                    ; 9950: ad a2 fe    ...            ; Read extra trailing byte from FIFO
    sta rx_extra_byte                                                 ; 9953: 8d 5d 0d    .].            ; Save extra byte at &0D5D for later use
    lda #&20 ; ' '                                                    ; 9956: a9 20       .              ; Bit5 = extra data byte available flag
    ora tx_flags                                                      ; 9958: 0d 4a 0d    .J.            ; Set extra byte flag in tx_flags
    sta tx_flags                                                      ; 995b: 8d 4a 0d    .J.            ; Store updated flags
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
; &995e referenced 2 times by &98f4, &9944
.ack_tx
    lda tx_flags                                                      ; 995e: ad 4a 0d    .J.            ; Load TX flags to check ACK type
    bpl ack_tx_configure                                              ; 9961: 10 03       ..             ; Bit7 clear: normal scout ACK
    jmp tx_result_ok                                                  ; 9963: 4c 39 9f    L9.            ; Jump to TX success result

; &9966 referenced 1 time by &9961
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 9966: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 9968: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    lda #&a7                                                          ; 996b: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 996d: 8d a1 fe    ...            ; Write CR2: enable TX with status clear
    lda #&bb                                                          ; 9970: a9 bb       ..             ; Install saved next handler (&99BB for scout ACK)
    ldy #&99                                                          ; 9972: a0 99       ..             ; High byte of post-ACK handler
; &9974 referenced 2 times by &982a, &9b0f
.ack_tx_write_dest
    sta nmi_next_lo                                                   ; 9974: 8d 4b 0d    .K.            ; Store next handler low byte
    sty nmi_next_hi                                                   ; 9977: 8c 4c 0d    .L.            ; Store next handler high byte
    lda rx_src_stn                                                    ; 997a: ad 3d 0d    .=.            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 997d: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc tdra_error                                                    ; 9980: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9982: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda rx_src_net                                                    ; 9985: ad 3e 0d    .>.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9988: 8d a2 fe    ...            ; Write dest net byte to FIFO
    lda #&92                                                          ; 998b: a9 92       ..             ; Install handler at &9992 (write src addr)
    ldy #&99                                                          ; 998d: a0 99       ..             ; High byte of nmi_ack_tx_src
    jmp set_nmi_vector                                                ; 998f: 4c 0e 0d    L..            ; Set NMI vector to ack_tx_src handler

; ***************************************************************************************
; ACK TX continuation
; 
; Writes source station and network to TX FIFO, completing the 4-byte
; ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 9992: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9995: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc tdra_error                                                    ; 9998: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 999a: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 999d: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 999f: 8d a2 fe    ...            ; Write network=0 (local) to TX FIFO
    lda tx_flags                                                      ; 99a2: ad 4a 0d    .J.            ; Check tx_flags for data phase
    bmi start_data_tx                                                 ; 99a5: 30 0e       0.             ; bit7 set: start data TX phase
    lda #&3f ; '?'                                                    ; 99a7: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 99a9: 8d a1 fe    ...            ; Write CR2 to clear status after ACK TX
    lda nmi_next_lo                                                   ; 99ac: ad 4b 0d    .K.            ; Install saved handler from &0D4B/&0D4C
    ldy nmi_next_hi                                                   ; 99af: ac 4c 0d    .L.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 99b2: 4c 0e 0d    L..            ; Install next NMI handler

; &99b5 referenced 1 time by &99a5
.start_data_tx
    jmp data_tx_begin                                                 ; 99b5: 4c 3b 9e    L;.            ; Jump to start data TX phase

; &99b8 referenced 2 times by &9980, &9998
.tdra_error
    jmp rx_error                                                      ; 99b8: 4c 8a 98    L..            ; TDRA error: jump to error handler

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
    lda rx_port                                                       ; 99bb: ad 40 0d    .@.            ; Check port byte from scout
    bne advance_rx_buffer_ptr                                         ; 99be: d0 03       ..             ; Non-zero port: advance RX buffer
.dispatch_nmi_error
    jmp check_imm_op_ctrl                                             ; 99c0: 4c 12 9b    L..            ; Jump to error handler

; ***************************************************************************************
; Advance RX buffer pointer after transfer
; 
; Adds the transfer count to the RXCB buffer pointer (4-byte
; addition). If a Tube transfer is active, re-claims the Tube
; address and sends the extra RX byte via R3, incrementing the
; Tube pointer by 1.
; ***************************************************************************************
; &99c3 referenced 1 time by &99be
.advance_rx_buffer_ptr
    lda #2                                                            ; 99c3: a9 02       ..             ; A=2: test bit1 of tx_flags
    bit tx_flags                                                      ; 99c5: 2c 4a 0d    ,J.            ; BIT tx_flags: check data transfer bit
    beq add_buf_to_base                                               ; 99c8: f0 3d       .=             ; Bit1 clear: no transfer -- return
    clc                                                               ; 99ca: 18          .              ; CLC: init carry for 4-byte add
    php                                                               ; 99cb: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 99cc: a0 08       ..             ; Y=8: RXCB high pointer offset
; &99ce referenced 1 time by &99da
.add_rxcb_ptr
    lda (port_ws_offset),y                                            ; 99ce: b1 a6       ..             ; Load RXCB[Y] (buffer pointer byte)
    plp                                                               ; 99d0: 28          (              ; Restore carry from stack
    adc net_tx_ptr,y                                                  ; 99d1: 79 9a 00    y..            ; Add transfer count byte
    sta (port_ws_offset),y                                            ; 99d4: 91 a6       ..             ; Store updated pointer back to RXCB
    iny                                                               ; 99d6: c8          .              ; Next byte
    php                                                               ; 99d7: 08          .              ; Save carry for next iteration
    cpy #&0c                                                          ; 99d8: c0 0c       ..             ; Done 4 bytes? (Y reaches &0C)
    bcc add_rxcb_ptr                                                  ; 99da: 90 f2       ..             ; No: continue adding
    plp                                                               ; 99dc: 28          (              ; Discard final carry
    lda #&20 ; ' '                                                    ; 99dd: a9 20       .              ; A=&20: test bit5 of tx_flags
    bit tx_flags                                                      ; 99df: 2c 4a 0d    ,J.            ; BIT tx_flags: check Tube bit
    beq jmp_store_rxcb                                                ; 99e2: f0 20       .              ; No Tube: skip Tube update
    txa                                                               ; 99e4: 8a          .              ; Save X on stack
    pha                                                               ; 99e5: 48          H              ; Push X
    lda #8                                                            ; 99e6: a9 08       ..             ; A=8: offset for Tube address
    clc                                                               ; 99e8: 18          .              ; CLC for address calculation
    adc port_ws_offset                                                ; 99e9: 65 a6       e.             ; Add workspace base offset
    tax                                                               ; 99eb: aa          .              ; X = address low for Tube claim
    ldy rx_buf_offset                                                 ; 99ec: a4 a7       ..             ; Y = address high for Tube claim
    lda #1                                                            ; 99ee: a9 01       ..             ; A=1: Tube claim type (read)
    jsr tube_addr_claim                                               ; 99f0: 20 06 04     ..            ; Claim Tube address for transfer
    lda rx_extra_byte                                                 ; 99f3: ad 5d 0d    .].            ; Load extra RX data byte
    sta tube_data_register_3                                          ; 99f6: 8d e5 fe    ...            ; Send to Tube via R3
    pla                                                               ; 99f9: 68          h              ; Restore X from stack
    tax                                                               ; 99fa: aa          .              ; Transfer to X register
    ldy #8                                                            ; 99fb: a0 08       ..             ; Y=8: RXCB buffer ptr offset
    lda (port_ws_offset),y                                            ; 99fd: b1 a6       ..             ; Load current RXCB buffer ptr lo
    sec                                                               ; 99ff: 38          8              ; SEC for ADC #0 = add carry
    adc #0                                                            ; 9a00: 69 00       i.             ; Increment by 1 (Tube extra byte)
    sta (port_ws_offset),y                                            ; 9a02: 91 a6       ..             ; Store updated ptr back to RXCB
; &9a04 referenced 1 time by &99e2
.jmp_store_rxcb
    jmp store_rxcb_completion                                         ; 9a04: 4c 19 9a    L..            ; Other port-0 ops: immediate dispatch

; &9a07 referenced 1 time by &99c8
.add_buf_to_base
    lda port_buf_len                                                  ; 9a07: a5 a2       ..             ; Load buffer bytes remaining
    clc                                                               ; 9a09: 18          .              ; CLC for address add
    adc open_port_buf                                                 ; 9a0a: 65 a4       e.             ; Add to buffer base address
    bcc store_buf_ptr_lo                                              ; 9a0c: 90 02       ..             ; No carry: skip high byte increment
; &9a0e referenced 1 time by &9a87
.inc_rxcb_buf_hi
    inc open_port_buf_hi                                              ; 9a0e: e6 a5       ..             ; Carry: increment buffer high byte
; &9a10 referenced 1 time by &9a0c
.store_buf_ptr_lo
    ldy #8                                                            ; 9a10: a0 08       ..             ; Y=8: store updated buffer position
.store_rxcb_buf_ptr
    sta (port_ws_offset),y                                            ; 9a12: 91 a6       ..             ; Store updated low byte to RXCB
    iny                                                               ; 9a14: c8          .              ; Y=9: buffer high byte offset
.load_rxcb_buf_hi
rxcb_buf_hi_operand = load_rxcb_buf_hi+1
    lda open_port_buf_hi                                              ; 9a15: a5 a5       ..             ; Load updated buffer high byte
; &9a16 referenced 1 time by &9a83
.store_rxcb_buf_hi
    sta (port_ws_offset),y                                            ; 9a17: 91 a6       ..             ; Store high byte to RXCB
; ***************************************************************************************
; Store RXCB completion fields from scout buffer
; 
; Writes source network, source station, port, and control
; byte from the scout buffer into the active RXCB. Sets
; bit 7 of the control byte to mark reception complete.
; ***************************************************************************************
; &9a19 referenced 2 times by &9a04, &9a56
.store_rxcb_completion
    lda rx_src_net                                                    ; 9a19: ad 3e 0d    .>.            ; Load source network from scout buffer
    ldy #3                                                            ; 9a1c: a0 03       ..             ; Y=3: RXCB source network offset
    sta (port_ws_offset),y                                            ; 9a1e: 91 a6       ..             ; Store source network to RXCB
    dey                                                               ; 9a20: 88          .              ; Y=2: source station offset; Y=&02
    lda rx_src_stn                                                    ; 9a21: ad 3d 0d    .=.            ; Load source station from scout buffer
    sta (port_ws_offset),y                                            ; 9a24: 91 a6       ..             ; Store source station to RXCB
    dey                                                               ; 9a26: 88          .              ; Y=1: port byte offset; Y=&01
    lda rx_port                                                       ; 9a27: ad 40 0d    .@.            ; Load port byte
    sta (port_ws_offset),y                                            ; 9a2a: 91 a6       ..             ; Store port to RXCB
    dey                                                               ; 9a2c: 88          .              ; Y=0: control/flag byte offset; Y=&00
    lda rx_ctrl                                                       ; 9a2d: ad 3f 0d    .?.            ; Load control byte from scout
    ora #&80                                                          ; 9a30: 09 80       ..             ; Set bit7 = reception complete flag
    sta (port_ws_offset),y                                            ; 9a32: 91 a6       ..             ; Store to RXCB (marks CB as complete)
; ***************************************************************************************
; Discard with full ADLC reset
; 
; Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
; then falls through to discard_after_reset. Used when the ADLC is
; in an unexpected state and needs a hard reset before returning
; to idle listen mode. 5 references — the main error recovery path.
; ***************************************************************************************
; &9a34 referenced 4 times by &9897, &9b4f, &9e93, &9f48
.discard_reset_listen
    lda #2                                                            ; 9a34: a9 02       ..             ; Tube flag bit 1 AND tx_flags bit 1
    bit tx_flags                                                      ; 9a36: 2c 4a 0d    ,J.            ; Test tx_flags for Tube transfer
    beq discard_listen                                                ; 9a39: f0 05       ..             ; No Tube transfer active -- skip release
    lda #&82                                                          ; 9a3b: a9 82       ..             ; A=&82: Tube release claim type
    jsr tube_addr_claim                                               ; 9a3d: 20 06 04     ..            ; Release Tube claim before discarding
; ***************************************************************************************
; Discard frame (gentle)
; 
; Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
; current frame reception without a full reset, then falls through
; to discard_after_reset. Used for clean rejection of frames that
; are correctly formatted but not for us (wrong station/network).
; ***************************************************************************************
; &9a40 referenced 2 times by &9744, &9a39
.discard_listen
    jsr adlc_rx_listen                                                ; 9a40: 20 eb 96     ..            ; Re-enter idle RX listen mode
; ***************************************************************************************
; Return to idle listen after reset/discard
; 
; Just calls adlc_rx_listen (CR1=&82, CR2=&67) to re-enter idle
; RX mode, then RTI. The simplest of the three discard paths —
; used as the tail of both discard_reset_listen and discard_listen.
; ***************************************************************************************
; &9a43 referenced 2 times by &9728, &9741
.discard_after_reset
.install_rx_scout_handler
    lda #&f6                                                          ; 9a43: a9 f6       ..             ; Install nmi_rx_scout (&96F6) as NMI handler
    ldy #&96                                                          ; 9a45: a0 96       ..             ; High byte of nmi_rx_scout
    jmp set_nmi_vector                                                ; 9a47: 4c 0e 0d    L..            ; Set NMI vector and return

; &9a4a referenced 1 time by &97f8
.copy_scout_fields
    ldy #4                                                            ; 9a4a: a0 04       ..             ; Y=4: start at RX CB offset 4
; &9a4c referenced 1 time by &9a54
.copy_scout_loop
    lda rx_src_stn,y                                                  ; 9a4c: b9 3d 0d    .=.            ; Load scout field (stn/net/ctrl/port)
    sta (port_ws_offset),y                                            ; 9a4f: 91 a6       ..             ; Store to port workspace buffer
    iny                                                               ; 9a51: c8          .              ; Advance buffer pointer
    cpy #&0c                                                          ; 9a52: c0 0c       ..             ; All 8 fields copied?
    bne copy_scout_loop                                               ; 9a54: d0 f6       ..             ; No: continue copy loop
    jmp store_rxcb_completion                                         ; 9a56: 4c 19 9a    L..            ; Jump to completion handler

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
; &9a59 referenced 1 time by &9794
.immediate_op
    ldy rx_ctrl                                                       ; 9a59: ac 3f 0d    .?.            ; Control byte &81-&88 range check
    cpy #&81                                                          ; 9a5c: c0 81       ..             ; Below &81: not an immediate op
    bcc imm_op_out_of_range                                           ; 9a5e: 90 2c       .,             ; Out of range low: jump to discard
    cpy #&89                                                          ; 9a60: c0 89       ..             ; Above &88: not an immediate op
    bcs imm_op_out_of_range                                           ; 9a62: b0 28       .(             ; Out of range high: jump to discard
    cpy #&87                                                          ; 9a64: c0 87       ..             ; HALT(&87)/CONTINUE(&88) skip protection
    bcs imm_op_dispatch                                               ; 9a66: b0 18       ..             ; Ctrl >= &87: dispatch without mask check
    lda rx_src_stn                                                    ; 9a68: ad 3d 0d    .=.            ; Load source station number
    cmp #&f0                                                          ; 9a6b: c9 f0       ..             ; Station >= &F0? (privileged)
    bcs imm_op_dispatch                                               ; 9a6d: b0 11       ..             ; Privileged: skip protection check
    tya                                                               ; 9a6f: 98          .              ; Convert ctrl byte to 0-based index for mask
    sec                                                               ; 9a70: 38          8              ; SEC for subtract
    sbc #&81                                                          ; 9a71: e9 81       ..             ; A = ctrl - &81 (0-based operation index)
    tay                                                               ; 9a73: a8          .              ; Y = index for mask rotation count
    lda prot_status                                                   ; 9a74: ad 63 0d    .c.            ; Load protection mask from LSTAT
; &9a77 referenced 1 time by &9a79
.rotate_prot_mask
    ror a                                                             ; 9a77: 6a          j              ; Rotate mask right by control byte index
    dey                                                               ; 9a78: 88          .              ; Decrement rotation counter
    bpl rotate_prot_mask                                              ; 9a79: 10 fc       ..             ; Loop until bit aligned
    bcc imm_op_dispatch                                               ; 9a7b: 90 03       ..             ; Carry clear: operation permitted
    jmp imm_op_discard                                                ; 9a7d: 4c 4f 9b    LO.            ; Operation blocked by LSTAT mask

; &9a80 referenced 3 times by &9a66, &9a6d, &9a7b
.imm_op_dispatch
    ldy rx_ctrl                                                       ; 9a80: ac 3f 0d    .?.            ; Reload ctrl byte for dispatch table
    lda rxcb_buf_hi_operand,y                                         ; 9a83: b9 16 9a    ...            ; Look up handler address high byte
    pha                                                               ; 9a86: 48          H              ; Push handler address high
    lda inc_rxcb_buf_hi,y                                             ; 9a87: b9 0e 9a    ...            ; Load handler low byte from jump table
    pha                                                               ; 9a8a: 48          H              ; Push handler address low
    rts                                                               ; 9a8b: 60          `              ; RTS dispatches to handler

; &9a8c referenced 2 times by &9a5e, &9a62
.imm_op_out_of_range
    jmp rx_error                                                      ; 9a8c: 4c 8a 98    L..            ; Jump to discard handler

    equb <(rx_imm_peek-1)                                             ; 9a8f: da          .
    equb <(rx_imm_poke-1)                                             ; 9a90: bc          .
    equb <(rx_imm_exec-1)                                             ; 9a91: 9e          .
    equb <(rx_imm_exec-1)                                             ; 9a92: 9e          .
    equb <(rx_imm_exec-1)                                             ; 9a93: 9e          .
    equb <(rx_imm_halt_cont-1)                                        ; 9a94: 00          .
    equb <(rx_imm_halt_cont-1)                                        ; 9a95: 00          .
    equb <(rx_imm_machine_type-1)                                     ; 9a96: c7          .
    equb >(rx_imm_peek-1)                                             ; 9a97: 9a          .
    equb >(rx_imm_poke-1)                                             ; 9a98: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a99: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a9a: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9a9b: 9a          .
    equb >(rx_imm_halt_cont-1)                                        ; 9a9c: 9b          .
    equb >(rx_imm_halt_cont-1)                                        ; 9a9d: 9b          .
    equb >(rx_imm_machine_type-1)                                     ; 9a9e: 9a          .

; ***************************************************************************************
; RX immediate: JSR/UserProc/OSProc setup
; 
; Sets up the port buffer to receive remote procedure data.
; Copies the 4-byte remote address from rx_remote_addr into
; the execution address workspace, then jumps to the common
; receive path. Used for operation types &83-&85.
; ***************************************************************************************
.rx_imm_exec
    lda #0                                                            ; 9a9f: a9 00       ..             ; Buffer start lo = &00
    sta open_port_buf                                                 ; 9aa1: 85 a4       ..             ; Set port buffer lo
    lda #&82                                                          ; 9aa3: a9 82       ..             ; Buffer length lo = &82
    sta port_buf_len                                                  ; 9aa5: 85 a2       ..             ; Set buffer length lo
    lda #1                                                            ; 9aa7: a9 01       ..             ; Buffer length hi = 1
    sta port_buf_len_hi                                               ; 9aa9: 85 a3       ..             ; Set buffer length hi
    lda net_rx_ptr_hi                                                 ; 9aab: a5 9d       ..             ; Load RX page hi for buffer
    sta open_port_buf_hi                                              ; 9aad: 85 a5       ..             ; Set port buffer hi
    ldy #3                                                            ; 9aaf: a0 03       ..             ; Y=3: copy 4 bytes (3 down to 0)
; &9ab1 referenced 1 time by &9ab8
.copy_addr_loop
    lda rx_remote_addr,y                                              ; 9ab1: b9 41 0d    .A.            ; Load remote address byte
    sta l0d58,y                                                       ; 9ab4: 99 58 0d    .X.            ; Store to exec address workspace
    dey                                                               ; 9ab7: 88          .              ; Next byte (descending)
    bpl copy_addr_loop                                                ; 9ab8: 10 f7       ..             ; Loop until all 4 bytes copied
    jmp send_data_rx_ack                                              ; 9aba: 4c 1c 98    L..            ; Enter common data-receive path

; ***************************************************************************************
; RX immediate: POKE setup
; 
; Sets up workspace offsets for receiving POKE data, then
; jumps to the common data-receive path.
; ***************************************************************************************
.rx_imm_poke
    lda #&3d ; '='                                                    ; 9abd: a9 3d       .=             ; Port workspace offset = &3D
    sta port_ws_offset                                                ; 9abf: 85 a6       ..             ; Store workspace offset lo
    lda #&0d                                                          ; 9ac1: a9 0d       ..             ; RX buffer page = &0D
    sta rx_buf_offset                                                 ; 9ac3: 85 a7       ..             ; Store workspace offset hi
    jmp ack_scout_match                                               ; 9ac5: 4c fb 97    L..            ; Enter POKE data-receive path

; ***************************************************************************************
; RX immediate: machine type query
; 
; Sets up a buffer at &7F21 (length #&01FC) for the machine
; type query response. Returns system identification data
; to the remote station.
; ***************************************************************************************
.rx_imm_machine_type
    lda #1                                                            ; 9ac8: a9 01       ..             ; Buffer length hi = 1
    sta port_buf_len_hi                                               ; 9aca: 85 a3       ..             ; Set buffer length hi
    lda #&fc                                                          ; 9acc: a9 fc       ..             ; Buffer length lo = &FC
    sta port_buf_len                                                  ; 9ace: 85 a2       ..             ; Set buffer length lo
    lda #&21 ; '!'                                                    ; 9ad0: a9 21       .!             ; Buffer start lo = &25
    sta open_port_buf                                                 ; 9ad2: 85 a4       ..             ; Set port buffer lo
    lda #&7f                                                          ; 9ad4: a9 7f       ..             ; Buffer hi = &7F (below screen)
    sta open_port_buf_hi                                              ; 9ad6: 85 a5       ..             ; Set port buffer hi
    jmp set_tx_reply_flag                                             ; 9ad8: 4c f9 9a    L..            ; Enter reply build path

; ***************************************************************************************
; RX immediate: PEEK setup
; 
; Saves the current TX block pointer, replaces it with a
; pointer to the workspace, and prepares to send the PEEK
; response data back to the requesting station.
; ***************************************************************************************
.rx_imm_peek
    lda nmi_tx_block                                                  ; 9adb: a5 a0       ..             ; Save current TX block low byte
    pha                                                               ; 9add: 48          H              ; Push to stack
    lda nmi_tx_block_hi                                               ; 9ade: a5 a1       ..             ; Save current TX block high byte
    pha                                                               ; 9ae0: 48          H              ; Push to stack
; ***************************************************************************************
; RX immediate: PEEK setup
; 
; Writes &0D3D to port_ws_offset/rx_buf_offset, sets
; scout_status=2, then calls tx_calc_transfer to send the
; PEEK response data back to the requesting station.
; Uses workspace offsets (&A6/&A7) for nmi_tx_block.
; ***************************************************************************************
.rx_imm_peek_setup
    lda #&3d ; '='                                                    ; 9ae1: a9 3d       .=             ; Port workspace offset = &3D
    sta nmi_tx_block                                                  ; 9ae3: 85 a0       ..             ; Store workspace offset lo
    lda #&0d                                                          ; 9ae5: a9 0d       ..             ; RX buffer page = &0D
    sta nmi_tx_block_hi                                               ; 9ae7: 85 a1       ..             ; Store workspace offset hi
    lda #2                                                            ; 9ae9: a9 02       ..             ; Scout status = 2 (PEEK response)
    sta scout_status                                                  ; 9aeb: 8d 5c 0d    .\.            ; Store scout status
    jsr tx_calc_transfer                                              ; 9aee: 20 5b 9f     [.            ; Calculate transfer size for response
    pla                                                               ; 9af1: 68          h              ; Restore saved nmi_tx_block_hi
    sta nmi_tx_block_hi                                               ; 9af2: 85 a1       ..             ; Restore workspace ptr hi byte
    pla                                                               ; 9af4: 68          h              ; Restore saved nmi_tx_block
    sta nmi_tx_block                                                  ; 9af5: 85 a0       ..             ; Restore workspace ptr lo byte
    bcc imm_op_discard                                                ; 9af7: 90 56       .V             ; C=0: transfer not set up, discard
; &9af9 referenced 1 time by &9ad8
.set_tx_reply_flag
    lda tx_flags                                                      ; 9af9: ad 4a 0d    .J.            ; Mark TX flags bit 7 (reply pending)
    ora #&80                                                          ; 9afc: 09 80       ..             ; Set reply pending flag
    sta tx_flags                                                      ; 9afe: 8d 4a 0d    .J.            ; Store updated TX flags
.rx_imm_halt_cont
    lda #&44 ; 'D'                                                    ; 9b01: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    sta econet_control1_or_status1                                    ; 9b03: 8d a0 fe    ...            ; Write CR1: enable TX interrupts
.tx_cr2_setup
    lda #&a7                                                          ; 9b06: a9 a7       ..             ; CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE
    sta econet_control23_or_status2                                   ; 9b08: 8d a1 fe    ...            ; Write CR2 for TX setup
.tx_nmi_setup
    lda #&2f ; '/'                                                    ; 9b0b: a9 2f       ./             ; NMI handler lo byte (self-modifying)
.tx_nmi_dispatch_page
tx_dispatch_page_operand = tx_nmi_dispatch_page+1
    ldy #&9b                                                          ; 9b0d: a0 9b       ..             ; Y=&9B: dispatch table page
; &9b0e referenced 1 time by &9b8c
    jmp ack_tx_write_dest                                             ; 9b0f: 4c 74 99    Lt.            ; Acknowledge and write TX dest

; ***************************************************************************************
; Check control byte for immediate operation type
; 
; Loads the RX control byte and compares against &82
; (immediate HALT). If HALT, discards the frame via
; imm_op_discard. Otherwise falls through to
; imm_op_build_reply.
; ***************************************************************************************
; &9b12 referenced 1 time by &99c0
.check_imm_op_ctrl
rx_ctrl_operand = check_imm_op_ctrl+1
    ldy rx_ctrl                                                       ; 9b12: ac 3f 0d    .?.            ; Load RX control byte
; &9b13 referenced 1 time by &9b88
    cpy #&82                                                          ; 9b15: c0 82       ..             ; Compare against &82 (HALT)
    beq imm_op_discard                                                ; 9b17: f0 36       .6             ; HALT: discard frame
; ***************************************************************************************
; Build immediate operation reply header
; 
; Stores data length, source station/network, and control byte
; into the RX buffer header area for port-0 immediate operations.
; Then disables SR interrupts and configures the VIA shift
; register for shift-in mode before returning to
; idle listen.
; ***************************************************************************************
.imm_op_build_reply
    lda port_buf_len                                                  ; 9b19: a5 a2       ..             ; Get buffer position for reply header
    clc                                                               ; 9b1b: 18          .              ; Clear carry for offset addition
    adc #&80                                                          ; 9b1c: 69 80       i.             ; Data offset = buf_len + &80 (past header)
    ldy #&7f                                                          ; 9b1e: a0 7f       ..             ; Y=&7F: reply data length slot
    sta (net_rx_ptr),y                                                ; 9b20: 91 9c       ..             ; Store reply data length in RX buffer
    ldy #&80                                                          ; 9b22: a0 80       ..             ; Y=&80: source station slot
    lda rx_src_stn                                                    ; 9b24: ad 3d 0d    .=.            ; Load requesting station number
    sta (net_rx_ptr),y                                                ; 9b27: 91 9c       ..             ; Store source station in reply header
    iny                                                               ; 9b29: c8          .              ; Y=&81
    lda rx_src_net                                                    ; 9b2a: ad 3e 0d    .>.            ; Load requesting network number
    sta (net_rx_ptr),y                                                ; 9b2d: 91 9c       ..             ; Store source network in reply header
    lda rx_ctrl                                                       ; 9b2f: ad 3f 0d    .?.            ; Load control byte from received frame
    sta tx_work_57                                                    ; 9b32: 8d 57 0d    .W.            ; Save ctrl byte for TX response
    lda #&84                                                          ; 9b35: a9 84       ..             ; IER bit 2: disable SR interrupt
    sta system_via_ier                                                ; 9b37: 8d 4e fe    .N.            ; Write IER to disable SR
    lda system_via_acr                                                ; 9b3a: ad 4b fe    .K.            ; Read ACR for shift register config
    and #&1c                                                          ; 9b3d: 29 1c       ).             ; Isolate shift register mode bits (2-4)
    sta tx_work_51                                                    ; 9b3f: 8d 51 0d    .Q.            ; Save original SR mode for later restore
    lda system_via_acr                                                ; 9b42: ad 4b fe    .K.            ; Reload ACR for modification
    and #&e3                                                          ; 9b45: 29 e3       ).             ; Clear SR mode bits (keep other bits)
    ora #8                                                            ; 9b47: 09 08       ..             ; SR mode 2: shift in under φ2
    sta system_via_acr                                                ; 9b49: 8d 4b fe    .K.            ; Apply new shift register mode
    bit system_via_sr                                                 ; 9b4c: 2c 4a fe    ,J.            ; Read SR to clear pending interrupt
; &9b4f referenced 3 times by &9a7d, &9af7, &9b17
.imm_op_discard
    jmp discard_reset_listen                                          ; 9b4f: 4c 34 9a    L4.            ; Return to idle listen mode

; &9b52 referenced 1 time by &966c
.check_sr_irq
    lda #4                                                            ; 9b52: a9 04       ..             ; A=&04: IFR bit 2 (SR) mask
    bit system_via_ifr                                                ; 9b54: 2c 4d fe    ,M.            ; Test SR interrupt pending
    bne tx_done_error                                                 ; 9b57: d0 03       ..             ; SR fired: handle TX completion
    lda #5                                                            ; 9b59: a9 05       ..             ; A=5: no SR, return status 5
    rts                                                               ; 9b5b: 60          `              ; Return (no SR interrupt)

; &9b5c referenced 1 time by &9b57
.tx_done_error
    txa                                                               ; 9b5c: 8a          .              ; Save X
    pha                                                               ; 9b5d: 48          H              ; Push X
    tya                                                               ; 9b5e: 98          .              ; Save Y
    pha                                                               ; 9b5f: 48          H              ; Push Y
    lda system_via_acr                                                ; 9b60: ad 4b fe    .K.            ; Read ACR for shift register mode
    and #&e3                                                          ; 9b63: 29 e3       ).             ; Clear SR mode bits (2-4)
    ora tx_work_51                                                    ; 9b65: 0d 51 0d    .Q.            ; Restore original SR mode
    sta system_via_acr                                                ; 9b68: 8d 4b fe    .K.            ; Write updated ACR
    lda system_via_sr                                                 ; 9b6b: ad 4a fe    .J.            ; Read SR to clear pending interrupt
    lda #4                                                            ; 9b6e: a9 04       ..             ; A=&04: SR bit mask
    sta system_via_ifr                                                ; 9b70: 8d 4d fe    .M.            ; Clear SR in IFR
    sta system_via_ier                                                ; 9b73: 8d 4e fe    .N.            ; Disable SR in IER
    ldy tx_work_57                                                    ; 9b76: ac 57 0d    .W.            ; Load ctrl byte for dispatch
    cpy #&86                                                          ; 9b79: c0 86       ..             ; Ctrl >= &86? (HALT/CONTINUE)
    bcs tx_done_classify                                              ; 9b7b: b0 0b       ..             ; Yes: skip protection mask save
    lda prot_status                                                   ; 9b7d: ad 63 0d    .c.            ; Load current protection mask
    sta rx_ctrl_copy                                                  ; 9b80: 8d 3b 0d    .;.            ; Save mask before JSR modification
    ora #&1c                                                          ; 9b83: 09 1c       ..             ; Enable bits 2-4 (allow JSR ops)
    sta prot_status                                                   ; 9b85: 8d 63 0d    .c.            ; Store modified protection mask
; &9b88 referenced 1 time by &9b7b
.tx_done_classify
    lda rx_ctrl_operand,y                                             ; 9b88: b9 13 9b    ...            ; Load handler addr hi from table
    pha                                                               ; 9b8b: 48          H              ; Push handler hi
    lda tx_dispatch_page_operand,y                                    ; 9b8c: b9 0e 9b    ...            ; Load handler addr lo from table
    pha                                                               ; 9b8f: 48          H              ; Push handler lo
    rts                                                               ; 9b90: 60          `              ; Dispatch via RTS (addr-1 on stack)

    equb <(tx_done_jsr-1)                                             ; 9b91: 9a          .
    equb <(tx_done_user_proc-1)                                       ; 9b92: a3          .
    equb <(tx_done_os_proc-1)                                         ; 9b93: b1          .
    equb <(tx_done_halt-1)                                            ; 9b94: bd          .
    equb <(tx_done_continue-1)                                        ; 9b95: d4          .
    equb >(tx_done_jsr-1)                                             ; 9b96: 9b          .
    equb >(tx_done_user_proc-1)                                       ; 9b97: 9b          .
    equb >(tx_done_os_proc-1)                                         ; 9b98: 9b          .
    equb >(tx_done_halt-1)                                            ; 9b99: 9b          .
    equb >(tx_done_continue-1)                                        ; 9b9a: 9b          .

; ***************************************************************************************
; TX done: remote JSR execution
; 
; Pushes a return address on the stack (pointing to
; tx_done_exit), then does JMP indirect to call the remote
; JSR target routine. When that routine returns via RTS,
; control resumes at tx_done_exit.
; ***************************************************************************************
.tx_done_jsr
    lda #&9b                                                          ; 9b9b: a9 9b       ..             ; Push hi of (tx_done_exit-1)
    pha                                                               ; 9b9d: 48          H              ; Push hi byte on stack
    lda #&dc                                                          ; 9b9e: a9 dc       ..             ; Push lo of (tx_done_exit-1)
    pha                                                               ; 9ba0: 48          H              ; Push lo byte on stack
    jmp (l0d58)                                                       ; 9ba1: 6c 58 0d    lX.            ; Call remote JSR; RTS to tx_done_exit

; ***************************************************************************************
; TX done: UserProc event
; 
; Generates a network event (event 8) via OSEVEN with the
; remote address. This notifies the user program that a
; UserProc operation has completed.
; ***************************************************************************************
.tx_done_user_proc
    ldy #event_network_error                                          ; 9ba4: a0 08       ..             ; Y=8: network event type
    ldx l0d58                                                         ; 9ba6: ae 58 0d    .X.            ; X = remote address lo
    lda l0d59                                                         ; 9ba9: ad 59 0d    .Y.            ; A = remote address hi
    jsr oseven                                                        ; 9bac: 20 bf ff     ..            ; Generate event Y='Network error'
    jmp tx_done_exit                                                  ; 9baf: 4c dd 9b    L..            ; Exit TX done handler

; ***************************************************************************************
; TX done: OSProc call
; 
; Calls the ROM entry point at &8000 (rom_header) with
; X/Y from the remote address workspace. This invokes an
; OS-level procedure on behalf of the remote station.
; ***************************************************************************************
.tx_done_os_proc
    ldx l0d58                                                         ; 9bb2: ae 58 0d    .X.            ; X = remote address lo
    ldy l0d59                                                         ; 9bb5: ac 59 0d    .Y.            ; Y = remote address hi
    jsr rom_header                                                    ; 9bb8: 20 00 80     ..            ; Call ROM entry point at &8000
    jmp tx_done_exit                                                  ; 9bbb: 4c dd 9b    L..            ; Exit TX done handler

; ***************************************************************************************
; TX done: HALT
; 
; Sets bit 2 of rx_flags, enables interrupts, and spin-waits
; until bit 2 is cleared (by a CONTINUE from the remote
; station). If bit 2 is already set, skips to exit.
; ***************************************************************************************
.tx_done_halt
    lda #4                                                            ; 9bbe: a9 04       ..             ; A=&04: bit 2 mask for rx_flags
    bit rx_status_flags                                               ; 9bc0: 2c 38 0d    ,8.            ; Test if already halted
    bne tx_done_exit                                                  ; 9bc3: d0 18       ..             ; Already halted: skip to exit
    ora rx_status_flags                                               ; 9bc5: 0d 38 0d    .8.            ; Set bit 2 in rx_flags
    sta rx_status_flags                                               ; 9bc8: 8d 38 0d    .8.            ; Store halt flag
    lda #4                                                            ; 9bcb: a9 04       ..             ; A=4: re-load halt bit mask
    cli                                                               ; 9bcd: 58          X              ; Enable interrupts during halt wait
; &9bce referenced 1 time by &9bd1
.halt_spin_loop
    bit rx_status_flags                                               ; 9bce: 2c 38 0d    ,8.            ; Test halt flag
    bne halt_spin_loop                                                ; 9bd1: d0 fb       ..             ; Still halted: keep spinning
    beq tx_done_exit                                                  ; 9bd3: f0 08       ..             ; ALWAYS branch

; ***************************************************************************************
; TX done: CONTINUE
; 
; Clears bit 2 of rx_flags, releasing any station that is
; halted and spinning in tx_done_halt.
; ***************************************************************************************
.tx_done_continue
    lda rx_status_flags                                               ; 9bd5: ad 38 0d    .8.            ; Load current RX flags
    and #&fb                                                          ; 9bd8: 29 fb       ).             ; Clear bit 2: release halted station
    sta rx_status_flags                                               ; 9bda: 8d 38 0d    .8.            ; Store updated flags
; &9bdd referenced 4 times by &9baf, &9bbb, &9bc3, &9bd3
.tx_done_exit
    pla                                                               ; 9bdd: 68          h              ; Restore Y from stack
    tay                                                               ; 9bde: a8          .              ; Transfer to Y register
    pla                                                               ; 9bdf: 68          h              ; Restore X from stack
    tax                                                               ; 9be0: aa          .              ; Transfer to X register
    lda #0                                                            ; 9be1: a9 00       ..             ; A=0: success status
    rts                                                               ; 9be3: 60          `              ; Return with A=0 (success)

; ***************************************************************************************
; Begin TX operation
; 
; Main TX initiation entry point (called via trampoline at &06CE).
; Copies dest station/network from the TXCB to the scout buffer,
; dispatches to immediate op setup (ctrl >= &81) or normal data
; transfer, calculates transfer sizes, copies extra parameters,
; then enters the INACTIVE polling loop.
; ***************************************************************************************
; &9be4 referenced 1 time by &9660
.tx_begin
    txa                                                               ; 9be4: 8a          .              ; Save X on stack
    pha                                                               ; 9be5: 48          H              ; Push X
    ldy #2                                                            ; 9be6: a0 02       ..             ; Y=2: TXCB offset for dest station
    lda (nmi_tx_block),y                                              ; 9be8: b1 a0       ..             ; Load dest station from TX control block
    sta tx_dst_stn                                                    ; 9bea: 8d 20 0d    . .            ; Store to TX scout buffer
    iny                                                               ; 9bed: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 9bee: b1 a0       ..             ; Load dest network from TX control block
    sta tx_dst_net                                                    ; 9bf0: 8d 21 0d    .!.            ; Store to TX scout buffer
    ldy #0                                                            ; 9bf3: a0 00       ..             ; Y=0: first byte of TX control block
    lda (nmi_tx_block),y                                              ; 9bf5: b1 a0       ..             ; Load control/flag byte
    bmi tx_imm_op_setup                                               ; 9bf7: 30 03       0.             ; Bit7 set: immediate operation ctrl byte
    jmp tx_active_start                                               ; 9bf9: 4c 84 9c    L..            ; Bit7 clear: normal data transfer

; &9bfc referenced 1 time by &9bf7
.tx_imm_op_setup
    sta tx_ctrl_byte                                                  ; 9bfc: 8d 24 0d    .$.            ; Store control byte to TX scout buffer
    tax                                                               ; 9bff: aa          .              ; X = control byte for range checks
    iny                                                               ; 9c00: c8          .              ; Y=1: port byte offset
    lda (nmi_tx_block),y                                              ; 9c01: b1 a0       ..             ; Load port byte from TX control block
    sta tx_port                                                       ; 9c03: 8d 25 0d    .%.            ; Store port byte to TX scout buffer
    bne tx_line_idle_check                                            ; 9c06: d0 2f       ./             ; Port != 0: skip immediate op setup
    cpx #&83                                                          ; 9c08: e0 83       ..             ; Ctrl < &83: PEEK/POKE need address calc
    bcs check_imm_range                                               ; 9c0a: b0 1b       ..             ; Ctrl >= &83: skip to range check
    sec                                                               ; 9c0c: 38          8              ; SEC: init borrow for 4-byte subtract
    php                                                               ; 9c0d: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 9c0e: a0 08       ..             ; Y=8: high pointer offset in TXCB
; &9c10 referenced 1 time by &9c24
.calc_peek_poke_size
    lda (nmi_tx_block),y                                              ; 9c10: b1 a0       ..             ; Load TXCB[Y] (end addr byte)
    dey                                                               ; 9c12: 88          .              ; Y -= 4: back to start addr offset
    dey                                                               ; 9c13: 88          .              ; (Y -= 4: reach start addr offset)
    dey                                                               ; 9c14: 88          .              ; (continued)
    dey                                                               ; 9c15: 88          .              ; (continued)
    plp                                                               ; 9c16: 28          (              ; Restore borrow from stack
    sbc (nmi_tx_block),y                                              ; 9c17: f1 a0       ..             ; end - start = transfer size byte
    sta tx_data_start,y                                               ; 9c19: 99 26 0d    .&.            ; Store result to tx_data_start
    iny                                                               ; 9c1c: c8          .              ; (Y += 5: advance to next end byte)
    iny                                                               ; 9c1d: c8          .              ; (continued)
    iny                                                               ; 9c1e: c8          .              ; (continued)
    iny                                                               ; 9c1f: c8          .              ; (continued)
    iny                                                               ; 9c20: c8          .              ; (continued)
    php                                                               ; 9c21: 08          .              ; Save borrow for next byte
    cpy #&0c                                                          ; 9c22: c0 0c       ..             ; Done all 4 bytes? (Y reaches &0C)
    bcc calc_peek_poke_size                                           ; 9c24: 90 ea       ..             ; No: next byte pair
    plp                                                               ; 9c26: 28          (              ; Discard final borrow
; &9c27 referenced 1 time by &9c0a
.check_imm_range
    cpx #&89                                                          ; 9c27: e0 89       ..             ; Ctrl >= &89: out of immediate range
    bcs tx_active_start                                               ; 9c29: b0 59       .Y             ; Above range: normal data transfer
    ldy #&0c                                                          ; 9c2b: a0 0c       ..             ; Y=&0C: start of extra data in TXCB
; &9c2d referenced 1 time by &9c35
.copy_imm_params
    lda (nmi_tx_block),y                                              ; 9c2d: b1 a0       ..             ; Load extra parameter byte from TXCB
    sta nmi_shim_1a,y                                                 ; 9c2f: 99 1a 0d    ...            ; Copy to NMI shim workspace at &0D1A+Y
    iny                                                               ; 9c32: c8          .              ; Next byte
    cpy #&10                                                          ; 9c33: c0 10       ..             ; Done 4 bytes? (Y reaches &10)
    bcc copy_imm_params                                               ; 9c35: 90 f6       ..             ; No: continue copying
; &9c37 referenced 1 time by &9c06
.tx_line_idle_check
    lda #&20 ; ' '                                                    ; 9c37: a9 20       .              ; A=&20: mask for SR2 INACTIVE bit
    bit econet_control23_or_status2                                   ; 9c39: 2c a1 fe    ,..            ; BIT SR2: test if line is idle
    bne tx_no_clock_error                                             ; 9c3c: d0 56       .V             ; Line not idle: handle as line jammed
    lda #&fd                                                          ; 9c3e: a9 fd       ..             ; A=&FD: high byte of timeout counter
    pha                                                               ; 9c40: 48          H              ; Push timeout high byte to stack
    lda #6                                                            ; 9c41: a9 06       ..             ; Scout frame = 6 address+ctrl bytes
    sta tx_length                                                     ; 9c43: 8d 50 0d    .P.            ; Store scout frame length
    lda #0                                                            ; 9c46: a9 00       ..             ; A=0: init low byte of timeout counter
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
    sta tx_index                                                      ; 9c48: 8d 4f 0d    .O.            ; Save TX index
    pha                                                               ; 9c4b: 48          H              ; Push timeout byte 1 on stack
    pha                                                               ; 9c4c: 48          H              ; Push timeout byte 2 on stack
    ldy #&e7                                                          ; 9c4d: a0 e7       ..             ; Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &9c4f referenced 3 times by &9c75, &9c7a, &9c7f
.test_inactive_retry
    lda #4                                                            ; 9c4f: a9 04       ..             ; A=&04: INACTIVE mask for SR2 bit2
    php                                                               ; 9c51: 08          .              ; Save interrupt state
    sei                                                               ; 9c52: 78          x              ; Disable interrupts for ADLC access
; ***************************************************************************************
; Disable NMIs and test INACTIVE
; 
; Mid-instruction label within the INACTIVE polling loop. The
; address &9BE2 is referenced as a constant for self-modifying
; code. Disables NMIs twice (belt-and-braces) then tests SR2
; for INACTIVE before proceeding with TX.
; ***************************************************************************************
; &9c53 referenced 1 time by &9ccf
.intoff_test_inactive
    bit station_id_disable_net_nmis                                   ; 9c53: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
    bit station_id_disable_net_nmis                                   ; 9c56: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
.test_line_idle
sr2_test_operand = test_line_idle+2
    bit econet_control23_or_status2                                   ; 9c59: 2c a1 fe    ,..            ; BIT SR2: Z = &04 AND SR2 -- tests INACTIVE
; &9c5b referenced 1 time by &9ccb
    beq inactive_retry                                                ; 9c5c: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 9c5e: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 9c61: a9 67       .g             ; CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9c63: 8d a1 fe    ...            ; Write CR2: clear status, prepare TX
    lda #&10                                                          ; 9c66: a9 10       ..             ; A=&10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 9c68: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 9c6b: d0 35       .5             ; CTS set -- clock hardware detected, start TX
; &9c6d referenced 1 time by &9c5c
.inactive_retry
    bit video_ula_control                                             ; 9c6d: 2c 20 fe    , .            ; INTON -- re-enable NMIs (&FE20 read)
    plp                                                               ; 9c70: 28          (              ; Restore interrupt state
    tsx                                                               ; 9c71: ba          .              ; 3-byte timeout counter on stack
    inc l0101,x                                                       ; 9c72: fe 01 01    ...            ; Increment timeout counter byte 1
    bne test_inactive_retry                                           ; 9c75: d0 d8       ..             ; Not overflowed: retry INACTIVE test
    inc l0102,x                                                       ; 9c77: fe 02 01    ...            ; Increment timeout counter byte 2
    bne test_inactive_retry                                           ; 9c7a: d0 d3       ..             ; Not overflowed: retry INACTIVE test
    inc l0103,x                                                       ; 9c7c: fe 03 01    ...            ; Increment timeout counter byte 3
    bne test_inactive_retry                                           ; 9c7f: d0 ce       ..             ; Not overflowed: retry INACTIVE test
    jmp tx_line_jammed                                                ; 9c81: 4c 88 9c    L..            ; All 3 bytes overflowed: line jammed

; TX_ACTIVE branch (A=&44 = CR1 value for TX active)
; &9c84 referenced 2 times by &9bf9, &9c29
.tx_active_start
    lda #&44 ; 'D'                                                    ; 9c84: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    bne store_tx_error                                                ; 9c86: d0 0e       ..             ; ALWAYS branch

; ***************************************************************************************
; TX timeout error handler (Line Jammed)
; 
; Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
; timeout loop's state), then stores error code &40 ("Line
; Jammed") into the TX control block and signals completion.
; ***************************************************************************************
; &9c88 referenced 1 time by &9c81
.tx_line_jammed
    lda #7                                                            ; 9c88: a9 07       ..             ; CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)
    sta econet_control23_or_status2                                   ; 9c8a: 8d a1 fe    ...            ; Write CR2 to abort TX
    pla                                                               ; 9c8d: 68          h              ; Clean 3 bytes of timeout loop state
    pla                                                               ; 9c8e: 68          h              ; Pop saved register
    pla                                                               ; 9c8f: 68          h              ; Pop saved register
    lda #&40 ; '@'                                                    ; 9c90: a9 40       .@             ; Error &40 = 'Line Jammed'
    bne store_tx_error                                                ; 9c92: d0 02       ..             ; ALWAYS branch to shared error handler; ALWAYS branch

; &9c94 referenced 1 time by &9c3c
.tx_no_clock_error
    lda #&43 ; 'C'                                                    ; 9c94: a9 43       .C             ; Error &43 = 'No Clock'
; &9c96 referenced 2 times by &9c86, &9c92
.store_tx_error
    ldy #0                                                            ; 9c96: a0 00       ..             ; Offset 0 = error byte in TX control block
    sta (nmi_tx_block),y                                              ; 9c98: 91 a0       ..             ; Store error code in TX CB byte 0
    lda #&80                                                          ; 9c9a: a9 80       ..             ; &80 = TX complete flag
    sta tx_ctrl_status                                                ; 9c9c: 8d 3a 0d    .:.            ; Signal TX operation complete
    pla                                                               ; 9c9f: 68          h              ; Restore X saved by caller
    tax                                                               ; 9ca0: aa          .              ; Move to X register
    rts                                                               ; 9ca1: 60          `              ; Return to TX caller

; ***************************************************************************************
; TX preparation
; 
; Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
; installs NMI TX handler at &9D4C, and re-enables NMIs.
; ***************************************************************************************
; &9ca2 referenced 1 time by &9c6b
.tx_prepare
    sty econet_control23_or_status2                                   ; 9ca2: 8c a1 fe    ...            ; Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
    ldx #&44 ; 'D'                                                    ; 9ca5: a2 44       .D             ; CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)
    stx econet_control1_or_status1                                    ; 9ca7: 8e a0 fe    ...            ; Write to ADLC CR1
    ldx #&4c ; 'L'                                                    ; 9caa: a2 4c       .L             ; Install NMI handler at &9D4C (TX data handler)
    ldy #&9d                                                          ; 9cac: a0 9d       ..             ; High byte of NMI handler address
    stx nmi_jmp_lo                                                    ; 9cae: 8e 0c 0d    ...            ; Write NMI vector low byte directly
    sty nmi_jmp_hi                                                    ; 9cb1: 8c 0d 0d    ...            ; Write NMI vector high byte directly
    bit video_ula_control                                             ; 9cb4: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA (&FE20 read)
    lda tx_port                                                       ; 9cb7: ad 25 0d    .%.            ; Load destination port number
    bne setup_data_xfer                                               ; 9cba: d0 5a       .Z             ; Port != 0: standard data transfer
    ldy tx_ctrl_byte                                                  ; 9cbc: ac 24 0d    .$.            ; Port 0: load control byte for table lookup
    lda tube_tx_byte4_operand,y                                       ; 9cbf: b9 d2 9e    ...            ; Look up tx_flags from table
    sta tx_flags                                                      ; 9cc2: 8d 4a 0d    .J.            ; Store operation flags
    lda tube_tx_byte2_operand,y                                       ; 9cc5: b9 ca 9e    ...            ; Look up tx_length from table
    sta tx_length                                                     ; 9cc8: 8d 50 0d    .P.            ; Store expected transfer length
    lda sr2_test_operand,y                                            ; 9ccb: b9 5b 9c    .[.            ; Load handler from dispatch table
    pha                                                               ; 9cce: 48          H              ; Push high byte for PHA/PHA/RTS dispatch
    lda intoff_test_inactive,y                                        ; 9ccf: b9 53 9c    .S.            ; Look up handler address low from table
    pha                                                               ; 9cd2: 48          H              ; Push low byte for PHA/PHA/RTS dispatch
    rts                                                               ; 9cd3: 60          `              ; RTS dispatches to control-byte handler

    equb <(tx_ctrl_peek-1)                                            ; 9cd4: e7          .
    equb <(tx_ctrl_poke-1)                                            ; 9cd5: eb          .
    equb <(tx_ctrl_proc-1)                                            ; 9cd6: 0a          .
    equb <(tx_ctrl_proc-1)                                            ; 9cd7: 0a          .
    equb <(tx_ctrl_proc-1)                                            ; 9cd8: 0a          .
    equb <(tx_ctrl_exit-1)                                            ; 9cd9: 44          D
    equb <(tx_ctrl_exit-1)                                            ; 9cda: 44          D
    equb <(imm_op_status3-1)                                          ; 9cdb: e3          .
    equb >(tx_ctrl_peek-1)                                            ; 9cdc: 9c          .
    equb >(tx_ctrl_poke-1)                                            ; 9cdd: 9c          .
    equb >(tx_ctrl_proc-1)                                            ; 9cde: 9d          .
    equb >(tx_ctrl_proc-1)                                            ; 9cdf: 9d          .
    equb >(tx_ctrl_proc-1)                                            ; 9ce0: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9ce1: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9ce2: 9d          .
    equb >(imm_op_status3-1)                                          ; 9ce3: 9c          .

.imm_op_status3
    lda #3                                                            ; 9ce4: a9 03       ..             ; A=3: scout_status for PEEK
    bne store_status_calc_xfer                                        ; 9ce6: d0 25       .%             ; ALWAYS branch

; ***************************************************************************************
; TX ctrl: PEEK transfer setup
; 
; Sets scout_status=3, then performs a 4-byte addition of
; bytes from the TX block into the transfer parameter
; workspace (with carry propagation). Calls tx_calc_transfer
; to finalise, then exits via tx_ctrl_exit.
; ***************************************************************************************
.tx_ctrl_peek
    lda #3                                                            ; 9ce8: a9 03       ..             ; A=3: scout_status for PEEK op
    bne store_status_add4                                             ; 9cea: d0 02       ..             ; ALWAYS branch

; ***************************************************************************************
; TX ctrl: POKE transfer setup
; 
; Sets scout_status=2 and shares the 4-byte addition and
; transfer calculation path with tx_ctrl_peek.
; ***************************************************************************************
.tx_ctrl_poke
    lda #2                                                            ; 9cec: a9 02       ..             ; Scout status = 2 (POKE transfer)
; &9cee referenced 1 time by &9cea
.store_status_add4
    sta scout_status                                                  ; 9cee: 8d 5c 0d    .\.            ; Store scout status
    clc                                                               ; 9cf1: 18          .              ; Clear carry for 4-byte addition
    php                                                               ; 9cf2: 08          .              ; Save carry on stack
    ldy #&0c                                                          ; 9cf3: a0 0c       ..             ; Y=&0C: start at offset 12
; &9cf5 referenced 1 time by &9d02
.add_bytes_loop
    lda l0d1e,y                                                       ; 9cf5: b9 1e 0d    ...            ; Load workspace address byte
    plp                                                               ; 9cf8: 28          (              ; Restore carry from previous byte
    adc (nmi_tx_block),y                                              ; 9cf9: 71 a0       q.             ; Add TXCB address byte
    sta l0d1e,y                                                       ; 9cfb: 99 1e 0d    ...            ; Store updated address byte
    iny                                                               ; 9cfe: c8          .              ; Next byte
    php                                                               ; 9cff: 08          .              ; Save carry for next addition
; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_add_done
    cpy #&10                                                          ; 9d00: c0 10       ..             ; Compare Y with 16-byte boundary
    bcc add_bytes_loop                                                ; 9d02: 90 f1       ..             ; Below boundary: continue addition
    plp                                                               ; 9d04: 28          (              ; Restore processor flags
    jsr tx_calc_transfer                                              ; 9d05: 20 5b 9f     [.            ; Calculate transfer byte count
    jmp tx_ctrl_exit                                                  ; 9d08: 4c 45 9d    LE.            ; Jump to TX control exit

; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_proc
    lda #2                                                            ; 9d0b: a9 02       ..             ; A=2: scout_status for procedure ops
; &9d0d referenced 1 time by &9ce6
.store_status_calc_xfer
    sta scout_status                                                  ; 9d0d: 8d 5c 0d    .\.            ; Store scout status
    jsr tx_calc_transfer                                              ; 9d10: 20 5b 9f     [.            ; Calculate transfer parameters
    jmp tx_ctrl_exit                                                  ; 9d13: 4c 45 9d    LE.            ; Exit TX ctrl setup

; &9d16 referenced 1 time by &9cba
.setup_data_xfer
    lda tx_dst_stn                                                    ; 9d16: ad 20 0d    . .            ; Load dest station for broadcast check
    and tx_dst_net                                                    ; 9d19: 2d 21 0d    -!.            ; AND with dest network
    cmp #&ff                                                          ; 9d1c: c9 ff       ..             ; Both &FF = broadcast address?
    bne setup_unicast_xfer                                            ; 9d1e: d0 18       ..             ; Not broadcast: unicast path
    lda #&0e                                                          ; 9d20: a9 0e       ..             ; Broadcast scout: 14 bytes total
    sta tx_length                                                     ; 9d22: 8d 50 0d    .P.            ; Store broadcast scout length
    lda #&40 ; '@'                                                    ; 9d25: a9 40       .@             ; A=&40: broadcast flag
    sta tx_flags                                                      ; 9d27: 8d 4a 0d    .J.            ; Set broadcast flag in tx_flags
    ldy #4                                                            ; 9d2a: a0 04       ..             ; Y=4: start of address data in TXCB
; &9d2c referenced 1 time by &9d34
.copy_bcast_addr
    lda (nmi_tx_block),y                                              ; 9d2c: b1 a0       ..             ; Copy TXCB address bytes to scout buffer
    sta tx_src_stn,y                                                  ; 9d2e: 99 22 0d    .".            ; Store to TX source/data area
    iny                                                               ; 9d31: c8          .              ; Next byte
    cpy #&0c                                                          ; 9d32: c0 0c       ..             ; Done 8 bytes? (Y reaches &0C)
    bcc copy_bcast_addr                                               ; 9d34: 90 f6       ..             ; No: continue copying
    bcs tx_ctrl_exit                                                  ; 9d36: b0 0d       ..             ; ALWAYS branch

; &9d38 referenced 1 time by &9d1e
.setup_unicast_xfer
    lda #0                                                            ; 9d38: a9 00       ..             ; A=0: clear flags for unicast
    sta tx_flags                                                      ; 9d3a: 8d 4a 0d    .J.            ; Clear tx_flags
.proc_op_status2
    lda #2                                                            ; 9d3d: a9 02       ..             ; scout_status=2: data transfer pending
.store_status_copy_ptr
    sta scout_status                                                  ; 9d3f: 8d 5c 0d    .\.            ; Store scout status
    jsr tx_calc_transfer                                              ; 9d42: 20 5b 9f     [.            ; Calculate transfer size from RXCB
; &9d45 referenced 3 times by &9d08, &9d13, &9d36
.tx_ctrl_exit
    plp                                                               ; 9d45: 28          (              ; Restore processor status from stack
    pla                                                               ; 9d46: 68          h              ; Restore stacked registers (4 PLAs)
    pla                                                               ; 9d47: 68          h              ; Second PLA
    pla                                                               ; 9d48: 68          h              ; Third PLA
    pla                                                               ; 9d49: 68          h              ; Fourth PLA
    tax                                                               ; 9d4a: aa          .              ; Restore X from A
    rts                                                               ; 9d4b: 60          `              ; Return to caller

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
    ldy tx_index                                                      ; 9d4c: ac 4f 0d    .O.            ; Load TX buffer index
    bit econet_control1_or_status1                                    ; 9d4f: 2c a0 fe    ,..            ; BIT SR1: V=bit6(TDRA), N=bit7(IRQ)
; &9d52 referenced 1 time by &9d6d
.tx_fifo_write
    bvc tx_fifo_not_ready                                             ; 9d52: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 9d54: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 9d57: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 9d5a: c8          .              ; Next TX buffer byte
    lda tx_dst_stn,y                                                  ; 9d5b: b9 20 0d    . .            ; Load second byte from TX buffer
    iny                                                               ; 9d5e: c8          .              ; Advance TX index past second byte
    sty tx_index                                                      ; 9d5f: 8c 4f 0d    .O.            ; Save updated TX buffer index
    sta econet_data_continue_frame                                    ; 9d62: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy tx_length                                                     ; 9d65: cc 50 0d    .P.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 9d68: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA
    bit econet_control1_or_status1                                    ; 9d6a: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi tx_fifo_write                                                 ; 9d6d: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 9d6f: 4c 14 0d    L..            ; RTI -- wait for next NMI

; TX error path
; &9d72 referenced 1 time by &9db7
.tx_error
    lda #&42 ; 'B'                                                    ; 9d72: a9 42       .B             ; Error &42
    bne tx_store_error                                                ; 9d74: d0 07       ..             ; ALWAYS branch

; &9d76 referenced 1 time by &9d52
.tx_fifo_not_ready
    lda #&67 ; 'g'                                                    ; 9d76: a9 67       .g             ; CR2=&67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 9d78: 8d a1 fe    ...            ; Write CR2: clear status, idle listen
    lda #&41 ; 'A'                                                    ; 9d7b: a9 41       .A             ; Error &41 (TDRA not ready)
; &9d7d referenced 1 time by &9d74
.tx_store_error
    ldy station_id_disable_net_nmis                                   ; 9d7d: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &9d80 referenced 1 time by &9d83
.delay_nmi_disable
    pha                                                               ; 9d80: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 9d81: 68          h              ; PHA/PLA delay (~7 cycles each)
    iny                                                               ; 9d82: c8          .              ; Increment delay counter
    bne delay_nmi_disable                                             ; 9d83: d0 fb       ..             ; Loop 256 times for NMI disable
    jmp tx_store_result                                               ; 9d85: 4c 3f 9f    L?.            ; Jump to error handler

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
; &9d88 referenced 1 time by &9d68
.tx_last_data
    lda #&3f ; '?'                                                    ; 9d88: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 9d8a: 8d a1 fe    ...            ; Write to ADLC CR2
    lda #&94                                                          ; 9d8d: a9 94       ..             ; Install NMI handler at &9D94 (TX completion)
    ldy #&9d                                                          ; 9d8f: a0 9d       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9d91: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

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
    lda #&82                                                          ; 9d94: a9 82       ..             ; CR1=&82: TX_RESET | RIE (now in RX mode)
    sta econet_control1_or_status1                                    ; 9d96: 8d a0 fe    ...            ; Write CR1 to switch from TX to RX
    bit tx_flags                                                      ; 9d99: 2c 4a 0d    ,J.            ; Test workspace flags
    bvc check_handshake_bit                                           ; 9d9c: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 9d9e: 4c 39 9f    L9.            ; bit6 set -- TX completion

; &9da1 referenced 1 time by &9d9c
.check_handshake_bit
    lda #1                                                            ; 9da1: a9 01       ..             ; A=1: mask for bit0 test
    bit tx_flags                                                      ; 9da3: 2c 4a 0d    ,J.            ; Test tx_flags bit0 (handshake)
    beq install_reply_scout                                           ; 9da6: f0 03       ..             ; bit0 clear: install reply handler
    jmp handshake_await_ack                                           ; 9da8: 4c dd 9e    L..            ; bit0 set -- four-way handshake data phase

; &9dab referenced 1 time by &9da6
.install_reply_scout
    lda #&b2                                                          ; 9dab: a9 b2       ..             ; Install RX reply handler at &9DB2
    ldy #&9d                                                          ; 9dad: a0 9d       ..             ; High byte of nmi_reply_scout addr
    jmp set_nmi_vector                                                ; 9daf: 4c 0e 0d    L..            ; Install handler and RTI

; ***************************************************************************************
; RX reply scout handler
; 
; Handles reception of the reply scout frame after transmission.
; Checks SR2 bit0 (AP) for incoming data, reads the first byte
; (destination station) and compares to our station ID via &FE18
; (which also disables NMIs as a side effect).
; ***************************************************************************************
.nmi_reply_scout
    lda #1                                                            ; 9db2: a9 01       ..             ; A=&01: AP mask for SR2
    bit econet_control23_or_status2                                   ; 9db4: 2c a1 fe    ,..            ; BIT SR2: test AP (Address Present)
    beq tx_error                                                      ; 9db7: f0 b9       ..             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9db9: ad a2 fe    ...            ; Read first RX byte (destination station)
    cmp station_id_disable_net_nmis                                   ; 9dbc: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne reply_error                                                   ; 9dbf: d0 1d       ..             ; Not our station -- error/reject
    lda #&c8                                                          ; 9dc1: a9 c8       ..             ; Install next handler at &9DC8 (reply continuation)
    ldy #&9d                                                          ; 9dc3: a0 9d       ..             ; High byte of nmi_reply_cont
    jmp set_nmi_vector                                                ; 9dc5: 4c 0e 0d    L..            ; Install continuation handler

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
    bit econet_control23_or_status2                                   ; 9dc8: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl reply_error                                                   ; 9dcb: 10 11       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9dcd: ad a2 fe    ...            ; Read destination network byte
    bne reply_error                                                   ; 9dd0: d0 0c       ..             ; Non-zero -- network mismatch, error
    lda #&e3                                                          ; 9dd2: a9 e3       ..             ; Install next handler at &9DE3 (reply validation)
    ldy #&9d                                                          ; 9dd4: a0 9d       ..             ; High byte of nmi_reply_validate
    bit econet_control1_or_status1                                    ; 9dd6: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 9dd9: 30 08       0.             ; IRQ set -- fall through to &9D5B without RTI
    jmp set_nmi_vector                                                ; 9ddb: 4c 0e 0d    L..            ; IRQ not set -- install handler and RTI

; &9dde referenced 7 times by &9dbf, &9dcb, &9dd0, &9de6, &9dee, &9df6, &9dfd
.reply_error
    lda #&41 ; 'A'                                                    ; 9dde: a9 41       .A             ; A=&41: 'not listening' error code
.reject_reply
    jmp tx_store_result                                               ; 9de0: 4c 3f 9f    L?.            ; Store error and return to idle

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
; &9de3 referenced 1 time by &9dd9
.nmi_reply_validate
    bit econet_control23_or_status2                                   ; 9de3: 2c a1 fe    ,..            ; BIT SR2: test RDA (bit7). Must be set for valid reply.
    bpl reply_error                                                   ; 9de6: 10 f6       ..             ; No RDA -- error (FV masking RDA via PSE would cause this)
    lda econet_data_continue_frame                                    ; 9de8: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9deb: cd 20 0d    . .            ; Compare to original TX destination station (&0D20)
    bne reply_error                                                   ; 9dee: d0 ee       ..             ; Mismatch -- not the expected reply, error
    lda econet_data_continue_frame                                    ; 9df0: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9df3: cd 21 0d    .!.            ; Compare to original TX destination network (&0D21)
    bne reply_error                                                   ; 9df6: d0 e6       ..             ; Mismatch -- error
    lda #2                                                            ; 9df8: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9dfa: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq reply_error                                                   ; 9dfd: f0 df       ..             ; No FV -- incomplete frame, error
    lda #&a7                                                          ; 9dff: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)
    sta econet_control23_or_status2                                   ; 9e01: 8d a1 fe    ...            ; Write CR2: enable RTS for TX handshake
    lda #&44 ; 'D'                                                    ; 9e04: a9 44       .D             ; CR1=&44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 9e06: 8d a0 fe    ...            ; Write CR1: reset RX, enable TX interrupt
    lda #&dd                                                          ; 9e09: a9 dd       ..             ; Install next handler at &9EDD (four-way data phase) into &0D4B/&0D4C
    ldy #&9e                                                          ; 9e0b: a0 9e       ..             ; High byte &9E of next handler address
    sta nmi_next_lo                                                   ; 9e0d: 8d 4b 0d    .K.            ; Store low byte to nmi_next_lo
    sty nmi_next_hi                                                   ; 9e10: 8c 4c 0d    .L.            ; Store high byte to nmi_next_hi
    lda tx_dst_stn                                                    ; 9e13: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 9e16: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc data_tx_error                                                 ; 9e19: 50 73       Ps             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9e1b: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 9e1e: ad 21 0d    .!.            ; Load dest network for scout ACK TX
    sta econet_data_continue_frame                                    ; 9e21: 8d a2 fe    ...            ; Write dest network to TX FIFO
    lda #&2b ; '+'                                                    ; 9e24: a9 2b       .+             ; Install handler at &9E2B (write src addr for scout ACK)
    ldy #&9e                                                          ; 9e26: a0 9e       ..             ; High byte &9D of handler address
    jmp set_nmi_vector                                                ; 9e28: 4c 0e 0d    L..            ; Set NMI vector and return

; ***************************************************************************************
; TX scout ACK: write source address
; 
; Writes our station ID and network=0 to TX FIFO, completing the
; 4-byte scout ACK frame. Then proceeds to send the data frame.
; ***************************************************************************************
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 9e2b: ad 18 fe    ...            ; Read our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9e2e: 2c a0 fe    ,..            ; BIT SR1: check TDRA before writing
    bvc data_tx_error                                                 ; 9e31: 50 5b       P[             ; TDRA not ready: TX error
    sta econet_data_continue_frame                                    ; 9e33: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9e36: a9 00       ..             ; Network = 0 (local network)
    sta econet_data_continue_frame                                    ; 9e38: 8d a2 fe    ...            ; Write network byte to TX FIFO
; &9e3b referenced 1 time by &99b5
.data_tx_begin
    lda #2                                                            ; 9e3b: a9 02       ..             ; Test bit 1 of tx_flags
    bit tx_flags                                                      ; 9e3d: 2c 4a 0d    ,J.            ; Check if immediate-op or data-transfer
    bne install_imm_data_nmi                                          ; 9e40: d0 07       ..             ; Bit 1 set: immediate op, use alt handler
    lda #&50 ; 'P'                                                    ; 9e42: a9 50       .P             ; Install nmi_data_tx at &9E50
    ldy #&9e                                                          ; 9e44: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9e46: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; &9e49 referenced 1 time by &9e40
.install_imm_data_nmi
    lda #&a4                                                          ; 9e49: a9 a4       ..             ; Install nmi_data_tx_tube at &9EA4
    ldy #&9e                                                          ; 9e4b: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9e4d: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; ***************************************************************************************
; TX data phase: send payload
; 
; Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
; Same pattern as the NMI TX handler at &9D4C but reads from the port
; buffer instead of the TX workspace. Writes two bytes per iteration,
; checking SR1 IRQ between pairs for tight looping.
; ***************************************************************************************
.nmi_data_tx
    ldy port_buf_len                                                  ; 9e50: a4 a2       ..             ; Y = buffer offset, resume from last position
    bit econet_control1_or_status1                                    ; 9e52: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
; &9e55 referenced 1 time by &9e78
.data_tx_check_fifo
    bvc data_tx_error                                                 ; 9e55: 50 37       P7             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 9e57: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 9e59: 8d a2 fe    ...            ; Write first byte of pair to FIFO
    iny                                                               ; 9e5c: c8          .              ; Advance buffer offset
    bne write_second_tx_byte                                          ; 9e5d: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 9e5f: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 9e61: f0 1a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 9e63: e6 a5       ..             ; Increment buffer high byte
; &9e65 referenced 1 time by &9e5d
.write_second_tx_byte
    lda (open_port_buf),y                                             ; 9e65: b1 a4       ..             ; Load second byte of pair
    sta econet_data_continue_frame                                    ; 9e67: 8d a2 fe    ...            ; Write second byte to FIFO
    iny                                                               ; 9e6a: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 9e6b: 84 a2       ..             ; Save updated buffer position
    bne check_irq_loop                                                ; 9e6d: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 9e6f: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 9e71: f0 0a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 9e73: e6 a5       ..             ; Increment buffer high byte
; &9e75 referenced 1 time by &9e6d
.check_irq_loop
    bit econet_control1_or_status1                                    ; 9e75: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) for tight loop
    bmi data_tx_check_fifo                                            ; 9e78: 30 db       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 9e7a: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; &9e7d referenced 4 times by &9e61, &9e71, &9ebd, &9ed3
.data_tx_last
    lda #&3f ; '?'                                                    ; 9e7d: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 9e7f: 8d a1 fe    ...            ; Write CR2 to close frame
    lda tx_flags                                                      ; 9e82: ad 4a 0d    .J.            ; Check tx_flags for next action
    bpl install_saved_handler                                         ; 9e85: 10 14       ..             ; Bit7 clear: error, install saved handler
    lda #&34 ; '4'                                                    ; 9e87: a9 34       .4             ; Install discard_reset_listen at &9A34
    ldy #&9a                                                          ; 9e89: a0 9a       ..             ; High byte of &9A34 handler
    jmp set_nmi_vector                                                ; 9e8b: 4c 0e 0d    L..            ; Set NMI vector and return

; &9e8e referenced 4 times by &9e19, &9e31, &9e55, &9ea7
.data_tx_error
    lda tx_flags                                                      ; 9e8e: ad 4a 0d    .J.            ; Load saved next handler low byte
    bpl nmi_tx_not_listening                                          ; 9e91: 10 03       ..             ; bit7 clear: error path
    jmp discard_reset_listen                                          ; 9e93: 4c 34 9a    L4.            ; ADLC reset and return to idle

; &9e96 referenced 1 time by &9e91
.nmi_tx_not_listening
    lda #&41 ; 'A'                                                    ; 9e96: a9 41       .A             ; A=&41: 'not listening' error
.jmp_tx_result_fail
    jmp tx_store_result                                               ; 9e98: 4c 3f 9f    L?.            ; Store result and return to idle

; &9e9b referenced 1 time by &9e85
.install_saved_handler
    lda nmi_next_lo                                                   ; 9e9b: ad 4b 0d    .K.            ; Load saved handler low byte
    ldy nmi_next_hi                                                   ; 9e9e: ac 4c 0d    .L.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 9ea1: 4c 0e 0d    L..            ; Install saved handler and return

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 9ea4: 2c a0 fe    ,..            ; Tube TX: BIT SR1 test TDRA
; &9ea7 referenced 1 time by &9ed8
.tube_tx_fifo_write
    bvc data_tx_error                                                 ; 9ea7: 50 e5       P.             ; TDRA not ready -- error
    lda tube_data_register_3                                          ; 9ea9: ad e5 fe    ...            ; Read byte from Tube R3
    sta econet_data_continue_frame                                    ; 9eac: 8d a2 fe    ...            ; Write to TX FIFO
    inc port_buf_len                                                  ; 9eaf: e6 a2       ..             ; Increment 4-byte buffer counter
    bne write_second_tube_byte                                        ; 9eb1: d0 0c       ..             ; Low byte didn't wrap
    inc port_buf_len_hi                                               ; 9eb3: e6 a3       ..             ; Carry into second byte
    bne write_second_tube_byte                                        ; 9eb5: d0 08       ..             ; No further carry
    inc open_port_buf                                                 ; 9eb7: e6 a4       ..             ; Carry into third byte
    bne write_second_tube_byte                                        ; 9eb9: d0 04       ..             ; No further carry
    inc open_port_buf_hi                                              ; 9ebb: e6 a5       ..             ; Carry into fourth byte
    beq data_tx_last                                                  ; 9ebd: f0 be       ..             ; Counter wrapped to zero: last data
; &9ebf referenced 3 times by &9eb1, &9eb5, &9eb9
.write_second_tube_byte
    lda tube_data_register_3                                          ; 9ebf: ad e5 fe    ...            ; Read second Tube byte from R3
    sta econet_data_continue_frame                                    ; 9ec2: 8d a2 fe    ...            ; Write second byte to TX FIFO
    inc port_buf_len                                                  ; 9ec5: e6 a2       ..             ; Increment 4-byte counter (second byte)
    bne check_tube_irq_loop                                           ; 9ec7: d0 0c       ..             ; Low byte didn't wrap
.tube_tx_inc_byte2
tube_tx_byte2_operand = tube_tx_inc_byte2+1
    inc port_buf_len_hi                                               ; 9ec9: e6 a3       ..             ; Carry into second byte
; &9eca referenced 1 time by &9cc5
    bne check_tube_irq_loop                                           ; 9ecb: d0 08       ..             ; No further carry
.tube_tx_inc_byte3
    inc open_port_buf                                                 ; 9ecd: e6 a4       ..             ; Carry into third byte
    bne check_tube_irq_loop                                           ; 9ecf: d0 04       ..             ; No further carry
.tube_tx_inc_byte4
tube_tx_byte4_operand = tube_tx_inc_byte4+1
    inc open_port_buf_hi                                              ; 9ed1: e6 a5       ..             ; Carry into fourth byte
; &9ed2 referenced 1 time by &9cbf
    beq data_tx_last                                                  ; 9ed3: f0 a8       ..             ; Counter wrapped to zero: last data
; &9ed5 referenced 3 times by &9ec7, &9ecb, &9ecf
.check_tube_irq_loop
    bit econet_control1_or_status1                                    ; 9ed5: 2c a0 fe    ,..            ; BIT SR1: test IRQ for tight loop
    bmi tube_tx_fifo_write                                            ; 9ed8: 30 cd       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 9eda: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; ***************************************************************************************
; Four-way handshake: switch to RX for final ACK
; 
; After the data frame TX completes, switches to RX mode (CR1=&82)
; and installs &9EE9 to receive the final ACK from the remote station.
; ***************************************************************************************
; &9edd referenced 1 time by &9da8
.handshake_await_ack
    lda #&82                                                          ; 9edd: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 9edf: 8d a0 fe    ...            ; Write to ADLC CR1
    lda #&e9                                                          ; 9ee2: a9 e9       ..             ; Install handler at &9EE9 (RX final ACK)
    ldy #&9e                                                          ; 9ee4: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9ee6: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

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
    lda #1                                                            ; 9ee9: a9 01       ..             ; A=&01: AP mask
    bit econet_control23_or_status2                                   ; 9eeb: 2c a1 fe    ,..            ; BIT SR2: test AP
    beq tx_result_fail                                                ; 9eee: f0 4d       .M             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9ef0: ad a2 fe    ...            ; Read dest station
    cmp station_id_disable_net_nmis                                   ; 9ef3: cd 18 fe    ...            ; Compare to our station (INTOFF side effect)
    bne tx_result_fail                                                ; 9ef6: d0 45       .E             ; Not our station -- error
    lda #&ff                                                          ; 9ef8: a9 ff       ..             ; Install handler at &9EFF (final ACK continuation)
    ldy #&9e                                                          ; 9efa: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9efc: 4c 0e 0d    L..            ; Install continuation handler

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 9eff: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9f02: 10 39       .9             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9f04: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 9f07: d0 34       .4             ; Non-zero -- network mismatch, error
    lda #&15                                                          ; 9f09: a9 15       ..             ; Install handler at &9F15 (final ACK validation)
    ldy #&9f                                                          ; 9f0b: a0 9f       ..             ; High byte of handler address
    bit econet_control1_or_status1                                    ; 9f0d: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 9f10: 30 03       0.             ; IRQ set -- fall through to &9F15 without RTI
    jmp set_nmi_vector                                                ; 9f12: 4c 0e 0d    L..            ; Install handler and RTI

; ***************************************************************************************
; Final ACK validation
; 
; Reads and validates src_stn and src_net against original TX dest.
; Then checks FV for frame completion.
; ***************************************************************************************
; &9f15 referenced 1 time by &9f10
.nmi_final_ack_validate
    bit econet_control23_or_status2                                   ; 9f15: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9f18: 10 23       .#             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9f1a: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9f1d: cd 20 0d    . .            ; Compare to TX dest station (&0D20)
    bne tx_result_fail                                                ; 9f20: d0 1b       ..             ; Mismatch -- error
    lda econet_data_continue_frame                                    ; 9f22: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9f25: cd 21 0d    .!.            ; Compare to TX dest network (&0D21)
    bne tx_result_fail                                                ; 9f28: d0 13       ..             ; Mismatch -- error
    lda tx_flags                                                      ; 9f2a: ad 4a 0d    .J.            ; Load TX flags for next action
    bpl check_fv_final_ack                                            ; 9f2d: 10 03       ..             ; bit7 clear: no data phase
    jmp install_data_rx_handler                                       ; 9f2f: 4c 70 98    Lp.            ; Install data RX handler

; &9f32 referenced 1 time by &9f2d
.check_fv_final_ack
    lda #2                                                            ; 9f32: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9f34: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq tx_result_fail                                                ; 9f37: f0 04       ..             ; No FV -- error
; ***************************************************************************************
; TX completion handler
; 
; Stores result code 0 (success) into the first byte of the TX control
; block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
; and calls full ADLC reset + idle listen via &9A34.
; ***************************************************************************************
; &9f39 referenced 2 times by &9963, &9d9e
.tx_result_ok
    lda #0                                                            ; 9f39: a9 00       ..             ; A=0: success result code
    beq tx_store_result                                               ; 9f3b: f0 02       ..             ; BEQ: always taken (A=0); ALWAYS branch

; ***************************************************************************************
; TX failure: not listening
; 
; Loads error code &41 (not listening) and falls through to
; tx_store_result. The most common TX error path — reached from
; 11 sites across the final-ACK validation chain when the remote
; station doesn't respond or the frame is malformed.
; ***************************************************************************************
; &9f3d referenced 8 times by &9eee, &9ef6, &9f02, &9f07, &9f18, &9f20, &9f28, &9f37
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 9f3d: a9 41       .A             ; A=&41: not listening error code
; ***************************************************************************************
; TX error handler
; 
; Stores error code (A) into the TX control block, sets &0D3A bit7
; for completion, and returns to idle via &9A34.
; Error codes: &00=success, &40=line jammed, &41=not listening,
; &42=net error.
; ***************************************************************************************
; &9f3f referenced 5 times by &9891, &9d85, &9de0, &9e98, &9f3b
.tx_store_result
    ldy #0                                                            ; 9f3f: a0 00       ..             ; Y=0: index into TX control block
    sta (nmi_tx_block),y                                              ; 9f41: 91 a0       ..             ; Store result/error code at (nmi_tx_block),0
    lda #&80                                                          ; 9f43: a9 80       ..             ; &80: completion flag for &0D3A
    sta tx_ctrl_status                                                ; 9f45: 8d 3a 0d    .:.            ; Signal TX complete
    jmp discard_reset_listen                                          ; 9f48: 4c 34 9a    L4.            ; Full ADLC reset and return to idle listen

; Unreferenced data block (purpose unknown)
    equb &0e, &0e, &0a, &0a, &0a, 6, 6, &0a, &81, 0, 0, 0, 0, 1, 1    ; 9f4b: 0e 0e 0a... ...
    equb &81                                                          ; 9f5a: 81          .

; ***************************************************************************************
; Calculate transfer size
; 
; Computes the number of bytes actually transferred during a data
; frame reception. Subtracts the low pointer (LPTR, offset 4 in
; the RXCB) from the current buffer position to get the byte count,
; and stores it back into the RXCB's high pointer field (HPTR,
; offset 8). This tells the caller how much data was received.
; ***************************************************************************************
; &9f5b referenced 5 times by &980e, &9aee, &9d05, &9d10, &9d42
.tx_calc_transfer
    ldy #6                                                            ; 9f5b: a0 06       ..             ; Load RXCB[6] (buffer addr byte 2)
    lda (nmi_tx_block),y                                              ; 9f5d: b1 a0       ..             ; Load TX block byte at offset 6
    iny                                                               ; 9f5f: c8          .              ; Y=&07
    and (nmi_tx_block),y                                              ; 9f60: 31 a0       1.             ; AND with TX block[7] (byte 3)
    cmp #&ff                                                          ; 9f62: c9 ff       ..             ; Both &FF = no buffer?
    beq fallback_calc_transfer                                        ; 9f64: f0 41       .A             ; Yes: fallback path
    lda tx_in_progress                                                ; 9f66: ad 52 0d    .R.            ; Tube transfer in progress?
    beq fallback_calc_transfer                                        ; 9f69: f0 3c       .<             ; No: fallback path
    lda tx_flags                                                      ; 9f6b: ad 4a 0d    .J.            ; Load TX flags for transfer setup
    ora #2                                                            ; 9f6e: 09 02       ..             ; Set bit 1 (transfer complete)
    sta tx_flags                                                      ; 9f70: 8d 4a 0d    .J.            ; Store with bit 1 set (Tube xfer)
    sec                                                               ; 9f73: 38          8              ; Init borrow for 4-byte subtract
    php                                                               ; 9f74: 08          .              ; Save carry on stack
    ldy #4                                                            ; 9f75: a0 04       ..             ; Y=4: start at RXCB offset 4
; &9f77 referenced 1 time by &9f89
.calc_transfer_size
    lda (nmi_tx_block),y                                              ; 9f77: b1 a0       ..             ; Load RXCB[Y] (current ptr byte)
    iny                                                               ; 9f79: c8          .              ; Y += 4: advance to RXCB[Y+4]
    iny                                                               ; 9f7a: c8          .              ; Y += 4: advance to high ptr offset
    iny                                                               ; 9f7b: c8          .              ; (continued)
    iny                                                               ; 9f7c: c8          .              ; (continued)
    plp                                                               ; 9f7d: 28          (              ; Restore borrow from previous byte
    sbc (nmi_tx_block),y                                              ; 9f7e: f1 a0       ..             ; Subtract RXCB[Y+4] (start ptr byte)
    sta net_tx_ptr,y                                                  ; 9f80: 99 9a 00    ...            ; Store result byte
    dey                                                               ; 9f83: 88          .              ; Y -= 3: next source byte
    dey                                                               ; 9f84: 88          .              ; Y -= 3: back to next low ptr byte
    dey                                                               ; 9f85: 88          .              ; (continued)
    php                                                               ; 9f86: 08          .              ; Save borrow for next byte
    cpy #8                                                            ; 9f87: c0 08       ..             ; Done all 4 bytes?
    bcc calc_transfer_size                                            ; 9f89: 90 ec       ..             ; No: next byte pair
    plp                                                               ; 9f8b: 28          (              ; Discard final borrow
    txa                                                               ; 9f8c: 8a          .              ; A = saved X
    pha                                                               ; 9f8d: 48          H              ; Save X
    lda #4                                                            ; 9f8e: a9 04       ..             ; Compute address of RXCB+4
    clc                                                               ; 9f90: 18          .              ; CLC for base pointer addition
    adc nmi_tx_block                                                  ; 9f91: 65 a0       e.             ; Add RXCB base to get RXCB+4 addr
    tax                                                               ; 9f93: aa          .              ; X = low byte of RXCB+4
    ldy nmi_tx_block_hi                                               ; 9f94: a4 a1       ..             ; Y = high byte of RXCB ptr
    lda #&c2                                                          ; 9f96: a9 c2       ..             ; Tube claim type &C2
    jsr tube_addr_claim                                               ; 9f98: 20 06 04     ..            ; Claim Tube transfer address
    bcc restore_x_and_return                                          ; 9f9b: 90 07       ..             ; No Tube: skip reclaim
    lda scout_status                                                  ; 9f9d: ad 5c 0d    .\.            ; Tube: reclaim with scout status
    jsr tube_addr_claim                                               ; 9fa0: 20 06 04     ..            ; Reclaim with scout status type
    sec                                                               ; 9fa3: 38          8              ; C=1: Tube address claimed
; &9fa4 referenced 1 time by &9f9b
.restore_x_and_return
    pla                                                               ; 9fa4: 68          h              ; Restore X
    tax                                                               ; 9fa5: aa          .              ; Restore X from stack
    rts                                                               ; 9fa6: 60          `              ; Return with C = transfer status

; &9fa7 referenced 2 times by &9f64, &9f69
.fallback_calc_transfer
    ldy #4                                                            ; 9fa7: a0 04       ..             ; Y=4: RXCB current pointer offset
    lda (nmi_tx_block),y                                              ; 9fa9: b1 a0       ..             ; Load RXCB[4] (current ptr lo)
    ldy #8                                                            ; 9fab: a0 08       ..             ; Y=8: RXCB start address offset
    sec                                                               ; 9fad: 38          8              ; Set carry for subtraction
    sbc (nmi_tx_block),y                                              ; 9fae: f1 a0       ..             ; Subtract RXCB[8] (start ptr lo)
    sta port_buf_len                                                  ; 9fb0: 85 a2       ..             ; Store transfer size lo
    ldy #5                                                            ; 9fb2: a0 05       ..             ; Y=5: current ptr hi offset
    lda (nmi_tx_block),y                                              ; 9fb4: b1 a0       ..             ; Load RXCB[5] (current ptr hi)
    sbc #0                                                            ; 9fb6: e9 00       ..             ; Propagate borrow from lo subtraction
    sta open_port_buf_hi                                              ; 9fb8: 85 a5       ..             ; Temp store adjusted current ptr hi
    ldy #8                                                            ; 9fba: a0 08       ..             ; Y=8: start address lo offset
    lda (nmi_tx_block),y                                              ; 9fbc: b1 a0       ..             ; Copy RXCB[8] to open port buffer lo
    sta open_port_buf                                                 ; 9fbe: 85 a4       ..             ; Store to scratch (side effect)
    ldy #9                                                            ; 9fc0: a0 09       ..             ; Y=9: start address hi offset
    lda (nmi_tx_block),y                                              ; 9fc2: b1 a0       ..             ; Load RXCB[9] (start ptr hi)
    sec                                                               ; 9fc4: 38          8              ; Set carry for subtraction
    sbc open_port_buf_hi                                              ; 9fc5: e5 a5       ..             ; start_hi - adjusted current_hi
    sta port_buf_len_hi                                               ; 9fc7: 85 a3       ..             ; Store transfer size hi
    sec                                                               ; 9fc9: 38          8              ; Return with C=1
; &9fca referenced 1 time by &96d1
.nmi_shim_rom_src
    rts                                                               ; 9fca: 60          `              ; Return with C=1 (success)

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
    bit station_id_disable_net_nmis                                   ; 9fcb: 2c 18 fe    ,..            ; INTOFF: disable NMIs while switching ROM
    pha                                                               ; 9fce: 48          H              ; Save A
    tya                                                               ; 9fcf: 98          .              ; Transfer Y to A
    pha                                                               ; 9fd0: 48          H              ; Save Y (via A)
    lda #0                                                            ; 9fd1: a9 00       ..             ; ROM bank 0 (patched during init for actual bank)
    sta romsel                                                        ; 9fd3: 8d 30 fe    .0.            ; Select Econet ROM bank via ROMSEL
    jmp nmi_rx_scout                                                  ; 9fd6: 4c f6 96    L..            ; Jump to scout handler in ROM

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
    sty nmi_jmp_hi                                                    ; 9fd9: 8c 0d 0d    ...            ; Store handler high byte at &0D0D
    sta nmi_jmp_lo                                                    ; 9fdc: 8d 0c 0d    ...            ; Store handler low byte at &0D0C
    lda romsel_copy                                                   ; 9fdf: a5 f4       ..             ; Restore NFS ROM bank
    sta romsel                                                        ; 9fe1: 8d 30 fe    .0.            ; Page in via hardware latch
    pla                                                               ; 9fe4: 68          h              ; Restore Y from stack
    tay                                                               ; 9fe5: a8          .              ; Transfer ROM bank to Y
    pla                                                               ; 9fe6: 68          h              ; Restore A from stack
    bit video_ula_control                                             ; 9fe7: 2c 20 fe    , .            ; INTON: re-enable NMIs
    rti                                                               ; 9fea: 40          @              ; Return from interrupt

.rom_nmi_tail
    lda tx_flags                                                      ; 9feb: ad 4a 0d    .J.            ; Load current TX flags
    ora #2                                                            ; 9fee: 09 02       ..             ; Set bit 1 (transfer mode flag)
    sta tx_flags                                                      ; 9ff0: 8d 4a 0d    .J.            ; Store updated TX flags
    sec                                                               ; 9ff3: 38          8              ; SEC for subtraction
    php                                                               ; 9ff4: 08          .              ; Save carry on stack
    ldy #4                                                            ; 9ff5: a0 04       ..             ; Y=4: TXCB data start low offset
    lda (nmi_tx_block),y                                              ; 9ff7: b1 a0       ..             ; Load data start low byte
    iny                                                               ; 9ff9: c8          .              ; Y=&05
    iny                                                               ; 9ffa: c8          .              ; Y=&06
    iny                                                               ; 9ffb: c8          .              ; Y=&07
    iny                                                               ; 9ffc: c8          .              ; Y=&08
    plp                                                               ; 9ffd: 28          (              ; Restore carry for subtraction
    sbc (nmi_tx_block),y                                              ; 9ffe: f1 a0       ..             ; Subtract buffer end from start
.pydis_end

    assert <(dispatch_net_cmd-1) == &68
    assert <(econet_tx_rx-1) == &72
    assert <(fscv_0_opt-1) == &a1
    assert <(fscv_1_eof-1) == &1f
    assert <(fscv_3_star_cmd-1) == &92
    assert <(fscv_5_cat-1) == &fd
    assert <(fscv_6_shutdown-1) == &fd
    assert <(fscv_7_read_handles-1) == &da
    assert <(fsreply_0_print_dir-1) == &73
    assert <(fsreply_1_copy_handles_boot-1) == &1f
    assert <(fsreply_2_copy_handles-1) == &20
    assert <(fsreply_3_set_csd-1) == &fc
    assert <(fsreply_4_notify_exec-1) == &84
    assert <(fsreply_5_set_lib-1) == &f7
    assert <(imm_op_status3-1) == &e3
    assert <(l0130) == &30
    assert <(lang_0_insert_remote_key-1) == &4a
    assert <(lang_1_remote_boot-1) == &fc
    assert <(lang_2_save_palette_vdu-1) == &91
    assert <(lang_3_execute_at_0100-1) == &2a
    assert <(lang_4_remote_validated-1) == &3a
    assert <(net_1_read_handle-1) == &af
    assert <(net_2_read_handle_entry-1) == &c9
    assert <(net_3_close_handle-1) == &df
    assert <(net_4_resume_remote-1) == &f2
    assert <(net_write_char-1) == &3d
    assert <(osword_0f_handler-1) == &33
    assert <(osword_10_handler-1) == &f0
    assert <(osword_11_handler-1) == &53
    assert <(osword_12_handler-1) == &7b
    assert <(printer_select_handler-1) == &b5
    assert <(remote_cmd_data-1) == &cd
    assert <(remote_cmd_dispatch-1) == &63
    assert <(remote_print_handler-1) == &c7
    assert <(return_2-1) == &44
    assert <(rx_imm_exec-1) == &9e
    assert <(rx_imm_halt_cont-1) == &00
    assert <(rx_imm_machine_type-1) == &c7
    assert <(rx_imm_peek-1) == &da
    assert <(rx_imm_poke-1) == &bc
    assert <(sp_dot_string) == &45
    assert <(svc_11_nmi_claim-1) == &68
    assert <(svc_12_nmi_release-1) == &65
    assert <(svc_1_abs_workspace-1) == &6f
    assert <(svc_2_private_workspace-1) == &78
    assert <(svc_3_autoboot-1) == &d1
    assert <(svc_4_star_command-1) == &71
    assert <(svc_5_unknown_irq-1) == &6b
    assert <(svc_8_osword-1) == &f7
    assert <(svc_9_help-1) == &bb
    assert <(tx_ctrl_exit-1) == &44
    assert <(tx_ctrl_peek-1) == &e7
    assert <(tx_ctrl_poke-1) == &eb
    assert <(tx_ctrl_proc-1) == &0a
    assert <(tx_done_continue-1) == &d4
    assert <(tx_done_halt-1) == &bd
    assert <(tx_done_jsr-1) == &9a
    assert <(tx_done_os_proc-1) == &b1
    assert <(tx_done_user_proc-1) == &a3
    assert >(dispatch_net_cmd-1) == &80
    assert >(econet_tx_rx-1) == &8f
    assert >(fscv_0_opt-1) == &89
    assert >(fscv_1_eof-1) == &88
    assert >(fscv_3_star_cmd-1) == &8b
    assert >(fscv_5_cat-1) == &8b
    assert >(fscv_6_shutdown-1) == &82
    assert >(fscv_7_read_handles-1) == &85
    assert >(fsreply_0_print_dir-1) == &8d
    assert >(fsreply_1_copy_handles_boot-1) == &8d
    assert >(fsreply_2_copy_handles-1) == &8d
    assert >(fsreply_3_set_csd-1) == &8c
    assert >(fsreply_4_notify_exec-1) == &8d
    assert >(fsreply_5_set_lib-1) == &8c
    assert >(imm_op_status3-1) == &9c
    assert >(l0130) == &01
    assert >(lang_0_insert_remote_key-1) == &91
    assert >(lang_1_remote_boot-1) == &90
    assert >(lang_2_save_palette_vdu-1) == &92
    assert >(lang_3_execute_at_0100-1) == &91
    assert >(lang_4_remote_validated-1) == &91
    assert >(net_1_read_handle-1) == &8d
    assert >(net_2_read_handle_entry-1) == &8d
    assert >(net_3_close_handle-1) == &8d
    assert >(net_4_resume_remote-1) == &8d
    assert >(net_write_char-1) == &90
    assert >(osword_0f_handler-1) == &8e
    assert >(osword_10_handler-1) == &8e
    assert >(osword_11_handler-1) == &8e
    assert >(osword_12_handler-1) == &8e
    assert >(printer_select_handler-1) == &91
    assert >(remote_cmd_data-1) == &90
    assert >(remote_cmd_dispatch-1) == &90
    assert >(remote_print_handler-1) == &91
    assert >(return_2-1) == &81
    assert >(rx_imm_exec-1) == &9a
    assert >(rx_imm_halt_cont-1) == &9b
    assert >(rx_imm_machine_type-1) == &9a
    assert >(rx_imm_peek-1) == &9a
    assert >(rx_imm_poke-1) == &9a
    assert >(sp_dot_string) == &84
    assert >(svc_11_nmi_claim-1) == &96
    assert >(svc_12_nmi_release-1) == &96
    assert >(svc_1_abs_workspace-1) == &82
    assert >(svc_2_private_workspace-1) == &82
    assert >(svc_3_autoboot-1) == &81
    assert >(svc_4_star_command-1) == &81
    assert >(svc_5_unknown_irq-1) == &96
    assert >(svc_8_osword-1) == &8d
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
    assert tube_osbyte_long == &063b
    assert tube_osbyte_short == &0626
    assert tube_oscli == &05c5
    assert tube_osfile == &05d8
    assert tube_osfind == &0569
    assert tube_osgbpb == &0602
    assert tube_osrdch == &055b
    assert tube_osword == &065d
    assert tube_osword_rdln == &06a3
    assert tube_release_return == &053d
    assert tube_restore_regs == &04ef

save pydis_start, pydis_end

; Label references by decreasing frequency:
;     nfs_workspace:                           53
;     econet_control23_or_status2:             45
;     fs_options:                              41
;     econet_data_continue_frame:              37
;     fs_cmd_data:                             36
;     net_rx_ptr:                              35
;     econet_control1_or_status1:              31
;     nmi_tx_block:                            31
;     osword_pb_ptr:                           28
;     tx_flags:                                28
;     port_ws_offset:                          24
;     fs_load_addr_2:                          23
;     net_tx_ptr:                              23
;     osbyte:                                  22
;     set_nmi_vector:                          22
;     tube_read_r2:                            22
;     fs_crc_lo:                               21
;     port_buf_len:                            20
;     rx_status_flags:                         18
;     tube_send_r2:                            18
;     open_port_buf_hi:                        16
;     fs_func_code:                            15
;     station_id_disable_net_nmis:             15
;     nfs_temp:                                14
;     open_port_buf:                           14
;     fs_load_addr:                            13
;     port_buf_len_hi:                         13
;     print_inline:                            13
;     fs_error_ptr:                            12
;     nmi_error_dispatch:                      12
;     prepare_fs_cmd:                          12
;     rx_error:                                12
;     tube_data_register_2:                    12
;     tube_status_register_2:                  11
;     fs_last_byte_flag:                       10
;     nfs_workspace_hi:                        10
;     rom_svc_num:                             10
;     tube_addr_claim:                         10
;     txcb_start:                              10
;     nmi_tx_block_hi:                          9
;     prot_status:                              9
;     rx_src_stn:                               9
;     tube_data_register_3:                     9
;     txcb_end:                                 9
;     fs_work_4:                                8
;     l0d60:                                    8
;     restore_args_return:                      8
;     tx_result_fail:                           8
;     zp_ptr_lo:                                8
;     fs_block_offset:                          7
;     fs_cmd_urd:                               7
;     fs_crc_hi:                                7
;     fs_load_addr_3:                           7
;     reply_error:                              7
;     tube_main_loop:                           7
;     tx_dst_stn:                               7
;     clear_svc_restore_args:                   6
;     fs_cmd_csd:                               6
;     fs_load_addr_hi:                          6
;     fs_sequence_nos:                          6
;     net_rx_ptr_hi:                            6
;     net_tx_ptr_hi:                            6
;     nmi_rti:                                  6
;     osasci:                                   6
;     return_1:                                 6
;     rx_buf_offset:                            6
;     save_fscv_args:                           6
;     scout_status:                             6
;     tube_status_1_and_tube_control:           6
;     tx_ctrl_status:                           6
;     tx_in_progress:                           6
;     zp_temp_10:                               6
;     calc_handle_offset:                       5
;     copy_param_block:                         5
;     dispatch:                                 5
;     fs_data_count:                            5
;     l0106:                                    5
;     printer_buf_ptr:                          5
;     restore_xy_return:                        5
;     rx_ctrl:                                  5
;     scout_error:                              5
;     set_fs_flag:                              5
;     system_via_acr:                           5
;     tube_reply_byte:                          5
;     tube_send_r1:                             5
;     tube_send_r4:                             5
;     tube_status_register_4_and_cpu_control:   5
;     tx_calc_transfer:                         5
;     tx_dst_net:                               5
;     tx_store_result:                          5
;     zp_ptr_hi:                                5
;     zp_temp_11:                               5
;     clear_jsr_protection:                     4
;     copy_string_to_cmd:                       4
;     data_tx_error:                            4
;     data_tx_last:                             4
;     discard_reset_listen:                     4
;     fs_boot_option:                           4
;     fs_eof_flags:                             4
;     fs_server_net:                            4
;     fs_spool0:                                4
;     fs_work_7:                                4
;     l0100:                                    4
;     l0101:                                    4
;     l0d58:                                    4
;     nmi_next_hi:                              4
;     nmi_next_lo:                              4
;     osbyte_a_copy:                            4
;     osrdsc_ptr:                               4
;     print_spaces:                             4
;     restore_ay_return:                        4
;     rx_port:                                  4
;     rx_src_net:                               4
;     tube_claimed_id:                          4
;     tx_done_exit:                             4
;     tx_length:                                4
;     txcb_ctrl:                                4
;     txcb_port:                                4
;     video_ula_control:                        4
;     addr_work:                                3
;     adlc_full_reset:                          3
;     carry_exit_or_read:                       3
;     check_tube_irq_loop:                      3
;     clear_fs_flag:                            3
;     clear_svc_return:                         3
;     copy_filename:                            3
;     copy_string_from_offset:                  3
;     ctrl_block_setup_alt:                     3
;     data_rx_complete:                         3
;     data_rx_tube_error:                       3
;     dispatch_remote_osbyte:                   3
;     flush_r3_nmi_check:                       3
;     fs_csd_handle:                            3
;     fs_getb_buf:                              3
;     fs_handle_mask:                           3
;     fs_messages_flag:                         3
;     fs_reply_cmd:                             3
;     fs_server_stn:                            3
;     fs_urd_handle:                            3
;     handle_to_mask_a:                         3
;     handle_to_mask_clc:                       3
;     imm_op_discard:                           3
;     imm_op_dispatch:                          3
;     incpx:                                    3
;     init_tx_ctrl_block:                       3
;     l00b6:                                    3
;     match_osbyte_code:                        3
;     next_port_slot:                           3
;     openl4:                                   3
;     os_text_ptr:                              3
;     oscli:                                    3
;     osword:                                   3
;     pad_filename_spaces:                      3
;     print_reply_bytes:                        3
;     return_a_zero:                            3
;     romsel_copy:                              3
;     rx_check_error:                           3
;     rx_ctrl_copy:                             3
;     rx_update_buf:                            3
;     scout_no_match:                           3
;     send_to_fs_star:                          3
;     set_handle_return:                        3
;     setup_tx_and_send:                        3
;     skip_spaces:                              3
;     test_inactive_retry:                      3
;     tube_claim_flag:                          3
;     tube_claim_loop:                          3
;     tube_data_register_4:                     3
;     tube_read_string:                         3
;     tube_reply_ack:                           3
;     tx_clear_flag:                            3
;     tx_ctrl_exit:                             3
;     tx_ctrl_upper:                            3
;     tx_index:                                 3
;     tx_poll_ff:                               3
;     write_second_tube_byte:                   3
;     ack_scout_match:                          2
;     ack_tx:                                   2
;     ack_tx_write_dest:                        2
;     adjust_addrs:                             2
;     beginr:                                   2
;     binary_version:                           2
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
;     data_rx_tube_complete:                    2
;     decode_attribs_5bit:                      2
;     decode_attribs_6bit:                      2
;     delay_1ms:                                2
;     discard_after_reset:                      2
;     discard_listen:                           2
;     econet_tx_retry:                          2
;     escape_flag:                              2
;     fallback_calc_transfer:                   2
;     find_cr_terminator:                       2
;     flush_output_block:                       2
;     fs_access_level:                          2
;     fs_cmd_context:                           2
;     fs_cmd_match_table:                       2
;     fs_cmd_y_param:                           2
;     fs_context_hi:                            2
;     fs_error_flags:                           2
;     fs_file_len_3:                            2
;     fs_last_error:                            2
;     fs_lib_handle:                            2
;     fs_load_vector:                           2
;     fs_obj_type:                              2
;     fs_putb_buf:                              2
;     fs_state_deb:                             2
;     fs_work_5:                                2
;     gbpb_done:                                2
;     handle_mask_exit:                         2
;     imm_op_out_of_range:                      2
;     init_tx_ctrl_port:                        2
;     install_rx_scout_handler:                 2
;     l0102:                                    2
;     l0103:                                    2
;     l0130:                                    2
;     l0700:                                    2
;     l0d1e:                                    2
;     l0d59:                                    2
;     language_entry:                           2
;     mask_to_handle:                           2
;     match_rom_string:                         2
;     net_handle_validate:                      2
;     nlisne:                                   2
;     nmi_jmp_hi:                               2
;     nmi_jmp_lo:                               2
;     no_dot_exit:                              2
;     num01:                                    2
;     nvwrch:                                   2
;     opter1:                                   2
;     osfind:                                   2
;     osword_pb_ptr_hi:                         2
;     parse_decimal:                            2
;     poll_r2_reply:                            2
;     prepare_cmd_clv:                          2
;     prepare_fs_cmd_v:                         2
;     print_decimal:                            2
;     print_decimal_digit:                      2
;     print_dir_from_offset:                    2
;     print_file_info:                          2
;     print_hex:                                2
;     print_hex_bytes:                          2
;     print_hex_digit:                          2
;     print_reply_counted:                      2
;     print_space:                              2
;     prlp1:                                    2
;     pydis_start:                              2
;     read_station_id:                          2
;     readc1:                                   2
;     reenable_rx:                              2
;     remot1:                                   2
;     restore_y_return:                         2
;     resume_after_remote:                      2
;     return_2:                                 2
;     return_3:                                 2
;     return_bget:                              2
;     return_copy_param:                        2
;     return_nbyte:                             2
;     return_printer_select:                    2
;     return_tube_init:                         2
;     rom_header:                               2
;     romsel:                                   2
;     run_fscv_cmd:                             2
;     rx_extra_byte:                            2
;     rxpol2:                                   2
;     scout_complete:                           2
;     send_ack:                                 2
;     send_data_blocks:                         2
;     send_data_rx_ack:                         2
;     send_fs_reply_cmd:                        2
;     send_rom_byte:                            2
;     send_to_fs:                               2
;     set_carry_dispatch:                       2
;     setup_tx_ptr_c0:                          2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     store_rxcb_completion:                    2
;     store_tube_flag:                          2
;     store_tx_error:                           2
;     sub_3_from_y:                             2
;     system_via_ier:                           2
;     system_via_ifr:                           2
;     system_via_sr:                            2
;     tdra_error:                               2
;     trampoline_tx_setup:                      2
;     transfer_file_blocks:                     2
;     tube_data_ptr:                            2
;     tube_dispatch_table:                      2
;     tube_enter_main_loop:                     2
;     tube_osbyte_send_x:                       2
;     tube_osword_read_lp:                      2
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
;     adlc_init_workspace:                      1
;     adlc_rx_listen:                           1
;     advance_rx_buffer_ptr:                    1
;     argsv_check_return:                       1
;     argsv_dispatch_a:                         1
;     argsv_zero_length:                        1
;     argsw:                                    1
;     attrib_error_exit:                        1
;     attrib_shift_bits:                        1
;     begink:                                   1
;     block_addr_loop:                          1
;     boot_option_offsets:                      1
;     brkv:                                     1
;     bspsx:                                    1
;     bsxl0:                                    1
;     bsxl1:                                    1
;     build_send_fs_cmd:                        1
;     bytex:                                    1
;     c954d:                                    1
;     calc_peek_poke_size:                      1
;     calc_transfer_size:                       1
;     cat_access_setup:                         1
;     cat_examine_continue:                     1
;     cat_init_display:                         1
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
;     check_imm_op_ctrl:                        1
;     check_imm_range:                          1
;     check_irq_loop:                           1
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
;     cmd_match_retry:                          1
;     cmd_table_entry_1:                        1
;     compare_addr_byte:                        1
;     copy_addr_loop:                           1
;     copy_attr_loop:                           1
;     copy_bcast_addr:                          1
;     copy_block_addrs:                         1
;     copy_dir_handles:                         1
;     copy_error_message:                       1
;     copy_fileptr_reply:                       1
;     copy_fileptr_to_cmd:                      1
;     copy_fs_addr:                             1
;     copy_fs_reply_to_cb:                      1
;     copy_handles_to_ws:                       1
;     copy_imm_params:                          1
;     copy_load_end_addr:                       1
;     copy_nmi_shim_loop:                       1
;     copy_nmi_workspace:                       1
;     copy_osword_params:                       1
;     copy_params_rword:                        1
;     copy_reply_bytes:                         1
;     copy_rxcb_to_param:                       1
;     copy_save_params:                         1
;     copy_scout_fields:                        1
;     copy_scout_loop:                          1
;     copyl3:                                   1
;     copyright_offset:                         1
;     count_columns_loop:                       1
;     ctrl_block_setup:                         1
;     ctrl_block_setup_clv:                     1
;     ctrl_block_template:                      1
;     data_rx_loop:                             1
;     data_tx_begin:                            1
;     data_tx_check_fifo:                       1
;     decfir:                                   1
;     decimal_divide_loop:                      1
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
;     dofs01:                                   1
;     dofs2:                                    1
;     dofsl1:                                   1
;     dofsl5:                                   1
;     dofsl7:                                   1
;     done_option_name:                         1
;     econet_data_terminate_frame:              1
;     entry1:                                   1
;     error1:                                   1
;     error_msg_table:                          1
;     error_not_listening:                      1
;     error_offsets:                            1
;     evntv:                                    1
;     execute_brk_error:                        1
;     file1:                                    1
;     filev:                                    1
;     filev_attrib_code_check:                  1
;     filev_attrib_dispatch:                    1
;     filev_save:                               1
;     findv_eof_check:                          1
;     floop:                                    1
;     forward_star_cmd:                         1
;     fs2al1:                                   1
;     fs_addr_check:                            1
;     fs_boot_data:                             1
;     fs_cmd_lib:                               1
;     fs_cmd_ptr:                               1
;     fs_cmd_type:                              1
;     fs_context_base:                          1
;     fs_error_buf:                             1
;     fs_file_attrs:                            1
;     fs_file_len:                              1
;     fs_len_clear:                             1
;     fs_load_upper:                            1
;     fs_osword_tbl_hi:                         1
;     fs_osword_tbl_lo:                         1
;     fs_reply_data:                            1
;     fs_reply_stn:                             1
;     fs_vector_addrs:                          1
;     fs_wait_cleanup:                          1
;     fs_work_16:                               1
;     fscv:                                     1
;     fscv_3_star_cmd:                          1
;     fsdiel:                                   1
;     fsreply_handle_copy:                      1
;     fstxl1:                                   1
;     fstxl2:                                   1
;     gbpb6_read_name:                          1
;     gbpb8_read_dir:                           1
;     gbpb_read_path:                           1
;     gbpb_write_path:                          1
;     gbpbe1:                                   1
;     gbpbf1:                                   1
;     gbpbf2:                                   1
;     gbpbf3:                                   1
;     gbpbl1:                                   1
;     gbpbl3:                                   1
;     gbpbv_func_dispatch:                      1
;     gbpbx:                                    1
;     gbpbx0:                                   1
;     gbpbx1:                                   1
;     get_disc_title:                           1
;     get_file_protection:                      1
;     gsinit:                                   1
;     gsread:                                   1
;     halt_spin_loop:                           1
;     halve_args_a:                             1
;     handle_bput_bget:                         1
;     handle_to_mask:                           1
;     handle_tx_result:                         1
;     handshake_await_ack:                      1
;     immediate_op:                             1
;     inactive_retry:                           1
;     inc_rxcb_buf_hi:                          1
;     info2:                                    1
;     infol2:                                   1
;     init_fs_vectors:                          1
;     init_rxcb_entries:                        1
;     init_tx_ctrl_data:                        1
;     init_tx_reply_port:                       1
;     init_vectors_and_copy:                    1
;     initl:                                    1
;     install_data_rx_handler:                  1
;     install_imm_data_nmi:                     1
;     install_nmi_shim:                         1
;     install_reply_scout:                      1
;     install_saved_handler:                    1
;     install_tube_rx:                          1
;     intoff_test_inactive:                     1
;     issue_vectors_claimed:                    1
;     jmp_clear_svc_restore:                    1
;     jmp_restore_args:                         1
;     jmp_store_rxcb:                           1
;     l0104:                                    1
;     l0350:                                    1
;     l0351:                                    1
;     l0355:                                    1
;     l0cff:                                    1
;     l0dda:                                    1
;     l0e0c:                                    1
;     l0e11:                                    1
;     l0fc5:                                    1
;     l0fc6:                                    1
;     l212e:                                    1
;     l944d:                                    1
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
;     logon3:                                   1
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
;     nlistn:                                   1
;     nmi_data_rx_bulk:                         1
;     nmi_data_rx_skip:                         1
;     nmi_final_ack_validate:                   1
;     nmi_reply_validate:                       1
;     nmi_rx_scout:                             1
;     nmi_shim_07:                              1
;     nmi_shim_1a:                              1
;     nmi_shim_rom_src:                         1
;     nmi_tx_not_listening:                     1
;     nmi_workspace_start:                      1
;     no_page_wrap:                             1
;     not_svc_12_nfs:                           1
;     nvrdch:                                   1
;     openl6:                                   1
;     openl7:                                   1
;     opt_return:                               1
;     option_name_offsets:                      1
;     option_name_strings:                      1
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
;     osnewl:                                   1
;     osrdsc_ptr_hi:                            1
;     osword_12_error:                          1
;     osword_12_subfunc:                        1
;     osword_12_ws_offsets:                     1
;     osword_tbl_hi:                            1
;     osword_tbl_lo:                            1
;     osword_trampoline:                        1
;     parse_decimal_rts:                        1
;     poll_r2_osword_result:                    1
;     poll_r3_ready:                            1
;     poll_rxcb_loop:                           1
;     poll_txcb_status:                         1
;     prepare_cmd_with_flag:                    1
;     print_exec_and_len:                       1
;     print_filename_loop:                      1
;     print_hex_nibble:                         1
;     print_inline_char:                        1
;     print_next_char:                          1
;     print_option_char:                        1
;     print_public:                             1
;     print_station_info:                       1
;     print_via_osasci:                         1
;     quote1:                                   1
;     rchex:                                    1
;     rdchv:                                    1
;     read_args_size:                           1
;     read_gbpb_params:                         1
;     read_local_station:                       1
;     read_osargs_params:                       1
;     read_rdln_ctrl_block:                     1
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
;     rest1:                                    1
;     restore_econet_state:                     1
;     restore_x_and_return:                     1
;     restore_y_check_svc:                      1
;     return_bspsx:                             1
;     return_calc_handle:                       1
;     return_compare:                           1
;     return_copy_string:                       1
;     return_dofsl7:                            1
;     return_fscv_handles:                      1
;     return_lodchk:                            1
;     return_match_osbyte:                      1
;     return_remote_cmd:                        1
;     return_tube_xfer:                         1
;     rom_type:                                 1
;     rotate_prot_mask:                         1
;     rsl1:                                     1
;     rssl1:                                    1
;     rssl2:                                    1
;     rx_ctrl_operand:                          1
;     rx_data_phase:                            1
;     rx_error_reset:                           1
;     rx_first_packet:                          1
;     rx_imm_discard:                           1
;     rx_remote_addr:                           1
;     rx_tube_data:                             1
;     rxcb_buf_hi_operand:                      1
;     rxcb_matched:                             1
;     savchk:                                   1
;     save1:                                    1
;     save_args_handle:                         1
;     save_econet_state:                        1
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
;     send_gbpb_params:                         1
;     send_osargs_result:                       1
;     send_osfile_ctrl_blk:                     1
;     send_reply_ok:                            1
;     send_xfer_addr_bytes:                     1
;     service_entry:                            1
;     service_handler:                          1
;     service_handler_entry:                    1
;     set_listen_offset:                        1
;     set_star_reply_port:                      1
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
;     store_fs_hdr_clc:                         1
;     store_fs_hdr_fn:                          1
;     store_handle_return:                      1
;     store_retry_count:                        1
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
;     tube_ctrl_write_2:                        1
;     tube_data_ptr_hi:                         1
;     tube_data_register_1:                     1
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
;     tx_begin:                                 1
;     tx_ctrl_template:                         1
;     tx_data_start:                            1
;     tx_dispatch_page_operand:                 1
;     tx_done_classify:                         1
;     tx_done_error:                            1
;     tx_error:                                 1
;     tx_error_classify:                        1
;     tx_fifo_not_ready:                        1
;     tx_fifo_write:                            1
;     tx_flow_control:                          1
;     tx_imm_op_setup:                          1
;     tx_last_data:                             1
;     tx_line_idle_check:                       1
;     tx_line_jammed:                           1
;     tx_no_clock_error:                        1
;     tx_poll_core:                             1
;     tx_poll_timeout:                          1
;     tx_prepare:                               1
;     tx_result_check:                          1
;     tx_retry:                                 1
;     tx_semaphore_spin:                        1
;     tx_src_net:                               1
;     tx_store_error:                           1
;     tx_success:                               1
;     txcb_dest:                                1
;     txcb_pos:                                 1
;     update_sequence_return:                   1
;     work_ae:                                  1
;     wrch_echo_reply:                          1
;     wrchv:                                    1
;     write_second_tx_byte:                     1
;     y2fsl2:                                   1
;     y2fsl5:                                   1
;     zero_0100_loop:                           1
;     zero_cmd_bytes:                           1
;     zp_work_2:                                1

; Automatically generated labels:
;     c954d
;     l00b6
;     l0100
;     l0101
;     l0102
;     l0103
;     l0104
;     l0106
;     l0130
;     l0350
;     l0351
;     l0355
;     l0700
;     l0cff
;     l0d1e
;     l0d58
;     l0d59
;     l0d60
;     l0dda
;     l0e0c
;     l0e11
;     l0fc5
;     l0fc6
;     l212e
;     l944d

; Stats:
;     Total size (Code + Data) = 8192 bytes
;     Code                     = 7599 bytes (93%)
;     Data                     = 593 bytes (7%)
;
;     Number of instructions   = 3662
;     Number of data bytes     = 352 bytes
;     Number of data words     = 28 bytes
;     Number of string bytes   = 213 bytes
;     Number of strings        = 34
