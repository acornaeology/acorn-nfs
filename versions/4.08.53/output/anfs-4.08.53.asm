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
inkey_key_ctrl                              = 254
osbyte_acknowledge_escape                   = 126
osbyte_close_spool_exec                     = 119
osbyte_explode_chars                        = 20
osbyte_flush_buffer_class                   = 15
osbyte_insert_input_buffer                  = 153
osbyte_issue_service_request                = 143
osbyte_read_buffer                          = 145
osbyte_read_os_version                      = 0
osbyte_read_rom_ptr_table_low               = 168
osbyte_read_write_econet_keyboard_disable   = 201
osbyte_read_write_last_break_type           = 253
osbyte_scan_keyboard                        = 121
osbyte_scan_keyboard_from_16                = 122
osbyte_vsync                                = 19
osbyte_write_keys_pressed                   = 120
osfile_read_catalogue_info                  = 5
osfind_close                                = 0
osfind_open_input                           = 64
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
l0063                                   = &0063
l0078                                   = &0078
l0085                                   = &0085
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
l00ad                                   = &00ad
l00ae                                   = &00ae
l00af                                   = &00af
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
l00cc                                   = &00cc
nfs_temp                                = &00cd
rom_svc_num                             = &00ce
fs_spool0                               = &00cf
l00d0                                   = &00d0
l00da                                   = &00da
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
error_block                             = &0100
error_text                              = &0101
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
l026a                                   = &026a
l028d                                   = &028d
l02a0                                   = &02a0
vdu_screen_mode                         = &0350
l0351                                   = &0351
l0355                                   = &0355
string_buf                              = &0700
l072c                                   = &072c
l072e                                   = &072e
l0a0e                                   = &0a0e
nmi_code_base                           = &0cff
l0d07                                   = &0d07
nmi_jmp_lo                              = &0d0c
nmi_jmp_hi                              = &0d0d
set_nmi_vector                          = &0d0e
install_nmi_handler                     = &0d11
nmi_rti                                 = &0d14
l0d1a                                   = &0d1a
tx_dst_stn                              = &0d20
tx_dst_net                              = &0d21
tx_src_stn                              = &0d22
tx_src_net                              = &0d23
tx_ctrl_byte                            = &0d24
tx_port                                 = &0d25
tx_data_start                           = &0d26
tx_data_len                             = &0d2a
l0d2e                                   = &0d2e
l0d2f                                   = &0d2f
l0d30                                   = &0d30
l0d31                                   = &0d31
rx_src_stn                              = &0d3d
rx_src_net                              = &0d3e
rx_ctrl                                 = &0d3f
rx_port                                 = &0d40
rx_remote_addr                          = &0d41
l0d42                                   = &0d42
l0d43                                   = &0d43
l0d44                                   = &0d44
tx_flags                                = &0d4a
nmi_next_lo                             = &0d4b
nmi_next_hi                             = &0d4c
tx_index                                = &0d4f
tx_length                               = &0d50
ws_0d60                                 = &0d60
l0d61                                   = &0d61
ws_0d62                                 = &0d62
l0d63                                   = &0d63
ws_0d64                                 = &0d64
ws_0d65                                 = &0d65
ws_0d68                                 = &0d68
ws_0d69                                 = &0d69
ws_0d6a                                 = &0d6a
l0d6b                                   = &0d6b
l0d6c                                   = &0d6c
l0d6d                                   = &0d6d
l0d6e                                   = &0d6e
l0d6f                                   = &0d6f
l0d70                                   = &0d70
l0d72                                   = &0d72
l0de6                                   = &0de6
l0df0                                   = &0df0
l0dfa                                   = &0dfa
l0dfe                                   = &0dfe
l0e00                                   = &0e00
l0e01                                   = &0e01
l0e02                                   = &0e02
l0e03                                   = &0e03
l0e04                                   = &0e04
l0e05                                   = &0e05
l0e06                                   = &0e06
l0e07                                   = &0e07
l0e09                                   = &0e09
l0e0a                                   = &0e0a
l0e0b                                   = &0e0b
l0e16                                   = &0e16
l0e2f                                   = &0e2f
l0e30                                   = &0e30
l0e31                                   = &0e31
l0e32                                   = &0e32
l0e38                                   = &0e38
l0ef7                                   = &0ef7
l0f00                                   = &0f00
l0f01                                   = &0f01
l0f02                                   = &0f02
l0f03                                   = &0f03
l0f04                                   = &0f04
l0f05                                   = &0f05
l0f06                                   = &0f06
l0f07                                   = &0f07
l0f08                                   = &0f08
l0f09                                   = &0f09
l0f0a                                   = &0f0a
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
l0f2f                                   = &0f2f
l0f30                                   = &0f30
l0fdc                                   = &0fdc
l0fdd                                   = &0fdd
l0fde                                   = &0fde
l0fdf                                   = &0fdf
l0fe0                                   = &0fe0
l0ff0                                   = &0ff0
l1000                                   = &1000
l1010                                   = &1010
l1020                                   = &1020
l1030                                   = &1030
l1040                                   = &1040
l1050                                   = &1050
l1060                                   = &1060
l1070                                   = &1070
l1071                                   = &1071
l1072                                   = &1072
l1073                                   = &1073
l1074                                   = &1074
l1078                                   = &1078
l1088                                   = &1088
l1098                                   = &1098
l10a8                                   = &10a8
l10b8                                   = &10b8
l10c8                                   = &10c8
l10c9                                   = &10c9
l10ca                                   = &10ca
l10cb                                   = &10cb
l10cc                                   = &10cc
l10cd                                   = &10cd
l10ce                                   = &10ce
l10cf                                   = &10cf
l10d0                                   = &10d0
l10d1                                   = &10d1
l10d4                                   = &10d4
l10d5                                   = &10d5
l10d6                                   = &10d6
l10d7                                   = &10d7
l10d8                                   = &10d8
l10d9                                   = &10d9
l10f3                                   = &10f3
l2322                                   = &2322
l6f6e                                   = &6f6e
l7dfd                                   = &7dfd
sub_cbe5e                               = &be5e
cbe6f                                   = &be6f
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
osrdsc                                  = &ffb9
oseven                                  = &ffbf
gsinit                                  = &ffc2
gsread                                  = &ffc5
osfind                                  = &ffce
osgbpb                                  = &ffd1
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

    org &bebf

.reloc_zp_src

; Move 1: &bebf to &16 for length 65
    org &16
; &bebf referenced 1 time by &beb7
.nmi_workspace_start
    lda #&ff                                                          ; bebf: a9 ff       ..  :0016[1]   ; A=&FF: signal error to co-processor via R4
    jsr tube_send_r4                                                  ; bec1: 20 9e 06     .. :0018[1]   ; Send &FF error signal to Tube R4
    lda tube_data_register_2                                          ; bec4: ad e3 fe    ... :001b[1]   ; Flush any pending R2 byte
    lda #0                                                            ; bec7: a9 00       ..  :001e[1]   ; A=0: send zero prefix to R2
; &bec9 referenced 1 time by &b865
.tube_send_zero_r2
    jsr tube_send_r2                                                  ; bec9: 20 95 06     .. :0020[1]   ; Send zero prefix byte via R2
    tay                                                               ; becc: a8          .   :0023[1]   ; Y=0: start of error block at (&FD)
    lda (brk_ptr),y                                                   ; becd: b1 fd       ..  :0024[1]   ; Load error number from (&FD),0
; &becf referenced 1 time by &a167
.tube_send_error_num
    jsr tube_send_r2                                                  ; becf: 20 95 06     .. :0026[1]   ; Send error number via R2
; &bed2 referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; bed2: c8          .   :0029[1]   ; Advance to next error string byte
; &bed3 referenced 1 time by &053d[3]
.tube_send_error_byte
    lda (brk_ptr),y                                                   ; bed3: b1 fd       ..  :002a[1]   ; Load next error string byte
    jsr tube_send_r2                                                  ; bed5: 20 95 06     .. :002c[1]   ; Send error string byte via R2
    tax                                                               ; bed8: aa          .   :002f[1]   ; Zero byte = end of error string
    bne tube_brk_send_loop                                            ; bed9: d0 f7       ..  :0030[1]   ; Loop until zero terminator sent
; &bedb referenced 1 time by &0477[2]
.tube_reset_stack
    ldx #&ff                                                          ; bedb: a2 ff       ..  :0032[1]   ; Reset stack pointer to top
    txs                                                               ; bedd: 9a          .   :0034[1]   ; TXS: set stack pointer from X
    cli                                                               ; bede: 58          X   :0035[1]   ; Enable interrupts for main loop
; &bedf referenced 6 times by &0044[1], &057f[3], &05a6[3], &0604[4], &0665[4], &0692[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; bedf: 2c e0 fe    ,.. :0036[1]   ; BIT R1 status: check WRCH request
    bpl tube_poll_r2                                                  ; bee2: 10 06       ..  :0039[1]   ; R1 not ready: check R2 instead
; &bee4 referenced 1 time by &0049[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; bee4: ad e1 fe    ... :003b[1]   ; Read character from Tube R1 data
    jsr oswrch                                                        ; bee7: 20 ee ff     .. :003e[1]   ; Write character
; &beea referenced 1 time by &0039[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; beea: 2c e2 fe    ,.. :0041[1]   ; BIT R2 status: check command byte
    bpl tube_main_loop                                                ; beed: 10 f0       ..  :0044[1]   ; R2 not ready: loop back to R1 check
    bit tube_status_1_and_tube_control                                ; beef: 2c e0 fe    ,.. :0046[1]   ; Re-check R1: WRCH has priority over R2
    bmi tube_handle_wrch                                              ; bef2: 30 f0       0.  :0049[1]   ; R1 ready: handle WRCH first
    ldx tube_data_register_2                                          ; bef4: ae e3 fe    ... :004b[1]   ; Read command byte from Tube R2 data
    stx tube_cmd_lo                                                   ; bef7: 86 51       .Q  :004e[1]   ; Self-modify JMP low byte for dispatch
.tube_dispatch_cmd
tube_cmd_lo = tube_dispatch_cmd+1
    jmp (tube_r2_dispatch_table)                                      ; bef9: 6c 00 05    l.. :0050[1]   ; Dispatch to handler via indirect JMP

; &befa referenced 1 time by &004e[1]
; &befc referenced 2 times by &04de[2], &04ee[2]
.tube_transfer_addr
    equb 0                                                            ; befc: 00          .   :0053[1]   ; Tube transfer address low byte
; &befd referenced 3 times by &04b6[2], &04d4[2], &04f3[2]
.tube_xfer_page
    equb &80                                                          ; befd: 80          .   :0054[1]   ; Tube transfer page (default &80)
; &befe referenced 2 times by &04ba[2], &04fd[2]
.tube_xfer_addr_2
    equb 0                                                            ; befe: 00          .   :0055[1]   ; Tube transfer address byte 2
; &beff referenced 2 times by &04be[2], &04fb[2]
.tube_xfer_addr_3
    equb 0                                                            ; beff: 00          .   :0056[1]   ; Tube transfer address byte 3

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

; Move 2: &bf00 to &0400 for length 256
    org &0400
; &bf00 referenced 1 time by &be9d
.tube_page4_vectors
    jmp tube_begin                                                    ; bf00: 4c 84 04    L.. :0400[2]   ; JMP to BEGIN startup entry; Tube host startup. Claim address &FF,
; relocate ROM code, and enter the main
; command polling loop.

    jmp tube_escape_check                                             ; bf03: 4c a7 06    L.. :0403[2]   ; JMP to tube_escape_check (&06A7)

; &bf06 referenced 10 times by &049a[2], &04cf[2], &8371, &8445, &8929, &8931, &9fda, &9ff1, &a05d, &a2d4
.tube_addr_data_dispatch
    cmp #&80                                                          ; bf06: c9 80       ..  :0406[2]   ; A>=&80: address claim; A<&80: data transfer
    bcc tube_transfer_setup                                           ; bf08: 90 2b       .+  :0408[2]   ; A<&80: data transfer setup (SENDW)
    cmp #&c0                                                          ; bf0a: c9 c0       ..  :040a[2]   ; A>=&C0: new address claim from another host
    bcs addr_claim_external                                           ; bf0c: b0 1a       ..  :040c[2]   ; C=1: external claim, check ownership
    ora #&40 ; '@'                                                    ; bf0e: 09 40       .@  :040e[2]   ; Map &80-&BF range to &C0-&FF for comparison
    cmp tube_claimed_id                                               ; bf10: c5 15       ..  :0410[2]   ; Is this for our currently-claimed address?
    bne return_tube_init                                              ; bf12: d0 20       .   :0412[2]   ; Match: we own it, return (no release)
; ***************************************************************************************
; Release or claim Tube processor.
; A>=&C0: external claim from another host.
; A>=&80: release our current claim.
; A<&80: set up data transfer.
; ***************************************************************************************
; &bf14 referenced 1 time by &0471[2]
.tube_release_claim
    php                                                               ; bf14: 08          .   :0414[2]   ; PHP: save interrupt state for release
    sei                                                               ; bf15: 78          x   :0415[2]   ; SEI: disable interrupts during R4 protocol
    lda #5                                                            ; bf16: a9 05       ..  :0416[2]   ; R4 cmd 5: release our address claim
    jsr tube_send_r4                                                  ; bf18: 20 9e 06     .. :0418[2]   ; Send release command to co-processor
    lda tube_claimed_id                                               ; bf1b: a5 15       ..  :041b[2]   ; Load our currently-claimed address
    jsr tube_send_r4                                                  ; bf1d: 20 9e 06     .. :041d[2]   ; Send our address as release parameter
    plp                                                               ; bf20: 28          (   :0420[2]   ; Restore interrupt state
; &bf21 referenced 1 time by &beaf
.clear_tube_claim
    lda #&80                                                          ; bf21: a9 80       ..  :0421[2]   ; &80 sentinel: clear address claim
    sta tube_claimed_id                                               ; bf23: 85 15       ..  :0423[2]   ; &80 sentinel = no address currently claimed
    sta tube_claim_flag                                               ; bf25: 85 14       ..  :0425[2]   ; Store to claim-in-progress flag
    rts                                                               ; bf27: 60          `   :0427[2]   ; Return from tube_post_init

; &bf28 referenced 1 time by &040c[2]
.addr_claim_external
    asl tube_claim_flag                                               ; bf28: 06 14       ..  :0428[2]   ; Another host claiming; check if we're owner
    bcs accept_new_claim                                              ; bf2a: b0 06       ..  :042a[2]   ; C=1: we have an active claim
    cmp tube_claimed_id                                               ; bf2c: c5 15       ..  :042c[2]   ; Compare with our claimed address
    beq return_tube_init                                              ; bf2e: f0 04       ..  :042e[2]   ; Match: return (we already have it)
    clc                                                               ; bf30: 18          .   :0430[2]   ; Not ours: CLC = we don't own this address
    rts                                                               ; bf31: 60          `   :0431[2]   ; Return with C=0 (claim denied)

; &bf32 referenced 1 time by &042a[2]
.accept_new_claim
    sta tube_claimed_id                                               ; bf32: 85 15       ..  :0432[2]   ; Accept new claim: update our address
; &bf34 referenced 2 times by &0412[2], &042e[2]
.return_tube_init
    rts                                                               ; bf34: 60          `   :0434[2]   ; Return with address updated

; &bf35 referenced 1 time by &0408[2]
.tube_transfer_setup
    php                                                               ; bf35: 08          .   :0435[2]   ; PHP: save interrupt state
    sei                                                               ; bf36: 78          x   :0436[2]   ; SEI: disable interrupts for R4 protocol
.setup_data_transfer
    sty tube_data_ptr_hi                                              ; bf37: 84 13       ..  :0437[2]   ; Save 16-bit transfer address from (X,Y)
    stx tube_data_ptr                                                 ; bf39: 86 12       ..  :0439[2]   ; Store address pointer low byte
    jsr tube_send_r4                                                  ; bf3b: 20 9e 06     .. :043b[2]   ; Send transfer type byte to co-processor
    tax                                                               ; bf3e: aa          .   :043e[2]   ; X = transfer type for table lookup
    ldy #3                                                            ; bf3f: a0 03       ..  :043f[2]   ; Y=3: send 4 bytes (address + claimed addr)
    lda tube_claimed_id                                               ; bf41: a5 15       ..  :0441[2]   ; Send our claimed address + 4-byte xfer addr
    jsr tube_send_r4                                                  ; bf43: 20 9e 06     .. :0443[2]   ; Send transfer address byte
; &bf46 referenced 1 time by &044c[2]
.send_xfer_addr_bytes
    lda (tube_data_ptr),y                                             ; bf46: b1 12       ..  :0446[2]   ; Load transfer address byte from (X,Y)
    jsr tube_send_r4                                                  ; bf48: 20 9e 06     .. :0448[2]   ; Send address byte to co-processor via R4
    dey                                                               ; bf4b: 88          .   :044b[2]   ; Previous byte (big-endian: 3,2,1,0)
    bpl send_xfer_addr_bytes                                          ; bf4c: 10 f8       ..  :044c[2]   ; Loop for all 4 address bytes
    ldy #&18                                                          ; bf4e: a0 18       ..  :044e[2]   ; Y=&18: enable Tube control register
    sty tube_status_1_and_tube_control                                ; bf50: 8c e0 fe    ... :0450[2]   ; Enable Tube interrupt generation
    lda tube_ctrl_values,x                                            ; bf53: bd 18 05    ... :0453[2]   ; Look up Tube control bits for this xfer type
    sta tube_status_1_and_tube_control                                ; bf56: 8d e0 fe    ... :0456[2]   ; Apply transfer-specific control bits
    lsr a                                                             ; bf59: 4a          J   :0459[2]   ; LSR: check bit 2 (2-byte flush needed?)
    lsr a                                                             ; bf5a: 4a          J   :045a[2]   ; LSR: shift bit 2 to carry
    bcc skip_r3_flush                                                 ; bf5b: 90 06       ..  :045b[2]   ; C=0: no flush needed, skip R3 reads
    bit tube_data_register_3                                          ; bf5d: 2c e5 fe    ,.. :045d[2]   ; Dummy R3 reads: flush for 2-byte transfers
    bit tube_data_register_3                                          ; bf60: 2c e5 fe    ,.. :0460[2]   ; Second dummy read to flush R3 FIFO
; &bf63 referenced 1 time by &045b[2]
.skip_r3_flush
    jsr tube_send_r4                                                  ; bf63: 20 9e 06     .. :0463[2]   ; Trigger co-processor ack via R4
; &bf66 referenced 1 time by &0469[2]
.poll_r4_copro_ack
    bit tube_status_register_4_and_cpu_control                        ; bf66: 2c e6 fe    ,.. :0466[2]   ; Poll R4 status for co-processor response
    bvc poll_r4_copro_ack                                             ; bf69: 50 fb       P.  :0469[2]   ; Bit 6 clear: not ready, keep polling
    bcs copro_ack_nmi_check                                           ; bf6b: b0 0d       ..  :046b[2]   ; R4 bit 7: co-processor acknowledged transfer
    cpx #4                                                            ; bf6d: e0 04       ..  :046d[2]   ; Type 4 = SENDW (host-to-parasite word xfer)
    bne skip_nmi_release                                              ; bf6f: d0 11       ..  :046f[2]   ; Not SENDW type: skip release path
; &bf71 referenced 1 time by &0496[2]
.tube_sendw_complete
    jsr tube_release_claim                                            ; bf71: 20 14 04     .. :0471[2]   ; SENDW complete: release, sync, restart; Release or claim Tube processor.
; A>=&C0: external claim from another host.
; A>=&80: release our current claim.
; A<&80: set up data transfer.
    jsr tube_send_r2                                                  ; bf74: 20 95 06     .. :0474[2]   ; Sync via R2 send
    jmp tube_reset_stack                                              ; bf77: 4c 32 00    L2. :0477[2]   ; Restart Tube main loop

; &bf7a referenced 1 time by &046b[2]
.copro_ack_nmi_check
    lsr a                                                             ; bf7a: 4a          J   :047a[2]   ; LSR: check bit 0 (NMI used?)
    bcc skip_nmi_release                                              ; bf7b: 90 05       ..  :047b[2]   ; C=0: NMI not used, skip NMI release
    ldy #&88                                                          ; bf7d: a0 88       ..  :047d[2]   ; Release Tube NMI (transfer used interrupts)
    sty tube_status_1_and_tube_control                                ; bf7f: 8c e0 fe    ... :047f[2]   ; Write &88 to Tube control to release NMI
; &bf82 referenced 2 times by &046f[2], &047b[2]
.skip_nmi_release
    plp                                                               ; bf82: 28          (   :0482[2]   ; Restore interrupt state
.return_tube_xfer
    rts                                                               ; bf83: 60          `   :0483[2]   ; Return from transfer setup

; ***************************************************************************************
; Tube host startup. Claim address &FF,
; relocate ROM code, and enter the main
; command polling loop.
; ***************************************************************************************
; &bf84 referenced 1 time by &0400[2]
.tube_begin
    cli                                                               ; bf84: 58          X   :0484[2]   ; BEGIN: enable interrupts for Tube host code
    bcs claim_addr_ff                                                 ; bf85: b0 11       ..  :0485[2]   ; C=1: hard break, claim addr &FF
    bne check_break_type                                              ; bf87: d0 03       ..  :0487[2]   ; C=0, A!=0: re-init path
    jmp tube_reply_ack                                                ; bf89: 4c 9c 05    L.. :0489[2]   ; Z=1 from C=0 path: just acknowledge

; &bf8c referenced 1 time by &0487[2]
.check_break_type
    ldx #0                                                            ; bf8c: a2 00       ..  :048c[2]   ; X=0 for OSBYTE
    ldy #&ff                                                          ; bf8e: a0 ff       ..  :048e[2]   ; Y=&FF for OSBYTE
    lda #osbyte_read_write_last_break_type                            ; bf90: a9 fd       ..  :0490[2]   ; OSBYTE &FD: what type of reset was this?
    jsr osbyte                                                        ; bf92: 20 f4 ff     .. :0492[2]   ; Read type of last reset
    txa                                                               ; bf95: 8a          .   :0495[2]   ; X=value of type of last reset
    beq tube_sendw_complete                                           ; bf96: f0 d9       ..  :0496[2]   ; Soft break (X=0): re-init Tube and restart
; &bf98 referenced 2 times by &0485[2], &049d[2]
.claim_addr_ff
    lda #&ff                                                          ; bf98: a9 ff       ..  :0498[2]   ; Claim address &FF (startup = highest prio)
    jsr tube_addr_data_dispatch                                       ; bf9a: 20 06 04     .. :049a[2]   ; Request address claim from Tube system
    bcc claim_addr_ff                                                 ; bf9d: 90 f9       ..  :049d[2]   ; C=0: claim failed, retry
    jsr tube_init_reloc                                               ; bf9f: 20 d2 04     .. :049f[2]   ; Init reloc pointers from ROM header; Relocate Tube host code from ROM to RAM
; and initialise transfer address defaults.
; &bfa2 referenced 1 time by &04c4[2]
.next_rom_page
    lda #7                                                            ; bfa2: a9 07       ..  :04a2[2]   ; R4 cmd 7: SENDW to send ROM to parasite
    jsr tube_claim_default                                            ; bfa4: 20 cb 04     .. :04a4[2]   ; Set up Tube for SENDW transfer; Claim Tube for this ROM's default address.
    ldy #0                                                            ; bfa7: a0 00       ..  :04a7[2]   ; Y=0: start at beginning of page
    sty zp_ptr_lo                                                     ; bfa9: 84 00       ..  :04a9[2]   ; Store to zero page pointer low byte
; &bfab referenced 1 time by &04b4[2]
.send_rom_page_bytes
    lda (zp_ptr_lo),y                                                 ; bfab: b1 00       ..  :04ab[2]   ; Send 256-byte page via R3, byte at a time
    sta tube_data_register_3                                          ; bfad: 8d e5 fe    ... :04ad[2]   ; Write byte to Tube R3 data register
    nop                                                               ; bfb0: ea          .   :04b0[2]   ; Timing delay: Tube data register needs NOPs
    nop                                                               ; bfb1: ea          .   :04b1[2]   ; NOP delay (2)
    nop                                                               ; bfb2: ea          .   :04b2[2]   ; NOP delay (3)
    iny                                                               ; bfb3: c8          .   :04b3[2]   ; Next byte in page
    bne send_rom_page_bytes                                           ; bfb4: d0 f5       ..  :04b4[2]   ; Loop for all 256 bytes
    inc tube_xfer_page                                                ; bfb6: e6 54       .T  :04b6[2]   ; Increment 24-bit destination addr
    bne skip_addr_carry                                               ; bfb8: d0 06       ..  :04b8[2]   ; No carry: skip higher bytes
    inc tube_xfer_addr_2                                              ; bfba: e6 55       .U  :04ba[2]   ; Carry into second byte
    bne skip_addr_carry                                               ; bfbc: d0 02       ..  :04bc[2]   ; No carry: skip third byte
    inc tube_xfer_addr_3                                              ; bfbe: e6 56       .V  :04be[2]   ; Carry into third byte
; &bfc0 referenced 2 times by &04b8[2], &04bc[2]
.skip_addr_carry
    inc zp_ptr_hi                                                     ; bfc0: e6 01       ..  :04c0[2]   ; Increment page counter
    bit zp_ptr_hi                                                     ; bfc2: 24 01       $.  :04c2[2]   ; Bit 6 set = all pages transferred
    bvc next_rom_page                                                 ; bfc4: 50 dc       P.  :04c4[2]   ; More pages: loop back to SENDW
    jsr tube_init_reloc                                               ; bfc6: 20 d2 04     .. :04c6[2]   ; Re-init reloc pointers for final claim; Relocate Tube host code from ROM to RAM
; and initialise transfer address defaults.
    lda #4                                                            ; bfc9: a9 04       ..  :04c9[2]   ; A=4: transfer type for final address claim
; ***************************************************************************************
; Claim Tube for this ROM's default address.
; ***************************************************************************************
; &bfcb referenced 1 time by &04a4[2]
.tube_claim_default
    ldy #0                                                            ; bfcb: a0 00       ..  :04cb[2]   ; Y=0: transfer address low byte
    ldx #&53 ; 'S'                                                    ; bfcd: a2 53       .S  :04cd[2]   ; X=&53: transfer address high byte (&0053)
    jmp tube_addr_data_dispatch                                       ; bfcf: 4c 06 04    L.. :04cf[2]   ; Claim Tube address for transfer

; ***************************************************************************************
; Relocate Tube host code from ROM to RAM
; and initialise transfer address defaults.
; ***************************************************************************************
; &bfd2 referenced 2 times by &049f[2], &04c6[2]
.tube_init_reloc
    lda #&80                                                          ; bfd2: a9 80       ..  :04d2[2]   ; Init: start sending from &8000
    sta tube_xfer_page                                                ; bfd4: 85 54       .T  :04d4[2]   ; Store &80 as source page high byte
    sta zp_ptr_hi                                                     ; bfd6: 85 01       ..  :04d6[2]   ; Store &80 as page counter initial value
    lda #&20 ; ' '                                                    ; bfd8: a9 20       .   :04d8[2]   ; A=&20: bit 5 mask for ROM type check
    and rom_type                                                      ; bfda: 2d 06 80    -.. :04da[2]   ; ROM type bit 5: reloc address in header?
    tay                                                               ; bfdd: a8          .   :04dd[2]   ; Y = 0 or &20 (reloc flag)
    sty tube_transfer_addr                                            ; bfde: 84 53       .S  :04de[2]   ; Store as transfer address selector
    beq store_xfer_end_addr                                           ; bfe0: f0 19       ..  :04e0[2]   ; No reloc addr: use defaults
    ldx copyright_offset                                              ; bfe2: ae 07 80    ... :04e2[2]   ; Skip past copyright string to find reloc addr
; &bfe5 referenced 1 time by &04e9[2]
.scan_copyright_end
    inx                                                               ; bfe5: e8          .   :04e5[2]   ; Skip past null-terminated copyright string
    lda rom_header,x                                                  ; bfe6: bd 00 80    ... :04e6[2]   ; Load next byte from ROM header
    bne scan_copyright_end                                            ; bfe9: d0 fa       ..  :04e9[2]   ; Loop until null terminator found
    lda rom_header_byte1,x                                            ; bfeb: bd 01 80    ... :04eb[2]   ; Read 4-byte reloc address from ROM header
    sta tube_transfer_addr                                            ; bfee: 85 53       .S  :04ee[2]   ; Store reloc addr byte 1 as transfer addr
    lda rom_header_byte2,x                                            ; bff0: bd 02 80    ... :04f0[2]   ; Load reloc addr byte 2
    sta tube_xfer_page                                                ; bff3: 85 54       .T  :04f3[2]   ; Store as source page start
    ldy service_entry,x                                               ; bff5: bc 03 80    ... :04f5[2]   ; Load reloc addr byte 3
    lda service_handler_lo,x                                          ; bff8: bd 04 80    ... :04f8[2]   ; Load reloc addr byte 4 (highest)
; &bffb referenced 1 time by &04e0[2]
.store_xfer_end_addr
    sta tube_xfer_addr_3                                              ; bffb: 85 56       .V  :04fb[2]   ; Store high byte of end address
    sty tube_xfer_addr_2                                              ; bffd: 84 55       .U  :04fd[2]   ; Store byte 3 of end address
    rts                                                               ; bfff: 60          `   :04ff[2]   ; Return with pointers initialised


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_page4_vectors, *, reloc_p4_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_page4_vectors, &0500

    ; Set the program counter to the next position in the binary file.
    org reloc_p4_src + (* - tube_page4_vectors)

.pydis_end

    org &bc90

.reloc_p5_src

; Move 3: &bc90 to &0500 for length 256
    org &0500
; &bc90 referenced 2 times by &0050[1], &bea3
.tube_r2_dispatch_table
    equb &37, 5, &96, 5, &f2, 5,   7, 6, &27, 6, &68, 6, &5e, 5       ; bc90: 37 05 96... 7.. :0500[3]   ; 12-entry Tube R2 command dispatch table
    equb &2d, 5, &20, 5, &42, 5, &a9, 5, &d1, 5                       ; bc9e: 2d 05 20... -.  :050e[3]
; &bca8 referenced 1 time by &0453[2]
.tube_ctrl_values
    equb &86, &88, &96, &98, &18, &18, &82, &18                       ; bca8: 86 88 96... ... :0518[3]   ; Tube control register value table (8 bytes)
.tube_osbput
    equb &20, &c5, 6, &a8, &20, &c5, 6                                ; bcb0: 20 c5 06...  .. :0520[3]   ; Read channel handle from R2 for BPUT
.tube_poll_r1_wrch
    equb &20, &d4, &ff, &4c, &9c, 5                                   ; bcb7: 20 d4 ff...  .. :0527[3]
.tube_osbget
    equb &20, &c5, 6, &a8, &20, &d7, &ff, &4c, &3a, 5                 ; bcbd: 20 c5 06...  .. :052d[3]   ; Read channel handle from R2 for BGET
.tube_osrdch
    equb &20, &e0, &ff                                                ; bcc7: 20 e0 ff     .. :0537[3]

; &bcca referenced 1 time by &05ef[3]
.tube_rdch_reply
    ror a                                                             ; bcca: 6a          j   :053a[3]   ; ROR A: encode carry (error flag) into bit 7
    equb &20, &95                                                     ; bccb: 20 95        .  :053b[3]

.tube_release_return
    asl tube_send_error_byte                                          ; bccd: 06 2a       .*  :053d[3]   ; ASL: shift carry out of &002A (dead code)
    jmp tube_reply_byte                                               ; bccf: 4c 9e 05    L.. :053f[3]   ; JMP tube_reply_byte (dead code path)

.tube_osfind
    jsr tube_read_r2                                                  ; bcd2: 20 c5 06     .. :0542[3]   ; Read open mode from R2 for OSFIND; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    beq tube_osfind_close                                             ; bcd5: f0 0b       ..  :0545[3]
    pha                                                               ; bcd7: 48          H   :0547[3]
    jsr tube_read_string                                              ; bcd8: 20 82 05     .. :0548[3]
    pla                                                               ; bcdb: 68          h   :054b[3]
    jsr osfind                                                        ; bcdc: 20 ce ff     .. :054c[3]   ; Open or close file(s)
    jmp tube_reply_byte                                               ; bcdf: 4c 9e 05    L.. :054f[3]

; &bce2 referenced 1 time by &0545[3]
.tube_osfind_close
    jsr tube_read_r2                                                  ; bce2: 20 c5 06     .. :0552[3]   ; OSFIND close: read handle from R2; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    tay                                                               ; bce5: a8          .   :0555[3]
    lda #osfind_close                                                 ; bce6: a9 00       ..  :0556[3]
    jsr osfind                                                        ; bce8: 20 ce ff     .. :0558[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; bceb: 4c 9c 05    L.. :055b[3]

.tube_osargs
    equb &20, &c5, 6, &a8                                             ; bcee: 20 c5 06...  .. :055e[3]   ; Read file handle from R2 for OSARGS
.tube_read_params
    equb &a2, 4                                                       ; bcf2: a2 04       ..  :0562[3]   ; Read 4-byte arg + reason from R2 into ZP

; &bcf4 referenced 1 time by &056a[3]
.read_osargs_params
    jsr tube_read_r2                                                  ; bcf4: 20 c5 06     .. :0564[3]   ; Read next param byte from R2; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    sta escape_flag,x                                                 ; bcf7: 95 ff       ..  :0567[3]
    dex                                                               ; bcf9: ca          .   :0569[3]
    bne read_osargs_params                                            ; bcfa: d0 f8       ..  :056a[3]
    jsr tube_read_r2                                                  ; bcfc: 20 c5 06     .. :056c[3]   ; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    jsr osargs                                                        ; bcff: 20 da ff     .. :056f[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; bd02: 20 95 06     .. :0572[3]
    ldx #3                                                            ; bd05: a2 03       ..  :0575[3]
; &bd07 referenced 1 time by &057d[3]
.send_osargs_result
    lda zp_ptr_lo,x                                                   ; bd07: b5 00       ..  :0577[3]   ; Load result byte from zero page
    jsr tube_send_r2                                                  ; bd09: 20 95 06     .. :0579[3]
    dex                                                               ; bd0c: ca          .   :057c[3]
    bpl send_osargs_result                                            ; bd0d: 10 f8       ..  :057d[3]
    jmp tube_main_loop                                                ; bd0f: 4c 36 00    L6. :057f[3]

; &bd12 referenced 2 times by &0548[3], &05b3[3]
.tube_read_string
    ldx #0                                                            ; bd12: a2 00       ..  :0582[3]   ; X=0: initialise string buffer index
    ldy #0                                                            ; bd14: a0 00       ..  :0584[3]
; &bd16 referenced 1 time by &0591[3]
.strnh
    jsr tube_read_r2                                                  ; bd16: 20 c5 06     .. :0586[3]   ; Read next string byte from R2; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    sta string_buf,y                                                  ; bd19: 99 00 07    ... :0589[3]
    iny                                                               ; bd1c: c8          .   :058c[3]
    beq string_buf_done                                               ; bd1d: f0 04       ..  :058d[3]
    cmp #&0d                                                          ; bd1f: c9 0d       ..  :058f[3]
    bne strnh                                                         ; bd21: d0 f3       ..  :0591[3]
; &bd23 referenced 1 time by &058d[3]
.string_buf_done
    ldy #7                                                            ; bd23: a0 07       ..  :0593[3]   ; Y=7: set XY=&0700 for OSCLI/OSFIND
    rts                                                               ; bd25: 60          `   :0595[3]

.tube_oscli
    equb &20, &82, 5, &20, &f7, &ff                                   ; bd26: 20 82 05...  .. :0596[3]   ; Read command string from R2 into &0700

; &bd2c referenced 2 times by &0489[2], &055b[3]
.tube_reply_ack
    lda #&7f                                                          ; bd2c: a9 7f       ..  :059c[3]   ; &7F = success acknowledgement
; &bd2e referenced 4 times by &053f[3], &054f[3], &05a1[3], &067d[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; bd2e: 2c e2 fe    ,.. :059e[3]   ; Poll R2 status until ready
    bvc tube_reply_byte                                               ; bd31: 50 fb       P.  :05a1[3]   ; Bit 6 clear: not ready, loop
    sta tube_data_register_2                                          ; bd33: 8d e3 fe    ... :05a3[3]   ; Write byte to R2 data register
; &bd36 referenced 1 time by &05cf[3]
.mj
    jmp tube_main_loop                                                ; bd36: 4c 36 00    L6. :05a6[3]   ; Return to Tube main loop

.tube_osfile
    equb &a2, &10                                                     ; bd39: a2 10       ..  :05a9[3]   ; Read 16-byte OSFILE control block from R2

; &bd3b referenced 1 time by &05b1[3]
.argsw
    jsr tube_read_r2                                                  ; bd3b: 20 c5 06     .. :05ab[3]   ; Read next control block byte from R2; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    sta zp_ptr_hi,x                                                   ; bd3e: 95 01       ..  :05ae[3]
    dex                                                               ; bd40: ca          .   :05b0[3]
    bne argsw                                                         ; bd41: d0 f8       ..  :05b1[3]
    jsr tube_read_string                                              ; bd43: 20 82 05     .. :05b3[3]
    stx zp_ptr_lo                                                     ; bd46: 86 00       ..  :05b6[3]
    sty zp_ptr_hi                                                     ; bd48: 84 01       ..  :05b8[3]
    ldy #0                                                            ; bd4a: a0 00       ..  :05ba[3]
    jsr tube_read_r2                                                  ; bd4c: 20 c5 06     .. :05bc[3]   ; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    jsr osfile                                                        ; bd4f: 20 dd ff     .. :05bf[3]
    jsr tube_send_r2                                                  ; bd52: 20 95 06     .. :05c2[3]
    ldx #&10                                                          ; bd55: a2 10       ..  :05c5[3]
; &bd57 referenced 1 time by &05cd[3]
.send_osfile_ctrl_blk
    lda zp_ptr_hi,x                                                   ; bd57: b5 01       ..  :05c7[3]   ; Load control block byte
    jsr tube_send_r2                                                  ; bd59: 20 95 06     .. :05c9[3]
    dex                                                               ; bd5c: ca          .   :05cc[3]
    bne send_osfile_ctrl_blk                                          ; bd5d: d0 f8       ..  :05cd[3]
    beq mj                                                            ; bd5f: f0 d5       ..  :05cf[3]   ; ALWAYS branch

    ldx #&0d                                                          ; bd61: a2 0d       ..  :05d1[3]
; &bd63 referenced 1 time by &05d9[3]
.read_osgbpb_ctrl_blk
    jsr tube_read_r2                                                  ; bd63: 20 c5 06     .. :05d3[3]   ; Read next control block byte from R2; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    sta escape_flag,x                                                 ; bd66: 95 ff       ..  :05d6[3]
    dex                                                               ; bd68: ca          .   :05d8[3]
    bne read_osgbpb_ctrl_blk                                          ; bd69: d0 f8       ..  :05d9[3]
    jsr tube_read_r2                                                  ; bd6b: 20 c5 06     .. :05db[3]   ; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    ldy #0                                                            ; bd6e: a0 00       ..  :05de[3]
    jsr osgbpb                                                        ; bd70: 20 d1 ff     .. :05e0[3]   ; Read or write multiple bytes to an open file
    pha                                                               ; bd73: 48          H   :05e3[3]
    ldx #&0c                                                          ; bd74: a2 0c       ..  :05e4[3]
; &bd76 referenced 1 time by &05ec[3]
.send_osgbpb_result
    lda zp_ptr_lo,x                                                   ; bd76: b5 00       ..  :05e6[3]   ; Load result byte from zero page
    jsr tube_send_r2                                                  ; bd78: 20 95 06     .. :05e8[3]
    dex                                                               ; bd7b: ca          .   :05eb[3]
    bpl send_osgbpb_result                                            ; bd7c: 10 f8       ..  :05ec[3]
    pla                                                               ; bd7e: 68          h   :05ee[3]   ; Recover completion status from stack
    jmp tube_rdch_reply                                               ; bd7f: 4c 3a 05    L:. :05ef[3]

    equb &20, &c5, 6, &aa, &20, &c5, 6, &20, &f4, &ff                 ; bd82: 20 c5 06...  .. :05f2[3]

; &bd8c referenced 2 times by &05ff[3], &0625[4]
.tube_poll_r2_result
    bit tube_status_register_2                                        ; bd8c: 2c e2 fe    ,.. :05fc[3]   ; Poll R2 status for result send
    equb &50                                                          ; bd8f: 50          P   :05ff[3]   ; BVC: page 5/6 boundary straddle

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_r2_dispatch_table, *, reloc_p5_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_r2_dispatch_table, &0600

    ; Set the program counter to the next position in the binary file.
    org reloc_p5_src + (* - tube_r2_dispatch_table)

.reloc_p6_src

; Move 4: &bd90 to &0600 for length 256
    org &0600
; &bd90 referenced 1 time by &bea9
.tube_osbyte_reply_block
    equb &fb                                                          ; bd90: fb          .   :0600[4]   ; Send carry+status to co-processor via R2

    stx tube_data_register_2                                          ; bd91: 8e e3 fe    ... :0601[4]   ; Send X result for 2-param OSBYTE
; &bd94 referenced 1 time by &0617[4]
.bytex
    jmp tube_main_loop                                                ; bd94: 4c 36 00    L6. :0604[4]   ; Return to main event loop

.tube_osbyte_long
    jsr tube_read_r2                                                  ; bd97: 20 c5 06     .. :0607[4]   ; Read X, Y, A from R2 for 3-param OSBYTE; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    tax                                                               ; bd9a: aa          .   :060a[4]   ; Save in X
    jsr tube_read_r2                                                  ; bd9b: 20 c5 06     .. :060b[4]   ; Read Y parameter from co-processor; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    tay                                                               ; bd9e: a8          .   :060e[4]   ; Save in Y
    jsr tube_read_r2                                                  ; bd9f: 20 c5 06     .. :060f[4]   ; Read A (OSBYTE function code); Poll Tube R2 status until data is ready,
; then read and return the data byte.
    jsr osbyte                                                        ; bda2: 20 f4 ff     .. :0612[4]   ; Execute OSBYTE A,X,Y
    eor #&9d                                                          ; bda5: 49 9d       I.  :0615[4]   ; Send carry result to co-processor
    beq bytex                                                         ; bda7: f0 eb       ..  :0617[4]   ; OSBYTE &9D (fast Tube BPUT): no result needed
    ror a                                                             ; bda9: 6a          j   :0619[4]   ; Encode carry (error flag) into bit 7
    jsr tube_send_r2                                                  ; bdaa: 20 95 06     .. :061a[4]   ; Send carry+status byte via R2
; &bdad referenced 1 time by &0620[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; bdad: 2c e2 fe    ,.. :061d[4]   ; Poll R2 status for ready
    bvc tube_osbyte_send_y                                            ; bdb0: 50 fb       P.  :0620[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; bdb2: 8c e3 fe    ... :0622[4]   ; Send Y result, then fall through to send X
.tube_osbyte_short
    bvs tube_poll_r2_result                                           ; bdb5: 70 d5       p.  :0625[4]
.tube_osword
    jsr tube_read_r2                                                  ; bdb7: 20 c5 06     .. :0627[4]   ; Overlapping entry: &20 = JSR c06c5 (OSWORD); Poll Tube R2 status until data is ready,
; then read and return the data byte.
    tay                                                               ; bdba: a8          .   :062a[4]   ; Save OSWORD number in Y
; &bdbb referenced 1 time by &062e[4]
.tube_osword_read
    bit tube_status_register_2                                        ; bdbb: 2c e2 fe    ,.. :062b[4]   ; Poll R2 status for data ready
    bpl tube_osword_read                                              ; bdbe: 10 fb       ..  :062e[4]   ; Not ready: keep polling
.tube_osbyte_send_x
    ldx tube_data_register_2                                          ; bdc0: ae e3 fe    ... :0630[4]   ; Read param block length from R2
    dex                                                               ; bdc3: ca          .   :0633[4]   ; DEX: length 0 means no params to read
    bmi skip_param_read                                               ; bdc4: 30 0f       0.  :0634[4]   ; No params (length=0): skip read loop
; &bdc6 referenced 2 times by &0639[4], &0642[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; bdc6: 2c e2 fe    ,.. :0636[4]   ; Poll R2 status for data ready
    bpl tube_osword_read_lp                                           ; bdc9: 10 fb       ..  :0639[4]   ; Not ready: keep polling
    lda tube_data_register_2                                          ; bdcb: ad e3 fe    ... :063b[4]   ; Read param byte from R2
    sta l0128,x                                                       ; bdce: 9d 28 01    .(. :063e[4]   ; Store param bytes into block at &0128
    dex                                                               ; bdd1: ca          .   :0641[4]   ; Next param byte (descending)
    bpl tube_osword_read_lp                                           ; bdd2: 10 f2       ..  :0642[4]   ; Loop until all params read
    tya                                                               ; bdd4: 98          .   :0644[4]   ; Restore OSWORD number from Y
; &bdd5 referenced 1 time by &0634[4]
.skip_param_read
    ldx #<(l0128)                                                     ; bdd5: a2 28       .(  :0645[4]   ; XY=&0128: param block address for OSWORD
    ldy #>(l0128)                                                     ; bdd7: a0 01       ..  :0647[4]   ; Y=&01: param block at &0128
    jsr osword                                                        ; bdd9: 20 f1 ff     .. :0649[4]   ; Send result marker via R2
; &bddc referenced 1 time by &064f[4]
.poll_r2_osword_result
    bit tube_status_register_2                                        ; bddc: 2c e2 fe    ,.. :064c[4]   ; Poll R2 status for ready
    bpl poll_r2_osword_result                                         ; bddf: 10 fb       ..  :064f[4]   ; Not ready: keep polling
    ldx tube_data_register_2                                          ; bde1: ae e3 fe    ... :0651[4]   ; Read result block length from R2
    dex                                                               ; bde4: ca          .   :0654[4]   ; Decrement result byte counter
    bmi tube_return_main                                              ; bde5: 30 0e       0.  :0655[4]   ; No results to send: return to main loop
; &bde7 referenced 1 time by &0663[4]
.tube_osword_write
    ldy l0128,x                                                       ; bde7: bc 28 01    .(. :0657[4]   ; Send result block bytes from &0128 via R2
; &bdea referenced 1 time by &065d[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; bdea: 2c e2 fe    ,.. :065a[4]   ; Poll R2 status for ready
    bvc tube_osword_write_lp                                          ; bded: 50 fb       P.  :065d[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; bdef: 8c e3 fe    ... :065f[4]   ; Send result byte via R2
    dex                                                               ; bdf2: ca          .   :0662[4]   ; Next result byte (descending)
    bpl tube_osword_write                                             ; bdf3: 10 f2       ..  :0663[4]   ; Loop until all results sent
; &bdf5 referenced 1 time by &0655[4]
.tube_return_main
    jmp tube_main_loop                                                ; bdf5: 4c 36 00    L6. :0665[4]   ; Return to main event loop

.tube_osword_rdln
    ldx #4                                                            ; bdf8: a2 04       ..  :0668[4]   ; Read 5-byte OSWORD 0 control block from R2
; &bdfa referenced 1 time by &0670[4]
.read_rdln_ctrl_block
    jsr tube_read_r2                                                  ; bdfa: 20 c5 06     .. :066a[4]   ; Read control block byte from R2; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    sta zp_ptr_lo,x                                                   ; bdfd: 95 00       ..  :066d[4]   ; Store in zero page params
    dex                                                               ; bdff: ca          .   :066f[4]   ; Next byte (descending)
    bpl read_rdln_ctrl_block                                          ; be00: 10 f8       ..  :0670[4]   ; Loop until all 5 bytes read
    inx                                                               ; be02: e8          .   :0672[4]   ; X=0 after loop, A=0 for OSWORD 0 (read line)
    ldy #0                                                            ; be03: a0 00       ..  :0673[4]   ; Y=0 for OSWORD 0
    txa                                                               ; be05: 8a          .   :0675[4]   ; A=0: OSWORD 0 (read line)
    jsr osword                                                        ; be06: 20 f1 ff     .. :0676[4]   ; Read input line from keyboard
    bcc tube_rdln_send_line                                           ; be09: 90 05       ..  :0679[4]   ; C=0: line read OK; C=1: escape pressed
    lda #&ff                                                          ; be0b: a9 ff       ..  :067b[4]   ; &FF = escape/error signal to co-processor
    jmp tube_reply_byte                                               ; be0d: 4c 9e 05    L.. :067d[4]   ; Escape: send &FF error to co-processor

; &be10 referenced 1 time by &0679[4]
.tube_rdln_send_line
    ldx #0                                                            ; be10: a2 00       ..  :0680[4]   ; X=0: start of input buffer at &0700
    lda #&7f                                                          ; be12: a9 7f       ..  :0682[4]   ; &7F = line read successfully
    jsr tube_send_r2                                                  ; be14: 20 95 06     .. :0684[4]   ; Send &7F (success) to co-processor
; &be17 referenced 1 time by &0690[4]
.tube_rdln_send_loop
    lda string_buf,x                                                  ; be17: bd 00 07    ... :0687[4]   ; Load char from input buffer
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; be1a: 20 95 06     .. :068a[4]   ; Send char to co-processor
    inx                                                               ; be1d: e8          .   :068d[4]   ; Next character
    cmp #&0d                                                          ; be1e: c9 0d       ..  :068e[4]   ; Loop until CR terminator sent
    bne tube_rdln_send_loop                                           ; be20: d0 f5       ..  :0690[4]   ; Loop until CR terminator sent
    jmp tube_main_loop                                                ; be22: 4c 36 00    L6. :0692[4]   ; Return to main event loop

; &be25 referenced 13 times by &0020[1], &0026[1], &002c[1], &0474[2], &0572[3], &0579[3], &05c2[3], &05c9[3], &05e8[3], &061a[4], &0684[4], &068a[4], &0698[4]
.tube_send_r2
    bit tube_status_register_2                                        ; be25: 2c e2 fe    ,.. :0695[4]   ; Poll R2 status (bit 6 = ready)
    bvc tube_send_r2                                                  ; be28: 50 fb       P.  :0698[4]   ; Not ready: keep polling
    sta tube_data_register_2                                          ; be2a: 8d e3 fe    ... :069a[4]   ; Write A to Tube R2 data register
    rts                                                               ; be2d: 60          `   :069d[4]   ; Return to caller

; &be2e referenced 8 times by &0018[1], &0418[2], &041d[2], &043b[2], &0443[2], &0448[2], &0463[2], &06a1[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; be2e: 2c e6 fe    ,.. :069e[4]   ; Poll R4 status (bit 6 = ready)
    bvc tube_send_r4                                                  ; be31: 50 fb       P.  :06a1[4]   ; Not ready: keep polling
    sta tube_data_register_4                                          ; be33: 8d e7 fe    ... :06a3[4]   ; Write A to Tube R4 data register
    rts                                                               ; be36: 60          `   :06a6[4]   ; Return to caller

; &be37 referenced 1 time by &0403[2]
.tube_escape_check
    lda escape_flag                                                   ; be37: a5 ff       ..  :06a7[4]   ; Check OS escape flag at &FF
    sec                                                               ; be39: 38          8   :06a9[4]   ; SEC+ROR: put bit 7 of &FF into carry+bit 7
    ror a                                                             ; be3a: 6a          j   :06aa[4]   ; ROR: shift escape bit 7 to carry
    bmi tube_send_r1                                                  ; be3b: 30 0f       0.  :06ab[4]   ; Escape set: forward to co-processor via R1
.tube_event_handler
    pha                                                               ; be3d: 48          H   :06ad[4]   ; EVNTV: forward event A, Y, X to co-processor
    lda #0                                                            ; be3e: a9 00       ..  :06ae[4]   ; Send &00 prefix (event notification)
    jsr tube_send_r1                                                  ; be40: 20 bc 06     .. :06b0[4]   ; Send event number via R1
    tya                                                               ; be43: 98          .   :06b3[4]   ; Y value for event
    jsr tube_send_r1                                                  ; be44: 20 bc 06     .. :06b4[4]   ; Send Y via R1
    txa                                                               ; be47: 8a          .   :06b7[4]   ; X value for event
    jsr tube_send_r1                                                  ; be48: 20 bc 06     .. :06b8[4]   ; Send X via R1
    pla                                                               ; be4b: 68          h   :06bb[4]   ; Restore A (event type)
; &be4c referenced 5 times by &06ab[4], &06b0[4], &06b4[4], &06b8[4], &06bf[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; be4c: 2c e0 fe    ,.. :06bc[4]   ; Poll R1 status (bit 6 = ready)
    bvc tube_send_r1                                                  ; be4f: 50 fb       P.  :06bf[4]   ; Not ready: keep polling
    sta tube_data_register_1                                          ; be51: 8d e1 fe    ... :06c1[4]   ; Write A to Tube R1 data register
    rts                                                               ; be54: 60          `   :06c4[4]   ; Return to caller

; ***************************************************************************************
; Poll Tube R2 status until data is ready,
; then read and return the data byte.
; ***************************************************************************************
; &be55 referenced 15 times by &0542[3], &0552[3], &0564[3], &056c[3], &0586[3], &05ab[3], &05bc[3], &05d3[3], &05db[3], &0607[4], &060b[4], &060f[4], &0627[4], &066a[4], &06c8[4]
.tube_read_r2
    bit tube_status_register_2                                        ; be55: 2c e2 fe    ,.. :06c5[4]   ; Poll R2 status (bit 7 = ready)
    bpl tube_read_r2                                                  ; be58: 10 fb       ..  :06c8[4]   ; Not ready: keep polling; Poll Tube R2 status until data is ready,
; then read and return the data byte.
    lda tube_data_register_2                                          ; be5a: ad e3 fe    ... :06ca[4]   ; Read data byte from R2
    rts                                                               ; be5d: 60          `   :06cd[4]   ; Return with byte in A

    cmp #&fe                                                          ; be5e: c9 fe       ..  :06ce[4]
    bcc l072e                                                         ; be60: 90 5c       .\  :06d0[4]
    bne c06ef                                                         ; be62: d0 1b       ..  :06d2[4]
    cpy #0                                                            ; be64: c0 00       ..  :06d4[4]
    beq l072e                                                         ; be66: f0 56       .V  :06d6[4]
    ldx #6                                                            ; be68: a2 06       ..  :06d8[4]
    lda #osbyte_explode_chars                                         ; be6a: a9 14       ..  :06da[4]
    jsr osbyte                                                        ; be6c: 20 f4 ff     .. :06dc[4]   ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
; &be6f referenced 1 time by &06e2[4]
.loop_c06df
    bit tube_status_1_and_tube_control                                ; be6f: 2c e0 fe    ,.. :06df[4]
    bpl loop_c06df                                                    ; be72: 10 fb       ..  :06e2[4]
    lda tube_data_register_1                                          ; be74: ad e1 fe    ... :06e4[4]
    beq l072c                                                         ; be77: f0 43       .C  :06e7[4]
    jsr oswrch                                                        ; be79: 20 ee ff     .. :06e9[4]   ; Write character
.svc_11_nmi_claim
    jmp cbe6f                                                         ; be7c: 4c 6f be    Lo. :06ec[4]   ; Trampoline: init NMI workspace

; &be7f referenced 1 time by &06d2[4]
.c06ef
    lda #&ad                                                          ; be7f: a9 ad       ..  :06ef[4]   ; A=4: CB1 interrupt bit mask
    sta evntv                                                         ; be81: 8d 20 02    . . :06f1[4]
    lda #6                                                            ; be84: a9 06       ..  :06f4[4]   ; A=5: NMI not for us
    sta evntv+1                                                       ; be86: 8d 21 02    .!. :06f6[4]
    lda #&16                                                          ; be89: a9 16       ..  :06f9[4]
    sta brkv                                                          ; be8b: 8d 02 02    ... :06fb[4]
    lda #0                                                            ; be8e: a9 00       ..  :06fe[4]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_osbyte_reply_block, *, reloc_p6_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_osbyte_reply_block, &0700

    ; Set the program counter to the next position in the binary file.
    org reloc_p6_src + (* - tube_osbyte_reply_block)


    org &8000

; Sideways ROM header
; &8000 referenced 1 time by &04e6[2]
.pydis_start
.rom_header
.language_entry
rom_header_byte1 = rom_header+1
rom_header_byte2 = rom_header+2
    equb 0, &42, &43                                                  ; 8000: 00 42 43    .BC
; &8001 referenced 1 time by &04eb[2]
; &8002 referenced 1 time by &04f0[2]

; &8003 referenced 1 time by &04f5[2]
.service_entry
service_handler_lo = service_entry+1
    jmp service_handler                                               ; 8003: 4c 0b 8a    L..            ; JMP service_handler; Service call handler.
; On entry: A=service call number, X=ROM slot, Y=parameter.
; Service 1: absolute workspace claim.
; Service 4: unrecognised star command.
; Service 8: unrecognised OSWORD.
; Service 9: *HELP.
; Service 13: ROM initialisation.
; Service 14: ROM initialisation complete.
; Service 15: vectors claimed.

; &8004 referenced 1 time by &04f8[2]
; &8006 referenced 1 time by &04da[2]
.rom_type
    equb &82                                                          ; 8006: 82          .              ; ROM type: service + language
; &8007 referenced 1 time by &04e2[2]
.copyright_offset
    equb copyright - rom_header                                       ; 8007: 14          .
.binary_version
    equb 4                                                            ; 8008: 04          .
.title
    equs "Acorn ANFS"                                                 ; 8009: 41 63 6f... Aco
.version
    equb 0                                                            ; 8013: 00          .
.copyright
    equb 0                                                            ; 8014: 00          .              ; Null terminator before copyright
.copyright_string
    equs "(C)1985 Acorn", 0                                           ; 8015: 28 43 29... (C)

; ***************************************************************************************
; Service 5 handler: unrecognised interrupt.
; Checks for CB1 (shift register complete),
; restores VIA state, and dispatches the TX
; completion callback via ws_0d65 index.
; ***************************************************************************************
.nmi_handler
    lda #4                                                            ; 8023: a9 04       ..             ; A=4: CB1 bit mask for IFR test
    bit system_via_ifr                                                ; 8025: 2c 4d fe    ,M.            ; Test IFR bit 2: CB1 active edge
    bne c802d                                                         ; 8028: d0 03       ..             ; CB1 set: shift register complete
    lda #5                                                            ; 802a: a9 05       ..             ; A=5: not our interrupt, pass on
    rts                                                               ; 802c: 60          `              ; Return service code 5 to MOS

; &802d referenced 1 time by &8028
.c802d
    txa                                                               ; 802d: 8a          .              ; Save X on stack
    pha                                                               ; 802e: 48          H              ; Push saved X
    tya                                                               ; 802f: 98          .              ; Save Y on stack
    pha                                                               ; 8030: 48          H              ; Push saved Y
    lda system_via_acr                                                ; 8031: ad 4b fe    .K.            ; Read ACR for shift register restore
    and #&e3                                                          ; 8034: 29 e3       ).             ; Clear SR mode bits (2-4)
    ora ws_0d64                                                       ; 8036: 0d 64 0d    .d.            ; Restore saved SR mode from ws_0d64
    sta system_via_acr                                                ; 8039: 8d 4b fe    .K.            ; Write restored ACR to system VIA
    lda system_via_sr                                                 ; 803c: ad 4a fe    .J.            ; Read SR to clear shift register IRQ
    lda #4                                                            ; 803f: a9 04       ..             ; A=4: CB1 bit mask
    sta system_via_ifr                                                ; 8041: 8d 4d fe    .M.            ; Clear CB1 interrupt flag in IFR
    sta system_via_ier                                                ; 8044: 8d 4e fe    .N.            ; Disable CB1 interrupt in IER
    ldy ws_0d65                                                       ; 8047: ac 65 0d    .e.            ; Load TX completion handler index
    tya                                                               ; 804a: 98          .              ; Copy to A for sign test
    bmi c8052                                                         ; 804b: 30 05       0.             ; Bit 7 set: dispatch via table
    ldy #&fe                                                          ; 804d: a0 fe       ..             ; Y=&FE: Econet event number
    jmp tx_done_fire_event                                            ; 804f: 4c 4a 85    LJ.            ; Generate event and exit

; &8052 referenced 1 time by &804b
.c8052
    cpy #&86                                                          ; 8052: c0 86       ..             ; Y >= &86: above dispatch range
    bcs dispatch_svc5                                                 ; 8054: b0 0b       ..             ; Out of range: skip protection
    lda ws_0d68                                                       ; 8056: ad 68 0d    .h.            ; Save current JSR protection mask
    sta ws_0d69                                                       ; 8059: 8d 69 0d    .i.            ; Backup to saved_jsr_mask
    ora #&1c                                                          ; 805c: 09 1c       ..             ; Set protection bits 2-4
    sta ws_0d68                                                       ; 805e: 8d 68 0d    .h.            ; Apply protection during dispatch
; &8061 referenced 1 time by &8054
.dispatch_svc5
    lda #&85                                                          ; 8061: a9 85       ..             ; Push return addr high (&85)
    pha                                                               ; 8063: 48          H              ; High byte on stack for RTS
    lda set_rx_buf_len_hi,y                                           ; 8064: b9 b1 84    ...            ; Load dispatch target low byte
    pha                                                               ; 8067: 48          H              ; Low byte on stack for RTS
.svc_5_unknown_irq
    rts                                                               ; 8068: 60          `              ; RTS = dispatch to PHA'd address

; ***************************************************************************************
; Initialise ADLC: full hardware reset then
; configure for receive/listen mode.
; Falls through to init_nmi_workspace.
; ***************************************************************************************
; &8069 referenced 1 time by &8f40
.adlc_init
    bit station_id_disable_net_nmis                                   ; 8069: 2c 18 fe    ,..            ; INTOFF: read station ID, disable NMIs
    jsr adlc_full_reset                                               ; 806c: 20 5f 89     _.            ; Full ADLC hardware reset; Full MC6854 ADLC hardware reset. Set CR1
; with TX and RX in reset, then configure
; CR4 and CR3 via address control mode.
    lda #&ea                                                          ; 806f: a9 ea       ..             ; OSBYTE &EA: check Tube co-processor
    ldx #0                                                            ; 8071: a2 00       ..             ; X=0 for OSBYTE
    stx ws_0d62                                                       ; 8073: 8e 62 0d    .b.            ; Clear Econet init flag before setup
    jsr osbyte_x0                                                     ; 8076: 20 6d 8e     m.            ; OSBYTE with X=0, Y=&FF.
; Called from dispatch table for specific OSBYTE calls.
    stx l0d63                                                         ; 8079: 8e 63 0d    .c.            ; Store Tube presence flag from OSBYTE &EA
    lda #&8f                                                          ; 807c: a9 8f       ..             ; OSBYTE &8F: issue service request
    ldx #&0c                                                          ; 807e: a2 0c       ..             ; X=&0C: NMI claim service
    jsr osbyte_yff                                                    ; 8080: 20 6f 8e     o.            ; OSBYTE with Y=&FF.
; Entry with X already set by caller.
    ldy #5                                                            ; 8083: a0 05       ..             ; Y=5: NMI claim service number
    cpy #5                                                            ; 8085: c0 05       ..             ; Check if NMI service was claimed (Y changed)
    bne return_1                                                      ; 8087: d0 29       .)             ; Service claimed by other ROM: skip init
; ***************************************************************************************
; Copy NMI shim code from ROM to &0D00 and
; initialise Econet NMI workspace variables.
; ***************************************************************************************
.init_nmi_workspace
    ldy #&20 ; ' '                                                    ; 8089: a0 20       .              ; Copy 32 bytes of NMI shim from ROM to &0D00
; &808b referenced 1 time by &8092
.copy_nmi_shim
    lda listen_jmp_hi,y                                               ; 808b: b9 9c 89    ...            ; Read byte from NMI shim ROM source
    sta nmi_code_base,y                                               ; 808e: 99 ff 0c    ...            ; Write to NMI shim RAM at &0D00
    dey                                                               ; 8091: 88          .              ; Next byte (descending)
    bne copy_nmi_shim                                                 ; 8092: d0 f7       ..             ; Loop until all 32 bytes copied
    lda romsel_copy                                                   ; 8094: a5 f4       ..             ; Patch current ROM bank into NMI shim
    sta l0d07                                                         ; 8096: 8d 07 0d    ...            ; Self-modifying code: ROM bank at &0D07
    sty tx_src_net                                                    ; 8099: 8c 23 0d    .#.            ; Clear source network (Y=0 from copy loop)
    sty need_release_tube                                             ; 809c: 84 98       ..             ; Clear Tube release flag
    sty ws_0d65                                                       ; 809e: 8c 65 0d    .e.            ; Clear TX completion handler index
    ldy station_id_disable_net_nmis                                   ; 80a1: ac 18 fe    ...            ; Read station ID (and disable NMIs)
    sty tx_src_stn                                                    ; 80a4: 8c 22 0d    .".            ; Set own station as TX source
    lda #&80                                                          ; 80a7: a9 80       ..             ; &80 = Econet initialised
    sta ws_0d60                                                       ; 80a9: 8d 60 0d    .`.            ; Mark TX as complete (ready)
    sta ws_0d62                                                       ; 80ac: 8d 62 0d    .b.            ; Mark Econet as initialised
    bit video_ula_control                                             ; 80af: 2c 20 fe    , .            ; INTON: re-enable NMIs (&FE20 read side effect)
; &80b2 referenced 1 time by &8087
.return_1
    rts                                                               ; 80b2: 60          `              ; Return

; ***************************************************************************************
; NMI handler for incoming scout frames.
; Check destination station; accept if it
; matches our ID or is broadcast (&FF).
; ***************************************************************************************
; &80b3 referenced 1 time by &89a8
.nmi_rx_scout
    lda #1                                                            ; 80b3: a9 01       ..             ; A=&01: mask for SR2 bit0 (AP = Address Present)
    bit econet_control23_or_status2                                   ; 80b5: 2c a1 fe    ,..            ; BIT SR2: Z = A AND SR2 -- tests if AP is set
    beq scout_error                                                   ; 80b8: f0 38       .8             ; AP not set, no incoming data -- check for errors; Handle scout reception error. Read SR2 to
; determine error type and discard the frame.
    lda econet_data_continue_frame                                    ; 80ba: ad a2 fe    ...            ; Read first RX byte (destination station address)
    cmp station_id_disable_net_nmis                                   ; 80bd: cd 18 fe    ...            ; Compare to our station ID (&FE18 read = INTOFF, disables NMIs)
    beq accept_frame                                                  ; 80c0: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 80c2: c9 ff       ..             ; Check for broadcast address (&FF)
    bne scout_reject                                                  ; 80c4: d0 18       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 80c6: a9 40       .@             ; Flag &40 = broadcast frame
    sta rx_src_net                                                    ; 80c8: 8d 3e 0d    .>.            ; Clear TX flags for new reception
; &80cb referenced 1 time by &80c0
.accept_frame
    lda #&d0                                                          ; 80cb: a9 d0       ..             ; Install nmi_rx_scout_net NMI handler
    jmp install_nmi_handler                                           ; 80cd: 4c 11 0d    L..            ; Install next handler and RTI

; ***************************************************************************************
; NMI handler for scout frame network byte.
; Accept local network (0) or broadcast
; (&FF); reject frames for other networks.
; ***************************************************************************************
.nmi_rx_scout_net
    bit econet_control23_or_status2                                   ; 80d0: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl scout_error                                                   ; 80d3: 10 1d       ..             ; No RDA -- check errors; Handle scout reception error. Read SR2 to
; determine error type and discard the frame.
    lda econet_data_continue_frame                                    ; 80d5: ad a2 fe    ...            ; Read destination network byte
    beq accept_local_net                                              ; 80d8: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 80da: 49 ff       I.             ; EOR &FF: test if network = &FF (broadcast)
    beq accept_scout_net                                              ; 80dc: f0 0b       ..             ; Broadcast network -- accept
; &80de referenced 1 time by &80c4
.scout_reject
    lda #&a2                                                          ; 80de: a9 a2       ..             ; Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 80e0: 8d a0 fe    ...            ; Write CR1 to discontinue RX
    jmp set_nmi_rx_scout                                              ; 80e3: 4c f1 83    L..            ; Return to idle scout listening

; &80e6 referenced 1 time by &80d8
.accept_local_net
    sta rx_src_net                                                    ; 80e6: 8d 3e 0d    .>.            ; Network = &FF broadcast: clear &0D4A
; &80e9 referenced 1 time by &80dc
.accept_scout_net
    sta port_buf_len                                                  ; 80e9: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #2                                                            ; 80eb: a9 02       ..             ; Install scout data handler (&8102)
    ldy #&81                                                          ; 80ed: a0 81       ..             ; High byte of scout data handler
    jmp set_nmi_vector                                                ; 80ef: 4c 0e 0d    L..            ; Install scout data loop and RTI

; ***************************************************************************************
; Handle scout reception error. Read SR2 to
; determine error type and discard the frame.
; ***************************************************************************************
; &80f2 referenced 5 times by &80b8, &80d3, &8107, &813b, &813d
.scout_error
    lda econet_control23_or_status2                                   ; 80f2: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 80f5: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 80f7: f0 06       ..             ; Neither set -- clean end, discard frame
    jsr adlc_full_reset                                               ; 80f9: 20 5f 89     _.            ; Unexpected data/status: full ADLC reset; Full MC6854 ADLC hardware reset. Set CR1
; with TX and RX in reset, then configure
; CR4 and CR3 via address control mode.
    jmp set_nmi_rx_scout                                              ; 80fc: 4c f1 83    L..            ; Discard and return to idle

; &80ff referenced 1 time by &80f7
.scout_discard
    jmp reset_adlc_rx_listen                                          ; 80ff: 4c ee 83    L..            ; Gentle discard: RX_DISCONTINUE

    ldy port_buf_len                                                  ; 8102: a4 a2       ..             ; Y = buffer offset
    lda econet_control23_or_status2                                   ; 8104: ad a1 fe    ...            ; Read SR2
; &8107 referenced 1 time by &8127
.scout_loop_rda
    bpl scout_error                                                   ; 8107: 10 e9       ..             ; No RDA -- error handler; Handle scout reception error. Read SR2 to
; determine error type and discard the frame.
    lda econet_data_continue_frame                                    ; 8109: ad a2 fe    ...            ; Read data byte from RX FIFO
    sta l0d2e,y                                                       ; 810c: 99 2e 0d    ...            ; Store at &0D3D+Y (scout buffer)
    iny                                                               ; 810f: c8          .              ; Advance buffer index
    lda econet_control23_or_status2                                   ; 8110: ad a1 fe    ...            ; Read SR2 again (FV detection point)
    bmi scout_loop_second                                             ; 8113: 30 02       0.             ; RDA set -- more data, read second byte
    bne scout_complete                                                ; 8115: d0 15       ..             ; SR2 non-zero (FV or other) -- scout completion; Process completed scout frame. Match port
; against open receive control blocks, set up
; data phase handler, and send acknowledge.
; &8117 referenced 1 time by &8113
.scout_loop_second
    lda econet_data_continue_frame                                    ; 8117: ad a2 fe    ...            ; Read second byte of pair
    sta l0d2e,y                                                       ; 811a: 99 2e 0d    ...            ; Store at &0D3D+Y
    iny                                                               ; 811d: c8          .              ; Advance and check buffer limit
    cpy #&0c                                                          ; 811e: c0 0c       ..             ; Copied all 12 scout bytes?
    beq scout_complete                                                ; 8120: f0 0a       ..             ; Buffer full (Y=12) -- force completion; Process completed scout frame. Match port
; against open receive control blocks, set up
; data phase handler, and send acknowledge.
    sty port_buf_len                                                  ; 8122: 84 a2       ..             ; Save final buffer offset
    lda econet_control23_or_status2                                   ; 8124: ad a1 fe    ...            ; Read SR2 for next pair
    bne scout_loop_rda                                                ; 8127: d0 de       ..             ; SR2 non-zero -- loop back for more bytes
    jmp nmi_rti                                                       ; 8129: 4c 14 0d    L..            ; SR2 = 0 -- RTI, wait for next NMI

; ***************************************************************************************
; Process completed scout frame. Match port
; against open receive control blocks, set up
; data phase handler, and send acknowledge.
; ***************************************************************************************
; &812c referenced 2 times by &8115, &8120
.scout_complete
    lda #0                                                            ; 812c: a9 00       ..             ; Save Y for next iteration
    sta econet_control1_or_status1                                    ; 812e: 8d a0 fe    ...            ; Write CR1
    lda #&84                                                          ; 8131: a9 84       ..             ; CR2=&84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 8133: 8d a1 fe    ...            ; Write CR2
    lda #2                                                            ; 8136: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 8138: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 813b: f0 b5       ..             ; No FV -- not a valid frame end, error; Handle scout reception error. Read SR2 to
; determine error type and discard the frame.
    bpl scout_error                                                   ; 813d: 10 b3       ..             ; FV set but no RDA -- missing last byte, error; Handle scout reception error. Read SR2 to
; determine error type and discard the frame.
    lda econet_data_continue_frame                                    ; 813f: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta l0d2e,y                                                       ; 8142: 99 2e 0d    ...            ; Store last byte at &0D3D+Y
    lda #&44 ; 'D'                                                    ; 8145: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 8147: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    sec                                                               ; 814a: 38          8              ; Set bit7 of need_release_tube flag
    ror need_release_tube                                             ; 814b: 66 98       f.             ; Rotate C=1 into bit7: mark Tube release needed
    lda l0d31                                                         ; 814d: ad 31 0d    .1.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 8150: d0 03       ..             ; Port non-zero -- look for matching receive block
.scout_no_match
    jmp discard_after_reset                                           ; 8152: 4c 4b 84    LK.            ; Port = 0 -- immediate operation handler; Discard frame after ADLC reset. Wait for
; idle line, then restore listen mode and
; dispatch any pending immediate operations.

; &8155 referenced 1 time by &8150
.scout_match_port
    bit rx_src_net                                                    ; 8155: 2c 3e 0d    ,>.            ; Check if broadcast (bit6 of tx_flags)
    bvc scan_port_list                                                ; 8158: 50 05       P.             ; Not broadcast -- skip CR2 setup
    lda #7                                                            ; 815a: a9 07       ..             ; CR2=&07: broadcast prep
    sta econet_control23_or_status2                                   ; 815c: 8d a1 fe    ...            ; Write CR2: broadcast frame prep
; &815f referenced 1 time by &8158
.scan_port_list
    bit l0d61                                                         ; 815f: 2c 61 0d    ,a.            ; Check if RX port list active (bit7)
    bpl try_nfs_port_list                                             ; 8162: 10 40       .@             ; No active ports -- try NFS workspace
    lda #&c0                                                          ; 8164: a9 c0       ..             ; Start scanning port list at page &C0
    ldy #0                                                            ; 8166: a0 00       ..             ; Y=0: start offset within each port slot
; &8168 referenced 1 time by &81ad
.scan_nfs_port_list
    sta port_ws_offset                                                ; 8168: 85 a6       ..             ; Store page to workspace pointer low
    sty rx_buf_offset                                                 ; 816a: 84 a7       ..             ; Store page high byte for slot scanning
; &816c referenced 1 time by &819f
.check_port_slot
    ldy #0                                                            ; 816c: a0 00       ..             ; Y=0: read control byte from start of slot
.scout_ctrl_check
    lda (port_ws_offset),y                                            ; 816e: b1 a6       ..             ; Read port control byte from slot
    beq discard_no_match                                              ; 8170: f0 2f       ./             ; Zero = end of port list, no match
    cmp #&7f                                                          ; 8172: c9 7f       ..             ; &7F = any-port wildcard
    bne next_port_slot                                                ; 8174: d0 1e       ..             ; Not wildcard -- check specific port match
    iny                                                               ; 8176: c8          .              ; Y=1: advance to port byte in slot
    lda (port_ws_offset),y                                            ; 8177: b1 a6       ..             ; Read port number from slot (offset 1)
    beq check_station_filter                                          ; 8179: f0 05       ..             ; Zero port in slot = match any port
    cmp l0d31                                                         ; 817b: cd 31 0d    .1.            ; Check if port matches this slot
    bne next_port_slot                                                ; 817e: d0 14       ..             ; Port mismatch -- try next slot
; &8180 referenced 1 time by &8179
.check_station_filter
    iny                                                               ; 8180: c8          .              ; Y=2: advance to station byte
    lda (port_ws_offset),y                                            ; 8181: b1 a6       ..             ; Read station filter from slot (offset 2)
    beq port_match_found                                              ; 8183: f0 2a       .*             ; Zero station = match any station, accept
    cmp l0d2e                                                         ; 8185: cd 2e 0d    ...            ; Check if source station matches
    bne next_port_slot                                                ; 8188: d0 0a       ..             ; Station mismatch -- try next slot
.scout_port_match
    iny                                                               ; 818a: c8          .              ; Y=3: advance to network byte
    lda (port_ws_offset),y                                            ; 818b: b1 a6       ..             ; Read network filter from slot (offset 3)
    beq port_match_found                                              ; 818d: f0 20       .              ; Zero = accept any network
    cmp l0d2f                                                         ; 818f: cd 2f 0d    ./.            ; Check if source network matches
    beq port_match_found                                              ; 8192: f0 1b       ..             ; Network matches or zero = accept
; &8194 referenced 3 times by &8174, &817e, &8188
.next_port_slot
    lda rx_buf_offset                                                 ; 8194: a5 a7       ..             ; Check if NFS workspace search pending
    beq try_nfs_port_list                                             ; 8196: f0 0c       ..             ; No NFS workspace -- try fallback path
    lda port_ws_offset                                                ; 8198: a5 a6       ..             ; Load current slot base address
    clc                                                               ; 819a: 18          .              ; CLC for 12-byte slot advance
    adc #&0c                                                          ; 819b: 69 0c       i.             ; Advance to next 12-byte port slot
    sta port_ws_offset                                                ; 819d: 85 a6       ..             ; Update workspace pointer to next slot
    bcc check_port_slot                                               ; 819f: 90 cb       ..             ; Always branches (page &C0 won't overflow)
; &81a1 referenced 2 times by &8170, &81a7
.discard_no_match
    jmp nmi_error_dispatch                                            ; 81a1: 4c 2b 82    L+.            ; No match found -- discard frame; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.

; &81a4 referenced 2 times by &8162, &8196
.try_nfs_port_list
    bit l0d61                                                         ; 81a4: 2c 61 0d    ,a.            ; Try NFS workspace if paged list exhausted
    bvc discard_no_match                                              ; 81a7: 50 f8       P.             ; No NFS workspace RX (bit6 clear) -- discard
    lda #0                                                            ; 81a9: a9 00       ..             ; NFS workspace starts at offset 0 in page
    ldy nfs_workspace_hi                                              ; 81ab: a4 9f       ..             ; NFS workspace high byte for port list
    bne scan_nfs_port_list                                            ; 81ad: d0 b9       ..             ; Scan NFS workspace port list
; &81af referenced 3 times by &8183, &818d, &8192
.port_match_found
    lda #3                                                            ; 81af: a9 03       ..             ; Match found: set scout_status = 3
    sta rx_port                                                       ; 81b1: 8d 40 0d    .@.            ; Record match for completion handler
    jsr tx_calc_transfer                                              ; 81b4: 20 e8 88     ..            ; Calculate transfer parameters; Calculate transfer size for data phase.
; Compute byte count from buffer start/end
; pointers in the TX control block.
    bcc nmi_error_dispatch                                            ; 81b7: 90 72       .r             ; C=0: no Tube claimed -- discard; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    bit rx_src_net                                                    ; 81b9: 2c 3e 0d    ,>.            ; Check broadcast flag for ACK path
    bvc send_data_rx_ack                                              ; 81bc: 50 03       P.             ; Not broadcast -- normal ACK path
    jmp copy_scout_to_buffer                                          ; 81be: 4c 06 84    L..            ; Broadcast: different completion path; Copy received scout data into the RXCB
; buffer. Handle both direct RAM and Tube
; transfer paths.

; &81c1 referenced 1 time by &81bc
.send_data_rx_ack
    lda #&44 ; 'D'                                                    ; 81c1: a9 44       .D             ; CR1=&44: RX_RESET | TIE
    sta econet_control1_or_status1                                    ; 81c3: 8d a0 fe    ...            ; Write CR1: TX mode for ACK
    lda #&a7                                                          ; 81c6: a9 a7       ..             ; CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE
    sta econet_control23_or_status2                                   ; 81c8: 8d a1 fe    ...            ; Write CR2: enable TX with PSE
    lda #&d2                                                          ; 81cb: a9 d2       ..             ; Install data_rx_setup at &81D2
    ldy #&81                                                          ; 81cd: a0 81       ..             ; High byte of data_rx_setup handler
    jmp ack_tx_write_dest                                             ; 81cf: 4c fd 82    L..            ; Send ACK with data_rx_setup as next NMI

.data_rx_setup
    lda #&82                                                          ; 81d2: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 81d4: 8d a0 fe    ...            ; Write CR1: switch to RX for data frame
    lda #&dc                                                          ; 81d7: a9 dc       ..             ; Install nmi_data_rx at &81DC
    jmp install_nmi_handler                                           ; 81d9: 4c 11 0d    L..            ; Install nmi_data_rx and return from NMI

; ***************************************************************************************
; NMI handler for data frame reception.
; Verify dest station/network, then skip
; control and port bytes known from scout.
; ***************************************************************************************
.nmi_data_rx
    lda #1                                                            ; 81dc: a9 01       ..             ; Read SR2 for AP check
    bit econet_control23_or_status2                                   ; 81de: 2c a1 fe    ,..            ; BIT SR2: test AP bit
    beq nmi_error_dispatch                                            ; 81e1: f0 48       .H             ; No AP: wrong frame or error; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    lda econet_data_continue_frame                                    ; 81e3: ad a2 fe    ...            ; Read first byte (dest station)
    cmp station_id_disable_net_nmis                                   ; 81e6: cd 18 fe    ...            ; Compare to our station ID (INTOFF)
    bne nmi_error_dispatch                                            ; 81e9: d0 40       .@             ; Not for us: error path; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    lda #&f0                                                          ; 81eb: a9 f0       ..             ; Install net check handler at &81F0
    jmp install_nmi_handler                                           ; 81ed: 4c 11 0d    L..            ; Set NMI vector via RAM shim

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 81f0: 2c a1 fe    ,..            ; Validate source network = 0
    bpl nmi_error_dispatch                                            ; 81f3: 10 36       .6             ; SR2 bit7 clear: no data ready -- error; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    lda econet_data_continue_frame                                    ; 81f5: ad a2 fe    ...            ; Read dest network byte
    bne nmi_error_dispatch                                            ; 81f8: d0 31       .1             ; Network != 0: wrong network -- error; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    lda #6                                                            ; 81fa: a9 06       ..             ; Install skip handler at &8206
    ldy #&82                                                          ; 81fc: a0 82       ..             ; High byte of &8206 handler
    bit econet_control1_or_status1                                    ; 81fe: 2c a0 fe    ,..            ; SR1 bit7: IRQ, data already waiting
    bmi nmi_data_rx_skip                                              ; 8201: 30 03       0.             ; Data ready: skip directly, no RTI
    jmp set_nmi_vector                                                ; 8203: 4c 0e 0d    L..            ; Install handler and return via RTI

; &8206 referenced 1 time by &8201
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 8206: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl nmi_error_dispatch                                            ; 8209: 10 20       .              ; SR2 bit7 clear: error; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    lda econet_data_continue_frame                                    ; 820b: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 820e: ad a2 fe    ...            ; Discard port byte
; ***************************************************************************************
; Install NMI handler for data reception:
; bulk RAM path or Tube transfer path.
; Enter bulk read directly if data waiting.
; ***************************************************************************************
; &8211 referenced 1 time by &88bc
.install_data_rx_handler
    lda #2                                                            ; 8211: a9 02       ..             ; A=2: Tube transfer flag mask
    bit rx_src_net                                                    ; 8213: 2c 3e 0d    ,>.            ; Check if Tube transfer active
    bne install_tube_rx                                               ; 8216: d0 0c       ..             ; Tube active: use Tube RX path
    lda #&39 ; '9'                                                    ; 8218: a9 39       .9             ; Install bulk read at &8239
    ldy #&82                                                          ; 821a: a0 82       ..             ; High byte of &8239 handler
    bit econet_control1_or_status1                                    ; 821c: 2c a0 fe    ,..            ; SR1 bit7: more data already waiting?
    bmi nmi_data_rx_bulk                                              ; 821f: 30 18       0.             ; Yes: enter bulk read directly; NMI bulk data receive loop. Read byte
; pairs from ADLC RX FIFO into the port
; receive buffer, handling page boundaries.
    jmp set_nmi_vector                                                ; 8221: 4c 0e 0d    L..            ; No: install handler and RTI

; &8224 referenced 1 time by &8216
.install_tube_rx
    lda #&96                                                          ; 8224: a9 96       ..             ; Tube: install Tube RX at &8296
    ldy #&82                                                          ; 8226: a0 82       ..             ; High byte of &8296 handler
    jmp set_nmi_vector                                                ; 8228: 4c 0e 0d    L..            ; Install Tube handler and RTI

; ***************************************************************************************
; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
; ***************************************************************************************
; &822b referenced 12 times by &81a1, &81b7, &81e1, &81e9, &81f3, &81f8, &8209, &824c, &827e, &8284, &8341, &847b
.nmi_error_dispatch
    lda rx_src_net                                                    ; 822b: ad 3e 0d    .>.            ; Check tx_flags for error path
    bpl rx_error_reset                                                ; 822e: 10 03       ..             ; Bit7 clear: RX error path
    jmp tx_result_fail                                                ; 8230: 4c ca 88    L..            ; Bit7 set: TX result = not listening; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.

; &8233 referenced 1 time by &822e
.rx_error_reset
    jsr adlc_full_reset                                               ; 8233: 20 5f 89     _.            ; Full ADLC reset on RX error; Full MC6854 ADLC hardware reset. Set CR1
; with TX and RX in reset, then configure
; CR4 and CR3 via address control mode.
    jmp discard_reset_rx                                              ; 8236: 4c eb 83    L..            ; Discard and return to idle listen

; ***************************************************************************************
; NMI bulk data receive loop. Read byte
; pairs from ADLC RX FIFO into the port
; receive buffer, handling page boundaries.
; ***************************************************************************************
; &8239 referenced 1 time by &821f
.nmi_data_rx_bulk
    ldy port_buf_len                                                  ; 8239: a4 a2       ..             ; Y = buffer offset, resume from last position
    lda econet_control23_or_status2                                   ; 823b: ad a1 fe    ...            ; Read SR2 for next pair
; &823e referenced 1 time by &8268
.data_rx_loop
    bpl data_rx_complete                                              ; 823e: 10 2d       .-             ; SR2 bit7 clear: frame complete (FV); Complete data frame reception. Verify
; frame valid (FV) flag, update buffer
; pointers, and begin ACK transmission.
    lda econet_data_continue_frame                                    ; 8240: ad a2 fe    ...            ; Read first byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 8243: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 8245: c8          .              ; Advance buffer offset
    bne read_sr2_between_pairs                                        ; 8246: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 8248: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 824a: c6 a3       ..             ; Decrement remaining page count
    beq nmi_error_dispatch                                            ; 824c: f0 dd       ..             ; No pages left: handle as complete; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
; &824e referenced 1 time by &8246
.read_sr2_between_pairs
    lda econet_control23_or_status2                                   ; 824e: ad a1 fe    ...            ; Read SR2 between byte pairs
    bmi read_second_rx_byte                                           ; 8251: 30 02       0.             ; SR2 bit7 set: more data available
    bne data_rx_complete                                              ; 8253: d0 18       ..             ; SR2 non-zero, bit7 clear: frame done; Complete data frame reception. Verify
; frame valid (FV) flag, update buffer
; pointers, and begin ACK transmission.
; &8255 referenced 1 time by &8251
.read_second_rx_byte
    lda econet_data_continue_frame                                    ; 8255: ad a2 fe    ...            ; Read second byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 8258: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 825a: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 825b: 84 a2       ..             ; Save updated buffer position
    bne check_sr2_loop_again                                          ; 825d: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 825f: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 8261: c6 a3       ..             ; Decrement remaining page count
    beq data_rx_complete                                              ; 8263: f0 08       ..             ; No pages left: frame complete; Complete data frame reception. Verify
; frame valid (FV) flag, update buffer
; pointers, and begin ACK transmission.
; &8265 referenced 1 time by &825d
.check_sr2_loop_again
    lda econet_control23_or_status2                                   ; 8265: ad a1 fe    ...            ; Read SR2 for next iteration
    bne data_rx_loop                                                  ; 8268: d0 d4       ..             ; SR2 non-zero: more data, loop back
    jmp nmi_rti                                                       ; 826a: 4c 14 0d    L..            ; SR2=0: no more data yet, wait for NMI

; ***************************************************************************************
; Complete data frame reception. Verify
; frame valid (FV) flag, update buffer
; pointers, and begin ACK transmission.
; ***************************************************************************************
; &826d referenced 3 times by &823e, &8253, &8263
.data_rx_complete
    lda #&84                                                          ; 826d: a9 84       ..             ; CR1=&00: disable all interrupts
    sta econet_control23_or_status2                                   ; 826f: 8d a1 fe    ...            ; Write CR2: disable PSE for bit testing
    lda #0                                                            ; 8272: a9 00       ..             ; CR2=&84: disable PSE for individual bit testing
    sta econet_control1_or_status1                                    ; 8274: 8d a0 fe    ...            ; Write CR1: disable all interrupts
    sty port_buf_len                                                  ; 8277: 84 a2       ..             ; Save Y (byte count from data RX loop)
    lda #2                                                            ; 8279: a9 02       ..             ; A=&02: FV mask
    bit econet_control23_or_status2                                   ; 827b: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq nmi_error_dispatch                                            ; 827e: f0 ab       ..             ; No FV -- error; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    bpl send_ack                                                      ; 8280: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 8282: a5 a3       ..             ; Check if buffer space remains
; &8284 referenced 3 times by &82a1, &82c8, &82d4
.read_last_rx_byte
    beq nmi_error_dispatch                                            ; 8284: f0 a5       ..             ; No buffer space: error/discard frame; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.
    lda econet_data_continue_frame                                    ; 8286: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 8289: a4 a2       ..             ; Y = current buffer write offset
    sta (open_port_buf),y                                             ; 828b: 91 a4       ..             ; Store last byte in port receive buffer
    inc port_buf_len                                                  ; 828d: e6 a2       ..             ; Advance buffer write offset
    bne send_ack                                                      ; 828f: d0 02       ..             ; No page wrap: proceed to send ACK
    inc open_port_buf_hi                                              ; 8291: e6 a5       ..             ; Page boundary: advance buffer page
; &8293 referenced 2 times by &8280, &828f
.send_ack
    jmp ack_tx                                                        ; 8293: 4c e4 82    L..            ; Send ACK frame to complete handshake; Begin transmitting ACK frame. Write
; destination station and network bytes
; to ADLC TX FIFO.

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 8296: ad a1 fe    ...            ; Read SR2 for Tube data receive path
; &8299 referenced 1 time by &82b4
.rx_tube_data
    bpl data_rx_tube_complete                                         ; 8299: 10 1e       ..             ; RDA clear: no more data, frame complete
    lda econet_data_continue_frame                                    ; 829b: ad a2 fe    ...            ; Read data byte from ADLC RX FIFO
    jsr advance_buffer_ptr                                            ; 829e: 20 25 85     %.            ; Check buffer limits and transfer size; Increment the 4-byte buffer pointer at
; port_buf_len/open_port_buf (&A2-&A5)
; by one. Used to advance the RX data
; write position after storing a byte.
    beq read_last_rx_byte                                             ; 82a1: f0 e1       ..             ; Zero: buffer full, handle as error
    sta tube_data_register_3                                          ; 82a3: 8d e5 fe    ...            ; Send byte to Tube data register 3
    lda econet_data_continue_frame                                    ; 82a6: ad a2 fe    ...            ; Read second data byte (paired transfer)
    sta tube_data_register_3                                          ; 82a9: 8d e5 fe    ...            ; Send second byte to Tube
    jsr advance_buffer_ptr                                            ; 82ac: 20 25 85     %.            ; Check limits after byte pair; Increment the 4-byte buffer pointer at
; port_buf_len/open_port_buf (&A2-&A5)
; by one. Used to advance the RX data
; write position after storing a byte.
    beq data_rx_tube_complete                                         ; 82af: f0 08       ..             ; Zero: Tube transfer complete
    lda econet_control23_or_status2                                   ; 82b1: ad a1 fe    ...            ; Re-read SR2 for next byte pair
    bne rx_tube_data                                                  ; 82b4: d0 e3       ..             ; More data available: continue loop
.data_rx_tube_error
    jmp nmi_rti                                                       ; 82b6: 4c 14 0d    L..            ; Unexpected end: return from NMI

; &82b9 referenced 2 times by &8299, &82af
.data_rx_tube_complete
    lda #0                                                            ; 82b9: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 82bb: 8d a0 fe    ...            ; Write CR1 for individual bit testing
    lda #&84                                                          ; 82be: a9 84       ..             ; CR2=&84: disable PSE
    sta econet_control23_or_status2                                   ; 82c0: 8d a1 fe    ...            ; Write CR2: same pattern as main path
    lda #2                                                            ; 82c3: a9 02       ..             ; A=&02: FV mask for Tube completion
    bit econet_control23_or_status2                                   ; 82c5: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq read_last_rx_byte                                             ; 82c8: f0 ba       ..             ; No FV: incomplete frame, error
    bpl ack_tx                                                        ; 82ca: 10 18       ..             ; FV set, no RDA: proceed to ACK; Begin transmitting ACK frame. Write
; destination station and network bytes
; to ADLC TX FIFO.
    lda port_buf_len                                                  ; 82cc: a5 a2       ..             ; Check if any buffer was allocated
    ora port_buf_len_hi                                               ; 82ce: 05 a3       ..             ; OR all 4 buffer pointer bytes together
    ora open_port_buf                                                 ; 82d0: 05 a4       ..             ; Check buffer low byte
    ora open_port_buf_hi                                              ; 82d2: 05 a5       ..             ; Check buffer high byte
    beq read_last_rx_byte                                             ; 82d4: f0 ae       ..             ; All zero (null buffer): error
    lda econet_data_continue_frame                                    ; 82d6: ad a2 fe    ...            ; Read extra trailing byte from FIFO
    sta l0d42                                                         ; 82d9: 8d 42 0d    .B.            ; Save extra byte at &0D5D for later use
    lda #&20 ; ' '                                                    ; 82dc: a9 20       .              ; Bit5 = extra data byte available flag
    ora rx_src_net                                                    ; 82de: 0d 3e 0d    .>.            ; Set extra byte flag in tx_flags
    sta rx_src_net                                                    ; 82e1: 8d 3e 0d    .>.            ; Store updated flags
; ***************************************************************************************
; Begin transmitting ACK frame. Write
; destination station and network bytes
; to ADLC TX FIFO.
; ***************************************************************************************
; &82e4 referenced 2 times by &8293, &82ca
.ack_tx
    lda rx_src_net                                                    ; 82e4: ad 3e 0d    .>.            ; Load TX flags to check ACK type
    bpl ack_tx_configure                                              ; 82e7: 10 06       ..             ; Bit7 clear: normal scout ACK
    jsr advance_rx_buffer_ptr                                         ; 82e9: 20 44 83     D.            ; Final ACK: call completion handler; Update RXCB buffer pointer and length
; after data reception. Handle page
; boundary crossings and Tube transfers.
    jmp tx_result_ok                                                  ; 82ec: 4c c6 88    L..            ; Jump to TX success result; Set transmit result to success (A=0)
; and fall through to tx_store_result.

; &82ef referenced 1 time by &82e7
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 82ef: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 82f1: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    lda #&a7                                                          ; 82f4: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 82f6: 8d a1 fe    ...            ; Write CR2: enable TX with status clear
    lda #&8b                                                          ; 82f9: a9 8b       ..             ; Install saved next handler (&838B for scout ACK)
    ldy #&83                                                          ; 82fb: a0 83       ..             ; High byte of post-ACK handler
; &82fd referenced 2 times by &81cf, &84e9
.ack_tx_write_dest
    sta l0d43                                                         ; 82fd: 8d 43 0d    .C.            ; Store next handler low byte
    sty l0d44                                                         ; 8300: 8c 44 0d    .D.            ; Store next handler high byte
    lda l0d2e                                                         ; 8303: ad 2e 0d    ...            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 8306: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc dispatch_nmi_error                                            ; 8309: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 830b: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda l0d2f                                                         ; 830e: ad 2f 0d    ./.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 8311: 8d a2 fe    ...            ; Write dest net byte to FIFO
    lda #&1b                                                          ; 8314: a9 1b       ..             ; Install handler at &831B (write src addr)
    ldy #&83                                                          ; 8316: a0 83       ..             ; High byte of nmi_ack_tx_src
    jmp set_nmi_vector                                                ; 8318: 4c 0e 0d    L..            ; Set NMI vector to ack_tx_src handler

; ***************************************************************************************
; NMI handler: transmit source address in
; ACK frame. Write our station ID and
; network=0 to TX FIFO.
; ***************************************************************************************
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 831b: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 831e: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc dispatch_nmi_error                                            ; 8321: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 8323: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 8326: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 8328: 8d a2 fe    ...            ; Write network=0 (local) to TX FIFO
    lda rx_src_net                                                    ; 832b: ad 3e 0d    .>.            ; Check tx_flags for data phase
    bmi start_data_tx                                                 ; 832e: 30 0e       0.             ; bit7 set: start data TX phase
    lda #&3f ; '?'                                                    ; 8330: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
; ***************************************************************************************
; NMI handler after ACK frame sent.
; Reset ADLC and copy scout data to the
; receive control block buffer.
; ***************************************************************************************
.post_ack_scout
    sta econet_control23_or_status2                                   ; 8332: 8d a1 fe    ...            ; Write CR2 to clear status after ACK TX
    lda l0d43                                                         ; 8335: ad 43 0d    .C.            ; Install saved handler from &0D4B/&0D4C
    ldy l0d44                                                         ; 8338: ac 44 0d    .D.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 833b: 4c 0e 0d    L..            ; Install next NMI handler

; &833e referenced 1 time by &832e
.start_data_tx
    jmp data_tx_begin                                                 ; 833e: 4c c7 87    L..            ; Jump to start data TX phase

; &8341 referenced 2 times by &8309, &8321
.dispatch_nmi_error
    jmp nmi_error_dispatch                                            ; 8341: 4c 2b 82    L+.            ; Jump to error handler; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.

; ***************************************************************************************
; Update RXCB buffer pointer and length
; after data reception. Handle page
; boundary crossings and Tube transfers.
; ***************************************************************************************
; &8344 referenced 2 times by &82e9, &839a
.advance_rx_buffer_ptr
    lda #2                                                            ; 8344: a9 02       ..             ; A=2: test bit1 of tx_flags
    bit rx_src_net                                                    ; 8346: 2c 3e 0d    ,>.            ; BIT tx_flags: check data transfer bit
    beq return_rx_complete                                            ; 8349: f0 3f       .?             ; Bit1 clear: no transfer -- return
    clc                                                               ; 834b: 18          .              ; CLC: init carry for 4-byte add
    php                                                               ; 834c: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 834d: a0 08       ..             ; Y=8: RXCB high pointer offset
; &834f referenced 1 time by &835b
.add_rxcb_ptr
    lda (port_ws_offset),y                                            ; 834f: b1 a6       ..             ; Load RXCB[Y] (buffer pointer byte)
    plp                                                               ; 8351: 28          (              ; Restore carry from stack
    adc net_tx_ptr,y                                                  ; 8352: 79 9a 00    y..            ; Add transfer count byte
    sta (port_ws_offset),y                                            ; 8355: 91 a6       ..             ; Store updated pointer back to RXCB
    iny                                                               ; 8357: c8          .              ; Next byte
    php                                                               ; 8358: 08          .              ; Save carry for next iteration
    cpy #&0c                                                          ; 8359: c0 0c       ..             ; Done 4 bytes? (Y reaches &0C)
    bcc add_rxcb_ptr                                                  ; 835b: 90 f2       ..             ; No: continue adding
    plp                                                               ; 835d: 28          (              ; Discard final carry
    lda #&20 ; ' '                                                    ; 835e: a9 20       .              ; A=&20: test bit5 of tx_flags
    bit rx_src_net                                                    ; 8360: 2c 3e 0d    ,>.            ; BIT tx_flags: check Tube bit
    beq skip_tube_update                                              ; 8363: f0 23       .#             ; No Tube: skip Tube update
    txa                                                               ; 8365: 8a          .              ; Save X on stack
    pha                                                               ; 8366: 48          H              ; Push X
    lda #8                                                            ; 8367: a9 08       ..             ; A=8: offset for Tube address
    clc                                                               ; 8369: 18          .              ; CLC for address calculation
    adc port_ws_offset                                                ; 836a: 65 a6       e.             ; Add workspace base offset
    tax                                                               ; 836c: aa          .              ; X = address low for Tube claim
    ldy rx_buf_offset                                                 ; 836d: a4 a7       ..             ; Y = address high for Tube claim
    lda #1                                                            ; 836f: a9 01       ..             ; A=1: Tube claim type (read)
    jsr tube_addr_data_dispatch                                       ; 8371: 20 06 04     ..            ; Claim Tube address for transfer
    lda l0d42                                                         ; 8374: ad 42 0d    .B.            ; Load extra RX data byte
    sta tube_data_register_3                                          ; 8377: 8d e5 fe    ...            ; Send to Tube via R3
    sec                                                               ; 837a: 38          8              ; SEC: init carry for increment
    ldy #8                                                            ; 837b: a0 08       ..             ; Y=8: start at high pointer
; &837d referenced 1 time by &8384
.inc_rxcb_ptr
    lda #0                                                            ; 837d: a9 00       ..             ; A=0: add carry only (increment)
    adc (port_ws_offset),y                                            ; 837f: 71 a6       q.             ; Add carry to pointer byte
    sta (port_ws_offset),y                                            ; 8381: 91 a6       ..             ; Store back to RXCB
    iny                                                               ; 8383: c8          .              ; Next byte
    bcs inc_rxcb_ptr                                                  ; 8384: b0 f7       ..             ; Keep going while carry propagates
    pla                                                               ; 8386: 68          h              ; Restore X from stack
    tax                                                               ; 8387: aa          .              ; Transfer to X register
; &8388 referenced 1 time by &8363
.skip_tube_update
    lda #&ff                                                          ; 8388: a9 ff       ..             ; A=&FF: return value (transfer done)
; &838a referenced 1 time by &8349
.return_rx_complete
    rts                                                               ; 838a: 60          `              ; Return

    lda l0d31                                                         ; 838b: ad 31 0d    .1.            ; Load received port byte
    bne rx_complete_update_rxcb                                       ; 838e: d0 0a       ..             ; Port != 0: data transfer frame; Mark receive control block as complete.
; Update buffer pointer and remaining
; length, clear flag byte.
    ldy l0d30                                                         ; 8390: ac 30 0d    .0.            ; Port=0: load control byte
    cpy #&82                                                          ; 8393: c0 82       ..             ; Ctrl = &82 (POKE)?
    beq rx_complete_update_rxcb                                       ; 8395: f0 03       ..             ; Yes: POKE also needs data transfer; Mark receive control block as complete.
; Update buffer pointer and remaining
; length, clear flag byte.
    jmp imm_op_build_reply                                            ; 8397: 4c ec 84    L..            ; Other port-0 ops: immediate dispatch; Build reply header for immediate operation.
; Store data offset, source station/network
; in RX buffer, then configure shift register
; for CB1-driven TX completion callback.

; ***************************************************************************************
; Mark receive control block as complete.
; Update buffer pointer and remaining
; length, clear flag byte.
; ***************************************************************************************
; &839a referenced 3 times by &838e, &8395, &842a
.rx_complete_update_rxcb
    jsr advance_rx_buffer_ptr                                         ; 839a: 20 44 83     D.            ; Update buffer pointer and check for Tube; Update RXCB buffer pointer and length
; after data reception. Handle page
; boundary crossings and Tube transfers.
    bne skip_buf_ptr_update                                           ; 839d: d0 12       ..             ; Transfer not done: skip buffer update
.add_buf_to_base
    lda port_buf_len                                                  ; 839f: a5 a2       ..             ; Load buffer bytes remaining
    clc                                                               ; 83a1: 18          .              ; CLC for address add
    adc open_port_buf                                                 ; 83a2: 65 a4       e.             ; Add to buffer base address
    bcc store_buf_ptr_lo                                              ; 83a4: 90 02       ..             ; No carry: skip high byte increment
.inc_rxcb_buf_hi
    inc open_port_buf_hi                                              ; 83a6: e6 a5       ..             ; Carry: increment buffer high byte
; &83a8 referenced 1 time by &83a4
.store_buf_ptr_lo
    ldy #8                                                            ; 83a8: a0 08       ..             ; Y=8: store updated buffer position
.store_rxcb_buf_ptr
    sta (port_ws_offset),y                                            ; 83aa: 91 a6       ..             ; Store updated low byte to RXCB
    iny                                                               ; 83ac: c8          .              ; Y=9: buffer high byte offset
    lda open_port_buf_hi                                              ; 83ad: a5 a5       ..             ; Load updated buffer high byte
.store_rxcb_buf_hi
    sta (port_ws_offset),y                                            ; 83af: 91 a6       ..             ; Store high byte to RXCB
; &83b1 referenced 1 time by &839d
.skip_buf_ptr_update
    lda l0d31                                                         ; 83b1: ad 31 0d    .1.            ; Check port byte again
    beq discard_reset_rx                                              ; 83b4: f0 35       .5             ; Port=0: immediate op, discard+listen
    lda l0d2f                                                         ; 83b6: ad 2f 0d    ./.            ; Load source network from scout buffer
    ldy #3                                                            ; 83b9: a0 03       ..             ; Y=3: RXCB source network offset
    sta (port_ws_offset),y                                            ; 83bb: 91 a6       ..             ; Store source network to RXCB
    dey                                                               ; 83bd: 88          .              ; Y=2: source station offset; Y=&02
    lda l0d2e                                                         ; 83be: ad 2e 0d    ...            ; Load source station from scout buffer
    sta (port_ws_offset),y                                            ; 83c1: 91 a6       ..             ; Store source station to RXCB
    dey                                                               ; 83c3: 88          .              ; Y=1: port byte offset; Y=&01
    lda l0d31                                                         ; 83c4: ad 31 0d    .1.            ; Load port byte
    sta (port_ws_offset),y                                            ; 83c7: 91 a6       ..             ; Store port to RXCB
    dey                                                               ; 83c9: 88          .              ; Y=0: control/flag byte offset; Y=&00
    lda l0d30                                                         ; 83ca: ad 30 0d    .0.            ; Load control byte from scout
    ora #&80                                                          ; 83cd: 09 80       ..             ; Set bit7 = reception complete flag
    sta (port_ws_offset),y                                            ; 83cf: 91 a6       ..             ; Store to RXCB (marks CB as complete)
    lda l0d6c                                                         ; 83d1: ad 6c 0d    .l.            ; Load callback event flags
    ror a                                                             ; 83d4: 6a          j              ; Shift bit 0 into carry
    bcc discard_reset_rx                                              ; 83d5: 90 14       ..             ; Bit 0 clear: no callback, skip to reset
    sec                                                               ; 83d7: 38          8              ; Set carry for subtraction
    lda port_ws_offset                                                ; 83d8: a5 a6       ..             ; Load RXCB workspace pointer low byte
; &83da referenced 1 time by &83dd
.loop_c83da
    iny                                                               ; 83da: c8          .              ; Count slots
    sbc #&0c                                                          ; 83db: e9 0c       ..             ; Subtract 12 bytes per RXCB slot
    bcs loop_c83da                                                    ; 83dd: b0 fb       ..             ; Loop until pointer exhausted
    dey                                                               ; 83df: 88          .              ; Adjust for off-by-one
    cpy #3                                                            ; 83e0: c0 03       ..             ; Check slot index >= 3
    bcc discard_reset_rx                                              ; 83e2: 90 07       ..             ; Slot < 3: no callback, skip to reset
    jsr discard_reset_listen                                          ; 83e4: 20 f8 83     ..            ; Discard current frame. Reset ADLC
; to listen mode and return.
    tya                                                               ; 83e7: 98          .              ; Pass slot index as callback parameter
    jmp setup_cb1_sr_tx                                               ; 83e8: 4c 05 85    L..            ; Jump to TX completion with slot index

; &83eb referenced 6 times by &8236, &83b4, &83d5, &83e2, &886b, &88d5
.discard_reset_rx
    jsr discard_reset_listen                                          ; 83eb: 20 f8 83     ..            ; Discard current frame. Reset ADLC
; to listen mode and return.
; &83ee referenced 3 times by &80ff, &8466, &8522
.reset_adlc_rx_listen
    jsr adlc_rx_listen                                                ; 83ee: 20 6e 89     n.            ; Configure ADLC for receive/listen mode.
; TX held in reset, RX interrupts enabled,
; status flags cleared.
; &83f1 referenced 2 times by &80e3, &80fc
.set_nmi_rx_scout
    lda #&b3                                                          ; 83f1: a9 b3       ..             ; A=&B3: low byte of nmi_rx_scout
    ldy #&80                                                          ; 83f3: a0 80       ..             ; Y=&80: high byte of nmi_rx_scout
    jmp set_nmi_vector                                                ; 83f5: 4c 0e 0d    L..            ; Install nmi_rx_scout as NMI handler

; ***************************************************************************************
; Discard current frame. Reset ADLC
; to listen mode and return.
; ***************************************************************************************
; &83f8 referenced 2 times by &83e4, &83eb
.discard_reset_listen
    lda #2                                                            ; 83f8: a9 02       ..             ; Tube flag bit 1 AND tx_flags bit 1
    and l0d63                                                         ; 83fa: 2d 63 0d    -c.            ; Check if Tube transfer active
; &83fd referenced 1 time by &846e
.test_tube_release
    bit rx_src_net                                                    ; 83fd: 2c 3e 0d    ,>.            ; Test tx_flags for Tube transfer
    beq return_2                                                      ; 8400: f0 03       ..             ; No Tube transfer active -- skip release
    jsr release_tube                                                  ; 8402: 20 3f 84     ?.            ; Release Tube claim before discarding; Release the Tube address claim if one is
; held. Clear the release-needed flag.
; &8405 referenced 1 time by &8400
.return_2
    rts                                                               ; 8405: 60          `              ; Return

; ***************************************************************************************
; Copy received scout data into the RXCB
; buffer. Handle both direct RAM and Tube
; transfer paths.
; ***************************************************************************************
; &8406 referenced 1 time by &81be
.copy_scout_to_buffer
    txa                                                               ; 8406: 8a          .              ; Save X on stack
    pha                                                               ; 8407: 48          H              ; Push X
    ldx #4                                                            ; 8408: a2 04       ..             ; X=4: start at scout byte offset 4
    lda #2                                                            ; 840a: a9 02       ..             ; A=2: Tube transfer check mask
.copy_scout_select
    bit rx_src_net                                                    ; 840c: 2c 3e 0d    ,>.            ; BIT tx_flags: check Tube bit
    bne copy_scout_via_tube                                           ; 840f: d0 1c       ..             ; Tube active: use R3 write path
    ldy port_buf_len                                                  ; 8411: a4 a2       ..             ; Y = current buffer position
; &8413 referenced 1 time by &8426
.copy_scout_bytes
    lda l0d2e,x                                                       ; 8413: bd 2e 0d    ...            ; Load scout data byte
    sta (open_port_buf),y                                             ; 8416: 91 a4       ..             ; Store to port buffer
    iny                                                               ; 8418: c8          .              ; Advance buffer pointer
    bne next_scout_byte                                               ; 8419: d0 06       ..             ; No page crossing
    inc open_port_buf_hi                                              ; 841b: e6 a5       ..             ; Page crossing: inc buffer high byte
    dec port_buf_len_hi                                               ; 841d: c6 a3       ..             ; Decrement remaining page count
    beq scout_page_overflow                                           ; 841f: f0 52       .R             ; No pages left: overflow
; &8421 referenced 1 time by &8419
.next_scout_byte
    inx                                                               ; 8421: e8          .              ; Next scout data byte
    sty port_buf_len                                                  ; 8422: 84 a2       ..             ; Save updated buffer position
    cpx #&0c                                                          ; 8424: e0 0c       ..             ; Done all scout data? (X reaches &0C)
    bne copy_scout_bytes                                              ; 8426: d0 eb       ..             ; No: continue copying
; &8428 referenced 2 times by &843d, &8477
.scout_copy_done
    pla                                                               ; 8428: 68          h              ; Restore X from stack
    tax                                                               ; 8429: aa          .              ; Transfer to X register
    jmp rx_complete_update_rxcb                                       ; 842a: 4c 9a 83    L..            ; Jump to completion handler; Mark receive control block as complete.
; Update buffer pointer and remaining
; length, clear flag byte.

; &842d referenced 2 times by &840f, &843b
.copy_scout_via_tube
    lda l0d2e,x                                                       ; 842d: bd 2e 0d    ...            ; Tube path: load scout data byte
    sta tube_data_register_3                                          ; 8430: 8d e5 fe    ...            ; Send byte to Tube via R3
    jsr advance_buffer_ptr                                            ; 8433: 20 25 85     %.            ; Increment buffer position counters; Increment the 4-byte buffer pointer at
; port_buf_len/open_port_buf (&A2-&A5)
; by one. Used to advance the RX data
; write position after storing a byte.
    beq check_scout_done                                              ; 8436: f0 3d       .=             ; Counter overflow: handle end of buffer
    inx                                                               ; 8438: e8          .              ; Next scout data byte
    cpx #&0c                                                          ; 8439: e0 0c       ..             ; Done all scout data?
    bne copy_scout_via_tube                                           ; 843b: d0 f0       ..             ; No: continue Tube writes
    beq scout_copy_done                                               ; 843d: f0 e9       ..             ; ALWAYS branch

; ***************************************************************************************
; Release the Tube address claim if one is
; held. Clear the release-needed flag.
; ***************************************************************************************
; &843f referenced 2 times by &8402, &8934
.release_tube
    bit need_release_tube                                             ; 843f: 24 98       $.             ; Check if Tube needs releasing
    bmi clear_release_flag                                            ; 8441: 30 05       0.             ; Bit7 set: already released
    lda #&82                                                          ; 8443: a9 82       ..             ; A=&82: Tube release claim type
    jsr tube_addr_data_dispatch                                       ; 8445: 20 06 04     ..            ; Release Tube address claim
; &8448 referenced 1 time by &8441
.clear_release_flag
    lsr need_release_tube                                             ; 8448: 46 98       F.             ; Clear release flag (LSR clears bit7)
    rts                                                               ; 844a: 60          `              ; Return

; ***************************************************************************************
; Discard frame after ADLC reset. Wait for
; idle line, then restore listen mode and
; dispatch any pending immediate operations.
; ***************************************************************************************
; &844b referenced 1 time by &8152
.discard_after_reset
    ldy l0d30                                                         ; 844b: ac 30 0d    .0.            ; Control byte &81-&88 range check
    cpy #&81                                                          ; 844e: c0 81       ..             ; Below &81: not an immediate op
    bcc imm_op_out_of_range                                           ; 8450: 90 29       .)             ; Out of range low: jump to discard
    cpy #&89                                                          ; 8452: c0 89       ..             ; Above &88: not an immediate op
    bcs imm_op_out_of_range                                           ; 8454: b0 25       .%             ; Out of range high: jump to discard
    cpy #&87                                                          ; 8456: c0 87       ..             ; HALT(&87)/CONTINUE(&88) skip protection
    bcs dispatch_imm_op                                               ; 8458: b0 0e       ..             ; Ctrl >= &87: dispatch without mask check
    tya                                                               ; 845a: 98          .              ; Convert ctrl byte to 0-based index for mask
    sec                                                               ; 845b: 38          8              ; SEC for subtract
    sbc #&81                                                          ; 845c: e9 81       ..             ; A = ctrl - &81 (0-based operation index)
    tay                                                               ; 845e: a8          .              ; Y = index for mask rotation count
    lda ws_0d68                                                       ; 845f: ad 68 0d    .h.            ; Load protection mask from LSTAT
; &8462 referenced 1 time by &8464
.rotate_prot_mask
    ror a                                                             ; 8462: 6a          j              ; Rotate mask right by control byte index
    dey                                                               ; 8463: 88          .              ; Decrement rotation counter
    bpl rotate_prot_mask                                              ; 8464: 10 fc       ..             ; Loop until bit aligned
    bcs reset_adlc_rx_listen                                          ; 8466: b0 86       ..             ; Bit set = operation disabled, discard
; &8468 referenced 1 time by &8458
.dispatch_imm_op
    ldy l0d30                                                         ; 8468: ac 30 0d    .0.            ; Reload ctrl byte for dispatch table
    lda #&84                                                          ; 846b: a9 84       ..             ; PHA hi byte / PHA lo byte / RTS dispatch
    pha                                                               ; 846d: 48          H              ; Push &9A as dispatch high byte
    lda test_tube_release,y                                           ; 846e: b9 fd 83    ...            ; Load handler low byte from jump table
    pha                                                               ; 8471: 48          H              ; Push handler low byte
    rts                                                               ; 8472: 60          `              ; RTS dispatches to handler

; &8473 referenced 1 time by &841f
.scout_page_overflow
    inc port_buf_len                                                  ; 8473: e6 a2       ..             ; Increment port buffer length
; &8475 referenced 1 time by &8436
.check_scout_done
    cpx #&0b                                                          ; 8475: e0 0b       ..             ; Check if scout data index reached 11
    beq scout_copy_done                                               ; 8477: f0 af       ..             ; Yes: loop back to continue reading
    pla                                                               ; 8479: 68          h              ; Restore A from stack
    tax                                                               ; 847a: aa          .              ; Transfer to X
; &847b referenced 2 times by &8450, &8454
.imm_op_out_of_range
    jmp nmi_error_dispatch                                            ; 847b: 4c 2b 82    L+.            ; Jump to discard handler; NMI error handler dispatch. Route to
; receive error or transmit error based on
; SR1 flags.

    cpy #&a3                                                          ; 847e: c0 a3       ..
    sta l0085                                                         ; 8480: 85 85       ..
    sta l00da                                                         ; 8482: 85 da       ..
    equb &da, &ae, &a9,   0, &85, &a4, &a9, &82, &85, &a2, &a9, 1     ; 8484: da ae a9... ...            ; Set port buffer lo; Buffer length lo = &82; Set buffer length lo; Buffer length hi = 1
    equb &85, &a3, &a5, &9d, &85, &a5, &a0,   1                       ; 8490: 85 a3 a5... ...            ; Set buffer length hi; Load RX page hi for buffer; Set port buffer hi; Y=3: copy 4 bytes (3 down to 0)
.copy_addr_loop
    equb &b9, &32, &0d, &99, &66, &0d, &88, &10, &f7, &4c             ; 8498: b9 32 0d... .2.            ; Load remote address byte; Store to exec address workspace; Next byte (descending); Loop until all 4 bytes copied; Enter common data-receive path
.svc5_dispatch_lo
    equb &c1, &81                                                     ; 84a2: c1 81       ..             ; Svc 5 dispatch table low bytes
.rx_imm_poke
    equb &a9, &2e, &85, &a6, &a9, &0d, &85, &a7, &4c, &af, &81        ; 84a4: a9 2e 85... ...            ; Port workspace offset = &3D; Store workspace offset lo; RX buffer page = &0D; Store workspace offset hi; Enter POKE data-receive path
.rx_imm_machine_type
    equb &a9, 1                                                       ; 84af: a9 01       ..             ; Buffer length hi = 1

; &84b1 referenced 1 time by &8064
.set_rx_buf_len_hi
    sta port_buf_len_hi                                               ; 84b1: 85 a3       ..             ; Set buffer length hi
    lda #&fc                                                          ; 84b3: a9 fc       ..             ; Buffer length lo = &FC
    sta port_buf_len                                                  ; 84b5: 85 a2       ..             ; Set buffer length lo
    lda #&c1                                                          ; 84b7: a9 c1       ..             ; Buffer start lo = &25
    sta open_port_buf                                                 ; 84b9: 85 a4       ..             ; Set port buffer lo
    lda #&88                                                          ; 84bb: a9 88       ..             ; Buffer hi = &7F (below screen)
    sta open_port_buf_hi                                              ; 84bd: 85 a5       ..             ; Set port buffer hi
    bne set_tx_reply_flag                                             ; 84bf: d0 12       ..             ; ALWAYS branch

.rx_imm_peek
    lda #&2e ; '.'                                                    ; 84c1: a9 2e       ..             ; Port workspace offset = &3D
    sta port_ws_offset                                                ; 84c3: 85 a6       ..             ; Store workspace offset lo
    lda #&0d                                                          ; 84c5: a9 0d       ..             ; RX buffer page = &0D
    sta rx_buf_offset                                                 ; 84c7: 85 a7       ..             ; Store workspace offset hi
    lda #2                                                            ; 84c9: a9 02       ..             ; Scout status = 2 (PEEK response)
    sta rx_port                                                       ; 84cb: 8d 40 0d    .@.            ; Store scout status
    jsr tx_calc_transfer                                              ; 84ce: 20 e8 88     ..            ; Calculate transfer size for response; Calculate transfer size for data phase.
; Compute byte count from buffer start/end
; pointers in the TX control block.
    bcc imm_op_discard                                                ; 84d1: 90 4f       .O             ; C=0: transfer not set up, discard
; &84d3 referenced 1 time by &84bf
.set_tx_reply_flag
    lda rx_src_net                                                    ; 84d3: ad 3e 0d    .>.            ; Mark TX flags bit 7 (reply pending)
    ora #&80                                                          ; 84d6: 09 80       ..             ; Set reply pending flag
    sta rx_src_net                                                    ; 84d8: 8d 3e 0d    .>.            ; Store updated TX flags
.rx_imm_halt_cont
    lda #&44 ; 'D'                                                    ; 84db: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    sta econet_control1_or_status1                                    ; 84dd: 8d a0 fe    ...            ; Write CR1: enable TX interrupts
.tx_cr2_setup
    lda #&a7                                                          ; 84e0: a9 a7       ..             ; NMI handler hi byte (self-modifying)
    sta econet_control23_or_status2                                   ; 84e2: 8d a1 fe    ...            ; Write CR2 for TX setup
.tx_nmi_setup
    lda #2                                                            ; 84e5: a9 02       ..             ; NMI handler lo byte (self-modifying)
    ldy #&85                                                          ; 84e7: a0 85       ..             ; Y=&9B: dispatch table page
    jmp ack_tx_write_dest                                             ; 84e9: 4c fd 82    L..            ; Acknowledge and write TX dest

; ***************************************************************************************
; Build reply header for immediate operation.
; Store data offset, source station/network
; in RX buffer, then configure shift register
; for CB1-driven TX completion callback.
; ***************************************************************************************
; &84ec referenced 1 time by &8397
.imm_op_build_reply
    lda port_buf_len                                                  ; 84ec: a5 a2       ..             ; Get buffer position for reply header
    clc                                                               ; 84ee: 18          .              ; Clear carry for offset addition
    adc #&80                                                          ; 84ef: 69 80       i.             ; Data offset = buf_len + &80 (past header)
    ldy #&7f                                                          ; 84f1: a0 7f       ..             ; Y=&7F: reply data length slot
    sta (net_rx_ptr),y                                                ; 84f3: 91 9c       ..             ; Store reply data length in RX buffer
    ldy #&80                                                          ; 84f5: a0 80       ..             ; Y=&80: source station slot
    lda l0d2e                                                         ; 84f7: ad 2e 0d    ...            ; Load requesting station number
    sta (net_rx_ptr),y                                                ; 84fa: 91 9c       ..             ; Store source station in reply header
    iny                                                               ; 84fc: c8          .              ; Y=&81
    lda l0d2f                                                         ; 84fd: ad 2f 0d    ./.            ; Load requesting network number
    sta (net_rx_ptr),y                                                ; 8500: 91 9c       ..             ; Store source network in reply header
    lda l0d30                                                         ; 8502: ad 30 0d    .0.            ; Load control byte from received frame
; &8505 referenced 1 time by &83e8
.setup_cb1_sr_tx
    sta ws_0d65                                                       ; 8505: 8d 65 0d    .e.            ; Save ctrl byte for TX response
    lda #&84                                                          ; 8508: a9 84       ..             ; IER bit 2: disable CB1 interrupt
    sta system_via_ier                                                ; 850a: 8d 4e fe    .N.            ; Write IER to disable CB1
    lda system_via_acr                                                ; 850d: ad 4b fe    .K.            ; Read ACR for shift register config
    and #&1c                                                          ; 8510: 29 1c       ).             ; Isolate shift register mode bits (2-4)
    sta ws_0d64                                                       ; 8512: 8d 64 0d    .d.            ; Save original SR mode for later restore
    lda system_via_acr                                                ; 8515: ad 4b fe    .K.            ; Reload ACR for modification
    and #&e3                                                          ; 8518: 29 e3       ).             ; Clear SR mode bits (keep other bits)
    ora #8                                                            ; 851a: 09 08       ..             ; SR mode 4: shift out under CB1 control
    sta system_via_acr                                                ; 851c: 8d 4b fe    .K.            ; Apply new shift register mode
    bit system_via_sr                                                 ; 851f: 2c 4a fe    ,J.            ; Read SR to clear pending interrupt
; &8522 referenced 1 time by &84d1
.imm_op_discard
    jmp reset_adlc_rx_listen                                          ; 8522: 4c ee 83    L..            ; Return to idle listen mode

; ***************************************************************************************
; Increment the 4-byte buffer pointer at
; port_buf_len/open_port_buf (&A2-&A5)
; by one. Used to advance the RX data
; write position after storing a byte.
; ***************************************************************************************
; &8525 referenced 3 times by &829e, &82ac, &8433
.advance_buffer_ptr
    inc port_buf_len                                                  ; 8525: e6 a2       ..             ; Increment buffer length low byte
    bne return_3                                                      ; 8527: d0 0a       ..             ; No overflow: done
    inc port_buf_len_hi                                               ; 8529: e6 a3       ..             ; Increment buffer length high byte
    bne return_3                                                      ; 852b: d0 06       ..             ; No overflow: done
    inc open_port_buf                                                 ; 852d: e6 a4       ..             ; Increment buffer pointer low byte
    bne return_3                                                      ; 852f: d0 02       ..             ; No overflow: done
    inc open_port_buf_hi                                              ; 8531: e6 a5       ..             ; Increment buffer pointer high byte
; &8533 referenced 3 times by &8527, &852b, &852f
.return_3
    rts                                                               ; 8533: 60          `              ; Return

    equs "8AO[r"                                                      ; 8534: 38 41 4f... 8AO
.tx_done_jsr
    equb &a9, &85, &48, &a9                                           ; 8539: a9 85 48... ..H            ; Push hi byte on stack; Push lo of (tx_done_exit-1)
    equs "zHlf"                                                       ; 853d: 7a 48 6c... zHl            ; Push lo byte on stack; Call remote JSR; RTS to tx_done_exit
    equb &0d, &ae, &66, &0d, &ad, &67, &0d, &a0, 8                    ; 8541: 0d ae 66... ..f            ; ORA opcode (dead code / data overlap); X = remote address lo; A = remote address hi

; &854a referenced 1 time by &804f
.tx_done_fire_event
    jsr oseven                                                        ; 854a: 20 bf ff     ..            ; Generate event Y
    jmp tx_done_exit                                                  ; 854d: 4c 7b 85    L{.            ; Exit TX done handler

.tx_done_os_proc
    equb &ae, &66, &0d, &ac, &67, &0d, &20, &2d, &8e, &4c, &7b, &85   ; 8550: ae 66 0d... .f.            ; X = remote address lo; Y = remote address hi; Call ROM entry point at &8000; Exit TX done handler
.tx_done_halt
    equb &a9,   4, &2c, &61, &0d, &d0, &18, &0d, &61, &0d, &8d, &61   ; 855c: a9 04 2c... ..,            ; A=&04: bit 2 mask for rx_flags; Test if already halted; Already halted: skip to exit; Set bit 2 in rx_flags; Store halt flag
    equb &0d, &a9,   4, &58                                           ; 8568: 0d a9 04... ...            ; A=4: re-load halt bit mask; Enable interrupts during halt wait
.halt_spin_loop
    equb &2c, &61, &0d, &d0, &fb, &f0, 8                              ; 856c: 2c 61 0d... ,a.            ; Test halt flag; Still halted: keep spinning
.tx_done_continue
    equb &ad, &61, &0d, &29, &fb, &8d, &61, &0d                       ; 8573: ad 61 0d... .a.            ; Load current RX flags; Clear bit 2: release halted station; Store updated flags

; &857b referenced 1 time by &854d
.tx_done_exit
    pla                                                               ; 857b: 68          h              ; Restore Y from stack
    tay                                                               ; 857c: a8          .              ; Transfer to Y register
    pla                                                               ; 857d: 68          h              ; Restore X from stack
    tax                                                               ; 857e: aa          .              ; Transfer to X register
    lda #0                                                            ; 857f: a9 00       ..             ; A=0: success status
    rts                                                               ; 8581: 60          `              ; Return with A=0 (success)

; ***************************************************************************************
; Begin Econet transmission. Copy dest
; station/network from TX control block,
; set up immediate op params, poll for idle
; line before starting frame.
; ***************************************************************************************
; &8582 referenced 3 times by &98c1, &a5a5, &a89d
.tx_begin
    txa                                                               ; 8582: 8a          .              ; Save X on stack
    pha                                                               ; 8583: 48          H              ; Push X
    ldy #2                                                            ; 8584: a0 02       ..             ; Y=2: TXCB offset for dest station
    lda (nmi_tx_block),y                                              ; 8586: b1 a0       ..             ; Load dest station from TX control block
    sta tx_dst_stn                                                    ; 8588: 8d 20 0d    . .            ; Store to TX scout buffer
    iny                                                               ; 858b: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 858c: b1 a0       ..             ; Load dest network from TX control block
    sta tx_dst_net                                                    ; 858e: 8d 21 0d    .!.            ; Store to TX scout buffer
    ldy #0                                                            ; 8591: a0 00       ..             ; Y=0: first byte of TX control block
    lda (nmi_tx_block),y                                              ; 8593: b1 a0       ..             ; Load control/flag byte
    bmi tx_imm_op_setup                                               ; 8595: 30 03       0.             ; Bit7 set: immediate operation ctrl byte
    jmp tx_active_start                                               ; 8597: 4c 25 86    L%.            ; Bit7 clear: normal data transfer

; &859a referenced 1 time by &8595
.tx_imm_op_setup
    sta tx_ctrl_byte                                                  ; 859a: 8d 24 0d    .$.            ; Store control byte to TX scout buffer
    tax                                                               ; 859d: aa          .              ; X = control byte for range checks
    iny                                                               ; 859e: c8          .              ; Y=1: port byte offset
    lda (nmi_tx_block),y                                              ; 859f: b1 a0       ..             ; Load port byte from TX control block
    sta tx_port                                                       ; 85a1: 8d 25 0d    .%.            ; Store port byte to TX scout buffer
    bne tx_line_idle_check                                            ; 85a4: d0 33       .3             ; Port != 0: skip immediate op setup
    cpx #&83                                                          ; 85a6: e0 83       ..             ; Ctrl < &83: PEEK/POKE need address calc
    bcs tx_ctrl_range_check                                           ; 85a8: b0 1b       ..             ; Ctrl >= &83: skip to range check
    sec                                                               ; 85aa: 38          8              ; SEC: init borrow for 4-byte subtract
    php                                                               ; 85ab: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 85ac: a0 08       ..             ; Y=8: high pointer offset in TXCB
; &85ae referenced 1 time by &85c2
.calc_peek_poke_size
    lda (nmi_tx_block),y                                              ; 85ae: b1 a0       ..             ; Load TXCB[Y] (end addr byte)
    dey                                                               ; 85b0: 88          .              ; Y -= 4: back to start addr offset
    dey                                                               ; 85b1: 88          .              ; (Y -= 4: reach start addr offset)
    dey                                                               ; 85b2: 88          .              ; (continued)
    dey                                                               ; 85b3: 88          .              ; (continued)
    plp                                                               ; 85b4: 28          (              ; Restore borrow from stack
    sbc (nmi_tx_block),y                                              ; 85b5: f1 a0       ..             ; end - start = transfer size byte
    sta tx_data_start,y                                               ; 85b7: 99 26 0d    .&.            ; Store result to tx_data_start
    iny                                                               ; 85ba: c8          .              ; (Y += 5: advance to next end byte)
    iny                                                               ; 85bb: c8          .              ; (continued)
    iny                                                               ; 85bc: c8          .              ; (continued)
    iny                                                               ; 85bd: c8          .              ; (continued)
    iny                                                               ; 85be: c8          .              ; (continued)
    php                                                               ; 85bf: 08          .              ; Save borrow for next byte
    cpy #&0c                                                          ; 85c0: c0 0c       ..             ; Done all 4 bytes? (Y reaches &0C)
    bcc calc_peek_poke_size                                           ; 85c2: 90 ea       ..             ; No: next byte pair
    plp                                                               ; 85c4: 28          (              ; Discard final borrow
; &85c5 referenced 1 time by &85a8
.tx_ctrl_range_check
    cpx #&81                                                          ; 85c5: e0 81       ..             ; Ctrl < &81: not an immediate op
    bcc tx_active_start                                               ; 85c7: 90 5c       .\             ; Below range: normal data transfer
.check_imm_range
    cpx #&89                                                          ; 85c9: e0 89       ..             ; Ctrl >= &89: out of immediate range
    bcs tx_active_start                                               ; 85cb: b0 58       .X             ; Above range: normal data transfer
    ldy #&0c                                                          ; 85cd: a0 0c       ..             ; Y=&0C: start of extra data in TXCB
; &85cf referenced 1 time by &85d7
.copy_imm_params
    lda (nmi_tx_block),y                                              ; 85cf: b1 a0       ..             ; Load extra parameter byte from TXCB
    sta l0d1a,y                                                       ; 85d1: 99 1a 0d    ...            ; Copy to NMI shim workspace at &0D1A+Y
    iny                                                               ; 85d4: c8          .              ; Next byte
    cpy #&10                                                          ; 85d5: c0 10       ..             ; Done 4 bytes? (Y reaches &10)
    bcc copy_imm_params                                               ; 85d7: 90 f6       ..             ; No: continue copying
; &85d9 referenced 1 time by &85a4
.tx_line_idle_check
    lda #&20 ; ' '                                                    ; 85d9: a9 20       .              ; A=&20: mask for SR2 INACTIVE bit
    bit econet_control23_or_status2                                   ; 85db: 2c a1 fe    ,..            ; BIT SR2: test if line is idle
    bne tx_no_clock_error                                             ; 85de: d0 55       .U             ; Line not idle: handle as line jammed
    lda #&fd                                                          ; 85e0: a9 fd       ..             ; A=&FD: high byte of timeout counter
    pha                                                               ; 85e2: 48          H              ; Push timeout high byte to stack
    lda #6                                                            ; 85e3: a9 06       ..             ; Scout frame = 6 address+ctrl bytes
    sta rx_ctrl                                                       ; 85e5: 8d 3f 0d    .?.            ; Store scout frame length
    lda #0                                                            ; 85e8: a9 00       ..             ; A=0: init low byte of timeout counter
; ***************************************************************************************
; Init 3-byte timeout counter on the stack
; and begin polling ADLC for line inactive
; before starting transmission.
; ***************************************************************************************
.inactive_poll
    sta rx_remote_addr                                                ; 85ea: 8d 41 0d    .A.            ; Save TX index
    pha                                                               ; 85ed: 48          H              ; Push timeout byte 1 on stack
    pha                                                               ; 85ee: 48          H              ; Push timeout byte 2 on stack
    ldy #&e7                                                          ; 85ef: a0 e7       ..             ; Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &85f1 referenced 3 times by &8617, &861c, &8621
.reload_inactive_mask
    lda #4                                                            ; 85f1: a9 04       ..             ; A=&04: INACTIVE bit mask for SR2 test
.test_inactive_retry
    php                                                               ; 85f3: 08          .              ; Save interrupt state
    sei                                                               ; 85f4: 78          x              ; Disable interrupts for ADLC access
; ***************************************************************************************
; Test Econet line for inactive state with
; interrupts disabled. Poll SR2 INACTIVE bit
; with 3-byte timeout counter on the stack.
; ***************************************************************************************
.intoff_test_inactive
intoff_disable_nmi_op = intoff_test_inactive+1
    bit station_id_disable_net_nmis                                   ; 85f5: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
; &85f6 referenced 1 time by &8672
    bit station_id_disable_net_nmis                                   ; 85f8: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
.test_line_idle
    bit econet_control23_or_status2                                   ; 85fb: 2c a1 fe    ,..            ; BIT SR2: Z = &04 AND SR2 -- tests INACTIVE
    beq inactive_retry                                                ; 85fe: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 8600: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 8603: a9 67       .g             ; CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 8605: 8d a1 fe    ...            ; Write CR2: clear status, prepare TX
    lda #&10                                                          ; 8608: a9 10       ..             ; A=&10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 860a: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 860d: d0 34       .4             ; CTS set -- clock hardware detected, start TX; Prepare ADLC for transmission. Configure
; CR2 for TX mode, write destination address
; bytes to TX FIFO, and install TX data NMI
; handler.
; &860f referenced 1 time by &85fe
.inactive_retry
    bit video_ula_control                                             ; 860f: 2c 20 fe    , .            ; INTON -- re-enable NMIs (&FE20 read)
    plp                                                               ; 8612: 28          (              ; Restore interrupt state
    tsx                                                               ; 8613: ba          .              ; 3-byte timeout counter on stack
    inc error_text,x                                                  ; 8614: fe 01 01    ...            ; Increment timeout counter byte 1
    bne reload_inactive_mask                                          ; 8617: d0 d8       ..             ; Not overflowed: retry INACTIVE test
    inc l0102,x                                                       ; 8619: fe 02 01    ...            ; Increment timeout counter byte 2
    bne reload_inactive_mask                                          ; 861c: d0 d3       ..             ; Not overflowed: retry INACTIVE test
    inc l0103,x                                                       ; 861e: fe 03 01    ...            ; Increment timeout counter byte 3
    bne reload_inactive_mask                                          ; 8621: d0 ce       ..             ; Not overflowed: retry INACTIVE test
    beq tx_line_jammed                                                ; 8623: f0 04       ..             ; Handle line jammed error. Abort TX by
; writing CR2, clean timeout state from
; the stack, and store error &40 in the
; TX control block.; ALWAYS branch

; &8625 referenced 3 times by &8597, &85c7, &85cb
.tx_active_start
    lda #&44 ; 'D'                                                    ; 8625: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    bne store_tx_error                                                ; 8627: d0 0e       ..             ; ALWAYS branch

; ***************************************************************************************
; Handle line jammed error. Abort TX by
; writing CR2, clean timeout state from
; the stack, and store error &40 in the
; TX control block.
; ***************************************************************************************
; &8629 referenced 1 time by &8623
.tx_line_jammed
    lda #7                                                            ; 8629: a9 07       ..             ; CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)
    sta econet_control23_or_status2                                   ; 862b: 8d a1 fe    ...            ; Write CR2 to abort TX
    pla                                                               ; 862e: 68          h              ; Clean 3 bytes of timeout loop state
    pla                                                               ; 862f: 68          h              ; Pop saved register
    pla                                                               ; 8630: 68          h              ; Pop saved register
    lda #&40 ; '@'                                                    ; 8631: a9 40       .@             ; Error &40 = 'Line Jammed'
    bne store_tx_error                                                ; 8633: d0 02       ..             ; ALWAYS branch to shared error handler; ALWAYS branch

; &8635 referenced 1 time by &85de
.tx_no_clock_error
    lda #&43 ; 'C'                                                    ; 8635: a9 43       .C             ; Error &43 = 'No Clock'
; &8637 referenced 2 times by &8627, &8633
.store_tx_error
    ldy #0                                                            ; 8637: a0 00       ..             ; Offset 0 = error byte in TX control block
    sta (nmi_tx_block),y                                              ; 8639: 91 a0       ..             ; Store error code in TX CB byte 0
    lda #&80                                                          ; 863b: a9 80       ..             ; &80 = TX complete flag
    sta ws_0d60                                                       ; 863d: 8d 60 0d    .`.            ; Signal TX operation complete
    pla                                                               ; 8640: 68          h              ; Restore X saved by caller
    tax                                                               ; 8641: aa          .              ; Move to X register
    rts                                                               ; 8642: 60          `              ; Return to TX caller

; ***************************************************************************************
; Prepare ADLC for transmission. Configure
; CR2 for TX mode, write destination address
; bytes to TX FIFO, and install TX data NMI
; handler.
; ***************************************************************************************
; &8643 referenced 1 time by &860d
.tx_prepare
    sty econet_control23_or_status2                                   ; 8643: 8c a1 fe    ...            ; Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
    ldx #&44 ; 'D'                                                    ; 8646: a2 44       .D             ; CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)
    stx econet_control1_or_status1                                    ; 8648: 8e a0 fe    ...            ; Write to ADLC CR1
    ldx #&e0                                                          ; 864b: a2 e0       ..             ; Install NMI handler at &86E0 (TX data handler)
    ldy #&86                                                          ; 864d: a0 86       ..             ; High byte of NMI handler address
    stx nmi_jmp_lo                                                    ; 864f: 8e 0c 0d    ...            ; Write NMI vector low byte directly
    sty nmi_jmp_hi                                                    ; 8652: 8c 0d 0d    ...            ; Write NMI vector high byte directly
    sec                                                               ; 8655: 38          8              ; Set need_release_tube flag (SEC/ROR = bit7)
    ror need_release_tube                                             ; 8656: 66 98       f.             ; Rotate carry into bit 7 of flag
    bit video_ula_control                                             ; 8658: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA (&FE20 read)
    lda tx_port                                                       ; 865b: ad 25 0d    .%.            ; Load destination port number
    bne setup_data_xfer                                               ; 865e: d0 42       .B             ; Port != 0: standard data transfer
    ldy tx_ctrl_byte                                                  ; 8660: ac 24 0d    .$.            ; Port 0: load control byte for table lookup
    lda tube_tx_sr1_operand,y                                         ; 8663: b9 5f 88    ._.            ; Look up tx_flags from table
    sta rx_src_net                                                    ; 8666: 8d 3e 0d    .>.            ; Store operation flags
    lda tube_tx_inc_operand,y                                         ; 8669: b9 57 88    .W.            ; Look up tx_length from table
    sta rx_ctrl                                                       ; 866c: 8d 3f 0d    .?.            ; Store expected transfer length
    lda #&86                                                          ; 866f: a9 86       ..             ; Push high byte of return address (&9C)
    pha                                                               ; 8671: 48          H              ; Push high byte for PHA/PHA/RTS dispatch
    lda intoff_disable_nmi_op,y                                       ; 8672: b9 f6 85    ...            ; Look up handler address low from table
    pha                                                               ; 8675: 48          H              ; Push low byte for PHA/PHA/RTS dispatch
    rts                                                               ; 8676: 60          `              ; RTS dispatches to control-byte handler

    equb &82, &86, &c8, &c8, &c8, &d8, &d8, &7e, &a9, 3, &d0, &48     ; 8677: 82 86 c8... ...
.tx_ctrl_peek
    equb &a9, 3, &d0, 2                                               ; 8683: a9 03 d0... ...            ; A=3: scout_status for PEEK op
.tx_ctrl_poke
    equb &a9, 2                                                       ; 8687: a9 02       ..             ; Scout status = 2 (POKE transfer)
.store_status_add4
    equb &8d, &40, &0d, &18, 8, &a0, &0c                              ; 8689: 8d 40 0d... .@.            ; Store scout status; Clear carry for 4-byte addition; Save carry on stack; Y=&0C: start at offset 12
.add_bytes_loop
    equb &b9, &1e, &0d, &28, &71, &a0, &99, &1e, &0d, &c8, 8          ; 8690: b9 1e 0d... ...            ; Load workspace address byte; Restore carry from previous byte; Add TXCB address byte; Store updated address byte; Next byte; Save carry for next addition
.tx_ctrl_proc
    equb &c0, &10, &90, &f1, &28, &d0, &2c                            ; 869b: c0 10 90... ...            ; Compare Y with 16-byte boundary; Below boundary: continue addition; Restore processor flags

; &86a2 referenced 1 time by &865e
.setup_data_xfer
    lda tx_dst_stn                                                    ; 86a2: ad 20 0d    . .            ; Load dest station for broadcast check
    and tx_dst_net                                                    ; 86a5: 2d 21 0d    -!.            ; AND with dest network
    cmp #&ff                                                          ; 86a8: c9 ff       ..             ; Both &FF = broadcast address?
    bne setup_unicast_xfer                                            ; 86aa: d0 18       ..             ; Not broadcast: unicast path
    lda #&0e                                                          ; 86ac: a9 0e       ..             ; Broadcast scout: 14 bytes total
    sta rx_ctrl                                                       ; 86ae: 8d 3f 0d    .?.            ; Store broadcast scout length
    lda #&40 ; '@'                                                    ; 86b1: a9 40       .@             ; A=&40: broadcast flag
    sta rx_src_net                                                    ; 86b3: 8d 3e 0d    .>.            ; Set broadcast flag in tx_flags
    ldy #4                                                            ; 86b6: a0 04       ..             ; Y=4: start of address data in TXCB
; &86b8 referenced 1 time by &86c0
.copy_bcast_addr
    lda (nmi_tx_block),y                                              ; 86b8: b1 a0       ..             ; Copy TXCB address bytes to scout buffer
    sta tx_src_stn,y                                                  ; 86ba: 99 22 0d    .".            ; Store to TX source/data area
    iny                                                               ; 86bd: c8          .              ; Next byte
    cpy #&0c                                                          ; 86be: c0 0c       ..             ; Done 8 bytes? (Y reaches &0C)
    bcc copy_bcast_addr                                               ; 86c0: 90 f6       ..             ; No: continue copying
    bcs tx_ctrl_exit                                                  ; 86c2: b0 15       ..             ; ALWAYS branch

; &86c4 referenced 1 time by &86aa
.setup_unicast_xfer
    lda #0                                                            ; 86c4: a9 00       ..             ; A=0: clear flags for unicast
    sta rx_src_net                                                    ; 86c6: 8d 3e 0d    .>.            ; Clear tx_flags
.proc_op_status2
    lda #2                                                            ; 86c9: a9 02       ..             ; scout_status=2: data transfer pending
.store_status_copy_ptr
    sta rx_port                                                       ; 86cb: 8d 40 0d    .@.            ; Store scout status
.skip_buf_setup
    lda nmi_tx_block                                                  ; 86ce: a5 a0       ..             ; Copy TX block pointer to workspace ptr
    sta port_ws_offset                                                ; 86d0: 85 a6       ..             ; Store low byte
    lda nmi_tx_block_hi                                               ; 86d2: a5 a1       ..             ; Copy TX block pointer high byte
    sta rx_buf_offset                                                 ; 86d4: 85 a7       ..             ; Store high byte
    jsr tx_calc_transfer                                              ; 86d6: 20 e8 88     ..            ; Calculate transfer size from RXCB; Calculate transfer size for data phase.
; Compute byte count from buffer start/end
; pointers in the TX control block.
; &86d9 referenced 1 time by &86c2
.tx_ctrl_exit
    plp                                                               ; 86d9: 28          (              ; Restore processor status from stack
    pla                                                               ; 86da: 68          h              ; Restore stacked registers (4 PLAs)
    pla                                                               ; 86db: 68          h              ; Second PLA
    pla                                                               ; 86dc: 68          h              ; Third PLA
    pla                                                               ; 86dd: 68          h              ; Fourth PLA
    tax                                                               ; 86de: aa          .              ; Restore X from A
    rts                                                               ; 86df: 60          `              ; Return to caller

; ***************************************************************************************
; NMI handler: transmit data frame bytes.
; Write byte pairs from TX buffer at &0D20
; to ADLC TX FIFO in a tight loop while
; IRQ is asserted. Branch to tx_last_data
; when buffer index reaches frame length.
; ***************************************************************************************
.nmi_tx_data
    ldy rx_remote_addr                                                ; 86e0: ac 41 0d    .A.            ; Load TX buffer index
    bit econet_control1_or_status1                                    ; 86e3: 2c a0 fe    ,..            ; BIT SR1: V=bit6(TDRA), N=bit7(IRQ)
; &86e6 referenced 1 time by &8701
.tx_fifo_write
    bvc tx_fifo_not_ready                                             ; 86e6: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 86e8: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 86eb: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 86ee: c8          .              ; Next TX buffer byte
    lda tx_dst_stn,y                                                  ; 86ef: b9 20 0d    . .            ; Load second byte from TX buffer
    iny                                                               ; 86f2: c8          .              ; Advance TX index past second byte
    sty rx_remote_addr                                                ; 86f3: 8c 41 0d    .A.            ; Save updated TX buffer index
    sta econet_data_continue_frame                                    ; 86f6: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy rx_ctrl                                                       ; 86f9: cc 3f 0d    .?.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 86fc: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA; Signal last data byte of TX frame.
; Write TX_LAST_DATA to CR2 and install
; nmi_tx_complete as the next NMI handler.
    bit econet_control1_or_status1                                    ; 86fe: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi tx_fifo_write                                                 ; 8701: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 8703: 4c 14 0d    L..            ; RTI -- wait for next NMI

; &8706 referenced 1 time by &8749
.tx_error
    lda #&42 ; 'B'                                                    ; 8706: a9 42       .B             ; Error &42
    bne tx_store_error                                                ; 8708: d0 07       ..             ; ALWAYS branch

; &870a referenced 1 time by &86e6
.tx_fifo_not_ready
    lda #&67 ; 'g'                                                    ; 870a: a9 67       .g             ; CR2=&67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 870c: 8d a1 fe    ...            ; Write CR2: clear status, idle listen
    lda #&41 ; 'A'                                                    ; 870f: a9 41       .A             ; Error &41 (TDRA not ready)
; &8711 referenced 1 time by &8708
.tx_store_error
    ldy station_id_disable_net_nmis                                   ; 8711: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &8714 referenced 1 time by &8717
.delay_nmi_disable
    pha                                                               ; 8714: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 8715: 68          h              ; PHA/PLA delay (~7 cycles each)
    iny                                                               ; 8716: c8          .              ; Increment delay counter
    bne delay_nmi_disable                                             ; 8717: d0 fb       ..             ; Loop 256 times for NMI disable
    jmp tx_store_result                                               ; 8719: 4c cc 88    L..            ; Store error and return to idle; Store TX result code in control block,
; signal completion, and reset ADLC to
; idle listen mode.

; ***************************************************************************************
; Signal last data byte of TX frame.
; Write TX_LAST_DATA to CR2 and install
; nmi_tx_complete as the next NMI handler.
; ***************************************************************************************
; &871c referenced 1 time by &86fc
.tx_last_data
    lda #&3f ; '?'                                                    ; 871c: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 871e: 8d a1 fe    ...            ; Write to ADLC CR2
    lda #&28 ; '('                                                    ; 8721: a9 28       .(             ; Install NMI handler at &8728 (TX completion)
    ldy #&87                                                          ; 8723: a0 87       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 8725: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; ***************************************************************************************
; NMI handler: TX frame completed. Reset
; ADLC from TX to RX mode. Route to
; tx_result_ok (broadcast), reply scout
; handler (two-way), or handshake_await_ack
; (four-way) based on tx_flags.
; ***************************************************************************************
.nmi_tx_complete
    lda #&82                                                          ; 8728: a9 82       ..             ; Jump to error handler
    sta econet_control1_or_status1                                    ; 872a: 8d a0 fe    ...            ; Write CR1 to switch from TX to RX
    bit rx_src_net                                                    ; 872d: 2c 3e 0d    ,>.            ; Test workspace flags
    bvc check_handshake_bit                                           ; 8730: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 8732: 4c c6 88    L..            ; bit6 set -- TX completion; Set transmit result to success (A=0)
; and fall through to tx_store_result.

; &8735 referenced 1 time by &8730
.check_handshake_bit
    lda #1                                                            ; 8735: a9 01       ..             ; A=1: mask for bit0 test
    bit rx_src_net                                                    ; 8737: 2c 3e 0d    ,>.            ; Test tx_flags bit0 (handshake)
    beq install_reply_scout                                           ; 873a: f0 03       ..             ; bit0 clear: install reply handler
    jmp handshake_await_ack                                           ; 873c: 4c 6e 88    Ln.            ; bit0 set -- four-way handshake data phase; Switch ADLC from TX to RX mode and
; install nmi_final_ack as the NMI handler
; to await the final acknowledge frame of a
; four-way handshake.

; &873f referenced 1 time by &873a
.install_reply_scout
    lda #&44 ; 'D'                                                    ; 873f: a9 44       .D             ; Install RX reply handler at &8744
    jmp install_nmi_handler                                           ; 8741: 4c 11 0d    L..            ; Install handler and RTI

; ***************************************************************************************
; NMI handler: receive reply scout frame.
; Check SR2 for AP, read destination station
; byte, verify it matches our ID. Install
; nmi_reply_cont on match.
; ***************************************************************************************
.nmi_reply_scout
    lda #1                                                            ; 8744: a9 01       ..             ; A=&01: AP mask for SR2
    bit econet_control23_or_status2                                   ; 8746: 2c a1 fe    ,..            ; BIT SR2: test AP (Address Present)
    beq tx_error                                                      ; 8749: f0 bb       ..             ; No AP -- error
    lda econet_data_continue_frame                                    ; 874b: ad a2 fe    ...            ; Read first RX byte (destination station)
    cmp station_id_disable_net_nmis                                   ; 874e: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne reject_reply                                                  ; 8751: d0 19       ..             ; Not our station -- error/reject
    lda #&58 ; 'X'                                                    ; 8753: a9 58       .X             ; Install next handler at &8758 (reply continuation)
    jmp install_nmi_handler                                           ; 8755: 4c 11 0d    L..            ; Install continuation handler

; ***************************************************************************************
; NMI handler: continue reply scout frame
; reception. Read remaining scout bytes
; and install validation handler.
; ***************************************************************************************
.nmi_reply_cont
    bit econet_control23_or_status2                                   ; 8758: 2c a1 fe    ,..            ; Read RX byte (destination station)
    bpl reject_reply                                                  ; 875b: 10 0f       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 875d: ad a2 fe    ...            ; Read destination network byte
    bne reject_reply                                                  ; 8760: d0 0a       ..             ; Non-zero -- network mismatch, error
    lda #&6f ; 'o'                                                    ; 8762: a9 6f       .o             ; Install next handler at &876F (reply validation)
    bit econet_control1_or_status1                                    ; 8764: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 8767: 30 06       0.             ; IRQ set -- fall through to &876F without RTI; NMI handler: validate reply scout frame.
; Verify source station/network match the
; original TX destination, check FV for
; frame completion, then begin scout ACK
; transmission.
    jmp install_nmi_handler                                           ; 8769: 4c 11 0d    L..            ; IRQ not set -- install handler and RTI

; &876c referenced 7 times by &8751, &875b, &8760, &8772, &877a, &8782, &8789
.reject_reply
    jmp tx_result_fail                                                ; 876c: 4c ca 88    L..            ; Store error and return to idle; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.

; ***************************************************************************************
; NMI handler: validate reply scout frame.
; Verify source station/network match the
; original TX destination, check FV for
; frame completion, then begin scout ACK
; transmission.
; ***************************************************************************************
; &876f referenced 1 time by &8767
.nmi_reply_validate
    bit econet_control23_or_status2                                   ; 876f: 2c a1 fe    ,..            ; BIT SR2: test RDA (bit7). Must be set for valid reply.
    bpl reject_reply                                                  ; 8772: 10 f8       ..             ; No RDA -- error (FV masking RDA via PSE would cause this)
    lda econet_data_continue_frame                                    ; 8774: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 8777: cd 20 0d    . .            ; Compare to original TX destination station (&0D20)
    bne reject_reply                                                  ; 877a: d0 f0       ..             ; Mismatch -- not the expected reply, error
    lda econet_data_continue_frame                                    ; 877c: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 877f: cd 21 0d    .!.            ; Compare to original TX destination network (&0D21)
    bne reject_reply                                                  ; 8782: d0 e8       ..             ; Mismatch -- error
    lda #2                                                            ; 8784: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 8786: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq reject_reply                                                  ; 8789: f0 e1       ..             ; No FV -- incomplete frame, error
    lda #&a7                                                          ; 878b: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)
    sta econet_control23_or_status2                                   ; 878d: 8d a1 fe    ...            ; Write CR2: enable RTS for TX handshake
    lda #&44 ; 'D'                                                    ; 8790: a9 44       .D             ; CR1=&44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 8792: 8d a0 fe    ...            ; Write CR1: reset RX, enable TX interrupt
    lda #&6e ; 'n'                                                    ; 8795: a9 6e       .n             ; Install next handler at &886E (four-way data phase) into &0D43/&0D44
    ldy #&88                                                          ; 8797: a0 88       ..             ; High byte &88 of next handler address
    sta l0d43                                                         ; 8799: 8d 43 0d    .C.            ; Store low byte to nmi_next_lo
    sty l0d44                                                         ; 879c: 8c 44 0d    .D.            ; Store high byte to nmi_next_hi
    lda tx_dst_stn                                                    ; 879f: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 87a2: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc tx_check_tdra_ready                                           ; 87a5: 50 16       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 87a7: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 87aa: ad 21 0d    .!.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 87ad: 8d a2 fe    ...            ; Write dest network to TX FIFO
    lda #&b7                                                          ; 87b0: a9 b7       ..             ; Install handler at &87B7 (write src addr for scout ACK)
    ldy #&87                                                          ; 87b2: a0 87       ..             ; High byte &87 of handler address
    jmp set_nmi_vector                                                ; 87b4: 4c 0e 0d    L..            ; Set NMI vector and return

; ***************************************************************************************
; NMI handler: write source address bytes
; for scout ACK frame. Write our station
; ID and network 0 to TX FIFO, then install
; nmi_data_tx or nmi_imm_data handler.
; ***************************************************************************************
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 87b7: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 87ba: 2c a0 fe    ,..            ; BIT SR1: test TDRA
; &87bd referenced 1 time by &87a5
.tx_check_tdra_ready
    bvc data_tx_check_fifo                                            ; 87bd: 50 2c       P,             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 87bf: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 87c2: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 87c4: 8d a2 fe    ...            ; Write network byte to TX FIFO
; &87c7 referenced 1 time by &833e
.data_tx_begin
    lda #2                                                            ; 87c7: a9 02       ..             ; Test bit 1 of tx_flags
    bit rx_src_net                                                    ; 87c9: 2c 3e 0d    ,>.            ; Check if immediate-op or data-transfer
    bne install_imm_data_nmi                                          ; 87cc: d0 07       ..             ; Bit 1 set: immediate op, use alt handler
    lda #&e4                                                          ; 87ce: a9 e4       ..             ; Install nmi_data_tx at &87E4
    ldy #&87                                                          ; 87d0: a0 87       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 87d2: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; &87d5 referenced 1 time by &87cc
.install_imm_data_nmi
    lda #&2d ; '-'                                                    ; 87d5: a9 2d       .-             ; Install nmi_imm_data at &882D
    ldy #&88                                                          ; 87d7: a0 88       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 87d9: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; ***************************************************************************************
; NMI handler: transmit data phase of a
; four-way handshake. Send byte pairs from
; the buffer at (open_port_buf) or from Tube
; R3. Loop while IRQ is asserted. Signal
; TX_LAST_DATA when buffer is exhausted.
; ***************************************************************************************
; &87dc referenced 1 time by &87e6
.nmi_data_tx
    ldy port_buf_len_hi                                               ; 87dc: a4 a3       ..             ; Y = buffer offset, resume from last position
    beq data_tx_last                                                  ; 87de: f0 33       .3             ; No pages left: send final partial page
    ldy port_buf_len                                                  ; 87e0: a4 a2       ..             ; Load remaining byte count
    beq c87e8                                                         ; 87e2: f0 04       ..             ; Zero bytes left: skip to TDRA check
    ldy port_buf_len                                                  ; 87e4: a4 a2       ..             ; Load remaining byte count (alt entry)
    beq nmi_data_tx                                                   ; 87e6: f0 f4       ..             ; Zero: loop back to top of handler; NMI handler: transmit data phase of a
; four-way handshake. Send byte pairs from
; the buffer at (open_port_buf) or from Tube
; R3. Loop while IRQ is asserted. Signal
; TX_LAST_DATA when buffer is exhausted.
; &87e8 referenced 1 time by &87e2
.c87e8
    bit econet_control1_or_status1                                    ; 87e8: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
; &87eb referenced 2 times by &87bd, &880e
.data_tx_check_fifo
    bvc tube_tx_fifo_write                                            ; 87eb: 50 43       PC             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 87ed: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 87ef: 8d a2 fe    ...            ; Write first byte of pair to FIFO
    iny                                                               ; 87f2: c8          .              ; Advance buffer offset
    bne write_second_tx_byte                                          ; 87f3: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 87f5: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 87f7: f0 1a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 87f9: e6 a5       ..             ; Increment buffer high byte
; &87fb referenced 1 time by &87f3
.write_second_tx_byte
    lda (open_port_buf),y                                             ; 87fb: b1 a4       ..             ; Load second byte of pair
    sta econet_data_continue_frame                                    ; 87fd: 8d a2 fe    ...            ; Write second byte to FIFO
    iny                                                               ; 8800: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 8801: 84 a2       ..             ; Save updated buffer position
    bne check_irq_loop                                                ; 8803: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 8805: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 8807: f0 0a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 8809: e6 a5       ..             ; Increment buffer high byte
; &880b referenced 1 time by &8803
.check_irq_loop
    bit econet_control1_or_status1                                    ; 880b: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) for tight loop
    bmi data_tx_check_fifo                                            ; 880e: 30 db       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 8810: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; &8813 referenced 5 times by &87de, &87f7, &8807, &8846, &885c
.data_tx_last
    lda #&3f ; '?'                                                    ; 8813: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 8815: 8d a1 fe    ...            ; Write CR2 to close frame
    lda rx_src_net                                                    ; 8818: ad 3e 0d    .>.            ; Check tx_flags for next action
    bpl install_saved_handler                                         ; 881b: 10 07       ..             ; Bit7 clear: error, install saved handler
    lda #&eb                                                          ; 881d: a9 eb       ..             ; Install discard_reset_listen at &83EB
    ldy #&83                                                          ; 881f: a0 83       ..             ; High byte of &83EB handler
    jmp set_nmi_vector                                                ; 8821: 4c 0e 0d    L..            ; Set NMI vector and return

; &8824 referenced 1 time by &881b
.install_saved_handler
    lda l0d43                                                         ; 8824: ad 43 0d    .C.            ; Load saved next handler low byte
    ldy l0d44                                                         ; 8827: ac 44 0d    .D.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 882a: 4c 0e 0d    L..            ; Install saved handler and return

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 882d: 2c a0 fe    ,..            ; Tube TX: BIT SR1 test TDRA
; &8830 referenced 2 times by &87eb, &8861
.tube_tx_fifo_write
    bvc tx_tdra_error                                                 ; 8830: 50 34       P4             ; TDRA not ready -- error
    lda tube_data_register_3                                          ; 8832: ad e5 fe    ...            ; Read byte from Tube R3
    sta econet_data_continue_frame                                    ; 8835: 8d a2 fe    ...            ; Write to TX FIFO
    inc port_buf_len                                                  ; 8838: e6 a2       ..             ; Increment 4-byte buffer counter
    bne write_second_tube_byte                                        ; 883a: d0 0c       ..             ; Low byte didn't wrap
    inc port_buf_len_hi                                               ; 883c: e6 a3       ..             ; Carry into second byte
    bne write_second_tube_byte                                        ; 883e: d0 08       ..             ; No further carry
    inc open_port_buf                                                 ; 8840: e6 a4       ..             ; Carry into third byte
    bne write_second_tube_byte                                        ; 8842: d0 04       ..             ; No further carry
    inc open_port_buf_hi                                              ; 8844: e6 a5       ..             ; Carry into fourth byte
    beq data_tx_last                                                  ; 8846: f0 cb       ..             ; Counter wrapped to zero: last data
; &8848 referenced 3 times by &883a, &883e, &8842
.write_second_tube_byte
    lda tube_data_register_3                                          ; 8848: ad e5 fe    ...            ; Read second Tube byte from R3
    sta econet_data_continue_frame                                    ; 884b: 8d a2 fe    ...            ; Write second byte to TX FIFO
    inc port_buf_len                                                  ; 884e: e6 a2       ..             ; Increment 4-byte counter (second byte)
    bne check_tube_irq_loop                                           ; 8850: d0 0c       ..             ; Low byte didn't wrap
.tube_tx_inc_byte2
    inc port_buf_len_hi                                               ; 8852: e6 a3       ..             ; Carry into second byte
    bne check_tube_irq_loop                                           ; 8854: d0 08       ..             ; No further carry
.tube_tx_inc_byte3
tube_tx_inc_operand = tube_tx_inc_byte3+1
    inc open_port_buf                                                 ; 8856: e6 a4       ..             ; Carry into third byte
; &8857 referenced 1 time by &8669
    bne check_tube_irq_loop                                           ; 8858: d0 04       ..             ; No further carry
.tube_tx_inc_byte4
    inc open_port_buf_hi                                              ; 885a: e6 a5       ..             ; Carry into fourth byte
    beq data_tx_last                                                  ; 885c: f0 b5       ..             ; Counter wrapped to zero: last data
; &885e referenced 3 times by &8850, &8854, &8858
.check_tube_irq_loop
tube_tx_sr1_operand = check_tube_irq_loop+1
    bit econet_control1_or_status1                                    ; 885e: 2c a0 fe    ,..            ; BIT SR1: test IRQ for tight loop
; &885f referenced 1 time by &8663
    bmi tube_tx_fifo_write                                            ; 8861: 30 cd       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 8863: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; &8866 referenced 1 time by &8830
.tx_tdra_error
    lda rx_src_net                                                    ; 8866: ad 3e 0d    .>.            ; TX error: check flags for path
    bpl tx_result_fail                                                ; 8869: 10 5f       ._             ; Bit7 clear: TX result = not listening; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    jmp discard_reset_rx                                              ; 886b: 4c eb 83    L..            ; Bit7 set: discard and return to listen

; ***************************************************************************************
; Switch ADLC from TX to RX mode and
; install nmi_final_ack as the NMI handler
; to await the final acknowledge frame of a
; four-way handshake.
; ***************************************************************************************
; &886e referenced 1 time by &873c
.handshake_await_ack
    lda #&82                                                          ; 886e: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 8870: 8d a0 fe    ...            ; Write to ADLC CR1
    lda #&7a ; 'z'                                                    ; 8873: a9 7a       .z             ; Install nmi_final_ack handler
    ldy #&88                                                          ; 8875: a0 88       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 8877: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; ***************************************************************************************
; NMI handler: receive final ACK frame.
; Validate AP flag and destination station,
; then install continuation handler.
; ***************************************************************************************
.nmi_final_ack
    lda #1                                                            ; 887a: a9 01       ..             ; A=&01: AP mask
    bit econet_control23_or_status2                                   ; 887c: 2c a1 fe    ,..            ; BIT SR2: test AP
    beq tx_result_fail                                                ; 887f: f0 49       .I             ; No AP -- error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    lda econet_data_continue_frame                                    ; 8881: ad a2 fe    ...            ; Read dest station
    cmp station_id_disable_net_nmis                                   ; 8884: cd 18 fe    ...            ; Compare to our station (INTOFF side effect)
    bne tx_result_fail                                                ; 8887: d0 41       .A             ; Not our station -- error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    lda #&8e                                                          ; 8889: a9 8e       ..             ; Install nmi_final_ack_net handler
    jmp install_nmi_handler                                           ; 888b: 4c 11 0d    L..            ; Install continuation handler

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 888e: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 8891: 10 37       .7             ; No RDA -- error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    lda econet_data_continue_frame                                    ; 8893: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 8896: d0 32       .2             ; Non-zero -- network mismatch, error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    lda #&a2                                                          ; 8898: a9 a2       ..             ; Install nmi_final_ack_validate handler
    bit econet_control1_or_status1                                    ; 889a: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 889d: 30 03       0.             ; IRQ set -- fall through to validate; NMI handler: validate final ACK frame.
; Check source station/network, verify
; frame valid, and store success result.
    jmp install_nmi_handler                                           ; 889f: 4c 11 0d    L..            ; Install handler and RTI

; ***************************************************************************************
; NMI handler: validate final ACK frame.
; Check source station/network, verify
; frame valid, and store success result.
; ***************************************************************************************
; &88a2 referenced 1 time by &889d
.nmi_final_ack_validate
    bit econet_control23_or_status2                                   ; 88a2: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 88a5: 10 23       .#             ; No RDA -- error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    lda econet_data_continue_frame                                    ; 88a7: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 88aa: cd 20 0d    . .            ; Compare to TX dest station (&0D20)
    bne tx_result_fail                                                ; 88ad: d0 1b       ..             ; Mismatch -- error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    lda econet_data_continue_frame                                    ; 88af: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 88b2: cd 21 0d    .!.            ; Compare to TX dest network (&0D21)
    bne tx_result_fail                                                ; 88b5: d0 13       ..             ; Mismatch -- error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
    lda rx_src_net                                                    ; 88b7: ad 3e 0d    .>.            ; Load TX flags for next action
    bpl check_fv_final_ack                                            ; 88ba: 10 03       ..             ; bit7 clear: no data phase
    jmp install_data_rx_handler                                       ; 88bc: 4c 11 82    L..            ; Install data RX handler; Install NMI handler for data reception:
; bulk RAM path or Tube transfer path.
; Enter bulk read directly if data waiting.

; &88bf referenced 1 time by &88ba
.check_fv_final_ack
    lda #2                                                            ; 88bf: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 88c1: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq tx_result_fail                                                ; 88c4: f0 04       ..             ; No FV -- error; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
; ***************************************************************************************
; Set transmit result to success (A=0)
; and fall through to tx_store_result.
; ***************************************************************************************
; &88c6 referenced 2 times by &82ec, &8732
.tx_result_ok
    lda #0                                                            ; 88c6: a9 00       ..             ; A=0: success result code
    beq tx_store_result                                               ; 88c8: f0 02       ..             ; BEQ: always taken (A=0); Store TX result code in control block,
; signal completion, and reset ADLC to
; idle listen mode.; ALWAYS branch

; ***************************************************************************************
; Set transmit result to 'not listening'
; (A=&41) and fall through to tx_store_result.
; ***************************************************************************************
; &88ca referenced 11 times by &8230, &876c, &8869, &887f, &8887, &8891, &8896, &88a5, &88ad, &88b5, &88c4
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 88ca: a9 41       .A             ; A=&41: not listening error code
; ***************************************************************************************
; Store TX result code in control block,
; signal completion, and reset ADLC to
; idle listen mode.
; ***************************************************************************************
; &88cc referenced 2 times by &8719, &88c8
.tx_store_result
    ldy #0                                                            ; 88cc: a0 00       ..             ; Y=0: index into TX control block
    sta (nmi_tx_block),y                                              ; 88ce: 91 a0       ..             ; Store result/error code at (nmi_tx_block),0
    lda #&80                                                          ; 88d0: a9 80       ..             ; &80: completion flag for &0D3A
    sta ws_0d60                                                       ; 88d2: 8d 60 0d    .`.            ; Signal TX complete
    jmp discard_reset_rx                                              ; 88d5: 4c eb 83    L..            ; Full ADLC reset and return to idle listen

    asl l0a0e                                                         ; 88d8: 0e 0e 0a    ...            ; Unreferenced data block (purpose unknown)
    asl a                                                             ; 88db: 0a          .
    asl a                                                             ; 88dc: 0a          .
    asl l0006                                                         ; 88dd: 06 06       ..
    asl a                                                             ; 88df: 0a          .
    sta (zp_ptr_lo,x)                                                 ; 88e0: 81 00       ..
    brk                                                               ; 88e2: 00          .

    equb 0, 0, 1, 1, &81                                              ; 88e3: 00 00 01... ...

; ***************************************************************************************
; Calculate transfer size for data phase.
; Compute byte count from buffer start/end
; pointers in the TX control block.
; ***************************************************************************************
; &88e8 referenced 3 times by &81b4, &84ce, &86d6
.tx_calc_transfer
    ldy #7                                                            ; 88e8: a0 07       ..             ; Y=7: offset to RXCB buffer addr byte 3
    lda (port_ws_offset),y                                            ; 88ea: b1 a6       ..             ; Read RXCB[7] (buffer addr high byte)
    cmp #&ff                                                          ; 88ec: c9 ff       ..             ; Compare to &FF
    bne c88f7                                                         ; 88ee: d0 07       ..             ; Not &FF: normal buffer, skip Tube check
    dey                                                               ; 88f0: 88          .              ; Y=&06
    lda (port_ws_offset),y                                            ; 88f1: b1 a6       ..             ; Read RXCB[6] (buffer addr byte 2)
    cmp #&fe                                                          ; 88f3: c9 fe       ..             ; Check if addr byte 2 >= &FE (Tube range)
    bcs fallback_calc_transfer                                        ; 88f5: b0 44       .D             ; Tube/IO address: use fallback path
; &88f7 referenced 1 time by &88ee
.c88f7
    lda l0d63                                                         ; 88f7: ad 63 0d    .c.            ; Transmit in progress?
    beq fallback_calc_transfer                                        ; 88fa: f0 3f       .?             ; No: fallback path
    lda rx_src_net                                                    ; 88fc: ad 3e 0d    .>.            ; Load TX flags for transfer setup
    ora #2                                                            ; 88ff: 09 02       ..             ; Set bit 1 (transfer complete)
    sta rx_src_net                                                    ; 8901: 8d 3e 0d    .>.            ; Store with bit 1 set (Tube xfer)
    sec                                                               ; 8904: 38          8              ; Init borrow for 4-byte subtract
    php                                                               ; 8905: 08          .              ; Save carry on stack
    ldy #4                                                            ; 8906: a0 04       ..             ; Y=4: start at RXCB offset 4
; &8908 referenced 1 time by &891a
.calc_transfer_size
    lda (port_ws_offset),y                                            ; 8908: b1 a6       ..             ; Load RXCB[Y] (current ptr byte)
    iny                                                               ; 890a: c8          .              ; Y += 4: advance to RXCB[Y+4]
    iny                                                               ; 890b: c8          .              ; Y += 4: advance to high ptr offset
    iny                                                               ; 890c: c8          .              ; (continued)
    iny                                                               ; 890d: c8          .              ; (continued)
    plp                                                               ; 890e: 28          (              ; Restore borrow from previous byte
    sbc (port_ws_offset),y                                            ; 890f: f1 a6       ..             ; Subtract RXCB[Y+4] (start ptr byte)
    sta net_tx_ptr,y                                                  ; 8911: 99 9a 00    ...            ; Store result byte
    dey                                                               ; 8914: 88          .              ; Y -= 3: next source byte
    dey                                                               ; 8915: 88          .              ; Y -= 3: back to next low ptr byte
    dey                                                               ; 8916: 88          .              ; (continued)
    php                                                               ; 8917: 08          .              ; Save borrow for next byte
    cpy #8                                                            ; 8918: c0 08       ..             ; Done all 4 bytes?
    bcc calc_transfer_size                                            ; 891a: 90 ec       ..             ; No: next byte pair
    plp                                                               ; 891c: 28          (              ; Discard final borrow
    txa                                                               ; 891d: 8a          .              ; Save X
    pha                                                               ; 891e: 48          H              ; Save X
    lda #4                                                            ; 891f: a9 04       ..             ; Compute address of RXCB+4
    clc                                                               ; 8921: 18          .              ; CLC for base pointer addition
    adc port_ws_offset                                                ; 8922: 65 a6       e.             ; Add RXCB base to get RXCB+4 addr
    tax                                                               ; 8924: aa          .              ; X = low byte of RXCB+4
    ldy rx_buf_offset                                                 ; 8925: a4 a7       ..             ; Y = high byte of RXCB ptr
    lda #&c2                                                          ; 8927: a9 c2       ..             ; Tube claim type &C2
    jsr tube_addr_data_dispatch                                       ; 8929: 20 06 04     ..            ; Claim Tube transfer address
    bcc restore_x_and_return                                          ; 892c: 90 0a       ..             ; No Tube: skip reclaim
    lda rx_port                                                       ; 892e: ad 40 0d    .@.            ; Tube: reclaim with scout status
    jsr tube_addr_data_dispatch                                       ; 8931: 20 06 04     ..            ; Reclaim with scout status type
    jsr release_tube                                                  ; 8934: 20 3f 84     ?.            ; Release Tube claim after reclaim; Release the Tube address claim if one is
; held. Clear the release-needed flag.
    sec                                                               ; 8937: 38          8              ; C=1: Tube address claimed
; &8938 referenced 1 time by &892c
.restore_x_and_return
    pla                                                               ; 8938: 68          h              ; Restore X
    tax                                                               ; 8939: aa          .              ; Restore X from stack
    rts                                                               ; 893a: 60          `              ; Return with C = transfer status

; &893b referenced 2 times by &88f5, &88fa
.fallback_calc_transfer
    ldy #4                                                            ; 893b: a0 04       ..             ; Y=4: RXCB current pointer offset
    lda (port_ws_offset),y                                            ; 893d: b1 a6       ..             ; Load RXCB[4] (current ptr lo)
    ldy #8                                                            ; 893f: a0 08       ..             ; Y=8: RXCB start address offset
    sec                                                               ; 8941: 38          8              ; Set carry for subtraction
    sbc (port_ws_offset),y                                            ; 8942: f1 a6       ..             ; Subtract RXCB[8] (start ptr lo)
    sta port_buf_len                                                  ; 8944: 85 a2       ..             ; Store transfer size lo
    ldy #5                                                            ; 8946: a0 05       ..             ; Y=5: current ptr hi offset
    lda (port_ws_offset),y                                            ; 8948: b1 a6       ..             ; Load RXCB[5] (current ptr hi)
    sbc #0                                                            ; 894a: e9 00       ..             ; Propagate borrow only
    sta open_port_buf_hi                                              ; 894c: 85 a5       ..             ; Temp store of adjusted hi byte
    ldy #8                                                            ; 894e: a0 08       ..             ; Y=8: start address lo offset
    lda (port_ws_offset),y                                            ; 8950: b1 a6       ..             ; Copy RXCB[8] to open port buffer lo
    sta open_port_buf                                                 ; 8952: 85 a4       ..             ; Store to scratch (side effect)
    ldy #9                                                            ; 8954: a0 09       ..             ; Y=9: start address hi offset
    lda (port_ws_offset),y                                            ; 8956: b1 a6       ..             ; Load RXCB[9]
    sec                                                               ; 8958: 38          8              ; Set carry for subtraction
    sbc open_port_buf_hi                                              ; 8959: e5 a5       ..             ; Subtract adjusted hi byte
    sta port_buf_len_hi                                               ; 895b: 85 a3       ..             ; Store transfer size hi
    sec                                                               ; 895d: 38          8              ; Return with C=1
.nmi_shim_rom_src
    rts                                                               ; 895e: 60          `              ; Return with C=1 (success)

; ***************************************************************************************
; Full MC6854 ADLC hardware reset. Set CR1
; with TX and RX in reset, then configure
; CR4 and CR3 via address control mode.
; ***************************************************************************************
; &895f referenced 3 times by &806c, &80f9, &8233
.adlc_full_reset
    lda #&c1                                                          ; 895f: a9 c1       ..             ; CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 8961: 8d a0 fe    ...            ; Write CR1 to ADLC register 0
    lda #&1e                                                          ; 8964: a9 1e       ..             ; CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding
    sta econet_data_terminate_frame                                   ; 8966: 8d a3 fe    ...            ; Write CR4 to ADLC register 3
    lda #0                                                            ; 8969: a9 00       ..             ; CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 896b: 8d a1 fe    ...            ; Write CR3 to ADLC register 1
; ***************************************************************************************
; Configure ADLC for receive/listen mode.
; TX held in reset, RX interrupts enabled,
; status flags cleared.
; ***************************************************************************************
; &896e referenced 2 times by &83ee, &899a
.adlc_rx_listen
    lda #&82                                                          ; 896e: a9 82       ..             ; CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 8970: 8d a0 fe    ...            ; Write to ADLC CR1
    lda #&67 ; 'g'                                                    ; 8973: a9 67       .g             ; CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 8975: 8d a1 fe    ...            ; Write to ADLC CR2
    rts                                                               ; 8978: 60          `              ; Return; ADLC now in RX listen mode

; ***************************************************************************************
; Wait for NMI handler to return to idle
; state (nmi_rx_scout), then reset ADLC
; to listen mode. Service 12 handler.
; ***************************************************************************************
.wait_idle_and_reset
    bit ws_0d62                                                       ; 8979: 2c 62 0d    ,b.            ; Check if Econet has been initialised
    bpl reset_enter_listen                                            ; 897c: 10 1c       ..             ; Not initialised: skip to RX listen
; &897e referenced 2 times by &8983, &898a
.poll_nmi_idle
    lda nmi_jmp_lo                                                    ; 897e: ad 0c 0d    ...            ; Read current NMI handler low byte
    cmp #&b3                                                          ; 8981: c9 b3       ..             ; Expected: &B3 (nmi_rx_scout low)
    bne poll_nmi_idle                                                 ; 8983: d0 f9       ..             ; Not idle: spin and wait
    lda nmi_jmp_hi                                                    ; 8985: ad 0d 0d    ...            ; Read current NMI handler high byte
    eor #&80                                                          ; 8988: 49 80       I.             ; Test if high byte = &80 (page of nmi_rx_scout)
    bne poll_nmi_idle                                                 ; 898a: d0 f2       ..             ; Not idle: spin and wait
; ***************************************************************************************
; Save Econet state for ROM bank switch.
; Store current NMI handler address and
; prepare for NMI shim installation.
; ***************************************************************************************
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 898c: 2c 18 fe    ,..            ; INTOFF: disable NMIs
    bit station_id_disable_net_nmis                                   ; 898f: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
    sta ws_0d60                                                       ; 8992: 8d 60 0d    .`.            ; TX not in progress
    sta ws_0d62                                                       ; 8995: 8d 62 0d    .b.            ; Econet not initialised
    ldy #5                                                            ; 8998: a0 05       ..             ; Y=5: service call workspace page
; &899a referenced 1 time by &897c
.reset_enter_listen
listen_jmp_hi = reset_enter_listen+2
    jmp adlc_rx_listen                                                ; 899a: 4c 6e 89    Ln.            ; Set ADLC to RX listen mode; Configure ADLC for receive/listen mode.
; TX held in reset, RX interrupts enabled,
; status flags cleared.

; &899c referenced 1 time by &808b
; ***************************************************************************************
; NMI bootstrap entry point. Install
; ROM-based scout handler and set NMI
; vector to dispatch through the shim.
; ***************************************************************************************
.nmi_bootstrap_entry
    bit station_id_disable_net_nmis                                   ; 899d: 2c 18 fe    ,..            ; INTOFF: disable NMIs while switching ROM
    pha                                                               ; 89a0: 48          H              ; Save A
    tya                                                               ; 89a1: 98          .              ; Transfer Y to A
    pha                                                               ; 89a2: 48          H              ; Save Y (via A)
    lda #0                                                            ; 89a3: a9 00       ..             ; ROM bank 0 (patched during init for actual bank)
    sta romsel                                                        ; 89a5: 8d 30 fe    .0.            ; Select Econet ROM bank via ROMSEL
    jmp nmi_rx_scout                                                  ; 89a8: 4c b3 80    L..            ; Jump to scout handler in ROM; NMI handler for incoming scout frames.
; Check destination station; accept if it
; matches our ID or is broadcast (&FF).

; ***************************************************************************************
; Write NMI handler address, restore ROM
; bank and registers, re-enable NMIs,
; and return from interrupt.
; ***************************************************************************************
.rom_set_nmi_vector
    sty nmi_jmp_hi                                                    ; 89ab: 8c 0d 0d    ...            ; Store handler high byte at &0D0D
    sta nmi_jmp_lo                                                    ; 89ae: 8d 0c 0d    ...            ; Store handler low byte at &0D0C
    lda romsel_copy                                                   ; 89b1: a5 f4       ..             ; Restore NFS ROM bank
    sta romsel                                                        ; 89b3: 8d 30 fe    .0.            ; Page in via hardware latch
    pla                                                               ; 89b6: 68          h              ; Restore Y from stack
    tay                                                               ; 89b7: a8          .              ; Transfer ROM bank to Y
    pla                                                               ; 89b8: 68          h              ; Restore A from stack
    bit video_ula_control                                             ; 89b9: 2c 20 fe    , .            ; INTON: re-enable NMIs
    rti                                                               ; 89bc: 40          @              ; Return from interrupt

    equb 1, 0, 8                                                      ; 89bd: 01 00 08    ...
; &89c0 referenced 1 time by &8e3c
.svc_dispatch_lo
    equb 4, &41, &8e, &a1, &be                                        ; 89c0: 04 41 8e... .A.
    equs "B", '"', "A{"                                               ; 89c5: 42 22 41... B"A
    equb &d5, &51, &41, &84, &78,   4, &b7, &69, &85, &97, &a7, &bb   ; 89c9: d5 51 41... .QA
    equb &e1, &a8, &fb, &a8, &6d, &7f, &9b, &1d, &78, &82, &db, &a8   ; 89d5: e1 a8 fb... ...
    equb &e1, &cb, &d1, &e1                                           ; 89e1: e1 cb d1... ...
; &89e5 referenced 1 time by &8e38
.svc_dispatch_hi
    equb &cb, &8e, &8e, &8e, &8c, &8c, &80, &8e, &8e, &a4, &8c, &8e   ; 89e5: cb 8e 8e... ...
    equb &80, &89, &8b, &95, &95, &ac, &95, &95, &9d, &9d, &a1, &a0   ; 89f1: 80 89 8b... ...
    equb &a1, &ad, &8f, &92, &af, &a3, &a3, &a2, &a1, &a2, &a0, &a0   ; 89fd: a1 ad 8f... ...
    equb &a0, &8a                                                     ; 8a09: a0 8a       ..

; ***************************************************************************************
; Service call handler.
; On entry: A=service call number, X=ROM slot, Y=parameter.
; Service 1: absolute workspace claim.
; Service 4: unrecognised star command.
; Service 8: unrecognised OSWORD.
; Service 9: *HELP.
; Service 13: ROM initialisation.
; Service 14: ROM initialisation complete.
; Service 15: vectors claimed.
; ***************************************************************************************
; &8a0b referenced 1 time by &8003
.service_handler
    pha                                                               ; 8a0b: 48          H              ; Save service call number
    cmp #&0f                                                          ; 8a0c: c9 0f       ..             ; Is it service 15 (vectors claimed)?
    bne c8a32                                                         ; 8a0e: d0 22       ."             ; No: skip vectors-claimed handling
    tya                                                               ; 8a10: 98          .              ; Save Y parameter
    pha                                                               ; 8a11: 48          H              ; Save Y on stack
    lda #osbyte_read_os_version                                       ; 8a12: a9 00       ..             ; OSBYTE 0: read OS version
    ldx #1                                                            ; 8a14: a2 01       ..             ; X=1 to request version number

    jsr osbyte                                                        ; 8a16: 20 f4 ff     ..            ; Read OS version number into X
    ; X is the OS version number:
    ;     X=0, OS 1.00 (Early BBC B or Electron OS 1.00)
    ;     X=1, OS 1.20 or American OS
    ;     X=2, OS 2.00 (BBC B+)
    ;     X=3, OS 3.2/3.5 (Master 128)
    ;     X=4, OS 4.0 (Master Econet Terminal)
    ;     X=5, OS 5.0 (Master Compact)
    cpx #1                                                            ; 8a19: e0 01       ..             ; OS 1.20?
    beq c8a2e                                                         ; 8a1b: f0 11       ..             ; Yes: skip workspace setup
    cpx #2                                                            ; 8a1d: e0 02       ..             ; OS 2.00 (BBC B+)?
    beq c8a2e                                                         ; 8a1f: f0 0d       ..             ; Yes: skip workspace setup
    txa                                                               ; 8a21: 8a          .              ; Transfer OS version to A
    php                                                               ; 8a22: 08          .              ; Save flags (Z set if OS 1.00)
    ldx romsel_copy                                                   ; 8a23: a6 f4       ..             ; Get current ROM slot number
    plp                                                               ; 8a25: 28          (              ; Restore flags
    beq c8a29                                                         ; 8a26: f0 01       ..             ; OS 1.00: skip INX
    inx                                                               ; 8a28: e8          .              ; Adjust index for OS 3+ workspace
; &8a29 referenced 1 time by &8a26
.c8a29
    lda #0                                                            ; 8a29: a9 00       ..             ; A=0
    sta l02a0,x                                                       ; 8a2b: 9d a0 02    ...            ; Clear workspace byte for this ROM
; &8a2e referenced 2 times by &8a1b, &8a1f
.c8a2e
    ldx romsel_copy                                                   ; 8a2e: a6 f4       ..             ; Restore ROM slot to X
    pla                                                               ; 8a30: 68          h              ; Restore Y parameter
    tay                                                               ; 8a31: a8          .              ; Transfer to Y
; &8a32 referenced 1 time by &8a0e
.c8a32
    pla                                                               ; 8a32: 68          h              ; Restore service call number
    jsr sub_cbe5e                                                     ; 8a33: 20 5e be     ^.            ; Check relocated code service dispatch
    pha                                                               ; 8a36: 48          H              ; Save service call number
    cmp #1                                                            ; 8a37: c9 01       ..             ; Service 1 (workspace claim)?
    bne c8a50                                                         ; 8a39: d0 15       ..             ; No: skip ADLC check
    lda econet_control1_or_status1                                    ; 8a3b: ad a0 fe    ...            ; Read ADLC status register 1
    and #&ed                                                          ; 8a3e: 29 ed       ).             ; Mask relevant status bits
    bne c8a49                                                         ; 8a40: d0 07       ..             ; Non-zero: ADLC present, set flag
    lda econet_control23_or_status2                                   ; 8a42: ad a1 fe    ...            ; Read ADLC status register 2
    and #&db                                                          ; 8a45: 29 db       ).             ; Mask relevant status bits
    beq c8a50                                                         ; 8a47: f0 07       ..             ; Zero: no ADLC detected, skip
; &8a49 referenced 1 time by &8a40
.c8a49
    rol l0df0,x                                                       ; 8a49: 3e f0 0d    >..            ; Shift bit 7 into carry
    sec                                                               ; 8a4c: 38          8              ; Set carry to mark ADLC present
    ror l0df0,x                                                       ; 8a4d: 7e f0 0d    ~..            ; Rotate carry into bit 7 of slot flag
; &8a50 referenced 2 times by &8a39, &8a47
.c8a50
    lda l0df0,x                                                       ; 8a50: bd f0 0d    ...            ; Load ROM slot flag byte
    asl a                                                             ; 8a53: 0a          .              ; Shift bit 7 (ADLC present) into carry
    pla                                                               ; 8a54: 68          h              ; Restore service call number
    bcc c8a58                                                         ; 8a55: 90 01       ..             ; ADLC not present: continue dispatch
    rts                                                               ; 8a57: 60          `              ; ADLC present: claim service, return

; &8a58 referenced 1 time by &8a55
.c8a58
    cmp #&0f                                                          ; 8a58: c9 0f       ..             ; Service 15 (vectors claimed)?
    bne dispatch_svc_with_state                                       ; 8a5a: d0 43       .C             ; No: handle other services
    ldx ws_0d6a                                                       ; 8a5c: ae 6a 0d    .j.            ; Already initialised?
    bne c8a65                                                         ; 8a5f: d0 04       ..             ; Yes: skip first-time init
    inx                                                               ; 8a61: e8          .              ; X=1 (mark as initialised)
    stx l028d                                                         ; 8a62: 8e 8d 02    ...            ; Set ROM present flag
; &8a65 referenced 1 time by &8a5f
.c8a65
    sta error_block                                                   ; 8a65: 8d 00 01    ...            ; Store service number as ROM counter
; &8a68 referenced 1 time by &8a93
.c8a68
    lda #&80                                                          ; 8a68: a9 80       ..             ; Point to ROM header copyright offset
    sta osrdsc_ptr_hi                                                 ; 8a6a: 85 f7       ..             ; Set high byte of OSRDSC pointer
    lda #&0c                                                          ; 8a6c: a9 0c       ..             ; Offset &0C: copyright string offset
    sta osrdsc_ptr                                                    ; 8a6e: 85 f6       ..             ; Set low byte of OSRDSC pointer
    jsr read_paged_rom                                                ; 8a70: 20 97 8a     ..            ; Read byte from paged ROM via OSRDSC.
; Increments osrdsc_ptr and reads from ROM Y.
    cmp #&4e ; 'N'                                                    ; 8a73: c9 4e       .N             ; First char 'N'?
    bne c8a90                                                         ; 8a75: d0 19       ..             ; No: not a NET ROM, try next
    jsr read_paged_rom                                                ; 8a77: 20 97 8a     ..            ; Read byte from paged ROM via OSRDSC.
; Increments osrdsc_ptr and reads from ROM Y.
    cmp #&45 ; 'E'                                                    ; 8a7a: c9 45       .E             ; Second char 'E'?
    bne c8a90                                                         ; 8a7c: d0 12       ..             ; No: not a NET ROM, try next
    jsr read_paged_rom                                                ; 8a7e: 20 97 8a     ..            ; Read byte from paged ROM via OSRDSC.
; Increments osrdsc_ptr and reads from ROM Y.
    cmp #&54 ; 'T'                                                    ; 8a81: c9 54       .T             ; Third char 'T'?
    bne c8a90                                                         ; 8a83: d0 0b       ..             ; No: not a NET ROM, try next
    ldx error_block                                                   ; 8a85: ae 00 01    ...            ; Get ROM slot being checked
    lda l0df0,x                                                       ; 8a88: bd f0 0d    ...            ; Load its slot flag byte
    ora #&80                                                          ; 8a8b: 09 80       ..             ; Set bit 7 to mark as NET ROM
    sta l0df0,x                                                       ; 8a8d: 9d f0 0d    ...            ; Store updated flag
; &8a90 referenced 3 times by &8a75, &8a7c, &8a83
.c8a90
    dec error_block                                                   ; 8a90: ce 00 01    ...            ; Decrement ROM counter
    bpl c8a68                                                         ; 8a93: 10 d3       ..             ; More ROMs to check: loop
    bmi restore_romsel_rts                                            ; 8a95: 30 32       02             ; ALWAYS branch

; ***************************************************************************************
; Read byte from paged ROM via OSRDSC.
; Increments osrdsc_ptr and reads from ROM Y.
; ***************************************************************************************
; &8a97 referenced 3 times by &8a70, &8a77, &8a7e
.read_paged_rom
    inc osrdsc_ptr                                                    ; 8a97: e6 f6       ..             ; Advance read pointer to next byte
    ldy error_block                                                   ; 8a99: ac 00 01    ...            ; Y=ROM number
    jmp osrdsc                                                        ; 8a9c: 4c b9 ff    L..            ; Read byte from ROM Y or screen

; &8a9f referenced 1 time by &8a5a
.dispatch_svc_with_state
    tax                                                               ; 8a9f: aa          .              ; Transfer service number to X
    lda svc_state                                                     ; 8aa0: a5 a9       ..             ; Save current service state
    pha                                                               ; 8aa2: 48          H              ; Push old state
    txa                                                               ; 8aa3: 8a          .              ; Restore service number to A
    sta svc_state                                                     ; 8aa4: 85 a9       ..             ; Store as current service state
    cmp #&0d                                                          ; 8aa6: c9 0d       ..             ; Service < 13?
    bcc c8ab2                                                         ; 8aa8: 90 08       ..             ; Yes: use as dispatch index directly
    sbc #5                                                            ; 8aaa: e9 05       ..             ; Subtract 5 (map 13-17 to 8-12)
    cmp #&0d                                                          ; 8aac: c9 0d       ..             ; Mapped value = 13? (original was 18)
    beq c8ab2                                                         ; 8aae: f0 02       ..             ; Yes: valid service 18 (FS select)
    lda #0                                                            ; 8ab0: a9 00       ..             ; Unknown service: set index to 0
; &8ab2 referenced 2 times by &8aa8, &8aae
.c8ab2
    tax                                                               ; 8ab2: aa          .              ; Transfer dispatch index to X
    beq c8ac3                                                         ; 8ab3: f0 0e       ..             ; Index 0: unhandled service, skip
    lda ws_page                                                       ; 8ab5: a5 a8       ..             ; Save current workspace page
    pha                                                               ; 8ab7: 48          H              ; Push old page
    sty ws_page                                                       ; 8ab8: 84 a8       ..             ; Set workspace page from Y parameter
    tya                                                               ; 8aba: 98          .              ; Transfer Y to A
    ldy #0                                                            ; 8abb: a0 00       ..             ; Y=0 for dispatch offset
    jsr svc_dispatch                                                  ; 8abd: 20 33 8e     3.            ; Service dispatch via PHA/PHA/RTS.
; On entry: X=base index, Y=additional offset.
; Dispatches to svc_dispatch_lo/hi[X+Y+1].
    pla                                                               ; 8ac0: 68          h              ; Restore old workspace page
    sta ws_page                                                       ; 8ac1: 85 a8       ..             ; Store it back
; &8ac3 referenced 1 time by &8ab3
.c8ac3
    ldx svc_state                                                     ; 8ac3: a6 a9       ..             ; Get service state (return code)
    pla                                                               ; 8ac5: 68          h              ; Restore old service state
    sta svc_state                                                     ; 8ac6: 85 a9       ..             ; Store it back
    txa                                                               ; 8ac8: 8a          .              ; Transfer return code to A
; &8ac9 referenced 1 time by &8a95
.restore_romsel_rts
    ldx romsel_copy                                                   ; 8ac9: a6 f4       ..             ; Restore ROM slot to X
    rts                                                               ; 8acb: 60          `              ; Return to MOS

; ***************************************************************************************
; *ROFF command. Disables remote
; operation. Clears the receive buffer,
; re-enables the keyboard, and resets
; service state.
; ***************************************************************************************
.cmd_roff
    ldy #4                                                            ; 8acc: a0 04       ..             ; Offset 4 in receive block
    lda (net_rx_ptr),y                                                ; 8ace: b1 9c       ..             ; Load remote operation flag
    beq c8af3                                                         ; 8ad0: f0 21       .!             ; Zero: already off, skip to cleanup
    lda #0                                                            ; 8ad2: a9 00       ..             ; A=0
    tax                                                               ; 8ad4: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 8ad5: 91 9c       ..             ; Clear remote operation flag
    tay                                                               ; 8ad7: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 8ad8: a9 c9       ..             ; OSBYTE &C9: keyboard disable
    jsr osbyte                                                        ; 8ada: 20 f4 ff     ..            ; Enable keyboard (for Econet)
    lda #&0a                                                          ; 8add: a9 0a       ..             ; A=&0A: workspace init parameter
    jsr tx_econet_abort                                               ; 8adf: 20 ac a9     ..            ; Initialise workspace area
; &8ae2 referenced 1 time by &9589
.scan_remote_keys
    stx nfs_workspace                                                 ; 8ae2: 86 9e       ..             ; Save X in workspace
    lda #&ce                                                          ; 8ae4: a9 ce       ..             ; A=&CE: start of key range
; &8ae6 referenced 1 time by &8af1
.loop_c8ae6
    ldx nfs_workspace                                                 ; 8ae6: a6 9e       ..             ; Restore X from workspace
    ldy #&7f                                                          ; 8ae8: a0 7f       ..             ; Y=&7F: OSBYTE scan parameter
    jsr osbyte                                                        ; 8aea: 20 f4 ff     ..            ; OSBYTE: scan keyboard
    adc #1                                                            ; 8aed: 69 01       i.             ; Advance to next key code
    cmp #&d0                                                          ; 8aef: c9 d0       ..             ; Reached &D0?
    beq loop_c8ae6                                                    ; 8af1: f0 f3       ..             ; No: loop back (scan &CE and &CF)
; &8af3 referenced 1 time by &8ad0
.c8af3
    lda #0                                                            ; 8af3: a9 00       ..             ; A=0
    sta svc_state                                                     ; 8af5: 85 a9       ..             ; Clear service state
    sta nfs_workspace                                                 ; 8af7: 85 9e       ..             ; Clear workspace byte
    rts                                                               ; 8af9: 60          `              ; Return

; &8afa referenced 3 times by &8c47, &8c72, &a2a7
.save_text_ptr
    pha                                                               ; 8afa: 48          H              ; Save A
    lda os_text_ptr                                                   ; 8afb: a5 f2       ..             ; Copy OS text pointer low
    sta fs_crc_lo                                                     ; 8afd: 85 be       ..             ; to fs_crc_lo
    lda os_text_ptr_hi                                                ; 8aff: a5 f3       ..             ; Copy OS text pointer high
    sta fs_crc_hi                                                     ; 8b01: 85 bf       ..             ; to fs_crc_hi
    pla                                                               ; 8b03: 68          h              ; Restore A
; &8b04 referenced 2 times by &8b07, &8b0c
.return_4
    rts                                                               ; 8b04: 60          `              ; Return

; ***************************************************************************************
; Service 18: filing system selection.
; Selects Econet as the active filing system.
; ***************************************************************************************
.svc_18_fs_select
    cpy #5                                                            ; 8b05: c0 05       ..             ; Y=5 (Econet filing system)?
    bne return_4                                                      ; 8b07: d0 fb       ..             ; No: not ours, return unclaimed
    bit l0d6c                                                         ; 8b09: 2c 6c 0d    ,l.            ; Already selected?
    bmi return_4                                                      ; 8b0c: 30 f6       0.             ; Yes (bit 7 set): return unclaimed
; ***************************************************************************************
; *Net command (file server variant).
; Selects network filing system.
; ***************************************************************************************
; &8b0e referenced 1 time by &8cd5
.cmd_net_fs
    jsr get_ws_page                                                   ; 8b0e: 20 ae 8c     ..            ; Get workspace page for this ROM slot
    sta fs_load_addr_hi                                               ; 8b11: 85 b1       ..             ; Store as high byte of load address
    lda #0                                                            ; 8b13: a9 00       ..             ; A=0
    sta fs_load_addr                                                  ; 8b15: 85 b0       ..             ; Clear low byte of load address
    clc                                                               ; 8b17: 18          .              ; Clear carry for addition
    ldy #&76 ; 'v'                                                    ; 8b18: a0 76       .v             ; Y=&76: checksum range end
; &8b1a referenced 1 time by &8b1d
.loop_c8b1a
    adc (fs_load_addr),y                                              ; 8b1a: 71 b0       q.             ; Add byte to running checksum
    dey                                                               ; 8b1c: 88          .              ; Decrement index
    bpl loop_c8b1a                                                    ; 8b1d: 10 fb       ..             ; Loop until all bytes summed
    ldy #&77 ; 'w'                                                    ; 8b1f: a0 77       .w             ; Y=&77: checksum storage offset
    eor (fs_load_addr),y                                              ; 8b21: 51 b0       Q.             ; Compare with stored checksum
    beq c8b28                                                         ; 8b23: f0 03       ..             ; Match: checksum valid
    jmp error_net_checksum                                            ; 8b25: 4c cb 8f    L..            ; Mismatch: raise checksum error

; &8b28 referenced 1 time by &8b23
.c8b28
    jsr notify_new_fs                                                 ; 8b28: 20 f1 8c     ..            ; Call FSCV with A=6 (new FS)
    ldy #&0d                                                          ; 8b2b: a0 0d       ..             ; Y=&0D: end of FS context block
; &8b2d referenced 1 time by &8b35
.loop_c8b2d
    lda (net_rx_ptr),y                                                ; 8b2d: b1 9c       ..             ; Load byte from receive block
    sta l0dfa,y                                                       ; 8b2f: 99 fa 0d    ...            ; Store into FS workspace
    dey                                                               ; 8b32: 88          .              ; Decrement index
    cpy #5                                                            ; 8b33: c0 05       ..             ; Reached offset 5?
    bne loop_c8b2d                                                    ; 8b35: d0 f6       ..             ; No: continue copying
    rol l0d6c                                                         ; 8b37: 2e 6c 0d    .l.            ; Shift bit 7 of FS flags into carry
    clc                                                               ; 8b3a: 18          .              ; Clear carry
    ror l0d6c                                                         ; 8b3b: 6e 6c 0d    nl.            ; Clear bit 7 of FS flags
    ldy #&0d                                                          ; 8b3e: a0 0d       ..             ; Y=&0D: vector table size - 1
; &8b40 referenced 1 time by &8b47
.loop_c8b40
    lda fs_vector_table,y                                             ; 8b40: b9 4b 8e    .K.            ; Load FS vector address
    sta filev,y                                                       ; 8b43: 99 12 02    ...            ; Store into FILEV vector table
    dey                                                               ; 8b46: 88          .              ; Decrement index
    bpl loop_c8b40                                                    ; 8b47: 10 f7       ..             ; Loop until all vectors installed
    jsr init_adlc_and_vectors                                         ; 8b49: 20 40 8f     @.            ; Initialise ADLC and NMI workspace
    ldy #&1b                                                          ; 8b4c: a0 1b       ..             ; Y=&1B: extended vector offset
    ldx #7                                                            ; 8b4e: a2 07       ..             ; X=7: two more vectors to set up
    jsr write_vector_entry                                            ; 8b50: 20 53 8f     S.            ; Set up extended vectors
    lda #0                                                            ; 8b53: a9 00       ..             ; A=0
    sta l0e07                                                         ; 8b55: 8d 07 0e    ...            ; Clear FS state byte
    sta l10c9                                                         ; 8b58: 8d c9 10    ...            ; Clear workspace byte
    sta l1071                                                         ; 8b5b: 8d 71 10    .q.            ; Clear workspace byte
    sta svc_state                                                     ; 8b5e: 85 a9       ..             ; Clear service state
    ldy #&0e                                                          ; 8b60: a0 0e       ..             ; Offset &0E in receive block
    sta (net_rx_ptr),y                                                ; 8b62: 91 9c       ..             ; Clear receive block flag
    sta l0d6d                                                         ; 8b64: 8d 6d 0d    .m.            ; Clear workspace byte
    jsr setup_ws_ptr                                                  ; 8b67: 20 b5 8c     ..            ; Set up workspace pointers
    jsr init_channel_table                                            ; 8b6a: 20 39 b4     9.            ; Initialise FS state
    ldy #&77 ; 'w'                                                    ; 8b6d: a0 77       .w             ; Y=&77: workspace block size - 1
; &8b6f referenced 1 time by &8b75
.loop_c8b6f
    lda (l00cc),y                                                     ; 8b6f: b1 cc       ..             ; Load byte from source workspace
    sta l1000,y                                                       ; 8b71: 99 00 10    ...            ; Store to page &10 shadow copy
    dey                                                               ; 8b74: 88          .              ; Decrement index
    bpl loop_c8b6f                                                    ; 8b75: 10 f8       ..             ; Loop until all bytes copied
    lda #&80                                                          ; 8b77: a9 80       ..             ; A=&80: FS selected flag
    ora l0d6c                                                         ; 8b79: 0d 6c 0d    .l.            ; Set bit 7 of FS flags
    sta l0d6c                                                         ; 8b7c: 8d 6c 0d    .l.            ; Store updated flags
    jmp issue_svc_15                                                  ; 8b7f: 4c fd 8c    L..            ; Issue service 15 (FS initialised)

; &8b82 referenced 1 time by &8c6f
.help_print_nfs_cmds
    ldx #&4a ; 'J'                                                    ; 8b82: a2 4a       .J             ; X=&4A: NFS command table offset
    jsr print_cmd_table                                               ; 8b84: 20 8d 8b     ..            ; Print help for NFS commands
; ***************************************************************************************
; *Utils command. Dispatches to
; command utility table at offset 0.
; ***************************************************************************************
.cmd_utils
    ldx #0                                                            ; 8b87: a2 00       ..             ; X=0: FS command table offset
    beq print_cmd_table                                               ; 8b89: f0 02       ..             ; ALWAYS branch

; ***************************************************************************************
; *Net command (local variant).
; Selects Econet as active network.
; ***************************************************************************************
.cmd_net_local
    ldx #&4a ; 'J'                                                    ; 8b8b: a2 4a       .J             ; X=&4A: NFS command table offset
; &8b8d referenced 2 times by &8b84, &8b89
.print_cmd_table
    bvc c8b9d                                                         ; 8b8d: 50 0e       P.             ; V clear: need to print header first
    txa                                                               ; 8b8f: 8a          .              ; Save X (table offset)
    pha                                                               ; 8b90: 48          H              ; Push it
    tya                                                               ; 8b91: 98          .              ; Save Y
    pha                                                               ; 8b92: 48          H              ; Push it
    jsr print_version_header                                          ; 8b93: 20 94 8c     ..            ; Print version string header
    pla                                                               ; 8b96: 68          h              ; Restore Y
    tay                                                               ; 8b97: a8          .              ; Transfer to Y
    pla                                                               ; 8b98: 68          h              ; Restore X
    tax                                                               ; 8b99: aa          .              ; Transfer to X
    clv                                                               ; 8b9a: b8          .              ; Clear overflow flag
    bvc print_cmd_table_loop                                          ; 8b9b: 50 03       P.             ; ALWAYS branch

; &8b9d referenced 1 time by &8b8d
.c8b9d
    jsr osnewl                                                        ; 8b9d: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
; &8ba0 referenced 2 times by &8b9b, &8c62
.print_cmd_table_loop
    tya                                                               ; 8ba0: 98          .              ; Save Y (command line offset)
    pha                                                               ; 8ba1: 48          H              ; Push it
    php                                                               ; 8ba2: 08          .              ; Save processor status
; &8ba3 referenced 1 time by &8c21
.c8ba3
    lda cmd_table_fs,x                                                ; 8ba3: bd d8 a3    ...            ; Load byte from command table
    bpl c8bab                                                         ; 8ba6: 10 03       ..             ; Bit 7 clear: valid entry, continue
    jmp c8c24                                                         ; 8ba8: 4c 24 8c    L$.            ; End of table: finish up

; &8bab referenced 1 time by &8ba6
.c8bab
    jsr print_inline                                                  ; 8bab: 20 31 91     1.            ; Print two-space indent
    equs "  "                                                         ; 8bae: 20 20

    ldy #9                                                            ; 8bb0: a0 09       ..             ; Y=9: max command name length
    lda cmd_table_fs,x                                                ; 8bb2: bd d8 a3    ...            ; Load first char of command name
; &8bb5 referenced 1 time by &8bbd
.loop_c8bb5
    jsr osasci                                                        ; 8bb5: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8bb8: e8          .              ; Advance table pointer
    dey                                                               ; 8bb9: 88          .              ; Decrement padding counter
    lda cmd_table_fs,x                                                ; 8bba: bd d8 a3    ...            ; Load next character
    bpl loop_c8bb5                                                    ; 8bbd: 10 f6       ..             ; Bit 7 clear: more chars, continue
; &8bbf referenced 1 time by &8bc5
.loop_c8bbf
    lda #&20 ; ' '                                                    ; 8bbf: a9 20       .              ; Pad with spaces
    jsr osasci                                                        ; 8bc1: 20 e3 ff     ..            ; Write character 32
    dey                                                               ; 8bc4: 88          .              ; Decrement remaining pad count
    bpl loop_c8bbf                                                    ; 8bc5: 10 f8       ..             ; More padding needed: loop
    lda cmd_table_fs,x                                                ; 8bc7: bd d8 a3    ...            ; Load syntax descriptor byte
    and #&1f                                                          ; 8bca: 29 1f       ).             ; Mask to get syntax string index
    cmp #&0e                                                          ; 8bcc: c9 0e       ..             ; Index &0E: shared commands?
    beq c8beb                                                         ; 8bce: f0 1b       ..             ; Yes: handle shared commands list
    tay                                                               ; 8bd0: a8          .              ; Use index as Y
    lda cmd_syntax_table,y                                            ; 8bd1: b9 0e 91    ...            ; Look up syntax string offset
    tay                                                               ; 8bd4: a8          .              ; Transfer offset to Y
; &8bd5 referenced 2 times by &8be2, &8be8
.c8bd5
    iny                                                               ; 8bd5: c8          .              ; Advance to next character
    lda cmd_syntax_strings,y                                          ; 8bd6: b9 0e 90    ...            ; Load syntax string character
    beq c8c1b                                                         ; 8bd9: f0 40       .@             ; Zero terminator: end of syntax
    cmp #&0d                                                          ; 8bdb: c9 0d       ..             ; Carriage return: line continuation
    bne c8be5                                                         ; 8bdd: d0 06       ..             ; No: print the character
    jsr help_wrap_if_serial                                           ; 8bdf: 20 28 8c     (.            ; Handle line wrap in syntax output
    jmp c8bd5                                                         ; 8be2: 4c d5 8b    L..            ; Continue with next character

; &8be5 referenced 1 time by &8bdd
.c8be5
    jsr osasci                                                        ; 8be5: 20 e3 ff     ..            ; Write character
    jmp c8bd5                                                         ; 8be8: 4c d5 8b    L..            ; Continue with next character

; &8beb referenced 1 time by &8bce
.c8beb
    txa                                                               ; 8beb: 8a          .              ; Save table pointer
    pha                                                               ; 8bec: 48          H              ; Push it
    jsr print_inline                                                  ; 8bed: 20 31 91     1.            ; Print opening parenthesis
    equs "("                                                          ; 8bf0: 28          (

    ldy #0                                                            ; 8bf1: a0 00       ..             ; Y=0: shared command counter
    ldx #&d3                                                          ; 8bf3: a2 d3       ..             ; X=&D3: shared command table start
; &8bf5 referenced 1 time by &8c17
.c8bf5
    lda cmd_table_fs,x                                                ; 8bf5: bd d8 a3    ...            ; Load byte from shared command table
    bmi c8c19                                                         ; 8bf8: 30 1f       0.             ; Bit 7 set: end of shared commands
    dex                                                               ; 8bfa: ca          .              ; Back up one position
; &8bfb referenced 1 time by &8c04
.loop_c8bfb
    inx                                                               ; 8bfb: e8          .              ; Advance to next character
    lda cmd_table_fs,x                                                ; 8bfc: bd d8 a3    ...            ; Load command name character
    bmi c8c07                                                         ; 8bff: 30 06       0.             ; Bit 7 set: end of this name
    jsr osasci                                                        ; 8c01: 20 e3 ff     ..            ; Write character
    jmp loop_c8bfb                                                    ; 8c04: 4c fb 8b    L..            ; Print more characters of name

; &8c07 referenced 1 time by &8bff
.c8c07
    and #&7f                                                          ; 8c07: 29 7f       ).             ; Strip bit 7 from final character
    jsr osasci                                                        ; 8c09: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8c0c: c8          .              ; Count this shared command
    cpy #4                                                            ; 8c0d: c0 04       ..             ; Printed 4 commands?
    bne c8c14                                                         ; 8c0f: d0 03       ..             ; No: continue on same line
    jsr help_wrap_if_serial                                           ; 8c11: 20 28 8c     (.            ; Handle line wrap after 4 commands
; &8c14 referenced 1 time by &8c0f
.c8c14
    inx                                                               ; 8c14: e8          .              ; Skip 3 bytes (syntax descriptor)
    inx                                                               ; 8c15: e8          .              ; to advance to next command
    inx                                                               ; 8c16: e8          .              ; in the table
    bne c8bf5                                                         ; 8c17: d0 dc       ..             ; Loop for more shared commands
; &8c19 referenced 1 time by &8bf8
.c8c19
    pla                                                               ; 8c19: 68          h              ; Restore original table pointer
    tax                                                               ; 8c1a: aa          .              ; Transfer to X
; &8c1b referenced 1 time by &8bd9
.c8c1b
    jsr osnewl                                                        ; 8c1b: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    inx                                                               ; 8c1e: e8          .              ; Skip 3 bytes to next table entry
    inx                                                               ; 8c1f: e8          .              ; (syntax descriptor byte,
    inx                                                               ; 8c20: e8          .              ; dispatch address low and high)
    jmp c8ba3                                                         ; 8c21: 4c a3 8b    L..            ; Loop for next command

; &8c24 referenced 1 time by &8ba8
.c8c24
    plp                                                               ; 8c24: 28          (              ; Restore processor status
    pla                                                               ; 8c25: 68          h              ; Restore Y
    tay                                                               ; 8c26: a8          .              ; Transfer to Y
    rts                                                               ; 8c27: 60          `              ; Return

; &8c28 referenced 2 times by &8bdf, &8c11
.help_wrap_if_serial
    lda l0355                                                         ; 8c28: ad 55 03    .U.            ; Read output stream type
    beq return_5                                                      ; 8c2b: f0 15       ..             ; Stream 0 (VDU): no wrapping
    cmp #3                                                            ; 8c2d: c9 03       ..             ; Stream 3 (printer)?
    beq return_5                                                      ; 8c2f: f0 11       ..             ; Yes: no wrapping
    tya                                                               ; 8c31: 98          .              ; Save Y
    pha                                                               ; 8c32: 48          H              ; Push it
    jsr osnewl                                                        ; 8c33: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    ldy #&0b                                                          ; 8c36: a0 0b       ..             ; Y=&0B: indent width - 1
    lda #&20 ; ' '                                                    ; 8c38: a9 20       .              ; Space character
; &8c3a referenced 1 time by &8c3e
.loop_c8c3a
    jsr osasci                                                        ; 8c3a: 20 e3 ff     ..            ; Write character 32
    dey                                                               ; 8c3d: 88          .              ; Decrement indent counter
    bpl loop_c8c3a                                                    ; 8c3e: 10 fa       ..             ; More spaces needed: loop
    pla                                                               ; 8c40: 68          h              ; Restore Y
    tay                                                               ; 8c41: a8          .              ; Transfer to Y
; &8c42 referenced 2 times by &8c2b, &8c2f
.return_5
    rts                                                               ; 8c42: 60          `              ; Return

; ***************************************************************************************
; Service 4: unrecognised star command.
; Parses and dispatches NFS/ANFS star commands.
; ***************************************************************************************
.svc_4_star_command
    ldx #0                                                            ; 8c43: a2 00       ..             ; X=0: start of FS command table
    ldy ws_page                                                       ; 8c45: a4 a8       ..             ; Get command line offset
    jsr save_text_ptr                                                 ; 8c47: 20 fa 8a     ..            ; Save text pointer to fs_crc
    jsr match_fs_cmd                                                  ; 8c4a: 20 28 a1     (.            ; Try to match command in table
    bcs svc_return_unclaimed                                          ; 8c4d: b0 16       ..             ; No match: return to caller
    jmp cmd_fs_reentry                                                ; 8c4f: 4c 0d a1    L..            ; Match found: execute command

; ***************************************************************************************
; Service 9: *HELP.
; Prints NFS version and command list.
; ***************************************************************************************
.svc_9_help
    jsr check_credits_easter_egg                                      ; 8c52: 20 0c 8d     ..            ; Check for credits Easter egg
    ldy ws_page                                                       ; 8c55: a4 a8       ..             ; Get command line offset
    lda (os_text_ptr),y                                               ; 8c57: b1 f2       ..             ; Load character at offset
    cmp #&0d                                                          ; 8c59: c9 0d       ..             ; Is it CR (bare *HELP)?
    bne c8c68                                                         ; 8c5b: d0 0b       ..             ; No: check for specific topic
    jsr print_version_header                                          ; 8c5d: 20 94 8c     ..            ; Print version string
    ldx #&c4                                                          ; 8c60: a2 c4       ..             ; X=&C4: start of help command list
    jsr print_cmd_table_loop                                          ; 8c62: 20 a0 8b     ..            ; Print command list from table
; &8c65 referenced 3 times by &8c4d, &8c92, &8ccd
.svc_return_unclaimed
    ldy ws_page                                                       ; 8c65: a4 a8       ..             ; Restore Y (command line offset)
    rts                                                               ; 8c67: 60          `              ; Return unclaimed

; &8c68 referenced 1 time by &8c5b
.c8c68
    bit bit_test_ff_pad                                               ; 8c68: 2c 7d 94    ,}.            ; Test for topic match (sets flags)
    cmp #&2e ; '.'                                                    ; 8c6b: c9 2e       ..             ; Is first char '.' (abbreviation)?
    bne c8c72                                                         ; 8c6d: d0 03       ..             ; No: try topic-specific help
    jmp help_print_nfs_cmds                                           ; 8c6f: 4c 82 8b    L..            ; '.' found: show full command list

; &8c72 referenced 1 time by &8c6d
.c8c72
    jsr save_text_ptr                                                 ; 8c72: 20 fa 8a     ..            ; Save text pointer to fs_crc
; &8c75 referenced 1 time by &8c90
.loop_c8c75
    php                                                               ; 8c75: 08          .              ; Save flags
    ldx #&c4                                                          ; 8c76: a2 c4       ..             ; X=&C4: help command table start
    jsr match_fs_cmd                                                  ; 8c78: 20 28 a1     (.            ; Try to match help topic in table
    bcs c8c8d                                                         ; 8c7b: b0 10       ..             ; No match: try next topic
    plp                                                               ; 8c7d: 28          (              ; Restore flags
    lda #&8c                                                          ; 8c7e: a9 8c       ..             ; Push return address high (&8C)
    pha                                                               ; 8c80: 48          H              ; Push it for RTS dispatch
    lda #&74 ; 't'                                                    ; 8c81: a9 74       .t             ; Push return address low (&74)
    pha                                                               ; 8c83: 48          H              ; Push it for RTS dispatch
    lda cmd_table_fs_hi,x                                             ; 8c84: bd da a3    ...            ; Load dispatch address high
    pha                                                               ; 8c87: 48          H              ; Push dispatch high for RTS
    lda cmd_table_fs_lo,x                                             ; 8c88: bd d9 a3    ...            ; Load dispatch address low
    pha                                                               ; 8c8b: 48          H              ; Push dispatch low for RTS
    rts                                                               ; 8c8c: 60          `              ; Dispatch via RTS (returns to &8C75)

; &8c8d referenced 1 time by &8c7b
.c8c8d
    plp                                                               ; 8c8d: 28          (              ; Restore flags from before match
    cmp #&0d                                                          ; 8c8e: c9 0d       ..             ; End of command line?
    bne loop_c8c75                                                    ; 8c90: d0 e3       ..             ; No: try matching next topic
    beq svc_return_unclaimed                                          ; 8c92: f0 d1       ..             ; ALWAYS branch

; &8c94 referenced 2 times by &8b93, &8c5d
.print_version_header
    jsr print_inline                                                  ; 8c94: 20 31 91     1.            ; Print version string via inline
.version_string_cr
version_string = version_string_cr+1
    equs &0d, "Advanced  4.08.53", &0d                                ; 8c97: 0d 41 64... .Ad

    nop                                                               ; 8caa: ea          .              ; NOP (string terminator)
    jmp print_station_id                                              ; 8cab: 4c dd 8f    L..            ; Print station number

; &8cae referenced 4 times by &8b0e, &8cb5, &8f6e, &afc2
.get_ws_page
    ldy romsel_copy                                                   ; 8cae: a4 f4       ..             ; Get current ROM slot number
    lda l0df0,y                                                       ; 8cb0: b9 f0 0d    ...            ; Load workspace page for this slot
    tay                                                               ; 8cb3: a8          .              ; Transfer to Y
    rts                                                               ; 8cb4: 60          `              ; Return with page in A and Y

; &8cb5 referenced 2 times by &8b67, &8ece
.setup_ws_ptr
    jsr get_ws_page                                                   ; 8cb5: 20 ae 8c     ..            ; Get workspace page for ROM slot
    sty nfs_temp                                                      ; 8cb8: 84 cd       ..             ; Store page in nfs_temp
    lda #0                                                            ; 8cba: a9 00       ..             ; A=0
    sta l00cc                                                         ; 8cbc: 85 cc       ..             ; Clear low byte of pointer
; &8cbe referenced 1 time by &8ce0
.return_6
    rts                                                               ; 8cbe: 60          `              ; Return

; ***************************************************************************************
; Service 3: auto-boot.
; Handles boot from network on power-up/reset.
; ***************************************************************************************
.svc_3_auto_boot
    lda #osbyte_scan_keyboard_from_16                                 ; 8cbf: a9 7a       .z             ; OSBYTE &7A: scan keyboard from key 16
    jsr osbyte                                                        ; 8cc1: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 8cc4: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi c8cd5                                                         ; 8cc5: 30 0e       0.             ; No key pressed: select Net FS
    cmp #&19                                                          ; 8cc7: c9 19       ..             ; Key &19 (N)?
    beq c8ccf                                                         ; 8cc9: f0 04       ..             ; Yes: write key state and boot
    eor #&55 ; 'U'                                                    ; 8ccb: 49 55       IU             ; EOR with &55: maps to zero if 'N'
    bne svc_return_unclaimed                                          ; 8ccd: d0 96       ..             ; Not N key: return unclaimed
; &8ccf referenced 1 time by &8cc9
.c8ccf
    tay                                                               ; 8ccf: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 8cd0: a9 78       .x             ; OSBYTE &78: write keys pressed
    jsr osbyte                                                        ; 8cd2: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; &8cd5 referenced 1 time by &8cc5
.c8cd5
    jsr cmd_net_fs                                                    ; 8cd5: 20 0e 8b     ..            ; *Net command (file server variant).
; Selects network filing system.
    jsr print_station_id                                              ; 8cd8: 20 dd 8f     ..            ; Print station number
    jsr osnewl                                                        ; 8cdb: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    ldx ws_page                                                       ; 8cde: a6 a8       ..             ; Get workspace page
    bne return_6                                                      ; 8ce0: d0 dc       ..             ; Non-zero: already initialised, return
    lda l1071                                                         ; 8ce2: ad 71 10    .q.            ; Load boot flags
    ora #4                                                            ; 8ce5: 09 04       ..             ; Set bit 2 (auto-boot in progress)
    sta l1071                                                         ; 8ce7: 8d 71 10    .q.            ; Store updated boot flags
    ldx #4                                                            ; 8cea: a2 04       ..             ; X=4: boot filename parameter
    ldy #&8d                                                          ; 8cec: a0 8d       ..             ; Y=&8D: boot filename address high
    jmp cmd_fs_entry                                                  ; 8cee: 4c fc a0    L..            ; Execute boot file

; &8cf1 referenced 1 time by &8b28
.notify_new_fs
    lda #6                                                            ; 8cf1: a9 06       ..             ; A=6: notify new filing system
    jsr call_fscv                                                     ; 8cf3: 20 fa 8c     ..            ; Call FSCV
    ldx #&0a                                                          ; 8cf6: a2 0a       ..             ; X=&0A: service 10 parameter
    bne c8cff                                                         ; 8cf8: d0 05       ..             ; ALWAYS branch

; &8cfa referenced 1 time by &8cf3
.call_fscv
    jmp (fscv)                                                        ; 8cfa: 6c 1e 02    l..            ; Dispatch via FSCV

; &8cfd referenced 1 time by &8b7f
.issue_svc_15
    ldx #&0f                                                          ; 8cfd: a2 0f       ..             ; X=&0F: service 15 parameter
; &8cff referenced 1 time by &8cf8
.c8cff
    lda #osbyte_issue_service_request                                 ; 8cff: a9 8f       ..             ; OSBYTE &8F: issue service request
    jmp osbyte                                                        ; 8d01: 4c f4 ff    L..            ; Issue paged ROM service call

    equs "i .boot"                                                    ; 8d04: 69 20 2e... i .
    equb &0d                                                          ; 8d0b: 0d          .

; &8d0c referenced 1 time by &8c52
.check_credits_easter_egg
    ldy ws_page                                                       ; 8d0c: a4 a8       ..             ; Get command line offset
    ldx #5                                                            ; 8d0e: a2 05       ..             ; X=5: start of credits keyword
; &8d10 referenced 1 time by &8d19
.loop_c8d10
    lda (os_text_ptr),y                                               ; 8d10: b1 f2       ..             ; Load character from command line
    cmp credits_keyword_start,x                                       ; 8d12: dd 2d 8d    .-.            ; Compare with credits keyword
    bne c8d1b                                                         ; 8d15: d0 04       ..             ; Mismatch: check if keyword complete
    iny                                                               ; 8d17: c8          .              ; Advance command line pointer
    inx                                                               ; 8d18: e8          .              ; Advance keyword pointer
    bne loop_c8d10                                                    ; 8d19: d0 f5       ..             ; Continue matching
; &8d1b referenced 1 time by &8d15
.c8d1b
    cpx #&0d                                                          ; 8d1b: e0 0d       ..             ; Reached end of keyword (X=&0D)?
    bne return_7                                                      ; 8d1d: d0 0d       ..             ; No: keyword not fully matched, return
    ldx #0                                                            ; 8d1f: a2 00       ..             ; X=0: start of credits text
; &8d21 referenced 1 time by &8d2a
.loop_c8d21
    lda credits_keyword_start,x                                       ; 8d21: bd 2d 8d    .-.            ; Load character from credits string
    beq return_7                                                      ; 8d24: f0 06       ..             ; Zero terminator: done printing
    jsr osasci                                                        ; 8d26: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8d29: e8          .              ; Advance string pointer
    bne loop_c8d21                                                    ; 8d2a: d0 f5       ..             ; Continue printing
; &8d2c referenced 2 times by &8d1d, &8d24
.return_7
    rts                                                               ; 8d2c: 60          `              ; Return

; &8d2d referenced 2 times by &8d12, &8d21
.credits_keyword_start
    equb &0d                                                          ; 8d2d: 0d          .
.credits_string
    equs "The authors of ANFS are;"                                   ; 8d2e: 54 68 65... The
    equb &0d                                                          ; 8d46: 0d          .
    equs "B Co"                                                       ; 8d47: 42 20 43... B C
; &8d4b referenced 1 time by &affb
.credits_string_mid
    equs "ckburn"                                                     ; 8d4b: 63 6b 62... ckb
    equb &0d                                                          ; 8d51: 0d          .
    equs "J Dunn"                                                     ; 8d52: 4a 20 44... J D
    equb &0d                                                          ; 8d58: 0d          .
    equs "B Robertson"                                                ; 8d59: 42 20 52... B R
    equb &0d                                                          ; 8d64: 0d          .
    equs "J Wills"                                                    ; 8d65: 4a 20 57... J W
    equb &0d, 0                                                       ; 8d6c: 0d 00       ..

; ***************************************************************************************
; *I am command.
; Logs onto the file server with user credentials.
; ***************************************************************************************
.cmd_iam
    tya                                                               ; 8d6e: 98          .              ; Save Y (command line offset)
    pha                                                               ; 8d6f: 48          H              ; Push it
    lda #osbyte_close_spool_exec                                      ; 8d70: a9 77       .w             ; OSBYTE &77: close SPOOL/EXEC
    sta l0e07                                                         ; 8d72: 8d 07 0e    ...            ; Store as pending operation marker
    jsr osbyte                                                        ; 8d75: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 8d78: a0 00       ..             ; Y=0
    sty fs_work_4                                                     ; 8d7a: 84 b4       ..             ; Clear password entry flag
    jsr process_all_fcbs                                              ; 8d7c: 20 9f b7     ..            ; Reset FS connection state
    lda #0                                                            ; 8d7f: a9 00       ..             ; A=0
    sta l0e07                                                         ; 8d81: 8d 07 0e    ...            ; Clear pending operation marker
    pla                                                               ; 8d84: 68          h              ; Restore command line offset
    tay                                                               ; 8d85: a8          .              ; Transfer to Y
    lda (fs_options),y                                                ; 8d86: b1 bb       ..             ; Load first option byte
    jsr is_decimal_digit                                              ; 8d88: 20 44 92     D.            ; Parse station number if present
    bcc cmd_pass                                                      ; 8d8b: 90 24       .$             ; *Pass command.
; Changes file server password.
    jsr parse_addr_arg                                                ; 8d8d: 20 5a 91     Z.            ; Parse user ID string
    bcs c8d9c                                                         ; 8d90: b0 0a       ..             ; No user ID: go to password
    sta l0e01                                                         ; 8d92: 8d 01 0e    ...            ; Store file server station low
    jsr clear_if_station_match                                        ; 8d95: 20 fe 8d     ..            ; Check and store FS network
    iny                                                               ; 8d98: c8          .              ; Skip separator
    jsr parse_addr_arg                                                ; 8d99: 20 5a 91     Z.            ; Parse next argument
; &8d9c referenced 1 time by &8d90
.c8d9c
    beq cmd_pass                                                      ; 8d9c: f0 13       ..             ; *Pass command.
; Changes file server password.
    sta l0e00                                                         ; 8d9e: 8d 00 0e    ...            ; Store file server station high
    ldx #&ff                                                          ; 8da1: a2 ff       ..             ; X=&FF: pre-decrement for loop
; &8da3 referenced 1 time by &8daa
.loop_c8da3
    inx                                                               ; 8da3: e8          .              ; Advance index
    lda cmd_table_nfs_iam,x                                           ; 8da4: bd 5f a4    ._.            ; Load logon command template byte
    sta l0f05,x                                                       ; 8da7: 9d 05 0f    ...            ; Store into transmit buffer
    bpl loop_c8da3                                                    ; 8daa: 10 f7       ..             ; Bit 7 clear: more bytes, loop
    jsr copy_arg_validated                                            ; 8dac: 20 f4 ae     ..            ; Send logon with file server lookup
    beq scan_pass_prompt                                              ; 8daf: f0 03       ..             ; Success: skip to password entry
; ***************************************************************************************
; *Pass command.
; Changes file server password.
; ***************************************************************************************
; &8db1 referenced 2 times by &8d8b, &8d9c
.cmd_pass
    jsr copy_arg_to_buf_x0                                            ; 8db1: 20 f0 ae     ..            ; Build FS command packet
; &8db4 referenced 1 time by &8daf
.scan_pass_prompt
    ldy #&ff                                                          ; 8db4: a0 ff       ..             ; Y=&FF: pre-increment for loop
; &8db6 referenced 1 time by &8dc0
.loop_c8db6
    iny                                                               ; 8db6: c8          .              ; Advance to next byte
    lda l0f05,y                                                       ; 8db7: b9 05 0f    ...            ; Load byte from reply buffer
    cmp #&0d                                                          ; 8dba: c9 0d       ..             ; Is it CR (end of prompt)?
    beq c8def                                                         ; 8dbc: f0 31       .1             ; Yes: no colon found, skip to send
    cmp #&3a ; ':'                                                    ; 8dbe: c9 3a       .:             ; Is it ':' (password prompt)?
    bne loop_c8db6                                                    ; 8dc0: d0 f4       ..             ; No: keep scanning
    jsr oswrch                                                        ; 8dc2: 20 ee ff     ..            ; Write character
    sty fs_work_4                                                     ; 8dc5: 84 b4       ..             ; Save position of colon
; &8dc7 referenced 4 times by &8dd7, &8ddb, &8dde, &8dea
.c8dc7
    lda #&ff                                                          ; 8dc7: a9 ff       ..             ; A=&FF: mark as escapable
    sta escapable                                                     ; 8dc9: 85 97       ..             ; Set escape flag
    jsr check_escape                                                  ; 8dcb: 20 5a 95     Z.            ; Check for escape condition
    jsr osrdch                                                        ; 8dce: 20 e0 ff     ..            ; Read a character from the current input stream
    cmp #&15                                                          ; 8dd1: c9 15       ..             ; A=character read
    bne c8de0                                                         ; 8dd3: d0 0b       ..             ; Not NAK (&15): check other chars
    ldy fs_work_4                                                     ; 8dd5: a4 b4       ..             ; Restore colon position
    bne c8dc7                                                         ; 8dd7: d0 ee       ..             ; Non-zero: restart from colon
; &8dd9 referenced 1 time by &8de2
.loop_c8dd9
    cpy fs_work_4                                                     ; 8dd9: c4 b4       ..             ; At colon position?
    beq c8dc7                                                         ; 8ddb: f0 ea       ..             ; Yes: restart password input
    dey                                                               ; 8ddd: 88          .              ; Backspace: move back one character
    bne c8dc7                                                         ; 8dde: d0 e7       ..             ; If not at start: restart input
; &8de0 referenced 1 time by &8dd3
.c8de0
    cmp #&7f                                                          ; 8de0: c9 7f       ..             ; Delete key (&7F)?
    beq loop_c8dd9                                                    ; 8de2: f0 f5       ..             ; Yes: handle backspace
    sta l0f05,y                                                       ; 8de4: 99 05 0f    ...            ; Store character in password buffer
    iny                                                               ; 8de7: c8          .              ; Advance buffer pointer
    cmp #&0d                                                          ; 8de8: c9 0d       ..             ; Is it CR (end of password)?
    bne c8dc7                                                         ; 8dea: d0 db       ..             ; No: read another character
    jsr osnewl                                                        ; 8dec: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
; &8def referenced 1 time by &8dbc
.c8def
    tya                                                               ; 8def: 98          .              ; Transfer string length to A
    pha                                                               ; 8df0: 48          H              ; Save string length
    jsr init_txcb                                                     ; 8df1: 20 5f 94     _.            ; Set up transmit control block
    jsr init_tx_ptr_for_pass                                          ; 8df4: 20 7f 98     ..            ; Send to file server and get reply
    pla                                                               ; 8df7: 68          h              ; Restore string length
    tax                                                               ; 8df8: aa          .              ; Transfer to X (byte count)
    inx                                                               ; 8df9: e8          .              ; Include terminator
    ldy #0                                                            ; 8dfa: a0 00       ..             ; Y=0
    beq send_cmd_and_dispatch                                         ; 8dfc: f0 10       ..             ; ALWAYS branch

; &8dfe referenced 1 time by &8d95
.clear_if_station_match
    jsr init_bridge_poll                                              ; 8dfe: 20 68 a8     h.            ; Parse station number from cmd line
    eor l0e01                                                         ; 8e01: 4d 01 0e    M..            ; Compare with expected station
    bne return_8                                                      ; 8e04: d0 03       ..             ; Different: return without clearing
    sta l0e01                                                         ; 8e06: 8d 01 0e    ...            ; Same: clear station byte
; &8e09 referenced 1 time by &8e04
.return_8
    rts                                                               ; 8e09: 60          `              ; Return

; &8e0a referenced 1 time by &944e
.pass_send_cmd
    jsr copy_arg_to_buf_x0                                            ; 8e0a: 20 f0 ae     ..            ; Build FS command packet
    tay                                                               ; 8e0d: a8          .              ; Transfer result to Y
; &8e0e referenced 2 times by &8dfc, &9310
.send_cmd_and_dispatch
    jsr save_net_tx_cb                                                ; 8e0e: 20 99 94     ..            ; Set up command and send to FS
    ldx l0f03                                                         ; 8e11: ae 03 0f    ...            ; Load reply function code
    beq return_9                                                      ; 8e14: f0 2c       .,             ; Zero: no reply, return
    lda l0f05                                                         ; 8e16: ad 05 0f    ...            ; Load first reply byte
    ldy #&17                                                          ; 8e19: a0 17       ..             ; Y=&17: logon dispatch offset
    bne svc_dispatch                                                  ; 8e1b: d0 16       ..             ; Service dispatch via PHA/PHA/RTS.
; On entry: X=base index, Y=additional offset.
; Dispatches to svc_dispatch_lo/hi[X+Y+1].; ALWAYS branch

    jsr set_xfer_params                                               ; 8e1d: 20 81 92     ..            ; Parse reply as decimal number
    cmp #8                                                            ; 8e20: c9 08       ..             ; Result >= 8?
    bcs return_9                                                      ; 8e22: b0 1e       ..             ; Yes: out of range, return
    tax                                                               ; 8e24: aa          .              ; Transfer handle to X
    jsr mask_owner_access                                             ; 8e25: 20 12 af     ..            ; Look up in open files table
    tya                                                               ; 8e28: 98          .              ; Transfer result to A
    ldy #&13                                                          ; 8e29: a0 13       ..             ; Y=&13: handle dispatch offset
    bne svc_dispatch                                                  ; 8e2b: d0 06       ..             ; Service dispatch via PHA/PHA/RTS.
; On entry: X=base index, Y=additional offset.
; Dispatches to svc_dispatch_lo/hi[X+Y+1].; ALWAYS branch

    cpx #5                                                            ; 8e2d: e0 05       ..             ; Handle >= 5?
    bcs return_9                                                      ; 8e2f: b0 11       ..             ; Yes: out of range, return
    ldy #&0e                                                          ; 8e31: a0 0e       ..             ; Y=&0E: directory dispatch offset
; ***************************************************************************************
; Service dispatch via PHA/PHA/RTS.
; On entry: X=base index, Y=additional offset.
; Dispatches to svc_dispatch_lo/hi[X+Y+1].
; ***************************************************************************************
; &8e33 referenced 5 times by &8abd, &8e1b, &8e2b, &8e35, &8e8c
.svc_dispatch
    inx                                                               ; 8e33: e8          .              ; Advance X to target index
    dey                                                               ; 8e34: 88          .              ; Decrement Y offset counter
    bpl svc_dispatch                                                  ; 8e35: 10 fc       ..             ; Service dispatch via PHA/PHA/RTS.
; On entry: X=base index, Y=additional offset.
; Dispatches to svc_dispatch_lo/hi[X+Y+1].
    tay                                                               ; 8e37: a8          .              ; Y=&FF: will be ignored by caller
    lda svc_dispatch_hi,x                                             ; 8e38: bd e5 89    ...            ; Load dispatch address high byte
    pha                                                               ; 8e3b: 48          H              ; Push high byte for RTS dispatch
.push_dispatch_lo
svc_dispatch_lo_offset = push_dispatch_lo+2
    lda svc_dispatch_lo,x                                             ; 8e3c: bd c0 89    ...            ; Load dispatch address low byte
; &8e3e referenced 2 times by &8f53, &8f59
    pha                                                               ; 8e3f: 48          H              ; Push low byte for RTS dispatch
    ldx fs_options                                                    ; 8e40: a6 bb       ..             ; Load FS options pointer
; &8e42 referenced 3 times by &8e14, &8e22, &8e2f
.return_9
    rts                                                               ; 8e42: 60          `              ; Dispatch via RTS

.print_string
    equs "PRINT "                                                     ; 8e43: 50 52 49... PRI
    equb 1, 0                                                         ; 8e49: 01 00       ..
; &8e4b referenced 1 time by &8b40
.fs_vector_table
    equb &1b, &ff, &1e, &ff, &21, &ff, &24, &ff, &27, &ff, &2a, &ff   ; 8e4b: 1b ff 1e... ...
    equb &2d, &ff, &21, &99, &4a, &af, &9b, &44, &cf, &b7, &57, &50   ; 8e57: 2d ff 21... -.!
    equb &b8, &42, &23, &9e, &41, &42, &9d, &52, &1d, &8e             ; 8e63: b8 42 23... .B#

; ***************************************************************************************
; OSBYTE with X=0, Y=&FF.
; Called from dispatch table for specific OSBYTE calls.
; ***************************************************************************************
; &8e6d referenced 3 times by &8076, &8f45, &96fa
.osbyte_x0
    ldx #0                                                            ; 8e6d: a2 00       ..             ; X=0
; ***************************************************************************************
; OSBYTE with Y=&FF.
; Entry with X already set by caller.
; ***************************************************************************************
; &8e6f referenced 1 time by &8080
.osbyte_yff
    ldy #&ff                                                          ; 8e6f: a0 ff       ..             ; Y=&FF
; &8e71 referenced 1 time by &8e7a
.loop_c8e71
    jmp osbyte                                                        ; 8e71: 4c f4 ff    L..            ; Execute OSBYTE and return

    equb &68, &a9                                                     ; 8e74: 68 a9       h.

; &8e76 referenced 1 time by &970d
.osbyte_x0_y0
    ldx #0                                                            ; 8e76: a2 00       ..             ; X=0
    ldy #0                                                            ; 8e78: a0 00       ..             ; Y=0
    beq loop_c8e71                                                    ; 8e7a: f0 f5       ..             ; ALWAYS branch

; ***************************************************************************************
; Service 7: unrecognised OSBYTE.
; Handles Econet-specific OSBYTE calls.
; ***************************************************************************************
.svc_7_osbyte
    lda osbyte_a_copy                                                 ; 8e7c: a5 ef       ..             ; Get original OSBYTE A parameter
    sbc #&31 ; '1'                                                    ; 8e7e: e9 31       .1             ; Subtract &31 (map &32-&35 to 1-4)
    cmp #4                                                            ; 8e80: c9 04       ..             ; In range 0-3?
    bcs return_10                                                     ; 8e82: b0 11       ..             ; No: not ours, return unclaimed
    tax                                                               ; 8e84: aa          .              ; Transfer to X as dispatch index
    lda #0                                                            ; 8e85: a9 00       ..             ; A=0: claim the service call
    sta svc_state                                                     ; 8e87: 85 a9       ..             ; Set return value to 0 (claimed)
    tya                                                               ; 8e89: 98          .              ; Transfer Y to A (OSBYTE Y param)
    ldy #&21 ; '!'                                                    ; 8e8a: a0 21       .!             ; Y=&21: OSBYTE dispatch offset
    jmp svc_dispatch                                                  ; 8e8c: 4c 33 8e    L3.            ; Service dispatch via PHA/PHA/RTS.
; On entry: X=base index, Y=additional offset.
; Dispatches to svc_dispatch_lo/hi[X+Y+1].

; ***************************************************************************************
; Service 1: absolute workspace claim.
; Claims workspace pages for NFS use.
; ***************************************************************************************
.svc_1_workspace_claim
    cpy #&16                                                          ; 8e8f: c0 16       ..             ; Need at least &16 pages?
    bcs return_10                                                     ; 8e91: b0 02       ..             ; Already enough: return
    ldy #&16                                                          ; 8e93: a0 16       ..             ; Request &16 pages of workspace
; &8e95 referenced 2 times by &8e82, &8e91
.return_10
    rts                                                               ; 8e95: 60          `              ; Return

; &8e96 referenced 1 time by &8ec6
.store_ws_page_count
    tya                                                               ; 8e96: 98          .              ; Transfer Y to A
    cmp #&21 ; '!'                                                    ; 8e97: c9 21       .!             ; Y >= &21?
    bcc c8e9d                                                         ; 8e99: 90 02       ..             ; No: use Y as-is
    lda #&21 ; '!'                                                    ; 8e9b: a9 21       .!             ; Cap at &21
; &8e9d referenced 1 time by &8e99
.c8e9d
    ldy #&0f                                                          ; 8e9d: a0 0f       ..             ; Offset &0F in receive block
    sta (net_rx_ptr),y                                                ; 8e9f: 91 9c       ..             ; Store workspace page count
    rts                                                               ; 8ea1: 60          `              ; Return

; ***************************************************************************************
; Service 2: private workspace claim.
; Allocates private workspace page and initialises FS state.
; ***************************************************************************************
.svc_2_private_workspace
    sty net_rx_ptr_hi                                                 ; 8ea2: 84 9d       ..             ; Store Y as receive block page
    iny                                                               ; 8ea4: c8          .              ; Advance to next page
    sty nfs_workspace_hi                                              ; 8ea5: 84 9f       ..             ; Store as NFS workspace page
    iny                                                               ; 8ea7: c8          .              ; Advance to next page
    tya                                                               ; 8ea8: 98          .              ; Transfer page to A
    ldy romsel_copy                                                   ; 8ea9: a4 f4       ..             ; Get current ROM slot number
    sta l0df0,y                                                       ; 8eab: 99 f0 0d    ...            ; Store workspace page for this slot
    lda #0                                                            ; 8eae: a9 00       ..             ; A=0
    sta net_rx_ptr                                                    ; 8eb0: 85 9c       ..             ; Clear receive block pointer low
    sta nfs_workspace                                                 ; 8eb2: 85 9e       ..             ; Clear NFS workspace pointer low
    sta ws_page                                                       ; 8eb4: 85 a8       ..             ; Clear workspace page counter
    sta ws_0d60                                                       ; 8eb6: 8d 60 0d    .`.            ; Clear workspace byte
    ldy #4                                                            ; 8eb9: a0 04       ..             ; Offset 4 in receive block
    sta (net_rx_ptr),y                                                ; 8ebb: 91 9c       ..             ; Clear remote operation flag
    lda #osbyte_issue_service_request                                 ; 8ebd: a9 8f       ..             ; OSBYTE &8F: issue service request
    ldx #1                                                            ; 8ebf: a2 01       ..             ; X=1: workspace claim service
    ldy #&0e                                                          ; 8ec1: a0 0e       ..             ; Y=&0E: requested pages
    jsr osbyte                                                        ; 8ec3: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=1 - Absolute public workspace claim
    jsr store_ws_page_count                                           ; 8ec6: 20 96 8e     ..            ; Record final workspace allocation
    lda l028d                                                         ; 8ec9: ad 8d 02    ...            ; Load ROM present flag
    beq c8f23                                                         ; 8ecc: f0 55       .U             ; Zero: first ROM init, skip FS setup
    jsr setup_ws_ptr                                                  ; 8ece: 20 b5 8c     ..            ; Set up workspace pointers
    sta l0d6c                                                         ; 8ed1: 8d 6c 0d    .l.            ; Clear FS flags
    tay                                                               ; 8ed4: a8          .              ; A=0, transfer to Y
; &8ed5 referenced 1 time by &8eda
.loop_c8ed5
    sta (l00cc),y                                                     ; 8ed5: 91 cc       ..             ; Clear byte in FS workspace
    sta (nfs_workspace),y                                             ; 8ed7: 91 9e       ..             ; Clear byte in NFS workspace
    iny                                                               ; 8ed9: c8          .              ; Advance index
    bne loop_c8ed5                                                    ; 8eda: d0 f9       ..             ; Loop until full page zeroed
    ldy #&0c                                                          ; 8edc: a0 0c       ..             ; Offset &0C in receive block
    sta (net_rx_ptr),y                                                ; 8ede: 91 9c       ..             ; Clear protection flags
    jsr copy_ps_data_y1c                                              ; 8ee0: 20 f7 af     ..            ; Initialise station identity block
    ldy #6                                                            ; 8ee3: a0 06       ..             ; Offset 6 in receive block
    lda #&fe                                                          ; 8ee5: a9 fe       ..             ; A=&FE: default station ID marker
    sta l0e00                                                         ; 8ee7: 8d 00 0e    ...            ; Store default station low
    sta (net_rx_ptr),y                                                ; 8eea: 91 9c       ..             ; Store into receive block
    lda #0                                                            ; 8eec: a9 00       ..             ; A=0
    sta l0e01                                                         ; 8eee: 8d 01 0e    ...            ; Clear station high byte
    iny                                                               ; 8ef1: c8          .              ; Y=&07
    sta (net_rx_ptr),y                                                ; 8ef2: 91 9c       ..             ; Store into receive block
    ldy #3                                                            ; 8ef4: a0 03       ..             ; Offset 3 in NFS workspace
    sta (nfs_workspace),y                                             ; 8ef6: 91 9e       ..             ; Clear NFS workspace byte 3
    dey                                                               ; 8ef8: 88          .              ; Y=&02
    lda #&eb                                                          ; 8ef9: a9 eb       ..             ; A=&EB: default listen state
    sta (nfs_workspace),y                                             ; 8efb: 91 9e       ..             ; Store at NFS workspace offset 2
    ldx #3                                                            ; 8efd: a2 03       ..             ; X=3: init data byte count
; &8eff referenced 1 time by &8f06
.loop_c8eff
    lda ws_init_data,x                                                ; 8eff: bd 2b 8f    .+.            ; Load initialisation data byte
    sta l0d6d,x                                                       ; 8f02: 9d 6d 0d    .m.            ; Store in workspace
    dex                                                               ; 8f05: ca          .              ; Decrement counter
    bne loop_c8eff                                                    ; 8f06: d0 f7       ..             ; More bytes: loop
    stx ws_0d68                                                       ; 8f08: 8e 68 0d    .h.            ; Clear workspace flag
    stx l0e05                                                         ; 8f0b: 8e 05 0e    ...            ; Clear workspace byte
    jsr reset_spool_buf_state                                         ; 8f0e: 20 d0 aa     ..            ; Initialise ADLC protection table
; &8f11 referenced 1 time by &8f1e
.loop_c8f11
    lda ws_page                                                       ; 8f11: a5 a8       ..             ; Get current workspace page
    jsr byte_to_2bit_index                                            ; 8f13: 20 b6 a0     ..            ; Allocate FS handle page
    bcs c8f23                                                         ; 8f16: b0 0b       ..             ; Allocation failed: finish init
    lda #&3f ; '?'                                                    ; 8f18: a9 3f       .?             ; A=&3F: default handle permissions
    sta (nfs_workspace),y                                             ; 8f1a: 91 9e       ..             ; Store handle permissions
    inc ws_page                                                       ; 8f1c: e6 a8       ..             ; Advance to next page
    bne loop_c8f11                                                    ; 8f1e: d0 f1       ..             ; Continue allocating: loop
    jsr restore_fs_context                                            ; 8f20: 20 73 8f     s.            ; Restore FS context from saved state
; &8f23 referenced 2 times by &8ecc, &8f16
.c8f23
    ldy station_id_disable_net_nmis                                   ; 8f23: ac 18 fe    ...            ; Read station ID from hardware
    tya                                                               ; 8f26: 98          .              ; Transfer to A
    bne c8f2f                                                         ; 8f27: d0 06       ..             ; Non-zero: station ID valid
; &8f29 referenced 1 time by &8f30
.loop_c8f29
ws_init_data = loop_c8f29+2
    jmp err_bad_station_num                                           ; 8f29: 4c 01 92    L..            ; Station 0: report error

; &8f2b referenced 1 time by &8eff
    equb &ff, &28, &0a                                                ; 8f2c: ff 28 0a    .(.

; &8f2f referenced 1 time by &8f27
.c8f2f
    iny                                                               ; 8f2f: c8          .              ; Increment station ID
    beq loop_c8f29                                                    ; 8f30: f0 f7       ..             ; Overflow to 0: report error
    ldy #5                                                            ; 8f32: a0 05       ..             ; Offset 5: station ID in recv block
    sta (net_rx_ptr),y                                                ; 8f34: 91 9c       ..             ; Store station ID
    ldx #&40 ; '@'                                                    ; 8f36: a2 40       .@             ; X=&40: Econet flag byte
    stx l0d61                                                         ; 8f38: 8e 61 0d    .a.            ; Store Econet control flag
    lda #3                                                            ; 8f3b: a9 03       ..             ; A=3: protection level
    jsr handle_spool_ctrl_byte                                        ; 8f3d: 20 09 ab     ..            ; Set up Econet protection
; &8f40 referenced 1 time by &8b49
.init_adlc_and_vectors
    jsr adlc_init                                                     ; 8f40: 20 69 80     i.            ; Initialise ADLC: full hardware reset then
; configure for receive/listen mode.
; Falls through to init_nmi_workspace.
    lda #&a8                                                          ; 8f43: a9 a8       ..             ; OSBYTE &A8: read ROM pointer table
    jsr osbyte_x0                                                     ; 8f45: 20 6d 8e     m.            ; OSBYTE with X=0, Y=&FF.
; Called from dispatch table for specific OSBYTE calls.
    stx fs_error_ptr                                                  ; 8f48: 86 b8       ..             ; Store table pointer low
    sty fs_crflag                                                     ; 8f4a: 84 b9       ..             ; Store table pointer high
    ldy #&36 ; '6'                                                    ; 8f4c: a0 36       .6             ; Y=&36: NETV vector offset
    sty netv                                                          ; 8f4e: 8c 24 02    .$.            ; Set NETV address
    ldx #1                                                            ; 8f51: a2 01       ..             ; X=1: one more vector pair to set
; &8f53 referenced 2 times by &8b50, &8f65
.write_vector_entry
    lda svc_dispatch_lo_offset,y                                      ; 8f53: b9 3e 8e    .>.            ; Load vector address low byte
    sta (fs_error_ptr),y                                              ; 8f56: 91 b8       ..             ; Store into extended vector table
    iny                                                               ; 8f58: c8          .              ; Advance to high byte
    lda svc_dispatch_lo_offset,y                                      ; 8f59: b9 3e 8e    .>.            ; Load vector address high byte
    sta (fs_error_ptr),y                                              ; 8f5c: 91 b8       ..             ; Store into extended vector table
    iny                                                               ; 8f5e: c8          .              ; Advance to ROM ID byte
    lda romsel_copy                                                   ; 8f5f: a5 f4       ..             ; Load current ROM slot number
    sta (fs_error_ptr),y                                              ; 8f61: 91 b8       ..             ; Store ROM ID in extended vector
    iny                                                               ; 8f63: c8          .              ; Advance to next vector entry
    dex                                                               ; 8f64: ca          .              ; Decrement vector counter
    bne write_vector_entry                                            ; 8f65: d0 ec       ..             ; More vectors to set: loop
    dex                                                               ; 8f67: ca          .              ; X=&FF
    stx l0d72                                                         ; 8f68: 8e 72 0d    .r.            ; Store &FF in workspace flag
    jsr deselect_fs_if_active                                         ; 8f6b: 20 80 8f     ..            ; Restore FS state if previously active
    jsr get_ws_page                                                   ; 8f6e: 20 ae 8c     ..            ; Get workspace page for ROM slot
    iny                                                               ; 8f71: c8          .              ; Advance Y past workspace page
    rts                                                               ; 8f72: 60          `              ; Return

; &8f73 referenced 3 times by &8f20, &8f8f, &a376
.restore_fs_context
    ldy #&0d                                                          ; 8f73: a0 0d       ..             ; Y=&0D: end of FS context block
; &8f75 referenced 1 time by &8f7d
.loop_c8f75
    lda l0dfa,y                                                       ; 8f75: b9 fa 0d    ...            ; Load FS context byte
    sta (net_rx_ptr),y                                                ; 8f78: 91 9c       ..             ; Store into receive block
    dey                                                               ; 8f7a: 88          .              ; Decrement index
    cpy #5                                                            ; 8f7b: c0 05       ..             ; Reached offset 5?
    bne loop_c8f75                                                    ; 8f7d: d0 f6       ..             ; No: continue copying
    rts                                                               ; 8f7f: 60          `              ; Return

; &8f80 referenced 1 time by &8f6b
.deselect_fs_if_active
    bit l0d6c                                                         ; 8f80: 2c 6c 0d    ,l.            ; FS currently selected?
    bpl return_11                                                     ; 8f83: 10 2c       .,             ; No (bit 7 clear): return
    ldy #0                                                            ; 8f85: a0 00       ..             ; Y=0
    jsr process_all_fcbs                                              ; 8f87: 20 9f b7     ..            ; Reset FS connection state
    lda #osbyte_close_spool_exec                                      ; 8f8a: a9 77       .w             ; OSBYTE &77: close SPOOL/EXEC
    jsr osbyte                                                        ; 8f8c: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    jsr restore_fs_context                                            ; 8f8f: 20 73 8f     s.            ; Restore FS context to receive block
    ldy #&76 ; 'v'                                                    ; 8f92: a0 76       .v             ; Y=&76: checksum range end
    lda #0                                                            ; 8f94: a9 00       ..             ; A=0: checksum accumulator
    clc                                                               ; 8f96: 18          .              ; Clear carry for addition
; &8f97 referenced 1 time by &8f9b
.loop_c8f97
    adc l1000,y                                                       ; 8f97: 79 00 10    y..            ; Add byte from page &10 shadow
    dey                                                               ; 8f9a: 88          .              ; Decrement index
    bpl loop_c8f97                                                    ; 8f9b: 10 fa       ..             ; Loop until all bytes summed
    ldy #&77 ; 'w'                                                    ; 8f9d: a0 77       .w             ; Y=&77: checksum storage offset
    bpl c8fa4                                                         ; 8f9f: 10 03       ..             ; ALWAYS branch

; &8fa1 referenced 1 time by &8fa7
.loop_c8fa1
    lda l1000,y                                                       ; 8fa1: b9 00 10    ...            ; Load byte from page &10 shadow
; &8fa4 referenced 1 time by &8f9f
.c8fa4
    sta (l00cc),y                                                     ; 8fa4: 91 cc       ..             ; Copy to FS workspace
    dey                                                               ; 8fa6: 88          .              ; Decrement index
    bpl loop_c8fa1                                                    ; 8fa7: 10 f8       ..             ; Loop until all bytes copied
    lda l0d6c                                                         ; 8fa9: ad 6c 0d    .l.            ; Load FS flags
    and #&7f                                                          ; 8fac: 29 7f       ).             ; Clear bit 7 (FS no longer selected)
    sta l0d6c                                                         ; 8fae: 8d 6c 0d    .l.            ; Store updated flags
; &8fb1 referenced 1 time by &8f83
.return_11
    rts                                                               ; 8fb1: 60          `              ; Return

; &8fb2 referenced 5 times by &9baf, &9d42, &9de2, &9e23, &b5ef
.verify_ws_checksum
    php                                                               ; 8fb2: 08          .              ; Save processor status
    pha                                                               ; 8fb3: 48          H              ; Save A
    tya                                                               ; 8fb4: 98          .              ; Transfer Y to A
    pha                                                               ; 8fb5: 48          H              ; Save Y
    ldy #&76 ; 'v'                                                    ; 8fb6: a0 76       .v             ; Y=&76: checksum range end
    lda #0                                                            ; 8fb8: a9 00       ..             ; A=0: checksum accumulator
    clc                                                               ; 8fba: 18          .              ; Clear carry for addition
; &8fbb referenced 1 time by &8fbe
.loop_c8fbb
    adc (l00cc),y                                                     ; 8fbb: 71 cc       q.             ; Add byte from FS workspace
    dey                                                               ; 8fbd: 88          .              ; Decrement index
    bpl loop_c8fbb                                                    ; 8fbe: 10 fb       ..             ; Loop until all bytes summed
    ldy #&77 ; 'w'                                                    ; 8fc0: a0 77       .w             ; Y=&77: checksum storage offset
    cmp (l00cc),y                                                     ; 8fc2: d1 cc       ..             ; Compare with stored checksum
    bne error_net_checksum                                            ; 8fc4: d0 05       ..             ; Mismatch: raise checksum error
    pla                                                               ; 8fc6: 68          h              ; Restore Y
    tay                                                               ; 8fc7: a8          .              ; Transfer to Y
    pla                                                               ; 8fc8: 68          h              ; Restore A
    plp                                                               ; 8fc9: 28          (              ; Restore processor status
    rts                                                               ; 8fca: 60          `              ; Return (checksum valid)

; &8fcb referenced 2 times by &8b25, &8fc4
.error_net_checksum
    lda #&aa                                                          ; 8fcb: a9 aa       ..             ; Error number &AA
    jsr error_bad_inline                                              ; 8fcd: 20 a2 96     ..            ; Raise 'net checksum' error
    equs "net checksum", 0                                            ; 8fd0: 6e 65 74... net

; &8fdd referenced 2 times by &8cab, &8cd8
.print_station_id
    jsr print_inline                                                  ; 8fdd: 20 31 91     1.            ; Print 'Econet Station ' via inline
    equs "Econet Station "                                            ; 8fe0: 45 63 6f... Eco

    ldy #5                                                            ; 8fef: a0 05       ..             ; Offset 5: station ID
    lda (net_rx_ptr),y                                                ; 8ff1: b1 9c       ..             ; Load station ID from receive block
    jsr print_num_no_leading                                          ; 8ff3: 20 65 af     e.            ; Print station number as decimal
    lda #&20 ; ' '                                                    ; 8ff6: a9 20       .              ; Space character
    bit econet_control23_or_status2                                   ; 8ff8: 2c a1 fe    ,..            ; Check ADLC status register 2
    beq c900a                                                         ; 8ffb: f0 0d       ..             ; Clock present: skip warning
    jsr print_inline                                                  ; 8ffd: 20 31 91     1.            ; Print ' No Clock' via inline
    equs " No Clock"                                                  ; 9000: 20 4e 6f...  No

    nop                                                               ; 9009: ea          .              ; NOP (string terminator)
; &900a referenced 1 time by &8ffb
.c900a
    jsr osnewl                                                        ; 900a: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
.syntax_strings
    rts                                                               ; 900d: 60          `              ; Return

; &900e referenced 1 time by &8bd6
.cmd_syntax_strings
    equs "(<dir>)"                                                    ; 900e: 28 3c 64... (<d
    equb 0                                                            ; 9015: 00          .
    equs "(<stn. id.>) <user id.> "                                   ; 9016: 28 3c 73... (<s
    equb &0d                                                          ; 902e: 0d          .
    equs "((:<CR>)<password>)"                                        ; 902f: 28 28 3a... ((:
    equb 0                                                            ; 9042: 00          .
    equs "<object>"                                                   ; 9043: 3c 6f 62... <ob
    equb 0                                                            ; 904b: 00          .
    equs "<filename> (<offset> "                                      ; 904c: 3c 66 69... <fi
    equb &0d                                                          ; 9061: 0d          .
    equs "(<address>))"                                               ; 9062: 28 3c 61... (<a
    equb 0                                                            ; 906e: 00          .
    equs "<dir>"                                                      ; 906f: 3c 64 69... <di
    equb 0                                                            ; 9074: 00          .
    equs "<dir> (<number>)"                                           ; 9075: 3c 64 69... <di
    equb 0                                                            ; 9085: 00          .
    equs "(:<CR>) <password> "                                        ; 9086: 28 3a 3c... (:<
    equb &0d                                                          ; 9099: 0d          .
    equs "<new password>"                                             ; 909a: 3c 6e 65... <ne
    equb 0                                                            ; 90a8: 00          .
    equs "(<stn. id.>|<ps type>)"                                     ; 90a9: 28 3c 73... (<s
    equb 0                                                            ; 90bf: 00          .
    equs "<object> (L)(W)(R)(/(W)(R))"                                ; 90c0: 3c 6f 62... <ob
    equb 0                                                            ; 90db: 00          .
    equs "<filename> <new filename>"                                  ; 90dc: 3c 66 69... <fi
    equb 0                                                            ; 90f5: 00          .
    equs "(<stn. id.>)"                                               ; 90f6: 28 3c 73... (<s
    equb 0                                                            ; 9102: 00          .
    equs "<filename>"                                                 ; 9103: 3c 66 69... <fi
    equb 0                                                            ; 910d: 00          .
; &910e referenced 1 time by &8bd1
.cmd_syntax_table
    equb 6, &ff, 7                                                    ; 910e: 06 ff 07    ...
    equs "4=`fw"                                                      ; 9111: 34 3d 60... 4=`
    equb &9a, &b1, &cd, &e7, &f4                                      ; 9116: 9a b1 cd... ...

; &911b referenced 5 times by &9a54, &adff, &ba55, &ba7d, &bae5
.print_hex_byte
    pha                                                               ; 911b: 48          H              ; Save full byte
    lsr a                                                             ; 911c: 4a          J              ; Shift high nybble to low
    lsr a                                                             ; 911d: 4a          J              ; Continue shifting
    lsr a                                                             ; 911e: 4a          J              ; Continue shifting
    lsr a                                                             ; 911f: 4a          J              ; High nybble now in bits 0-3
    jsr print_hex_nybble                                              ; 9120: 20 24 91     $.            ; Print high nybble as hex digit
    pla                                                               ; 9123: 68          h              ; Restore full byte
; &9124 referenced 1 time by &9120
.print_hex_nybble
    and #&0f                                                          ; 9124: 29 0f       ).             ; Mask to low nybble
    cmp #&0a                                                          ; 9126: c9 0a       ..             ; Digit >= &0A?
    bcc c912c                                                         ; 9128: 90 02       ..             ; No: skip letter adjustment
    adc #6                                                            ; 912a: 69 06       i.             ; Add 7 to get 'A'-'F' (6 + carry)
; &912c referenced 1 time by &9128
.c912c
    adc #&30 ; '0'                                                    ; 912c: 69 30       i0             ; Add &30 for ASCII '0'-'9' or 'A'-'F'
    jmp osasci                                                        ; 912e: 4c e3 ff    L..            ; Write character

; ***************************************************************************************
; Print inline string, high-bit terminated
; 
; Pops the return address from the stack, prints each byte via OSASCI
; until a byte with bit 7 set is found, then jumps to that address.
; The high-bit byte serves as both the string terminator and the opcode
; of the first instruction after the string. Common terminators are
; &EA (NOP) for fall-through and &B8 (CLV) followed by BVC for an
; unconditional forward branch.
; 
; On Exit:
;     A: terminator byte (bit 7 set, also next opcode)
;     X: corrupted (by OSASCI)
;     Y: 0
; ***************************************************************************************
; &9131 referenced 35 times by &8bab, &8bed, &8c94, &8fdd, &8ffd, &9522, &adae, &adb8, &adc6, &add1, &aded, &ae02, &ae15, &ae24, &af33, &b07e, &b08a, &b0a1, &b0ab, &b0b6, &b186, &b228, &b23d, &b260, &b26d, &b27c, &b28c, &b29b, &b3a8, &b3cd, &ba71, &ba8f, &ba9c, &bad1, &baf6
.print_inline
    pla                                                               ; 9131: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_error_ptr                                                  ; 9132: 85 b8       ..
    pla                                                               ; 9134: 68          h              ; Pop return address (high)
    sta fs_crflag                                                     ; 9135: 85 b9       ..
    ldy #0                                                            ; 9137: a0 00       ..
; &9139 referenced 1 time by &9154
.loop_c9139
    inc fs_error_ptr                                                  ; 9139: e6 b8       ..             ; Advance pointer to next character
    bne c913f                                                         ; 913b: d0 02       ..
    inc fs_crflag                                                     ; 913d: e6 b9       ..
; &913f referenced 1 time by &913b
.c913f
    lda (fs_error_ptr),y                                              ; 913f: b1 b8       ..             ; Load next byte from inline string
    bmi c9157                                                         ; 9141: 30 14       0.             ; Bit 7 set? Done — this byte is the next opcode
    lda fs_error_ptr                                                  ; 9143: a5 b8       ..
    pha                                                               ; 9145: 48          H
    lda fs_crflag                                                     ; 9146: a5 b9       ..
    pha                                                               ; 9148: 48          H
    lda (fs_error_ptr),y                                              ; 9149: b1 b8       ..             ; Reload character (pointer may have been clobbered)
    jsr osasci                                                        ; 914b: 20 e3 ff     ..            ; Print character via OSASCI; Write character
    pla                                                               ; 914e: 68          h
    sta fs_crflag                                                     ; 914f: 85 b9       ..
    pla                                                               ; 9151: 68          h
    sta fs_error_ptr                                                  ; 9152: 85 b8       ..
    jmp loop_c9139                                                    ; 9154: 4c 39 91    L9.

; &9157 referenced 1 time by &9141
.c9157
    jmp (fs_error_ptr)                                                ; 9157: 6c b8 00    l..            ; Jump to address of high-bit byte (resumes code)

; &915a referenced 5 times by &8d8d, &8d99, &a095, &a0aa, &ad12
.parse_addr_arg
    lda #0                                                            ; 915a: a9 00       ..
    sta fs_load_addr_2                                                ; 915c: 85 b2       ..
    lda (fs_crc_lo),y                                                 ; 915e: b1 be       ..
    cmp #&26 ; '&'                                                    ; 9160: c9 26       .&
    bne c919a                                                         ; 9162: d0 36       .6
    iny                                                               ; 9164: c8          .
    lda (fs_crc_lo),y                                                 ; 9165: b1 be       ..
    bcs c9174                                                         ; 9167: b0 0b       ..
; &9169 referenced 1 time by &9198
.c9169
    iny                                                               ; 9169: c8          .
    lda (fs_crc_lo),y                                                 ; 916a: b1 be       ..
    cmp #&2e ; '.'                                                    ; 916c: c9 2e       ..
    beq c91e7                                                         ; 916e: f0 77       .w
    cmp #&21 ; '!'                                                    ; 9170: c9 21       .!
    bcc c91c6                                                         ; 9172: 90 52       .R
; &9174 referenced 1 time by &9167
.c9174
    cmp #&30 ; '0'                                                    ; 9174: c9 30       .0
    bcc c9184                                                         ; 9176: 90 0c       ..
    cmp #&3a ; ':'                                                    ; 9178: c9 3a       .:
    bcc c9186                                                         ; 917a: 90 0a       ..
    and #&5f ; '_'                                                    ; 917c: 29 5f       )_
    adc #&b8                                                          ; 917e: 69 b8       i.
    bcs err_bad_hex                                                   ; 9180: b0 72       .r
    cmp #&fa                                                          ; 9182: c9 fa       ..
; &9184 referenced 1 time by &9176
.c9184
    bcc err_bad_hex                                                   ; 9184: 90 6e       .n
; &9186 referenced 1 time by &917a
.c9186
    and #&0f                                                          ; 9186: 29 0f       ).
    sta fs_load_addr_3                                                ; 9188: 85 b3       ..
    lda fs_load_addr_2                                                ; 918a: a5 b2       ..
    cmp #&10                                                          ; 918c: c9 10       ..
    bcs c91fd                                                         ; 918e: b0 6d       .m
    asl a                                                             ; 9190: 0a          .
    asl a                                                             ; 9191: 0a          .
    asl a                                                             ; 9192: 0a          .
    asl a                                                             ; 9193: 0a          .
    adc fs_load_addr_3                                                ; 9194: 65 b3       e.
    sta fs_load_addr_2                                                ; 9196: 85 b2       ..
    bcc c9169                                                         ; 9198: 90 cf       ..
; &919a referenced 2 times by &9162, &91c4
.c919a
    lda (fs_crc_lo),y                                                 ; 919a: b1 be       ..
    cmp #&2e ; '.'                                                    ; 919c: c9 2e       ..
    beq c91e7                                                         ; 919e: f0 47       .G
    cmp #&21 ; '!'                                                    ; 91a0: c9 21       .!
    bcc c91c6                                                         ; 91a2: 90 22       ."
    jsr is_dec_digit_only                                             ; 91a4: 20 4c 92     L.
    bcc c9215                                                         ; 91a7: 90 6c       .l
    and #&0f                                                          ; 91a9: 29 0f       ).
    sta fs_load_addr_3                                                ; 91ab: 85 b3       ..
    asl fs_load_addr_2                                                ; 91ad: 06 b2       ..
    bcs c91fd                                                         ; 91af: b0 4c       .L
    lda fs_load_addr_2                                                ; 91b1: a5 b2       ..
    asl a                                                             ; 91b3: 0a          .
    bcs c91fd                                                         ; 91b4: b0 47       .G
    asl a                                                             ; 91b6: 0a          .
    bcs c91fd                                                         ; 91b7: b0 44       .D
    adc fs_load_addr_2                                                ; 91b9: 65 b2       e.
    bcs c91fd                                                         ; 91bb: b0 40       .@
    adc fs_load_addr_3                                                ; 91bd: 65 b3       e.
    bcs c91fd                                                         ; 91bf: b0 3c       .<
    sta fs_load_addr_2                                                ; 91c1: 85 b2       ..
    iny                                                               ; 91c3: c8          .
    bne c919a                                                         ; 91c4: d0 d4       ..
; &91c6 referenced 2 times by &9172, &91a2
.c91c6
    lda fs_work_4                                                     ; 91c6: a5 b4       ..
    bpl c91cf                                                         ; 91c8: 10 05       ..
    lda fs_load_addr_2                                                ; 91ca: a5 b2       ..
    beq c9221                                                         ; 91cc: f0 53       .S
    rts                                                               ; 91ce: 60          `

; &91cf referenced 1 time by &91c8
.c91cf
    lda fs_load_addr_2                                                ; 91cf: a5 b2       ..
    cmp #&ff                                                          ; 91d1: c9 ff       ..
    beq err_bad_station_num                                           ; 91d3: f0 2c       .,
    lda fs_load_addr_2                                                ; 91d5: a5 b2       ..
    bne c91e5                                                         ; 91d7: d0 0c       ..
    lda fs_work_4                                                     ; 91d9: a5 b4       ..
    beq err_bad_station_num                                           ; 91db: f0 24       .$
    dey                                                               ; 91dd: 88          .
    lda (fs_crc_lo),y                                                 ; 91de: b1 be       ..
    iny                                                               ; 91e0: c8          .
    eor #&2e ; '.'                                                    ; 91e1: 49 2e       I.
    bne err_bad_station_num                                           ; 91e3: d0 1c       ..
; &91e5 referenced 1 time by &91d7
.c91e5
    sec                                                               ; 91e5: 38          8
    rts                                                               ; 91e6: 60          `

; &91e7 referenced 2 times by &916e, &919e
.c91e7
    lda fs_work_4                                                     ; 91e7: a5 b4       ..
    bne c9215                                                         ; 91e9: d0 2a       .*
    inc fs_work_4                                                     ; 91eb: e6 b4       ..
    lda fs_load_addr_2                                                ; 91ed: a5 b2       ..
    cmp #&ff                                                          ; 91ef: c9 ff       ..
    beq c9230                                                         ; 91f1: f0 3d       .=
    rts                                                               ; 91f3: 60          `

; &91f4 referenced 3 times by &9180, &9184, &bbb2
.err_bad_hex
    lda #&f1                                                          ; 91f4: a9 f1       ..
    jsr error_bad_inline                                              ; 91f6: 20 a2 96     ..
    equs "hex", 0                                                     ; 91f9: 68 65 78... hex

; &91fd referenced 6 times by &918e, &91af, &91b4, &91b7, &91bb, &91bf
.c91fd
    bit fs_work_4                                                     ; 91fd: 24 b4       $.
    bmi c9221                                                         ; 91ff: 30 20       0
; &9201 referenced 4 times by &8f29, &91d3, &91db, &91e3
.err_bad_station_num
    lda #&d0                                                          ; 9201: a9 d0       ..
    jsr error_bad_inline                                              ; 9203: 20 a2 96     ..
    equs "station number", 0                                          ; 9206: 73 74 61... sta

; &9215 referenced 2 times by &91a7, &91e9
.c9215
    lda #&f0                                                          ; 9215: a9 f0       ..
    jsr error_bad_inline                                              ; 9217: 20 a2 96     ..
    equs "number", 0                                                  ; 921a: 6e 75 6d... num

; &9221 referenced 2 times by &91cc, &91ff
.c9221
    lda #&94                                                          ; 9221: a9 94       ..
    jsr error_bad_inline                                              ; 9223: 20 a2 96     ..
    equs "parameter", 0                                               ; 9226: 70 61 72... par

; &9230 referenced 1 time by &91f1
.c9230
    lda #&d1                                                          ; 9230: a9 d1       ..
    jsr error_bad_inline                                              ; 9232: 20 a2 96     ..
    equs "network number", 0                                          ; 9235: 6e 65 74... net

; &9244 referenced 3 times by &8d88, &afe5, &b1b8
.is_decimal_digit
    cmp #&26 ; '&'                                                    ; 9244: c9 26       .&
    beq return_12                                                     ; 9246: f0 0a       ..
    cmp #&2e ; '.'                                                    ; 9248: c9 2e       ..
    beq return_12                                                     ; 924a: f0 06       ..
; &924c referenced 1 time by &91a4
.is_dec_digit_only
    cmp #&3a ; ':'                                                    ; 924c: c9 3a       .:
    bcs c9253                                                         ; 924e: b0 03       ..
    cmp #&30 ; '0'                                                    ; 9250: c9 30       .0
; &9252 referenced 2 times by &9246, &924a
.return_12
    rts                                                               ; 9252: 60          `

; &9253 referenced 1 time by &924e
.c9253
    clc                                                               ; 9253: 18          .
    rts                                                               ; 9254: 60          `

; &9255 referenced 2 times by &9b0e, &9b3a
.get_access_bits
    ldy #&0e                                                          ; 9255: a0 0e       ..
    lda (fs_options),y                                                ; 9257: b1 bb       ..
    and #&3f ; '?'                                                    ; 9259: 29 3f       )?
    ldx #4                                                            ; 925b: a2 04       ..
    bne c9263                                                         ; 925d: d0 04       ..             ; ALWAYS branch

; &925f referenced 2 times by &9a16, &9b57
.get_prot_bits
    and #&1f                                                          ; 925f: 29 1f       ).
    ldx #&ff                                                          ; 9261: a2 ff       ..
; &9263 referenced 1 time by &925d
.c9263
    sta fs_error_ptr                                                  ; 9263: 85 b8       ..
    lda #0                                                            ; 9265: a9 00       ..
; &9267 referenced 1 time by &926f
.loop_c9267
    inx                                                               ; 9267: e8          .
    lsr fs_error_ptr                                                  ; 9268: 46 b8       F.
    bcc c926f                                                         ; 926a: 90 03       ..
    ora prot_bit_encode_table,x                                       ; 926c: 1d 72 92    .r.
; &926f referenced 1 time by &926a
.c926f
    bne loop_c9267                                                    ; 926f: d0 f6       ..
    rts                                                               ; 9271: 60          `

; &9272 referenced 1 time by &926c
.prot_bit_encode_table
    equb &50, &20, 5, 2, &88, 4, 8, &80, &10, 1, 2                    ; 9272: 50 20 05... P .

; &927d referenced 1 time by &a0fc
.set_text_and_xfer_ptr
    stx os_text_ptr                                                   ; 927d: 86 f2       ..
    sty os_text_ptr_hi                                                ; 927f: 84 f3       ..
; &9281 referenced 5 times by &8e1d, &9921, &9d45, &9e26, &ad6e
.set_xfer_params
    sta fs_last_byte_flag                                             ; 9281: 85 bd       ..
    stx fs_crc_lo                                                     ; 9283: 86 be       ..
    sty fs_crc_hi                                                     ; 9285: 84 bf       ..
; &9287 referenced 2 times by &9bb4, &b979
.set_options_ptr
    stx fs_options                                                    ; 9287: 86 bb       ..
    sty fs_block_offset                                               ; 9289: 84 bc       ..
; &928b referenced 1 time by &9870
.clear_escapable
    php                                                               ; 928b: 08          .
    lsr escapable                                                     ; 928c: 46 97       F.
    plp                                                               ; 928e: 28          (
    rts                                                               ; 928f: 60          `

; &9290 referenced 2 times by &9984, &9a89
.cmp_5byte_handle
    ldx #4                                                            ; 9290: a2 04       ..
; &9292 referenced 1 time by &9299
.loop_c9292
    lda l00af,x                                                       ; 9292: b5 af       ..
    eor fs_load_addr_3,x                                              ; 9294: 55 b3       U.
    bne return_13                                                     ; 9296: d0 03       ..
    dex                                                               ; 9298: ca          .
    bne loop_c9292                                                    ; 9299: d0 f7       ..
; &929b referenced 1 time by &9296
.return_13
    rts                                                               ; 929b: 60          `

    ldx #&20 ; ' '                                                    ; 929c: a2 20       .
    ldy #&2f ; '/'                                                    ; 929e: a0 2f       ./
    rts                                                               ; 92a0: 60          `

; &92a1 referenced 2 times by &9c3a, &9e83
.set_conn_active
    php                                                               ; 92a1: 08          .
    pha                                                               ; 92a2: 48          H
    txa                                                               ; 92a3: 8a          .
    pha                                                               ; 92a4: 48          H
    tsx                                                               ; 92a5: ba          .
    lda l0102,x                                                       ; 92a6: bd 02 01    ...
    jsr attr_to_chan_index                                            ; 92a9: 20 5b b4     [.
    bmi c92cd                                                         ; 92ac: 30 1f       0.
    lda #&40 ; '@'                                                    ; 92ae: a9 40       .@
    ora l1060,x                                                       ; 92b0: 1d 60 10    .`.
    sta l1060,x                                                       ; 92b3: 9d 60 10    .`.
    bne c92cd                                                         ; 92b6: d0 15       ..
; &92b8 referenced 2 times by &9c9b, &9e7e
.clear_conn_active
    php                                                               ; 92b8: 08          .
    pha                                                               ; 92b9: 48          H
    txa                                                               ; 92ba: 8a          .
    pha                                                               ; 92bb: 48          H
    tsx                                                               ; 92bc: ba          .
    lda l0102,x                                                       ; 92bd: bd 02 01    ...
    jsr attr_to_chan_index                                            ; 92c0: 20 5b b4     [.
    bmi c92cd                                                         ; 92c3: 30 08       0.
    lda #&bf                                                          ; 92c5: a9 bf       ..
    and l1060,x                                                       ; 92c7: 3d 60 10    =`.
    sta l1060,x                                                       ; 92ca: 9d 60 10    .`.
; &92cd referenced 3 times by &92ac, &92b6, &92c3
.c92cd
    pla                                                               ; 92cd: 68          h
    tax                                                               ; 92ce: aa          .
    pla                                                               ; 92cf: 68          h
    plp                                                               ; 92d0: 28          (
    rts                                                               ; 92d1: 60          `

; ***************************************************************************************
; Shared handler for *Access, *Delete, *Info, *Lib.
; Command code distinguishes operation.
; ***************************************************************************************
.cmd_fs_operation
    jsr copy_fs_cmd_name                                              ; 92d2: 20 13 93     ..            ; Copy command name to TX buffer
    txa                                                               ; 92d5: 8a          .              ; Save buffer position
    pha                                                               ; 92d6: 48          H              ; Push it
    jsr parse_quoted_arg                                              ; 92d7: 20 35 93     5.            ; Parse filename (handles quoting)
    jsr parse_access_prefix                                           ; 92da: 20 85 ae     ..            ; Parse owner/public access prefix
    pla                                                               ; 92dd: 68          h              ; Restore buffer position
    tax                                                               ; 92de: aa          .              ; Transfer to X
    jsr check_not_ampersand                                           ; 92df: 20 f5 92     ..            ; Reject '&' character in filename
    cmp #&0d                                                          ; 92e2: c9 0d       ..             ; End of line?
    bne read_filename_char                                            ; 92e4: d0 17       ..             ; No: copy filename chars to buffer
; &92e6 referenced 4 times by &92fa, &93f5, &aecd, &af02
.error_bad_filename
    lda #&cc                                                          ; 92e6: a9 cc       ..             ; Error number &CC
    jsr error_bad_inline                                              ; 92e8: 20 a2 96     ..            ; Raise 'Bad file name' error
    equs "file name", 0                                               ; 92eb: 66 69 6c... fil

; &92f5 referenced 2 times by &92df, &92fd
.check_not_ampersand
    lda l0e30                                                         ; 92f5: ad 30 0e    .0.            ; Load first parsed character
    cmp #&26 ; '&'                                                    ; 92f8: c9 26       .&             ; Is it '&'?
    beq error_bad_filename                                            ; 92fa: f0 ea       ..             ; Yes: invalid filename
    rts                                                               ; 92fc: 60          `              ; Return

; &92fd referenced 3 times by &92e4, &930b, &93c6
.read_filename_char
    jsr check_not_ampersand                                           ; 92fd: 20 f5 92     ..            ; Reject '&' in current char
    sta l0f05,x                                                       ; 9300: 9d 05 0f    ...            ; Store character in TX buffer
    inx                                                               ; 9303: e8          .              ; Advance buffer pointer
    cmp #&0d                                                          ; 9304: c9 0d       ..             ; End of line?
    beq send_fs_request                                               ; 9306: f0 06       ..             ; Yes: send request to file server
    jsr strip_token_prefix                                            ; 9308: 20 a5 ae     ..            ; Strip BASIC token prefix byte
    jmp read_filename_char                                            ; 930b: 4c fd 92    L..            ; Continue reading filename chars

; &930e referenced 2 times by &9306, &93ee
.send_fs_request
    ldy #0                                                            ; 930e: a0 00       ..             ; Y=0: no extra dispatch offset
    jmp send_cmd_and_dispatch                                         ; 9310: 4c 0e 8e    L..            ; Send command and dispatch reply

; &9313 referenced 2 times by &92d2, &9377
.copy_fs_cmd_name
    tya                                                               ; 9313: 98          .              ; Save command line offset
    pha                                                               ; 9314: 48          H              ; Push it
; &9315 referenced 1 time by &9319
.loop_c9315
    dex                                                               ; 9315: ca          .              ; Scan backwards in command table
    lda cmd_table_fs,x                                                ; 9316: bd d8 a3    ...            ; Load table byte
    bpl loop_c9315                                                    ; 9319: 10 fa       ..             ; Bit 7 clear: keep scanning
    inx                                                               ; 931b: e8          .              ; Point past flag byte to name start
    ldy #0                                                            ; 931c: a0 00       ..             ; Y=0: TX buffer offset
; &931e referenced 1 time by &9328
.loop_c931e
    lda cmd_table_fs,x                                                ; 931e: bd d8 a3    ...            ; Load command name character
    bmi c932a                                                         ; 9321: 30 07       0.             ; Bit 7 set: end of name
    sta l0f05,y                                                       ; 9323: 99 05 0f    ...            ; Store character in TX buffer
    inx                                                               ; 9326: e8          .              ; Advance table pointer
    iny                                                               ; 9327: c8          .              ; Advance buffer pointer
    bne loop_c931e                                                    ; 9328: d0 f4       ..             ; Continue copying name
; &932a referenced 1 time by &9321
.c932a
    lda #&20 ; ' '                                                    ; 932a: a9 20       .              ; Space separator
    sta l0f05,y                                                       ; 932c: 99 05 0f    ...            ; Append space after command name
    iny                                                               ; 932f: c8          .              ; Advance buffer pointer
    tya                                                               ; 9330: 98          .              ; Transfer length to A
    tax                                                               ; 9331: aa          .              ; And to X (buffer position)
    pla                                                               ; 9332: 68          h              ; Restore command line offset
    tay                                                               ; 9333: a8          .              ; Transfer to Y
; &9334 referenced 1 time by &9369
.return_14
    rts                                                               ; 9334: 60          `              ; Return

; &9335 referenced 2 times by &92d7, &937f
.parse_quoted_arg
    lda #0                                                            ; 9335: a9 00       ..             ; A=0: no quote mode
    tax                                                               ; 9337: aa          .              ; X=&00
    sta l10d8                                                         ; 9338: 8d d8 10    ...            ; Clear quote tracking flag
; &933b referenced 1 time by &9342
.loop_c933b
    lda (fs_crc_lo),y                                                 ; 933b: b1 be       ..             ; Load char from command line
    cmp #&20 ; ' '                                                    ; 933d: c9 20       .              ; Space?
    bne c9344                                                         ; 933f: d0 03       ..             ; No: check for opening quote
    iny                                                               ; 9341: c8          .              ; Skip leading space
    bne loop_c933b                                                    ; 9342: d0 f7       ..             ; Continue skipping spaces
; &9344 referenced 1 time by &933f
.c9344
    cmp #&22 ; '"'                                                    ; 9344: c9 22       ."             ; Double-quote character?
    bne c934f                                                         ; 9346: d0 07       ..             ; No: start reading filename
    iny                                                               ; 9348: c8          .              ; Skip opening quote
    eor l10d8                                                         ; 9349: 4d d8 10    M..            ; Toggle quote mode flag
    sta l10d8                                                         ; 934c: 8d d8 10    ...            ; Store updated quote mode
; &934f referenced 2 times by &9346, &9364
.c934f
    lda (fs_crc_lo),y                                                 ; 934f: b1 be       ..             ; Load char from command line
    cmp #&22 ; '"'                                                    ; 9351: c9 22       ."             ; Double-quote?
    bne c935d                                                         ; 9353: d0 08       ..             ; No: store character as-is
    eor l10d8                                                         ; 9355: 4d d8 10    M..            ; Toggle quote mode
    sta l10d8                                                         ; 9358: 8d d8 10    ...            ; Store updated quote mode
    lda #&20 ; ' '                                                    ; 935b: a9 20       .              ; Replace closing quote with space
; &935d referenced 1 time by &9353
.c935d
    sta l0e30,x                                                       ; 935d: 9d 30 0e    .0.            ; Store character in parse buffer
    iny                                                               ; 9360: c8          .              ; Advance command line pointer
    inx                                                               ; 9361: e8          .              ; Advance buffer pointer
    cmp #&0d                                                          ; 9362: c9 0d       ..             ; End of line?
    bne c934f                                                         ; 9364: d0 e9       ..             ; No: continue parsing
    lda l10d8                                                         ; 9366: ad d8 10    ...            ; Check quote balance flag
    beq return_14                                                     ; 9369: f0 c9       ..             ; Balanced: return OK
    lda brk_ptr                                                       ; 936b: a5 fd       ..             ; Unbalanced: use BRK ptr for error
    jsr error_bad_inline                                              ; 936d: 20 a2 96     ..            ; Raise 'Bad string' error
    equs "string", 0                                                  ; 9370: 73 74 72... str

; ***************************************************************************************
; *Rename command.
; Renames a file on the file server.
; ***************************************************************************************
.cmd_rename
    jsr copy_fs_cmd_name                                              ; 9377: 20 13 93     ..            ; Copy 'Rename ' to TX buffer
    txa                                                               ; 937a: 8a          .              ; Save buffer position
    pha                                                               ; 937b: 48          H              ; Push it
    jsr mask_owner_access                                             ; 937c: 20 12 af     ..            ; Set owner-only access mask
    jsr parse_quoted_arg                                              ; 937f: 20 35 93     5.            ; Parse first filename (quoted)
    jsr parse_access_prefix                                           ; 9382: 20 85 ae     ..            ; Parse access prefix
    pla                                                               ; 9385: 68          h              ; Restore buffer position
    tax                                                               ; 9386: aa          .              ; Transfer to X
; &9387 referenced 1 time by &93a5
.loop_c9387
    lda l0e30                                                         ; 9387: ad 30 0e    .0.            ; Load next parsed character
    cmp #&0d                                                          ; 938a: c9 0d       ..             ; End of line?
    bne c939a                                                         ; 938c: d0 0c       ..             ; No: store character
; &938e referenced 1 time by &93c4
.c938e
    lda #&b0                                                          ; 938e: a9 b0       ..             ; Error number &B0
    jsr error_bad_inline                                              ; 9390: 20 a2 96     ..            ; Raise 'Bad rename' error
    equs "rename", 0                                                  ; 9393: 72 65 6e... ren

; &939a referenced 1 time by &938c
.c939a
    sta l0f05,x                                                       ; 939a: 9d 05 0f    ...            ; Store character in TX buffer
    inx                                                               ; 939d: e8          .              ; Advance buffer pointer
    cmp #&20 ; ' '                                                    ; 939e: c9 20       .              ; Space (name separator)?
    beq c93a8                                                         ; 93a0: f0 06       ..             ; Yes: first name complete
    jsr strip_token_prefix                                            ; 93a2: 20 a5 ae     ..            ; Strip BASIC token prefix byte
    jmp loop_c9387                                                    ; 93a5: 4c 87 93    L..            ; Continue copying first filename

; &93a8 referenced 2 times by &93a0, &93b0
.c93a8
    jsr strip_token_prefix                                            ; 93a8: 20 a5 ae     ..            ; Strip token from next char
    lda l0e30                                                         ; 93ab: ad 30 0e    .0.            ; Load next parsed character
    cmp #&20 ; ' '                                                    ; 93ae: c9 20       .              ; Still a space?
    beq c93a8                                                         ; 93b0: f0 f6       ..             ; Yes: skip multiple spaces
    lda l1071                                                         ; 93b2: ad 71 10    .q.            ; Save current FS options
    pha                                                               ; 93b5: 48          H              ; Push them
    jsr mask_owner_access                                             ; 93b6: 20 12 af     ..            ; Reset access mask for second name
    txa                                                               ; 93b9: 8a          .              ; Save buffer position
    pha                                                               ; 93ba: 48          H              ; Push it
    jsr parse_access_prefix                                           ; 93bb: 20 85 ae     ..            ; Parse access prefix for second name
    pla                                                               ; 93be: 68          h              ; Restore buffer position
    tax                                                               ; 93bf: aa          .              ; Transfer to X
    pla                                                               ; 93c0: 68          h              ; Restore original FS options
    cmp l1071                                                         ; 93c1: cd 71 10    .q.            ; Options changed (cross-FS)?
    bne c938e                                                         ; 93c4: d0 c8       ..             ; Yes: error (can't rename across FS)
    jmp read_filename_char                                            ; 93c6: 4c fd 92    L..            ; Copy second filename and send

; ***************************************************************************************
; *Dir command.
; Sets the current directory on the
; file server.
; ***************************************************************************************
.cmd_dir
    lda (fs_crc_lo),y                                                 ; 93c9: b1 be       ..             ; Get first char of argument
    cmp #&26 ; '&'                                                    ; 93cb: c9 26       .&             ; Is it '&' (FS selector prefix)?
    bne c944e                                                         ; 93cd: d0 7f       ..             ; No: simple dir change
    iny                                                               ; 93cf: c8          .              ; Skip '&'
    lda (fs_crc_lo),y                                                 ; 93d0: b1 be       ..             ; Get char after '&'
    cmp #&0d                                                          ; 93d2: c9 0d       ..             ; End of line?
    beq c93da                                                         ; 93d4: f0 04       ..             ; Yes: '&' alone (root directory)
    cmp #&20 ; ' '                                                    ; 93d6: c9 20       .              ; Space?
    bne c93f1                                                         ; 93d8: d0 17       ..             ; No: check for '.' separator
; &93da referenced 1 time by &93d4
.c93da
    ldy #&ff                                                          ; 93da: a0 ff       ..             ; Y=&FF: pre-increment for loop
; &93dc referenced 1 time by &93e4
.loop_c93dc
    iny                                                               ; 93dc: c8          .              ; Advance index
    lda (fs_crc_lo),y                                                 ; 93dd: b1 be       ..             ; Load char from command line
    sta l0f05,y                                                       ; 93df: 99 05 0f    ...            ; Copy to TX buffer
    cmp #&26 ; '&'                                                    ; 93e2: c9 26       .&             ; Is it '&' (end of FS path)?
    bne loop_c93dc                                                    ; 93e4: d0 f6       ..             ; No: keep copying
    lda #&0d                                                          ; 93e6: a9 0d       ..             ; Replace '&' with CR terminator
    sta l0f05,y                                                       ; 93e8: 99 05 0f    ...            ; Store CR in buffer
    iny                                                               ; 93eb: c8          .              ; Point past CR
    tya                                                               ; 93ec: 98          .              ; Transfer length to A
    tax                                                               ; 93ed: aa          .              ; And to X (byte count)
    jmp send_fs_request                                               ; 93ee: 4c 0e 93    L..            ; Send directory request to server

; &93f1 referenced 1 time by &93d8
.c93f1
    cmp #&2e ; '.'                                                    ; 93f1: c9 2e       ..             ; Is char after '&' a dot?
    beq c93f8                                                         ; 93f3: f0 03       ..             ; Yes: &FS.dir format
    jmp error_bad_filename                                            ; 93f5: 4c e6 92    L..            ; No: invalid syntax

; &93f8 referenced 1 time by &93f3
.c93f8
    iny                                                               ; 93f8: c8          .              ; Skip '.'
    sty fs_load_addr                                                  ; 93f9: 84 b0       ..             ; Save dir path start position
    lda #4                                                            ; 93fb: a9 04       ..             ; FS command 4: examine directory
    sta l0f05                                                         ; 93fd: 8d 05 0f    ...            ; Store in TX buffer
    lda l1071                                                         ; 9400: ad 71 10    .q.            ; Load FS flags
    ora #&40 ; '@'                                                    ; 9403: 09 40       .@             ; Set bit 6 (FS selection active)
    sta l1071                                                         ; 9405: 8d 71 10    .q.            ; Store updated flags
    ldx #1                                                            ; 9408: a2 01       ..             ; X=1: buffer offset
    jsr copy_arg_validated                                            ; 940a: 20 f4 ae     ..            ; Copy FS number to buffer
    ldy #&12                                                          ; 940d: a0 12       ..             ; Y=&12: select FS command code
    jsr save_net_tx_cb                                                ; 940f: 20 99 94     ..            ; Send FS selection command
    lda l0f05                                                         ; 9412: ad 05 0f    ...            ; Load reply status
    cmp #2                                                            ; 9415: c9 02       ..             ; Status 2 (found)?
    beq c9428                                                         ; 9417: f0 0f       ..             ; Yes: proceed to dir change
    lda #&d6                                                          ; 9419: a9 d6       ..             ; Error number &D6
    jsr error_inline_log                                              ; 941b: 20 bb 96     ..            ; Raise 'Not found' error
    equs "Not found", 0                                               ; 941e: 4e 6f 74... Not

; &9428 referenced 1 time by &9417
.c9428
    lda l0e03                                                         ; 9428: ad 03 0e    ...            ; Load current FS station byte
    sta l0f05                                                         ; 942b: 8d 05 0f    ...            ; Store in TX buffer
    ldx #1                                                            ; 942e: a2 01       ..             ; X=1: buffer offset
    ldy #7                                                            ; 9430: a0 07       ..             ; Y=7: change directory command code
    jsr save_net_tx_cb                                                ; 9432: 20 99 94     ..            ; Send directory change request
    ldx #1                                                            ; 9435: a2 01       ..             ; X=1
    stx l0f05                                                         ; 9437: 8e 05 0f    ...            ; Store start marker in buffer
    stx l0f06                                                         ; 943a: 8e 06 0f    ...            ; Store start marker in buffer+1
    inx                                                               ; 943d: e8          .              ; X=&02
    ldy fs_load_addr                                                  ; 943e: a4 b0       ..             ; Restore dir path start position
    jsr copy_arg_validated                                            ; 9440: 20 f4 ae     ..            ; Copy directory path to buffer
    ldy #6                                                            ; 9443: a0 06       ..             ; Y=6: set directory command code
    jsr save_net_tx_cb                                                ; 9445: 20 99 94     ..            ; Send set directory command
    ldy l0f05                                                         ; 9448: ac 05 0f    ...            ; Load reply handle
    jmp find_fs_and_exit                                              ; 944b: 4c dc a2    L..            ; Select FS and return

; &944e referenced 1 time by &93cd
.c944e
    jmp pass_send_cmd                                                 ; 944e: 4c 0a 8e    L..            ; Simple: pass command to FS

; &9451 referenced 1 time by &94dd
.init_txcb_bye
    lda #&90                                                          ; 9451: a9 90       ..             ; A=&90: bye command port
; &9453 referenced 1 time by &9ace
.init_txcb_port
    jsr init_txcb                                                     ; 9453: 20 5f 94     _.            ; Initialise TXCB from template
    sta txcb_port                                                     ; 9456: 85 c1       ..             ; Set transmit port
    lda #3                                                            ; 9458: a9 03       ..             ; A=3: data start offset
    sta txcb_start                                                    ; 945a: 85 c4       ..             ; Set TXCB start offset
    dec txcb_ctrl                                                     ; 945c: c6 c0       ..             ; Decrement control byte
    rts                                                               ; 945e: 60          `              ; Return

; &945f referenced 5 times by &8df1, &9453, &94cc, &a8de, &b92f
.init_txcb
    pha                                                               ; 945f: 48          H              ; Save A
    ldy #&0b                                                          ; 9460: a0 0b       ..             ; Y=&0B: template size - 1
; &9462 referenced 1 time by &9473
.loop_c9462
    lda txcb_init_template,y                                          ; 9462: b9 77 94    .w.            ; Load byte from TXCB template
    sta txcb_ctrl,y                                                   ; 9465: 99 c0 00    ...            ; Store to TXCB workspace
    cpy #2                                                            ; 9468: c0 02       ..             ; Index >= 2?
    bpl c9472                                                         ; 946a: 10 06       ..             ; Yes: skip dest station copy
    lda l0e00,y                                                       ; 946c: b9 00 0e    ...            ; Load dest station byte
    sta txcb_dest,y                                                   ; 946f: 99 c2 00    ...            ; Store to TXCB destination
; &9472 referenced 1 time by &946a
.c9472
    dey                                                               ; 9472: 88          .              ; Decrement index
    bpl loop_c9462                                                    ; 9473: 10 ed       ..             ; More bytes: continue
    pla                                                               ; 9475: 68          h              ; Restore A
    rts                                                               ; 9476: 60          `              ; Return

; &9477 referenced 1 time by &9462
.txcb_init_template
    equb &80, &99, 0, 0, 0, &0f                                       ; 9477: 80 99 00... ...
; &947d referenced 22 times by &8c68, &9638, &9768, &9b2f, &9d02, &a086, &a185, &a2fe, &a329, &a360, &aa6e, &af5f, &af65, &b005, &b181, &b1e1, &b222, &b2b2, &b54e, &b58c, &b88b, &b988
.bit_test_ff_pad
    equb &ff, &ff, &ff, &0f, &ff, &ff                                 ; 947d: ff ff ff... ...            ; &FF padding (unused ROM space)

; &9483 referenced 1 time by &9f02
.send_request_nowrite
    pha                                                               ; 9483: 48          H              ; Save A
    sec                                                               ; 9484: 38          8              ; Set carry (read-only mode)
    bcs txcb_copy_carry_set                                           ; 9485: b0 1a       ..             ; ALWAYS branch

; &9487 referenced 2 times by &9944, &99f8
.send_request_write
    clv                                                               ; 9487: b8          .              ; Clear V
    bvc txcb_copy_carry_clr                                           ; 9488: 50 16       P.             ; ALWAYS branch

; ***************************************************************************************
; *Bye command.
; Logs off from the file server. Closes
; open files, clears FS context, and
; resets workspace state.
; ***************************************************************************************
.cmd_bye
    ldy #0                                                            ; 948a: a0 00       ..
    jsr process_all_fcbs                                              ; 948c: 20 9f b7     ..
    lda #osbyte_close_spool_exec                                      ; 948f: a9 77       .w
    jsr osbyte                                                        ; 9491: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    jsr close_all_net_chans                                           ; 9494: 20 4a b5     J.
    ldy #&17                                                          ; 9497: a0 17       ..
; &9499 referenced 26 times by &8e0e, &940f, &9432, &9445, &9b4b, &9c34, &9c44, &9c92, &9d2b, &9da4, &9dd8, &9e70, &9e93, &9f57, &a012, &a1be, &a1e6, &a52a, &ad2f, &ada6, &ade4, &ae53, &b365, &b406, &b6c9, &b8c8
.save_net_tx_cb
    clv                                                               ; 9499: b8          .
; &949a referenced 3 times by &9b32, &9d08, &af62
.save_net_tx_cb_vset
    lda l0e02                                                         ; 949a: ad 02 0e    ...
    sta l0f02                                                         ; 949d: 8d 02 0f    ...
; &94a0 referenced 1 time by &9488
.txcb_copy_carry_clr
    clc                                                               ; 94a0: 18          .
; &94a1 referenced 1 time by &9485
.txcb_copy_carry_set
    php                                                               ; 94a1: 08          .
    sty l0f01                                                         ; 94a2: 8c 01 0f    ...
    ldy #1                                                            ; 94a5: a0 01       ..
; &94a7 referenced 1 time by &94ae
.loop_c94a7
    lda l0e03,y                                                       ; 94a7: b9 03 0e    ...
    sta l0f03,y                                                       ; 94aa: 99 03 0f    ...
    dey                                                               ; 94ad: 88          .
    bpl loop_c94a7                                                    ; 94ae: 10 f7       ..
    bit l1071                                                         ; 94b0: 2c 71 10    ,q.
    bvs c94bf                                                         ; 94b3: 70 0a       p.
    bpl c94c5                                                         ; 94b5: 10 0e       ..
    lda l0e04                                                         ; 94b7: ad 04 0e    ...
    sta l0f03                                                         ; 94ba: 8d 03 0f    ...
    bvc c94c5                                                         ; 94bd: 50 06       P.             ; ALWAYS branch

; &94bf referenced 1 time by &94b3
.c94bf
    lda l0e02                                                         ; 94bf: ad 02 0e    ...
    sta l0f03                                                         ; 94c2: 8d 03 0f    ...
; &94c5 referenced 2 times by &94b5, &94bd
.c94c5
    plp                                                               ; 94c5: 28          (
; &94c6 referenced 1 time by &9fb0
.prep_send_tx_cb
    php                                                               ; 94c6: 08          .
    lda #&90                                                          ; 94c7: a9 90       ..
    sta l0f00                                                         ; 94c9: 8d 00 0f    ...
    jsr init_txcb                                                     ; 94cc: 20 5f 94     _.
    txa                                                               ; 94cf: 8a          .
    adc #5                                                            ; 94d0: 69 05       i.
    sta txcb_end                                                      ; 94d2: 85 c8       ..
    plp                                                               ; 94d4: 28          (
    bcs c94f1                                                         ; 94d5: b0 1a       ..
    php                                                               ; 94d7: 08          .
    jsr init_tx_ptr_and_send                                          ; 94d8: 20 22 98     ".
    plp                                                               ; 94db: 28          (
; &94dc referenced 2 times by &9a0b, &9f43
.recv_and_process_reply
    php                                                               ; 94dc: 08          .
    jsr init_txcb_bye                                                 ; 94dd: 20 51 94     Q.
    jsr wait_net_tx_ack                                               ; 94e0: 20 c7 95     ..
    plp                                                               ; 94e3: 28          (
; &94e4 referenced 1 time by &94f8
.loop_c94e4
    iny                                                               ; 94e4: c8          .
    lda (txcb_start),y                                                ; 94e5: b1 c4       ..
    tax                                                               ; 94e7: aa          .
    beq return_15                                                     ; 94e8: f0 06       ..
    bvc c94ee                                                         ; 94ea: 50 02       P.
    adc #&2a ; '*'                                                    ; 94ec: 69 2a       i*
; &94ee referenced 1 time by &94ea
.c94ee
    bne c94fa                                                         ; 94ee: d0 0a       ..
; &94f0 referenced 2 times by &94e8, &955e
.return_15
    rts                                                               ; 94f0: 60          `

; &94f1 referenced 1 time by &94d5
.c94f1
    pla                                                               ; 94f1: 68          h
    ldx #&c0                                                          ; 94f2: a2 c0       ..
    iny                                                               ; 94f4: c8          .
    jsr send_disconnect_reply                                         ; 94f5: 20 12 ac     ..
    bcc loop_c94e4                                                    ; 94f8: 90 ea       ..
; &94fa referenced 1 time by &94ee
.c94fa
    stx l0e09                                                         ; 94fa: 8e 09 0e    ...
    lda l0e07                                                         ; 94fd: ad 07 0e    ...
    bne c9506                                                         ; 9500: d0 04       ..
    cpx #&bf                                                          ; 9502: e0 bf       ..
    bne c953b                                                         ; 9504: d0 35       .5
; &9506 referenced 1 time by &9500
.c9506
    lda #&40 ; '@'                                                    ; 9506: a9 40       .@
    pha                                                               ; 9508: 48          H
    ldx #&0f                                                          ; 9509: a2 0f       ..
; &950b referenced 1 time by &9519
.loop_c950b
    pla                                                               ; 950b: 68          h
    ora l10b8,x                                                       ; 950c: 1d b8 10    ...
    pha                                                               ; 950f: 48          H
    lda l10b8,x                                                       ; 9510: bd b8 10    ...
    and #&c0                                                          ; 9513: 29 c0       ).
    sta l10b8,x                                                       ; 9515: 9d b8 10    ...
    dex                                                               ; 9518: ca          .
    bpl loop_c950b                                                    ; 9519: 10 f0       ..
    jsr close_all_net_chans                                           ; 951b: 20 4a b5     J.
    pla                                                               ; 951e: 68          h
    ror a                                                             ; 951f: 6a          j
    bcc c952f                                                         ; 9520: 90 0d       ..
    jsr print_inline                                                  ; 9522: 20 31 91     1.
    equs "Data Lost", &0d                                             ; 9525: 44 61 74... Dat

; &952f referenced 1 time by &9520
.c952f
    ldx l0e09                                                         ; 952f: ae 09 0e    ...
    lda l0e07                                                         ; 9532: ad 07 0e    ...
    beq c953b                                                         ; 9535: f0 04       ..
    pla                                                               ; 9537: 68          h
    pla                                                               ; 9538: 68          h
    pla                                                               ; 9539: 68          h
    rts                                                               ; 953a: 60          `

; &953b referenced 2 times by &9504, &9535
.c953b
    ldy #1                                                            ; 953b: a0 01       ..
    cpx #&a8                                                          ; 953d: e0 a8       ..
    bcs c9545                                                         ; 953f: b0 04       ..
    lda #&a8                                                          ; 9541: a9 a8       ..
    sta (txcb_start),y                                                ; 9543: 91 c4       ..
; &9545 referenced 1 time by &953f
.c9545
    ldy #&ff                                                          ; 9545: a0 ff       ..
; &9547 referenced 1 time by &954f
.loop_c9547
    iny                                                               ; 9547: c8          .
    lda (txcb_start),y                                                ; 9548: b1 c4       ..
    sta error_block,y                                                 ; 954a: 99 00 01    ...
    eor #&0d                                                          ; 954d: 49 0d       I.
    bne loop_c9547                                                    ; 954f: d0 f6       ..
    sta error_block,y                                                 ; 9551: 99 00 01    ...
    dey                                                               ; 9554: 88          .
    tya                                                               ; 9555: 98          .
    tax                                                               ; 9556: aa          .
    jmp check_net_error_code                                          ; 9557: 4c da 96    L..

; &955a referenced 2 times by &8dcb, &9846
.check_escape
    lda escape_flag                                                   ; 955a: a5 ff       ..
    and escapable                                                     ; 955c: 25 97       %.
    bpl return_15                                                     ; 955e: 10 90       ..
; &9560 referenced 1 time by &b42b
.raise_escape_error
    lda #osbyte_acknowledge_escape                                    ; 9560: a9 7e       .~
    jsr osbyte                                                        ; 9562: 20 f4 ff     ..            ; Clear escape condition and perform escape effects
    lda #6                                                            ; 9565: a9 06       ..
    jmp classify_reply_error                                          ; 9567: 4c 38 96    L8.

    ldy #4                                                            ; 956a: a0 04       ..
    lda (net_rx_ptr),y                                                ; 956c: b1 9c       ..
    beq c9573                                                         ; 956e: f0 03       ..
; &9570 referenced 1 time by &95b6
.c9570
    jmp commit_state_byte                                             ; 9570: 4c cb ac    L..

; &9573 referenced 2 times by &956e, &95ac
.c9573
    ora #9                                                            ; 9573: 09 09       ..
    sta (net_rx_ptr),y                                                ; 9575: 91 9c       ..
    ldx #&80                                                          ; 9577: a2 80       ..
    ldy #&80                                                          ; 9579: a0 80       ..
    lda (net_rx_ptr),y                                                ; 957b: b1 9c       ..
    pha                                                               ; 957d: 48          H
    iny                                                               ; 957e: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 957f: b1 9c       ..
    ldy #&0f                                                          ; 9581: a0 0f       ..
    sta (nfs_workspace),y                                             ; 9583: 91 9e       ..
    dey                                                               ; 9585: 88          .              ; Y=&0e
    pla                                                               ; 9586: 68          h
    sta (nfs_workspace),y                                             ; 9587: 91 9e       ..
    jsr scan_remote_keys                                              ; 9589: 20 e2 8a     ..
    jsr init_ws_copy_narrow                                           ; 958c: 20 73 aa     s.
    ldx #1                                                            ; 958f: a2 01       ..
    ldy #0                                                            ; 9591: a0 00       ..
    lda #osbyte_read_write_econet_keyboard_disable                    ; 9593: a9 c9       ..
    jsr osbyte                                                        ; 9595: 20 f4 ff     ..            ; Disable keyboard (for Econet)
    jsr commit_state_byte                                             ; 9598: 20 cb ac     ..
    lda #0                                                            ; 959b: a9 00       ..
    jsr error_inline_log                                              ; 959d: 20 bb 96     ..
    equs "Remoted", 0                                                 ; 95a0: 52 65 6d... Rem

    ldy #4                                                            ; 95a8: a0 04       ..
    lda (net_rx_ptr),y                                                ; 95aa: b1 9c       ..
    beq c9573                                                         ; 95ac: f0 c5       ..
    ldy #&80                                                          ; 95ae: a0 80       ..
    lda (net_rx_ptr),y                                                ; 95b0: b1 9c       ..
    ldy #&0e                                                          ; 95b2: a0 0e       ..
    cmp (nfs_workspace),y                                             ; 95b4: d1 9e       ..
    bne c9570                                                         ; 95b6: d0 b8       ..
    ldy #&82                                                          ; 95b8: a0 82       ..
    lda (net_rx_ptr),y                                                ; 95ba: b1 9c       ..
    tay                                                               ; 95bc: a8          .
    ldx #0                                                            ; 95bd: a2 00       ..
    jsr commit_state_byte                                             ; 95bf: 20 cb ac     ..
    lda #osbyte_insert_input_buffer                                   ; 95c2: a9 99       ..
    jmp osbyte                                                        ; 95c4: 4c f4 ff    L..            ; Insert character Y into input buffer X

; &95c7 referenced 6 times by &94e0, &999e, &9ad8, &a923, &abbf, &ac61
.wait_net_tx_ack
    lda l0d6f                                                         ; 95c7: ad 6f 0d    .o.
    pha                                                               ; 95ca: 48          H
    lda l0d61                                                         ; 95cb: ad 61 0d    .a.
    pha                                                               ; 95ce: 48          H
    lda net_tx_ptr_hi                                                 ; 95cf: a5 9b       ..
    bne c95d8                                                         ; 95d1: d0 05       ..
    ora #&80                                                          ; 95d3: 09 80       ..
    sta l0d61                                                         ; 95d5: 8d 61 0d    .a.
; &95d8 referenced 1 time by &95d1
.c95d8
    lda #0                                                            ; 95d8: a9 00       ..
    pha                                                               ; 95da: 48          H
    pha                                                               ; 95db: 48          H
    tay                                                               ; 95dc: a8          .              ; Y=&00
    tsx                                                               ; 95dd: ba          .
; &95de referenced 3 times by &95e5, &95ea, &95ef
.c95de
    lda (net_tx_ptr),y                                                ; 95de: b1 9a       ..
    bmi c95f1                                                         ; 95e0: 30 0f       0.
    dec error_text,x                                                  ; 95e2: de 01 01    ...
    bne c95de                                                         ; 95e5: d0 f7       ..
    dec l0102,x                                                       ; 95e7: de 02 01    ...
    bne c95de                                                         ; 95ea: d0 f2       ..
    dec l0104,x                                                       ; 95ec: de 04 01    ...
    bne c95de                                                         ; 95ef: d0 ed       ..
; &95f1 referenced 1 time by &95e0
.c95f1
    pla                                                               ; 95f1: 68          h
    pla                                                               ; 95f2: 68          h
    pla                                                               ; 95f3: 68          h
    sta l0d61                                                         ; 95f4: 8d 61 0d    .a.
    pla                                                               ; 95f7: 68          h
    beq c9604                                                         ; 95f8: f0 0a       ..
    rts                                                               ; 95fa: 60          `

; &95fb referenced 6 times by &9611, &964a, &9666, &9690, &96a2, &96bb
.cond_save_error_code
    bit l0d6c                                                         ; 95fb: 2c 6c 0d    ,l.
    bpl return_16                                                     ; 95fe: 10 03       ..
    sta l0e09                                                         ; 9600: 8d 09 0e    ...
; &9603 referenced 1 time by &95fe
.return_16
    rts                                                               ; 9603: 60          `

; &9604 referenced 1 time by &95f8
.c9604
    ldx #8                                                            ; 9604: a2 08       ..
    ldy net_error_lookup_data,x                                       ; 9606: bc 98 97    ...
    ldx #0                                                            ; 9609: a2 00       ..
    stx error_block                                                   ; 960b: 8e 00 01    ...
    lda error_msg_table,y                                             ; 960e: b9 a4 97    ...
    jsr cond_save_error_code                                          ; 9611: 20 fb 95     ..
; &9614 referenced 1 time by &961e
.loop_c9614
    lda error_msg_table,y                                             ; 9614: b9 a4 97    ...
    sta error_text,x                                                  ; 9617: 9d 01 01    ...
    beq c9620                                                         ; 961a: f0 04       ..
    inx                                                               ; 961c: e8          .
    iny                                                               ; 961d: c8          .
    bne loop_c9614                                                    ; 961e: d0 f4       ..
; &9620 referenced 1 time by &961a
.c9620
    jsr append_drv_dot_num                                            ; 9620: 20 38 97     8.
    lda #0                                                            ; 9623: a9 00       ..
    sta error_text,x                                                  ; 9625: 9d 01 01    ...
    jmp check_net_error_code                                          ; 9628: 4c da 96    L..

; &962b referenced 1 time by &98b1
.fixup_reply_status_a
    lda (net_tx_ptr,x)                                                ; 962b: a1 9a       ..
    cmp #&41 ; 'A'                                                    ; 962d: c9 41       .A
    bne c9633                                                         ; 962f: d0 02       ..
    lda #&42 ; 'B'                                                    ; 9631: a9 42       .B
; &9633 referenced 1 time by &962f
.c9633
    clv                                                               ; 9633: b8          .
    bvc c963b                                                         ; 9634: 50 05       P.             ; ALWAYS branch

; &9636 referenced 1 time by &986a
.load_reply_and_classify
    lda (net_tx_ptr,x)                                                ; 9636: a1 9a       ..
; &9638 referenced 2 times by &9567, &9dd0
.classify_reply_error
    bit bit_test_ff_pad                                               ; 9638: 2c 7d 94    ,}.
; &963b referenced 1 time by &9634
.c963b
    and #7                                                            ; 963b: 29 07       ).
    pha                                                               ; 963d: 48          H
    cmp #2                                                            ; 963e: c9 02       ..
    bne c9684                                                         ; 9640: d0 42       .B
    php                                                               ; 9642: 08          .
    tax                                                               ; 9643: aa          .
    ldy net_error_lookup_data,x                                       ; 9644: bc 98 97    ...
    lda error_msg_table,y                                             ; 9647: b9 a4 97    ...
    jsr cond_save_error_code                                          ; 964a: 20 fb 95     ..
    ldx #0                                                            ; 964d: a2 00       ..
    stx error_block                                                   ; 964f: 8e 00 01    ...
; &9652 referenced 1 time by &965c
.loop_c9652
    lda error_msg_table,y                                             ; 9652: b9 a4 97    ...
    sta error_text,x                                                  ; 9655: 9d 01 01    ...
    beq c965e                                                         ; 9658: f0 04       ..
    iny                                                               ; 965a: c8          .
    inx                                                               ; 965b: e8          .
    bne loop_c9652                                                    ; 965c: d0 f4       ..
; &965e referenced 1 time by &9658
.c965e
    jsr append_drv_dot_num                                            ; 965e: 20 38 97     8.
    plp                                                               ; 9661: 28          (
    bvs c9670                                                         ; 9662: 70 0c       p.
    lda #&a4                                                          ; 9664: a9 a4       ..
    jsr cond_save_error_code                                          ; 9666: 20 fb 95     ..
    sta error_text                                                    ; 9669: 8d 01 01    ...
    ldy #&0b                                                          ; 966c: a0 0b       ..
    bne c9672                                                         ; 966e: d0 02       ..             ; ALWAYS branch

; &9670 referenced 1 time by &9662
.c9670
    ldy #9                                                            ; 9670: a0 09       ..
; &9672 referenced 1 time by &966e
.c9672
    lda net_error_lookup_data,y                                       ; 9672: b9 98 97    ...
    tay                                                               ; 9675: a8          .
; &9676 referenced 1 time by &9680
.loop_c9676
    lda error_msg_table,y                                             ; 9676: b9 a4 97    ...
    sta error_text,x                                                  ; 9679: 9d 01 01    ...
    beq c9682                                                         ; 967c: f0 04       ..
    iny                                                               ; 967e: c8          .
    inx                                                               ; 967f: e8          .
    bne loop_c9676                                                    ; 9680: d0 f4       ..
; &9682 referenced 1 time by &967c
.c9682
    beq c9699                                                         ; 9682: f0 15       ..
; &9684 referenced 1 time by &9640
.c9684
    tax                                                               ; 9684: aa          .
    ldy net_error_lookup_data,x                                       ; 9685: bc 98 97    ...
    ldx #0                                                            ; 9688: a2 00       ..
    stx error_block                                                   ; 968a: 8e 00 01    ...
    lda error_msg_table,y                                             ; 968d: b9 a4 97    ...
    jsr cond_save_error_code                                          ; 9690: 20 fb 95     ..
; &9693 referenced 1 time by &969d
.loop_c9693
    lda error_msg_table,y                                             ; 9693: b9 a4 97    ...
    sta error_text,x                                                  ; 9696: 9d 01 01    ...
; &9699 referenced 1 time by &9682
.c9699
    beq check_net_error_code                                          ; 9699: f0 3f       .?
    iny                                                               ; 969b: c8          .
    inx                                                               ; 969c: e8          .
.bad_str_anchor
bad_prefix = bad_str_anchor+1
    bne loop_c9693                                                    ; 969d: d0 f4       ..
; &969e referenced 1 time by &96af
    equs "Bad"                                                        ; 969f: 42 61 64    Bad

; ***************************************************************************************
; Generate 'Bad ...' BRK error from inline string
; 
; Like error_inline, but prepends 'Bad ' to the error message. Copies
; the prefix from a lookup table, then appends the null-terminated
; inline string. The error number is passed in A. Never returns.
; 
; On Entry:
;     A: error number
; ***************************************************************************************
; &96a2 referenced 11 times by &8fcd, &91f6, &9203, &9217, &9223, &9232, &92e8, &936d, &9390, &a247, &bc5b
.error_bad_inline
    jsr cond_save_error_code                                          ; 96a2: 20 fb 95     ..            ; Conditionally log error code to workspace
    tay                                                               ; 96a5: a8          .              ; Save error number in Y
    pla                                                               ; 96a6: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 96a7: 85 b0       ..
    pla                                                               ; 96a9: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 96aa: 85 b1       ..
    ldx #0                                                            ; 96ac: a2 00       ..
; &96ae referenced 1 time by &96b7
.loop_c96ae
    inx                                                               ; 96ae: e8          .              ; Copy 'Bad ' prefix from lookup table
    lda bad_prefix,x                                                  ; 96af: bd 9e 96    ...
    sta error_text,x                                                  ; 96b2: 9d 01 01    ...
    cmp #&20 ; ' '                                                    ; 96b5: c9 20       .
    bne loop_c96ae                                                    ; 96b7: d0 f5       ..
    beq write_error_num_and_str                                       ; 96b9: f0 0c       ..             ; ALWAYS branch

; ***************************************************************************************
; Generate BRK error from inline string (with logging)
; 
; Like error_inline, but first conditionally logs the error code to
; workspace via sub_c95fb before building the error block.
; 
; On Entry:
;     A: error number
; ***************************************************************************************
; &96bb referenced 10 times by &941b, &959d, &a25e, &abee, &ac00, &b475, &b4ec, &b538, &b7e0, &b81b
.error_inline_log
    jsr cond_save_error_code                                          ; 96bb: 20 fb 95     ..            ; Conditionally log error code to workspace
; ***************************************************************************************
; Generate BRK error from inline string
; 
; Pops the return address from the stack and copies the null-terminated
; inline string into the error block at &0100. The error number is
; passed in A. Never returns — triggers the error via JMP error_block.
; 
; On Entry:
;     A: error number
; ***************************************************************************************
; &96be referenced 4 times by &a111, &b9fc, &bb2c, &bbee
.error_inline
    tay                                                               ; 96be: a8          .              ; Save error number in Y
    pla                                                               ; 96bf: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 96c0: 85 b0       ..
    pla                                                               ; 96c2: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 96c3: 85 b1       ..
    ldx #0                                                            ; 96c5: a2 00       ..
; &96c7 referenced 1 time by &96b9
.write_error_num_and_str
    sty error_text                                                    ; 96c7: 8c 01 01    ...            ; Store error number in error block
    tya                                                               ; 96ca: 98          .
    pha                                                               ; 96cb: 48          H
    ldy #0                                                            ; 96cc: a0 00       ..
    sty error_block                                                   ; 96ce: 8c 00 01    ...            ; Zero the BRK byte at &0100
; &96d1 referenced 1 time by &96d8
.loop_c96d1
    inx                                                               ; 96d1: e8          .              ; Copy inline string into error block
    iny                                                               ; 96d2: c8          .
    lda (fs_load_addr),y                                              ; 96d3: b1 b0       ..             ; Read next byte from inline string
    sta error_text,x                                                  ; 96d5: 9d 01 01    ...
    bne loop_c96d1                                                    ; 96d8: d0 f7       ..             ; Loop until null terminator
; &96da referenced 4 times by &9557, &9628, &9699, &b966
.check_net_error_code
    ldy #&0e                                                          ; 96da: a0 0e       ..
    lda (net_rx_ptr),y                                                ; 96dc: b1 9c       ..
    bne c96e8                                                         ; 96de: d0 08       ..
    pla                                                               ; 96e0: 68          h
    cmp #&de                                                          ; 96e1: c9 de       ..
    beq c972b                                                         ; 96e3: f0 46       .F
; &96e5 referenced 1 time by &9736
.c96e5
    jmp error_block                                                   ; 96e5: 4c 00 01    L..

; &96e8 referenced 1 time by &96de
.c96e8
    sta l0d6d                                                         ; 96e8: 8d 6d 0d    .m.
    pha                                                               ; 96eb: 48          H
    txa                                                               ; 96ec: 8a          .
    pha                                                               ; 96ed: 48          H
    ldy #&0e                                                          ; 96ee: a0 0e       ..
    lda (net_rx_ptr),y                                                ; 96f0: b1 9c       ..
    sta fs_load_addr                                                  ; 96f2: 85 b0       ..
    lda #0                                                            ; 96f4: a9 00       ..
    sta (net_rx_ptr),y                                                ; 96f6: 91 9c       ..
    lda #&c6                                                          ; 96f8: a9 c6       ..
    jsr osbyte_x0                                                     ; 96fa: 20 6d 8e     m.            ; OSBYTE with X=0, Y=&FF.
; Called from dispatch table for specific OSBYTE calls.
    cpy fs_load_addr                                                  ; 96fd: c4 b0       ..
    beq c970a                                                         ; 96ff: f0 09       ..
    cpx fs_load_addr                                                  ; 9701: e4 b0       ..
    bne c9717                                                         ; 9703: d0 12       ..
    pha                                                               ; 9705: 48          H
    lda #&c6                                                          ; 9706: a9 c6       ..
    bne c970d                                                         ; 9708: d0 03       ..             ; ALWAYS branch

; &970a referenced 1 time by &96ff
.c970a
    pha                                                               ; 970a: 48          H
    lda #&c7                                                          ; 970b: a9 c7       ..
; &970d referenced 1 time by &9708
.c970d
    jsr osbyte_x0_y0                                                  ; 970d: 20 76 8e     v.
    pla                                                               ; 9710: 68          h
    tay                                                               ; 9711: a8          .
    lda #osfind_close                                                 ; 9712: a9 00       ..
    jsr osfind                                                        ; 9714: 20 ce ff     ..            ; Close one or all files
; &9717 referenced 1 time by &9703
.c9717
    pla                                                               ; 9717: 68          h
    tax                                                               ; 9718: aa          .
    ldy #&0a                                                          ; 9719: a0 0a       ..
    lda net_error_lookup_data,y                                       ; 971b: b9 98 97    ...
    tay                                                               ; 971e: a8          .
; &971f referenced 1 time by &9729
.loop_c971f
    lda error_msg_table,y                                             ; 971f: b9 a4 97    ...
    sta error_text,x                                                  ; 9722: 9d 01 01    ...
    beq c972b                                                         ; 9725: f0 04       ..
    inx                                                               ; 9727: e8          .
    iny                                                               ; 9728: c8          .
    bne loop_c971f                                                    ; 9729: d0 f4       ..
; &972b referenced 2 times by &96e3, &9725
.c972b
    stx fs_load_addr_2                                                ; 972b: 86 b2       ..
    pla                                                               ; 972d: 68          h
    jsr append_space_and_num                                          ; 972e: 20 5c 97     \.
    lda #0                                                            ; 9731: a9 00       ..
    sta l0102,x                                                       ; 9733: 9d 02 01    ...
    beq c96e5                                                         ; 9736: f0 ad       ..             ; ALWAYS branch

; &9738 referenced 2 times by &9620, &965e
.append_drv_dot_num
    lda #&20 ; ' '                                                    ; 9738: a9 20       .
    sta error_text,x                                                  ; 973a: 9d 01 01    ...
    inx                                                               ; 973d: e8          .
    stx fs_load_addr_2                                                ; 973e: 86 b2       ..
    ldy #3                                                            ; 9740: a0 03       ..
    lda (net_tx_ptr),y                                                ; 9742: b1 9a       ..
    beq c9752                                                         ; 9744: f0 0c       ..
    jsr append_decimal_num                                            ; 9746: 20 67 97     g.
    ldx fs_load_addr_2                                                ; 9749: a6 b2       ..
    lda #&2e ; '.'                                                    ; 974b: a9 2e       ..
    sta error_text,x                                                  ; 974d: 9d 01 01    ...
    inc fs_load_addr_2                                                ; 9750: e6 b2       ..
; &9752 referenced 1 time by &9744
.c9752
    ldy #2                                                            ; 9752: a0 02       ..
    lda (net_tx_ptr),y                                                ; 9754: b1 9a       ..
    jsr append_decimal_num                                            ; 9756: 20 67 97     g.
    ldx fs_load_addr_2                                                ; 9759: a6 b2       ..
    rts                                                               ; 975b: 60          `

; &975c referenced 2 times by &972e, &b4ca
.append_space_and_num
    tay                                                               ; 975c: a8          .
    lda #&20 ; ' '                                                    ; 975d: a9 20       .
    ldx fs_load_addr_2                                                ; 975f: a6 b2       ..
    sta error_text,x                                                  ; 9761: 9d 01 01    ...
    inc fs_load_addr_2                                                ; 9764: e6 b2       ..
    tya                                                               ; 9766: 98          .
; &9767 referenced 2 times by &9746, &9756
.append_decimal_num
    tay                                                               ; 9767: a8          .
    bit bit_test_ff_pad                                               ; 9768: 2c 7d 94    ,}.
    lda #&64 ; 'd'                                                    ; 976b: a9 64       .d
    jsr append_decimal_digit                                          ; 976d: 20 78 97     x.
    lda #&0a                                                          ; 9770: a9 0a       ..
    jsr append_decimal_digit                                          ; 9772: 20 78 97     x.
    lda #1                                                            ; 9775: a9 01       ..
    clv                                                               ; 9777: b8          .
; &9778 referenced 2 times by &976d, &9772
.append_decimal_digit
    sta fs_load_addr_3                                                ; 9778: 85 b3       ..
    tya                                                               ; 977a: 98          .
    ldx #&2f ; '/'                                                    ; 977b: a2 2f       ./
    php                                                               ; 977d: 08          .
    sec                                                               ; 977e: 38          8
; &977f referenced 1 time by &9782
.loop_c977f
    inx                                                               ; 977f: e8          .
    sbc fs_load_addr_3                                                ; 9780: e5 b3       ..
    bcs loop_c977f                                                    ; 9782: b0 fb       ..
    adc fs_load_addr_3                                                ; 9784: 65 b3       e.
    plp                                                               ; 9786: 28          (
    tay                                                               ; 9787: a8          .
    txa                                                               ; 9788: 8a          .
    cmp #&30 ; '0'                                                    ; 9789: c9 30       .0
    bne c978f                                                         ; 978b: d0 02       ..
    bvs return_17                                                     ; 978d: 70 08       p.
; &978f referenced 1 time by &978b
.c978f
    clv                                                               ; 978f: b8          .
    ldx fs_load_addr_2                                                ; 9790: a6 b2       ..
    sta error_text,x                                                  ; 9792: 9d 01 01    ...
    inc fs_load_addr_2                                                ; 9795: e6 b2       ..
; &9797 referenced 1 time by &978d
.return_17
    rts                                                               ; 9797: 60          `

; &9798 referenced 5 times by &9606, &9644, &9672, &9685, &971b
.net_error_lookup_data
    equb 0, &0d, &18                                                  ; 9798: 00 0d 18    ...
    equs "!+++3?Veq"                                                  ; 979b: 21 2b 2b... !++
; &97a4 referenced 8 times by &960e, &9614, &9647, &9652, &9676, &968d, &9693, &971f
.error_msg_table
    equb &a0                                                          ; 97a4: a0          .
    equs "Line jammed"                                                ; 97a5: 4c 69 6e... Lin
    equb 0, &a1                                                       ; 97b0: 00 a1       ..
    equs "Net error"                                                  ; 97b2: 4e 65 74... Net
    equb 0, &a2                                                       ; 97bb: 00 a2       ..
    equs "Station"                                                    ; 97bd: 53 74 61... Sta
    equb 0, &a3                                                       ; 97c4: 00 a3       ..
    equs "No clock"                                                   ; 97c6: 4e 6f 20... No
    equb 0, &11                                                       ; 97ce: 00 11       ..
    equs "Escape"                                                     ; 97d0: 45 73 63... Esc
    equb 0, &cb                                                       ; 97d6: 00 cb       ..
    equs "Bad option"                                                 ; 97d8: 42 61 64... Bad
    equb 0, &a5                                                       ; 97e2: 00 a5       ..
    equs "No reply from station"                                      ; 97e4: 4e 6f 20... No
    equb 0                                                            ; 97f9: 00          .
    equs " not listening"                                             ; 97fa: 20 6e 6f...  no
    equb 0                                                            ; 9808: 00          .
    equs " on channel"                                                ; 9809: 20 6f 6e...  on
    equb 0                                                            ; 9814: 00          .
    equs " not present"                                               ; 9815: 20 6e 6f...  no
    equb 0                                                            ; 9821: 00          .

; &9822 referenced 2 times by &94d8, &9ac9
.init_tx_ptr_and_send
    ldx #&c0                                                          ; 9822: a2 c0       ..
    stx net_tx_ptr                                                    ; 9824: 86 9a       ..
    ldx #0                                                            ; 9826: a2 00       ..
    stx net_tx_ptr_hi                                                 ; 9828: 86 9b       ..
; &982a referenced 7 times by &a90c, &a965, &a9c2, &abb4, &ac3f, &b03b, &b216
.send_net_packet
    lda l0d6e                                                         ; 982a: ad 6e 0d    .n.
    bne c9831                                                         ; 982d: d0 02       ..
    lda #&ff                                                          ; 982f: a9 ff       ..
; &9831 referenced 1 time by &982d
.c9831
    ldy #&60 ; '`'                                                    ; 9831: a0 60       .`
    pha                                                               ; 9833: 48          H
    tya                                                               ; 9834: 98          .              ; A=&60
    pha                                                               ; 9835: 48          H
    ldx #0                                                            ; 9836: a2 00       ..
    lda (net_tx_ptr,x)                                                ; 9838: a1 9a       ..
; &983a referenced 1 time by &985c
.c983a
    sta (net_tx_ptr,x)                                                ; 983a: 81 9a       ..
    pha                                                               ; 983c: 48          H
    jsr c98b4                                                         ; 983d: 20 b4 98     ..
    asl a                                                             ; 9840: 0a          .
    bpl c986d                                                         ; 9841: 10 2a       .*
    asl a                                                             ; 9843: 0a          .
    beq c9869                                                         ; 9844: f0 23       .#
    jsr check_escape                                                  ; 9846: 20 5a 95     Z.
    pla                                                               ; 9849: 68          h
    tax                                                               ; 984a: aa          .
    pla                                                               ; 984b: 68          h
    tay                                                               ; 984c: a8          .
    pla                                                               ; 984d: 68          h
    beq c985e                                                         ; 984e: f0 0e       ..
; &9850 referenced 1 time by &9867
.loop_c9850
    sbc #1                                                            ; 9850: e9 01       ..
    pha                                                               ; 9852: 48          H
    tya                                                               ; 9853: 98          .
    pha                                                               ; 9854: 48          H
    txa                                                               ; 9855: 8a          .
; &9856 referenced 2 times by &9857, &985a
.c9856
    dex                                                               ; 9856: ca          .
    bne c9856                                                         ; 9857: d0 fd       ..
    dey                                                               ; 9859: 88          .
    bne c9856                                                         ; 985a: d0 fa       ..
    beq c983a                                                         ; 985c: f0 dc       ..             ; ALWAYS branch

; &985e referenced 1 time by &984e
.c985e
    cmp l0d6e                                                         ; 985e: cd 6e 0d    .n.
    bne c9869                                                         ; 9861: d0 06       ..
    lda #&80                                                          ; 9863: a9 80       ..
    sta escapable                                                     ; 9865: 85 97       ..
    bne loop_c9850                                                    ; 9867: d0 e7       ..             ; ALWAYS branch

; &9869 referenced 2 times by &9844, &9861
.c9869
    tax                                                               ; 9869: aa          .
    jmp load_reply_and_classify                                       ; 986a: 4c 36 96    L6.

; &986d referenced 1 time by &9841
.c986d
    pla                                                               ; 986d: 68          h
    pla                                                               ; 986e: 68          h
    pla                                                               ; 986f: 68          h
    jmp clear_escapable                                               ; 9870: 4c 8b 92    L..

; &9873 referenced 2 times by &9889, &98e3
.pass_txbuf_init_table
    equb &88, 0, &fd, &fd, &3a, &0d, &ff, &ff, &3e, &0d, &ff, &ff     ; 9873: 88 00 fd... ...

; &987f referenced 1 time by &8df4
.init_tx_ptr_for_pass
    ldy #&c0                                                          ; 987f: a0 c0       ..
    sty net_tx_ptr                                                    ; 9881: 84 9a       ..
    ldy #0                                                            ; 9883: a0 00       ..
    sty net_tx_ptr_hi                                                 ; 9885: 84 9b       ..
; &9887 referenced 1 time by &abb1
.setup_pass_txbuf
    ldy #&0b                                                          ; 9887: a0 0b       ..
; &9889 referenced 1 time by &9897
.loop_c9889
    ldx pass_txbuf_init_table,y                                       ; 9889: be 73 98    .s.
    cpx #&fd                                                          ; 988c: e0 fd       ..
    beq c9896                                                         ; 988e: f0 06       ..
    lda (net_tx_ptr),y                                                ; 9890: b1 9a       ..
    pha                                                               ; 9892: 48          H
    txa                                                               ; 9893: 8a          .
    sta (net_tx_ptr),y                                                ; 9894: 91 9a       ..
; &9896 referenced 1 time by &988e
.c9896
    dey                                                               ; 9896: 88          .
    bpl loop_c9889                                                    ; 9897: 10 f0       ..
    lda l0d70                                                         ; 9899: ad 70 0d    .p.
    pha                                                               ; 989c: 48          H
    tya                                                               ; 989d: 98          .
    pha                                                               ; 989e: 48          H
    ldx #0                                                            ; 989f: a2 00       ..
    lda (net_tx_ptr,x)                                                ; 98a1: a1 9a       ..
; &98a3 referenced 1 time by &98dc
.c98a3
    sta (net_tx_ptr,x)                                                ; 98a3: 81 9a       ..
    pha                                                               ; 98a5: 48          H
    jsr c98b4                                                         ; 98a6: 20 b4 98     ..
    asl a                                                             ; 98a9: 0a          .
    bpl c98de                                                         ; 98aa: 10 32       .2
    asl a                                                             ; 98ac: 0a          .
    bne c98c9                                                         ; 98ad: d0 1a       ..
; &98af referenced 1 time by &98ce
.loop_c98af
    ldx #0                                                            ; 98af: a2 00       ..
    jmp fixup_reply_status_a                                          ; 98b1: 4c 2b 96    L+.

; &98b4 referenced 3 times by &983d, &98a6, &98b7
.c98b4
    asl ws_0d60                                                       ; 98b4: 0e 60 0d    .`.
    bcc c98b4                                                         ; 98b7: 90 fb       ..
    lda net_tx_ptr                                                    ; 98b9: a5 9a       ..
    sta nmi_tx_block                                                  ; 98bb: 85 a0       ..
    lda net_tx_ptr_hi                                                 ; 98bd: a5 9b       ..
    sta nmi_tx_block_hi                                               ; 98bf: 85 a1       ..
    jsr tx_begin                                                      ; 98c1: 20 82 85     ..            ; Begin Econet transmission. Copy dest
; station/network from TX control block,
; set up immediate op params, poll for idle
; line before starting frame.
; &98c4 referenced 1 time by &98c6
.loop_c98c4
    lda (net_tx_ptr,x)                                                ; 98c4: a1 9a       ..
    bmi loop_c98c4                                                    ; 98c6: 30 fc       0.
    rts                                                               ; 98c8: 60          `

; &98c9 referenced 1 time by &98ad
.c98c9
    pla                                                               ; 98c9: 68          h
    tax                                                               ; 98ca: aa          .
    pla                                                               ; 98cb: 68          h
    tay                                                               ; 98cc: a8          .
    pla                                                               ; 98cd: 68          h
    beq loop_c98af                                                    ; 98ce: f0 df       ..
    sbc #1                                                            ; 98d0: e9 01       ..
    pha                                                               ; 98d2: 48          H
    tya                                                               ; 98d3: 98          .
    pha                                                               ; 98d4: 48          H
    txa                                                               ; 98d5: 8a          .
; &98d6 referenced 2 times by &98d7, &98da
.c98d6
    dex                                                               ; 98d6: ca          .
    bne c98d6                                                         ; 98d7: d0 fd       ..
    dey                                                               ; 98d9: 88          .
    bne c98d6                                                         ; 98da: d0 fa       ..
    beq c98a3                                                         ; 98dc: f0 c5       ..             ; ALWAYS branch

; &98de referenced 1 time by &98aa
.c98de
    pla                                                               ; 98de: 68          h
    pla                                                               ; 98df: 68          h
    pla                                                               ; 98e0: 68          h
    ldy #0                                                            ; 98e1: a0 00       ..
; &98e3 referenced 1 time by &98f0
.loop_c98e3
    ldx pass_txbuf_init_table,y                                       ; 98e3: be 73 98    .s.
    cpx #&fd                                                          ; 98e6: e0 fd       ..
    beq c98ed                                                         ; 98e8: f0 03       ..
    pla                                                               ; 98ea: 68          h
    sta (net_tx_ptr),y                                                ; 98eb: 91 9a       ..
; &98ed referenced 1 time by &98e8
.c98ed
    iny                                                               ; 98ed: c8          .
    cpy #&0c                                                          ; 98ee: c0 0c       ..
    bne loop_c98e3                                                    ; 98f0: d0 f1       ..
    rts                                                               ; 98f2: 60          `

; &98f3 referenced 1 time by &9924
.load_text_ptr_and_parse
    ldy #1                                                            ; 98f3: a0 01       ..
; &98f5 referenced 1 time by &98fb
.loop_c98f5
    lda (fs_options),y                                                ; 98f5: b1 bb       ..
    sta os_text_ptr,y                                                 ; 98f7: 99 f2 00    ...
    dey                                                               ; 98fa: 88          .
    bpl loop_c98f5                                                    ; 98fb: 10 f8       ..
    ldy #0                                                            ; 98fd: a0 00       ..
; &98ff referenced 1 time by &ae82
.gsread_to_buf
    ldx #&ff                                                          ; 98ff: a2 ff       ..
    clc                                                               ; 9901: 18          .
    jsr gsinit                                                        ; 9902: 20 c2 ff     ..
    beq c9912                                                         ; 9905: f0 0b       ..
; &9907 referenced 1 time by &9910
.loop_c9907
    jsr gsread                                                        ; 9907: 20 c5 ff     ..
    bcs c9912                                                         ; 990a: b0 06       ..
    inx                                                               ; 990c: e8          .
    sta l0e30,x                                                       ; 990d: 9d 30 0e    .0.
    bcc loop_c9907                                                    ; 9910: 90 f5       ..             ; ALWAYS branch

; &9912 referenced 2 times by &9905, &990a
.c9912
    inx                                                               ; 9912: e8          .
    lda #&0d                                                          ; 9913: a9 0d       ..
    sta l0e30,x                                                       ; 9915: 9d 30 0e    .0.
    lda #&30 ; '0'                                                    ; 9918: a9 30       .0
    sta fs_crc_lo                                                     ; 991a: 85 be       ..
    lda #&0e                                                          ; 991c: a9 0e       ..
    sta fs_crc_hi                                                     ; 991e: 85 bf       ..
    rts                                                               ; 9920: 60          `

    jsr set_xfer_params                                               ; 9921: 20 81 92     ..
    jsr load_text_ptr_and_parse                                       ; 9924: 20 f3 98     ..
    jsr mask_owner_access                                             ; 9927: 20 12 af     ..
    jsr parse_access_prefix                                           ; 992a: 20 85 ae     ..
    lda fs_last_byte_flag                                             ; 992d: a5 bd       ..
    bpl c99af                                                         ; 992f: 10 7e       .~
    cmp #&ff                                                          ; 9931: c9 ff       ..
    beq c9938                                                         ; 9933: f0 03       ..
    jmp return_with_last_flag                                         ; 9935: 4c b9 9c    L..

; &9938 referenced 1 time by &9933
.c9938
    jsr copy_arg_to_buf_x0                                            ; 9938: 20 f0 ae     ..
    ldy #2                                                            ; 993b: a0 02       ..
; &993d referenced 1 time by &a2b9
.do_fs_cmd_iteration
    lda #&92                                                          ; 993d: a9 92       ..
    sta escapable                                                     ; 993f: 85 97       ..
    sta l0f02                                                         ; 9941: 8d 02 0f    ...
    jsr send_request_write                                            ; 9944: 20 87 94     ..
    ldy #6                                                            ; 9947: a0 06       ..
    lda (fs_options),y                                                ; 9949: b1 bb       ..
    bne c9955                                                         ; 994b: d0 08       ..
    jsr copy_fsopts_to_zp                                             ; 994d: 20 60 9a     `.
    jsr copy_workspace_to_fsopts                                      ; 9950: 20 72 9a     r.
    bcc c995b                                                         ; 9953: 90 06       ..
; &9955 referenced 1 time by &994b
.c9955
    jsr copy_workspace_to_fsopts                                      ; 9955: 20 72 9a     r.
    jsr copy_fsopts_to_zp                                             ; 9958: 20 60 9a     `.
; &995b referenced 1 time by &9953
.c995b
    ldy #4                                                            ; 995b: a0 04       ..
; &995d referenced 1 time by &9968
.loop_c995d
    lda fs_load_addr,x                                                ; 995d: b5 b0       ..
    sta txcb_end,x                                                    ; 995f: 95 c8       ..
    adc l0f0d,x                                                       ; 9961: 7d 0d 0f    }..
    sta fs_work_4,x                                                   ; 9964: 95 b4       ..
    inx                                                               ; 9966: e8          .
    dey                                                               ; 9967: 88          .
    bne loop_c995d                                                    ; 9968: d0 f3       ..
    sec                                                               ; 996a: 38          8
    sbc l0f10                                                         ; 996b: ed 10 0f    ...
    sta fs_work_7                                                     ; 996e: 85 b7       ..
    jsr format_filename_field                                         ; 9970: 20 86 9b     ..
    jsr send_txcb_swap_addrs                                          ; 9973: 20 84 99     ..
    ldx #2                                                            ; 9976: a2 02       ..
; &9978 referenced 1 time by &997f
.loop_c9978
    lda l0f10,x                                                       ; 9978: bd 10 0f    ...
    sta l0f05,x                                                       ; 997b: 9d 05 0f    ...
    dex                                                               ; 997e: ca          .
    bpl loop_c9978                                                    ; 997f: 10 f7       ..
    jmp c9a0b                                                         ; 9981: 4c 0b 9a    L..

; &9984 referenced 2 times by &9973, &9f40
.send_txcb_swap_addrs
    jsr cmp_5byte_handle                                              ; 9984: 20 90 92     ..
    beq return_18                                                     ; 9987: f0 25       .%
    lda #&92                                                          ; 9989: a9 92       ..
    sta txcb_port                                                     ; 998b: 85 c1       ..
; &998d referenced 1 time by &99a9
.loop_c998d
    ldx #3                                                            ; 998d: a2 03       ..
; &998f referenced 1 time by &9998
.loop_c998f
    lda txcb_end,x                                                    ; 998f: b5 c8       ..
    sta txcb_start,x                                                  ; 9991: 95 c4       ..
    lda fs_work_4,x                                                   ; 9993: b5 b4       ..
    sta txcb_end,x                                                    ; 9995: 95 c8       ..
    dex                                                               ; 9997: ca          .
    bpl loop_c998f                                                    ; 9998: 10 f5       ..
    lda #&7f                                                          ; 999a: a9 7f       ..
    sta txcb_ctrl                                                     ; 999c: 85 c0       ..
    jsr wait_net_tx_ack                                               ; 999e: 20 c7 95     ..
    ldy #3                                                            ; 99a1: a0 03       ..
; &99a3 referenced 1 time by &99ac
.loop_c99a3
    lda txcb_end,y                                                    ; 99a3: b9 c8 00    ...
    eor fs_work_4,y                                                   ; 99a6: 59 b4 00    Y..
    bne loop_c998d                                                    ; 99a9: d0 e2       ..
    dey                                                               ; 99ab: 88          .
    bpl loop_c99a3                                                    ; 99ac: 10 f5       ..
; &99ae referenced 1 time by &9987
.return_18
    rts                                                               ; 99ae: 60          `

; &99af referenced 1 time by &992f
.c99af
    beq c99b4                                                         ; 99af: f0 03       ..
    jmp c9add                                                         ; 99b1: 4c dd 9a    L..

; &99b4 referenced 2 times by &99af, &9ae6
.c99b4
    ldx #4                                                            ; 99b4: a2 04       ..
    ldy #&0e                                                          ; 99b6: a0 0e       ..
    sec                                                               ; 99b8: 38          8
; &99b9 referenced 1 time by &99d3
.loop_c99b9
    lda (fs_options),y                                                ; 99b9: b1 bb       ..
    sta port_ws_offset,y                                              ; 99bb: 99 a6 00    ...
    jsr retreat_y_by_4                                                ; 99be: 20 7f 9a     ..
    sbc (fs_options),y                                                ; 99c1: f1 bb       ..
    sta l0f03,y                                                       ; 99c3: 99 03 0f    ...
    pha                                                               ; 99c6: 48          H
    lda (fs_options),y                                                ; 99c7: b1 bb       ..
    sta port_ws_offset,y                                              ; 99c9: 99 a6 00    ...
    pla                                                               ; 99cc: 68          h
    sta (fs_options),y                                                ; 99cd: 91 bb       ..
    jsr skip_one_and_advance5                                         ; 99cf: 20 6c 9a     l.
    dex                                                               ; 99d2: ca          .
    bne loop_c99b9                                                    ; 99d3: d0 e4       ..
    ldy #9                                                            ; 99d5: a0 09       ..
; &99d7 referenced 1 time by &99dd
.loop_c99d7
    lda (fs_options),y                                                ; 99d7: b1 bb       ..
    sta l0f03,y                                                       ; 99d9: 99 03 0f    ...
    dey                                                               ; 99dc: 88          .
    bne loop_c99d7                                                    ; 99dd: d0 f8       ..
    lda #&91                                                          ; 99df: a9 91       ..
    sta escapable                                                     ; 99e1: 85 97       ..
    sta l0f02                                                         ; 99e3: 8d 02 0f    ...
    sta fs_error_ptr                                                  ; 99e6: 85 b8       ..
    ldx #&0b                                                          ; 99e8: a2 0b       ..
    jsr copy_arg_to_buf                                               ; 99ea: 20 f2 ae     ..
    ldy #1                                                            ; 99ed: a0 01       ..
    lda fs_last_byte_flag                                             ; 99ef: a5 bd       ..
    cmp #7                                                            ; 99f1: c9 07       ..
    php                                                               ; 99f3: 08          .
    bne c99f8                                                         ; 99f4: d0 02       ..
    ldy #&1d                                                          ; 99f6: a0 1d       ..
; &99f8 referenced 1 time by &99f4
.c99f8
    jsr send_request_write                                            ; 99f8: 20 87 94     ..
    jsr format_filename_field                                         ; 99fb: 20 86 9b     ..
    plp                                                               ; 99fe: 28          (
    bne c9a05                                                         ; 99ff: d0 04       ..
    ldx #0                                                            ; 9a01: a2 00       ..
    beq c9a0e                                                         ; 9a03: f0 09       ..             ; ALWAYS branch

; &9a05 referenced 1 time by &99ff
.c9a05
    lda l0f05                                                         ; 9a05: ad 05 0f    ...
    jsr check_and_setup_txcb                                          ; 9a08: 20 88 9a     ..
; &9a0b referenced 1 time by &9981
.c9a0b
    jsr recv_and_process_reply                                        ; 9a0b: 20 dc 94     ..
; &9a0e referenced 1 time by &9a03
.c9a0e
    stx l0f08                                                         ; 9a0e: 8e 08 0f    ...
    ldy #&0e                                                          ; 9a11: a0 0e       ..
    lda l0f05                                                         ; 9a13: ad 05 0f    ...
    jsr get_prot_bits                                                 ; 9a16: 20 5f 92     _.
    beq c9a1e                                                         ; 9a19: f0 03       ..
; &9a1b referenced 1 time by &9a23
.loop_c9a1b
    lda l0ef7,y                                                       ; 9a1b: b9 f7 0e    ...
; &9a1e referenced 1 time by &9a19
.c9a1e
    sta (fs_options),y                                                ; 9a1e: 91 bb       ..
    iny                                                               ; 9a20: c8          .
    cpy #&12                                                          ; 9a21: c0 12       ..
    bne loop_c9a1b                                                    ; 9a23: d0 f6       ..
    ldy l0e06                                                         ; 9a25: ac 06 0e    ...
    beq return_19                                                     ; 9a28: f0 47       .G
    ldy #0                                                            ; 9a2a: a0 00       ..
; &9a2c referenced 1 time by &9a35
.loop_c9a2c
    lda l10f3,y                                                       ; 9a2c: b9 f3 10    ...
    jsr osasci                                                        ; 9a2f: 20 e3 ff     ..            ; Write character
    iny                                                               ; 9a32: c8          .
    cpy #&0c                                                          ; 9a33: c0 0c       ..
    bne loop_c9a2c                                                    ; 9a35: d0 f5       ..
    ldy #5                                                            ; 9a37: a0 05       ..
    jsr print_5_hex_bytes                                             ; 9a39: 20 50 9a     P.
    jsr print_load_exec_addrs                                         ; 9a3c: 20 45 9a     E.
    jsr osnewl                                                        ; 9a3f: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    jmp return_with_last_flag                                         ; 9a42: 4c b9 9c    L..

; &9a45 referenced 1 time by &9a3c
.print_load_exec_addrs
    ldy #9                                                            ; 9a45: a0 09       ..
    jsr print_5_hex_bytes                                             ; 9a47: 20 50 9a     P.
    ldy #&0c                                                          ; 9a4a: a0 0c       ..
    ldx #3                                                            ; 9a4c: a2 03       ..
    bne c9a52                                                         ; 9a4e: d0 02       ..             ; ALWAYS branch

; &9a50 referenced 2 times by &9a39, &9a47
.print_5_hex_bytes
    ldx #4                                                            ; 9a50: a2 04       ..
; &9a52 referenced 2 times by &9a4e, &9a59
.c9a52
    lda (fs_options),y                                                ; 9a52: b1 bb       ..
    jsr print_hex_byte                                                ; 9a54: 20 1b 91     ..
    dey                                                               ; 9a57: 88          .
    dex                                                               ; 9a58: ca          .
    bne c9a52                                                         ; 9a59: d0 f7       ..
    lda #&20 ; ' '                                                    ; 9a5b: a9 20       .
    jmp osasci                                                        ; 9a5d: 4c e3 ff    L..            ; Write character 32

; &9a60 referenced 2 times by &994d, &9958
.copy_fsopts_to_zp
    ldy #5                                                            ; 9a60: a0 05       ..
; &9a62 referenced 1 time by &9a6a
.loop_c9a62
    lda (fs_options),y                                                ; 9a62: b1 bb       ..
    sta l00ae,y                                                       ; 9a64: 99 ae 00    ...
    dey                                                               ; 9a67: 88          .
    cpy #2                                                            ; 9a68: c0 02       ..
    bcs loop_c9a62                                                    ; 9a6a: b0 f6       ..
; &9a6c referenced 1 time by &99cf
.skip_one_and_advance5
    iny                                                               ; 9a6c: c8          .
; &9a6d referenced 2 times by &9f1d, &b054
.advance_y_by_4
    iny                                                               ; 9a6d: c8          .
    iny                                                               ; 9a6e: c8          .
    iny                                                               ; 9a6f: c8          .
    iny                                                               ; 9a70: c8          .
; &9a71 referenced 1 time by &9a28
.return_19
    rts                                                               ; 9a71: 60          `

; &9a72 referenced 2 times by &9950, &9955
.copy_workspace_to_fsopts
    ldy #&0d                                                          ; 9a72: a0 0d       ..
    txa                                                               ; 9a74: 8a          .
; &9a75 referenced 1 time by &9a7d
.loop_c9a75
    sta (fs_options),y                                                ; 9a75: 91 bb       ..
    lda l0f02,y                                                       ; 9a77: b9 02 0f    ...
    dey                                                               ; 9a7a: 88          .
    cpy #2                                                            ; 9a7b: c0 02       ..
    bcs loop_c9a75                                                    ; 9a7d: b0 f6       ..
; &9a7f referenced 1 time by &99be
.retreat_y_by_4
    dey                                                               ; 9a7f: 88          .
; &9a80 referenced 2 times by &9afc, &9f25
.retreat_y_by_3
    dey                                                               ; 9a80: 88          .
    dey                                                               ; 9a81: 88          .
    dey                                                               ; 9a82: 88          .
    rts                                                               ; 9a83: 60          `

; &9a84 referenced 2 times by &9a8c, &9ad2
.c9a84
    pla                                                               ; 9a84: 68          h
    ldy fs_block_offset                                               ; 9a85: a4 bc       ..
    rts                                                               ; 9a87: 60          `

; &9a88 referenced 2 times by &9a08, &9f3b
.check_and_setup_txcb
    pha                                                               ; 9a88: 48          H
    jsr cmp_5byte_handle                                              ; 9a89: 20 90 92     ..
    beq c9a84                                                         ; 9a8c: f0 f6       ..
; &9a8e referenced 1 time by &9adb
.c9a8e
    ldx #0                                                            ; 9a8e: a2 00       ..
    ldy #4                                                            ; 9a90: a0 04       ..
    stx l0f08                                                         ; 9a92: 8e 08 0f    ...
    stx l0f09                                                         ; 9a95: 8e 09 0f    ...
    clc                                                               ; 9a98: 18          .
; &9a99 referenced 1 time by &9aa6
.loop_c9a99
    lda fs_load_addr,x                                                ; 9a99: b5 b0       ..
    sta txcb_start,x                                                  ; 9a9b: 95 c4       ..
    adc l0f06,x                                                       ; 9a9d: 7d 06 0f    }..
    sta txcb_end,x                                                    ; 9aa0: 95 c8       ..
    sta fs_load_addr,x                                                ; 9aa2: 95 b0       ..
    inx                                                               ; 9aa4: e8          .
    dey                                                               ; 9aa5: 88          .
    bne loop_c9a99                                                    ; 9aa6: d0 f1       ..
    bcs c9ab7                                                         ; 9aa8: b0 0d       ..
    sec                                                               ; 9aaa: 38          8
; &9aab referenced 1 time by &9ab3
.loop_c9aab
    lda fs_load_addr,y                                                ; 9aab: b9 b0 00    ...
    sbc fs_work_4,y                                                   ; 9aae: f9 b4 00    ...
    iny                                                               ; 9ab1: c8          .
    dex                                                               ; 9ab2: ca          .
    bne loop_c9aab                                                    ; 9ab3: d0 f6       ..
    bcc c9ac0                                                         ; 9ab5: 90 09       ..
; &9ab7 referenced 1 time by &9aa8
.c9ab7
    ldx #3                                                            ; 9ab7: a2 03       ..
; &9ab9 referenced 1 time by &9abe
.loop_c9ab9
    lda fs_work_4,x                                                   ; 9ab9: b5 b4       ..
    sta txcb_end,x                                                    ; 9abb: 95 c8       ..
    dex                                                               ; 9abd: ca          .
    bpl loop_c9ab9                                                    ; 9abe: 10 f9       ..
; &9ac0 referenced 1 time by &9ab5
.c9ac0
    pla                                                               ; 9ac0: 68          h
    pha                                                               ; 9ac1: 48          H
    php                                                               ; 9ac2: 08          .
    sta txcb_port                                                     ; 9ac3: 85 c1       ..
    lda #&80                                                          ; 9ac5: a9 80       ..
    sta txcb_ctrl                                                     ; 9ac7: 85 c0       ..
    jsr init_tx_ptr_and_send                                          ; 9ac9: 20 22 98     ".
    lda fs_error_ptr                                                  ; 9acc: a5 b8       ..
    jsr init_txcb_port                                                ; 9ace: 20 53 94     S.
    plp                                                               ; 9ad1: 28          (
    bcs c9a84                                                         ; 9ad2: b0 b0       ..
    lda #&91                                                          ; 9ad4: a9 91       ..
    sta txcb_port                                                     ; 9ad6: 85 c1       ..
    jsr wait_net_tx_ack                                               ; 9ad8: 20 c7 95     ..
    bne c9a8e                                                         ; 9adb: d0 b1       ..
; &9add referenced 1 time by &99b1
.c9add
    sta l0f05                                                         ; 9add: 8d 05 0f    ...
    cmp #7                                                            ; 9ae0: c9 07       ..
    bcc c9ae9                                                         ; 9ae2: 90 05       ..
    bne c9b35                                                         ; 9ae4: d0 4f       .O
    jmp c99b4                                                         ; 9ae6: 4c b4 99    L..

; &9ae9 referenced 1 time by &9ae2
.c9ae9
    cmp #6                                                            ; 9ae9: c9 06       ..
    beq c9b2a                                                         ; 9aeb: f0 3d       .=
    cmp #5                                                            ; 9aed: c9 05       ..
    beq c9b44                                                         ; 9aef: f0 53       .S
    cmp #4                                                            ; 9af1: c9 04       ..
    beq c9b3a                                                         ; 9af3: f0 45       .E
    cmp #1                                                            ; 9af5: c9 01       ..
    beq c9b0e                                                         ; 9af7: f0 15       ..
    asl a                                                             ; 9af9: 0a          .
    asl a                                                             ; 9afa: 0a          .
    tay                                                               ; 9afb: a8          .
    jsr retreat_y_by_3                                                ; 9afc: 20 80 9a     ..
    ldx #3                                                            ; 9aff: a2 03       ..
; &9b01 referenced 1 time by &9b08
.loop_c9b01
    lda (fs_options),y                                                ; 9b01: b1 bb       ..
    sta l0f06,x                                                       ; 9b03: 9d 06 0f    ...
    dey                                                               ; 9b06: 88          .
    dex                                                               ; 9b07: ca          .
    bpl loop_c9b01                                                    ; 9b08: 10 f7       ..
    ldx #5                                                            ; 9b0a: a2 05       ..
    bne c9b23                                                         ; 9b0c: d0 15       ..             ; ALWAYS branch

; &9b0e referenced 1 time by &9af7
.c9b0e
    jsr get_access_bits                                               ; 9b0e: 20 55 92     U.
    sta l0f0e                                                         ; 9b11: 8d 0e 0f    ...
    ldy #9                                                            ; 9b14: a0 09       ..
    ldx #8                                                            ; 9b16: a2 08       ..
; &9b18 referenced 1 time by &9b1f
.loop_c9b18
    lda (fs_options),y                                                ; 9b18: b1 bb       ..
    sta l0f05,x                                                       ; 9b1a: 9d 05 0f    ...
    dey                                                               ; 9b1d: 88          .
    dex                                                               ; 9b1e: ca          .
    bne loop_c9b18                                                    ; 9b1f: d0 f7       ..
    ldx #&0a                                                          ; 9b21: a2 0a       ..
; &9b23 referenced 2 times by &9b0c, &9b42
.c9b23
    jsr copy_arg_to_buf                                               ; 9b23: 20 f2 ae     ..
    ldy #&13                                                          ; 9b26: a0 13       ..
    bne c9b2f                                                         ; 9b28: d0 05       ..             ; ALWAYS branch

; &9b2a referenced 1 time by &9aeb
.c9b2a
    jsr copy_arg_to_buf_x0                                            ; 9b2a: 20 f0 ae     ..
    ldy #&14                                                          ; 9b2d: a0 14       ..
; &9b2f referenced 1 time by &9b28
.c9b2f
    bit bit_test_ff_pad                                               ; 9b2f: 2c 7d 94    ,}.
    jsr save_net_tx_cb_vset                                           ; 9b32: 20 9a 94     ..
; &9b35 referenced 1 time by &9ae4
.c9b35
    bcs c9b80                                                         ; 9b35: b0 49       .I
    jmp return_with_last_flag                                         ; 9b37: 4c b9 9c    L..

; &9b3a referenced 1 time by &9af3
.c9b3a
    jsr get_access_bits                                               ; 9b3a: 20 55 92     U.
    sta l0f06                                                         ; 9b3d: 8d 06 0f    ...
    ldx #2                                                            ; 9b40: a2 02       ..
    bne c9b23                                                         ; 9b42: d0 df       ..             ; ALWAYS branch

; &9b44 referenced 1 time by &9aef
.c9b44
    ldx #1                                                            ; 9b44: a2 01       ..
    jsr copy_arg_to_buf                                               ; 9b46: 20 f2 ae     ..
    ldy #&12                                                          ; 9b49: a0 12       ..
    jsr save_net_tx_cb                                                ; 9b4b: 20 99 94     ..
    lda l0f11                                                         ; 9b4e: ad 11 0f    ...
    stx l0f11                                                         ; 9b51: 8e 11 0f    ...
    stx l0f14                                                         ; 9b54: 8e 14 0f    ...
    jsr get_prot_bits                                                 ; 9b57: 20 5f 92     _.
    ldx l0f05                                                         ; 9b5a: ae 05 0f    ...
    beq c9b7f                                                         ; 9b5d: f0 20       .
    ldy #&0e                                                          ; 9b5f: a0 0e       ..
    sta (fs_options),y                                                ; 9b61: 91 bb       ..
    dey                                                               ; 9b63: 88          .              ; Y=&0d
    ldx #&0c                                                          ; 9b64: a2 0c       ..
; &9b66 referenced 1 time by &9b6d
.loop_c9b66
    lda l0f05,x                                                       ; 9b66: bd 05 0f    ...
    sta (fs_options),y                                                ; 9b69: 91 bb       ..
    dey                                                               ; 9b6b: 88          .
    dex                                                               ; 9b6c: ca          .
    bne loop_c9b66                                                    ; 9b6d: d0 f7       ..
    inx                                                               ; 9b6f: e8          .
    inx                                                               ; 9b70: e8          .
    ldy #&11                                                          ; 9b71: a0 11       ..
; &9b73 referenced 1 time by &9b7a
.loop_c9b73
    lda l0f12,x                                                       ; 9b73: bd 12 0f    ...
    sta (fs_options),y                                                ; 9b76: 91 bb       ..
    dey                                                               ; 9b78: 88          .
    dex                                                               ; 9b79: ca          .
    bpl loop_c9b73                                                    ; 9b7a: 10 f7       ..
    ldx l0f05                                                         ; 9b7c: ae 05 0f    ...
; &9b7f referenced 1 time by &9b5d
.c9b7f
    txa                                                               ; 9b7f: 8a          .
; &9b80 referenced 1 time by &9b35
.c9b80
    jmp finalise_and_return                                           ; 9b80: 4c bb 9c    L..

    equb &4c, &bb, &9c                                                ; 9b83: 4c bb 9c    L..

; &9b86 referenced 2 times by &9970, &99fb
.format_filename_field
    ldy #0                                                            ; 9b86: a0 00       ..
    ldx l0f03                                                         ; 9b88: ae 03 0f    ...
    bne c9ba6                                                         ; 9b8b: d0 19       ..
; &9b8d referenced 1 time by &9b97
.loop_c9b8d
    lda (fs_crc_lo),y                                                 ; 9b8d: b1 be       ..
    cmp #&21 ; '!'                                                    ; 9b8f: c9 21       .!
    bcc c9b99                                                         ; 9b91: 90 06       ..
    sta l10f3,y                                                       ; 9b93: 99 f3 10    ...
    iny                                                               ; 9b96: c8          .
    bne loop_c9b8d                                                    ; 9b97: d0 f4       ..
; &9b99 referenced 2 times by &9b91, &9ba1
.c9b99
    lda #&20 ; ' '                                                    ; 9b99: a9 20       .
    sta l10f3,y                                                       ; 9b9b: 99 f3 10    ...
    iny                                                               ; 9b9e: c8          .
    cpy #&0c                                                          ; 9b9f: c0 0c       ..
    bcc c9b99                                                         ; 9ba1: 90 f6       ..
    rts                                                               ; 9ba3: 60          `

; &9ba4 referenced 1 time by &9bac
.loop_c9ba4
    inx                                                               ; 9ba4: e8          .
    iny                                                               ; 9ba5: c8          .
; &9ba6 referenced 1 time by &9b8b
.c9ba6
    lda l0f05,x                                                       ; 9ba6: bd 05 0f    ...
    sta l10f3,y                                                       ; 9ba9: 99 f3 10    ...
    bpl loop_c9ba4                                                    ; 9bac: 10 f6       ..
    rts                                                               ; 9bae: 60          `

    jsr verify_ws_checksum                                            ; 9baf: 20 b2 8f     ..
    sta fs_last_byte_flag                                             ; 9bb2: 85 bd       ..
    jsr set_options_ptr                                               ; 9bb4: 20 87 92     ..
    ora #0                                                            ; 9bb7: 09 00       ..
    bpl c9be9                                                         ; 9bb9: 10 2e       ..
    asl a                                                             ; 9bbb: 0a          .
    beq c9bc1                                                         ; 9bbc: f0 03       ..
    jmp c9cb6                                                         ; 9bbe: 4c b6 9c    L..

; &9bc1 referenced 1 time by &9bbc
.c9bc1
    tya                                                               ; 9bc1: 98          .
    cmp #&20 ; ' '                                                    ; 9bc2: c9 20       .
    bcs c9bc9                                                         ; 9bc4: b0 03       ..
; &9bc6 referenced 1 time by &9bcb
.loop_c9bc6
    jmp err_net_chan_invalid                                          ; 9bc6: 4c 72 b4    Lr.

; &9bc9 referenced 1 time by &9bc4
.c9bc9
    cmp #&30 ; '0'                                                    ; 9bc9: c9 30       .0
    bcs loop_c9bc6                                                    ; 9bcb: b0 f9       ..
    jsr process_all_fcbs                                              ; 9bcd: 20 9f b7     ..
    tya                                                               ; 9bd0: 98          .
    pha                                                               ; 9bd1: 48          H
    tax                                                               ; 9bd2: aa          .
    ldy #0                                                            ; 9bd3: a0 00       ..
    sty fs_last_byte_flag                                             ; 9bd5: 84 bd       ..
    sty fs_block_offset                                               ; 9bd7: 84 bc       ..
; &9bd9 referenced 1 time by &9be4
.loop_c9bd9
    lda l1010,x                                                       ; 9bd9: bd 10 10    ...
    sta (fs_options),y                                                ; 9bdc: 91 bb       ..
    jsr advance_x_by_8                                                ; 9bde: 20 84 bc     ..
    iny                                                               ; 9be1: c8          .
    cpy #4                                                            ; 9be2: c0 04       ..
    bne loop_c9bd9                                                    ; 9be4: d0 f3       ..
    pla                                                               ; 9be6: 68          h
    sta fs_block_offset                                               ; 9be7: 85 bc       ..
; &9be9 referenced 1 time by &9bb9
.c9be9
    cmp #5                                                            ; 9be9: c9 05       ..
    bcs c9c3d                                                         ; 9beb: b0 50       .P
    cpy #0                                                            ; 9bed: c0 00       ..
    bne c9bf4                                                         ; 9bef: d0 03       ..
    jmp c9cc8                                                         ; 9bf1: 4c c8 9c    L..

; &9bf4 referenced 1 time by &9bef
.c9bf4
    pha                                                               ; 9bf4: 48          H
    txa                                                               ; 9bf5: 8a          .
    pha                                                               ; 9bf6: 48          H
    tya                                                               ; 9bf7: 98          .
    pha                                                               ; 9bf8: 48          H
    jsr check_not_dir                                                 ; 9bf9: 20 e3 b4     ..
    pla                                                               ; 9bfc: 68          h
    ldy #&0e                                                          ; 9bfd: a0 0e       ..
    sta (net_rx_ptr),y                                                ; 9bff: 91 9c       ..
    lda l1030,x                                                       ; 9c01: bd 30 10    .0.
    sta l0f05                                                         ; 9c04: 8d 05 0f    ...
    pla                                                               ; 9c07: 68          h
    tax                                                               ; 9c08: aa          .
    pla                                                               ; 9c09: 68          h
    lsr a                                                             ; 9c0a: 4a          J
    beq c9c5c                                                         ; 9c0b: f0 4f       .O
    php                                                               ; 9c0d: 08          .
    pha                                                               ; 9c0e: 48          H
    ldx fs_options                                                    ; 9c0f: a6 bb       ..
    ldy fs_block_offset                                               ; 9c11: a4 bc       ..
    jsr process_all_fcbs                                              ; 9c13: 20 9f b7     ..
    lda l1010,y                                                       ; 9c16: b9 10 10    ...
    sta l0f05                                                         ; 9c19: 8d 05 0f    ...
    pla                                                               ; 9c1c: 68          h
    sta l0f06                                                         ; 9c1d: 8d 06 0f    ...
    plp                                                               ; 9c20: 28          (
    tya                                                               ; 9c21: 98          .
    pha                                                               ; 9c22: 48          H
    bcc c9c40                                                         ; 9c23: 90 1b       ..
    ldy #3                                                            ; 9c25: a0 03       ..
; &9c27 referenced 1 time by &9c2e
.loop_c9c27
    lda zp_work_3,x                                                   ; 9c27: b5 03       ..
    sta l0f07,y                                                       ; 9c29: 99 07 0f    ...
    dex                                                               ; 9c2c: ca          .
    dey                                                               ; 9c2d: 88          .
    bpl loop_c9c27                                                    ; 9c2e: 10 f7       ..
    ldy #&0d                                                          ; 9c30: a0 0d       ..
    ldx #5                                                            ; 9c32: a2 05       ..
    jsr save_net_tx_cb                                                ; 9c34: 20 99 94     ..
    stx fs_last_byte_flag                                             ; 9c37: 86 bd       ..
    pla                                                               ; 9c39: 68          h
    jsr set_conn_active                                               ; 9c3a: 20 a1 92     ..
; &9c3d referenced 1 time by &9beb
.c9c3d
    jmp return_with_last_flag                                         ; 9c3d: 4c b9 9c    L..

; &9c40 referenced 1 time by &9c23
.c9c40
    ldy #&0c                                                          ; 9c40: a0 0c       ..
    ldx #2                                                            ; 9c42: a2 02       ..
    jsr save_net_tx_cb                                                ; 9c44: 20 99 94     ..
    sta fs_last_byte_flag                                             ; 9c47: 85 bd       ..
    ldx fs_options                                                    ; 9c49: a6 bb       ..
    ldy #2                                                            ; 9c4b: a0 02       ..
    sta zp_work_3,x                                                   ; 9c4d: 95 03       ..
; &9c4f referenced 1 time by &9c56
.loop_c9c4f
    lda l0f05,y                                                       ; 9c4f: b9 05 0f    ...
    sta zp_work_2,x                                                   ; 9c52: 95 02       ..
    dex                                                               ; 9c54: ca          .
    dey                                                               ; 9c55: 88          .
    bpl loop_c9c4f                                                    ; 9c56: 10 f7       ..
    pla                                                               ; 9c58: 68          h
    jmp return_with_last_flag                                         ; 9c59: 4c b9 9c    L..

; &9c5c referenced 1 time by &9c0b
.c9c5c
    bcs c9c7e                                                         ; 9c5c: b0 20       .
    lda fs_block_offset                                               ; 9c5e: a5 bc       ..
    jsr attr_to_chan_index                                            ; 9c60: 20 5b b4     [.
    ldy fs_options                                                    ; 9c63: a4 bb       ..
    lda l1000,x                                                       ; 9c65: bd 00 10    ...
    sta zp_ptr_lo,y                                                   ; 9c68: 99 00 00    ...
    lda l1010,x                                                       ; 9c6b: bd 10 10    ...
    sta zp_ptr_hi,y                                                   ; 9c6e: 99 01 00    ...
    lda l1020,x                                                       ; 9c71: bd 20 10    . .
    sta zp_work_2,y                                                   ; 9c74: 99 02 00    ...
    lda #0                                                            ; 9c77: a9 00       ..
    sta zp_work_3,y                                                   ; 9c79: 99 03 00    ...
    beq return_with_last_flag                                         ; 9c7c: f0 3b       .;             ; ALWAYS branch

; &9c7e referenced 1 time by &9c5c
.c9c7e
    sta l0f06                                                         ; 9c7e: 8d 06 0f    ...
    txa                                                               ; 9c81: 8a          .
    pha                                                               ; 9c82: 48          H
    ldy #3                                                            ; 9c83: a0 03       ..
; &9c85 referenced 1 time by &9c8c
.loop_c9c85
    lda zp_work_3,x                                                   ; 9c85: b5 03       ..
    sta l0f07,y                                                       ; 9c87: 99 07 0f    ...
    dex                                                               ; 9c8a: ca          .
    dey                                                               ; 9c8b: 88          .
    bpl loop_c9c85                                                    ; 9c8c: 10 f7       ..
    ldy #&0d                                                          ; 9c8e: a0 0d       ..
    ldx #5                                                            ; 9c90: a2 05       ..
    jsr save_net_tx_cb                                                ; 9c92: 20 99 94     ..
    stx fs_last_byte_flag                                             ; 9c95: 86 bd       ..
    pla                                                               ; 9c97: 68          h
    tay                                                               ; 9c98: a8          .
    lda fs_block_offset                                               ; 9c99: a5 bc       ..
    jsr clear_conn_active                                             ; 9c9b: 20 b8 92     ..
    jsr attr_to_chan_index                                            ; 9c9e: 20 5b b4     [.
    lda zp_ptr_lo,y                                                   ; 9ca1: b9 00 00    ...
    sta l1000,x                                                       ; 9ca4: 9d 00 10    ...
    lda zp_ptr_hi,y                                                   ; 9ca7: b9 01 00    ...
    sta l1010,x                                                       ; 9caa: 9d 10 10    ...
    lda zp_work_2,y                                                   ; 9cad: b9 02 00    ...
    sta l1020,x                                                       ; 9cb0: 9d 20 10    . .
    jmp return_with_last_flag                                         ; 9cb3: 4c b9 9c    L..

; &9cb6 referenced 1 time by &9bbe
.c9cb6
    jsr process_all_fcbs                                              ; 9cb6: 20 9f b7     ..
; &9cb9 referenced 12 times by &9935, &9a42, &9b37, &9c3d, &9c59, &9c7c, &9cb3, &9daf, &9e36, &a2df, &a2e5, &a399
.return_with_last_flag
    lda fs_last_byte_flag                                             ; 9cb9: a5 bd       ..
; &9cbb referenced 6 times by &9b80, &9cd1, &9ce4, &9d7b, &9ebd, &a1ee
.finalise_and_return
    pha                                                               ; 9cbb: 48          H
    lda #0                                                            ; 9cbc: a9 00       ..
    ldy #&0e                                                          ; 9cbe: a0 0e       ..
    sta (net_rx_ptr),y                                                ; 9cc0: 91 9c       ..
    pla                                                               ; 9cc2: 68          h
    ldx fs_options                                                    ; 9cc3: a6 bb       ..
    ldy fs_block_offset                                               ; 9cc5: a4 bc       ..
    rts                                                               ; 9cc7: 60          `

; &9cc8 referenced 1 time by &9bf1
.c9cc8
    cmp #2                                                            ; 9cc8: c9 02       ..
    bcs c9cdf                                                         ; 9cca: b0 13       ..
    tay                                                               ; 9ccc: a8          .
    bne c9cd3                                                         ; 9ccd: d0 04       ..
    lda #5                                                            ; 9ccf: a9 05       ..
    bne finalise_and_return                                           ; 9cd1: d0 e8       ..             ; ALWAYS branch

; &9cd3 referenced 2 times by &9ccd, &9cd9
.c9cd3
    lda l0e0a,y                                                       ; 9cd3: b9 0a 0e    ...
    sta (fs_options),y                                                ; 9cd6: 91 bb       ..
    dey                                                               ; 9cd8: 88          .
    bpl c9cd3                                                         ; 9cd9: 10 f8       ..
    sty zp_work_2,x                                                   ; 9cdb: 94 02       ..
    sty zp_work_3,x                                                   ; 9cdd: 94 03       ..
; &9cdf referenced 1 time by &9cca
.c9cdf
    beq c9ce3                                                         ; 9cdf: f0 02       ..
; &9ce1 referenced 2 times by &9ce8, &9ff4
.c9ce1
    lda #0                                                            ; 9ce1: a9 00       ..
; &9ce3 referenced 1 time by &9cdf
.c9ce3
    lsr a                                                             ; 9ce3: 4a          J
    bpl finalise_and_return                                           ; 9ce4: 10 d5       ..
; &9ce6 referenced 1 time by &9d55
.c9ce6
    and #&3f ; '?'                                                    ; 9ce6: 29 3f       )?
    bne c9ce1                                                         ; 9ce8: d0 f7       ..
    txa                                                               ; 9cea: 8a          .
    jsr alloc_fcb_or_error                                            ; 9ceb: 20 2e b5     ..
    eor #&80                                                          ; 9cee: 49 80       I.
    asl a                                                             ; 9cf0: 0a          .
    sta l0f05                                                         ; 9cf1: 8d 05 0f    ...
    rol a                                                             ; 9cf4: 2a          *
    sta l0f06                                                         ; 9cf5: 8d 06 0f    ...
    jsr parse_cmd_arg_y0                                              ; 9cf8: 20 80 ae     ..
    ldx #2                                                            ; 9cfb: a2 02       ..
    jsr copy_arg_to_buf                                               ; 9cfd: 20 f2 ae     ..
    ldy #6                                                            ; 9d00: a0 06       ..
    bit bit_test_ff_pad                                               ; 9d02: 2c 7d 94    ,}.
    sec                                                               ; 9d05: 38          8
    ror escapable                                                     ; 9d06: 66 97       f.
    jsr save_net_tx_cb_vset                                           ; 9d08: 20 9a 94     ..
    bcs c9d7b                                                         ; 9d0b: b0 6e       .n
    lda #&ff                                                          ; 9d0d: a9 ff       ..
    ldy #&0e                                                          ; 9d0f: a0 0e       ..
    sta (net_rx_ptr),y                                                ; 9d11: 91 9c       ..
    lda l0f05                                                         ; 9d13: ad 05 0f    ...
    pha                                                               ; 9d16: 48          H
    lda #4                                                            ; 9d17: a9 04       ..
    sta l0f05                                                         ; 9d19: 8d 05 0f    ...
    ldx #1                                                            ; 9d1c: a2 01       ..
; &9d1e referenced 1 time by &9d27
.loop_c9d1e
    lda l0f06,x                                                       ; 9d1e: bd 06 0f    ...
    sta l0f05,x                                                       ; 9d21: 9d 05 0f    ...
    inx                                                               ; 9d24: e8          .
    cmp #&0d                                                          ; 9d25: c9 0d       ..
    bne loop_c9d1e                                                    ; 9d27: d0 f5       ..
    ldy #&12                                                          ; 9d29: a0 12       ..
    jsr save_net_tx_cb                                                ; 9d2b: 20 99 94     ..
    lda fs_last_byte_flag                                             ; 9d2e: a5 bd       ..
    and #&bf                                                          ; 9d30: 29 bf       ).
    ora l0f05                                                         ; 9d32: 0d 05 0f    ...
    ora #1                                                            ; 9d35: 09 01       ..
    tay                                                               ; 9d37: a8          .
    and #2                                                            ; 9d38: 29 02       ).
    beq c9d5f                                                         ; 9d3a: f0 23       .#
    pla                                                               ; 9d3c: 68          h
    jsr alloc_fcb_slot                                                ; 9d3d: 20 fa b4     ..
    bne c9d75                                                         ; 9d40: d0 33       .3
    jsr verify_ws_checksum                                            ; 9d42: 20 b2 8f     ..
    jsr set_xfer_params                                               ; 9d45: 20 81 92     ..
    tax                                                               ; 9d48: aa          .
    jsr mask_owner_access                                             ; 9d49: 20 12 af     ..
    txa                                                               ; 9d4c: 8a          .
    beq c9d7e                                                         ; 9d4d: f0 2f       ./
    jsr save_ptr_to_os_text                                           ; 9d4f: 20 95 af     ..
    ldy l1070                                                         ; 9d52: ac 70 10    .p.
    beq c9ce6                                                         ; 9d55: f0 8f       ..
    tya                                                               ; 9d57: 98          .
    ldx #0                                                            ; 9d58: a2 00       ..
    stx l1070                                                         ; 9d5a: 8e 70 10    .p.
    beq c9d7b                                                         ; 9d5d: f0 1c       ..             ; ALWAYS branch

; &9d5f referenced 1 time by &9d3a
.c9d5f
    lda l0f06                                                         ; 9d5f: ad 06 0f    ...
    ror a                                                             ; 9d62: 6a          j
    bcs c9d71                                                         ; 9d63: b0 0c       ..
    ror a                                                             ; 9d65: 6a          j
    bcc c9d71                                                         ; 9d66: 90 09       ..
    bit l0f07                                                         ; 9d68: 2c 07 0f    ,..
    bpl c9d71                                                         ; 9d6b: 10 04       ..
    tya                                                               ; 9d6d: 98          .
    ora #&20 ; ' '                                                    ; 9d6e: 09 20       .
    tay                                                               ; 9d70: a8          .
; &9d71 referenced 3 times by &9d63, &9d66, &9d6b
.c9d71
    pla                                                               ; 9d71: 68          h
    jsr alloc_fcb_slot                                                ; 9d72: 20 fa b4     ..
; &9d75 referenced 1 time by &9d40
.c9d75
    tax                                                               ; 9d75: aa          .
    tya                                                               ; 9d76: 98          .
    sta l1040,x                                                       ; 9d77: 9d 40 10    .@.
    txa                                                               ; 9d7a: 8a          .
; &9d7b referenced 2 times by &9d0b, &9d5d
.c9d7b
    jmp finalise_and_return                                           ; 9d7b: 4c bb 9c    L..

; &9d7e referenced 1 time by &9d4d
.c9d7e
    jsr process_all_fcbs                                              ; 9d7e: 20 9f b7     ..
    tya                                                               ; 9d81: 98          .
    bne c9d97                                                         ; 9d82: d0 13       ..
    lda fs_options                                                    ; 9d84: a5 bb       ..
    pha                                                               ; 9d86: 48          H
    lda #osbyte_close_spool_exec                                      ; 9d87: a9 77       .w
    jsr osbyte                                                        ; 9d89: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    pla                                                               ; 9d8c: 68          h
    sta fs_options                                                    ; 9d8d: 85 bb       ..
    lda #0                                                            ; 9d8f: a9 00       ..
    sta fs_last_byte_flag                                             ; 9d91: 85 bd       ..
    sta fs_block_offset                                               ; 9d93: 85 bc       ..
    beq c9d9d                                                         ; 9d95: f0 06       ..             ; ALWAYS branch

; &9d97 referenced 1 time by &9d82
.c9d97
    jsr check_chan_char                                               ; 9d97: 20 6a b4     j.
    lda l1030,x                                                       ; 9d9a: bd 30 10    .0.
; &9d9d referenced 1 time by &9d95
.c9d9d
    sta l0f05                                                         ; 9d9d: 8d 05 0f    ...
    ldx #1                                                            ; 9da0: a2 01       ..
    ldy #7                                                            ; 9da2: a0 07       ..
    jsr save_net_tx_cb                                                ; 9da4: 20 99 94     ..
    ldy fs_block_offset                                               ; 9da7: a4 bc       ..
    bne c9db2                                                         ; 9da9: d0 07       ..
    clv                                                               ; 9dab: b8          .
    jsr scan_fcb_flags                                                ; 9dac: 20 51 b5     Q.
; &9daf referenced 3 times by &9dba, &9dcc, &9de0
.c9daf
    jmp return_with_last_flag                                         ; 9daf: 4c b9 9c    L..

; &9db2 referenced 1 time by &9da9
.c9db2
    lda #0                                                            ; 9db2: a9 00       ..
    sta l1010,y                                                       ; 9db4: 99 10 10    ...
    sta l1040,y                                                       ; 9db7: 99 40 10    .@.
    beq c9daf                                                         ; 9dba: f0 f3       ..             ; ALWAYS branch

    beq c9dc9                                                         ; 9dbc: f0 0b       ..
    cpx #4                                                            ; 9dbe: e0 04       ..
    bne c9dc6                                                         ; 9dc0: d0 04       ..
    cpy #4                                                            ; 9dc2: c0 04       ..
    bcc c9dd3                                                         ; 9dc4: 90 0d       ..
; &9dc6 referenced 1 time by &9dc0
.c9dc6
    dex                                                               ; 9dc6: ca          .
    bne c9dce                                                         ; 9dc7: d0 05       ..
; &9dc9 referenced 1 time by &9dbc
.c9dc9
    sty l0e06                                                         ; 9dc9: 8c 06 0e    ...
    bcc c9daf                                                         ; 9dcc: 90 e1       ..
; &9dce referenced 1 time by &9dc7
.c9dce
    lda #7                                                            ; 9dce: a9 07       ..
    jmp classify_reply_error                                          ; 9dd0: 4c 38 96    L8.

; &9dd3 referenced 1 time by &9dc4
.c9dd3
    sty l0f05                                                         ; 9dd3: 8c 05 0f    ...
    ldy #&16                                                          ; 9dd6: a0 16       ..
    jsr save_net_tx_cb                                                ; 9dd8: 20 99 94     ..
    ldy fs_block_offset                                               ; 9ddb: a4 bc       ..
    sty l0e05                                                         ; 9ddd: 8c 05 0e    ...
    bpl c9daf                                                         ; 9de0: 10 cd       ..
    jsr verify_ws_checksum                                            ; 9de2: 20 b2 8f     ..
    pha                                                               ; 9de5: 48          H
    lda fs_block_offset                                               ; 9de6: a5 bc       ..
    pha                                                               ; 9de8: 48          H
    stx l10c9                                                         ; 9de9: 8e c9 10    ...
    jsr find_matching_fcb                                             ; 9dec: 20 38 b7     8.
    beq c9dfd                                                         ; 9def: f0 0c       ..
    lda l1000,y                                                       ; 9df1: b9 00 10    ...
    cmp l1098,x                                                       ; 9df4: dd 98 10    ...
    bcc c9dfd                                                         ; 9df7: 90 04       ..
    ldx #&ff                                                          ; 9df9: a2 ff       ..
    bmi c9dff                                                         ; 9dfb: 30 02       0.             ; ALWAYS branch

; &9dfd referenced 2 times by &9def, &9df7
.c9dfd
    ldx #0                                                            ; 9dfd: a2 00       ..
; &9dff referenced 1 time by &9dfb
.c9dff
    pla                                                               ; 9dff: 68          h
    tay                                                               ; 9e00: a8          .
    pla                                                               ; 9e01: 68          h
    rts                                                               ; 9e02: 60          `

; &9e03 referenced 1 time by &9f48
.update_addr_from_offset9
    ldy #9                                                            ; 9e03: a0 09       ..
    jsr add_workspace_to_fsopts                                       ; 9e05: 20 0a 9e     ..
; &9e08 referenced 1 time by &a03b
.update_addr_from_offset1
    ldy #1                                                            ; 9e08: a0 01       ..
; &9e0a referenced 1 time by &9e05
.add_workspace_to_fsopts
    clc                                                               ; 9e0a: 18          .
; &9e0b referenced 2 times by &9f4e, &a047
.adjust_fsopts_4bytes
    ldx #&fc                                                          ; 9e0b: a2 fc       ..
; &9e0d referenced 1 time by &9e20
.loop_c9e0d
    lda (fs_options),y                                                ; 9e0d: b1 bb       ..
    bit fs_load_addr_2                                                ; 9e0f: 24 b2       $.
    bmi c9e19                                                         ; 9e11: 30 06       0.
    adc l0e0a,x                                                       ; 9e13: 7d 0a 0e    }..
    jmp c9e1c                                                         ; 9e16: 4c 1c 9e    L..

; &9e19 referenced 1 time by &9e11
.c9e19
    sbc l0e0a,x                                                       ; 9e19: fd 0a 0e    ...
; &9e1c referenced 1 time by &9e16
.c9e1c
    sta (fs_options),y                                                ; 9e1c: 91 bb       ..
    iny                                                               ; 9e1e: c8          .
    inx                                                               ; 9e1f: e8          .
    bne loop_c9e0d                                                    ; 9e20: d0 eb       ..
    rts                                                               ; 9e22: 60          `

    jsr verify_ws_checksum                                            ; 9e23: 20 b2 8f     ..
    jsr set_xfer_params                                               ; 9e26: 20 81 92     ..
    pha                                                               ; 9e29: 48          H
    jsr mask_owner_access                                             ; 9e2a: 20 12 af     ..
    pla                                                               ; 9e2d: 68          h
    tax                                                               ; 9e2e: aa          .
    beq c9e36                                                         ; 9e2f: f0 05       ..
    dex                                                               ; 9e31: ca          .
    cpx #8                                                            ; 9e32: e0 08       ..
    bcc c9e39                                                         ; 9e34: 90 03       ..
; &9e36 referenced 1 time by &9e2f
.c9e36
    jmp return_with_last_flag                                         ; 9e36: 4c b9 9c    L..

; &9e39 referenced 1 time by &9e34
.c9e39
    txa                                                               ; 9e39: 8a          .
    ldy #0                                                            ; 9e3a: a0 00       ..
    pha                                                               ; 9e3c: 48          H
    cmp #4                                                            ; 9e3d: c9 04       ..
    bcc c9e44                                                         ; 9e3f: 90 03       ..
    jmp c9f6a                                                         ; 9e41: 4c 6a 9f    Lj.

; &9e44 referenced 1 time by &9e3f
.c9e44
    lda (fs_options),y                                                ; 9e44: b1 bb       ..
    pha                                                               ; 9e46: 48          H
    jsr check_not_dir                                                 ; 9e47: 20 e3 b4     ..
    pla                                                               ; 9e4a: 68          h
    tay                                                               ; 9e4b: a8          .
    jsr process_all_fcbs                                              ; 9e4c: 20 9f b7     ..
    lda l1030,x                                                       ; 9e4f: bd 30 10    .0.
    sta l0f05                                                         ; 9e52: 8d 05 0f    ...
    lda #0                                                            ; 9e55: a9 00       ..
    sta l0f06                                                         ; 9e57: 8d 06 0f    ...
    lda l1000,x                                                       ; 9e5a: bd 00 10    ...
    sta l0f07                                                         ; 9e5d: 8d 07 0f    ...
    lda l1010,x                                                       ; 9e60: bd 10 10    ...
    sta l0f08                                                         ; 9e63: 8d 08 0f    ...
    lda l1020,x                                                       ; 9e66: bd 20 10    . .
    sta l0f09                                                         ; 9e69: 8d 09 0f    ...
    ldy #&0d                                                          ; 9e6c: a0 0d       ..
    ldx #5                                                            ; 9e6e: a2 05       ..
    jsr save_net_tx_cb                                                ; 9e70: 20 99 94     ..
    pla                                                               ; 9e73: 68          h
    jsr setup_transfer_workspace                                      ; 9e74: 20 cb 9e     ..
    php                                                               ; 9e77: 08          .
    ldy #0                                                            ; 9e78: a0 00       ..
    lda (fs_options),y                                                ; 9e7a: b1 bb       ..
    bcs c9e83                                                         ; 9e7c: b0 05       ..
    jsr clear_conn_active                                             ; 9e7e: 20 b8 92     ..
    bpl c9e86                                                         ; 9e81: 10 03       ..
; &9e83 referenced 1 time by &9e7c
.c9e83
    jsr set_conn_active                                               ; 9e83: 20 a1 92     ..
; &9e86 referenced 1 time by &9e81
.c9e86
    sty l0f06                                                         ; 9e86: 8c 06 0f    ...
    jsr lookup_cat_slot_data                                          ; 9e89: 20 c4 9e     ..
    sta l0f05                                                         ; 9e8c: 8d 05 0f    ...
    ldy #&0c                                                          ; 9e8f: a0 0c       ..
    ldx #2                                                            ; 9e91: a2 02       ..
    jsr save_net_tx_cb                                                ; 9e93: 20 99 94     ..
    jsr lookup_cat_entry_0                                            ; 9e96: 20 c0 9e     ..
    ldy #9                                                            ; 9e99: a0 09       ..
    lda l0f05                                                         ; 9e9b: ad 05 0f    ...
    sta l1000,x                                                       ; 9e9e: 9d 00 10    ...
    sta (fs_options),y                                                ; 9ea1: 91 bb       ..
    iny                                                               ; 9ea3: c8          .              ; Y=&0a
    lda l0f06                                                         ; 9ea4: ad 06 0f    ...
    sta l1010,x                                                       ; 9ea7: 9d 10 10    ...
    sta (fs_options),y                                                ; 9eaa: 91 bb       ..
    iny                                                               ; 9eac: c8          .              ; Y=&0b
    lda l0f07                                                         ; 9ead: ad 07 0f    ...
    sta l1020,x                                                       ; 9eb0: 9d 20 10    . .
    sta (fs_options),y                                                ; 9eb3: 91 bb       ..
    lda #0                                                            ; 9eb5: a9 00       ..
    iny                                                               ; 9eb7: c8          .              ; Y=&0c
    sta (fs_options),y                                                ; 9eb8: 91 bb       ..
    plp                                                               ; 9eba: 28          (
    lda #0                                                            ; 9ebb: a9 00       ..
    jmp finalise_and_return                                           ; 9ebd: 4c bb 9c    L..

; &9ec0 referenced 2 times by &9e96, &9ecc
.lookup_cat_entry_0
    ldy #0                                                            ; 9ec0: a0 00       ..
    lda (fs_options),y                                                ; 9ec2: b1 bb       ..
; &9ec4 referenced 1 time by &9e89
.lookup_cat_slot_data
    jsr lookup_chan_by_char                                           ; 9ec4: 20 9d b4     ..
    lda l1030,x                                                       ; 9ec7: bd 30 10    .0.
    rts                                                               ; 9eca: 60          `

; &9ecb referenced 2 times by &9e74, &b97c
.setup_transfer_workspace
    pha                                                               ; 9ecb: 48          H
    jsr lookup_cat_entry_0                                            ; 9ecc: 20 c0 9e     ..
    sta l0f05                                                         ; 9ecf: 8d 05 0f    ...
    ldy #&0b                                                          ; 9ed2: a0 0b       ..
    ldx #6                                                            ; 9ed4: a2 06       ..
; &9ed6 referenced 1 time by &9ee2
.loop_c9ed6
    lda (fs_options),y                                                ; 9ed6: b1 bb       ..
    sta l0f06,x                                                       ; 9ed8: 9d 06 0f    ...
    dey                                                               ; 9edb: 88          .
    cpy #8                                                            ; 9edc: c0 08       ..
    bne c9ee1                                                         ; 9ede: d0 01       ..
    dey                                                               ; 9ee0: 88          .
; &9ee1 referenced 1 time by &9ede
.c9ee1
    dex                                                               ; 9ee1: ca          .
    bne loop_c9ed6                                                    ; 9ee2: d0 f2       ..
    pla                                                               ; 9ee4: 68          h
    lsr a                                                             ; 9ee5: 4a          J
    pha                                                               ; 9ee6: 48          H
    bcc c9eea                                                         ; 9ee7: 90 01       ..
    inx                                                               ; 9ee9: e8          .
; &9eea referenced 1 time by &9ee7
.c9eea
    stx l0f06                                                         ; 9eea: 8e 06 0f    ...
    ldy #&0b                                                          ; 9eed: a0 0b       ..
    ldx #&91                                                          ; 9eef: a2 91       ..
    pla                                                               ; 9ef1: 68          h
    pha                                                               ; 9ef2: 48          H
    beq c9ef8                                                         ; 9ef3: f0 03       ..
    ldx #&92                                                          ; 9ef5: a2 92       ..
    dey                                                               ; 9ef7: 88          .              ; Y=&0a
; &9ef8 referenced 1 time by &9ef3
.c9ef8
    stx l0f02                                                         ; 9ef8: 8e 02 0f    ...
    stx fs_error_ptr                                                  ; 9efb: 86 b8       ..
    ldx #8                                                            ; 9efd: a2 08       ..
    lda l0f05                                                         ; 9eff: ad 05 0f    ...
    jsr send_request_nowrite                                          ; 9f02: 20 83 94     ..
    ldx #0                                                            ; 9f05: a2 00       ..
    lda (fs_options,x)                                                ; 9f07: a1 bb       ..
    tax                                                               ; 9f09: aa          .
    lda l1040,x                                                       ; 9f0a: bd 40 10    .@.
    eor #1                                                            ; 9f0d: 49 01       I.
    sta l1040,x                                                       ; 9f0f: 9d 40 10    .@.
    clc                                                               ; 9f12: 18          .
    ldx #4                                                            ; 9f13: a2 04       ..
; &9f15 referenced 1 time by &9f29
.loop_c9f15
    lda (fs_options),y                                                ; 9f15: b1 bb       ..
    sta l00af,y                                                       ; 9f17: 99 af 00    ...
    sta txcb_pos,y                                                    ; 9f1a: 99 c7 00    ...
    jsr advance_y_by_4                                                ; 9f1d: 20 6d 9a     m.
    adc (fs_options),y                                                ; 9f20: 71 bb       q.
    sta l00af,y                                                       ; 9f22: 99 af 00    ...
    jsr retreat_y_by_3                                                ; 9f25: 20 80 9a     ..
    dex                                                               ; 9f28: ca          .
    bne loop_c9f15                                                    ; 9f29: d0 ea       ..
    inx                                                               ; 9f2b: e8          .
; &9f2c referenced 1 time by &9f33
.loop_c9f2c
    lda l0f03,x                                                       ; 9f2c: bd 03 0f    ...
    sta l0f06,x                                                       ; 9f2f: 9d 06 0f    ...
    dex                                                               ; 9f32: ca          .
    bpl loop_c9f2c                                                    ; 9f33: 10 f7       ..
    pla                                                               ; 9f35: 68          h
    bne c9f40                                                         ; 9f36: d0 08       ..
    lda l0f02                                                         ; 9f38: ad 02 0f    ...
    jsr check_and_setup_txcb                                          ; 9f3b: 20 88 9a     ..
    bcs c9f43                                                         ; 9f3e: b0 03       ..
; &9f40 referenced 1 time by &9f36
.c9f40
    jsr send_txcb_swap_addrs                                          ; 9f40: 20 84 99     ..
; &9f43 referenced 1 time by &9f3e
.c9f43
    jsr recv_and_process_reply                                        ; 9f43: 20 dc 94     ..
    stx fs_load_addr_2                                                ; 9f46: 86 b2       ..
    jsr update_addr_from_offset9                                      ; 9f48: 20 03 9e     ..
    dec fs_load_addr_2                                                ; 9f4b: c6 b2       ..
    sec                                                               ; 9f4d: 38          8
    jsr adjust_fsopts_4bytes                                          ; 9f4e: 20 0b 9e     ..
    asl l0f05                                                         ; 9f51: 0e 05 0f    ...
    rts                                                               ; 9f54: 60          `

; &9f55 referenced 1 time by &9f85
.c9f55
    ldy #&15                                                          ; 9f55: a0 15       ..
    jsr save_net_tx_cb                                                ; 9f57: 20 99 94     ..
    lda l0e05                                                         ; 9f5a: ad 05 0e    ...
    sta l0f16                                                         ; 9f5d: 8d 16 0f    ...
    stx fs_load_addr                                                  ; 9f60: 86 b0       ..
    stx fs_load_addr_hi                                               ; 9f62: 86 b1       ..
    lda #&12                                                          ; 9f64: a9 12       ..
    sta fs_load_addr_2                                                ; 9f66: 85 b2       ..
    bne write_data_block                                              ; 9f68: d0 4e       .N             ; ALWAYS branch

; &9f6a referenced 1 time by &9e41
.c9f6a
    ldy #4                                                            ; 9f6a: a0 04       ..
    lda l0d63                                                         ; 9f6c: ad 63 0d    .c.
    beq c9f78                                                         ; 9f6f: f0 07       ..
    cmp (fs_options),y                                                ; 9f71: d1 bb       ..
    bne c9f78                                                         ; 9f73: d0 03       ..
    dey                                                               ; 9f75: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 9f76: f1 bb       ..
; &9f78 referenced 2 times by &9f6f, &9f73
.c9f78
    sta svc_state                                                     ; 9f78: 85 a9       ..
; &9f7a referenced 1 time by &9f80
.loop_c9f7a
    lda (fs_options),y                                                ; 9f7a: b1 bb       ..
    sta fs_last_byte_flag,y                                           ; 9f7c: 99 bd 00    ...
    dey                                                               ; 9f7f: 88          .
    bne loop_c9f7a                                                    ; 9f80: d0 f8       ..
    pla                                                               ; 9f82: 68          h
    and #3                                                            ; 9f83: 29 03       ).
    beq c9f55                                                         ; 9f85: f0 ce       ..
    lsr a                                                             ; 9f87: 4a          J
    beq c9f8c                                                         ; 9f88: f0 02       ..
    bcs c9ff7                                                         ; 9f8a: b0 6b       .k
; &9f8c referenced 1 time by &9f88
.c9f8c
    tay                                                               ; 9f8c: a8          .
    lda l0e03,y                                                       ; 9f8d: b9 03 0e    ...
    sta l0f03                                                         ; 9f90: 8d 03 0f    ...
    lda l0e04                                                         ; 9f93: ad 04 0e    ...
    sta l0f04                                                         ; 9f96: 8d 04 0f    ...
    lda l0e02                                                         ; 9f99: ad 02 0e    ...
    sta l0f02                                                         ; 9f9c: 8d 02 0f    ...
    ldx #&12                                                          ; 9f9f: a2 12       ..
    stx l0f01                                                         ; 9fa1: 8e 01 0f    ...
    lda #&0d                                                          ; 9fa4: a9 0d       ..
    sta l0f06                                                         ; 9fa6: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 9fa9: 85 b2       ..
    lsr a                                                             ; 9fab: 4a          J
    sta l0f05                                                         ; 9fac: 8d 05 0f    ...
    clc                                                               ; 9faf: 18          .
    jsr prep_send_tx_cb                                               ; 9fb0: 20 c6 94     ..
    stx fs_load_addr_hi                                               ; 9fb3: 86 b1       ..
    inx                                                               ; 9fb5: e8          .
    stx fs_load_addr                                                  ; 9fb6: 86 b0       ..
; &9fb8 referenced 2 times by &9f68, &a030
.write_data_block
    lda svc_state                                                     ; 9fb8: a5 a9       ..
    bne c9fcd                                                         ; 9fba: d0 11       ..
    ldx fs_load_addr                                                  ; 9fbc: a6 b0       ..
    ldy fs_load_addr_hi                                               ; 9fbe: a4 b1       ..
; &9fc0 referenced 1 time by &9fc9
.loop_c9fc0
    lda l0f05,x                                                       ; 9fc0: bd 05 0f    ...
    sta (fs_crc_lo),y                                                 ; 9fc3: 91 be       ..
    inx                                                               ; 9fc5: e8          .
    iny                                                               ; 9fc6: c8          .
    dec fs_load_addr_2                                                ; 9fc7: c6 b2       ..
    bne loop_c9fc0                                                    ; 9fc9: d0 f5       ..
    beq tail_update_catalogue                                         ; 9fcb: f0 27       .'             ; ALWAYS branch

; &9fcd referenced 1 time by &9fba
.c9fcd
    jsr tube_claim_c3                                                 ; 9fcd: 20 5b a0     [.
    lda #1                                                            ; 9fd0: a9 01       ..
    ldx fs_options                                                    ; 9fd2: a6 bb       ..
    ldy fs_block_offset                                               ; 9fd4: a4 bc       ..
    inx                                                               ; 9fd6: e8          .
    bne c9fda                                                         ; 9fd7: d0 01       ..
    iny                                                               ; 9fd9: c8          .
; &9fda referenced 1 time by &9fd7
.c9fda
    jsr tube_addr_data_dispatch                                       ; 9fda: 20 06 04     ..
    ldx fs_load_addr                                                  ; 9fdd: a6 b0       ..
; &9fdf referenced 1 time by &9fed
.loop_c9fdf
    lda l0f05,x                                                       ; 9fdf: bd 05 0f    ...
    sta tube_data_register_3                                          ; 9fe2: 8d e5 fe    ...
    inx                                                               ; 9fe5: e8          .
    ldy #6                                                            ; 9fe6: a0 06       ..
; &9fe8 referenced 1 time by &9fe9
.loop_c9fe8
    dey                                                               ; 9fe8: 88          .
    bne loop_c9fe8                                                    ; 9fe9: d0 fd       ..
    dec fs_load_addr_2                                                ; 9feb: c6 b2       ..
    bne loop_c9fdf                                                    ; 9fed: d0 f0       ..
    lda #&83                                                          ; 9fef: a9 83       ..
    jsr tube_addr_data_dispatch                                       ; 9ff1: 20 06 04     ..
; &9ff4 referenced 2 times by &9fcb, &a058
.tail_update_catalogue
    jmp c9ce1                                                         ; 9ff4: 4c e1 9c    L..

; &9ff7 referenced 1 time by &9f8a
.c9ff7
    ldy #9                                                            ; 9ff7: a0 09       ..
    lda (fs_options),y                                                ; 9ff9: b1 bb       ..
    sta l0f06                                                         ; 9ffb: 8d 06 0f    ...
    ldy #5                                                            ; 9ffe: a0 05       ..
    lda (fs_options),y                                                ; a000: b1 bb       ..
    sta l0f07                                                         ; a002: 8d 07 0f    ...
    ldx #&0d                                                          ; a005: a2 0d       ..
    stx l0f08                                                         ; a007: 8e 08 0f    ...
    ldy #2                                                            ; a00a: a0 02       ..
    sty fs_load_addr                                                  ; a00c: 84 b0       ..
    sty l0f05                                                         ; a00e: 8c 05 0f    ...
    iny                                                               ; a011: c8          .              ; Y=&03
    jsr save_net_tx_cb                                                ; a012: 20 99 94     ..
    stx fs_load_addr_hi                                               ; a015: 86 b1       ..
    lda l0f06                                                         ; a017: ad 06 0f    ...
    sta (fs_options,x)                                                ; a01a: 81 bb       ..
    lda l0f05                                                         ; a01c: ad 05 0f    ...
    ldy #9                                                            ; a01f: a0 09       ..
    adc (fs_options),y                                                ; a021: 71 bb       q.
    sta (fs_options),y                                                ; a023: 91 bb       ..
    lda txcb_end                                                      ; a025: a5 c8       ..
    sbc #7                                                            ; a027: e9 07       ..
    sta l0f06                                                         ; a029: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; a02c: 85 b2       ..
    beq ca033                                                         ; a02e: f0 03       ..
    jsr write_data_block                                              ; a030: 20 b8 9f     ..
; &a033 referenced 1 time by &a02e
.ca033
    ldx #2                                                            ; a033: a2 02       ..
; &a035 referenced 1 time by &a039
.loop_ca035
    sta l0f07,x                                                       ; a035: 9d 07 0f    ...
    dex                                                               ; a038: ca          .
    bpl loop_ca035                                                    ; a039: 10 fa       ..
    jsr update_addr_from_offset1                                      ; a03b: 20 08 9e     ..
    sec                                                               ; a03e: 38          8
    dec fs_load_addr_2                                                ; a03f: c6 b2       ..
    lda l0f05                                                         ; a041: ad 05 0f    ...
    sta l0f06                                                         ; a044: 8d 06 0f    ...
    jsr adjust_fsopts_4bytes                                          ; a047: 20 0b 9e     ..
    ldx #3                                                            ; a04a: a2 03       ..
    ldy #5                                                            ; a04c: a0 05       ..
    sec                                                               ; a04e: 38          8
; &a04f referenced 1 time by &a055
.loop_ca04f
    lda (fs_options),y                                                ; a04f: b1 bb       ..
    bne ca058                                                         ; a051: d0 05       ..
    iny                                                               ; a053: c8          .
    dex                                                               ; a054: ca          .
    bpl loop_ca04f                                                    ; a055: 10 f8       ..
    clc                                                               ; a057: 18          .
; &a058 referenced 1 time by &a051
.ca058
    jmp tail_update_catalogue                                         ; a058: 4c f4 9f    L..

; &a05b referenced 3 times by &9fcd, &a060, &a2cb
.tube_claim_c3
    lda #&c3                                                          ; a05b: a9 c3       ..
    jsr tube_addr_data_dispatch                                       ; a05d: 20 06 04     ..
    bcc tube_claim_c3                                                 ; a060: 90 f9       ..
    rts                                                               ; a062: 60          `

; ***************************************************************************************
; *FS command.
; Selects filing system by number.
; ***************************************************************************************
.cmd_fs
    lda l0e00                                                         ; a063: ad 00 0e    ...
    sta fs_work_5                                                     ; a066: 85 b5       ..
    lda l0e01                                                         ; a068: ad 01 0e    ...
    sta l00b6                                                         ; a06b: 85 b6       ..
    lda (fs_crc_lo),y                                                 ; a06d: b1 be       ..
    cmp #&0d                                                          ; a06f: c9 0d       ..
    beq ca083                                                         ; a071: f0 10       ..
    jsr parse_fs_ps_args                                              ; a073: 20 8f a0     ..
    lda #1                                                            ; a076: a9 01       ..
    sta fs_work_4                                                     ; a078: 85 b4       ..
    lda #&13                                                          ; a07a: a9 13       ..
    ldx #<(fs_work_4)                                                 ; a07c: a2 b4       ..
    ldy #>(fs_work_4)                                                 ; a07e: a0 00       ..
    jmp osword                                                        ; a080: 4c f1 ff    L..            ; Read/Write NFS information (see https://beebwiki.mdfs.net/OSWORDs)

; &a083 referenced 1 time by &a071
.ca083
    jsr print_file_server_is                                          ; a083: 20 a1 b0     ..
; &a086 referenced 1 time by &b092
.print_fs_info_newline
    bit bit_test_ff_pad                                               ; a086: 2c 7d 94    ,}.
    jsr print_station_addr                                            ; a089: 20 74 b1     t.
    jmp osnewl                                                        ; a08c: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &a08f referenced 3 times by &a073, &aff1, &b1c4
.parse_fs_ps_args
    txa                                                               ; a08f: 8a          .
    pha                                                               ; a090: 48          H
    lda #0                                                            ; a091: a9 00       ..
    sta fs_work_4                                                     ; a093: 85 b4       ..
    jsr parse_addr_arg                                                ; a095: 20 5a 91     Z.
    bcs ca0ad                                                         ; a098: b0 13       ..
    tya                                                               ; a09a: 98          .
    pha                                                               ; a09b: 48          H
    jsr init_bridge_poll                                              ; a09c: 20 68 a8     h.
    eor fs_load_addr_2                                                ; a09f: 45 b2       E.
    beq ca0a5                                                         ; a0a1: f0 02       ..
    lda fs_load_addr_2                                                ; a0a3: a5 b2       ..
; &a0a5 referenced 1 time by &a0a1
.ca0a5
    sta l00b6                                                         ; a0a5: 85 b6       ..
    pla                                                               ; a0a7: 68          h
    tay                                                               ; a0a8: a8          .
    iny                                                               ; a0a9: c8          .
    jsr parse_addr_arg                                                ; a0aa: 20 5a 91     Z.
; &a0ad referenced 1 time by &a098
.ca0ad
    beq ca0b1                                                         ; a0ad: f0 02       ..
    sta fs_work_5                                                     ; a0af: 85 b5       ..
; &a0b1 referenced 1 time by &a0ad
.ca0b1
    pla                                                               ; a0b1: 68          h
    tax                                                               ; a0b2: aa          .
    rts                                                               ; a0b3: 60          `

; &a0b4 referenced 2 times by &a0d2, &a0e2
.get_pb_ptr_as_index
    lda osword_pb_ptr                                                 ; a0b4: a5 f0       ..
; &a0b6 referenced 2 times by &8f13, &b0e4
.byte_to_2bit_index
    asl a                                                             ; a0b6: 0a          .
    asl a                                                             ; a0b7: 0a          .
    pha                                                               ; a0b8: 48          H
    asl a                                                             ; a0b9: 0a          .
    tsx                                                               ; a0ba: ba          .
    php                                                               ; a0bb: 08          .
    adc error_text,x                                                  ; a0bc: 7d 01 01    }..
    ror a                                                             ; a0bf: 6a          j
    plp                                                               ; a0c0: 28          (
    asl a                                                             ; a0c1: 0a          .
    tay                                                               ; a0c2: a8          .
    pla                                                               ; a0c3: 68          h
    cmp #&48 ; 'H'                                                    ; a0c4: c9 48       .H
    bcc return_20                                                     ; a0c6: 90 03       ..
    ldy #0                                                            ; a0c8: a0 00       ..
    tya                                                               ; a0ca: 98          .              ; A=&00
; &a0cb referenced 1 time by &a0c6
.return_20
    rts                                                               ; a0cb: 60          `

    ldy #&6f ; 'o'                                                    ; a0cc: a0 6f       .o
    lda (net_rx_ptr),y                                                ; a0ce: b1 9c       ..
    bcc ca0df                                                         ; a0d0: 90 0d       ..
    jsr get_pb_ptr_as_index                                           ; a0d2: 20 b4 a0     ..
    bcs ca0dd                                                         ; a0d5: b0 06       ..
    lda (nfs_workspace),y                                             ; a0d7: b1 9e       ..
    cmp #&3f ; '?'                                                    ; a0d9: c9 3f       .?
    bne ca0df                                                         ; a0db: d0 02       ..
; &a0dd referenced 1 time by &a0d5
.ca0dd
    lda #0                                                            ; a0dd: a9 00       ..
; &a0df referenced 2 times by &a0d0, &a0db
.ca0df
    sta osword_pb_ptr                                                 ; a0df: 85 f0       ..
    rts                                                               ; a0e1: 60          `

    jsr get_pb_ptr_as_index                                           ; a0e2: 20 b4 a0     ..
    bcc ca0f1                                                         ; a0e5: 90 0a       ..
    ror l0d6c                                                         ; a0e7: 6e 6c 0d    nl.
    lda osword_pb_ptr                                                 ; a0ea: a5 f0       ..
    rol a                                                             ; a0ec: 2a          *
    rol l0d6c                                                         ; a0ed: 2e 6c 0d    .l.
    rts                                                               ; a0f0: 60          `

; &a0f1 referenced 1 time by &a0e5
.ca0f1
    ror l0d61                                                         ; a0f1: 6e 61 0d    na.
    lda #&3f ; '?'                                                    ; a0f4: a9 3f       .?
    sta (nfs_workspace),y                                             ; a0f6: 91 9e       ..
    rol l0d61                                                         ; a0f8: 2e 61 0d    .a.
    rts                                                               ; a0fb: 60          `

; &a0fc referenced 1 time by &8cee
.cmd_fs_entry
    jsr set_text_and_xfer_ptr                                         ; a0fc: 20 7d 92     }.
    ldy #&ff                                                          ; a0ff: a0 ff       ..
    sty fs_spool_handle                                               ; a101: 84 ba       ..
    sty escapable                                                     ; a103: 84 97       ..
    iny                                                               ; a105: c8          .              ; Y=&00
    ldx #&4a ; 'J'                                                    ; a106: a2 4a       .J
    jsr match_fs_cmd                                                  ; a108: 20 28 a1     (.
    bcs ca11b                                                         ; a10b: b0 0e       ..
; &a10d referenced 1 time by &8c4f
.cmd_fs_reentry
    bvc ca11b                                                         ; a10d: 50 0c       P.
; &a10f referenced 1 time by &af4f
.error_syntax
    lda #&dc                                                          ; a10f: a9 dc       ..
    jsr error_inline                                                  ; a111: 20 be 96     ..
    equs "Syntax", 0                                                  ; a114: 53 79 6e... Syn

; &a11b referenced 2 times by &a10b, &a10d
.ca11b
    lda #0                                                            ; a11b: a9 00       ..
    sta svc_state                                                     ; a11d: 85 a9       ..
    lda cmd_table_fs_hi,x                                             ; a11f: bd da a3    ...
    pha                                                               ; a122: 48          H
    lda cmd_table_fs_lo,x                                             ; a123: bd d9 a3    ...
    pha                                                               ; a126: 48          H
    rts                                                               ; a127: 60          `

; &a128 referenced 5 times by &8c4a, &8c78, &a108, &b304, &b331
.match_fs_cmd
    tya                                                               ; a128: 98          .
    pha                                                               ; a129: 48          H
; &a12a referenced 1 time by &a150
.ca12a
    pla                                                               ; a12a: 68          h
    pha                                                               ; a12b: 48          H
    tay                                                               ; a12c: a8          .
    lda cmd_table_fs,x                                                ; a12d: bd d8 a3    ...
    bmi ca191                                                         ; a130: 30 5f       0_
; &a132 referenced 1 time by &a13f
.loop_ca132
    lda cmd_table_fs,x                                                ; a132: bd d8 a3    ...
    bmi ca152                                                         ; a135: 30 1b       0.
    eor (fs_crc_lo),y                                                 ; a137: 51 be       Q.
    and #&df                                                          ; a139: 29 df       ).
    bne ca141                                                         ; a13b: d0 04       ..
    iny                                                               ; a13d: c8          .
    inx                                                               ; a13e: e8          .
    bne loop_ca132                                                    ; a13f: d0 f1       ..
; &a141 referenced 2 times by &a13b, &a145
.ca141
    inx                                                               ; a141: e8          .
    lda cmd_table_fs,x                                                ; a142: bd d8 a3    ...
    bpl ca141                                                         ; a145: 10 fa       ..
    lda (fs_crc_lo),y                                                 ; a147: b1 be       ..
    cmp #&2e ; '.'                                                    ; a149: c9 2e       ..
    beq ca175                                                         ; a14b: f0 28       .(
; &a14d referenced 1 time by &a162
.loop_ca14d
    inx                                                               ; a14d: e8          .
    inx                                                               ; a14e: e8          .
    inx                                                               ; a14f: e8          .
    bne ca12a                                                         ; a150: d0 d8       ..
; &a152 referenced 1 time by &a135
.ca152
    tya                                                               ; a152: 98          .
    pha                                                               ; a153: 48          H
    lda (fs_crc_lo),y                                                 ; a154: b1 be       ..
    ldy #9                                                            ; a156: a0 09       ..
; &a158 referenced 1 time by &a15e
.loop_ca158
    cmp ca164,y                                                       ; a158: d9 64 a1    .d.
    beq ca16d                                                         ; a15b: f0 10       ..
    dey                                                               ; a15d: 88          .
    bpl loop_ca158                                                    ; a15e: 10 f8       ..
    pla                                                               ; a160: 68          h
    tay                                                               ; a161: a8          .
    bne loop_ca14d                                                    ; a162: d0 e9       ..
; &a164 referenced 1 time by &a158
.ca164
    jsr l2322                                                         ; a164: 20 22 23     "#
    bit tube_send_error_num                                           ; a167: 24 26       $&
    rol a                                                             ; a169: 2a          *
    equb &3a, &40, &0d                                                ; a16a: 3a 40 0d    :@.

; &a16d referenced 1 time by &a15b
.ca16d
    pla                                                               ; a16d: 68          h
    tay                                                               ; a16e: a8          .
; &a16f referenced 1 time by &a176
.loop_ca16f
    lda (fs_crc_lo),y                                                 ; a16f: b1 be       ..
    cmp #&20 ; ' '                                                    ; a171: c9 20       .
    bne ca179                                                         ; a173: d0 04       ..
; &a175 referenced 1 time by &a14b
.ca175
    iny                                                               ; a175: c8          .
    jmp loop_ca16f                                                    ; a176: 4c 6f a1    Lo.

; &a179 referenced 1 time by &a173
.ca179
    lda cmd_table_fs,x                                                ; a179: bd d8 a3    ...
    asl a                                                             ; a17c: 0a          .
    bpl ca18a                                                         ; a17d: 10 0b       ..
    lda (fs_crc_lo),y                                                 ; a17f: b1 be       ..
    cmp #&0d                                                          ; a181: c9 0d       ..
    bne ca18a                                                         ; a183: d0 05       ..
    bit bit_test_ff_pad                                               ; a185: 2c 7d 94    ,}.
    bvs ca18b                                                         ; a188: 70 01       p.
; &a18a referenced 2 times by &a17d, &a183
.ca18a
    clv                                                               ; a18a: b8          .
; &a18b referenced 1 time by &a188
.ca18b
    clc                                                               ; a18b: 18          .
; &a18c referenced 1 time by &a1a7
.loop_ca18c
    pla                                                               ; a18c: 68          h
    lda (fs_crc_lo),y                                                 ; a18d: b1 be       ..
    rts                                                               ; a18f: 60          `

; &a190 referenced 1 time by &a19d
.loop_ca190
    iny                                                               ; a190: c8          .
; &a191 referenced 1 time by &a130
.ca191
    lda (fs_crc_lo),y                                                 ; a191: b1 be       ..
    cmp #&0d                                                          ; a193: c9 0d       ..
    beq ca1a6                                                         ; a195: f0 0f       ..
    cmp #&2e ; '.'                                                    ; a197: c9 2e       ..
    beq ca19f                                                         ; a199: f0 04       ..
    cmp #&20 ; ' '                                                    ; a19b: c9 20       .
    bne loop_ca190                                                    ; a19d: d0 f1       ..
; &a19f referenced 2 times by &a199, &a1a4
.ca19f
    iny                                                               ; a19f: c8          .
    lda (fs_crc_lo),y                                                 ; a1a0: b1 be       ..
    cmp #&20 ; ' '                                                    ; a1a2: c9 20       .
    beq ca19f                                                         ; a1a4: f0 f9       ..
; &a1a6 referenced 1 time by &a195
.ca1a6
    sec                                                               ; a1a6: 38          8
    bcs loop_ca18c                                                    ; a1a7: b0 e3       ..             ; ALWAYS branch

    jsr save_ptr_to_os_text                                           ; a1a9: 20 95 af     ..
    jsr mask_owner_access                                             ; a1ac: 20 12 af     ..
    jsr parse_cmd_arg_y0                                              ; a1af: 20 80 ae     ..
; &a1b2 referenced 1 time by &a229
.ca1b2
    ldx #1                                                            ; a1b2: a2 01       ..
    jsr copy_arg_to_buf                                               ; a1b4: 20 f2 ae     ..
    lda #2                                                            ; a1b7: a9 02       ..
    sta l0f05                                                         ; a1b9: 8d 05 0f    ...
    ldy #&12                                                          ; a1bc: a0 12       ..
    jsr save_net_tx_cb                                                ; a1be: 20 99 94     ..
    lda l0f05                                                         ; a1c1: ad 05 0f    ...
    cmp #1                                                            ; a1c4: c9 01       ..
    bne ca1f1                                                         ; a1c6: d0 29       .)
    ldx #3                                                            ; a1c8: a2 03       ..
; &a1ca referenced 1 time by &a1d3
.loop_ca1ca
    inc l0f0a,x                                                       ; a1ca: fe 0a 0f    ...
    beq ca1d2                                                         ; a1cd: f0 03       ..
    jmp ca252                                                         ; a1cf: 4c 52 a2    LR.

; &a1d2 referenced 1 time by &a1cd
.ca1d2
    dex                                                               ; a1d2: ca          .
    bpl loop_ca1ca                                                    ; a1d3: 10 f5       ..
    jsr alloc_fcb_or_error                                            ; a1d5: 20 2e b5     ..
    ldx #1                                                            ; a1d8: a2 01       ..
    stx l0f05                                                         ; a1da: 8e 05 0f    ...
    stx l0f06                                                         ; a1dd: 8e 06 0f    ...
    inx                                                               ; a1e0: e8          .              ; X=&02
    jsr copy_arg_to_buf                                               ; a1e1: 20 f2 ae     ..
    ldy #6                                                            ; a1e4: a0 06       ..
    jsr save_net_tx_cb                                                ; a1e6: 20 99 94     ..
    bcs ca1ee                                                         ; a1e9: b0 03       ..
    jmp ca265                                                         ; a1eb: 4c 65 a2    Le.

; &a1ee referenced 1 time by &a1e9
.ca1ee
    jmp finalise_and_return                                           ; a1ee: 4c bb 9c    L..

; &a1f1 referenced 1 time by &a1c6
.ca1f1
    lda l0e30                                                         ; a1f1: ad 30 0e    .0.
    cmp #&24 ; '$'                                                    ; a1f4: c9 24       .$
    beq error_bad_command                                             ; a1f6: f0 4d       .M
    lda l1071                                                         ; a1f8: ad 71 10    .q.
    bmi ca242                                                         ; a1fb: 30 45       0E
    rol a                                                             ; a1fd: 2a          *
    rol a                                                             ; a1fe: 2a          *
    bmi ca22b                                                         ; a1ff: 30 2a       0*
    bcs error_bad_command                                             ; a201: b0 42       .B
    ldx #&ff                                                          ; a203: a2 ff       ..
; &a205 referenced 1 time by &a20b
.loop_ca205
    inx                                                               ; a205: e8          .
    lda l0e30,x                                                       ; a206: bd 30 0e    .0.
    cmp #&0d                                                          ; a209: c9 0d       ..
    bne loop_ca205                                                    ; a20b: d0 f8       ..
; &a20d referenced 1 time by &a214
.loop_ca20d
    lda l0e30,x                                                       ; a20d: bd 30 0e    .0.
    sta l0e38,x                                                       ; a210: 9d 38 0e    .8.
    dex                                                               ; a213: ca          .
    bpl loop_ca20d                                                    ; a214: 10 f7       ..
    ldx #7                                                            ; a216: a2 07       ..
; &a218 referenced 1 time by &a21f
.loop_ca218
    lda library_dir_prefix,x                                          ; a218: bd 79 a2    .y.
    sta l0e30,x                                                       ; a21b: 9d 30 0e    .0.
    dex                                                               ; a21e: ca          .
    bpl loop_ca218                                                    ; a21f: 10 f7       ..
    lda l1071                                                         ; a221: ad 71 10    .q.
    ora #&60 ; '`'                                                    ; a224: 09 60       .`
    sta l1071                                                         ; a226: 8d 71 10    .q.
; &a229 referenced 1 time by &a240
.loop_ca229
    bne ca1b2                                                         ; a229: d0 87       ..
; &a22b referenced 1 time by &a1ff
.ca22b
    ldx #&ff                                                          ; a22b: a2 ff       ..
; &a22d referenced 1 time by &a236
.loop_ca22d
    inx                                                               ; a22d: e8          .
    lda l0e38,x                                                       ; a22e: bd 38 0e    .8.
    sta l0e30,x                                                       ; a231: 9d 30 0e    .0.
    eor #&0d                                                          ; a234: 49 0d       I.
    bne loop_ca22d                                                    ; a236: d0 f5       ..
    jsr mask_owner_access                                             ; a238: 20 12 af     ..
    ora #&80                                                          ; a23b: 09 80       ..
    sta l1071                                                         ; a23d: 8d 71 10    .q.
    bne loop_ca229                                                    ; a240: d0 e7       ..             ; ALWAYS branch

; &a242 referenced 1 time by &a1fb
.ca242
    jsr mask_owner_access                                             ; a242: 20 12 af     ..
; &a245 referenced 3 times by &a1f6, &a201, &b316
.error_bad_command
    lda #&fe                                                          ; a245: a9 fe       ..
    jsr error_bad_inline                                              ; a247: 20 a2 96     ..
    equs "command", 0                                                 ; a24a: 63 6f 6d... com

; &a252 referenced 1 time by &a1cf
.ca252
    ldx #3                                                            ; a252: a2 03       ..
; &a254 referenced 1 time by &a25a
.loop_ca254
    inc l0f06,x                                                       ; a254: fe 06 0f    ...
    bne ca281                                                         ; a257: d0 28       .(
    dex                                                               ; a259: ca          .
    bne loop_ca254                                                    ; a25a: d0 f8       ..
    lda #&93                                                          ; a25c: a9 93       ..
    jsr error_inline_log                                              ; a25e: 20 bb 96     ..
    equs "No!", 0                                                     ; a261: 4e 6f 21... No!

; &a265 referenced 1 time by &a1eb
.ca265
    lda l0f05                                                         ; a265: ad 05 0f    ...
    jsr alloc_fcb_slot                                                ; a268: 20 fa b4     ..
    tay                                                               ; a26b: a8          .
    lda #0                                                            ; a26c: a9 00       ..
    sta l1060,x                                                       ; a26e: 9d 60 10    .`.
    sty l1070                                                         ; a271: 8c 70 10    .p.
    ldy #3                                                            ; a274: a0 03       ..
    jmp boot_cmd_oscli                                                ; a276: 4c d0 a3    L..

; &a279 referenced 1 time by &a218
.library_dir_prefix
    equs "Library."                                                   ; a279: 4c 69 62... Lib

; &a281 referenced 1 time by &a257
.ca281
    jsr copy_arg_to_buf_x0                                            ; a281: 20 f0 ae     ..
    ldy #0                                                            ; a284: a0 00       ..
    clc                                                               ; a286: 18          .
    jsr gsinit                                                        ; a287: 20 c2 ff     ..
; &a28a referenced 1 time by &a28d
.loop_ca28a
    jsr gsread                                                        ; a28a: 20 c5 ff     ..
    bcc loop_ca28a                                                    ; a28d: 90 fb       ..
    dey                                                               ; a28f: 88          .
; &a290 referenced 1 time by &a295
.loop_ca290
    iny                                                               ; a290: c8          .
    lda (os_text_ptr),y                                               ; a291: b1 f2       ..
    cmp #&20 ; ' '                                                    ; a293: c9 20       .
    beq loop_ca290                                                    ; a295: f0 f9       ..
    eor #&0d                                                          ; a297: 49 0d       I.
    clc                                                               ; a299: 18          .
    tya                                                               ; a29a: 98          .
    adc os_text_ptr                                                   ; a29b: 65 f2       e.
    sta l0e0a                                                         ; a29d: 8d 0a 0e    ...
    lda os_text_ptr_hi                                                ; a2a0: a5 f3       ..
    adc #0                                                            ; a2a2: 69 00       i.
    sta l0e0b                                                         ; a2a4: 8d 0b 0e    ...
    jsr save_text_ptr                                                 ; a2a7: 20 fa 8a     ..
    ldx #&0e                                                          ; a2aa: a2 0e       ..
    stx fs_block_offset                                               ; a2ac: 86 bc       ..
    lda #&10                                                          ; a2ae: a9 10       ..
    sta fs_options                                                    ; a2b0: 85 bb       ..
    sta l0e16                                                         ; a2b2: 8d 16 0e    ...
    ldx #&4a ; 'J'                                                    ; a2b5: a2 4a       .J
    ldy #5                                                            ; a2b7: a0 05       ..
    jsr do_fs_cmd_iteration                                           ; a2b9: 20 3d 99     =.
    lda l0d63                                                         ; a2bc: ad 63 0d    .c.
    beq ca2d7                                                         ; a2bf: f0 16       ..
    and l0f0b                                                         ; a2c1: 2d 0b 0f    -..
    and l0f0c                                                         ; a2c4: 2d 0c 0f    -..
    cmp #&ff                                                          ; a2c7: c9 ff       ..
    beq ca2d7                                                         ; a2c9: f0 0c       ..
    jsr tube_claim_c3                                                 ; a2cb: 20 5b a0     [.
    ldx #9                                                            ; a2ce: a2 09       ..
    ldy #&0f                                                          ; a2d0: a0 0f       ..
    lda #4                                                            ; a2d2: a9 04       ..
    jmp tube_addr_data_dispatch                                       ; a2d4: 4c 06 04    L..

; &a2d7 referenced 2 times by &a2bf, &a2c9
.ca2d7
    lda #1                                                            ; a2d7: a9 01       ..
    jmp (l0f09)                                                       ; a2d9: 6c 09 0f    l..

; &a2dc referenced 1 time by &944b
.find_fs_and_exit
    jsr find_station_bit3                                             ; a2dc: 20 13 a3     ..
    jmp return_with_last_flag                                         ; a2df: 4c b9 9c    L..

    jsr flip_set_station_boot                                         ; a2e2: 20 4a a3     J.
    jmp return_with_last_flag                                         ; a2e5: 4c b9 9c    L..

; &a2e8 referenced 1 time by &a387
.find_station_bit2
    ldx #&10                                                          ; a2e8: a2 10       ..
    clv                                                               ; a2ea: b8          .
; &a2eb referenced 2 times by &a2f1, &a2f8
.ca2eb
    dex                                                               ; a2eb: ca          .
    bmi ca301                                                         ; a2ec: 30 13       0.
    jsr match_station_net                                             ; a2ee: 20 7a b5     z.
    bne ca2eb                                                         ; a2f1: d0 f8       ..
    lda l1060,x                                                       ; a2f3: bd 60 10    .`.
    and #4                                                            ; a2f6: 29 04       ).
    beq ca2eb                                                         ; a2f8: f0 f1       ..
    tya                                                               ; a2fa: 98          .
    sta l1030,x                                                       ; a2fb: 9d 30 10    .0.
    bit bit_test_ff_pad                                               ; a2fe: 2c 7d 94    ,}.
; &a301 referenced 1 time by &a2ec
.ca301
    sty l0e02                                                         ; a301: 8c 02 0e    ...
    bvs ca30f                                                         ; a304: 70 09       p.
    tya                                                               ; a306: 98          .
    jsr alloc_fcb_slot                                                ; a307: 20 fa b4     ..
    sta l1072                                                         ; a30a: 8d 72 10    .r.
    beq jmp_restore_fs_ctx                                            ; a30d: f0 67       .g
; &a30f referenced 1 time by &a304
.ca30f
    lda #&26 ; '&'                                                    ; a30f: a9 26       .&
    bne store_stn_flags_restore                                       ; a311: d0 60       .`             ; ALWAYS branch

; &a313 referenced 3 times by &a2dc, &a345, &a38d
.find_station_bit3
    ldx #&10                                                          ; a313: a2 10       ..
    clv                                                               ; a315: b8          .
; &a316 referenced 2 times by &a31c, &a323
.ca316
    dex                                                               ; a316: ca          .
    bmi ca32c                                                         ; a317: 30 13       0.
    jsr match_station_net                                             ; a319: 20 7a b5     z.
    bne ca316                                                         ; a31c: d0 f8       ..
    lda l1060,x                                                       ; a31e: bd 60 10    .`.
    and #8                                                            ; a321: 29 08       ).
    beq ca316                                                         ; a323: f0 f1       ..
    tya                                                               ; a325: 98          .
    sta l1030,x                                                       ; a326: 9d 30 10    .0.
    bit bit_test_ff_pad                                               ; a329: 2c 7d 94    ,}.
; &a32c referenced 1 time by &a317
.ca32c
    sty l0e03                                                         ; a32c: 8c 03 0e    ...
    bvs ca33a                                                         ; a32f: 70 09       p.
    tya                                                               ; a331: 98          .
    jsr alloc_fcb_slot                                                ; a332: 20 fa b4     ..
    sta l1073                                                         ; a335: 8d 73 10    .s.
    beq jmp_restore_fs_ctx                                            ; a338: f0 3c       .<
; &a33a referenced 1 time by &a32f
.ca33a
    lda #&2a ; '*'                                                    ; a33a: a9 2a       .*
    bne store_stn_flags_restore                                       ; a33c: d0 35       .5             ; ALWAYS branch

; ***************************************************************************************
; *Flip command.
; Toggles auto-boot configuration
; setting.
; ***************************************************************************************
.cmd_flip
    lda l0e03                                                         ; a33e: ad 03 0e    ...            ; Load FS station byte
    pha                                                               ; a341: 48          H              ; Save it
    ldy l0e04                                                         ; a342: ac 04 0e    ...            ; Load boot type flag
    jsr find_station_bit3                                             ; a345: 20 13 a3     ..            ; Find station entry with bit 3 set
    pla                                                               ; a348: 68          h              ; Restore FS station
    tay                                                               ; a349: a8          .              ; Transfer to Y (boot type)
; &a34a referenced 2 times by &a2e2, &a393
.flip_set_station_boot
    ldx #&10                                                          ; a34a: a2 10       ..             ; X=&10: max 16 station entries
    clv                                                               ; a34c: b8          .              ; Clear V (no match found yet)
; &a34d referenced 2 times by &a353, &a35a
.ca34d
    dex                                                               ; a34d: ca          .              ; Decrement station index
    bmi ca363                                                         ; a34e: 30 13       0.             ; All searched: exit loop
    jsr match_station_net                                             ; a350: 20 7a b5     z.            ; Check if station[X] matches
    bne ca34d                                                         ; a353: d0 f8       ..             ; No match: try next station
    lda l1060,x                                                       ; a355: bd 60 10    .`.            ; Load station flags byte
    and #&10                                                          ; a358: 29 10       ).             ; Test bit 4 (active flag)
    beq ca34d                                                         ; a35a: f0 f1       ..             ; Not active: try next station
    tya                                                               ; a35c: 98          .              ; Transfer boot type to A
    sta l1030,x                                                       ; a35d: 9d 30 10    .0.            ; Store boot setting for station
    bit bit_test_ff_pad                                               ; a360: 2c 7d 94    ,}.            ; Set V flag (station match found)
; &a363 referenced 1 time by &a34e
.ca363
    sty l0e04                                                         ; a363: 8c 04 0e    ...            ; Store boot type
    bvs ca371                                                         ; a366: 70 09       p.             ; V set (matched): skip allocation
    tya                                                               ; a368: 98          .              ; Boot type to A
    jsr alloc_fcb_slot                                                ; a369: 20 fa b4     ..            ; Allocate FCB slot for new entry
    sta l1074                                                         ; a36c: 8d 74 10    .t.            ; Store allocation result
    beq jmp_restore_fs_ctx                                            ; a36f: f0 05       ..             ; Zero: allocation failed, exit
; &a371 referenced 1 time by &a366
.ca371
    lda #&32 ; '2'                                                    ; a371: a9 32       .2             ; A=&32: station flags (active+boot)
; &a373 referenced 2 times by &a311, &a33c
.store_stn_flags_restore
    sta l1060,x                                                       ; a373: 9d 60 10    .`.            ; Store station flags
; &a376 referenced 3 times by &a30d, &a338, &a36f
.jmp_restore_fs_ctx
    jmp restore_fs_context                                            ; a376: 4c 73 8f    Ls.            ; Restore FS context and return

    jsr close_all_net_chans                                           ; a379: 20 4a b5     J.            ; Close all network channels
    sec                                                               ; a37c: 38          8              ; Set carry flag
    lda l0f08                                                         ; a37d: ad 08 0f    ...            ; Load reply boot type
    sta l0e05                                                         ; a380: 8d 05 0e    ...            ; Store as current boot type
    php                                                               ; a383: 08          .              ; Save processor status
    ldy l0f05                                                         ; a384: ac 05 0f    ...            ; Load station number from reply
    jsr find_station_bit2                                             ; a387: 20 e8 a2     ..            ; Find station entry with bit 2
    ldy l0f06                                                         ; a38a: ac 06 0f    ...            ; Load network number from reply
    jsr find_station_bit3                                             ; a38d: 20 13 a3     ..            ; Find station entry with bit 3
    ldy l0f07                                                         ; a390: ac 07 0f    ...            ; Load boot type from reply
    jsr flip_set_station_boot                                         ; a393: 20 4a a3     J.            ; Set boot config for station
    plp                                                               ; a396: 28          (              ; Restore processor status
    bcs ca39c                                                         ; a397: b0 03       ..             ; Carry set: proceed with boot
    jmp return_with_last_flag                                         ; a399: 4c b9 9c    L..            ; Return with last flag

; &a39c referenced 1 time by &a397
.ca39c
    lda l1071                                                         ; a39c: ad 71 10    .q.            ; Load config flags
    tax                                                               ; a39f: aa          .              ; Save copy in X
    and #4                                                            ; a3a0: 29 04       ).             ; Test bit 2 (auto-boot flag)
    php                                                               ; a3a2: 08          .              ; Save bit 2 test result
    txa                                                               ; a3a3: 8a          .              ; Restore full flags
    and #&fb                                                          ; a3a4: 29 fb       ).             ; Clear bit 2 (consume flag)
    sta l1071                                                         ; a3a6: 8d 71 10    .q.            ; Store cleared flags
    plp                                                               ; a3a9: 28          (              ; Restore bit 2 test result
    bne ca3cb                                                         ; a3aa: d0 1f       ..             ; Bit 2 was set: skip to boot cmd
    lda #osbyte_scan_keyboard                                         ; a3ac: a9 79       .y             ; OSBYTE &79: scan keyboard
    ldx #(255 - inkey_key_ctrl) EOR 128                               ; a3ae: a2 81       ..             ; X=internal key number EOR 128
    jsr osbyte                                                        ; a3b0: 20 f4 ff     ..            ; Test for 'CTRL' key pressed (X=129)
    txa                                                               ; a3b3: 8a          .              ; X has top bit set if 'CTRL' pressed
    bpl ca3cb                                                         ; a3b4: 10 15       ..             ; CTRL not pressed: proceed to boot
; &a3b6 referenced 1 time by &a3ce
.boot_load_cmd
    rts                                                               ; a3b6: 60          `              ; CTRL pressed: cancel boot, return

    equs "L.!BOOT"                                                    ; a3b7: 4c 2e 21... L.!
    equb &0d                                                          ; a3be: 0d          .
.boot_exec_cmd
    equs "E.!BOOT"                                                    ; a3bf: 45 2e 21... E.!
    equb &0d                                                          ; a3c6: 0d          .
; &a3c7 referenced 1 time by &a3d0
.boot_oscli_lo_table
    equb &c6, &b7, &b9, &bf                                           ; a3c7: c6 b7 b9... ...

; &a3cb referenced 2 times by &a3aa, &a3b4
.ca3cb
    ldy l0e05                                                         ; a3cb: ac 05 0e    ...            ; Load boot type
    beq boot_load_cmd                                                 ; a3ce: f0 e6       ..             ; Type 0: no command, just return
; &a3d0 referenced 1 time by &a276
.boot_cmd_oscli
    ldx boot_oscli_lo_table,y                                         ; a3d0: be c7 a3    ...            ; Look up boot command address low
    ldy #&a3                                                          ; a3d3: a0 a3       ..             ; Boot command address high (&A3xx)
    jmp oscli                                                         ; a3d5: 4c f7 ff    L..            ; Execute boot command via OSCLI

; &a3d8 referenced 12 times by &8ba3, &8bb2, &8bba, &8bc7, &8bf5, &8bfc, &9316, &931e, &a12d, &a132, &a142, &a179
.cmd_table_fs
    equb &43                                                          ; a3d8: 43          C
; &a3d9 referenced 3 times by &8c88, &a123, &b30a
.cmd_table_fs_lo
    equb &6c                                                          ; a3d9: 6c          l
; &a3da referenced 3 times by &8c84, &a11f, &b337
.cmd_table_fs_hi
    equs "ose"                                                        ; a3da: 6f 73 65    ose
    equb &80, &7e, &b9                                                ; a3dd: 80 7e b9    .~.
    equs "Dump"                                                       ; a3e0: 44 75 6d... Dum
    equb &c4, 5, &ba                                                  ; a3e4: c4 05 ba    ...
    equs "Net"                                                        ; a3e7: 4e 65 74    Net
    equb &80, &0d, &8b                                                ; a3ea: 80 0d 8b    ...
    equs "Pollps"                                                     ; a3ed: 50 6f 6c... Pol
    equb &88, &9e, &b1                                                ; a3f3: 88 9e b1    ...
    equs "Print"                                                      ; a3f6: 50 72 69... Pri
    equb &cc, &87, &b9                                                ; a3fb: cc 87 b9    ...
    equs "Prot"                                                       ; a3fe: 50 72 6f... Pro
    equb &8e, &ef, &b2, &50, &53, &88, &cd, &af                       ; a402: 8e ef b2... ...
    equs "Roff"                                                       ; a40a: 52 6f 66... Rof
    equb &80, &cb, &8a                                                ; a40e: 80 cb 8a    ...
    equs "Type"                                                       ; a411: 54 79 70... Typ
    equb &cc, &84, &b9                                                ; a415: cc 84 b9    ...
    equs "Unprot"                                                     ; a418: 55 6e 70... Unp
    equb &8e, &20, &b3, &80                                           ; a41e: 8e 20 b3... . .
.cmd_table_nfs
    equs "Access"                                                     ; a422: 41 63 63... Acc
    equb &c9, &d1, &92                                                ; a428: c9 d1 92    ...
    equs "Bye"                                                        ; a42b: 42 79 65    Bye
    equb &80, &89, &94                                                ; a42e: 80 89 94    ...
    equs "Cdir"                                                       ; a431: 43 64 69... Cdi
    equb &c6, &fd, &ac                                                ; a435: c6 fd ac    ...
    equs "Delete"                                                     ; a438: 44 65 6c... Del
    equb &c3, &d1, &92                                                ; a43e: c3 d1 92    ...
    equs "Dir"                                                        ; a441: 44 69 72    Dir
    equb &81, &c8, &93, &45, &78, &81, &58, &ad                       ; a444: 81 c8 93... ...
    equs "Flip"                                                       ; a44c: 46 6c 69... Fli
    equb &80, &3d, &a3, &46, &53, &8b, &62, &a0                       ; a450: 80 3d a3... .=.
    equs "Info"                                                       ; a458: 49 6e 66... Inf
    equb &c3, &d1, &92                                                ; a45c: c3 d1 92    ...
; &a45f referenced 1 time by &8da4
.cmd_table_nfs_iam
    equs "I am"                                                       ; a45f: 49 20 61... I a
    equb &c2, &6d, &8d                                                ; a463: c2 6d 8d    .m.
    equs "Lcat"                                                       ; a466: 4c 63 61... Lca
    equb &81, &4c, &ad                                                ; a46a: 81 4c ad    .L.
    equs "Lex"                                                        ; a46d: 4c 65 78    Lex
    equb &81, &52, &ad                                                ; a470: 81 52 ad    .R.
    equs "Lib"                                                        ; a473: 4c 69 62    Lib
    equb &c5, &d1, &92                                                ; a476: c5 d1 92    ...
    equs "Pass"                                                       ; a479: 50 61 73... Pas
    equb &c7, &b0, &8d                                                ; a47d: c7 b0 8d    ...
    equs "Remove"                                                     ; a480: 52 65 6d... Rem
    equb &c3, &45, &af                                                ; a486: c3 45 af    .E.
    equs "Rename"                                                     ; a489: 52 65 6e... Ren
    equb &ca, &76, &93                                                ; a48f: ca 76 93    .v.
    equs "Wipe"                                                       ; a492: 57 69 70... Wip
    equb &81, &3c, &b3, &80                                           ; a496: 81 3c b3... .<.
.cmd_table_net
    equb 9, &8e                                                       ; a49a: 09 8e       ..
    equs "Net"                                                        ; a49c: 4e 65 74    Net
    equb &80, &8a, &8b                                                ; a49f: 80 8a 8b    ...
    equs "Utils"                                                      ; a4a2: 55 74 69... Uti
    equb &80, &86, &8b, &80                                           ; a4a7: 80 86 8b... ...
.cmd_table_copro
    equs "Halt"                                                       ; a4ab: 48 61 6c... Hal
    equb &fc, &20, &df                                                ; a4af: fc 20 df    . .
    equs "JSR"                                                        ; a4b2: 4a 53 52    JSR
    equb &fc, 4, &fb                                                  ; a4b5: fc 04 fb    ...
    equs "Peek"                                                       ; a4b8: 50 65 65... Pee
    equb &fc, 1, &fe                                                  ; a4bc: fc 01 fe    ...
    equs "Poke"                                                       ; a4bf: 50 6f 6b... Pok
    equb &fc, 2, &fd                                                  ; a4c3: fc 02 fd    ...
    equs "Proc"                                                       ; a4c6: 50 72 6f... Pro
    equb &fc, 8, &f7                                                  ; a4ca: fc 08 f7    ...
    equs "Utils"                                                      ; a4cd: 55 74 69... Uti
    equb &a9, &10, &ef, &80                                           ; a4d2: a9 10 ef... ...

; ***************************************************************************************
; Service 8: unrecognised OSWORD.
; Handles Econet OSWORD calls (transmit, receive, etc.).
; ***************************************************************************************
.svc_8_osword
    clc                                                               ; a4d6: 18          .
    lda osbyte_a_copy                                                 ; a4d7: a5 ef       ..
    sbc #&0d                                                          ; a4d9: e9 0d       ..
    bmi return_21                                                     ; a4db: 30 2a       0*
    cmp #7                                                            ; a4dd: c9 07       ..
    bcs return_21                                                     ; a4df: b0 26       .&
    jsr osword_setup_handler                                          ; a4e1: 20 ef a4     ..
    ldy #2                                                            ; a4e4: a0 02       ..
; &a4e6 referenced 1 time by &a4ec
.loop_ca4e6
    lda (net_rx_ptr),y                                                ; a4e6: b1 9c       ..
    sta osword_flag,y                                                 ; a4e8: 99 aa 00    ...
    dey                                                               ; a4eb: 88          .
    bpl loop_ca4e6                                                    ; a4ec: 10 f8       ..
    rts                                                               ; a4ee: 60          `

; &a4ef referenced 1 time by &a4e1
.osword_setup_handler
    tax                                                               ; a4ef: aa          .
    lda ca50f,x                                                       ; a4f0: bd 0f a5    ...
    pha                                                               ; a4f3: 48          H
    lda osword_dispatch_lo_table,x                                    ; a4f4: bd 08 a5    ...
    pha                                                               ; a4f7: 48          H
    ldy #2                                                            ; a4f8: a0 02       ..
; &a4fa referenced 1 time by &a500
.loop_ca4fa
    lda osword_flag,y                                                 ; a4fa: b9 aa 00    ...
    sta (net_rx_ptr),y                                                ; a4fd: 91 9c       ..
    dey                                                               ; a4ff: 88          .
    bpl loop_ca4fa                                                    ; a500: 10 f8       ..
    iny                                                               ; a502: c8          .
    lda (osword_pb_ptr),y                                             ; a503: b1 f0       ..
    sty svc_state                                                     ; a505: 84 a9       ..
; &a507 referenced 2 times by &a4db, &a4df
.return_21
    rts                                                               ; a507: 60          `

; &a508 referenced 1 time by &a4f4
.osword_dispatch_lo_table
    equb &15, 6, &8a, &a7, &1b, &30, &cf                              ; a508: 15 06 8a... ...

; &a50f referenced 1 time by &a4f0
.ca50f
    lda open_port_buf_hi                                              ; a50f: a5 a5       ..
    lda open_port_buf_hi                                              ; a511: a5 a5       ..
    ldx port_ws_offset                                                ; a513: a6 a6       ..
    tay                                                               ; a515: a8          .
    pha                                                               ; a516: 48          H
    bit l0d6c                                                         ; a517: 2c 6c 0d    ,l.
    bpl return_22                                                     ; a51a: 10 09       ..
    pla                                                               ; a51c: 68          h
    cmp #4                                                            ; a51d: c9 04       ..
    beq ca526                                                         ; a51f: f0 05       ..
    lda #8                                                            ; a521: a9 08       ..
    sta svc_state                                                     ; a523: 85 a9       ..
; &a525 referenced 1 time by &a51a
.return_22
    rts                                                               ; a525: 60          `

; &a526 referenced 1 time by &a51f
.ca526
    ldx #0                                                            ; a526: a2 00       ..
    ldy #&10                                                          ; a528: a0 10       ..
    jsr save_net_tx_cb                                                ; a52a: 20 99 94     ..
    lda l0f09                                                         ; a52d: ad 09 0f    ...
    jsr bin_to_bcd                                                    ; a530: 20 7c a5     |.
    sta l0f0b                                                         ; a533: 8d 0b 0f    ...
    lda l0f08                                                         ; a536: ad 08 0f    ...
    jsr bin_to_bcd                                                    ; a539: 20 7c a5     |.
    sta l0f0a                                                         ; a53c: 8d 0a 0f    ...
    lda l0f07                                                         ; a53f: ad 07 0f    ...
    jsr bin_to_bcd                                                    ; a542: 20 7c a5     |.
    sta l0f09                                                         ; a545: 8d 09 0f    ...
    lda #0                                                            ; a548: a9 00       ..
    sta l0f08                                                         ; a54a: 8d 08 0f    ...
    lda l0f06                                                         ; a54d: ad 06 0f    ...
    pha                                                               ; a550: 48          H
    lda l0f05                                                         ; a551: ad 05 0f    ...
    jsr bin_to_bcd                                                    ; a554: 20 7c a5     |.
    sta l0f07                                                         ; a557: 8d 07 0f    ...
    pla                                                               ; a55a: 68          h
    pha                                                               ; a55b: 48          H
    and #&0f                                                          ; a55c: 29 0f       ).
    jsr bin_to_bcd                                                    ; a55e: 20 7c a5     |.
    sta l0f06                                                         ; a561: 8d 06 0f    ...
    pla                                                               ; a564: 68          h
    lsr a                                                             ; a565: 4a          J
    lsr a                                                             ; a566: 4a          J
    lsr a                                                             ; a567: 4a          J
    lsr a                                                             ; a568: 4a          J
    adc #&51 ; 'Q'                                                    ; a569: 69 51       iQ
    jsr bin_to_bcd                                                    ; a56b: 20 7c a5     |.
    sta l0f05                                                         ; a56e: 8d 05 0f    ...
    ldy #6                                                            ; a571: a0 06       ..
; &a573 referenced 1 time by &a579
.loop_ca573
    lda l0f05,y                                                       ; a573: b9 05 0f    ...
    sta (osword_pb_ptr),y                                             ; a576: 91 f0       ..
    dey                                                               ; a578: 88          .
    bpl loop_ca573                                                    ; a579: 10 f8       ..
    rts                                                               ; a57b: 60          `

; &a57c referenced 6 times by &a530, &a539, &a542, &a554, &a55e, &a56b
.bin_to_bcd
    php                                                               ; a57c: 08          .
    tax                                                               ; a57d: aa          .
    beq ca589                                                         ; a57e: f0 09       ..
    sed                                                               ; a580: f8          .
    lda #0                                                            ; a581: a9 00       ..
; &a583 referenced 1 time by &a587
.loop_ca583
    clc                                                               ; a583: 18          .
    adc #1                                                            ; a584: 69 01       i.
    dex                                                               ; a586: ca          .
    bne loop_ca583                                                    ; a587: d0 fa       ..
; &a589 referenced 1 time by &a57e
.ca589
    plp                                                               ; a589: 28          (
    rts                                                               ; a58a: 60          `

    asl ws_0d60                                                       ; a58b: 0e 60 0d    .`.
    tya                                                               ; a58e: 98          .
    bcs ca594                                                         ; a58f: b0 03       ..
    sta (osword_pb_ptr),y                                             ; a591: 91 f0       ..
    rts                                                               ; a593: 60          `

; &a594 referenced 1 time by &a58f
.ca594
    lda net_rx_ptr_hi                                                 ; a594: a5 9d       ..
    sta ws_ptr_hi                                                     ; a596: 85 ac       ..
    sta nmi_tx_block_hi                                               ; a598: 85 a1       ..
    lda #&6f ; 'o'                                                    ; a59a: a9 6f       .o
    sta ws_ptr_lo                                                     ; a59c: 85 ab       ..
    sta nmi_tx_block                                                  ; a59e: 85 a0       ..
    ldx #&0f                                                          ; a5a0: a2 0f       ..
    jsr ca6fb                                                         ; a5a2: 20 fb a6     ..
    jmp tx_begin                                                      ; a5a5: 4c 82 85    L..            ; Begin Econet transmission. Copy dest
; station/network from TX control block,
; set up immediate op params, poll for idle
; line before starting frame.

    equb &a6, &9f, &86, &ac, &84, &ab, &6e, &61, &0d, &b1, &f0, &85   ; a5a8: a6 9f 86... ...
    equb &aa, &d0, &1b, &a9,   3, &20, &b6, &a0, &b0                  ; a5b4: aa d0 1b... ...
    equs "=JJ"                                                        ; a5bd: 3d 4a 4a    =JJ
    equb &aa, &b1, &ab, &f0, &36, &c9, &3f, &f0,   4, &e8, &8a, &d0   ; a5c0: aa b1 ab... ...
    equb &ec, &8a, &a2,   0, &81, &f0, &20, &b6, &a0, &b0, &24, &88   ; a5cc: ec 8a a2... ...
    equb &84, &ab, &a9, &c0, &a0,   1, &a2, &0b, &c4, &aa, &71, &ab   ; a5d8: 84 ab a9... ...
    equb &f0,   3, &30, &0e, &18, &20, &fb, &a6, &b0, &0f, &a9, &3f   ; a5e4: f0 03 30... ..0
    equb &a0,   1, &91, &ab, &d0,   7, &69,   1, &d0, &ee, &88, &91   ; a5f0: a0 01 91... ...
    equb &f0, &2e, &61, &0d, &60                                      ; a5fc: f0 2e 61... ..a

; &a601 referenced 1 time by &a8f0
.store_osword_pb_ptr
    ldy #&1c                                                          ; a601: a0 1c       ..
    lda osword_pb_ptr                                                 ; a603: a5 f0       ..
    adc #1                                                            ; a605: 69 01       i.
    jsr store_ptr_at_ws_y                                             ; a607: 20 12 a6     ..
    ldy #1                                                            ; a60a: a0 01       ..
    lda (osword_pb_ptr),y                                             ; a60c: b1 f0       ..
    ldy #&20 ; ' '                                                    ; a60e: a0 20       .
    adc osword_pb_ptr                                                 ; a610: 65 f0       e.
; &a612 referenced 1 time by &a607
.store_ptr_at_ws_y
    sta (nfs_workspace),y                                             ; a612: 91 9e       ..
    iny                                                               ; a614: c8          .
    lda osword_pb_ptr_hi                                              ; a615: a5 f1       ..
    adc #0                                                            ; a617: 69 00       i.
    sta (nfs_workspace),y                                             ; a619: 91 9e       ..
    rts                                                               ; a61b: 60          `

    lda net_rx_ptr_hi                                                 ; a61c: a5 9d       ..
    sta ws_ptr_hi                                                     ; a61e: 85 ac       ..
    ldy #&7f                                                          ; a620: a0 7f       ..
    lda (net_rx_ptr),y                                                ; a622: b1 9c       ..
    iny                                                               ; a624: c8          .              ; Y=&80
    sty ws_ptr_lo                                                     ; a625: 84 ab       ..
    tax                                                               ; a627: aa          .
    dex                                                               ; a628: ca          .
    ldy #0                                                            ; a629: a0 00       ..
    jsr ca6fb                                                         ; a62b: 20 fb a6     ..
    jmp commit_state_byte                                             ; a62e: 4c cb ac    L..

    equb &aa, &c9, &13, &b0, 8, &bd, &51, &a6, &48, &bd, &3f, &a6     ; a631: aa c9 13... ...
    equs "H`bu"                                                       ; a63d: 48 60 62... H`b
    equb 9, &15                                                       ; a641: 09 15       ..
    equs "*06F"                                                       ; a643: 2a 30 36... *06
    equb &e6, &ef, &fd,   3, &ea, &ed,   9, &13, &1e, &29, &a6, &a6   ; a647: e6 ef fd... ...
    equb &a7, &a7, &a7, &a7, &a7, &a7, &a7, &a7, &a7, &a8, &a6, &a6   ; a653: a7 a7 a7... ...
    equb &a8, &a8, &a8, &a8, &2c, &6c, &0d, &30,   3, &4c, &4c, &a7   ; a65f: a8 a8 a8... ...
    equb &a0,   2, &b9, &ff, &0d, &91, &f0, &88, &d0, &f8             ; a66b: a0 02 b9... ...
    equs "`,l"                                                        ; a675: 60 2c 6c    `,l
    equb &0d, &10, &ed, &a0,   0, &20, &9f, &b7, &a0,   2, &b1, &f0   ; a678: 0d 10 ed... ...
    equb &99, &ff, &0d, &88, &d0, &f8, &20, &fe, &8d, &a2, &0f, &bd   ; a684: 99 ff 0d... ...
    equb &60, &10, &a8, &29,   2, &f0, &50, &98, &29, &df, &9d, &60   ; a690: 60 10 a8... `..
    equb &10, &a8, &20, &7a, &b5, &d0, &44, &18, &98, &29,   4, &f0   ; a69c: 10 a8 20... ..
    equb &10, &98,   9, &20, &a8, &bd, &30, &10, &8d,   2, &0e, &8a   ; a6a8: 10 98 09... ...
    equb &69, &20, &8d, &72, &10, &98, &29,   8, &f0, &10, &98,   9   ; a6b4: 69 20 8d... i .
    equb &20, &a8, &bd, &30, &10, &8d,   3, &0e, &8a, &69, &20, &8d   ; a6c0: 20 a8 bd...  ..
    equb &73, &10, &98, &29, &10, &f0, &10, &98,   9, &20, &a8, &bd   ; a6cc: 73 10 98... s..
    equb &30, &10, &8d,   4, &0e, &8a, &69, &20, &8d, &74, &10, &98   ; a6d8: 30 10 8d... 0..
    equb &9d, &60, &10, &ca, &10, &a5, &60, &18, &90,   1, &38, &a9   ; a6e4: 9d 60 10... .`.
    equb &1b, &85, &ab, &a5, &9d, &85, &ac, &a0,   1, &a2,   5        ; a6f0: 1b 85 ab... ...

; &a6fb referenced 3 times by &a5a2, &a62b, &a707
.ca6fb
    bcc ca701                                                         ; a6fb: 90 04       ..
    lda (osword_pb_ptr),y                                             ; a6fd: b1 f0       ..
    sta (ws_ptr_lo),y                                                 ; a6ff: 91 ab       ..
; &a701 referenced 1 time by &a6fb
.ca701
    lda (ws_ptr_lo),y                                                 ; a701: b1 ab       ..
    sta (osword_pb_ptr),y                                             ; a703: 91 f0       ..
    iny                                                               ; a705: c8          .
    dex                                                               ; a706: ca          .
    bpl ca6fb                                                         ; a707: 10 f2       ..
    rts                                                               ; a709: 60          `

    equb &a5, &9f, &85, &ac, &c8, &98, &85, &ab, &aa, &18, &90, &e5   ; a70a: a5 9f 85... ...
    equb &c8, &b1, &f0, &c8, &91, &9e, &b1, &f0, &c8, &91, &9e, &20   ; a716: c8 b1 f0... ...
    equb &68, &a8, &51, &9e, &d0,   2, &91, &9e, &60, &ad, &68, &0d   ; a722: 68 a8 51... h.Q
    equb &4c, &10, &a8, &c8, &b1, &f0, &4c, &1a, &b3, &2c, &6c, &0d   ; a72e: 4c 10 a8... L..
    equb &10, &10, &a0,   3, &b9, &71, &10, &91, &f0, &88, &d0, &f8   ; a73a: 10 10 a0... ...
    equs "`,l"                                                        ; a746: 60 2c 6c    `,l
    equb &0d, &30,   6, &a9,   0, &a8, &91, &f0, &60, &a0,   1, &b1   ; a749: 0d 30 06... .0.
    equb &f0, &c9, &20, &90, &0a, &c9, &30, &b0,   6, &aa, &bd, &10   ; a755: f0 c9 20... ..
    equb &10, &d0,   7, &a9,   0, &aa, &81, &f0, &f0, &26, &bd, &40   ; a761: 10 d0 07... ...
    equb &10, &29,   2, &f0, &f2, &8a, &99, &71, &10, &bd, &10, &10   ; a76d: 10 29 02... .).
    equb &99,   1, &0e, &c0,   1, &d0, &18, &98, &48, &a0,   4, &20   ; a779: 99 01 0e... ...
    equb &c2, &a7, &68, &a8, &bd, &40, &10,   9, &24, &9d, &40, &10   ; a785: c2 a7 68... ..h
    equb &c8, &c0,   4, &d0, &be, &88, &60, &c0,   2, &d0, &13, &98   ; a791: c8 c0 04... ...
    equb &48, &a0,   8, &20, &c2, &a7, &68, &a8, &bd, &40, &10,   9   ; a79d: 48 a0 08... H..
    equb &28, &9d, &40, &10, &d0, &e2, &98, &48, &a0, &10, &20, &c2   ; a7a9: 28 9d 40... (.@
    equb &a7, &68, &a8, &bd, &40, &10,   9, &30, &9d, &40, &10, &d0   ; a7b5: a7 68 a8... .h.
    equb &cf, &8a, &48, &a2, &0f, &bd, &60, &10, &2a, &2a, &10, &14   ; a7c1: cf 8a 48... ..H
    equb &98, &3d, &60, &10, &f0,   5, &98,   9, &20, &d0,   1, &98   ; a7cd: 98 3d 60... .=`
    equb &49, &ff, &3d, &60, &10, &9d, &60, &10, &ca, &10, &e2, &68   ; a7d9: 49 ff 3d... I.=
    equb &aa, &60, &a0,   5, &b1, &9c, &a0,   0, &4c, &10, &a8, &a0   ; a7e5: aa 60 a0... .`.
    equb &7f, &b1, &9c, &a0,   1, &91, &f0, &c8, &a9, &80, &91, &f0   ; a7f1: 7f b1 9c... ...
    equb &60, &ad,   9, &0e, &4c, &10, &a8, &ad, &6d, &0d, &4c, &10   ; a7fd: 60 ad 09... `..
    equb &a8, &a9, &6f, &38, &ed, &6b, &0d, &c8, &91, &f0, &60, &c8   ; a809: a8 a9 6f... ..o
    equb &b9, &6d, &0d, &91, &f0, &c0,   3, &d0, &f6, &60, &c8, &b1   ; a815: b9 6d 0d... .m.
    equb &f0, &99, &6d, &0d, &c0,   3, &d0, &f6                       ; a821: f0 99 6d... ..m
    equs "` h"                                                        ; a829: 60 20 68    ` h
    equb &a8, &a0,   0, &ad, &72, &0d, &c9, &ff, &d0,   4, &98, &91   ; a82c: a8 a0 00... ...
    equb &f0, &60, &c8, &91, &f0, &c8, &c8, &b1, &f0, &f0,   7, &4d   ; a838: f0 60 c8... .`.
; &a844 referenced 1 time by &a878
.bridge_ws_init_data
    equb &72, &0d, &d0, 7, &f0, 3, &ad, 1, &0e, &91, &f0, &60         ; a844: 72 0d d0... r..
; &a850 referenced 1 time by &a87d
.bridge_txcb_init_table
    equb &82, &9c, &ff, &ff                                           ; a850: 82 9c ff... ...
    equs "BRIDGE"                                                     ; a854: 42 52 49... BRI
    equb &9c, 0, &7f, &9c, 0, 0, &72, &0d, &ff, &ff, &74, &0d, &ff    ; a85a: 9c 00 7f... ...
    equb &ff                                                          ; a867: ff          .

; &a868 referenced 2 times by &8dfe, &a09c
.init_bridge_poll
    lda l0d72                                                         ; a868: ad 72 0d    .r.
    cmp #&ff                                                          ; a86b: c9 ff       ..
    bne return_23                                                     ; a86d: d0 60       .`
    tya                                                               ; a86f: 98          .
    pha                                                               ; a870: 48          H
    ldy #&18                                                          ; a871: a0 18       ..
    ldx #&0b                                                          ; a873: a2 0b       ..
    ror l0d61                                                         ; a875: 6e 61 0d    na.
; &a878 referenced 1 time by &a884
.loop_ca878
    lda bridge_ws_init_data,y                                         ; a878: b9 44 a8    .D.
    sta (nfs_workspace),y                                             ; a87b: 91 9e       ..
    lda bridge_txcb_init_table,x                                      ; a87d: bd 50 a8    .P.
    sta txcb_ctrl,x                                                   ; a880: 95 c0       ..
    iny                                                               ; a882: c8          .
    dex                                                               ; a883: ca          .
    bpl loop_ca878                                                    ; a884: 10 f2       ..
    stx l0d72                                                         ; a886: 8e 72 0d    .r.
    rol l0d61                                                         ; a889: 2e 61 0d    .a.
; &a88c referenced 2 times by &a88f, &a8be
.ca88c
    asl ws_0d60                                                       ; a88c: 0e 60 0d    .`.
    bcc ca88c                                                         ; a88f: 90 fb       ..
    lda #&82                                                          ; a891: a9 82       ..
    sta txcb_ctrl                                                     ; a893: 85 c0       ..
    lda #&c0                                                          ; a895: a9 c0       ..
    sta nmi_tx_block                                                  ; a897: 85 a0       ..
    lda #0                                                            ; a899: a9 00       ..
    sta nmi_tx_block_hi                                               ; a89b: 85 a1       ..
    jsr tx_begin                                                      ; a89d: 20 82 85     ..            ; Begin Econet transmission. Copy dest
; station/network from TX control block,
; set up immediate op params, poll for idle
; line before starting frame.
; &a8a0 referenced 1 time by &a8a2
.loop_ca8a0
    bit txcb_ctrl                                                     ; a8a0: 24 c0       $.
    bmi loop_ca8a0                                                    ; a8a2: 30 fc       0.
    tax                                                               ; a8a4: aa          .
    pha                                                               ; a8a5: 48          H
    lda osword_pb_ptr_hi                                              ; a8a6: a5 f1       ..
    pha                                                               ; a8a8: 48          H
    ldx osword_pb_ptr                                                 ; a8a9: a6 f0       ..
    lda #osbyte_vsync                                                 ; a8ab: a9 13       ..
    jsr osbyte                                                        ; a8ad: 20 f4 ff     ..            ; Wait for vertical sync
    pla                                                               ; a8b0: 68          h
    sta osword_pb_ptr_hi                                              ; a8b1: 85 f1       ..
    pla                                                               ; a8b3: 68          h
    tax                                                               ; a8b4: aa          .
    ldy #&18                                                          ; a8b5: a0 18       ..
    lda (nfs_workspace),y                                             ; a8b7: b1 9e       ..
    bmi ca8c0                                                         ; a8b9: 30 05       0.
    jsr advance_x_by_8                                                ; a8bb: 20 84 bc     ..
    bpl ca88c                                                         ; a8be: 10 cc       ..
; &a8c0 referenced 1 time by &a8b9
.ca8c0
    lda #&3f ; '?'                                                    ; a8c0: a9 3f       .?
    sta (nfs_workspace),y                                             ; a8c2: 91 9e       ..
    pla                                                               ; a8c4: 68          h
    tay                                                               ; a8c5: a8          .
    lda l0d72                                                         ; a8c6: ad 72 0d    .r.
    tax                                                               ; a8c9: aa          .
    eor #&ff                                                          ; a8ca: 49 ff       I.
    beq return_23                                                     ; a8cc: f0 01       ..
    txa                                                               ; a8ce: 8a          .
; &a8cf referenced 4 times by &a86d, &a8cc, &a8d7, &a943
.return_23
    rts                                                               ; a8cf: 60          `

    cmp #1                                                            ; a8d0: c9 01       ..
    bcs ca926                                                         ; a8d2: b0 52       .R
    bit l0d6c                                                         ; a8d4: 2c 6c 0d    ,l.
    bpl return_23                                                     ; a8d7: 10 f6       ..
    ldy #&23 ; '#'                                                    ; a8d9: a0 23       .#
    jsr mask_owner_access                                             ; a8db: 20 12 af     ..
; &a8de referenced 1 time by &a8eb
.loop_ca8de
    lda init_txcb,y                                                   ; a8de: b9 5f 94    ._.
    bne ca8e6                                                         ; a8e1: d0 03       ..
    lda l0de6,y                                                       ; a8e3: b9 e6 0d    ...
; &a8e6 referenced 1 time by &a8e1
.ca8e6
    sta (nfs_workspace),y                                             ; a8e6: 91 9e       ..
    dey                                                               ; a8e8: 88          .
    cpy #&17                                                          ; a8e9: c0 17       ..
    bne loop_ca8de                                                    ; a8eb: d0 f1       ..
    iny                                                               ; a8ed: c8          .
    sty net_tx_ptr                                                    ; a8ee: 84 9a       ..
    jsr store_osword_pb_ptr                                           ; a8f0: 20 01 a6     ..
    ldy #2                                                            ; a8f3: a0 02       ..
    lda #&90                                                          ; a8f5: a9 90       ..
    sta escapable                                                     ; a8f7: 85 97       ..
    sta (osword_pb_ptr),y                                             ; a8f9: 91 f0       ..
    iny                                                               ; a8fb: c8          .              ; Y=&03
    iny                                                               ; a8fc: c8          .              ; Y=&04
; &a8fd referenced 1 time by &a905
.loop_ca8fd
    lda l0dfe,y                                                       ; a8fd: b9 fe 0d    ...
    sta (osword_pb_ptr),y                                             ; a900: 91 f0       ..
    iny                                                               ; a902: c8          .
    cpy #7                                                            ; a903: c0 07       ..
    bne loop_ca8fd                                                    ; a905: d0 f6       ..
    lda nfs_workspace_hi                                              ; a907: a5 9f       ..
    sta net_tx_ptr_hi                                                 ; a909: 85 9b       ..
    cli                                                               ; a90b: 58          X
    jsr send_net_packet                                               ; a90c: 20 2a 98     *.
    ldy #&20 ; ' '                                                    ; a90f: a0 20       .
    lda #&ff                                                          ; a911: a9 ff       ..
    sta (nfs_workspace),y                                             ; a913: 91 9e       ..
    iny                                                               ; a915: c8          .              ; Y=&21
    sta (nfs_workspace),y                                             ; a916: 91 9e       ..
    ldy #&19                                                          ; a918: a0 19       ..
    lda #&90                                                          ; a91a: a9 90       ..
    sta (nfs_workspace),y                                             ; a91c: 91 9e       ..
    dey                                                               ; a91e: 88          .              ; Y=&18
    lda #&7f                                                          ; a91f: a9 7f       ..
    sta (nfs_workspace),y                                             ; a921: 91 9e       ..
    jmp wait_net_tx_ack                                               ; a923: 4c c7 95    L..

; &a926 referenced 1 time by &a8d2
.ca926
    php                                                               ; a926: 08          .
    ldy #1                                                            ; a927: a0 01       ..
    lda (osword_pb_ptr),y                                             ; a929: b1 f0       ..
    tax                                                               ; a92b: aa          .
    iny                                                               ; a92c: c8          .              ; Y=&02
    lda (osword_pb_ptr),y                                             ; a92d: b1 f0       ..
    iny                                                               ; a92f: c8          .              ; Y=&03
    sty ws_ptr_lo                                                     ; a930: 84 ab       ..
    ldy #&72 ; 'r'                                                    ; a932: a0 72       .r
    sta (net_rx_ptr),y                                                ; a934: 91 9c       ..
    dey                                                               ; a936: 88          .              ; Y=&71
    txa                                                               ; a937: 8a          .
    sta (net_rx_ptr),y                                                ; a938: 91 9c       ..
    plp                                                               ; a93a: 28          (
    bne ca959                                                         ; a93b: d0 1c       ..
; &a93d referenced 1 time by &a956
.loop_ca93d
    ldy ws_ptr_lo                                                     ; a93d: a4 ab       ..
    inc ws_ptr_lo                                                     ; a93f: e6 ab       ..
    lda (osword_pb_ptr),y                                             ; a941: b1 f0       ..
    beq return_23                                                     ; a943: f0 8a       ..
    ldy #&7d ; '}'                                                    ; a945: a0 7d       .}
    sta (net_rx_ptr),y                                                ; a947: 91 9c       ..
    pha                                                               ; a949: 48          H
    jsr init_ws_copy_wide                                             ; a94a: 20 6a aa     j.
    jsr enable_irq_and_poll                                           ; a94d: 20 64 a9     d.
; &a950 referenced 1 time by &a951
.loop_ca950
    dex                                                               ; a950: ca          .
    bne loop_ca950                                                    ; a951: d0 fd       ..
    pla                                                               ; a953: 68          h
    eor #&0d                                                          ; a954: 49 0d       I.
    bne loop_ca93d                                                    ; a956: d0 e5       ..
    rts                                                               ; a958: 60          `

; &a959 referenced 1 time by &a93b
.ca959
    jsr init_ws_copy_wide                                             ; a959: 20 6a aa     j.
    ldy #&7b ; '{'                                                    ; a95c: a0 7b       .{
    lda (net_rx_ptr),y                                                ; a95e: b1 9c       ..
    adc #3                                                            ; a960: 69 03       i.
    sta (net_rx_ptr),y                                                ; a962: 91 9c       ..
; &a964 referenced 1 time by &a94d
.enable_irq_and_poll
    cli                                                               ; a964: 58          X
    jmp send_net_packet                                               ; a965: 4c 2a 98    L*.

    php                                                               ; a968: 08          .
    pha                                                               ; a969: 48          H
    txa                                                               ; a96a: 8a          .
    pha                                                               ; a96b: 48          H
    tya                                                               ; a96c: 98          .
    pha                                                               ; a96d: 48          H
    tsx                                                               ; a96e: ba          .
    lda l0103,x                                                       ; a96f: bd 03 01    ...
    cmp #9                                                            ; a972: c9 09       ..
    bcs ca97a                                                         ; a974: b0 04       ..
    tax                                                               ; a976: aa          .
    jsr push_osword_handler_addr                                      ; a977: 20 81 a9     ..
; &a97a referenced 1 time by &a974
.ca97a
    pla                                                               ; a97a: 68          h
    tay                                                               ; a97b: a8          .
    pla                                                               ; a97c: 68          h
    tax                                                               ; a97d: aa          .
    pla                                                               ; a97e: 68          h
    plp                                                               ; a97f: 28          (
    rts                                                               ; a980: 60          `

; &a981 referenced 1 time by &a977
.push_osword_handler_addr
    lda osword_handler_hi_table,x                                     ; a981: bd 95 a9    ...
    pha                                                               ; a984: 48          H
    lda osword_handler_lo_table,x                                     ; a985: bd 8c a9    ...
    pha                                                               ; a988: 48          H
    lda osbyte_a_copy                                                 ; a989: a5 ef       ..
    rts                                                               ; a98b: 60          `

; &a98c referenced 1 time by &a985
.osword_handler_lo_table
    equb &41, &da, &da, &da, &9d, &c5, &41, &cf, &3e                  ; a98c: 41 da da... A..
; &a995 referenced 1 time by &a981
.osword_handler_hi_table
    equb &8e, &aa, &aa, &aa, &a9, &aa, &8e, &a9, &aa, &ba, &7e, 6, 1  ; a995: 8e aa aa... ...
    equb &1e,   6,   1, &98, &a0, &da, &91, &9e, &a9,   0             ; a9a2: 1e 06 01... ...

; &a9ac referenced 2 times by &8adf, &a9ff
.tx_econet_abort
    ldy #&d9                                                          ; a9ac: a0 d9       ..
    sta (nfs_workspace),y                                             ; a9ae: 91 9e       ..
    lda #&80                                                          ; a9b0: a9 80       ..
    ldy #&0c                                                          ; a9b2: a0 0c       ..
    sta (nfs_workspace),y                                             ; a9b4: 91 9e       ..
    lda net_tx_ptr                                                    ; a9b6: a5 9a       ..
    pha                                                               ; a9b8: 48          H
    lda net_tx_ptr_hi                                                 ; a9b9: a5 9b       ..
    pha                                                               ; a9bb: 48          H
    sty net_tx_ptr                                                    ; a9bc: 84 9a       ..
    ldx nfs_workspace_hi                                              ; a9be: a6 9f       ..
    stx net_tx_ptr_hi                                                 ; a9c0: 86 9b       ..
    jsr send_net_packet                                               ; a9c2: 20 2a 98     *.
    lda #&3f ; '?'                                                    ; a9c5: a9 3f       .?
    sta (net_tx_ptr,x)                                                ; a9c7: 81 9a       ..
    pla                                                               ; a9c9: 68          h
    sta net_tx_ptr_hi                                                 ; a9ca: 85 9b       ..
    pla                                                               ; a9cc: 68          h
    sta net_tx_ptr                                                    ; a9cd: 85 9a       ..
    rts                                                               ; a9cf: 60          `

    ldy osword_pb_ptr_hi                                              ; a9d0: a4 f1       ..
    cmp #&81                                                          ; a9d2: c9 81       ..
    beq ca9e9                                                         ; a9d4: f0 13       ..
    ldy #1                                                            ; a9d6: a0 01       ..
    ldx #&0a                                                          ; a9d8: a2 0a       ..
    jsr caa24                                                         ; a9da: 20 24 aa     $.
    beq ca9e9                                                         ; a9dd: f0 0a       ..
    dey                                                               ; a9df: 88          .
    dey                                                               ; a9e0: 88          .
    ldx #&11                                                          ; a9e1: a2 11       ..
    jsr caa24                                                         ; a9e3: 20 24 aa     $.
    beq ca9e9                                                         ; a9e6: f0 01       ..
    iny                                                               ; a9e8: c8          .
; &a9e9 referenced 3 times by &a9d4, &a9dd, &a9e6
.ca9e9
    ldx #2                                                            ; a9e9: a2 02       ..
    tya                                                               ; a9eb: 98          .
    beq return_24                                                     ; a9ec: f0 35       .5
    php                                                               ; a9ee: 08          .
    bpl ca9f2                                                         ; a9ef: 10 01       ..
    inx                                                               ; a9f1: e8          .              ; X=&03
; &a9f2 referenced 1 time by &a9ef
.ca9f2
    ldy #&dc                                                          ; a9f2: a0 dc       ..
; &a9f4 referenced 1 time by &a9fc
.loop_ca9f4
    lda tube_claimed_id,y                                             ; a9f4: b9 15 00    ...
    sta (nfs_workspace),y                                             ; a9f7: 91 9e       ..
    dey                                                               ; a9f9: 88          .
    cpy #&da                                                          ; a9fa: c0 da       ..
    bpl loop_ca9f4                                                    ; a9fc: 10 f6       ..
    txa                                                               ; a9fe: 8a          .
    jsr tx_econet_abort                                               ; a9ff: 20 ac a9     ..
    plp                                                               ; aa02: 28          (
    bpl return_24                                                     ; aa03: 10 1e       ..
    lda #&7f                                                          ; aa05: a9 7f       ..
    ldy #&0c                                                          ; aa07: a0 0c       ..
    sta (nfs_workspace),y                                             ; aa09: 91 9e       ..
; &aa0b referenced 1 time by &aa0d
.loop_caa0b
    lda (nfs_workspace),y                                             ; aa0b: b1 9e       ..
    bpl loop_caa0b                                                    ; aa0d: 10 fc       ..
    tsx                                                               ; aa0f: ba          .
    ldy #&dd                                                          ; aa10: a0 dd       ..
    lda (nfs_workspace),y                                             ; aa12: b1 9e       ..
    ora #&44 ; 'D'                                                    ; aa14: 09 44       .D
    bne caa1c                                                         ; aa16: d0 04       ..             ; ALWAYS branch

; &aa18 referenced 1 time by &aa21
.loop_caa18
    dey                                                               ; aa18: 88          .
    dex                                                               ; aa19: ca          .
    lda (nfs_workspace),y                                             ; aa1a: b1 9e       ..
; &aa1c referenced 1 time by &aa16
.caa1c
    sta l0106,x                                                       ; aa1c: 9d 06 01    ...
    cpy #&da                                                          ; aa1f: c0 da       ..
    bne loop_caa18                                                    ; aa21: d0 f5       ..
; &aa23 referenced 2 times by &a9ec, &aa03
.return_24
    rts                                                               ; aa23: 60          `

; &aa24 referenced 3 times by &a9da, &a9e3, &aa2a
.caa24
    cmp osword_claim_codes,x                                          ; aa24: dd 2d aa    .-.
    beq return_25                                                     ; aa27: f0 03       ..
    dex                                                               ; aa29: ca          .
    bpl caa24                                                         ; aa2a: 10 f8       ..
; &aa2c referenced 1 time by &aa27
.return_25
    rts                                                               ; aa2c: 60          `

; &aa2d referenced 1 time by &aa24
.osword_claim_codes
    equb   4,   9, &0a, &14, &15, &9a, &9b, &e1, &e2, &e3, &e4, &0b   ; aa2d: 04 09 0a... ...
    equb &0c, &0f, &79, &7a, &86, &87, &a0, &0e, &c9,   7, &f0,   4   ; aa39: 0c 0f 79... ..y
    equb &c9,   8, &d0, &e3, &a2, &db, &86, &9e, &b1, &f0, &91, &9e   ; aa45: c9 08 d0... ...
    equb &88, &10, &f9, &c8, &c6, &9e, &a5, &ef, &91, &9e, &84, &9e   ; aa51: 88 10 f9... ...
    equb &a0, &14, &a9, &e9, &91, &9e, &a9,   1, &20, &ac, &a9, &86   ; aa5d: a0 14 a9... ...
    equb &9e                                                          ; aa69: 9e          .

; &aa6a referenced 2 times by &a94a, &a959
.init_ws_copy_wide
    ldx #&0d                                                          ; aa6a: a2 0d       ..
    ldy #&7c ; '|'                                                    ; aa6c: a0 7c       .|
    bit bit_test_ff_pad                                               ; aa6e: 2c 7d 94    ,}.
    bvs caa78                                                         ; aa71: 70 05       p.
; &aa73 referenced 1 time by &958c
.init_ws_copy_narrow
    ldy #&17                                                          ; aa73: a0 17       ..
    ldx #&1a                                                          ; aa75: a2 1a       ..
; &aa77 referenced 1 time by &ab38
.ws_copy_vclr_entry
    clv                                                               ; aa77: b8          .
; &aa78 referenced 2 times by &aa71, &aa99
.caa78
    lda caa9f,x                                                       ; aa78: bd 9f aa    ...
    cmp #&fe                                                          ; aa7b: c9 fe       ..
    beq caa9b                                                         ; aa7d: f0 1c       ..
    cmp #&fd                                                          ; aa7f: c9 fd       ..
    beq caa97                                                         ; aa81: f0 14       ..
    cmp #&fc                                                          ; aa83: c9 fc       ..
    bne caa8f                                                         ; aa85: d0 08       ..
    lda net_rx_ptr_hi                                                 ; aa87: a5 9d       ..
    bvs caa8d                                                         ; aa89: 70 02       p.
    lda nfs_workspace_hi                                              ; aa8b: a5 9f       ..
; &aa8d referenced 1 time by &aa89
.caa8d
    sta net_tx_ptr_hi                                                 ; aa8d: 85 9b       ..
; &aa8f referenced 1 time by &aa85
.caa8f
    bvs caa95                                                         ; aa8f: 70 04       p.
    sta (nfs_workspace),y                                             ; aa91: 91 9e       ..
    bvc caa97                                                         ; aa93: 50 02       P.             ; ALWAYS branch

; &aa95 referenced 1 time by &aa8f
.caa95
    sta (net_rx_ptr),y                                                ; aa95: 91 9c       ..
; &aa97 referenced 2 times by &aa81, &aa93
.caa97
    dey                                                               ; aa97: 88          .
    dex                                                               ; aa98: ca          .
    bpl caa78                                                         ; aa99: 10 dd       ..
; &aa9b referenced 1 time by &aa7d
.caa9b
    iny                                                               ; aa9b: c8          .
    sty net_tx_ptr                                                    ; aa9c: 84 9a       ..
    rts                                                               ; aa9e: 60          `

; &aa9f referenced 1 time by &aa78
.caa9f
    sta zp_ptr_lo                                                     ; aa9f: 85 00       ..
    sbc l7dfd,x                                                       ; aaa1: fd fd 7d    ..}
    equb &fc, &ff, &ff, &7e, &fc, &ff, &ff,   0,   0, &fe, &80, &93   ; aaa4: fc ff ff... ...
    equb &fd, &fd, &d9, &fc, &ff, &ff, &de, &fc, &ff, &ff, &fe, &d1   ; aab0: fd fd d9... ...
    equb &fd, &fd, &25, &fd, &ff, &ff, &fd, &fd, &ff, &ff, &ca, &e4   ; aabc: fd fd 25... ..%
    equb &f0, &d0, &0f, &a5, &d0, &6a, &b0, &0a                       ; aac8: f0 d0 0f... ...

; &aad0 referenced 2 times by &8f0e, &ab21
.reset_spool_buf_state
    lda #&25 ; '%'                                                    ; aad0: a9 25       .%
    sta l0d6b                                                         ; aad2: 8d 6b 0d    .k.
    lda #&41 ; 'A'                                                    ; aad5: a9 41       .A
    sta ws_0d6a                                                       ; aad7: 8d 6a 0d    .j.
; &aada referenced 2 times by &aadd, &aaf1
.return_26
    rts                                                               ; aada: 60          `

    cpy #4                                                            ; aadb: c0 04       ..
    bne return_26                                                     ; aadd: d0 fb       ..
    txa                                                               ; aadf: 8a          .
    dex                                                               ; aae0: ca          .
    bne handle_spool_ctrl_byte                                        ; aae1: d0 26       .&
    tsx                                                               ; aae3: ba          .
    ora l0106,x                                                       ; aae4: 1d 06 01    ...
    sta l0106,x                                                       ; aae7: 9d 06 01    ...
; &aaea referenced 2 times by &aaf9, &aafe
.caaea
    lda #osbyte_read_buffer                                           ; aaea: a9 91       ..
    ldx #buffer_printer                                               ; aaec: a2 03       ..
    jsr osbyte                                                        ; aaee: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_26                                                     ; aaf1: b0 e7       ..
    tya                                                               ; aaf3: 98          .              ; Y is the character extracted from the buffer
    jsr append_byte_to_rxbuf                                          ; aaf4: 20 00 ab     ..
    cpy #&6e ; 'n'                                                    ; aaf7: c0 6e       .n
    bcc caaea                                                         ; aaf9: 90 ef       ..
    jsr cab24                                                         ; aafb: 20 24 ab     $.
    bcc caaea                                                         ; aafe: 90 ea       ..
; &ab00 referenced 3 times by &aaf4, &ab1b, &abd2
.append_byte_to_rxbuf
    ldy l0d6b                                                         ; ab00: ac 6b 0d    .k.
    sta (net_rx_ptr),y                                                ; ab03: 91 9c       ..
    inc l0d6b                                                         ; ab05: ee 6b 0d    .k.
    rts                                                               ; ab08: 60          `

; &ab09 referenced 2 times by &8f3d, &aae1
.handle_spool_ctrl_byte
    ror a                                                             ; ab09: 6a          j
    bcc cab63                                                         ; ab0a: 90 57       .W
    lda ws_0d6a                                                       ; ab0c: ad 6a 0d    .j.
    pha                                                               ; ab0f: 48          H
    ror a                                                             ; ab10: 6a          j
    pla                                                               ; ab11: 68          h
    bcs cab21                                                         ; ab12: b0 0d       ..
    ora #3                                                            ; ab14: 09 03       ..
    sta ws_0d6a                                                       ; ab16: 8d 6a 0d    .j.
    lda #3                                                            ; ab19: a9 03       ..
    jsr append_byte_to_rxbuf                                          ; ab1b: 20 00 ab     ..
    jsr cab24                                                         ; ab1e: 20 24 ab     $.
; &ab21 referenced 1 time by &ab12
.cab21
    jmp reset_spool_buf_state                                         ; ab21: 4c d0 aa    L..

; &ab24 referenced 4 times by &aafb, &ab1e, &ab67, &abd5
.cab24
    ldy #8                                                            ; ab24: a0 08       ..
    lda l0d6b                                                         ; ab26: ad 6b 0d    .k.
    sta (nfs_workspace),y                                             ; ab29: 91 9e       ..
    lda net_rx_ptr_hi                                                 ; ab2b: a5 9d       ..
    iny                                                               ; ab2d: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; ab2e: 91 9e       ..
    ldy #5                                                            ; ab30: a0 05       ..
    sta (nfs_workspace),y                                             ; ab32: 91 9e       ..
    ldy #&0b                                                          ; ab34: a0 0b       ..
    ldx #&26 ; '&'                                                    ; ab36: a2 26       .&
    jsr ws_copy_vclr_entry                                            ; ab38: 20 77 aa     w.
    dey                                                               ; ab3b: 88          .
    lda ws_0d6a                                                       ; ab3c: ad 6a 0d    .j.
    pha                                                               ; ab3f: 48          H
    rol a                                                             ; ab40: 2a          *
    pla                                                               ; ab41: 68          h
    eor #&80                                                          ; ab42: 49 80       I.
    sta ws_0d6a                                                       ; ab44: 8d 6a 0d    .j.
    rol a                                                             ; ab47: 2a          *
    sta (nfs_workspace),y                                             ; ab48: 91 9e       ..
    lda l00d0                                                         ; ab4a: a5 d0       ..
    pha                                                               ; ab4c: 48          H
    and #&fe                                                          ; ab4d: 29 fe       ).
    sta l00d0                                                         ; ab4f: 85 d0       ..
    ldy #&25 ; '%'                                                    ; ab51: a0 25       .%
    sty l0d6b                                                         ; ab53: 8c 6b 0d    .k.
    lda #0                                                            ; ab56: a9 00       ..
    tax                                                               ; ab58: aa          .              ; X=&00
    ldy nfs_workspace_hi                                              ; ab59: a4 9f       ..
    cli                                                               ; ab5b: 58          X
    jsr send_disconnect_reply                                         ; ab5c: 20 12 ac     ..
    pla                                                               ; ab5f: 68          h
    sta l00d0                                                         ; ab60: 85 d0       ..
    rts                                                               ; ab62: 60          `

; &ab63 referenced 1 time by &ab0a
.cab63
    lda ws_0d6a                                                       ; ab63: ad 6a 0d    .j.
    ror a                                                             ; ab66: 6a          j
    bcc cab24                                                         ; ab67: 90 bb       ..
    lda l00d0                                                         ; ab69: a5 d0       ..
    pha                                                               ; ab6b: 48          H
    and #&fe                                                          ; ab6c: 29 fe       ).
    sta l00d0                                                         ; ab6e: 85 d0       ..
    lda #&14                                                          ; ab70: a9 14       ..
; &ab72 referenced 1 time by &abe6
.cab72
    pha                                                               ; ab72: 48          H
    ldx #&0b                                                          ; ab73: a2 0b       ..
    ldy #&30 ; '0'                                                    ; ab75: a0 30       .0
; &ab77 referenced 1 time by &ab7e
.loop_cab77
    lda tx_econet_txcb_template,x                                     ; ab77: bd 6e ac    .n.
    sta (net_rx_ptr),y                                                ; ab7a: 91 9c       ..
    dey                                                               ; ab7c: 88          .
    dex                                                               ; ab7d: ca          .
    bpl loop_cab77                                                    ; ab7e: 10 f7       ..
    stx escapable                                                     ; ab80: 86 97       ..
    ldy #2                                                            ; ab82: a0 02       ..
    lda (nfs_workspace),y                                             ; ab84: b1 9e       ..
    pha                                                               ; ab86: 48          H
    iny                                                               ; ab87: c8          .              ; Y=&03
    lda (nfs_workspace),y                                             ; ab88: b1 9e       ..
    ldy #&28 ; '('                                                    ; ab8a: a0 28       .(
    sta (net_rx_ptr),y                                                ; ab8c: 91 9c       ..
    dey                                                               ; ab8e: 88          .              ; Y=&27
    pla                                                               ; ab8f: 68          h
    sta (net_rx_ptr),y                                                ; ab90: 91 9c       ..
    ldx #&0b                                                          ; ab92: a2 0b       ..
    ldy #&0b                                                          ; ab94: a0 0b       ..
; &ab96 referenced 1 time by &aba7
.loop_cab96
    lda rx_palette_txcb_template,x                                    ; ab96: bd 7a ac    .z.
    cmp #&fd                                                          ; ab99: c9 fd       ..
    beq caba5                                                         ; ab9b: f0 08       ..
    cmp #&fc                                                          ; ab9d: c9 fc       ..
    bne caba3                                                         ; ab9f: d0 02       ..
    lda net_rx_ptr_hi                                                 ; aba1: a5 9d       ..
; &aba3 referenced 1 time by &ab9f
.caba3
    sta (nfs_workspace),y                                             ; aba3: 91 9e       ..
; &aba5 referenced 1 time by &ab9b
.caba5
    dey                                                               ; aba5: 88          .
    dex                                                               ; aba6: ca          .
    bpl loop_cab96                                                    ; aba7: 10 ed       ..
    lda #&25 ; '%'                                                    ; aba9: a9 25       .%
    sta net_tx_ptr                                                    ; abab: 85 9a       ..
    lda net_rx_ptr_hi                                                 ; abad: a5 9d       ..
    sta net_tx_ptr_hi                                                 ; abaf: 85 9b       ..
    jsr setup_pass_txbuf                                              ; abb1: 20 87 98     ..
    jsr send_net_packet                                               ; abb4: 20 2a 98     *.
    lda #0                                                            ; abb7: a9 00       ..
    sta net_tx_ptr                                                    ; abb9: 85 9a       ..
    lda nfs_workspace_hi                                              ; abbb: a5 9f       ..
    sta net_tx_ptr_hi                                                 ; abbd: 85 9b       ..
    jsr wait_net_tx_ack                                               ; abbf: 20 c7 95     ..
    ldy #&31 ; '1'                                                    ; abc2: a0 31       .1
    lda (net_rx_ptr),y                                                ; abc4: b1 9c       ..
    beq cabcc                                                         ; abc6: f0 04       ..
    cmp #3                                                            ; abc8: c9 03       ..
    bne cabe1                                                         ; abca: d0 15       ..
; &abcc referenced 1 time by &abc6
.cabcc
    pla                                                               ; abcc: 68          h
    pla                                                               ; abcd: 68          h
    sta l00d0                                                         ; abce: 85 d0       ..
    lda #0                                                            ; abd0: a9 00       ..
    jsr append_byte_to_rxbuf                                          ; abd2: 20 00 ab     ..
    jsr cab24                                                         ; abd5: 20 24 ab     $.
    lda ws_0d6a                                                       ; abd8: ad 6a 0d    .j.
    and #&f0                                                          ; abdb: 29 f0       ).
    sta ws_0d6a                                                       ; abdd: 8d 6a 0d    .j.
    rts                                                               ; abe0: 60          `

; &abe1 referenced 1 time by &abca
.cabe1
    tax                                                               ; abe1: aa          .
    pla                                                               ; abe2: 68          h
    sec                                                               ; abe3: 38          8
    sbc #1                                                            ; abe4: e9 01       ..
    bne cab72                                                         ; abe6: d0 8a       ..
    cpx #1                                                            ; abe8: e0 01       ..
    bne cabfe                                                         ; abea: d0 12       ..
; &abec referenced 1 time by &afd5
.err_printer_busy
    lda #&a6                                                          ; abec: a9 a6       ..
    jsr error_inline_log                                              ; abee: 20 bb 96     ..
    equs "Printer busy", 0                                            ; abf1: 50 72 69... Pri

; &abfe referenced 1 time by &abea
.cabfe
    lda #&a7                                                          ; abfe: a9 a7       ..
    jsr error_inline_log                                              ; ac00: 20 bb 96     ..
    equs "Printer jammed", 0                                          ; ac03: 50 72 69... Pri

; &ac12 referenced 3 times by &94f5, &ab5c, &b946
.send_disconnect_reply
    stx net_tx_ptr                                                    ; ac12: 86 9a       ..
    sty net_tx_ptr_hi                                                 ; ac14: 84 9b       ..
    pha                                                               ; ac16: 48          H
    ora #0                                                            ; ac17: 09 00       ..
    beq cac38                                                         ; ac19: f0 1d       ..
    ldx #&ff                                                          ; ac1b: a2 ff       ..
    tay                                                               ; ac1d: a8          .
; &ac1e referenced 2 times by &ac27, &ac31
.cac1e
    tya                                                               ; ac1e: 98          .
    inx                                                               ; ac1f: e8          .
    cmp l1030,x                                                       ; ac20: dd 30 10    .0.
    beq cac2d                                                         ; ac23: f0 08       ..
    cpx #&0f                                                          ; ac25: e0 0f       ..
    bne cac1e                                                         ; ac27: d0 f5       ..
    lda #0                                                            ; ac29: a9 00       ..
    beq cac38                                                         ; ac2b: f0 0b       ..             ; ALWAYS branch

; &ac2d referenced 1 time by &ac23
.cac2d
    tay                                                               ; ac2d: a8          .
    jsr match_station_net                                             ; ac2e: 20 7a b5     z.
    bne cac1e                                                         ; ac31: d0 eb       ..
    lda l1060,x                                                       ; ac33: bd 60 10    .`.
    and #1                                                            ; ac36: 29 01       ).
; &ac38 referenced 2 times by &ac19, &ac2b
.cac38
    ldy #0                                                            ; ac38: a0 00       ..
    ora (net_tx_ptr),y                                                ; ac3a: 11 9a       ..
    pha                                                               ; ac3c: 48          H
    sta (net_tx_ptr),y                                                ; ac3d: 91 9a       ..
    jsr send_net_packet                                               ; ac3f: 20 2a 98     *.
    lda #&ff                                                          ; ac42: a9 ff       ..
    ldy #8                                                            ; ac44: a0 08       ..
    sta (net_tx_ptr),y                                                ; ac46: 91 9a       ..
    iny                                                               ; ac48: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; ac49: 91 9a       ..
    pla                                                               ; ac4b: 68          h
    tax                                                               ; ac4c: aa          .
    ldy #&d1                                                          ; ac4d: a0 d1       ..
    pla                                                               ; ac4f: 68          h
    pha                                                               ; ac50: 48          H
    beq cac55                                                         ; ac51: f0 02       ..
    ldy #&90                                                          ; ac53: a0 90       ..
; &ac55 referenced 1 time by &ac51
.cac55
    tya                                                               ; ac55: 98          .
    ldy #1                                                            ; ac56: a0 01       ..
    sta (net_tx_ptr),y                                                ; ac58: 91 9a       ..
    txa                                                               ; ac5a: 8a          .
    dey                                                               ; ac5b: 88          .              ; Y=&00
    pha                                                               ; ac5c: 48          H
; &ac5d referenced 1 time by &ac69
.loop_cac5d
    lda #&7f                                                          ; ac5d: a9 7f       ..
    sta (net_tx_ptr),y                                                ; ac5f: 91 9a       ..
    jsr wait_net_tx_ack                                               ; ac61: 20 c7 95     ..
    pla                                                               ; ac64: 68          h
    pha                                                               ; ac65: 48          H
    eor (net_tx_ptr),y                                                ; ac66: 51 9a       Q.
    ror a                                                             ; ac68: 6a          j
    bcs loop_cac5d                                                    ; ac69: b0 f2       ..
    pla                                                               ; ac6b: 68          h
    pla                                                               ; ac6c: 68          h
    rts                                                               ; ac6d: 60          `

; &ac6e referenced 1 time by &ab77
.tx_econet_txcb_template
    equb &80, &9f, 0, 0, &43, &8e, &ff, &ff, &4b, &8e, &ff, &ff       ; ac6e: 80 9f 00... ...
; &ac7a referenced 1 time by &ab96
.rx_palette_txcb_template
    equb &7f, &9e, &fd, &fd, &31, &fc, &ff, &ff, &34, &fc, &ff, &ff   ; ac7a: 7f 9e fd... ...

    lda l00ad                                                         ; ac86: a5 ad       ..
    pha                                                               ; ac88: 48          H
    lda #&e9                                                          ; ac89: a9 e9       ..
    sta nfs_workspace                                                 ; ac8b: 85 9e       ..
    ldy #0                                                            ; ac8d: a0 00       ..
    sty l00ad                                                         ; ac8f: 84 ad       ..
    lda vdu_screen_mode                                               ; ac91: ad 50 03    .P.
    sta (nfs_workspace),y                                             ; ac94: 91 9e       ..
    inc nfs_workspace                                                 ; ac96: e6 9e       ..
    lda l0351                                                         ; ac98: ad 51 03    .Q.
    pha                                                               ; ac9b: 48          H
    tya                                                               ; ac9c: 98          .              ; A=&00
; &ac9d referenced 1 time by &acbc
.loop_cac9d
    sta (nfs_workspace),y                                             ; ac9d: 91 9e       ..
    ldx nfs_workspace                                                 ; ac9f: a6 9e       ..
    ldy nfs_workspace_hi                                              ; aca1: a4 9f       ..
    lda #osword_read_palette                                          ; aca3: a9 0b       ..
    jsr osword                                                        ; aca5: 20 f1 ff     ..            ; Read palette
    pla                                                               ; aca8: 68          h
    ldy #0                                                            ; aca9: a0 00       ..
    sta (nfs_workspace),y                                             ; acab: 91 9e       ..
    iny                                                               ; acad: c8          .              ; Y=&01
    lda (nfs_workspace),y                                             ; acae: b1 9e       ..
    pha                                                               ; acb0: 48          H
    ldx nfs_workspace                                                 ; acb1: a6 9e       ..
    inc nfs_workspace                                                 ; acb3: e6 9e       ..
    inc l00ad                                                         ; acb5: e6 ad       ..
    dey                                                               ; acb7: 88          .              ; Y=&00
    lda l00ad                                                         ; acb8: a5 ad       ..
    cpx #&f9                                                          ; acba: e0 f9       ..
    bne loop_cac9d                                                    ; acbc: d0 df       ..
    pla                                                               ; acbe: 68          h
    sty l00ad                                                         ; acbf: 84 ad       ..
    inc nfs_workspace                                                 ; acc1: e6 9e       ..
    jsr serialise_palette_entry                                       ; acc3: 20 d2 ac     ..
    inc nfs_workspace                                                 ; acc6: e6 9e       ..
    pla                                                               ; acc8: 68          h
    sta l00ad                                                         ; acc9: 85 ad       ..
; &accb referenced 4 times by &9570, &9598, &95bf, &a62e
.commit_state_byte
    lda ws_0d69                                                       ; accb: ad 69 0d    .i.
    sta ws_0d68                                                       ; acce: 8d 68 0d    .h.
    rts                                                               ; acd1: 60          `

; &acd2 referenced 1 time by &acc3
.serialise_palette_entry
    lda l0355                                                         ; acd2: ad 55 03    .U.
    sta (nfs_workspace),y                                             ; acd5: 91 9e       ..
    ldx l0355                                                         ; acd7: ae 55 03    .U.
    jsr read_osbyte_to_ws                                             ; acda: 20 e7 ac     ..
    inc nfs_workspace                                                 ; acdd: e6 9e       ..
    tya                                                               ; acdf: 98          .
    sta (nfs_workspace,x)                                             ; ace0: 81 9e       ..
    jsr read_osbyte_to_ws_x0                                          ; ace2: 20 e5 ac     ..
; &ace5 referenced 1 time by &ace2
.read_osbyte_to_ws_x0
    ldx #0                                                            ; ace5: a2 00       ..
; &ace7 referenced 1 time by &acda
.read_osbyte_to_ws
    ldy l00ad                                                         ; ace7: a4 ad       ..
    inc l00ad                                                         ; ace9: e6 ad       ..
    inc nfs_workspace                                                 ; aceb: e6 9e       ..
    lda osbyte_mode_read_codes,y                                      ; aced: b9 fb ac    ...
    ldy #&ff                                                          ; acf0: a0 ff       ..
    jsr osbyte                                                        ; acf2: 20 f4 ff     ..
    txa                                                               ; acf5: 8a          .
    ldx #0                                                            ; acf6: a2 00       ..
    sta (nfs_workspace,x)                                             ; acf8: 81 9e       ..
    rts                                                               ; acfa: 60          `

; &acfb referenced 1 time by &aced
.osbyte_mode_read_codes
    equb &85, &c2, &c3                                                ; acfb: 85 c2 c3    ...

; ***************************************************************************************
; *CDir command.
; Creates a new directory on the file
; server.
; ***************************************************************************************
.cmd_cdir
    tya                                                               ; acfe: 98          .              ; Save command line offset
    pha                                                               ; acff: 48          H              ; Push onto stack
    jsr mask_owner_access                                             ; ad00: 20 12 af     ..            ; Set owner-only access mask
    jsr skip_to_next_arg                                              ; ad03: 20 a1 af     ..            ; Skip to optional size argument
    cmp #&0d                                                          ; ad06: c9 0d       ..             ; End of line?
    bne cad0e                                                         ; ad08: d0 04       ..             ; No: parse size argument
    ldx #2                                                            ; ad0a: a2 02       ..             ; Default allocation size index = 2
    bne cad1d                                                         ; ad0c: d0 0f       ..             ; ALWAYS branch

; &ad0e referenced 1 time by &ad08
.cad0e
    lda #&ff                                                          ; ad0e: a9 ff       ..             ; A=&FF: mark as decimal parse
    sta fs_work_4                                                     ; ad10: 85 b4       ..             ; Store decimal parse flag
    jsr parse_addr_arg                                                ; ad12: 20 5a 91     Z.            ; Parse numeric size argument
    ldx #&1b                                                          ; ad15: a2 1b       ..             ; X=&1B: top of 27-entry size table
; &ad17 referenced 1 time by &ad1b
.loop_cad17
    dex                                                               ; ad17: ca          .              ; Try next lower index
    cmp cdir_alloc_size_table,x                                       ; ad18: dd 31 ad    .1.            ; Compare size with threshold
    bcc loop_cad17                                                    ; ad1b: 90 fa       ..             ; A < threshold: keep searching
; &ad1d referenced 1 time by &ad0c
.cad1d
    stx l0f05                                                         ; ad1d: 8e 05 0f    ...            ; Store allocation size index
    pla                                                               ; ad20: 68          h              ; Restore command line offset
    tay                                                               ; ad21: a8          .              ; Transfer to Y
    jsr save_ptr_to_os_text                                           ; ad22: 20 95 af     ..            ; Save text pointer for filename parse
    jsr parse_filename_arg                                            ; ad25: 20 82 ae     ..            ; Parse directory name argument
    ldx #1                                                            ; ad28: a2 01       ..             ; X=1: one argument to copy
    jsr copy_arg_to_buf                                               ; ad2a: 20 f2 ae     ..            ; Copy directory name to TX buffer
    ldy #&1b                                                          ; ad2d: a0 1b       ..             ; Y=&1B: *CDir FS command code
.cdir_dispatch_col
cdir_alloc_size_table = cdir_dispatch_col+2
    jmp save_net_tx_cb                                                ; ad2f: 4c 99 94    L..            ; Send command to file server

; &ad31 referenced 1 time by &ad18
    equb 0, &0a, &14, &1d                                             ; ad32: 00 0a 14... ...
    equs "'1;EOXblv"                                                  ; ad36: 27 31 3b... '1;
    equb &80, &8a, &94, &9d, &a7, &b1, &bb, &c5, &cf, &d8, &e2, &ec   ; ad3f: 80 8a 94... ...
    equb &f6, &ff                                                     ; ad4b: f6 ff       ..

; ***************************************************************************************
; *LCat command.
; Lists catalogue from the library
; directory. Falls through to *Ex.
; ***************************************************************************************
.cmd_lcat
    ror l1071                                                         ; ad4d: 6e 71 10    nq.            ; Rotate carry into lib flag bit 7
    sec                                                               ; ad50: 38          8              ; Set carry (= library directory)
    bcs cat_set_lib_flag                                              ; ad51: b0 24       .$             ; ALWAYS branch

; ***************************************************************************************
; *LEx command.
; Examines the library directory.
; Falls through to *Ex.
; ***************************************************************************************
.cmd_lex
    ror l1071                                                         ; ad53: 6e 71 10    nq.            ; Rotate carry into lib flag bit 7
    sec                                                               ; ad56: 38          8              ; Set carry (= library directory)
    bcs ex_set_lib_flag                                               ; ad57: b0 04       ..             ; ALWAYS branch

; ***************************************************************************************
; *Ex command.
; Examines a directory, listing files
; with attributes. *LCat and *LEx
; fall through to this handler.
; ***************************************************************************************
.cmd_ex
    ror l1071                                                         ; ad59: 6e 71 10    nq.            ; Rotate carry into lib flag bit 7
    clc                                                               ; ad5c: 18          .              ; Clear carry (= current directory)
; &ad5d referenced 1 time by &ad57
.ex_set_lib_flag
    rol l1071                                                         ; ad5d: 2e 71 10    .q.            ; Rotate carry back, clearing bit 7
    lda #&ff                                                          ; ad60: a9 ff       ..             ; A=&FF: initial column counter
    sta fs_spool_handle                                               ; ad62: 85 ba       ..             ; Store column counter
    lda #1                                                            ; ad64: a9 01       ..             ; One entry per line (Ex format)
    sta fs_work_7                                                     ; ad66: 85 b7       ..             ; Store entries per page
    lda #3                                                            ; ad68: a9 03       ..             ; FS command code 3: Examine
    sta fs_work_5                                                     ; ad6a: 85 b5       ..             ; Store command code
    bne cad84                                                         ; ad6c: d0 16       ..             ; ALWAYS branch

    jsr set_xfer_params                                               ; ad6e: 20 81 92     ..            ; Set transfer parameters
    ldy #0                                                            ; ad71: a0 00       ..             ; Y=0: start from entry 0
    ror l1071                                                         ; ad73: 6e 71 10    nq.            ; Rotate carry into lib flag
    clc                                                               ; ad76: 18          .              ; Clear carry (= current directory)
; &ad77 referenced 1 time by &ad51
.cat_set_lib_flag
    rol l1071                                                         ; ad77: 2e 71 10    .q.            ; Rotate carry back, clearing bit 7
    lda #3                                                            ; ad7a: a9 03       ..             ; Three entries per column (Cat)
    sta fs_spool_handle                                               ; ad7c: 85 ba       ..             ; Store column counter
    sta fs_work_7                                                     ; ad7e: 85 b7       ..             ; Store entries per page
    lda #&0b                                                          ; ad80: a9 0b       ..             ; FS command code &0B: Catalogue
    sta fs_work_5                                                     ; ad82: 85 b5       ..             ; Store command code
; &ad84 referenced 1 time by &ad6c
.cad84
    jsr save_ptr_to_os_text                                           ; ad84: 20 95 af     ..            ; Save text pointer
    lda #&ff                                                          ; ad87: a9 ff       ..             ; A=&FF: enable escape checking
    sta escapable                                                     ; ad89: 85 97       ..             ; Set escapable flag
    lda #6                                                            ; ad8b: a9 06       ..             ; Command code 6
    sta l0f05                                                         ; ad8d: 8d 05 0f    ...            ; Store in TX buffer
    jsr parse_filename_arg                                            ; ad90: 20 82 ae     ..            ; Parse directory argument
    ldx #1                                                            ; ad93: a2 01       ..             ; X=1: offset in buffer
    jsr copy_arg_to_buf                                               ; ad95: 20 f2 ae     ..            ; Copy argument to TX buffer
    lda l1071                                                         ; ad98: ad 71 10    .q.            ; Get library/FS flags
    lsr a                                                             ; ad9b: 4a          J              ; Shift bit 0 to carry
    bcc cada0                                                         ; ad9c: 90 02       ..             ; Bit 0 clear: skip
    ora #&40 ; '@'                                                    ; ad9e: 09 40       .@             ; Set bit 6 (owner access flag)
; &ada0 referenced 1 time by &ad9c
.cada0
    rol a                                                             ; ada0: 2a          *              ; Rotate back
    sta l1071                                                         ; ada1: 8d 71 10    .q.            ; Store modified flags
    ldy #&12                                                          ; ada4: a0 12       ..             ; Y=&12: FS command for examine
    jsr save_net_tx_cb                                                ; ada6: 20 99 94     ..            ; Send request to file server
    ldx #3                                                            ; ada9: a2 03       ..             ; X=3: offset to directory title
    jsr print_10_chars                                                ; adab: 20 70 ae     p.            ; Print directory title (10 chars)
    jsr print_inline                                                  ; adae: 20 31 91     1.            ; Print '('
    equs "("                                                          ; adb1: 28          (

    lda l0f13                                                         ; adb2: ad 13 0f    ...            ; Get cycle number
    jsr print_decimal_3dig                                            ; adb5: 20 68 af     h.            ; Print as 3-digit decimal
    jsr print_inline                                                  ; adb8: 20 31 91     1.            ; Print ')     '
    equs ")     "                                                     ; adbb: 29 20 20... )

    ldy l0f12                                                         ; adc1: ac 12 0f    ...            ; Get owner/public flag
    bne cadd1                                                         ; adc4: d0 0b       ..             ; Non-zero: public access
    jsr print_inline                                                  ; adc6: 20 31 91     1.            ; Print 'Owner' + CR
    equs "Owner", &0d                                                 ; adc9: 4f 77 6e... Own

    bne caddb                                                         ; adcf: d0 0a       ..             ; Skip public; ALWAYS branch
; &add1 referenced 1 time by &adc4
.cadd1
    jsr print_inline                                                  ; add1: 20 31 91     1.            ; Print 'Public' + CR
    equs "Public", &0d                                                ; add4: 50 75 62... Pub

; &addb referenced 1 time by &adcf
.caddb
    lda l1071                                                         ; addb: ad 71 10    .q.            ; Get flags
    pha                                                               ; adde: 48          H              ; Save flags
    jsr mask_owner_access                                             ; addf: 20 12 af     ..            ; Mask owner access bits
    ldy #&15                                                          ; ade2: a0 15       ..             ; Y=&15: FS command for dir info
    jsr save_net_tx_cb                                                ; ade4: 20 99 94     ..            ; Send request to file server
    inx                                                               ; ade7: e8          .              ; Advance X past header
    ldy #&10                                                          ; ade8: a0 10       ..             ; Y=&10: print 16 chars
    jsr cae72                                                         ; adea: 20 72 ae     r.            ; Print file entry
    jsr print_inline                                                  ; aded: 20 31 91     1.            ; Print '    Option '
    equs "    Option "                                                ; adf0: 20 20 20...

    lda l0e05                                                         ; adfb: ad 05 0e    ...            ; Get option byte
    tax                                                               ; adfe: aa          .              ; Transfer to X for table lookup
    jsr print_hex_byte                                                ; adff: 20 1b 91     ..            ; Print option as hex
    jsr print_inline                                                  ; ae02: 20 31 91     1.            ; Print ' ('
    equs " ("                                                         ; ae05: 20 28        (

    ldy caee9,x                                                       ; ae07: bc e9 ae    ...            ; Index into option string table
; &ae0a referenced 1 time by &ae13
.loop_cae0a
    lda roff_off_string,y                                             ; ae0a: b9 ed ae    ...            ; Get option name character
    bmi cae15                                                         ; ae0d: 30 06       0.             ; High bit set: end of string
    jsr osasci                                                        ; ae0f: 20 e3 ff     ..            ; Write character
    iny                                                               ; ae12: c8          .              ; Next character
    bne loop_cae0a                                                    ; ae13: d0 f5       ..             ; Loop; ALWAYS branch
; &ae15 referenced 1 time by &ae0d
.cae15
    jsr print_inline                                                  ; ae15: 20 31 91     1.            ; Print ')' + CR + 'Dir. '
    equs ")", &0d, "Dir. "                                            ; ae18: 29 0d 44... ).D

    ldx #&11                                                          ; ae1f: a2 11       ..             ; Offset &11: directory name
    jsr print_10_chars                                                ; ae21: 20 70 ae     p.            ; Print directory name (10 chars)
    jsr print_inline                                                  ; ae24: 20 31 91     1.            ; Print '     Lib. '
    equs "     Lib. "                                                 ; ae27: 20 20 20...

    ldx #&1b                                                          ; ae31: a2 1b       ..             ; Offset &1B: library name
    jsr print_10_chars                                                ; ae33: 20 70 ae     p.            ; Print library name (10 chars)
    jsr osnewl                                                        ; ae36: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    pla                                                               ; ae39: 68          h              ; Restore flags
    sta l1071                                                         ; ae3a: 8d 71 10    .q.            ; Store restored flags
; &ae3d referenced 1 time by &ae6e
.cae3d
    sty l0f06                                                         ; ae3d: 8c 06 0f    ...            ; Store entry count
    sty fs_work_4                                                     ; ae40: 84 b4       ..             ; Also store in work_4
    ldx fs_work_5                                                     ; ae42: a6 b5       ..             ; Get command code
    stx l0f07                                                         ; ae44: 8e 07 0f    ...            ; Store in buffer
    ldx fs_work_7                                                     ; ae47: a6 b7       ..             ; Get entries per page
    stx l0f05                                                         ; ae49: 8e 05 0f    ...            ; Store in buffer
    ldx #3                                                            ; ae4c: a2 03       ..             ; X=3: buffer offset
    jsr copy_arg_to_buf                                               ; ae4e: 20 f2 ae     ..            ; Copy argument to buffer
    ldy #3                                                            ; ae51: a0 03       ..             ; Y=3: FS command for examine/cat
    jsr save_net_tx_cb                                                ; ae53: 20 99 94     ..            ; Send request to file server
    inx                                                               ; ae56: e8          .              ; Advance past header
    lda l0f05                                                         ; ae57: ad 05 0f    ...            ; Get number of entries returned
    beq cae7d                                                         ; ae5a: f0 21       .!             ; Zero: no more entries
    pha                                                               ; ae5c: 48          H              ; Save entry count
; &ae5d referenced 1 time by &ae61
.loop_cae5d
    iny                                                               ; ae5d: c8          .              ; Advance Y
    lda l0f05,y                                                       ; ae5e: b9 05 0f    ...            ; Get entry data byte
    bpl loop_cae5d                                                    ; ae61: 10 fa       ..             ; Bit 7 clear: more data
    sta l0f04,y                                                       ; ae63: 99 04 0f    ...            ; Store terminator byte
    jsr ex_print_col_sep                                              ; ae66: 20 27 af     '.            ; Print entry with column separator
    pla                                                               ; ae69: 68          h              ; Restore entry count
    clc                                                               ; ae6a: 18          .              ; Clear carry for addition
    adc fs_work_4                                                     ; ae6b: 65 b4       e.             ; Add entries processed
    tay                                                               ; ae6d: a8          .              ; Transfer to Y
    bne cae3d                                                         ; ae6e: d0 cd       ..             ; More entries: loop
; &ae70 referenced 3 times by &adab, &ae21, &ae33
.print_10_chars
    ldy #&0a                                                          ; ae70: a0 0a       ..             ; Y=10: characters to print
; &ae72 referenced 2 times by &adea, &ae7a
.cae72
    lda l0f05,x                                                       ; ae72: bd 05 0f    ...            ; Get character from buffer
    jsr osasci                                                        ; ae75: 20 e3 ff     ..            ; Write character
    inx                                                               ; ae78: e8          .              ; Next buffer position
    dey                                                               ; ae79: 88          .              ; Decrement count
    bne cae72                                                         ; ae7a: d0 f6       ..             ; Loop until 10 printed
    rts                                                               ; ae7c: 60          `              ; Return

; &ae7d referenced 1 time by &ae5a
.cae7d
    jmp osnewl                                                        ; ae7d: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &ae80 referenced 2 times by &9cf8, &a1af
.parse_cmd_arg_y0
    ldy #0                                                            ; ae80: a0 00       ..             ; Y=0: start of command line
; &ae82 referenced 4 times by &ad25, &ad90, &af57, &b347
.parse_filename_arg
    jsr gsread_to_buf                                                 ; ae82: 20 ff 98     ..            ; Read string to buffer via GSREAD
; &ae85 referenced 4 times by &92da, &9382, &93bb, &992a
.parse_access_prefix
    lda l0e30                                                         ; ae85: ad 30 0e    .0.            ; Get first parsed character
    eor #&26 ; '&'                                                    ; ae88: 49 26       I&             ; Is it '&'?
    bne caed0                                                         ; ae8a: d0 44       .D             ; No: check for ':' prefix
    lda l1071                                                         ; ae8c: ad 71 10    .q.            ; Get flags
    ora #&40 ; '@'                                                    ; ae8f: 09 40       .@             ; Set FS selection flag (bit 6)
    sta l1071                                                         ; ae91: 8d 71 10    .q.            ; Store updated flags
    jsr strip_token_prefix                                            ; ae94: 20 a5 ae     ..            ; Remove '&' prefix character
    lda l0e30                                                         ; ae97: ad 30 0e    .0.            ; Get next character
    eor #&2e ; '.'                                                    ; ae9a: 49 2e       I.             ; Is it '.'?
    bne caec9                                                         ; ae9c: d0 2b       .+             ; No: check for '#'
    lda l0e31                                                         ; ae9e: ad 31 0e    .1.            ; Get char after '.'
    eor #&0d                                                          ; aea1: 49 0d       I.             ; Is it CR (end of line)?
    beq caecd                                                         ; aea3: f0 28       .(             ; Yes: '&.' + CR only = bad filename
; &aea5 referenced 5 times by &9308, &93a2, &93a8, &ae94, &aee7
.strip_token_prefix
    txa                                                               ; aea5: 8a          .              ; Save X
    pha                                                               ; aea6: 48          H              ; Push X
    ldx #&ff                                                          ; aea7: a2 ff       ..             ; X=&FF, will increment to 0
; &aea9 referenced 1 time by &aeb2
.loop_caea9
    inx                                                               ; aea9: e8          .              ; Increment X
    lda l0e31,x                                                       ; aeaa: bd 31 0e    .1.            ; Get character at offset+1
    sta l0e30,x                                                       ; aead: 9d 30 0e    .0.            ; Store at offset (shift left)
    eor #&0d                                                          ; aeb0: 49 0d       I.             ; Is it CR (end of line)?
    bne loop_caea9                                                    ; aeb2: d0 f5       ..             ; No: continue shifting
    txa                                                               ; aeb4: 8a          .              ; Get shifted string length
    beq caec6                                                         ; aeb5: f0 0f       ..             ; Zero length: skip trailing trim
; &aeb7 referenced 1 time by &aec4
.loop_caeb7
    lda l0e2f,x                                                       ; aeb7: bd 2f 0e    ./.            ; Get character at end of string
    eor #&20 ; ' '                                                    ; aeba: 49 20       I              ; Is it a space?
    bne caec6                                                         ; aebc: d0 08       ..             ; No: done trimming
    lda #&0d                                                          ; aebe: a9 0d       ..             ; Replace trailing space with CR
    sta l0e2f,x                                                       ; aec0: 9d 2f 0e    ./.            ; Store CR
    dex                                                               ; aec3: ca          .              ; Move back
    bne loop_caeb7                                                    ; aec4: d0 f1       ..             ; Loop while more trailing spaces
; &aec6 referenced 2 times by &aeb5, &aebc
.caec6
    pla                                                               ; aec6: 68          h              ; Restore X
    tax                                                               ; aec7: aa          .              ; Transfer back to X
; &aec8 referenced 3 times by &aecb, &aed2, &aedd
.return_27
    rts                                                               ; aec8: 60          `              ; Return

; &aec9 referenced 1 time by &ae9c
.caec9
    eor #&23 ; '#'                                                    ; aec9: 49 23       I#             ; Is it '#'?
    beq return_27                                                     ; aecb: f0 fb       ..             ; Yes: '#' prefix accepted
; &aecd referenced 1 time by &aea3
.caecd
    jmp error_bad_filename                                            ; aecd: 4c e6 92    L..            ; Bad filename error

; &aed0 referenced 1 time by &ae8a
.caed0
    eor #&1c                                                          ; aed0: 49 1c       I.             ; Check for ':' prefix
    bne return_27                                                     ; aed2: d0 f4       ..             ; Neither '&' nor ':': no prefix
    lda l0e32                                                         ; aed4: ad 32 0e    .2.            ; Get character after ':'
    eor #&2e ; '.'                                                    ; aed7: 49 2e       I.             ; Is it '.'?
    beq caedf                                                         ; aed9: f0 04       ..             ; Yes: ':.' qualified prefix
    eor #&23 ; '#'                                                    ; aedb: 49 23       I#             ; Is it CR (end of line)?
    bne return_27                                                     ; aedd: d0 e9       ..             ; No: no FS prefix, return
; &aedf referenced 1 time by &aed9
.caedf
    lda l1071                                                         ; aedf: ad 71 10    .q.            ; Get flags
    ora #&40 ; '@'                                                    ; aee2: 09 40       .@             ; Set FS selection flag (bit 6)
    sta l1071                                                         ; aee4: 8d 71 10    .q.            ; Store updated flags
    bne strip_token_prefix                                            ; aee7: d0 bc       ..             ; ALWAYS branch

; &aee9 referenced 1 time by &ae07
.caee9
    brk                                                               ; aee9: 00          .

    equs "!.U"                                                        ; aeea: 21 2e 55    !.U
; &aeed referenced 1 time by &ae0a
.roff_off_string
    equs "Off"                                                        ; aeed: 4f 66 66    Off

; &aef0 referenced 6 times by &8db1, &8e0a, &9938, &9b2a, &a281, &af5a
.copy_arg_to_buf_x0
    ldx #0                                                            ; aef0: a2 00       ..             ; X=0: start of buffer
; &aef2 referenced 10 times by &99ea, &9b23, &9b46, &9cfd, &a1b4, &a1e1, &ad2a, &ad95, &ae4e, &b35c
.copy_arg_to_buf
    ldy #0                                                            ; aef2: a0 00       ..             ; Y=0: start of argument
; &aef4 referenced 3 times by &8dac, &940a, &9440
.copy_arg_validated
    sec                                                               ; aef4: 38          8              ; Set carry: enable '&' validation
; &aef5 referenced 1 time by &af0b
.loop_caef5
    lda (fs_crc_lo),y                                                 ; aef5: b1 be       ..             ; Get character from command line
    sta l0f05,x                                                       ; aef7: 9d 05 0f    ...            ; Store in TX buffer
    bcc caf07                                                         ; aefa: 90 0b       ..             ; Carry clear: skip validation
    cmp #&21 ; '!'                                                    ; aefc: c9 21       .!             ; Is it '!' or above?
    eor #&26 ; '&'                                                    ; aefe: 49 26       I&             ; Is it '&'?
    bne caf05                                                         ; af00: d0 03       ..             ; No: continue copying
    jmp error_bad_filename                                            ; af02: 4c e6 92    L..            ; '&' in filename: bad filename

; &af05 referenced 1 time by &af00
.caf05
    eor #&26 ; '&'                                                    ; af05: 49 26       I&             ; Restore A (undo '&' EOR)
; &af07 referenced 1 time by &aefa
.caf07
    inx                                                               ; af07: e8          .              ; Advance buffer position
    iny                                                               ; af08: c8          .              ; Advance source position
    eor #&0d                                                          ; af09: 49 0d       I.             ; Is it CR (end of line)?
    bne loop_caef5                                                    ; af0b: d0 e8       ..             ; No: continue copying
; &af0d referenced 1 time by &af23
.return_28
    rts                                                               ; af0d: 60          `              ; Return

    equs "Load"                                                       ; af0e: 4c 6f 61... Loa

; &af12 referenced 13 times by &8e25, &937c, &93b6, &9927, &9d49, &9e2a, &a1ac, &a238, &a242, &a8db, &ad00, &addf, &b33d
.mask_owner_access
    lda l1071                                                         ; af12: ad 71 10    .q.            ; Get flags
    and #&1f                                                          ; af15: 29 1f       ).             ; Mask to low 5 bits only
    sta l1071                                                         ; af17: 8d 71 10    .q.            ; Store masked flags
    rts                                                               ; af1a: 60          `              ; Return

    equs "Run"                                                        ; af1b: 52 75 6e    Run

    ldx #0                                                            ; af1e: a2 00       ..             ; X=0: start from first entry
; &af20 referenced 1 time by &af40
.caf20
    lda l0f05,x                                                       ; af20: bd 05 0f    ...            ; Get entry byte from buffer
    bmi return_28                                                     ; af23: 30 e8       0.             ; High bit set: end of entries
    bne caf3c                                                         ; af25: d0 15       ..             ; Non-zero: printable character
; &af27 referenced 1 time by &ae66
.ex_print_col_sep
    ldy fs_spool_handle                                               ; af27: a4 ba       ..             ; Get column counter
    bmi caf3a                                                         ; af29: 30 0f       0.             ; Negative: newline mode (Ex)
    iny                                                               ; af2b: c8          .              ; Increment column counter
    tya                                                               ; af2c: 98          .              ; Transfer to A
    and #3                                                            ; af2d: 29 03       ).             ; Modulo 4 (Cat: 3 per row)
    sta fs_spool_handle                                               ; af2f: 85 ba       ..             ; Store updated counter
    beq caf3a                                                         ; af31: f0 07       ..             ; Zero: row full, print newline
    jsr print_inline                                                  ; af33: 20 31 91     1.            ; Print '  ' column separator
    equs "  "                                                         ; af36: 20 20

    bne caf3f                                                         ; af38: d0 05       ..             ; Skip newline; ALWAYS branch
; &af3a referenced 2 times by &af29, &af31
.caf3a
    lda #&0d                                                          ; af3a: a9 0d       ..             ; CR character for newline
; &af3c referenced 1 time by &af25
.caf3c
    jsr osasci                                                        ; af3c: 20 e3 ff     ..            ; Write character 13
; &af3f referenced 1 time by &af38
.caf3f
    inx                                                               ; af3f: e8          .              ; Advance to next entry
    bne caf20                                                         ; af40: d0 de       ..             ; Loop for more entries
    eor l0078                                                         ; af42: 45 78       Ex             ; Embedded string data 'Exec'
    adc l0063                                                         ; af44: 65 63       ec             ; Embedded string data (contd)
; ***************************************************************************************
; *Remove command.
; Deletes a file from the file server.
; ***************************************************************************************
.cmd_remove
    tya                                                               ; af46: 98          .              ; Save command line offset
    pha                                                               ; af47: 48          H              ; Push onto stack
    jsr skip_to_next_arg                                              ; af48: 20 a1 af     ..            ; Skip to check for extra arguments
    cmp #&0d                                                          ; af4b: c9 0d       ..             ; End of line?
    beq caf52                                                         ; af4d: f0 03       ..             ; Yes: single arg, proceed
    jmp error_syntax                                                  ; af4f: 4c 0f a1    L..            ; No: extra args, syntax error

; &af52 referenced 1 time by &af4d
.caf52
    pla                                                               ; af52: 68          h              ; Restore command line offset
    tay                                                               ; af53: a8          .              ; Transfer to Y
    jsr save_ptr_to_os_text                                           ; af54: 20 95 af     ..            ; Save text pointer for parsing
    jsr parse_filename_arg                                            ; af57: 20 82 ae     ..            ; Parse filename argument
    jsr copy_arg_to_buf_x0                                            ; af5a: 20 f0 ae     ..            ; Copy filename to TX buffer
    ldy #&14                                                          ; af5d: a0 14       ..             ; Y=&14: *Delete FS command code
    bit bit_test_ff_pad                                               ; af5f: 2c 7d 94    ,}.            ; Set V flag (via BIT #&FF)
    jmp save_net_tx_cb_vset                                           ; af62: 4c 9a 94    L..            ; Send to FS with V-flag dispatch

; &af65 referenced 1 time by &8ff3
.print_num_no_leading
    bit bit_test_ff_pad                                               ; af65: 2c 7d 94    ,}.            ; Set V (suppress leading zeros)
; &af68 referenced 3 times by &adb5, &b179, &b190
.print_decimal_3dig
    tay                                                               ; af68: a8          .              ; Transfer value to Y (remainder)
    lda #&64 ; 'd'                                                    ; af69: a9 64       .d             ; A=100: hundreds divisor
    jsr print_decimal_digit                                           ; af6b: 20 76 af     v.            ; Print hundreds digit
    lda #&0a                                                          ; af6e: a9 0a       ..             ; A=10: tens divisor
    jsr print_decimal_digit                                           ; af70: 20 76 af     v.            ; Print tens digit
    clv                                                               ; af73: b8          .              ; Clear V (always print units)
    lda #1                                                            ; af74: a9 01       ..             ; A=1: units divisor
; &af76 referenced 2 times by &af6b, &af70
.print_decimal_digit
    sta fs_error_ptr                                                  ; af76: 85 b8       ..             ; Store divisor
    tya                                                               ; af78: 98          .              ; Get remaining value
    ldx #&2f ; '/'                                                    ; af79: a2 2f       ./             ; X='0'-1: digit counter
    sec                                                               ; af7b: 38          8              ; Set carry for subtraction
    php                                                               ; af7c: 08          .              ; Save V flag for leading zero check
; &af7d referenced 1 time by &af80
.loop_caf7d
    inx                                                               ; af7d: e8          .              ; Count quotient digit
    sbc fs_error_ptr                                                  ; af7e: e5 b8       ..             ; Subtract divisor
    bcs loop_caf7d                                                    ; af80: b0 fb       ..             ; No underflow: continue dividing
    adc fs_error_ptr                                                  ; af82: 65 b8       e.             ; Add back divisor (get remainder)
    tay                                                               ; af84: a8          .              ; Remainder to Y for next digit
    txa                                                               ; af85: 8a          .              ; Digit character to A
    plp                                                               ; af86: 28          (              ; Restore V flag
    bvc caf8d                                                         ; af87: 50 04       P.             ; V clear: always print digit
    cmp #&30 ; '0'                                                    ; af89: c9 30       .0             ; V set: is digit '0'?
    beq return_29                                                     ; af8b: f0 07       ..             ; Yes: suppress leading zero
; &af8d referenced 1 time by &af87
.caf8d
    ldx fs_error_ptr                                                  ; af8d: a6 b8       ..             ; Save divisor across OSASCI call
    jsr osasci                                                        ; af8f: 20 e3 ff     ..            ; Write character
    stx fs_error_ptr                                                  ; af92: 86 b8       ..             ; Restore divisor
; &af94 referenced 1 time by &af8b
.return_29
    rts                                                               ; af94: 60          `              ; Return

; &af95 referenced 8 times by &9d4f, &a1a9, &ad22, &ad84, &af54, &b018, &b1f2, &b344
.save_ptr_to_os_text
    pha                                                               ; af95: 48          H              ; Save A
    lda fs_crc_lo                                                     ; af96: a5 be       ..             ; Copy text pointer low byte
    sta os_text_ptr                                                   ; af98: 85 f2       ..             ; To OS text pointer low
    lda fs_crc_hi                                                     ; af9a: a5 bf       ..             ; Copy text pointer high byte
    sta os_text_ptr_hi                                                ; af9c: 85 f3       ..             ; To OS text pointer high
    pla                                                               ; af9e: 68          h              ; Restore A
    rts                                                               ; af9f: 60          `              ; Return

; &afa0 referenced 1 time by &afab
.loop_cafa0
    iny                                                               ; afa0: c8          .              ; Advance past current character
; &afa1 referenced 2 times by &ad03, &af48
.skip_to_next_arg
    lda (fs_crc_lo),y                                                 ; afa1: b1 be       ..             ; Load char from command line
    cmp #&20 ; ' '                                                    ; afa3: c9 20       .              ; Space?
    beq cafad                                                         ; afa5: f0 06       ..             ; Yes: skip trailing spaces
    cmp #&0d                                                          ; afa7: c9 0d       ..             ; CR (end of line)?
    beq return_30                                                     ; afa9: f0 09       ..             ; Yes: return (at end)
    bne loop_cafa0                                                    ; afab: d0 f3       ..             ; ALWAYS branch

; &afad referenced 2 times by &afa5, &afb2
.cafad
    iny                                                               ; afad: c8          .              ; Advance past space
    lda (fs_crc_lo),y                                                 ; afae: b1 be       ..             ; Load next character
    cmp #&20 ; ' '                                                    ; afb0: c9 20       .              ; Still a space?
    beq cafad                                                         ; afb2: f0 f9       ..             ; Yes: skip multiple spaces
; &afb4 referenced 1 time by &afa9
.return_30
    rts                                                               ; afb4: 60          `              ; Return (at next argument)

; &afb5 referenced 2 times by &afdb, &b1ae
.save_ptr_to_spool_buf
    pha                                                               ; afb5: 48          H              ; Save A
    lda fs_crc_lo                                                     ; afb6: a5 be       ..             ; Copy text pointer low byte
    sta fs_options                                                    ; afb8: 85 bb       ..             ; To spool buffer pointer low
    lda fs_crc_hi                                                     ; afba: a5 bf       ..             ; Copy text pointer high byte
    sta fs_block_offset                                               ; afbc: 85 bc       ..             ; To spool buffer pointer high
    pla                                                               ; afbe: 68          h              ; Restore A
    rts                                                               ; afbf: 60          `              ; Return

; &afc0 referenced 2 times by &afd8, &b1a1
.init_spool_drive
    tya                                                               ; afc0: 98          .              ; Save Y
    pha                                                               ; afc1: 48          H              ; Push it
    jsr get_ws_page                                                   ; afc2: 20 ae 8c     ..            ; Get workspace page number
    sta l00af                                                         ; afc5: 85 af       ..             ; Store as spool drive page high
    pla                                                               ; afc7: 68          h              ; Restore Y
    tay                                                               ; afc8: a8          .              ; Transfer to Y
    lda #0                                                            ; afc9: a9 00       ..             ; A=0
    sta l00ae                                                         ; afcb: 85 ae       ..             ; Clear spool drive page low
    rts                                                               ; afcd: 60          `              ; Return

; ***************************************************************************************
; *PS command.
; Lists printer server queue status.
; ***************************************************************************************
.cmd_ps
    lda #1                                                            ; afce: a9 01       ..             ; A=1: check printer ready
    bit ws_0d6a                                                       ; afd0: 2c 6a 0d    ,j.            ; Test printer server workspace flag
    bne cafd8                                                         ; afd3: d0 03       ..             ; Non-zero: printer available
    jmp err_printer_busy                                              ; afd5: 4c ec ab    L..            ; Printer not available: error

; &afd8 referenced 1 time by &afd3
.cafd8
    jsr init_spool_drive                                              ; afd8: 20 c0 af     ..            ; Initialise spool drive
    jsr save_ptr_to_spool_buf                                         ; afdb: 20 b5 af     ..            ; Save pointer to spool buffer
    lda (fs_options),y                                                ; afde: b1 bb       ..             ; Get first argument character
    cmp #&0d                                                          ; afe0: c9 0d       ..             ; End of command line?
    beq cb005                                                         ; afe2: f0 21       .!             ; Yes: no argument given
    clv                                                               ; afe4: b8          .              ; Clear V (= explicit PS name given)
    jsr is_decimal_digit                                              ; afe5: 20 44 92     D.            ; Is first char a decimal digit?
    bcc cb008                                                         ; afe8: 90 1e       ..             ; Yes: station number, skip PS name
    tya                                                               ; afea: 98          .              ; PS name follows
    pha                                                               ; afeb: 48          H              ; Save Y
    jsr load_ps_server_addr                                           ; afec: 20 c6 b0     ..            ; Load PS server address
    pla                                                               ; afef: 68          h              ; Restore Y
    tay                                                               ; aff0: a8          .              ; Back to Y register
    jsr parse_fs_ps_args                                              ; aff1: 20 8f a0     ..            ; Parse FS/PS arguments
    jmp cb095                                                         ; aff4: 4c 95 b0    L..            ; Jump to store station address

; &aff7 referenced 1 time by &8ee0
.copy_ps_data_y1c
    ldy #&1c                                                          ; aff7: a0 1c       ..             ; Start at offset &1C
; &aff9 referenced 1 time by &b1d4
.copy_ps_data
    ldx #&f8                                                          ; aff9: a2 f8       ..             ; X=&F8: offset into template
; &affb referenced 1 time by &b002
.loop_caffb
    lda credits_string_mid,x                                          ; affb: bd 4b 8d    .K.            ; Get template byte
    sta (net_rx_ptr),y                                                ; affe: 91 9c       ..             ; Store in RX buffer
    iny                                                               ; b000: c8          .              ; Next destination offset
    inx                                                               ; b001: e8          .              ; Next source offset
    bne loop_caffb                                                    ; b002: d0 f7       ..             ; Loop until X wraps to 0
    rts                                                               ; b004: 60          `              ; Return

; &b005 referenced 1 time by &afe2
.cb005
    bit bit_test_ff_pad                                               ; b005: 2c 7d 94    ,}.            ; Set V (= no explicit PS name)
; &b008 referenced 1 time by &afe8
.cb008
    sty ws_ptr_hi                                                     ; b008: 84 ac       ..             ; Save command line pointer
    bvs cb038                                                         ; b00a: 70 2c       p,             ; V set: skip PS name parsing
    ldx #6                                                            ; b00c: a2 06       ..             ; Max 6 characters for PS name
    ldy #&1c                                                          ; b00e: a0 1c       ..             ; Buffer offset &1C for PS name
    lda #&20 ; ' '                                                    ; b010: a9 20       .              ; Space character
; &b012 referenced 1 time by &b016
.loop_cb012
    sta (net_rx_ptr),y                                                ; b012: 91 9c       ..             ; Fill buffer with space
    iny                                                               ; b014: c8          .              ; Next position
    dex                                                               ; b015: ca          .              ; Count down
    bne loop_cb012                                                    ; b016: d0 fa       ..             ; Loop until 6 spaces filled
    jsr save_ptr_to_os_text                                           ; b018: 20 95 af     ..            ; Save text pointer
    ldy ws_ptr_hi                                                     ; b01b: a4 ac       ..             ; Restore command line pointer
    jsr gsinit                                                        ; b01d: 20 c2 ff     ..            ; Initialise string reading
    beq cb038                                                         ; b020: f0 16       ..             ; Empty string: skip to send
    ldx #6                                                            ; b022: a2 06       ..             ; Max 6 characters
    sty ws_ptr_hi                                                     ; b024: 84 ac       ..             ; Save updated string pointer
    ldy #&1c                                                          ; b026: a0 1c       ..             ; Buffer offset for PS name
    sty l00ad                                                         ; b028: 84 ad       ..             ; Save buffer position
; &b02a referenced 1 time by &b036
.loop_cb02a
    ldy ws_ptr_hi                                                     ; b02a: a4 ac       ..             ; Restore string pointer
    jsr gsread                                                        ; b02c: 20 c5 ff     ..            ; Read next character
    sty ws_ptr_hi                                                     ; b02f: 84 ac       ..             ; Save updated pointer
    bcs cb038                                                         ; b031: b0 05       ..             ; End of string: go to send
    jsr store_char_uppercase                                          ; b033: 20 db b2     ..            ; Store char uppercased in buffer
    bne loop_cb02a                                                    ; b036: d0 f2       ..             ; Loop for more characters
; &b038 referenced 3 times by &b00a, &b020, &b031
.cb038
    jsr reverse_ps_name_to_tx                                         ; b038: 20 49 b1     I.            ; Copy reversed PS name to TX
    jsr send_net_packet                                               ; b03b: 20 2a 98     *.            ; Send PS status request
    jsr pop_requeue_ps_scan                                           ; b03e: 20 d2 b0     ..            ; Pop and requeue PS scan
    jsr load_ps_server_addr                                           ; b041: 20 c6 b0     ..            ; Load PS server address
    lda #0                                                            ; b044: a9 00       ..             ; A=0
    tax                                                               ; b046: aa          .              ; X=&00
    ldy #&24 ; '$'                                                    ; b047: a0 24       .$             ; Offset &24 in buffer
    sta (net_rx_ptr),y                                                ; b049: 91 9c       ..             ; Clear PS status byte
; &b04b referenced 1 time by &b073
.cb04b
    pla                                                               ; b04b: 68          h              ; Get slot offset from stack
    beq cb075                                                         ; b04c: f0 27       .'             ; Zero: all slots done
    pha                                                               ; b04e: 48          H              ; Save slot offset
    tay                                                               ; b04f: a8          .              ; Transfer to Y
    lda (nfs_workspace),y                                             ; b050: b1 9e       ..             ; Read slot status
    bpl cb06d                                                         ; b052: 10 19       ..             ; Bit 7 clear: slot inactive
    jsr advance_y_by_4                                                ; b054: 20 6d 9a     m.            ; Advance Y by 4 (to status page)
    lda (nfs_workspace),y                                             ; b057: b1 9e       ..             ; Read status page pointer
    sta l00ae                                                         ; b059: 85 ae       ..             ; Store pointer low
    lda (l00ae,x)                                                     ; b05b: a1 ae       ..             ; Read printer status byte
    bne cb06d                                                         ; b05d: d0 0e       ..             ; Non-zero (busy): skip
    dey                                                               ; b05f: 88          .              ; Back to network number
    lda (nfs_workspace),y                                             ; b060: b1 9e       ..             ; Read network number
    sta l00b6                                                         ; b062: 85 b6       ..             ; Store network number
    dey                                                               ; b064: 88          .              ; Back to station number
    lda (nfs_workspace),y                                             ; b065: b1 9e       ..             ; Read station number
    sta fs_work_5                                                     ; b067: 85 b5       ..             ; Store station low
    ldy #&24 ; '$'                                                    ; b069: a0 24       .$             ; Offset &24 in buffer
    sta (net_rx_ptr),y                                                ; b06b: 91 9c       ..             ; Store ready station in buffer
; &b06d referenced 2 times by &b052, &b05d
.cb06d
    pla                                                               ; b06d: 68          h              ; Retrieve slot offset
    tay                                                               ; b06e: a8          .              ; Transfer to Y
    lda #&3f ; '?'                                                    ; b06f: a9 3f       .?             ; Mark slot as processed (&3F)
    sta (nfs_workspace),y                                             ; b071: 91 9e       ..             ; Write marker to workspace
    bne cb04b                                                         ; b073: d0 d6       ..             ; ALWAYS branch

; &b075 referenced 1 time by &b04c
.cb075
    jsr print_printer_server_is                                       ; b075: 20 ab b0     ..            ; Print 'Printer server is '
    ldy #&24 ; '$'                                                    ; b078: a0 24       .$             ; Offset &24: PS station number
    lda (net_rx_ptr),y                                                ; b07a: b1 9c       ..             ; Get stored station number
    bne cb08a                                                         ; b07c: d0 0c       ..             ; Non-zero: server changed
    jsr print_inline                                                  ; b07e: 20 31 91     1.            ; Print 'still '
    equs "still "                                                     ; b081: 73 74 69... sti

    clv                                                               ; b087: b8          .              ; Clear V
    bvc cb092                                                         ; b088: 50 08       P.             ; ALWAYS branch

; &b08a referenced 1 time by &b07c
.cb08a
    jsr print_inline                                                  ; b08a: 20 31 91     1.            ; Print 'now '
    equs "now "                                                       ; b08d: 6e 6f 77... now

    nop                                                               ; b091: ea          .              ; Padding
; &b092 referenced 1 time by &b088
.cb092
    jsr print_fs_info_newline                                         ; b092: 20 86 a0     ..            ; Print FS info and newline
; &b095 referenced 1 time by &aff4
.cb095
    ldy #2                                                            ; b095: a0 02       ..             ; Workspace offset 2
    lda fs_work_5                                                     ; b097: a5 b5       ..             ; Get station low
    sta (nfs_workspace),y                                             ; b099: 91 9e       ..             ; Store in workspace
    iny                                                               ; b09b: c8          .              ; Y=&03
    lda l00b6                                                         ; b09c: a5 b6       ..             ; Get network number
    sta (nfs_workspace),y                                             ; b09e: 91 9e       ..             ; Store in workspace
    rts                                                               ; b0a0: 60          `              ; Return

; &b0a1 referenced 1 time by &a083
.print_file_server_is
    jsr print_inline                                                  ; b0a1: 20 31 91     1.            ; Print 'File'
    equs "File"                                                       ; b0a4: 46 69 6c... Fil

    clv                                                               ; b0a8: b8          .              ; Clear V
    bvc cb0b6                                                         ; b0a9: 50 0b       P.             ; ALWAYS branch

; &b0ab referenced 2 times by &b075, &b21c
.print_printer_server_is
    jsr print_inline                                                  ; b0ab: 20 31 91     1.            ; Print 'Printer'
    equs "Printer"                                                    ; b0ae: 50 72 69... Pri

    nop                                                               ; b0b5: ea          .              ; Padding
; &b0b6 referenced 1 time by &b0a9
.cb0b6
    jsr print_inline                                                  ; b0b6: 20 31 91     1.            ; Print ' server is '
    equs " server is "                                                ; b0b9: 20 73 65...  se

    nop                                                               ; b0c4: ea          .              ; Padding
    rts                                                               ; b0c5: 60          `              ; Return

; &b0c6 referenced 4 times by &afec, &b041, &b1bf, &b21f
.load_ps_server_addr
    ldy #2                                                            ; b0c6: a0 02       ..             ; Workspace offset 2
    lda (nfs_workspace),y                                             ; b0c8: b1 9e       ..             ; Read station low
    sta fs_work_5                                                     ; b0ca: 85 b5       ..             ; Store station low
    iny                                                               ; b0cc: c8          .              ; Y=&03
    lda (nfs_workspace),y                                             ; b0cd: b1 9e       ..             ; Read network number
    sta l00b6                                                         ; b0cf: 85 b6       ..             ; Store network number
    rts                                                               ; b0d1: 60          `              ; Return

; &b0d2 referenced 2 times by &b03e, &b219
.pop_requeue_ps_scan
    pla                                                               ; b0d2: 68          h              ; Pop return address low
    sta osword_flag                                                   ; b0d3: 85 aa       ..             ; Save return address low
    pla                                                               ; b0d5: 68          h              ; Pop return address high
    sta ws_ptr_lo                                                     ; b0d6: 85 ab       ..             ; Save return address high
    lda #0                                                            ; b0d8: a9 00       ..             ; Push 0 as end-of-list marker
    pha                                                               ; b0da: 48          H              ; Push it
    lda #&84                                                          ; b0db: a9 84       ..             ; Start scanning from offset &84
    sta ws_ptr_hi                                                     ; b0dd: 85 ac       ..             ; Store scan position
    lsr l0d61                                                         ; b0df: 4e 61 0d    Na.            ; Shift PS slot flags right
    lda #3                                                            ; b0e2: a9 03       ..             ; Counter: 3 PS slots
; &b0e4 referenced 1 time by &b0f6
.loop_cb0e4
    jsr byte_to_2bit_index                                            ; b0e4: 20 b6 a0     ..            ; Convert to 2-bit workspace index
    bcs cb120                                                         ; b0e7: b0 37       .7             ; Carry set: no more slots
    lsr a                                                             ; b0e9: 4a          J              ; Shift right twice
    lsr a                                                             ; b0ea: 4a          J              ; To get slot offset
    tax                                                               ; b0eb: aa          .              ; Transfer to X
    lda (nfs_workspace),y                                             ; b0ec: b1 9e       ..             ; Read slot status byte
    beq cb120                                                         ; b0ee: f0 30       .0             ; Zero: empty slot, done
    cmp #&3f ; '?'                                                    ; b0f0: c9 3f       .?             ; Is it processed marker (&3F)?
    beq cb0f8                                                         ; b0f2: f0 04       ..             ; Yes: re-initialise this slot
; &b0f4 referenced 1 time by &b11d
.cb0f4
    inx                                                               ; b0f4: e8          .              ; Try next slot
    txa                                                               ; b0f5: 8a          .              ; Transfer slot index to A
    bne loop_cb0e4                                                    ; b0f6: d0 ec       ..             ; Loop for more slots
; &b0f8 referenced 1 time by &b0f2
.cb0f8
    tya                                                               ; b0f8: 98          .              ; Y = workspace offset of slot
    pha                                                               ; b0f9: 48          H              ; Push slot offset for scan list
    lda #&7f                                                          ; b0fa: a9 7f       ..             ; Set active status (&7F)
    sta (nfs_workspace),y                                             ; b0fc: 91 9e       ..             ; Write status byte
    iny                                                               ; b0fe: c8          .              ; Next byte
    lda #&9e                                                          ; b0ff: a9 9e       ..             ; Low byte: workspace page
    sta (nfs_workspace),y                                             ; b101: 91 9e       ..             ; Write workspace pointer low
    lda #0                                                            ; b103: a9 00       ..             ; A=0
    jsr write_two_bytes_inc_y                                         ; b105: 20 41 b1     A.            ; Write two zero bytes + advance Y
    lda ws_ptr_hi                                                     ; b108: a5 ac       ..             ; Get current scan page
    sta (nfs_workspace),y                                             ; b10a: 91 9e       ..             ; Write RX buffer page low
    clc                                                               ; b10c: 18          .              ; Clear carry for addition
    php                                                               ; b10d: 08          .              ; Save processor status
    adc #3                                                            ; b10e: 69 03       i.             ; Advance by 3 pages
    plp                                                               ; b110: 28          (              ; Restore processor status
    sta ws_ptr_hi                                                     ; b111: 85 ac       ..             ; Update scan position
    jsr write_ps_slot_byte_ff                                         ; b113: 20 3a b1     :.            ; Write buffer page + &FF bytes
    lda ws_ptr_hi                                                     ; b116: a5 ac       ..             ; Get updated scan position
    sta (nfs_workspace),y                                             ; b118: 91 9e       ..             ; Write RX buffer page high
.write_ps_slot_hi_link
write_ps_slot_link_addr = write_ps_slot_hi_link+1
    jsr write_ps_slot_byte_ff                                         ; b11a: 20 3a b1     :.            ; Write another page + &FF bytes
; &b11b referenced 1 time by &b2c6
    jmp cb0f4                                                         ; b11d: 4c f4 b0    L..            ; Continue scanning slots

; &b120 referenced 2 times by &b0e7, &b0ee
.cb120
    asl l0d61                                                         ; b120: 0e 61 0d    .a.            ; Shift PS slot flags back
    lda ws_ptr_lo                                                     ; b123: a5 ab       ..             ; Restore return address high
    pha                                                               ; b125: 48          H              ; Push onto stack
    lda osword_flag                                                   ; b126: a5 aa       ..             ; Restore return address low
    pha                                                               ; b128: 48          H              ; Push onto stack
    lda #&0a                                                          ; b129: a9 0a       ..             ; Delay counter: 10
    tay                                                               ; b12b: a8          .              ; Y=&0a
    tax                                                               ; b12c: aa          .              ; X=&0a
    sta fs_work_4                                                     ; b12d: 85 b4       ..             ; Outer loop counter = 10
; &b12f referenced 3 times by &b130, &b133, &b137
.cb12f
    dey                                                               ; b12f: 88          .              ; Decrement Y (inner loop)
    bne cb12f                                                         ; b130: d0 fd       ..             ; Inner loop: 10 iterations
    dex                                                               ; b132: ca          .              ; Decrement X (middle loop)
    bne cb12f                                                         ; b133: d0 fa       ..             ; Middle loop: 10 iterations
    dec fs_work_4                                                     ; b135: c6 b4       ..             ; Decrement outer counter
    bne cb12f                                                         ; b137: d0 f6       ..             ; Outer loop: ~1000 delay cycles
    rts                                                               ; b139: 60          `              ; Return

; &b13a referenced 2 times by &b113, &b11a
.write_ps_slot_byte_ff
    iny                                                               ; b13a: c8          .              ; Advance Y
    lda l00af                                                         ; b13b: a5 af       ..             ; Get buffer page
    sta (nfs_workspace),y                                             ; b13d: 91 9e       ..             ; Store in workspace
    lda #&ff                                                          ; b13f: a9 ff       ..             ; A=&FF
; &b141 referenced 1 time by &b105
.write_two_bytes_inc_y
    iny                                                               ; b141: c8          .              ; Advance Y
    sta (nfs_workspace),y                                             ; b142: 91 9e       ..             ; Write byte to workspace
    iny                                                               ; b144: c8          .              ; Advance Y
    sta (nfs_workspace),y                                             ; b145: 91 9e       ..             ; Write byte to workspace
    iny                                                               ; b147: c8          .              ; Advance Y
    rts                                                               ; b148: 60          `              ; Return

; &b149 referenced 2 times by &b038, &b1a6
.reverse_ps_name_to_tx
    ldy #&1c                                                          ; b149: a0 1c       ..             ; Start of PS name at offset &1C
; &b14b referenced 1 time by &b151
.loop_cb14b
    lda (net_rx_ptr),y                                                ; b14b: b1 9c       ..             ; Load byte from RX buffer
    pha                                                               ; b14d: 48          H              ; Push to stack (for reversal)
    iny                                                               ; b14e: c8          .              ; Next source byte
    cpy #&24 ; '$'                                                    ; b14f: c0 24       .$             ; End of PS name field (&24)?
    bne loop_cb14b                                                    ; b151: d0 f8       ..             ; No: continue pushing
    ldy #&1b                                                          ; b153: a0 1b       ..             ; End of TX name field at &1B
; &b155 referenced 1 time by &b15b
.loop_cb155
    pla                                                               ; b155: 68          h              ; Pop byte (reversed order)
    sta (net_rx_ptr),y                                                ; b156: 91 9c       ..             ; Store in RX buffer
    dey                                                               ; b158: 88          .              ; Previous position
    cpy #&13                                                          ; b159: c0 13       ..             ; Start of TX field (&13)?
    bne loop_cb155                                                    ; b15b: d0 f8       ..             ; No: continue popping
    lda net_rx_ptr_hi                                                 ; b15d: a5 9d       ..             ; Copy RX page to TX
    sta net_tx_ptr_hi                                                 ; b15f: 85 9b       ..             ; Set TX pointer high
    lda #&10                                                          ; b161: a9 10       ..             ; TX offset &10
    sta net_tx_ptr                                                    ; b163: 85 9a       ..             ; Set TX pointer low
    ldy #3                                                            ; b165: a0 03       ..             ; Copy 4 header bytes
; &b167 referenced 1 time by &b16d
.loop_cb167
    lda ps_tx_header_template,y                                       ; b167: b9 70 b1    .p.            ; Get header template byte
    sta (net_tx_ptr),y                                                ; b16a: 91 9a       ..             ; Store in TX buffer
    dey                                                               ; b16c: 88          .              ; Previous byte
    bpl loop_cb167                                                    ; b16d: 10 f8       ..             ; Loop until all 4 copied
    rts                                                               ; b16f: 60          `              ; Return

; &b170 referenced 1 time by &b167
.ps_tx_header_template
    equb &80, &9f, &ff, &ff                                           ; b170: 80 9f ff... ...

; &b174 referenced 4 times by &a089, &b225, &b25d, &b2b5
.print_station_addr
    php                                                               ; b174: 08          .              ; Save V flag (controls padding)
    lda l00b6                                                         ; b175: a5 b6       ..             ; Get network number
    beq cb184                                                         ; b177: f0 0b       ..             ; Zero: no network prefix
    jsr print_decimal_3dig                                            ; b179: 20 68 af     h.            ; Print network as 3 digits
    lda #&2e ; '.'                                                    ; b17c: a9 2e       ..             ; '.' separator
    jsr osasci                                                        ; b17e: 20 e3 ff     ..            ; Write character 46
    bit bit_test_ff_pad                                               ; b181: 2c 7d 94    ,}.            ; Set V (suppress station padding)
; &b184 referenced 1 time by &b177
.cb184
    bvs cb18d                                                         ; b184: 70 07       p.             ; V set: skip padding spaces
    jsr print_inline                                                  ; b186: 20 31 91     1.            ; Print 4 spaces (padding)
    equs "    "                                                       ; b189: 20 20 20...

; &b18d referenced 1 time by &b184
.cb18d
    lda fs_work_5                                                     ; b18d: a5 b5       ..             ; Get station number
    plp                                                               ; b18f: 28          (              ; Restore flags
    jmp print_decimal_3dig                                            ; b190: 4c 68 af    Lh.            ; Print station as 3 digits

    equb &80, &9f, 0, 0, &14, 0, &ff, &ff, &1c, 0, &ff, &ff           ; b193: 80 9f 00... ...

; ***************************************************************************************
; Poll printer server status.
; Waits for completion of the current
; print job, displaying progress.
; ***************************************************************************************
.cmd_pollps
    sty ws_ptr_hi                                                     ; b19f: 84 ac       ..             ; Save command line pointer high
    jsr init_spool_drive                                              ; b1a1: 20 c0 af     ..            ; Initialise spool/print drive
    sta fs_work_4                                                     ; b1a4: 85 b4       ..             ; Save spool drive number
    jsr reverse_ps_name_to_tx                                         ; b1a6: 20 49 b1     I.            ; Copy PS name to TX buffer
    jsr init_ps_slot_from_rx                                          ; b1a9: 20 c4 b2     ..            ; Init PS slot from RX data
    ldy ws_ptr_hi                                                     ; b1ac: a4 ac       ..             ; Restore command line pointer
    jsr save_ptr_to_spool_buf                                         ; b1ae: 20 b5 af     ..            ; Save pointer to spool buffer
    lda (fs_options),y                                                ; b1b1: b1 bb       ..             ; Get first argument character
    cmp #&0d                                                          ; b1b3: c9 0d       ..             ; End of command line?
    beq cb1e1                                                         ; b1b5: f0 2a       .*             ; Yes: no argument given
    clv                                                               ; b1b7: b8          .              ; Clear V (= explicit PS name given)
    jsr is_decimal_digit                                              ; b1b8: 20 44 92     D.            ; Is first char a decimal digit?
    bcc cb1e4                                                         ; b1bb: 90 27       .'             ; Yes: station number, skip PS name
    tya                                                               ; b1bd: 98          .              ; PS name follows
    pha                                                               ; b1be: 48          H              ; Save Y
    jsr load_ps_server_addr                                           ; b1bf: 20 c6 b0     ..            ; Load PS server address
    pla                                                               ; b1c2: 68          h              ; Restore Y
    tay                                                               ; b1c3: a8          .              ; Back to Y register
    jsr parse_fs_ps_args                                              ; b1c4: 20 8f a0     ..            ; Parse FS/PS arguments
    ldy #&7a ; 'z'                                                    ; b1c7: a0 7a       .z             ; Offset &7A in slot buffer
    lda fs_work_5                                                     ; b1c9: a5 b5       ..             ; Get parsed station low
    sta (l00ae),y                                                     ; b1cb: 91 ae       ..             ; Store station number low
    iny                                                               ; b1cd: c8          .              ; Y=&7b
    lda l00b6                                                         ; b1ce: a5 b6       ..             ; Get parsed network number
    sta (l00ae),y                                                     ; b1d0: 91 ae       ..             ; Store station number high
    ldy #&14                                                          ; b1d2: a0 14       ..             ; Offset &14 in TX buffer
    jsr copy_ps_data                                                  ; b1d4: 20 f9 af     ..            ; Copy PS data to TX buffer
    lda l00af                                                         ; b1d7: a5 af       ..             ; Get buffer page high
    sta net_tx_ptr_hi                                                 ; b1d9: 85 9b       ..             ; Set TX pointer high byte
    lda #&78 ; 'x'                                                    ; b1db: a9 78       .x             ; Offset &78 in buffer
    sta net_tx_ptr                                                    ; b1dd: 85 9a       ..             ; Set TX pointer low byte
    bne cb212                                                         ; b1df: d0 31       .1             ; ALWAYS branch

; &b1e1 referenced 1 time by &b1b5
.cb1e1
    bit bit_test_ff_pad                                               ; b1e1: 2c 7d 94    ,}.            ; Set V (= no explicit PS name)
; &b1e4 referenced 1 time by &b1bb
.cb1e4
    bvs cb212                                                         ; b1e4: 70 2c       p,             ; V set (no arg): skip to send
    ldx #6                                                            ; b1e6: a2 06       ..             ; Max 6 characters for PS name
    ldy #&14                                                          ; b1e8: a0 14       ..             ; Buffer offset for PS name
    lda #&20 ; ' '                                                    ; b1ea: a9 20       .              ; Space character
; &b1ec referenced 1 time by &b1f0
.loop_cb1ec
    sta (net_rx_ptr),y                                                ; b1ec: 91 9c       ..             ; Fill buffer position with space
    iny                                                               ; b1ee: c8          .              ; Next position
    dex                                                               ; b1ef: ca          .              ; Count down
    bne loop_cb1ec                                                    ; b1f0: d0 fa       ..             ; Loop until 6 spaces filled
    jsr save_ptr_to_os_text                                           ; b1f2: 20 95 af     ..            ; Save pointer to OS text
    ldy ws_ptr_hi                                                     ; b1f5: a4 ac       ..             ; Restore command line pointer
    jsr gsinit                                                        ; b1f7: 20 c2 ff     ..            ; Initialise string reading
    beq cb212                                                         ; b1fa: f0 16       ..             ; Empty string: skip to send
    ldx #6                                                            ; b1fc: a2 06       ..             ; Max 6 characters
    sty ws_ptr_hi                                                     ; b1fe: 84 ac       ..             ; Save updated string pointer
    ldy #&14                                                          ; b200: a0 14       ..             ; Buffer offset for PS name
    sty l00ad                                                         ; b202: 84 ad       ..             ; Save buffer position
; &b204 referenced 1 time by &b210
.loop_cb204
    ldy ws_ptr_hi                                                     ; b204: a4 ac       ..             ; Restore string pointer
    jsr gsread                                                        ; b206: 20 c5 ff     ..            ; Read next char from string
    sty ws_ptr_hi                                                     ; b209: 84 ac       ..             ; Save updated string pointer
    bcs cb212                                                         ; b20b: b0 05       ..             ; End of string: go to send
    jsr store_char_uppercase                                          ; b20d: 20 db b2     ..            ; Store char uppercased in buffer
    bne loop_cb204                                                    ; b210: d0 f2       ..             ; Loop if more chars to copy
; &b212 referenced 4 times by &b1df, &b1e4, &b1fa, &b20b
.cb212
    lda #&80                                                          ; b212: a9 80       ..             ; Enable escape checking
    sta escapable                                                     ; b214: 85 97       ..             ; Set escapable flag
    jsr send_net_packet                                               ; b216: 20 2a 98     *.            ; Send the poll request packet
    jsr pop_requeue_ps_scan                                           ; b219: 20 d2 b0     ..            ; Pop and requeue PS scan
    jsr print_printer_server_is                                       ; b21c: 20 ab b0     ..            ; Print 'Printer server '
    jsr load_ps_server_addr                                           ; b21f: 20 c6 b0     ..            ; Load PS server address
    bit bit_test_ff_pad                                               ; b222: 2c 7d 94    ,}.            ; Set V and N flags
    jsr print_station_addr                                            ; b225: 20 74 b1     t.            ; Print station address
    jsr print_inline                                                  ; b228: 20 31 91     1.            ; Print ' "'
    equs " ", '"'                                                     ; b22b: 20 22        "

    ldy #&1c                                                          ; b22d: a0 1c       ..             ; Start of PS name in buffer
; &b22f referenced 1 time by &b23b
.loop_cb22f
    lda (net_rx_ptr),y                                                ; b22f: b1 9c       ..             ; Get character from name field
    cmp #&20 ; ' '                                                    ; b231: c9 20       .              ; Is it a space?
    beq cb23d                                                         ; b233: f0 08       ..             ; Yes: end of name
    jsr osasci                                                        ; b235: 20 e3 ff     ..            ; Write character
    iny                                                               ; b238: c8          .              ; Next character
    cpy #&22 ; '"'                                                    ; b239: c0 22       ."             ; Past end of name field?
    bne loop_cb22f                                                    ; b23b: d0 f2       ..             ; No: continue printing name
; &b23d referenced 1 time by &b233
.cb23d
    jsr print_inline                                                  ; b23d: 20 31 91     1.            ; Print '"' + CR
    equs '"', &0d                                                     ; b240: 22 0d       ".

    nop                                                               ; b242: ea          .              ; Padding byte
; &b243 referenced 1 time by &b2c1
.cb243
    pla                                                               ; b243: 68          h              ; Get slot offset from stack
    beq return_31                                                     ; b244: f0 7d       .}             ; Zero: all slots done, return
    pha                                                               ; b246: 48          H              ; Save slot offset
    tay                                                               ; b247: a8          .              ; Transfer to Y
    lda (nfs_workspace),y                                             ; b248: b1 9e       ..             ; Read slot status byte
    bpl cb2bb                                                         ; b24a: 10 6f       .o             ; Bit 7 clear: slot inactive
    iny                                                               ; b24c: c8          .              ; Advance to station number
    iny                                                               ; b24d: c8          .              ; Offset+2 in slot
    lda (nfs_workspace),y                                             ; b24e: b1 9e       ..             ; Read station number low
    sta fs_work_5                                                     ; b250: 85 b5       ..             ; Store station low
    iny                                                               ; b252: c8          .              ; Next byte (offset+3)
    lda (nfs_workspace),y                                             ; b253: b1 9e       ..             ; Read network number
    sta l00b6                                                         ; b255: 85 b6       ..             ; Store network number
    iny                                                               ; b257: c8          .              ; Next byte (offset+4)
    lda (nfs_workspace),y                                             ; b258: b1 9e       ..             ; Read status page pointer
    sta l00ae                                                         ; b25a: 85 ae       ..             ; Store pointer low
    clv                                                               ; b25c: b8          .              ; Clear V flag
    jsr print_station_addr                                            ; b25d: 20 74 b1     t.            ; Print station address (V=0)
    jsr print_inline                                                  ; b260: 20 31 91     1.            ; Print ' is '
    equs " is "                                                       ; b263: 20 69 73...  is

    ldx #0                                                            ; b267: a2 00       ..             ; X=0 for indirect indexed access
    lda (l00ae,x)                                                     ; b269: a1 ae       ..             ; Read printer status byte
    bne cb278                                                         ; b26b: d0 0b       ..             ; Non-zero: not ready
    jsr print_inline                                                  ; b26d: 20 31 91     1.            ; Print 'ready'
    equs "ready"                                                      ; b270: 72 65 61... rea

    clv                                                               ; b275: b8          .              ; Clear V
    bvc cb2b8                                                         ; b276: 50 40       P@             ; ALWAYS branch

; &b278 referenced 1 time by &b26b
.cb278
    cmp #2                                                            ; b278: c9 02       ..             ; Status = 2?
    bne cb288                                                         ; b27a: d0 0c       ..             ; No: check for busy
; &b27c referenced 1 time by &b28a
.loop_cb27c
    jsr print_inline                                                  ; b27c: 20 31 91     1.            ; Print 'jammed'
    equs "jammed"                                                     ; b27f: 6a 61 6d... jam

    clv                                                               ; b285: b8          .              ; Clear V
    bvc cb2b8                                                         ; b286: 50 30       P0             ; ALWAYS branch

; &b288 referenced 1 time by &b27a
.cb288
    cmp #1                                                            ; b288: c9 01       ..             ; Status = 1?
    bne loop_cb27c                                                    ; b28a: d0 f0       ..             ; Not 1 or 2: default to jammed
    jsr print_inline                                                  ; b28c: 20 31 91     1.            ; Print 'busy'
    equs "busy"                                                       ; b28f: 62 75 73... bus

    inc l00ae                                                         ; b293: e6 ae       ..             ; Advance past status byte
    lda (l00ae,x)                                                     ; b295: a1 ae       ..             ; Read client station number
    sta fs_work_5                                                     ; b297: 85 b5       ..             ; Store station low
    beq cb2b8                                                         ; b299: f0 1d       ..             ; Zero: no client info, skip
    jsr print_inline                                                  ; b29b: 20 31 91     1.            ; Print ' with station '
    equs " with station "                                             ; b29e: 20 77 69...  wi

    inc l00ae                                                         ; b2ac: e6 ae       ..             ; Advance past station low
    lda (l00ae,x)                                                     ; b2ae: a1 ae       ..             ; Read client network number
    sta l00b6                                                         ; b2b0: 85 b6       ..             ; Store network number
    bit bit_test_ff_pad                                               ; b2b2: 2c 7d 94    ,}.            ; Set V flag
    jsr print_station_addr                                            ; b2b5: 20 74 b1     t.            ; Print client station address
; &b2b8 referenced 3 times by &b276, &b286, &b299
.cb2b8
    jsr osnewl                                                        ; b2b8: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
; &b2bb referenced 1 time by &b24a
.cb2bb
    pla                                                               ; b2bb: 68          h              ; Retrieve slot offset
    tay                                                               ; b2bc: a8          .              ; Transfer to Y
    lda #&3f ; '?'                                                    ; b2bd: a9 3f       .?             ; Mark slot as processed (&3F)
    sta (nfs_workspace),y                                             ; b2bf: 91 9e       ..             ; Write marker to workspace
    bne cb243                                                         ; b2c1: d0 80       ..             ; ALWAYS branch

; &b2c3 referenced 1 time by &b244
.return_31
    rts                                                               ; b2c3: 60          `              ; Return

; &b2c4 referenced 1 time by &b1a9
.init_ps_slot_from_rx
    ldy #&78 ; 'x'                                                    ; b2c4: a0 78       .x             ; Start at offset &78
; &b2c6 referenced 1 time by &b2d8
.loop_cb2c6
    lda write_ps_slot_link_addr,y                                     ; b2c6: b9 1b b1    ...            ; Load template byte
    cpy #&7d ; '}'                                                    ; b2c9: c0 7d       .}             ; At offset &7D?
    beq cb2d1                                                         ; b2cb: f0 04       ..             ; Yes: substitute RX page
    cpy #&81                                                          ; b2cd: c0 81       ..             ; At offset &81?
    bne cb2d3                                                         ; b2cf: d0 02       ..             ; No: use template byte
; &b2d1 referenced 1 time by &b2cb
.cb2d1
    lda net_rx_ptr_hi                                                 ; b2d1: a5 9d       ..             ; Use RX buffer page instead
; &b2d3 referenced 1 time by &b2cf
.cb2d3
    sta (l00ae),y                                                     ; b2d3: 91 ae       ..             ; Store byte in slot buffer
    iny                                                               ; b2d5: c8          .              ; Next offset
    cpy #&84                                                          ; b2d6: c0 84       ..             ; Past end of slot (&84)?
    bne loop_cb2c6                                                    ; b2d8: d0 ec       ..             ; No: continue copying
    rts                                                               ; b2da: 60          `              ; Return

; &b2db referenced 2 times by &b033, &b20d
.store_char_uppercase
    ldy l00ad                                                         ; b2db: a4 ad       ..             ; Y = current buffer position
    and #&7f                                                          ; b2dd: 29 7f       ).             ; Strip high bit
    cmp #&61 ; 'a'                                                    ; b2df: c9 61       .a             ; Is it lowercase 'a' or above?
    bcc cb2e9                                                         ; b2e1: 90 06       ..             ; Below 'a': not lowercase
    cmp #&7b ; '{'                                                    ; b2e3: c9 7b       .{             ; Above 'z'?
    bcs cb2e9                                                         ; b2e5: b0 02       ..             ; Yes: not lowercase
    and #&5f ; '_'                                                    ; b2e7: 29 5f       )_             ; Convert to uppercase
; &b2e9 referenced 2 times by &b2e1, &b2e5
.cb2e9
    sta (net_rx_ptr),y                                                ; b2e9: 91 9c       ..             ; Store in RX buffer
    iny                                                               ; b2eb: c8          .              ; Next buffer position
    sty l00ad                                                         ; b2ec: 84 ad       ..             ; Update buffer position
    dex                                                               ; b2ee: ca          .              ; Decrement character count
    rts                                                               ; b2ef: 60          `              ; Return (Z set if count=0)

; ***************************************************************************************
; *Prot command.
; Sets protection attribute on a file
; to prevent accidental deletion.
; ***************************************************************************************
.cmd_prot
    lda (fs_crc_lo),y                                                 ; b2f0: b1 be       ..             ; Get next char from command line
    eor #&0d                                                          ; b2f2: 49 0d       I.             ; Compare with CR (end of line)
    bne cb2fa                                                         ; b2f4: d0 04       ..             ; Not CR: attribute keywords follow
    lda #&ff                                                          ; b2f6: a9 ff       ..             ; A=&FF: protect all attributes
    bne store_prot_mask                                               ; b2f8: d0 20       .              ; ALWAYS branch

; &b2fa referenced 1 time by &b2f4
.cb2fa
    lda ws_0d68                                                       ; b2fa: ad 68 0d    .h.            ; Load current protection mask
    pha                                                               ; b2fd: 48          H              ; Save as starting value
; &b2fe referenced 1 time by &b30e
.loop_cb2fe
    ldx #&d3                                                          ; b2fe: a2 d3       ..             ; X=&D3: attribute keyword table offset
    lda (fs_crc_lo),y                                                 ; b300: b1 be       ..             ; Get next char from command line
    sta ws_page                                                       ; b302: 85 a8       ..             ; Save for end-of-args check
    jsr match_fs_cmd                                                  ; b304: 20 28 a1     (.            ; Match attribute keyword in table
    bcs prot_check_arg_end                                            ; b307: b0 07       ..             ; No match: check if end of arguments
    pla                                                               ; b309: 68          h              ; Retrieve accumulated mask
    ora cmd_table_fs_lo,x                                             ; b30a: 1d d9 a3    ...            ; OR in attribute bit for keyword
    pha                                                               ; b30d: 48          H              ; Save updated mask
    bne loop_cb2fe                                                    ; b30e: d0 ee       ..             ; Always non-zero after ORA: loop
; &b310 referenced 2 times by &b307, &b334
.prot_check_arg_end
    lda ws_page                                                       ; b310: a5 a8       ..             ; Get the unmatched character
    eor #&0d                                                          ; b312: 49 0d       I.             ; Is it CR?
    beq cb319                                                         ; b314: f0 03       ..             ; Yes: arguments ended correctly
    jmp error_bad_command                                             ; b316: 4c 45 a2    LE.            ; No: invalid attribute keyword

; &b319 referenced 1 time by &b314
.cb319
    pla                                                               ; b319: 68          h              ; Retrieve final protection mask
; &b31a referenced 2 times by &b2f8, &b325
.store_prot_mask
    sta ws_0d68                                                       ; b31a: 8d 68 0d    .h.            ; Store protection mask
    sta ws_0d69                                                       ; b31d: 8d 69 0d    .i.            ; Store protection mask copy
    rts                                                               ; b320: 60          `              ; Return

; ***************************************************************************************
; *Unprot command.
; Removes protection attribute from
; a file.
; ***************************************************************************************
.cmd_unprot
    lda (fs_crc_lo),y                                                 ; b321: b1 be       ..             ; Get next char from command line
    eor #&0d                                                          ; b323: 49 0d       I.             ; Compare with CR (end of line)
    beq store_prot_mask                                               ; b325: f0 f3       ..             ; No args: A=0 clears all protection
    lda ws_0d68                                                       ; b327: ad 68 0d    .h.            ; Load current protection mask
    pha                                                               ; b32a: 48          H              ; Save as starting value
; &b32b referenced 1 time by &b33b
.loop_cb32b
    ldx #&d3                                                          ; b32b: a2 d3       ..             ; X=&D3: attribute keyword table offset
    lda (fs_crc_lo),y                                                 ; b32d: b1 be       ..             ; Get next char from command line
    sta ws_page                                                       ; b32f: 85 a8       ..             ; Save for end-of-args check
    jsr match_fs_cmd                                                  ; b331: 20 28 a1     (.            ; Match attribute keyword in table
    bcs prot_check_arg_end                                            ; b334: b0 da       ..             ; No match: check if end of arguments
    pla                                                               ; b336: 68          h              ; Retrieve accumulated mask
    and cmd_table_fs_hi,x                                             ; b337: 3d da a3    =..            ; AND to clear matched attribute bit
    pha                                                               ; b33a: 48          H              ; Save updated mask
    bcc loop_cb32b                                                    ; b33b: 90 ee       ..             ; ALWAYS branch

; ***************************************************************************************
; *Wipe command.
; Deletes files with interactive per-
; file confirmation prompt.
; ***************************************************************************************
.cmd_wipe
    jsr mask_owner_access                                             ; b33d: 20 12 af     ..
    lda #0                                                            ; b340: a9 00       ..
    sta fs_work_5                                                     ; b342: 85 b5       ..
    jsr save_ptr_to_os_text                                           ; b344: 20 95 af     ..
    jsr parse_filename_arg                                            ; b347: 20 82 ae     ..
    inx                                                               ; b34a: e8          .
    stx l00b6                                                         ; b34b: 86 b6       ..
; &b34d referenced 1 time by &b389
.cb34d
    lda #1                                                            ; b34d: a9 01       ..
    sta l0f05                                                         ; b34f: 8d 05 0f    ...
    sta l0f07                                                         ; b352: 8d 07 0f    ...
    ldx fs_work_5                                                     ; b355: a6 b5       ..
    stx l0f06                                                         ; b357: 8e 06 0f    ...
    ldx #3                                                            ; b35a: a2 03       ..
    jsr copy_arg_to_buf                                               ; b35c: 20 f2 ae     ..
    ldy #3                                                            ; b35f: a0 03       ..
    lda #&80                                                          ; b361: a9 80       ..
    sta escapable                                                     ; b363: 85 97       ..
    jsr save_net_tx_cb                                                ; b365: 20 99 94     ..
    lda l0f05                                                         ; b368: ad 05 0f    ...
    bne cb380                                                         ; b36b: d0 13       ..
    lda #osbyte_flush_buffer_class                                    ; b36d: a9 0f       ..
    ldx #1                                                            ; b36f: a2 01       ..
    jsr osbyte                                                        ; b371: 20 f4 ff     ..            ; Flush input buffers (X non-zero)
    lda #osbyte_scan_keyboard_from_16                                 ; b374: a9 7a       .z
    jsr osbyte                                                        ; b376: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    ldy #0                                                            ; b379: a0 00       ..             ; Y=key
    lda #osbyte_write_keys_pressed                                    ; b37b: a9 78       .x
    jmp osbyte                                                        ; b37d: 4c f4 ff    L..            ; Write current keys pressed (X and Y)

; &b380 referenced 1 time by &b36b
.cb380
    lda l0f2f                                                         ; b380: ad 2f 0f    ./.
; &b383 referenced 1 time by &b393
.loop_cb383
    cmp #&4c ; 'L'                                                    ; b383: c9 4c       .L
    bne cb38c                                                         ; b385: d0 05       ..
; &b387 referenced 1 time by &b40e
.cb387
    inc fs_work_5                                                     ; b387: e6 b5       ..
    jmp cb34d                                                         ; b389: 4c 4d b3    LM.

; &b38c referenced 1 time by &b385
.cb38c
    cmp #&44 ; 'D'                                                    ; b38c: c9 44       .D
    bne cb395                                                         ; b38e: d0 05       ..
    lda l0f30                                                         ; b390: ad 30 0f    .0.
    bne loop_cb383                                                    ; b393: d0 ee       ..
; &b395 referenced 1 time by &b38e
.cb395
    ldx #1                                                            ; b395: a2 01       ..
    ldy l00b6                                                         ; b397: a4 b6       ..
; &b399 referenced 1 time by &b3a6
.loop_cb399
    lda l0f06,x                                                       ; b399: bd 06 0f    ...
    jsr osasci                                                        ; b39c: 20 e3 ff     ..            ; Write character
    sta l0e30,y                                                       ; b39f: 99 30 0e    .0.
    iny                                                               ; b3a2: c8          .
    inx                                                               ; b3a3: e8          .
    cpx #&0c                                                          ; b3a4: e0 0c       ..
    bne loop_cb399                                                    ; b3a6: d0 f1       ..
    jsr print_inline                                                  ; b3a8: 20 31 91     1.
    equs "(Y/N/?) "                                                   ; b3ab: 28 59 2f... (Y/

    nop                                                               ; b3b3: ea          .
    jsr flush_and_read_char                                           ; b3b4: 20 1f b4     ..
    cmp #&3f ; '?'                                                    ; b3b7: c9 3f       .?
    bne cb3db                                                         ; b3b9: d0 20       .
    lda #&0d                                                          ; b3bb: a9 0d       ..
    jsr oswrch                                                        ; b3bd: 20 ee ff     ..            ; Write character 13
    ldx #2                                                            ; b3c0: a2 02       ..
; &b3c2 referenced 1 time by &b3cb
.loop_cb3c2
    lda l0f05,x                                                       ; b3c2: bd 05 0f    ...
    jsr osasci                                                        ; b3c5: 20 e3 ff     ..            ; Write character
    inx                                                               ; b3c8: e8          .
    cpx #&3e ; '>'                                                    ; b3c9: e0 3e       .>
    bne loop_cb3c2                                                    ; b3cb: d0 f5       ..
    jsr print_inline                                                  ; b3cd: 20 31 91     1.
    equs " (Y/N) "                                                    ; b3d0: 20 28 59...  (Y

    nop                                                               ; b3d7: ea          .
    jsr flush_and_read_char                                           ; b3d8: 20 1f b4     ..
; &b3db referenced 1 time by &b3b9
.cb3db
    and #&df                                                          ; b3db: 29 df       ).
    cmp #&59 ; 'Y'                                                    ; b3dd: c9 59       .Y
    bne cb40b                                                         ; b3df: d0 2a       .*
    jsr osasci                                                        ; b3e1: 20 e3 ff     ..            ; Write character
    ldx #0                                                            ; b3e4: a2 00       ..
    lda l0e30,x                                                       ; b3e6: bd 30 0e    .0.
    cmp #&0d                                                          ; b3e9: c9 0d       ..
    beq cb411                                                         ; b3eb: f0 24       .$
; &b3ed referenced 1 time by &b402
.loop_cb3ed
    lda l0e30,x                                                       ; b3ed: bd 30 0e    .0.
    cmp #&0d                                                          ; b3f0: c9 0d       ..
    bne cb3f6                                                         ; b3f2: d0 02       ..
    lda #&2e ; '.'                                                    ; b3f4: a9 2e       ..
; &b3f6 referenced 1 time by &b3f2
.cb3f6
    cmp #&20 ; ' '                                                    ; b3f6: c9 20       .
    bne cb3fc                                                         ; b3f8: d0 02       ..
; &b3fa referenced 1 time by &b41d
.cb3fa
    lda #&0d                                                          ; b3fa: a9 0d       ..
; &b3fc referenced 1 time by &b3f8
.cb3fc
    sta l0f05,x                                                       ; b3fc: 9d 05 0f    ...
    inx                                                               ; b3ff: e8          .
    cmp #&0d                                                          ; b400: c9 0d       ..
    bne loop_cb3ed                                                    ; b402: d0 e9       ..
    ldy #&14                                                          ; b404: a0 14       ..
    jsr save_net_tx_cb                                                ; b406: 20 99 94     ..
    dec fs_work_5                                                     ; b409: c6 b5       ..
; &b40b referenced 1 time by &b3df
.cb40b
    jsr osnewl                                                        ; b40b: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    jmp cb387                                                         ; b40e: 4c 87 b3    L..

; &b411 referenced 1 time by &b3eb
.cb411
    dex                                                               ; b411: ca          .
; &b412 referenced 1 time by &b41b
.loop_cb412
    inx                                                               ; b412: e8          .
    lda l0e31,x                                                       ; b413: bd 31 0e    .1.
    sta l0f05,x                                                       ; b416: 9d 05 0f    ...
    cmp #&20 ; ' '                                                    ; b419: c9 20       .
    bne loop_cb412                                                    ; b41b: d0 f5       ..
    beq cb3fa                                                         ; b41d: f0 db       ..             ; ALWAYS branch

; &b41f referenced 2 times by &b3b4, &b3d8
.flush_and_read_char
    lda #osbyte_flush_buffer_class                                    ; b41f: a9 0f       ..
    ldx #1                                                            ; b421: a2 01       ..
    jsr osbyte                                                        ; b423: 20 f4 ff     ..            ; Flush input buffers (X non-zero)
    jsr osrdch                                                        ; b426: 20 e0 ff     ..            ; Read a character from the current input stream
    bcc return_32                                                     ; b429: 90 03       ..
    jmp raise_escape_error                                            ; b42b: 4c 60 95    L`.

; &b42e referenced 1 time by &b429
.return_32
    rts                                                               ; b42e: 60          `

    equb &a9, 0, &a0, &78, &88, &91, &cc, &d0, &fb, &60               ; b42f: a9 00 a0... ...

; &b439 referenced 1 time by &8b6a
.init_channel_table
    lda #0                                                            ; b439: a9 00       ..
    tay                                                               ; b43b: a8          .              ; Y=&00
; &b43c referenced 1 time by &b440
.loop_cb43c
    sta l1000,y                                                       ; b43c: 99 00 10    ...
    iny                                                               ; b43f: c8          .
    bne loop_cb43c                                                    ; b440: d0 fa       ..
    ldy #&0f                                                          ; b442: a0 0f       ..
    lda (net_rx_ptr),y                                                ; b444: b1 9c       ..
    sec                                                               ; b446: 38          8
    sbc #&5a ; 'Z'                                                    ; b447: e9 5a       .Z
    tay                                                               ; b449: a8          .
    lda #&40 ; '@'                                                    ; b44a: a9 40       .@
; &b44c referenced 1 time by &b452
.loop_cb44c
    sta l1000,y                                                       ; b44c: 99 00 10    ...
    dey                                                               ; b44f: 88          .
    cpy #&b8                                                          ; b450: c0 b8       ..
    bpl loop_cb44c                                                    ; b452: 10 f8       ..
    iny                                                               ; b454: c8          .
    lda #&c0                                                          ; b455: a9 c0       ..
    sta l1000,y                                                       ; b457: 99 00 10    ...
    rts                                                               ; b45a: 60          `

; &b45b referenced 5 times by &92a9, &92c0, &9c60, &9c9e, &b745
.attr_to_chan_index
    php                                                               ; b45b: 08          .
    sec                                                               ; b45c: 38          8
    sbc #&20 ; ' '                                                    ; b45d: e9 20       .
    bmi cb465                                                         ; b45f: 30 04       0.
    cmp #&10                                                          ; b461: c9 10       ..
    bcc cb467                                                         ; b463: 90 02       ..
; &b465 referenced 1 time by &b45f
.cb465
    lda #&ff                                                          ; b465: a9 ff       ..
; &b467 referenced 1 time by &b463
.cb467
    plp                                                               ; b467: 28          (
    tax                                                               ; b468: aa          .
    rts                                                               ; b469: 60          `

; &b46a referenced 2 times by &9d97, &b4e3
.check_chan_char
    cmp #&20 ; ' '                                                    ; b46a: c9 20       .
    bcc err_net_chan_invalid                                          ; b46c: 90 04       ..
    cmp #&30 ; '0'                                                    ; b46e: c9 30       .0
    bcc lookup_chan_by_char                                           ; b470: 90 2b       .+
; &b472 referenced 2 times by &9bc6, &b46c
.err_net_chan_invalid
    pha                                                               ; b472: 48          H
; &b473 referenced 1 time by &b4a5
.cb473
    lda #&de                                                          ; b473: a9 de       ..
.err_net_chan_not_found
net_channel_err_string = err_net_chan_not_found+2
    jsr error_inline_log                                              ; b475: 20 bb 96     ..
; &b477 referenced 2 times by &b4bd, &b4d1
    equs "Net channel", 0                                             ; b478: 4e 65 74... Net

    jsr l6f6e                                                         ; b484: 20 6e 6f     no
    equs "t on this file server"                                      ; b487: 74 20 6f... t o
    equb 0                                                            ; b49c: 00          .

; &b49d referenced 2 times by &9ec4, &b470
.lookup_chan_by_char
    pha                                                               ; b49d: 48          H
    sec                                                               ; b49e: 38          8
    sbc #&20 ; ' '                                                    ; b49f: e9 20       .
    tax                                                               ; b4a1: aa          .
    lda l1030,x                                                       ; b4a2: bd 30 10    .0.
    beq cb473                                                         ; b4a5: f0 cc       ..
    jsr match_station_net                                             ; b4a7: 20 7a b5     z.
    bne cb4b1                                                         ; b4aa: d0 05       ..
    pla                                                               ; b4ac: 68          h
    lda l1060,x                                                       ; b4ad: bd 60 10    .`.
    rts                                                               ; b4b0: 60          `

; &b4b1 referenced 1 time by &b4aa
.cb4b1
    lda #&de                                                          ; b4b1: a9 de       ..
    sta error_text                                                    ; b4b3: 8d 01 01    ...
    lda #0                                                            ; b4b6: a9 00       ..
    sta error_block                                                   ; b4b8: 8d 00 01    ...
    tax                                                               ; b4bb: aa          .              ; X=&00
; &b4bc referenced 1 time by &b4c3
.loop_cb4bc
    inx                                                               ; b4bc: e8          .
    lda net_channel_err_string,x                                      ; b4bd: bd 77 b4    .w.
    sta error_text,x                                                  ; b4c0: 9d 01 01    ...
    bne loop_cb4bc                                                    ; b4c3: d0 f7       ..
    stx fs_load_addr_2                                                ; b4c5: 86 b2       ..
    stx fs_work_4                                                     ; b4c7: 86 b4       ..
    pla                                                               ; b4c9: 68          h
    jsr append_space_and_num                                          ; b4ca: 20 5c 97     \.
    ldy fs_work_4                                                     ; b4cd: a4 b4       ..
; &b4cf referenced 1 time by &b4d7
.loop_cb4cf
    iny                                                               ; b4cf: c8          .
    inx                                                               ; b4d0: e8          .
    lda net_channel_err_string,y                                      ; b4d1: b9 77 b4    .w.
    sta error_text,x                                                  ; b4d4: 9d 01 01    ...
    bne loop_cb4cf                                                    ; b4d7: d0 f6       ..
    jmp error_block                                                   ; b4d9: 4c 00 01    L..

; &b4dc referenced 2 times by &b7d4, &b85c
.store_result_check_dir
    lda l10c9                                                         ; b4dc: ad c9 10    ...
    ldy #&0e                                                          ; b4df: a0 0e       ..
    sta (net_rx_ptr),y                                                ; b4e1: 91 9c       ..
; &b4e3 referenced 2 times by &9bf9, &9e47
.check_not_dir
    jsr check_chan_char                                               ; b4e3: 20 6a b4     j.
    and #2                                                            ; b4e6: 29 02       ).
    beq return_33                                                     ; b4e8: f0 0f       ..
    lda #&a8                                                          ; b4ea: a9 a8       ..
    jsr error_inline_log                                              ; b4ec: 20 bb 96     ..
    equs "Is a dir.", 0                                               ; b4ef: 49 73 20... Is

; &b4f9 referenced 1 time by &b4e8
.return_33
    rts                                                               ; b4f9: 60          `

; &b4fa referenced 7 times by &9d3d, &9d72, &a268, &a307, &a332, &a369, &b531
.alloc_fcb_slot
    pha                                                               ; b4fa: 48          H
    ldx #&20 ; ' '                                                    ; b4fb: a2 20       .
; &b4fd referenced 1 time by &b505
.loop_cb4fd
    lda l1010,x                                                       ; b4fd: bd 10 10    ...
    beq cb50b                                                         ; b500: f0 09       ..
    inx                                                               ; b502: e8          .
    cpx #&30 ; '0'                                                    ; b503: e0 30       .0
    bne loop_cb4fd                                                    ; b505: d0 f6       ..
    pla                                                               ; b507: 68          h
    lda #0                                                            ; b508: a9 00       ..
    rts                                                               ; b50a: 60          `

; &b50b referenced 1 time by &b500
.cb50b
    pla                                                               ; b50b: 68          h
    sta l1010,x                                                       ; b50c: 9d 10 10    ...
    lda #0                                                            ; b50f: a9 00       ..
    sta l0fe0,x                                                       ; b511: 9d e0 0f    ...
    sta l0ff0,x                                                       ; b514: 9d f0 0f    ...
    sta l1000,x                                                       ; b517: 9d 00 10    ...
    lda l0e00                                                         ; b51a: ad 00 0e    ...
    sta l1020,x                                                       ; b51d: 9d 20 10    . .
    lda l0e01                                                         ; b520: ad 01 0e    ...
    sta l1030,x                                                       ; b523: 9d 30 10    .0.
    txa                                                               ; b526: 8a          .
    pha                                                               ; b527: 48          H
    sec                                                               ; b528: 38          8
    sbc #&20 ; ' '                                                    ; b529: e9 20       .
    tax                                                               ; b52b: aa          .
    pla                                                               ; b52c: 68          h
    rts                                                               ; b52d: 60          `

; &b52e referenced 2 times by &9ceb, &a1d5
.alloc_fcb_or_error
    pha                                                               ; b52e: 48          H
    lda #0                                                            ; b52f: a9 00       ..
    jsr alloc_fcb_slot                                                ; b531: 20 fa b4     ..
    bne cb548                                                         ; b534: d0 12       ..
    lda #&c0                                                          ; b536: a9 c0       ..
    jsr error_inline_log                                              ; b538: 20 bb 96     ..
    equs "No more FCBs", 0                                            ; b53b: 4e 6f 20... No

; &b548 referenced 1 time by &b534
.cb548
    pla                                                               ; b548: 68          h
    rts                                                               ; b549: 60          `

; &b54a referenced 3 times by &9494, &951b, &a379
.close_all_net_chans
    clc                                                               ; b54a: 18          .
    bcc cb54e                                                         ; b54b: 90 01       ..             ; ALWAYS branch

    sec                                                               ; b54d: 38          8
; &b54e referenced 1 time by &b54b
.cb54e
    bit bit_test_ff_pad                                               ; b54e: 2c 7d 94    ,}.
; &b551 referenced 1 time by &9dac
.scan_fcb_flags
    ldx #&10                                                          ; b551: a2 10       ..
; &b553 referenced 4 times by &b55f, &b569, &b56e, &b578
.cb553
    dex                                                               ; b553: ca          .
    bpl cb557                                                         ; b554: 10 01       ..
    rts                                                               ; b556: 60          `

; &b557 referenced 1 time by &b554
.cb557
    lda l1060,x                                                       ; b557: bd 60 10    .`.
    tay                                                               ; b55a: a8          .
    and #2                                                            ; b55b: 29 02       ).
    beq cb56b                                                         ; b55d: f0 0c       ..
    bvc cb553                                                         ; b55f: 50 f2       P.
    bcc cb56b                                                         ; b561: 90 08       ..
    tya                                                               ; b563: 98          .
    and #&df                                                          ; b564: 29 df       ).
    sta l1060,x                                                       ; b566: 9d 60 10    .`.
    bvs cb553                                                         ; b569: 70 e8       p.             ; ALWAYS branch

; &b56b referenced 2 times by &b55d, &b561
.cb56b
    jsr match_station_net                                             ; b56b: 20 7a b5     z.
    bne cb553                                                         ; b56e: d0 e3       ..
    lda #0                                                            ; b570: a9 00       ..
    sta l1060,x                                                       ; b572: 9d 60 10    .`.
    sta l1030,x                                                       ; b575: 9d 30 10    .0.
    beq cb553                                                         ; b578: f0 d9       ..             ; ALWAYS branch

; &b57a referenced 6 times by &a2ee, &a319, &a350, &ac2e, &b4a7, &b56b
.match_station_net
    lda l1040,x                                                       ; b57a: bd 40 10    .@.
    eor l0e00                                                         ; b57d: 4d 00 0e    M..
    bne return_34                                                     ; b580: d0 06       ..
    lda l1050,x                                                       ; b582: bd 50 10    .P.
    eor l0e01                                                         ; b585: 4d 01 0e    M..
; &b588 referenced 1 time by &b580
.return_34
    rts                                                               ; b588: 60          `

; &b589 referenced 2 times by &b68a, &b788
.find_open_fcb
    ldx l10c8                                                         ; b589: ae c8 10    ...
    bit bit_test_ff_pad                                               ; b58c: 2c 7d 94    ,}.
; &b58f referenced 4 times by &b59e, &b5a4, &b5c1, &b5c8
.cb58f
    inx                                                               ; b58f: e8          .
    cpx #&10                                                          ; b590: e0 10       ..
    bne cb596                                                         ; b592: d0 02       ..
    ldx #0                                                            ; b594: a2 00       ..
; &b596 referenced 1 time by &b592
.cb596
    cpx l10c8                                                         ; b596: ec c8 10    ...
    bne cb5a0                                                         ; b599: d0 05       ..
    bvc cb5ab                                                         ; b59b: 50 0e       P.
    clv                                                               ; b59d: b8          .
    bvc cb58f                                                         ; b59e: 50 ef       P.             ; ALWAYS branch

; &b5a0 referenced 1 time by &b599
.cb5a0
    lda l10b8,x                                                       ; b5a0: bd b8 10    ...
    rol a                                                             ; b5a3: 2a          *
    bpl cb58f                                                         ; b5a4: 10 e9       ..
    and #4                                                            ; b5a6: 29 04       ).
    bne cb5c1                                                         ; b5a8: d0 17       ..
; &b5aa referenced 1 time by &b5ca
.cb5aa
    dex                                                               ; b5aa: ca          .
; &b5ab referenced 2 times by &b59b, &b5b6
.cb5ab
    inx                                                               ; b5ab: e8          .
    cpx #&10                                                          ; b5ac: e0 10       ..
    bne cb5b2                                                         ; b5ae: d0 02       ..
    ldx #0                                                            ; b5b0: a2 00       ..
; &b5b2 referenced 1 time by &b5ae
.cb5b2
    lda l10b8,x                                                       ; b5b2: bd b8 10    ...
    rol a                                                             ; b5b5: 2a          *
    bpl cb5ab                                                         ; b5b6: 10 f3       ..
    sec                                                               ; b5b8: 38          8
    ror a                                                             ; b5b9: 6a          j
    sta l10b8,x                                                       ; b5ba: 9d b8 10    ...
    ldx l10c8                                                         ; b5bd: ae c8 10    ...
    rts                                                               ; b5c0: 60          `

; &b5c1 referenced 1 time by &b5a8
.cb5c1
    bvs cb58f                                                         ; b5c1: 70 cc       p.
    lda l10b8,x                                                       ; b5c3: bd b8 10    ...
    and #&20 ; ' '                                                    ; b5c6: 29 20       )
    bne cb58f                                                         ; b5c8: d0 c5       ..
    beq cb5aa                                                         ; b5ca: f0 de       ..             ; ALWAYS branch

; &b5cc referenced 2 times by &b60f, &b6cc
.init_wipe_counters
    ldy #1                                                            ; b5cc: a0 01       ..
    sty l10d0                                                         ; b5ce: 8c d0 10    ...
    dey                                                               ; b5d1: 88          .              ; Y=&00
    sty l10cb                                                         ; b5d2: 8c cb 10    ...
    sty l10cf                                                         ; b5d5: 8c cf 10    ...
    sty l10d6                                                         ; b5d8: 8c d6 10    ...
    tya                                                               ; b5db: 98          .              ; A=&00
    ldx #2                                                            ; b5dc: a2 02       ..
; &b5de referenced 1 time by &b5e2
.loop_cb5de
    sta l10d1,x                                                       ; b5de: 9d d1 10    ...
    dex                                                               ; b5e1: ca          .
    bpl loop_cb5de                                                    ; b5e2: 10 fa       ..
    stx l10cd                                                         ; b5e4: 8e cd 10    ...
    stx l10ce                                                         ; b5e7: 8e ce 10    ...
    ldx #&ca                                                          ; b5ea: a2 ca       ..
    ldy #&10                                                          ; b5ec: a0 10       ..
    rts                                                               ; b5ee: 60          `

; &b5ef referenced 2 times by &b681, &b7ba
.start_wipe_pass
    jsr verify_ws_checksum                                            ; b5ef: 20 b2 8f     ..
    stx l10c8                                                         ; b5f2: 8e c8 10    ...
    lda l10b8,x                                                       ; b5f5: bd b8 10    ...
    ror a                                                             ; b5f8: 6a          j
    bcc cb657                                                         ; b5f9: 90 5c       .\
    lda l10d4                                                         ; b5fb: ad d4 10    ...
    pha                                                               ; b5fe: 48          H
    lda l10d5                                                         ; b5ff: ad d5 10    ...
    pha                                                               ; b602: 48          H
    lda l1078,x                                                       ; b603: bd 78 10    .x.
    sta l10d4                                                         ; b606: 8d d4 10    ...
    lda l1088,x                                                       ; b609: bd 88 10    ...
    sta l10d5                                                         ; b60c: 8d d5 10    ...
    jsr init_wipe_counters                                            ; b60f: 20 cc b5     ..
    dec l10cf                                                         ; b612: ce cf 10    ...
    dec l10d0                                                         ; b615: ce d0 10    ...
    ldx l10c8                                                         ; b618: ae c8 10    ...
    txa                                                               ; b61b: 8a          .
    clc                                                               ; b61c: 18          .
    adc #&11                                                          ; b61d: 69 11       i.
    sta l10cc                                                         ; b61f: 8d cc 10    ...
    lda l10b8,x                                                       ; b622: bd b8 10    ...
    and #&20 ; ' '                                                    ; b625: 29 20       )
    beq cb62f                                                         ; b627: f0 06       ..
    lda l1098,x                                                       ; b629: bd 98 10    ...
    sta l10cf                                                         ; b62c: 8d cf 10    ...
; &b62f referenced 1 time by &b627
.cb62f
    lda l10a8,x                                                       ; b62f: bd a8 10    ...
    sta l10ca                                                         ; b632: 8d ca 10    ...
    tax                                                               ; b635: aa          .
    ldy #&0e                                                          ; b636: a0 0e       ..
    lda (net_rx_ptr),y                                                ; b638: b1 9c       ..
    pha                                                               ; b63a: 48          H
    txa                                                               ; b63b: 8a          .
    sta (net_rx_ptr),y                                                ; b63c: 91 9c       ..
    ldx #&ca                                                          ; b63e: a2 ca       ..
    ldy #&10                                                          ; b640: a0 10       ..
    lda #0                                                            ; b642: a9 00       ..
    jsr send_and_receive                                              ; b644: 20 79 b9     y.
    ldx l10c8                                                         ; b647: ae c8 10    ...
    pla                                                               ; b64a: 68          h
    ldy #&0e                                                          ; b64b: a0 0e       ..
    sta (net_rx_ptr),y                                                ; b64d: 91 9c       ..
    pla                                                               ; b64f: 68          h
    sta l10d5                                                         ; b650: 8d d5 10    ...
    pla                                                               ; b653: 68          h
    sta l10d4                                                         ; b654: 8d d4 10    ...
; &b657 referenced 1 time by &b5f9
.cb657
    lda #&dc                                                          ; b657: a9 dc       ..
    and l10b8,x                                                       ; b659: 3d b8 10    =..
    sta l10b8,x                                                       ; b65c: 9d b8 10    ...
    rts                                                               ; b65f: 60          `

; &b660 referenced 2 times by &b735, &b8a2
.save_fcb_context
    ldx #&0c                                                          ; b660: a2 0c       ..
; &b662 referenced 1 time by &b66c
.loop_cb662
    lda l0f00,x                                                       ; b662: bd 00 0f    ...
    sta l10d9,x                                                       ; b665: 9d d9 10    ...
    lda fs_load_addr,x                                                ; b668: b5 b0       ..
    pha                                                               ; b66a: 48          H
    dex                                                               ; b66b: ca          .
    bpl loop_cb662                                                    ; b66c: 10 f4       ..
    cpy #0                                                            ; b66e: c0 00       ..
    bne cb675                                                         ; b670: d0 03       ..
    jmp cb720                                                         ; b672: 4c 20 b7    L .

; &b675 referenced 1 time by &b670
.cb675
    php                                                               ; b675: 08          .
    ldx #&ff                                                          ; b676: a2 ff       ..
; &b678 referenced 2 times by &b67c, &b67f
.cb678
    inx                                                               ; b678: e8          .
    lda l10b8,x                                                       ; b679: bd b8 10    ...
    bpl cb678                                                         ; b67c: 10 fa       ..
    asl a                                                             ; b67e: 0a          .
    bpl cb678                                                         ; b67f: 10 f7       ..
    jsr start_wipe_pass                                               ; b681: 20 ef b5     ..
    lda #&40 ; '@'                                                    ; b684: a9 40       .@
    sta l10b8,x                                                       ; b686: 9d b8 10    ...
    php                                                               ; b689: 08          .
    jsr find_open_fcb                                                 ; b68a: 20 89 b5     ..
    plp                                                               ; b68d: 28          (
    lda l10c9                                                         ; b68e: ad c9 10    ...
    sta l10ca                                                         ; b691: 8d ca 10    ...
    pha                                                               ; b694: 48          H
    tay                                                               ; b695: a8          .
    lda l1010,y                                                       ; b696: b9 10 10    ...
    sta l0f05                                                         ; b699: 8d 05 0f    ...
    pla                                                               ; b69c: 68          h
    sta l10a8,x                                                       ; b69d: 9d a8 10    ...
    lda l10d4                                                         ; b6a0: ad d4 10    ...
    sta l0f08                                                         ; b6a3: 8d 08 0f    ...
    sta l1078,x                                                       ; b6a6: 9d 78 10    .x.
    lda l10d5                                                         ; b6a9: ad d5 10    ...
    sta l0f09                                                         ; b6ac: 8d 09 0f    ...
    sta l1088,x                                                       ; b6af: 9d 88 10    ...
    txa                                                               ; b6b2: 8a          .
    clc                                                               ; b6b3: 18          .
    adc #&11                                                          ; b6b4: 69 11       i.
    sta l10cc                                                         ; b6b6: 8d cc 10    ...
    plp                                                               ; b6b9: 28          (
    bvc cb6cc                                                         ; b6ba: 50 10       P.
    ldx #0                                                            ; b6bc: a2 00       ..
    stx l0f06                                                         ; b6be: 8e 06 0f    ...
    inx                                                               ; b6c1: e8          .              ; X=&01
    stx l0f07                                                         ; b6c2: 8e 07 0f    ...
    ldy #&0d                                                          ; b6c5: a0 0d       ..
    ldx #5                                                            ; b6c7: a2 05       ..
    jsr save_net_tx_cb                                                ; b6c9: 20 99 94     ..
; &b6cc referenced 1 time by &b6ba
.cb6cc
    jsr init_wipe_counters                                            ; b6cc: 20 cc b5     ..
    ldy #&0e                                                          ; b6cf: a0 0e       ..
    lda (net_rx_ptr),y                                                ; b6d1: b1 9c       ..
    pha                                                               ; b6d3: 48          H
    lda l10ca                                                         ; b6d4: ad ca 10    ...
    sta (net_rx_ptr),y                                                ; b6d7: 91 9c       ..
    ldy #&10                                                          ; b6d9: a0 10       ..
    lda #2                                                            ; b6db: a9 02       ..
    jsr send_and_receive                                              ; b6dd: 20 79 b9     y.
    pla                                                               ; b6e0: 68          h
    ldy #&0e                                                          ; b6e1: a0 0e       ..
    sta (net_rx_ptr),y                                                ; b6e3: 91 9c       ..
    ldx l10c8                                                         ; b6e5: ae c8 10    ...
    lda l10d0                                                         ; b6e8: ad d0 10    ...
    bne cb6f2                                                         ; b6eb: d0 05       ..
    lda l10cf                                                         ; b6ed: ad cf 10    ...
    beq cb716                                                         ; b6f0: f0 24       .$
; &b6f2 referenced 1 time by &b6eb
.cb6f2
    lda l10cf                                                         ; b6f2: ad cf 10    ...
    eor #&ff                                                          ; b6f5: 49 ff       I.
    clc                                                               ; b6f7: 18          .
    adc #1                                                            ; b6f8: 69 01       i.
    sta l1098,x                                                       ; b6fa: 9d 98 10    ...
    lda #&20 ; ' '                                                    ; b6fd: a9 20       .
    ora l10b8,x                                                       ; b6ff: 1d b8 10    ...
    sta l10b8,x                                                       ; b702: 9d b8 10    ...
    lda l10cc                                                         ; b705: ad cc 10    ...
    sta fs_load_addr_3                                                ; b708: 85 b3       ..
    lda #0                                                            ; b70a: a9 00       ..
    sta fs_load_addr_2                                                ; b70c: 85 b2       ..
    ldy l1098,x                                                       ; b70e: bc 98 10    ...
; &b711 referenced 1 time by &b714
.loop_cb711
    sta (fs_load_addr_2),y                                            ; b711: 91 b2       ..
    iny                                                               ; b713: c8          .
    bne loop_cb711                                                    ; b714: d0 fb       ..
; &b716 referenced 1 time by &b6f0
.cb716
    lda #2                                                            ; b716: a9 02       ..
    ora l10b8,x                                                       ; b718: 1d b8 10    ...
    sta l10b8,x                                                       ; b71b: 9d b8 10    ...
    ldy #0                                                            ; b71e: a0 00       ..
; &b720 referenced 2 times by &b672, &b727
.cb720
    pla                                                               ; b720: 68          h
    sta fs_load_addr,y                                                ; b721: 99 b0 00    ...
    iny                                                               ; b724: c8          .
    cpy #&0d                                                          ; b725: c0 0d       ..
    bne cb720                                                         ; b727: d0 f7       ..
; &b729 referenced 1 time by &b8d3
.restore_catalog_entry
    ldy #&0c                                                          ; b729: a0 0c       ..
; &b72b referenced 1 time by &b732
.loop_cb72b
    lda l10d9,y                                                       ; b72b: b9 d9 10    ...
    sta l0f00,y                                                       ; b72e: 99 00 0f    ...
    dey                                                               ; b731: 88          .
    bpl loop_cb72b                                                    ; b732: 10 f7       ..
    rts                                                               ; b734: 60          `

; &b735 referenced 1 time by &b754
.loop_cb735
    jsr save_fcb_context                                              ; b735: 20 60 b6     `.
; &b738 referenced 3 times by &9dec, &b7ef, &b88e
.find_matching_fcb
    ldx #&ff                                                          ; b738: a2 ff       ..
; &b73a referenced 2 times by &b774, &b77c
.cb73a
    ldy l10c9                                                         ; b73a: ac c9 10    ...
; &b73d referenced 2 times by &b75c, &b762
.cb73d
    inx                                                               ; b73d: e8          .
    cpx #&10                                                          ; b73e: e0 10       ..
    bne cb757                                                         ; b740: d0 15       ..
    lda l10c9                                                         ; b742: ad c9 10    ...
    jsr attr_to_chan_index                                            ; b745: 20 5b b4     [.
    lda l1020,x                                                       ; b748: bd 20 10    . .
    sta l10d5                                                         ; b74b: 8d d5 10    ...
    lda l1010,x                                                       ; b74e: bd 10 10    ...
    sta l10d4                                                         ; b751: 8d d4 10    ...
    jmp loop_cb735                                                    ; b754: 4c 35 b7    L5.

; &b757 referenced 1 time by &b740
.cb757
    lda l10b8,x                                                       ; b757: bd b8 10    ...
    and #2                                                            ; b75a: 29 02       ).
    beq cb73d                                                         ; b75c: f0 df       ..
    tya                                                               ; b75e: 98          .
    cmp l10a8,x                                                       ; b75f: dd a8 10    ...
    bne cb73d                                                         ; b762: d0 d9       ..
    stx l10c8                                                         ; b764: 8e c8 10    ...
    sec                                                               ; b767: 38          8
    sbc #&20 ; ' '                                                    ; b768: e9 20       .
    tay                                                               ; b76a: a8          .
    ldx l10c8                                                         ; b76b: ae c8 10    ...
    lda l1010,y                                                       ; b76e: b9 10 10    ...
    cmp l1078,x                                                       ; b771: dd 78 10    .x.
    bne cb73a                                                         ; b774: d0 c4       ..
    lda l1020,y                                                       ; b776: b9 20 10    . .
    cmp l1088,x                                                       ; b779: dd 88 10    ...
    bne cb73a                                                         ; b77c: d0 bc       ..
    lda l10b8,x                                                       ; b77e: bd b8 10    ...
    bpl cb78e                                                         ; b781: 10 0b       ..
    and #&7f                                                          ; b783: 29 7f       ).
    sta l10b8,x                                                       ; b785: 9d b8 10    ...
    jsr find_open_fcb                                                 ; b788: 20 89 b5     ..
    lda l10b8,x                                                       ; b78b: bd b8 10    ...
; &b78e referenced 1 time by &b781
.cb78e
    and #&20 ; ' '                                                    ; b78e: 29 20       )
    rts                                                               ; b790: 60          `

; &b791 referenced 2 times by &b836, &b910
.inc_fcb_byte_count
    inc l1000,x                                                       ; b791: fe 00 10    ...
    bne return_35                                                     ; b794: d0 08       ..
    inc l1010,x                                                       ; b796: fe 10 10    ...
    bne return_35                                                     ; b799: d0 03       ..
    inc l1020,x                                                       ; b79b: fe 20 10    . .
; &b79e referenced 2 times by &b794, &b799
.return_35
    rts                                                               ; b79e: 60          `

; &b79f referenced 8 times by &8d7c, &8f87, &948c, &9bcd, &9c13, &9cb6, &9d7e, &9e4c
.process_all_fcbs
    txa                                                               ; b79f: 8a          .
    pha                                                               ; b7a0: 48          H
    tya                                                               ; b7a1: 98          .
    pha                                                               ; b7a2: 48          H
    lda fs_options                                                    ; b7a3: a5 bb       ..
    pha                                                               ; b7a5: 48          H
    lda fs_block_offset                                               ; b7a6: a5 bc       ..
    pha                                                               ; b7a8: 48          H
    ldx #&0f                                                          ; b7a9: a2 0f       ..
    stx l10c8                                                         ; b7ab: 8e c8 10    ...
; &b7ae referenced 1 time by &b7c2
.loop_cb7ae
    ldx l10c8                                                         ; b7ae: ae c8 10    ...
    tya                                                               ; b7b1: 98          .
    beq cb7b9                                                         ; b7b2: f0 05       ..
    cmp l10a8,x                                                       ; b7b4: dd a8 10    ...
    bne cb7bf                                                         ; b7b7: d0 06       ..
; &b7b9 referenced 1 time by &b7b2
.cb7b9
    pha                                                               ; b7b9: 48          H
    jsr start_wipe_pass                                               ; b7ba: 20 ef b5     ..
    pla                                                               ; b7bd: 68          h
    tay                                                               ; b7be: a8          .
; &b7bf referenced 1 time by &b7b7
.cb7bf
    dec l10c8                                                         ; b7bf: ce c8 10    ...
    bpl loop_cb7ae                                                    ; b7c2: 10 ea       ..
    pla                                                               ; b7c4: 68          h
    sta fs_block_offset                                               ; b7c5: 85 bc       ..
    pla                                                               ; b7c7: 68          h
    sta fs_options                                                    ; b7c8: 85 bb       ..
    pla                                                               ; b7ca: 68          h
    tay                                                               ; b7cb: a8          .
    pla                                                               ; b7cc: 68          h
    tax                                                               ; b7cd: aa          .
    rts                                                               ; b7ce: 60          `

    sty l10c9                                                         ; b7cf: 8c c9 10    ...
    txa                                                               ; b7d2: 8a          .
    pha                                                               ; b7d3: 48          H
    jsr store_result_check_dir                                        ; b7d4: 20 dc b4     ..
    lda l1060,x                                                       ; b7d7: bd 60 10    .`.
    and #&20 ; ' '                                                    ; b7da: 29 20       )
    beq cb7ee                                                         ; b7dc: f0 10       ..
    lda #&d4                                                          ; b7de: a9 d4       ..
    jsr error_inline_log                                              ; b7e0: 20 bb 96     ..
    equs "Write only", 0                                              ; b7e3: 57 72 69... Wri

; &b7ee referenced 1 time by &b7dc
.cb7ee
    clv                                                               ; b7ee: b8          .
    jsr find_matching_fcb                                             ; b7ef: 20 38 b7     8.
    beq cb82a                                                         ; b7f2: f0 36       .6
    lda l1000,y                                                       ; b7f4: b9 00 10    ...
    cmp l1098,x                                                       ; b7f7: dd 98 10    ...
    bcc cb82a                                                         ; b7fa: 90 2e       ..
    lda l1060,y                                                       ; b7fc: b9 60 10    .`.
    tax                                                               ; b7ff: aa          .
    and #&40 ; '@'                                                    ; b800: 29 40       )@
    bne cb819                                                         ; b802: d0 15       ..
    txa                                                               ; b804: 8a          .
    ora #&40 ; '@'                                                    ; b805: 09 40       .@
    sta l1060,y                                                       ; b807: 99 60 10    .`.
    lda #0                                                            ; b80a: a9 00       ..
    ldy #&0e                                                          ; b80c: a0 0e       ..
    sta (net_rx_ptr),y                                                ; b80e: 91 9c       ..
    pla                                                               ; b810: 68          h
    tax                                                               ; b811: aa          .
    lda #&fe                                                          ; b812: a9 fe       ..
    ldy l10c9                                                         ; b814: ac c9 10    ...
    sec                                                               ; b817: 38          8
    rts                                                               ; b818: 60          `

; &b819 referenced 1 time by &b802
.cb819
    lda #&df                                                          ; b819: a9 df       ..
    jsr error_inline_log                                              ; b81b: 20 bb 96     ..
    equs "End of file", 0                                             ; b81e: 45 6e 64... End

; &b82a referenced 2 times by &b7f2, &b7fa
.cb82a
    lda l1000,y                                                       ; b82a: b9 00 10    ...
    pha                                                               ; b82d: 48          H
    tya                                                               ; b82e: 98          .
    tax                                                               ; b82f: aa          .
    lda #0                                                            ; b830: a9 00       ..
    ldy #&0e                                                          ; b832: a0 0e       ..
    sta (net_rx_ptr),y                                                ; b834: 91 9c       ..
    jsr inc_fcb_byte_count                                            ; b836: 20 91 b7     ..
    pla                                                               ; b839: 68          h
    tay                                                               ; b83a: a8          .
    lda l10c8                                                         ; b83b: ad c8 10    ...
    clc                                                               ; b83e: 18          .
    adc #&11                                                          ; b83f: 69 11       i.
    sta fs_load_addr_3                                                ; b841: 85 b3       ..
    lda #0                                                            ; b843: a9 00       ..
    sta fs_load_addr_2                                                ; b845: 85 b2       ..
    pla                                                               ; b847: 68          h
    tax                                                               ; b848: aa          .
    lda (fs_load_addr_2),y                                            ; b849: b1 b2       ..
    ldy l10c9                                                         ; b84b: ac c9 10    ...
    clc                                                               ; b84e: 18          .
    rts                                                               ; b84f: 60          `

    sty l10c9                                                         ; b850: 8c c9 10    ...
    pha                                                               ; b853: 48          H
    tay                                                               ; b854: a8          .
    txa                                                               ; b855: 8a          .
    pha                                                               ; b856: 48          H
    tya                                                               ; b857: 98          .
    pha                                                               ; b858: 48          H
    sta l10d7                                                         ; b859: 8d d7 10    ...
    jsr store_result_check_dir                                        ; b85c: 20 dc b4     ..
    lda l1060,x                                                       ; b85f: bd 60 10    .`.
    bmi cb87d                                                         ; b862: 30 19       0.
    equb &a9                                                          ; b864: a9          .

    cmp (tube_send_zero_r2,x)                                         ; b865: c1 20       .
    equb &bb, &96                                                     ; b867: bb 96       ..
    equs "Not open for update", 0                                     ; b869: 4e 6f 74... Not

; &b87d referenced 1 time by &b862
.cb87d
    and #&20 ; ' '                                                    ; b87d: 29 20       )
    beq cb88b                                                         ; b87f: f0 0a       ..
    ldy l1030,x                                                       ; b881: bc 30 10    .0.
    pla                                                               ; b884: 68          h
    jsr send_wipe_request                                             ; b885: 20 20 b9      .
    jmp cb910                                                         ; b888: 4c 10 b9    L..

; &b88b referenced 1 time by &b87f
.cb88b
    bit bit_test_ff_pad                                               ; b88b: 2c 7d 94    ,}.
    jsr find_matching_fcb                                             ; b88e: 20 38 b7     8.
    lda l1000,y                                                       ; b891: b9 00 10    ...
    cmp #&ff                                                          ; b894: c9 ff       ..
    bne cb8dd                                                         ; b896: d0 45       .E
    txa                                                               ; b898: 8a          .
    pha                                                               ; b899: 48          H
    tya                                                               ; b89a: 98          .
    pha                                                               ; b89b: 48          H
    lda l1030,y                                                       ; b89c: b9 30 10    .0.
    pha                                                               ; b89f: 48          H
    ldy #0                                                            ; b8a0: a0 00       ..
    jsr save_fcb_context                                              ; b8a2: 20 60 b6     `.
    pla                                                               ; b8a5: 68          h
    sta l0f05                                                         ; b8a6: 8d 05 0f    ...
    tax                                                               ; b8a9: aa          .
    pla                                                               ; b8aa: 68          h
    tay                                                               ; b8ab: a8          .
    pha                                                               ; b8ac: 48          H
    txa                                                               ; b8ad: 8a          .
    pha                                                               ; b8ae: 48          H
    ldx #0                                                            ; b8af: a2 00       ..
    stx l0f06                                                         ; b8b1: 8e 06 0f    ...
    dex                                                               ; b8b4: ca          .              ; X=&ff
    stx l0f07                                                         ; b8b5: 8e 07 0f    ...
    lda l1010,y                                                       ; b8b8: b9 10 10    ...
    sta l0f08                                                         ; b8bb: 8d 08 0f    ...
    lda l1020,y                                                       ; b8be: b9 20 10    . .
    sta l0f09                                                         ; b8c1: 8d 09 0f    ...
    ldy #&0d                                                          ; b8c4: a0 0d       ..
    ldx #5                                                            ; b8c6: a2 05       ..
    jsr save_net_tx_cb                                                ; b8c8: 20 99 94     ..
    pla                                                               ; b8cb: 68          h
    tay                                                               ; b8cc: a8          .
    lda l10d7                                                         ; b8cd: ad d7 10    ...
    jsr send_wipe_request                                             ; b8d0: 20 20 b9      .
    jsr restore_catalog_entry                                         ; b8d3: 20 29 b7     ).
    pla                                                               ; b8d6: 68          h
    tay                                                               ; b8d7: a8          .
    pla                                                               ; b8d8: 68          h
    tax                                                               ; b8d9: aa          .
    lda l1000,y                                                       ; b8da: b9 00 10    ...
; &b8dd referenced 1 time by &b896
.cb8dd
    cmp l1098,x                                                       ; b8dd: dd 98 10    ...
    bcc cb8f1                                                         ; b8e0: 90 0f       ..
    adc #0                                                            ; b8e2: 69 00       i.
    sta l1098,x                                                       ; b8e4: 9d 98 10    ...
    bne cb8f1                                                         ; b8e7: d0 08       ..
    lda #&df                                                          ; b8e9: a9 df       ..
    and l10b8,x                                                       ; b8eb: 3d b8 10    =..
    sta l10b8,x                                                       ; b8ee: 9d b8 10    ...
; &b8f1 referenced 2 times by &b8e0, &b8e7
.cb8f1
    lda #1                                                            ; b8f1: a9 01       ..
    ora l10b8,x                                                       ; b8f3: 1d b8 10    ...
    sta l10b8,x                                                       ; b8f6: 9d b8 10    ...
    lda l1000,y                                                       ; b8f9: b9 00 10    ...
    pha                                                               ; b8fc: 48          H
    tya                                                               ; b8fd: 98          .
    tax                                                               ; b8fe: aa          .
    pla                                                               ; b8ff: 68          h
    tay                                                               ; b900: a8          .
    lda l10c8                                                         ; b901: ad c8 10    ...
    clc                                                               ; b904: 18          .
    adc #&11                                                          ; b905: 69 11       i.
    sta fs_load_addr_3                                                ; b907: 85 b3       ..
    lda #0                                                            ; b909: a9 00       ..
    sta fs_load_addr_2                                                ; b90b: 85 b2       ..
    pla                                                               ; b90d: 68          h
    sta (fs_load_addr_2),y                                            ; b90e: 91 b2       ..
; &b910 referenced 1 time by &b888
.cb910
    jsr inc_fcb_byte_count                                            ; b910: 20 91 b7     ..
    lda #0                                                            ; b913: a9 00       ..
    ldy #&0e                                                          ; b915: a0 0e       ..
    sta (net_rx_ptr),y                                                ; b917: 91 9c       ..
    pla                                                               ; b919: 68          h
    tax                                                               ; b91a: aa          .
    pla                                                               ; b91b: 68          h
    ldy l10c9                                                         ; b91c: ac c9 10    ...
    rts                                                               ; b91f: 60          `

; &b920 referenced 2 times by &b885, &b8d0
.send_wipe_request
    sty l0fde                                                         ; b920: 8c de 0f    ...
    sta l0fdf                                                         ; b923: 8d df 0f    ...
    tya                                                               ; b926: 98          .
    pha                                                               ; b927: 48          H
    txa                                                               ; b928: 8a          .
    pha                                                               ; b929: 48          H
    lda #&90                                                          ; b92a: a9 90       ..
    sta l0fdc                                                         ; b92c: 8d dc 0f    ...
    jsr init_txcb                                                     ; b92f: 20 5f 94     _.
    lda #&dc                                                          ; b932: a9 dc       ..
    sta txcb_start                                                    ; b934: 85 c4       ..
    lda #&e0                                                          ; b936: a9 e0       ..
    sta txcb_end                                                      ; b938: 85 c8       ..
    lda #9                                                            ; b93a: a9 09       ..
    sta l0fdd                                                         ; b93c: 8d dd 0f    ...
    ldx #&c0                                                          ; b93f: a2 c0       ..
    ldy #0                                                            ; b941: a0 00       ..
    lda l0fde                                                         ; b943: ad de 0f    ...
    jsr send_disconnect_reply                                         ; b946: 20 12 ac     ..
    lda l0fdd                                                         ; b949: ad dd 0f    ...
    beq cb969                                                         ; b94c: f0 1b       ..
    sta l0e09                                                         ; b94e: 8d 09 0e    ...
    ldx #0                                                            ; b951: a2 00       ..
; &b953 referenced 1 time by &b95e
.loop_cb953
    lda l0fdc,x                                                       ; b953: bd dc 0f    ...
    sta error_block,x                                                 ; b956: 9d 00 01    ...
    cmp #&0d                                                          ; b959: c9 0d       ..
    beq cb960                                                         ; b95b: f0 03       ..
    inx                                                               ; b95d: e8          .
    bne loop_cb953                                                    ; b95e: d0 f3       ..
; &b960 referenced 1 time by &b95b
.cb960
    lda #0                                                            ; b960: a9 00       ..
    sta error_block,x                                                 ; b962: 9d 00 01    ...
    dex                                                               ; b965: ca          .
    jmp check_net_error_code                                          ; b966: 4c da 96    L..

; &b969 referenced 1 time by &b94c
.cb969
    ldx l10c9                                                         ; b969: ae c9 10    ...
    lda l1040,x                                                       ; b96c: bd 40 10    .@.
    eor #1                                                            ; b96f: 49 01       I.
    sta l1040,x                                                       ; b971: 9d 40 10    .@.
    pla                                                               ; b974: 68          h
    tax                                                               ; b975: aa          .
    pla                                                               ; b976: 68          h
    tay                                                               ; b977: a8          .
    rts                                                               ; b978: 60          `

; &b979 referenced 2 times by &b644, &b6dd
.send_and_receive
    jsr set_options_ptr                                               ; b979: 20 87 92     ..
    jmp setup_transfer_workspace                                      ; b97c: 4c cb 9e    L..

; ***************************************************************************************
; *Close command.
; Closes all open files via OSFIND #0.
; ***************************************************************************************
.cmd_close
    lda #osfind_close                                                 ; b97f: a9 00       ..             ; A=0: close all open files
    tay                                                               ; b981: a8          .              ; Y=&00
    jmp osfind                                                        ; b982: 4c ce ff    L..            ; Close all files (Y=0)

; ***************************************************************************************
; *Type command.
; Displays file contents to screen.
; ***************************************************************************************
.cmd_type
    clv                                                               ; b985: b8          .              ; Clear V for unconditional BVC
    bvc open_and_read_file                                            ; b986: 50 03       P.             ; ALWAYS branch

; ***************************************************************************************
; *Print command.
; Sends file to printer server with
; optional page formatting.
; ***************************************************************************************
.cmd_print
    bit bit_test_ff_pad                                               ; b988: 2c 7d 94    ,}.            ; Set V flag (= print mode)
; &b98b referenced 1 time by &b986
.open_and_read_file
    jsr open_file_for_read                                            ; b98b: 20 13 bb     ..            ; Open file for reading
    ldy ws_page                                                       ; b98e: a4 a8       ..             ; Y=file handle
    lda #0                                                            ; b990: a9 00       ..             ; A = 0
    sta l00ad                                                         ; b992: 85 ad       ..             ; Clear previous-character tracker
    php                                                               ; b994: 08          .              ; Save V flag (print/type mode)
; &b995 referenced 3 times by &b9b5, &b9d5, &b9e8
.cb995
    jsr osbget                                                        ; b995: 20 d7 ff     ..            ; Read a single byte from an open file Y
    bcc cb9a1                                                         ; b998: 90 07       ..             ; Branch if not end of file
    plp                                                               ; b99a: 28          (              ; EOF: restore processor status
    jsr close_ws_file                                                 ; b99b: 20 0c bb     ..            ; Close the file
    jmp osnewl                                                        ; b99e: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &b9a1 referenced 1 time by &b998
.cb9a1
    jsr abort_if_escape                                               ; b9a1: 20 ea b9     ..            ; Check for escape key pressed
    plp                                                               ; b9a4: 28          (              ; Restore V (print/type mode)
    php                                                               ; b9a5: 08          .              ; Re-save for next iteration
    bvs cb9b0                                                         ; b9a6: 70 08       p.             ; Print mode: skip CR/LF handling
    cmp #&0d                                                          ; b9a8: c9 0d       ..             ; Is it a carriage return?
    beq cb9b8                                                         ; b9aa: f0 0c       ..             ; Yes: handle line ending
    cmp #&0a                                                          ; b9ac: c9 0a       ..             ; Is it a line feed?
    beq cb9b8                                                         ; b9ae: f0 08       ..             ; Yes: handle line ending
; &b9b0 referenced 1 time by &b9a6
.cb9b0
    sta l00ad                                                         ; b9b0: 85 ad       ..             ; Save as previous character
; &b9b2 referenced 1 time by &b9c3
.loop_cb9b2
    jsr oswrch                                                        ; b9b2: 20 ee ff     ..            ; Write character
    jmp cb995                                                         ; b9b5: 4c 95 b9    L..            ; Loop for next byte

; &b9b8 referenced 2 times by &b9aa, &b9ae
.cb9b8
    pha                                                               ; b9b8: 48          H              ; Save the CR or LF character
    ldx l026a                                                         ; b9b9: ae 6a 02    .j.            ; Check output destination flag
    beq cb9c5                                                         ; b9bc: f0 07       ..             ; Zero: normalise line endings
    lda #0                                                            ; b9be: a9 00       ..             ; Non-zero: output raw
    sta l00ad                                                         ; b9c0: 85 ad       ..             ; Clear previous-character tracker
    pla                                                               ; b9c2: 68          h              ; Retrieve CR/LF
    bne loop_cb9b2                                                    ; b9c3: d0 ed       ..             ; Output it directly; ALWAYS branch
; &b9c5 referenced 1 time by &b9bc
.cb9c5
    lda l00ad                                                         ; b9c5: a5 ad       ..             ; Get previous character
    cmp #&0d                                                          ; b9c7: c9 0d       ..             ; Was previous a CR?
    beq cb9d8                                                         ; b9c9: f0 0d       ..             ; Yes: check for CR+LF pair
    cmp #&0a                                                          ; b9cb: c9 0a       ..             ; Was previous a LF?
    beq cb9df                                                         ; b9cd: f0 10       ..             ; Yes: check for LF+CR pair
    pla                                                               ; b9cf: 68          h              ; Retrieve CR/LF from stack
    sta l00ad                                                         ; b9d0: 85 ad       ..             ; Save as previous character
; &b9d2 referenced 2 times by &b9dd, &b9e2
.cb9d2
    jsr osnewl                                                        ; b9d2: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    jmp cb995                                                         ; b9d5: 4c 95 b9    L..            ; Loop for next byte

; &b9d8 referenced 1 time by &b9c9
.cb9d8
    pla                                                               ; b9d8: 68          h              ; Retrieve current character
    cmp #&0a                                                          ; b9d9: c9 0a       ..             ; Is it LF? (CR+LF pair)
    beq cb9e4                                                         ; b9db: f0 07       ..             ; Yes: consume LF, no extra newline
    bne cb9d2                                                         ; b9dd: d0 f3       ..             ; No: output extra newline; ALWAYS branch

; &b9df referenced 1 time by &b9cd
.cb9df
    pla                                                               ; b9df: 68          h              ; Retrieve current character
    cmp #&0d                                                          ; b9e0: c9 0d       ..             ; Is it CR? (LF+CR pair)
    bne cb9d2                                                         ; b9e2: d0 ee       ..             ; No: output extra newline
; &b9e4 referenced 1 time by &b9db
.cb9e4
    lda #0                                                            ; b9e4: a9 00       ..             ; Pair consumed: A = 0
    sta l00ad                                                         ; b9e6: 85 ad       ..             ; Clear previous-character tracker
    beq cb995                                                         ; b9e8: f0 ab       ..             ; Loop for next byte; ALWAYS branch; ALWAYS branch

; &b9ea referenced 2 times by &b9a1, &ba1e
.abort_if_escape
    bit escape_flag                                                   ; b9ea: 24 ff       $.             ; Test bit 7 of escape flag
    bmi cb9ef                                                         ; b9ec: 30 01       0.             ; Escape pressed: handle abort
    rts                                                               ; b9ee: 60          `              ; No escape: return

; &b9ef referenced 1 time by &b9ec
.cb9ef
    jsr close_ws_file                                                 ; b9ef: 20 0c bb     ..            ; Close the open file
    jsr osnewl                                                        ; b9f2: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    lda #osbyte_acknowledge_escape                                    ; b9f5: a9 7e       .~             ; Acknowledge escape condition
    jsr osbyte                                                        ; b9f7: 20 f4 ff     ..            ; Clear escape condition and perform escape effects
    lda #&11                                                          ; b9fa: a9 11       ..             ; Error number &11
    jsr error_inline                                                  ; b9fc: 20 be 96     ..            ; Generate 'Escape' BRK error
    equs "Escape", 0                                                  ; b9ff: 45 73 63... Esc

; ***************************************************************************************
; *Dump command.
; Displays file contents in hex and
; ASCII format, 8 bytes per line.
; ***************************************************************************************
.cmd_dump
    jsr open_file_for_read                                            ; ba06: 20 13 bb     ..
    ldx #&14                                                          ; ba09: a2 14       ..
    lda #0                                                            ; ba0b: a9 00       ..
; &ba0d referenced 1 time by &ba0f
.loop_cba0d
    pha                                                               ; ba0d: 48          H
    dex                                                               ; ba0e: ca          .
    bpl loop_cba0d                                                    ; ba0f: 10 fc       ..
    tsx                                                               ; ba11: ba          .
    jsr init_dump_buffer                                              ; ba12: 20 be bb     ..
    lda (l00ae),y                                                     ; ba15: b1 ae       ..
    and #&f0                                                          ; ba17: 29 f0       ).
    beq cba1e                                                         ; ba19: f0 03       ..
    jsr print_dump_header                                             ; ba1b: 20 ce ba     ..
; &ba1e referenced 2 times by &ba19, &bac6
.cba1e
    jsr abort_if_escape                                               ; ba1e: 20 ea b9     ..
    lda #&ff                                                          ; ba21: a9 ff       ..
    sta osword_flag                                                   ; ba23: 85 aa       ..
; &ba25 referenced 1 time by &ba34
.loop_cba25
    ldy ws_page                                                       ; ba25: a4 a8       ..             ; Y=file handle
    jsr osbget                                                        ; ba27: 20 d7 ff     ..            ; Read a single byte from an open file Y
    bcs cba37                                                         ; ba2a: b0 0b       ..
    inc osword_flag                                                   ; ba2c: e6 aa       ..
    ldy osword_flag                                                   ; ba2e: a4 aa       ..
    sta (l00ae),y                                                     ; ba30: 91 ae       ..
    cpy #&0f                                                          ; ba32: c0 0f       ..
    bne loop_cba25                                                    ; ba34: d0 ef       ..
    clc                                                               ; ba36: 18          .
; &ba37 referenced 1 time by &ba2a
.cba37
    php                                                               ; ba37: 08          .
    lda osword_flag                                                   ; ba38: a5 aa       ..
    bpl cba45                                                         ; ba3a: 10 09       ..
    ldx #&15                                                          ; ba3c: a2 15       ..
; &ba3e referenced 2 times by &ba40, &bacb
.cba3e
    pla                                                               ; ba3e: 68          h
    dex                                                               ; ba3f: ca          .
    bpl cba3e                                                         ; ba40: 10 fc       ..
    jmp close_ws_file                                                 ; ba42: 4c 0c bb    L..

; &ba45 referenced 1 time by &ba3a
.cba45
    ldy #&10                                                          ; ba45: a0 10       ..
    lda (l00ae),y                                                     ; ba47: b1 ae       ..
    and #&f0                                                          ; ba49: 29 f0       ).
    bne cba50                                                         ; ba4b: d0 03       ..
    jsr print_dump_header                                             ; ba4d: 20 ce ba     ..
; &ba50 referenced 1 time by &ba4b
.cba50
    ldy #&13                                                          ; ba50: a0 13       ..
; &ba52 referenced 1 time by &ba5c
.loop_cba52
    lda (l00ae),y                                                     ; ba52: b1 ae       ..
    pha                                                               ; ba54: 48          H
    jsr print_hex_byte                                                ; ba55: 20 1b 91     ..
    pla                                                               ; ba58: 68          h
    dey                                                               ; ba59: 88          .
    cpy #&0f                                                          ; ba5a: c0 0f       ..
    bne loop_cba52                                                    ; ba5c: d0 f4       ..
    iny                                                               ; ba5e: c8          .
    clc                                                               ; ba5f: 18          .
    adc #&10                                                          ; ba60: 69 10       i.
    php                                                               ; ba62: 08          .
; &ba63 referenced 1 time by &ba6e
.loop_cba63
    plp                                                               ; ba63: 28          (
    sta (l00ae),y                                                     ; ba64: 91 ae       ..
    iny                                                               ; ba66: c8          .
    lda (l00ae),y                                                     ; ba67: b1 ae       ..
    adc #0                                                            ; ba69: 69 00       i.
    php                                                               ; ba6b: 08          .
    cpy #&14                                                          ; ba6c: c0 14       ..
    bne loop_cba63                                                    ; ba6e: d0 f3       ..
    plp                                                               ; ba70: 28          (
    jsr print_inline                                                  ; ba71: 20 31 91     1.
    equs " : "                                                        ; ba74: 20 3a 20     :

    ldy #0                                                            ; ba77: a0 00       ..
    ldx osword_flag                                                   ; ba79: a6 aa       ..
; &ba7b referenced 1 time by &ba8b
.loop_cba7b
    lda (l00ae),y                                                     ; ba7b: b1 ae       ..
    jsr print_hex_byte                                                ; ba7d: 20 1b 91     ..
    lda #&20 ; ' '                                                    ; ba80: a9 20       .
    jsr osasci                                                        ; ba82: 20 e3 ff     ..            ; Write character 32
; &ba85 referenced 1 time by &ba98
.loop_cba85
    iny                                                               ; ba85: c8          .
    cpy #&10                                                          ; ba86: c0 10       ..
    beq cba9b                                                         ; ba88: f0 11       ..
    dex                                                               ; ba8a: ca          .
    bpl loop_cba7b                                                    ; ba8b: 10 ee       ..
    tya                                                               ; ba8d: 98          .
    pha                                                               ; ba8e: 48          H
    jsr print_inline                                                  ; ba8f: 20 31 91     1.
    equs "   "                                                        ; ba92: 20 20 20

    nop                                                               ; ba95: ea          .
    pla                                                               ; ba96: 68          h
    tay                                                               ; ba97: a8          .
    jmp loop_cba85                                                    ; ba98: 4c 85 ba    L..

; &ba9b referenced 1 time by &ba88
.cba9b
    dex                                                               ; ba9b: ca          .
    jsr print_inline                                                  ; ba9c: 20 31 91     1.
    equs ": "                                                         ; ba9f: 3a 20       :

    nop                                                               ; baa1: ea          .
    jsr advance_x_by_8                                                ; baa2: 20 84 bc     ..
    ldy #0                                                            ; baa5: a0 00       ..
; &baa7 referenced 1 time by &babe
.loop_cbaa7
    lda (l00ae),y                                                     ; baa7: b1 ae       ..
    and #&7f                                                          ; baa9: 29 7f       ).
    cmp #&20 ; ' '                                                    ; baab: c9 20       .
    bcs cbab1                                                         ; baad: b0 02       ..
; &baaf referenced 1 time by &bab3
.loop_cbaaf
    lda #&2e ; '.'                                                    ; baaf: a9 2e       ..
; &bab1 referenced 1 time by &baad
.cbab1
    cmp #&7f                                                          ; bab1: c9 7f       ..
    beq loop_cbaaf                                                    ; bab3: f0 fa       ..
    jsr osasci                                                        ; bab5: 20 e3 ff     ..            ; Write character
    iny                                                               ; bab8: c8          .
    cpy #&10                                                          ; bab9: c0 10       ..
    beq cbac0                                                         ; babb: f0 03       ..
    dex                                                               ; babd: ca          .
    bpl loop_cbaa7                                                    ; babe: 10 e7       ..
; &bac0 referenced 1 time by &babb
.cbac0
    jsr osnewl                                                        ; bac0: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    plp                                                               ; bac3: 28          (
    bcs cbac9                                                         ; bac4: b0 03       ..
    jmp cba1e                                                         ; bac6: 4c 1e ba    L..

; &bac9 referenced 1 time by &bac4
.cbac9
    ldx #&14                                                          ; bac9: a2 14       ..
    jmp cba3e                                                         ; bacb: 4c 3e ba    L>.

; &bace referenced 2 times by &ba1b, &ba4d
.print_dump_header
    lda (l00ae),y                                                     ; bace: b1 ae       ..
    pha                                                               ; bad0: 48          H
    jsr print_inline                                                  ; bad1: 20 31 91     1.
    equs &0d, "Address  : "                                           ; bad4: 0d 41 64... .Ad

    nop                                                               ; bae0: ea          .
    pla                                                               ; bae1: 68          h
    ldx #&0f                                                          ; bae2: a2 0f       ..
; &bae4 referenced 1 time by &baf4
.loop_cbae4
    pha                                                               ; bae4: 48          H
    jsr print_hex_byte                                                ; bae5: 20 1b 91     ..
    lda #&20 ; ' '                                                    ; bae8: a9 20       .
    jsr osasci                                                        ; baea: 20 e3 ff     ..            ; Write character 32
    pla                                                               ; baed: 68          h
    sec                                                               ; baee: 38          8
    adc #0                                                            ; baef: 69 00       i.
    and #&0f                                                          ; baf1: 29 0f       ).
    dex                                                               ; baf3: ca          .
    bpl loop_cbae4                                                    ; baf4: 10 ee       ..
    jsr print_inline                                                  ; baf6: 20 31 91     1.
    equs ":    ASCII data", &0d, &0d                                  ; baf9: 3a 20 20... :

    nop                                                               ; bb0a: ea          .
    rts                                                               ; bb0b: 60          `

; &bb0c referenced 6 times by &b99b, &b9ef, &ba42, &bbaf, &bbe9, &bc56
.close_ws_file
    ldy ws_page                                                       ; bb0c: a4 a8       ..
    lda #osfind_close                                                 ; bb0e: a9 00       ..
    jmp osfind                                                        ; bb10: 4c ce ff    L..            ; Close one or all files

; &bb13 referenced 2 times by &b98b, &ba06
.open_file_for_read
    php                                                               ; bb13: 08          .
    tya                                                               ; bb14: 98          .
    clc                                                               ; bb15: 18          .
    adc os_text_ptr                                                   ; bb16: 65 f2       e.
    pha                                                               ; bb18: 48          H
    tax                                                               ; bb19: aa          .
    lda #0                                                            ; bb1a: a9 00       ..
    adc os_text_ptr_hi                                                ; bb1c: 65 f3       e.
    pha                                                               ; bb1e: 48          H
    tay                                                               ; bb1f: a8          .
    lda #osfind_open_input                                            ; bb20: a9 40       .@
    jsr osfind                                                        ; bb22: 20 ce ff     ..            ; Open file for input (A=64)
    tay                                                               ; bb25: a8          .              ; A=file handle (or zero on failure)
    sta ws_page                                                       ; bb26: 85 a8       ..
    bne cbb39                                                         ; bb28: d0 0f       ..
    lda #&d6                                                          ; bb2a: a9 d6       ..
    jsr error_inline                                                  ; bb2c: 20 be 96     ..
    equs "Not found", 0                                               ; bb2f: 4e 6f 74... Not

; &bb39 referenced 1 time by &bb28
.cbb39
    pla                                                               ; bb39: 68          h
    sta os_text_ptr_hi                                                ; bb3a: 85 f3       ..
    pla                                                               ; bb3c: 68          h
    sta os_text_ptr                                                   ; bb3d: 85 f2       ..
    ldy #0                                                            ; bb3f: a0 00       ..
; &bb41 referenced 1 time by &bb4a
.loop_cbb41
    iny                                                               ; bb41: c8          .
    lda (os_text_ptr),y                                               ; bb42: b1 f2       ..
    cmp #&0d                                                          ; bb44: c9 0d       ..
    beq cbb53                                                         ; bb46: f0 0b       ..
    cmp #&20 ; ' '                                                    ; bb48: c9 20       .
    bne loop_cbb41                                                    ; bb4a: d0 f5       ..
; &bb4c referenced 1 time by &bb51
.loop_cbb4c
    iny                                                               ; bb4c: c8          .
    lda (os_text_ptr),y                                               ; bb4d: b1 f2       ..
    cmp #&20 ; ' '                                                    ; bb4f: c9 20       .
    beq loop_cbb4c                                                    ; bb51: f0 f9       ..
; &bb53 referenced 1 time by &bb46
.cbb53
    plp                                                               ; bb53: 28          (
    rts                                                               ; bb54: 60          `

; &bb55 referenced 2 times by &bbc5, &bc51
.parse_dump_range
    tya                                                               ; bb55: 98          .
    tax                                                               ; bb56: aa          .
    lda #0                                                            ; bb57: a9 00       ..
    tay                                                               ; bb59: a8          .              ; Y=&00
; &bb5a referenced 1 time by &bb5f
.loop_cbb5a
    sta (l00ae),y                                                     ; bb5a: 91 ae       ..
    iny                                                               ; bb5c: c8          .
    cpy #4                                                            ; bb5d: c0 04       ..
    bne loop_cbb5a                                                    ; bb5f: d0 f9       ..
; &bb61 referenced 1 time by &bba8
.cbb61
    txa                                                               ; bb61: 8a          .
    inx                                                               ; bb62: e8          .
    tay                                                               ; bb63: a8          .
    lda (os_text_ptr),y                                               ; bb64: b1 f2       ..
    cmp #&0d                                                          ; bb66: c9 0d       ..
    beq cbbb6                                                         ; bb68: f0 4c       .L
    cmp #&20 ; ' '                                                    ; bb6a: c9 20       .
    beq cbbb6                                                         ; bb6c: f0 48       .H
    cmp #&30 ; '0'                                                    ; bb6e: c9 30       .0
    bcc cbbaf                                                         ; bb70: 90 3d       .=
    cmp #&3a ; ':'                                                    ; bb72: c9 3a       .:
    bcc cbb80                                                         ; bb74: 90 0a       ..
    and #&5f ; '_'                                                    ; bb76: 29 5f       )_
    adc #&b8                                                          ; bb78: 69 b8       i.
    bcs cbbaf                                                         ; bb7a: b0 33       .3
    cmp #&fa                                                          ; bb7c: c9 fa       ..
    bcc cbbaf                                                         ; bb7e: 90 2f       ./
; &bb80 referenced 1 time by &bb74
.cbb80
    and #&0f                                                          ; bb80: 29 0f       ).
    pha                                                               ; bb82: 48          H
    txa                                                               ; bb83: 8a          .
    pha                                                               ; bb84: 48          H
    ldx #4                                                            ; bb85: a2 04       ..
; &bb87 referenced 1 time by &bb9d
.loop_cbb87
    ldy #0                                                            ; bb87: a0 00       ..
    tya                                                               ; bb89: 98          .              ; A=&00
; &bb8a referenced 1 time by &bb96
.loop_cbb8a
    pha                                                               ; bb8a: 48          H
    plp                                                               ; bb8b: 28          (
    lda (l00ae),y                                                     ; bb8c: b1 ae       ..
    rol a                                                             ; bb8e: 2a          *
    sta (l00ae),y                                                     ; bb8f: 91 ae       ..
    php                                                               ; bb91: 08          .
    pla                                                               ; bb92: 68          h
    iny                                                               ; bb93: c8          .
    cpy #4                                                            ; bb94: c0 04       ..
    bne loop_cbb8a                                                    ; bb96: d0 f2       ..
    pha                                                               ; bb98: 48          H
    plp                                                               ; bb99: 28          (
    bcs cbbab                                                         ; bb9a: b0 0f       ..
    dex                                                               ; bb9c: ca          .
    bne loop_cbb87                                                    ; bb9d: d0 e8       ..
    pla                                                               ; bb9f: 68          h
    tax                                                               ; bba0: aa          .
    pla                                                               ; bba1: 68          h
    ldy #0                                                            ; bba2: a0 00       ..
    ora (l00ae),y                                                     ; bba4: 11 ae       ..
    sta (l00ae),y                                                     ; bba6: 91 ae       ..
    jmp cbb61                                                         ; bba8: 4c 61 bb    La.

; &bbab referenced 1 time by &bb9a
.cbbab
    pla                                                               ; bbab: 68          h
    pla                                                               ; bbac: 68          h
    sec                                                               ; bbad: 38          8
    rts                                                               ; bbae: 60          `

; &bbaf referenced 3 times by &bb70, &bb7a, &bb7e
.cbbaf
    jsr close_ws_file                                                 ; bbaf: 20 0c bb     ..
    jmp err_bad_hex                                                   ; bbb2: 4c f4 91    L..

; &bbb5 referenced 1 time by &bbba
.loop_cbbb5
    iny                                                               ; bbb5: c8          .
; &bbb6 referenced 2 times by &bb68, &bb6c
.cbbb6
    lda (os_text_ptr),y                                               ; bbb6: b1 f2       ..
    cmp #&20 ; ' '                                                    ; bbb8: c9 20       .
    beq loop_cbbb5                                                    ; bbba: f0 f9       ..
    clc                                                               ; bbbc: 18          .
    rts                                                               ; bbbd: 60          `

; &bbbe referenced 1 time by &ba12
.init_dump_buffer
    inx                                                               ; bbbe: e8          .
    stx l00ae                                                         ; bbbf: 86 ae       ..
    ldx #1                                                            ; bbc1: a2 01       ..
    stx l00af                                                         ; bbc3: 86 af       ..
    jsr parse_dump_range                                              ; bbc5: 20 55 bb     U.
    bcs cbbe9                                                         ; bbc8: b0 1f       ..
    tya                                                               ; bbca: 98          .
    pha                                                               ; bbcb: 48          H
    ldy ws_page                                                       ; bbcc: a4 a8       ..             ; Y=file handle
    ldx #&aa                                                          ; bbce: a2 aa       ..             ; X=zero page address for result
    lda #2                                                            ; bbd0: a9 02       ..
    jsr osargs                                                        ; bbd2: 20 da ff     ..            ; Get length of file into zero page address X (A=2)
    ldy #3                                                            ; bbd5: a0 03       ..
; &bbd7 referenced 1 time by &bbdf
.loop_cbbd7
    lda osword_flag,y                                                 ; bbd7: b9 aa 00    ...
    cmp (l00ae),y                                                     ; bbda: d1 ae       ..
    bne cbbe3                                                         ; bbdc: d0 05       ..
    dey                                                               ; bbde: 88          .
    bpl loop_cbbd7                                                    ; bbdf: 10 f6       ..
    bmi cbc03                                                         ; bbe1: 30 20       0              ; ALWAYS branch

; &bbe3 referenced 1 time by &bbdc
.cbbe3
    bcc cbbe9                                                         ; bbe3: 90 04       ..
    ldy #&ff                                                          ; bbe5: a0 ff       ..
    bne cbc03                                                         ; bbe7: d0 1a       ..             ; ALWAYS branch

; &bbe9 referenced 2 times by &bbc8, &bbe3
.cbbe9
    jsr close_ws_file                                                 ; bbe9: 20 0c bb     ..
    lda #&b7                                                          ; bbec: a9 b7       ..
    jsr error_inline                                                  ; bbee: 20 be 96     ..
    equs "Outside file", 0                                            ; bbf1: 4f 75 74... Out

; &bbfe referenced 1 time by &bc06
.loop_cbbfe
    lda (l00ae),y                                                     ; bbfe: b1 ae       ..
    sta osword_flag,y                                                 ; bc00: 99 aa 00    ...
; &bc03 referenced 2 times by &bbe1, &bbe7
.cbc03
    iny                                                               ; bc03: c8          .
    cpy #4                                                            ; bc04: c0 04       ..
    bne loop_cbbfe                                                    ; bc06: d0 f6       ..
    ldx #&aa                                                          ; bc08: a2 aa       ..             ; X=zero page address to write from
    ldy ws_page                                                       ; bc0a: a4 a8       ..             ; Y=file handle
    lda #1                                                            ; bc0c: a9 01       ..
    jsr osargs                                                        ; bc0e: 20 da ff     ..            ; Write sequential file pointer from zero page address X (A=1)
    pla                                                               ; bc11: 68          h
    tay                                                               ; bc12: a8          .
    lda (os_text_ptr),y                                               ; bc13: b1 f2       ..
    cmp #&0d                                                          ; bc15: c9 0d       ..
    bne cbc51                                                         ; bc17: d0 38       .8
    ldy #1                                                            ; bc19: a0 01       ..
; &bc1b referenced 1 time by &bc21
.loop_cbc1b
    lda os_text_ptr,y                                                 ; bc1b: b9 f2 00    ...
    sta (l00ae),y                                                     ; bc1e: 91 ae       ..
    dey                                                               ; bc20: 88          .
    bpl loop_cbc1b                                                    ; bc21: 10 f8       ..
    lda #osfile_read_catalogue_info                                   ; bc23: a9 05       ..
    ldx l00ae                                                         ; bc25: a6 ae       ..
    ldy l00af                                                         ; bc27: a4 af       ..
    jsr osfile                                                        ; bc29: 20 dd ff     ..            ; Read catalogue information (A=5)
    ldy #2                                                            ; bc2c: a0 02       ..
; &bc2e referenced 1 time by &bc39
.loop_cbc2e
    lda (l00ae),y                                                     ; bc2e: b1 ae       ..
    dey                                                               ; bc30: 88          .
    dey                                                               ; bc31: 88          .
    sta (l00ae),y                                                     ; bc32: 91 ae       ..
    iny                                                               ; bc34: c8          .
    iny                                                               ; bc35: c8          .
    iny                                                               ; bc36: c8          .
    cpy #6                                                            ; bc37: c0 06       ..
    bne loop_cbc2e                                                    ; bc39: d0 f3       ..
    dey                                                               ; bc3b: 88          .
    dey                                                               ; bc3c: 88          .
; &bc3d referenced 1 time by &bc44
.loop_cbc3d
    lda (l00ae),y                                                     ; bc3d: b1 ae       ..
    cmp #&ff                                                          ; bc3f: c9 ff       ..
    bne cbc66                                                         ; bc41: d0 23       .#
    dey                                                               ; bc43: 88          .
    bpl loop_cbc3d                                                    ; bc44: 10 f7       ..
    ldy #3                                                            ; bc46: a0 03       ..
    lda #0                                                            ; bc48: a9 00       ..
; &bc4a referenced 1 time by &bc4d
.loop_cbc4a
    sta (l00ae),y                                                     ; bc4a: 91 ae       ..
    dey                                                               ; bc4c: 88          .
    bpl loop_cbc4a                                                    ; bc4d: 10 fb       ..
    bmi cbc66                                                         ; bc4f: 30 15       0.             ; ALWAYS branch

; &bc51 referenced 1 time by &bc17
.cbc51
    jsr parse_dump_range                                              ; bc51: 20 55 bb     U.
    bcc cbc66                                                         ; bc54: 90 10       ..
    jsr close_ws_file                                                 ; bc56: 20 0c bb     ..
    lda #&fc                                                          ; bc59: a9 fc       ..
    jsr error_bad_inline                                              ; bc5b: 20 a2 96     ..
    equs "address", 0                                                 ; bc5e: 61 64 64... add

; &bc66 referenced 3 times by &bc41, &bc4f, &bc54
.cbc66
    ldy #0                                                            ; bc66: a0 00       ..
    ldx #4                                                            ; bc68: a2 04       ..
    clc                                                               ; bc6a: 18          .
; &bc6b referenced 1 time by &bc75
.loop_cbc6b
    lda (l00ae),y                                                     ; bc6b: b1 ae       ..
    adc osword_flag,y                                                 ; bc6d: 79 aa 00    y..
    sta osword_flag,y                                                 ; bc70: 99 aa 00    ...
    iny                                                               ; bc73: c8          .
    dex                                                               ; bc74: ca          .
    bne loop_cbc6b                                                    ; bc75: d0 f4       ..
    ldy #&14                                                          ; bc77: a0 14       ..
    ldx #3                                                            ; bc79: a2 03       ..
; &bc7b referenced 1 time by &bc81
.loop_cbc7b
    dey                                                               ; bc7b: 88          .
    lda osword_flag,x                                                 ; bc7c: b5 aa       ..
    sta (l00ae),y                                                     ; bc7e: 91 ae       ..
    dex                                                               ; bc80: ca          .
    bpl loop_cbc7b                                                    ; bc81: 10 f8       ..
    rts                                                               ; bc83: 60          `

; &bc84 referenced 3 times by &9bde, &a8bb, &baa2
.advance_x_by_8
    jsr advance_x_by_4                                                ; bc84: 20 87 bc     ..
; &bc87 referenced 1 time by &bc84
.advance_x_by_4
    jsr inx4                                                          ; bc87: 20 8a bc     ..
; &bc8a referenced 1 time by &bc87
.inx4
    inx                                                               ; bc8a: e8          .
    inx                                                               ; bc8b: e8          .
    inx                                                               ; bc8c: e8          .
    inx                                                               ; bc8d: e8          .
    rts                                                               ; bc8e: 60          `

    equb &ff                                                          ; bc8f: ff          .
; &bc90 referenced 1 time by &bea0

    org &be90

    sta brkv+1                                                        ; be90: 8d 03 02    ...
    lda #&8e                                                          ; be93: a9 8e       ..
    sta tube_status_1_and_tube_control                                ; be95: 8d e0 fe    ...
    ldy #0                                                            ; be98: a0 00       ..
; &be9a referenced 1 time by &bead
.loop_cbe9a
    lda reloc_p4_src,y                                                ; be9a: b9 00 bf    ...
    sta tube_page4_vectors,y                                          ; be9d: 99 00 04    ...
    lda reloc_p5_src,y                                                ; bea0: b9 90 bc    ...
    sta tube_r2_dispatch_table,y                                      ; bea3: 99 00 05    ...
    lda reloc_p6_src,y                                                ; bea6: b9 90 bd    ...
    sta tube_osbyte_reply_block,y                                     ; bea9: 99 00 06    ...
    dey                                                               ; beac: 88          .
    bne loop_cbe9a                                                    ; bead: d0 eb       ..
    jsr clear_tube_claim                                              ; beaf: 20 21 04     !.
    ldx #&41 ; 'A'                                                    ; beb2: a2 41       .A
; &beb4 referenced 1 time by &beba
.loop_cbeb4
    lda reloc_zp_src,x                                                ; beb4: bd bf be    ...
    sta nmi_workspace_start,x                                         ; beb7: 95 16       ..
    dex                                                               ; beb9: ca          .
    bpl loop_cbeb4                                                    ; beba: 10 f8       ..
    lda #0                                                            ; bebc: a9 00       ..
    rts                                                               ; bebe: 60          `

; &bebf referenced 1 time by &beb4

    assert (255 - inkey_key_ctrl) EOR 128 == &81
    assert <(fs_work_4) == &b4
    assert <(l0128) == &28
    assert >(fs_work_4) == &00
    assert >(l0128) == &01
    assert copyright - rom_header == &14

save pydis_start, pydis_end

; Label references by decreasing frequency:
;     nfs_workspace:                           76
;     l0f05:                                   69
;     net_rx_ptr:                              65
;     fs_options:                              57
;     econet_control23_or_status2:             46
;     fs_load_addr_2:                          38
;     l00ae:                                   38
;     econet_data_continue_frame:              37
;     net_tx_ptr:                              37
;     print_inline:                            35
;     port_ws_offset:                          34
;     fs_crc_lo:                               33
;     econet_control1_or_status1:              32
;     l0f06:                                   30
;     l1071:                                   30
;     osbyte:                                  27
;     rx_src_net:                              27
;     save_net_tx_cb:                          26
;     l10b8:                                   25
;     fs_work_4:                               24
;     osasci:                                  23
;     bit_test_ff_pad:                         22
;     fs_load_addr:                            22
;     port_buf_len:                            22
;     fs_error_ptr:                            21
;     error_text:                              20
;     ws_page:                                 20
;     l00ad:                                   18
;     l1000:                                   18
;     l1060:                                   18
;     fs_block_offset:                         17
;     l0e30:                                   17
;     open_port_buf_hi:                        17
;     osword_pb_ptr:                           17
;     ws_ptr_hi:                               17
;     fs_work_5:                               16
;     os_text_ptr:                             16
;     osnewl:                                  16
;     error_block:                             15
;     l0d6c:                                   15
;     station_id_disable_net_nmis:             15
;     tube_read_r2:                            15
;     l0f07:                                   14
;     l1010:                                   14
;     l10c8:                                   14
;     net_tx_ptr_hi:                           14
;     nmi_tx_block:                            14
;     osword_flag:                             14
;     set_nmi_vector:                          14
;     escapable:                               13
;     l1030:                                   13
;     mask_owner_access:                       13
;     open_port_buf:                           13
;     port_buf_len_hi:                         13
;     tube_send_r2:                            13
;     cmd_table_fs:                            12
;     fs_last_byte_flag:                       12
;     l0d61:                                   12
;     l10c9:                                   12
;     nmi_error_dispatch:                      12
;     return_with_last_flag:                   12
;     svc_state:                               12
;     error_bad_inline:                        11
;     fs_load_addr_3:                          11
;     l00b6:                                   11
;     tube_data_register_2:                    11
;     tx_result_fail:                          11
;     copy_arg_to_buf:                         10
;     error_inline_log:                        10
;     tube_addr_data_dispatch:                 10
;     tube_data_register_3:                    10
;     tube_status_register_2:                  10
;     ws_0d6a:                                 10
;     zp_ptr_lo:                               10
;     l0d2e:                                    9
;     l0f03:                                    9
;     l0f08:                                    9
;     l1020:                                    9
;     net_rx_ptr_hi:                            9
;     txcb_end:                                 9
;     ws_ptr_lo:                                9
;     error_msg_table:                          8
;     install_nmi_handler:                      8
;     l00af:                                    8
;     nfs_workspace_hi:                         8
;     process_all_fcbs:                         8
;     romsel_copy:                              8
;     save_ptr_to_os_text:                      8
;     tube_send_r4:                             8
;     tube_status_1_and_tube_control:           8
;     ws_0d60:                                  8
;     ws_0d68:                                  8
;     zp_ptr_hi:                                8
;     alloc_fcb_slot:                           7
;     fs_load_addr_hi:                          7
;     l0df0:                                    7
;     l0e01:                                    7
;     l0f02:                                    7
;     l0f09:                                    7
;     l1040:                                    7
;     l1098:                                    7
;     reject_reply:                             7
;     send_net_packet:                          7
;     tube_claimed_id:                          7
;     tx_dst_stn:                               7
;     txcb_ctrl:                                7
;     txcb_start:                               7
;     bin_to_bcd:                               6
;     c91fd:                                    6
;     close_ws_file:                            6
;     cond_save_error_code:                     6
;     copy_arg_to_buf_x0:                       6
;     discard_reset_rx:                         6
;     finalise_and_return:                      6
;     l00cc:                                    6
;     l00d0:                                    6
;     l0e00:                                    6
;     l0e05:                                    6
;     l10d8:                                    6
;     match_station_net:                        6
;     nmi_rti:                                  6
;     os_text_ptr_hi:                           6
;     osfind:                                   6
;     rx_buf_offset:                            6
;     tube_main_loop:                           6
;     wait_net_tx_ack:                          6
;     attr_to_chan_index:                       5
;     data_tx_last:                             5
;     escape_flag:                              5
;     fs_crc_hi:                                5
;     fs_crflag:                                5
;     fs_spool_handle:                          5
;     init_txcb:                                5
;     l0102:                                    5
;     l0d30:                                    5
;     l0d31:                                    5
;     l0d63:                                    5
;     l0d6b:                                    5
;     l0e03:                                    5
;     l0e07:                                    5
;     l10cf:                                    5
;     l10d4:                                    5
;     l10d5:                                    5
;     match_fs_cmd:                             5
;     need_release_tube:                        5
;     net_error_lookup_data:                    5
;     oswrch:                                   5
;     parse_addr_arg:                           5
;     print_hex_byte:                           5
;     scout_error:                              5
;     set_xfer_params:                          5
;     strip_token_prefix:                       5
;     svc_dispatch:                             5
;     system_via_acr:                           5
;     tube_send_r1:                             5
;     tx_dst_net:                               5
;     verify_ws_checksum:                       5
;     zp_work_3:                                5
;     c8dc7:                                    4
;     cab24:                                    4
;     cb212:                                    4
;     cb553:                                    4
;     cb58f:                                    4
;     check_net_error_code:                     4
;     commit_state_byte:                        4
;     err_bad_station_num:                      4
;     error_bad_filename:                       4
;     error_inline:                             4
;     fs_work_7:                                4
;     get_ws_page:                              4
;     gsinit:                                   4
;     gsread:                                   4
;     l0d2f:                                    4
;     l0d43:                                    4
;     l0d44:                                    4
;     l0d72:                                    4
;     l0e02:                                    4
;     l0e04:                                    4
;     l0e09:                                    4
;     l0e0a:                                    4
;     l10a8:                                    4
;     l10f3:                                    4
;     load_ps_server_addr:                      4
;     nmi_tx_block_hi:                          4
;     osword:                                   4
;     osword_pb_ptr_hi:                         4
;     parse_access_prefix:                      4
;     parse_filename_arg:                       4
;     print_station_addr:                       4
;     return_23:                                4
;     rx_ctrl:                                  4
;     rx_port:                                  4
;     tube_reply_byte:                          4
;     txcb_port:                                4
;     video_ula_control:                        4
;     ws_0d62:                                  4
;     zp_work_2:                                4
;     adlc_full_reset:                          3
;     advance_buffer_ptr:                       3
;     advance_x_by_8:                           3
;     append_byte_to_rxbuf:                     3
;     brk_ptr:                                  3
;     c8a90:                                    3
;     c92cd:                                    3
;     c95de:                                    3
;     c98b4:                                    3
;     c9d71:                                    3
;     c9daf:                                    3
;     ca6fb:                                    3
;     ca9e9:                                    3
;     caa24:                                    3
;     cb038:                                    3
;     cb12f:                                    3
;     cb2b8:                                    3
;     cb995:                                    3
;     cbbaf:                                    3
;     cbc66:                                    3
;     check_tube_irq_loop:                      3
;     close_all_net_chans:                      3
;     cmd_table_fs_hi:                          3
;     cmd_table_fs_lo:                          3
;     copy_arg_validated:                       3
;     data_rx_complete:                         3
;     err_bad_hex:                              3
;     error_bad_command:                        3
;     find_matching_fcb:                        3
;     find_station_bit3:                        3
;     is_decimal_digit:                         3
;     jmp_restore_fs_ctx:                       3
;     l0106:                                    3
;     l0355:                                    3
;     l0d6d:                                    3
;     l0e31:                                    3
;     l0f00:                                    3
;     l1070:                                    3
;     l1078:                                    3
;     l1088:                                    3
;     l10ca:                                    3
;     l10cc:                                    3
;     l10d0:                                    3
;     next_port_slot:                           3
;     nmi_jmp_hi:                               3
;     nmi_jmp_lo:                               3
;     osargs:                                   3
;     osbyte_a_copy:                            3
;     osbyte_x0:                                3
;     parse_fs_ps_args:                         3
;     port_match_found:                         3
;     print_10_chars:                           3
;     print_decimal_3dig:                       3
;     read_filename_char:                       3
;     read_last_rx_byte:                        3
;     read_paged_rom:                           3
;     reload_inactive_mask:                     3
;     reset_adlc_rx_listen:                     3
;     restore_fs_context:                       3
;     return_27:                                3
;     return_3:                                 3
;     return_9:                                 3
;     rx_complete_update_rxcb:                  3
;     rx_remote_addr:                           3
;     save_net_tx_cb_vset:                      3
;     save_text_ptr:                            3
;     send_disconnect_reply:                    3
;     svc_return_unclaimed:                     3
;     tube_claim_c3:                            3
;     tube_data_register_1:                     3
;     tube_xfer_page:                           3
;     tx_active_start:                          3
;     tx_begin:                                 3
;     tx_calc_transfer:                         3
;     write_second_tube_byte:                   3
;     ws_0d65:                                  3
;     ws_0d69:                                  3
;     abort_if_escape:                          2
;     ack_tx:                                   2
;     ack_tx_write_dest:                        2
;     adjust_fsopts_4bytes:                     2
;     adlc_rx_listen:                           2
;     advance_rx_buffer_ptr:                    2
;     advance_y_by_4:                           2
;     alloc_fcb_or_error:                       2
;     append_decimal_digit:                     2
;     append_decimal_num:                       2
;     append_drv_dot_num:                       2
;     append_space_and_num:                     2
;     byte_to_2bit_index:                       2
;     c8a2e:                                    2
;     c8a50:                                    2
;     c8ab2:                                    2
;     c8bd5:                                    2
;     c8f23:                                    2
;     c919a:                                    2
;     c91c6:                                    2
;     c91e7:                                    2
;     c9215:                                    2
;     c9221:                                    2
;     c934f:                                    2
;     c93a8:                                    2
;     c94c5:                                    2
;     c953b:                                    2
;     c9573:                                    2
;     c972b:                                    2
;     c9856:                                    2
;     c9869:                                    2
;     c98d6:                                    2
;     c9912:                                    2
;     c99b4:                                    2
;     c9a52:                                    2
;     c9a84:                                    2
;     c9b23:                                    2
;     c9b99:                                    2
;     c9cd3:                                    2
;     c9ce1:                                    2
;     c9d7b:                                    2
;     c9dfd:                                    2
;     c9f78:                                    2
;     ca0df:                                    2
;     ca11b:                                    2
;     ca141:                                    2
;     ca18a:                                    2
;     ca19f:                                    2
;     ca2d7:                                    2
;     ca2eb:                                    2
;     ca316:                                    2
;     ca34d:                                    2
;     ca3cb:                                    2
;     ca88c:                                    2
;     caa78:                                    2
;     caa97:                                    2
;     caaea:                                    2
;     cac1e:                                    2
;     cac38:                                    2
;     cae72:                                    2
;     caec6:                                    2
;     caf3a:                                    2
;     cafad:                                    2
;     cb06d:                                    2
;     cb120:                                    2
;     cb2e9:                                    2
;     cb56b:                                    2
;     cb5ab:                                    2
;     cb678:                                    2
;     cb720:                                    2
;     cb73a:                                    2
;     cb73d:                                    2
;     cb82a:                                    2
;     cb8f1:                                    2
;     cb9b8:                                    2
;     cb9d2:                                    2
;     cba1e:                                    2
;     cba3e:                                    2
;     cbbb6:                                    2
;     cbbe9:                                    2
;     cbc03:                                    2
;     check_and_setup_txcb:                     2
;     check_chan_char:                          2
;     check_escape:                             2
;     check_not_ampersand:                      2
;     check_not_dir:                            2
;     claim_addr_ff:                            2
;     classify_reply_error:                     2
;     clear_conn_active:                        2
;     cmd_pass:                                 2
;     cmp_5byte_handle:                         2
;     copy_fs_cmd_name:                         2
;     copy_fsopts_to_zp:                        2
;     copy_scout_via_tube:                      2
;     copy_workspace_to_fsopts:                 2
;     credits_keyword_start:                    2
;     data_rx_tube_complete:                    2
;     data_tx_check_fifo:                       2
;     discard_no_match:                         2
;     discard_reset_listen:                     2
;     dispatch_nmi_error:                       2
;     err_net_chan_invalid:                     2
;     error_net_checksum:                       2
;     fallback_calc_transfer:                   2
;     find_open_fcb:                            2
;     flip_set_station_boot:                    2
;     flush_and_read_char:                      2
;     format_filename_field:                    2
;     get_access_bits:                          2
;     get_pb_ptr_as_index:                      2
;     get_prot_bits:                            2
;     handle_spool_ctrl_byte:                   2
;     help_wrap_if_serial:                      2
;     imm_op_out_of_range:                      2
;     inc_fcb_byte_count:                       2
;     init_bridge_poll:                         2
;     init_spool_drive:                         2
;     init_tx_ptr_and_send:                     2
;     init_wipe_counters:                       2
;     init_ws_copy_wide:                        2
;     l0103:                                    2
;     l0128:                                    2
;     l028d:                                    2
;     l072e:                                    2
;     l0d42:                                    2
;     l0d6e:                                    2
;     l0dfa:                                    2
;     l0e06:                                    2
;     l0e2f:                                    2
;     l0e38:                                    2
;     l0f01:                                    2
;     l0f04:                                    2
;     l0f0a:                                    2
;     l0f0b:                                    2
;     l0f10:                                    2
;     l0f11:                                    2
;     l0f12:                                    2
;     l0fdc:                                    2
;     l0fdd:                                    2
;     l0fde:                                    2
;     l10d7:                                    2
;     l10d9:                                    2
;     lookup_cat_entry_0:                       2
;     lookup_chan_by_char:                      2
;     net_channel_err_string:                   2
;     open_file_for_read:                       2
;     osbget:                                   2
;     osfile:                                   2
;     osrdch:                                   2
;     osrdsc_ptr:                               2
;     parse_cmd_arg_y0:                         2
;     parse_dump_range:                         2
;     parse_quoted_arg:                         2
;     pass_txbuf_init_table:                    2
;     poll_nmi_idle:                            2
;     pop_requeue_ps_scan:                      2
;     print_5_hex_bytes:                        2
;     print_cmd_table:                          2
;     print_cmd_table_loop:                     2
;     print_decimal_digit:                      2
;     print_dump_header:                        2
;     print_printer_server_is:                  2
;     print_station_id:                         2
;     print_version_header:                     2
;     prot_check_arg_end:                       2
;     recv_and_process_reply:                   2
;     release_tube:                             2
;     reset_spool_buf_state:                    2
;     retreat_y_by_3:                           2
;     return_10:                                2
;     return_12:                                2
;     return_15:                                2
;     return_21:                                2
;     return_24:                                2
;     return_26:                                2
;     return_35:                                2
;     return_4:                                 2
;     return_5:                                 2
;     return_7:                                 2
;     return_tube_init:                         2
;     reverse_ps_name_to_tx:                    2
;     romsel:                                   2
;     save_fcb_context:                         2
;     save_ptr_to_spool_buf:                    2
;     scout_complete:                           2
;     scout_copy_done:                          2
;     send_ack:                                 2
;     send_and_receive:                         2
;     send_cmd_and_dispatch:                    2
;     send_fs_request:                          2
;     send_request_write:                       2
;     send_txcb_swap_addrs:                     2
;     send_wipe_request:                        2
;     set_conn_active:                          2
;     set_nmi_rx_scout:                         2
;     set_options_ptr:                          2
;     setup_transfer_workspace:                 2
;     setup_ws_ptr:                             2
;     skip_addr_carry:                          2
;     skip_nmi_release:                         2
;     skip_to_next_arg:                         2
;     start_wipe_pass:                          2
;     store_char_uppercase:                     2
;     store_prot_mask:                          2
;     store_result_check_dir:                   2
;     store_stn_flags_restore:                  2
;     store_tx_error:                           2
;     string_buf:                               2
;     svc_dispatch_lo_offset:                   2
;     system_via_ier:                           2
;     system_via_ifr:                           2
;     system_via_sr:                            2
;     tail_update_catalogue:                    2
;     try_nfs_port_list:                        2
;     tube_claim_flag:                          2
;     tube_data_ptr:                            2
;     tube_init_reloc:                          2
;     tube_osword_read_lp:                      2
;     tube_poll_r2_result:                      2
;     tube_r2_dispatch_table:                   2
;     tube_read_string:                         2
;     tube_reply_ack:                           2
;     tube_status_register_4_and_cpu_control:   2
;     tube_transfer_addr:                       2
;     tube_tx_fifo_write:                       2
;     tube_xfer_addr_2:                         2
;     tube_xfer_addr_3:                         2
;     tx_ctrl_byte:                             2
;     tx_econet_abort:                          2
;     tx_port:                                  2
;     tx_result_ok:                             2
;     tx_src_stn:                               2
;     tx_store_result:                          2
;     write_data_block:                         2
;     write_ps_slot_byte_ff:                    2
;     write_vector_entry:                       2
;     ws_0d64:                                  2
;     accept_frame:                             1
;     accept_local_net:                         1
;     accept_new_claim:                         1
;     accept_scout_net:                         1
;     ack_tx_configure:                         1
;     add_rxcb_ptr:                             1
;     add_workspace_to_fsopts:                  1
;     addr_claim_external:                      1
;     adlc_init:                                1
;     advance_x_by_4:                           1
;     argsw:                                    1
;     bad_prefix:                               1
;     boot_cmd_oscli:                           1
;     boot_load_cmd:                            1
;     boot_oscli_lo_table:                      1
;     bridge_txcb_init_table:                   1
;     bridge_ws_init_data:                      1
;     brkv:                                     1
;     bytex:                                    1
;     c06ef:                                    1
;     c802d:                                    1
;     c8052:                                    1
;     c87e8:                                    1
;     c88f7:                                    1
;     c8a29:                                    1
;     c8a32:                                    1
;     c8a49:                                    1
;     c8a58:                                    1
;     c8a65:                                    1
;     c8a68:                                    1
;     c8ac3:                                    1
;     c8af3:                                    1
;     c8b28:                                    1
;     c8b9d:                                    1
;     c8ba3:                                    1
;     c8bab:                                    1
;     c8be5:                                    1
;     c8beb:                                    1
;     c8bf5:                                    1
;     c8c07:                                    1
;     c8c14:                                    1
;     c8c19:                                    1
;     c8c1b:                                    1
;     c8c24:                                    1
;     c8c68:                                    1
;     c8c72:                                    1
;     c8c8d:                                    1
;     c8ccf:                                    1
;     c8cd5:                                    1
;     c8cff:                                    1
;     c8d1b:                                    1
;     c8d9c:                                    1
;     c8de0:                                    1
;     c8def:                                    1
;     c8e9d:                                    1
;     c8f2f:                                    1
;     c8fa4:                                    1
;     c900a:                                    1
;     c912c:                                    1
;     c913f:                                    1
;     c9157:                                    1
;     c9169:                                    1
;     c9174:                                    1
;     c9184:                                    1
;     c9186:                                    1
;     c91cf:                                    1
;     c91e5:                                    1
;     c9230:                                    1
;     c9253:                                    1
;     c9263:                                    1
;     c926f:                                    1
;     c932a:                                    1
;     c9344:                                    1
;     c935d:                                    1
;     c938e:                                    1
;     c939a:                                    1
;     c93da:                                    1
;     c93f1:                                    1
;     c93f8:                                    1
;     c9428:                                    1
;     c944e:                                    1
;     c9472:                                    1
;     c94bf:                                    1
;     c94ee:                                    1
;     c94f1:                                    1
;     c94fa:                                    1
;     c9506:                                    1
;     c952f:                                    1
;     c9545:                                    1
;     c9570:                                    1
;     c95d8:                                    1
;     c95f1:                                    1
;     c9604:                                    1
;     c9620:                                    1
;     c9633:                                    1
;     c963b:                                    1
;     c965e:                                    1
;     c9670:                                    1
;     c9672:                                    1
;     c9682:                                    1
;     c9684:                                    1
;     c9699:                                    1
;     c96e5:                                    1
;     c96e8:                                    1
;     c970a:                                    1
;     c970d:                                    1
;     c9717:                                    1
;     c9752:                                    1
;     c978f:                                    1
;     c9831:                                    1
;     c983a:                                    1
;     c985e:                                    1
;     c986d:                                    1
;     c9896:                                    1
;     c98a3:                                    1
;     c98c9:                                    1
;     c98de:                                    1
;     c98ed:                                    1
;     c9938:                                    1
;     c9955:                                    1
;     c995b:                                    1
;     c99af:                                    1
;     c99f8:                                    1
;     c9a05:                                    1
;     c9a0b:                                    1
;     c9a0e:                                    1
;     c9a1e:                                    1
;     c9a8e:                                    1
;     c9ab7:                                    1
;     c9ac0:                                    1
;     c9add:                                    1
;     c9ae9:                                    1
;     c9b0e:                                    1
;     c9b2a:                                    1
;     c9b2f:                                    1
;     c9b35:                                    1
;     c9b3a:                                    1
;     c9b44:                                    1
;     c9b7f:                                    1
;     c9b80:                                    1
;     c9ba6:                                    1
;     c9bc1:                                    1
;     c9bc9:                                    1
;     c9be9:                                    1
;     c9bf4:                                    1
;     c9c3d:                                    1
;     c9c40:                                    1
;     c9c5c:                                    1
;     c9c7e:                                    1
;     c9cb6:                                    1
;     c9cc8:                                    1
;     c9cdf:                                    1
;     c9ce3:                                    1
;     c9ce6:                                    1
;     c9d5f:                                    1
;     c9d75:                                    1
;     c9d7e:                                    1
;     c9d97:                                    1
;     c9d9d:                                    1
;     c9db2:                                    1
;     c9dc6:                                    1
;     c9dc9:                                    1
;     c9dce:                                    1
;     c9dd3:                                    1
;     c9dff:                                    1
;     c9e19:                                    1
;     c9e1c:                                    1
;     c9e36:                                    1
;     c9e39:                                    1
;     c9e44:                                    1
;     c9e83:                                    1
;     c9e86:                                    1
;     c9ee1:                                    1
;     c9eea:                                    1
;     c9ef8:                                    1
;     c9f40:                                    1
;     c9f43:                                    1
;     c9f55:                                    1
;     c9f6a:                                    1
;     c9f8c:                                    1
;     c9fcd:                                    1
;     c9fda:                                    1
;     c9ff7:                                    1
;     ca033:                                    1
;     ca058:                                    1
;     ca083:                                    1
;     ca0a5:                                    1
;     ca0ad:                                    1
;     ca0b1:                                    1
;     ca0dd:                                    1
;     ca0f1:                                    1
;     ca12a:                                    1
;     ca152:                                    1
;     ca164:                                    1
;     ca16d:                                    1
;     ca175:                                    1
;     ca179:                                    1
;     ca18b:                                    1
;     ca191:                                    1
;     ca1a6:                                    1
;     ca1b2:                                    1
;     ca1d2:                                    1
;     ca1ee:                                    1
;     ca1f1:                                    1
;     ca22b:                                    1
;     ca242:                                    1
;     ca252:                                    1
;     ca265:                                    1
;     ca281:                                    1
;     ca301:                                    1
;     ca30f:                                    1
;     ca32c:                                    1
;     ca33a:                                    1
;     ca363:                                    1
;     ca371:                                    1
;     ca39c:                                    1
;     ca50f:                                    1
;     ca526:                                    1
;     ca589:                                    1
;     ca594:                                    1
;     ca701:                                    1
;     ca8c0:                                    1
;     ca8e6:                                    1
;     ca926:                                    1
;     ca959:                                    1
;     ca97a:                                    1
;     ca9f2:                                    1
;     caa1c:                                    1
;     caa8d:                                    1
;     caa8f:                                    1
;     caa95:                                    1
;     caa9b:                                    1
;     caa9f:                                    1
;     cab21:                                    1
;     cab63:                                    1
;     cab72:                                    1
;     caba3:                                    1
;     caba5:                                    1
;     cabcc:                                    1
;     cabe1:                                    1
;     cabfe:                                    1
;     cac2d:                                    1
;     cac55:                                    1
;     cad0e:                                    1
;     cad1d:                                    1
;     cad84:                                    1
;     cada0:                                    1
;     cadd1:                                    1
;     caddb:                                    1
;     cae15:                                    1
;     cae3d:                                    1
;     cae7d:                                    1
;     caec9:                                    1
;     caecd:                                    1
;     caed0:                                    1
;     caedf:                                    1
;     caee9:                                    1
;     caf05:                                    1
;     caf07:                                    1
;     caf20:                                    1
;     caf3c:                                    1
;     caf3f:                                    1
;     caf52:                                    1
;     caf8d:                                    1
;     cafd8:                                    1
;     calc_peek_poke_size:                      1
;     calc_transfer_size:                       1
;     call_fscv:                                1
;     cat_set_lib_flag:                         1
;     cb005:                                    1
;     cb008:                                    1
;     cb04b:                                    1
;     cb075:                                    1
;     cb08a:                                    1
;     cb092:                                    1
;     cb095:                                    1
;     cb0b6:                                    1
;     cb0f4:                                    1
;     cb0f8:                                    1
;     cb184:                                    1
;     cb18d:                                    1
;     cb1e1:                                    1
;     cb1e4:                                    1
;     cb23d:                                    1
;     cb243:                                    1
;     cb278:                                    1
;     cb288:                                    1
;     cb2bb:                                    1
;     cb2d1:                                    1
;     cb2d3:                                    1
;     cb2fa:                                    1
;     cb319:                                    1
;     cb34d:                                    1
;     cb380:                                    1
;     cb387:                                    1
;     cb38c:                                    1
;     cb395:                                    1
;     cb3db:                                    1
;     cb3f6:                                    1
;     cb3fa:                                    1
;     cb3fc:                                    1
;     cb40b:                                    1
;     cb411:                                    1
;     cb465:                                    1
;     cb467:                                    1
;     cb473:                                    1
;     cb4b1:                                    1
;     cb50b:                                    1
;     cb548:                                    1
;     cb54e:                                    1
;     cb557:                                    1
;     cb596:                                    1
;     cb5a0:                                    1
;     cb5aa:                                    1
;     cb5b2:                                    1
;     cb5c1:                                    1
;     cb62f:                                    1
;     cb657:                                    1
;     cb675:                                    1
;     cb6cc:                                    1
;     cb6f2:                                    1
;     cb716:                                    1
;     cb757:                                    1
;     cb78e:                                    1
;     cb7b9:                                    1
;     cb7bf:                                    1
;     cb7ee:                                    1
;     cb819:                                    1
;     cb87d:                                    1
;     cb88b:                                    1
;     cb8dd:                                    1
;     cb910:                                    1
;     cb960:                                    1
;     cb969:                                    1
;     cb9a1:                                    1
;     cb9b0:                                    1
;     cb9c5:                                    1
;     cb9d8:                                    1
;     cb9df:                                    1
;     cb9e4:                                    1
;     cb9ef:                                    1
;     cba37:                                    1
;     cba45:                                    1
;     cba50:                                    1
;     cba9b:                                    1
;     cbab1:                                    1
;     cbac0:                                    1
;     cbac9:                                    1
;     cbb39:                                    1
;     cbb53:                                    1
;     cbb61:                                    1
;     cbb80:                                    1
;     cbbab:                                    1
;     cbbe3:                                    1
;     cbc51:                                    1
;     cbe6f:                                    1
;     cdir_alloc_size_table:                    1
;     check_break_type:                         1
;     check_credits_easter_egg:                 1
;     check_fv_final_ack:                       1
;     check_handshake_bit:                      1
;     check_irq_loop:                           1
;     check_port_slot:                          1
;     check_scout_done:                         1
;     check_sr2_loop_again:                     1
;     check_station_filter:                     1
;     clear_escapable:                          1
;     clear_if_station_match:                   1
;     clear_release_flag:                       1
;     clear_tube_claim:                         1
;     cmd_fs_entry:                             1
;     cmd_fs_reentry:                           1
;     cmd_net_fs:                               1
;     cmd_syntax_strings:                       1
;     cmd_syntax_table:                         1
;     cmd_table_nfs_iam:                        1
;     copro_ack_nmi_check:                      1
;     copy_bcast_addr:                          1
;     copy_imm_params:                          1
;     copy_nmi_shim:                            1
;     copy_ps_data:                             1
;     copy_ps_data_y1c:                         1
;     copy_scout_bytes:                         1
;     copy_scout_to_buffer:                     1
;     copyright_offset:                         1
;     credits_string_mid:                       1
;     data_rx_loop:                             1
;     data_tx_begin:                            1
;     delay_nmi_disable:                        1
;     deselect_fs_if_active:                    1
;     discard_after_reset:                      1
;     dispatch_imm_op:                          1
;     dispatch_svc5:                            1
;     dispatch_svc_with_state:                  1
;     do_fs_cmd_iteration:                      1
;     econet_data_terminate_frame:              1
;     enable_irq_and_poll:                      1
;     err_printer_busy:                         1
;     error_syntax:                             1
;     evntv:                                    1
;     ex_print_col_sep:                         1
;     ex_set_lib_flag:                          1
;     filev:                                    1
;     find_fs_and_exit:                         1
;     find_station_bit2:                        1
;     fixup_reply_status_a:                     1
;     fs_vector_table:                          1
;     fscv:                                     1
;     gsread_to_buf:                            1
;     handshake_await_ack:                      1
;     help_print_nfs_cmds:                      1
;     imm_op_build_reply:                       1
;     imm_op_discard:                           1
;     inactive_retry:                           1
;     inc_rxcb_ptr:                             1
;     init_adlc_and_vectors:                    1
;     init_channel_table:                       1
;     init_dump_buffer:                         1
;     init_ps_slot_from_rx:                     1
;     init_tx_ptr_for_pass:                     1
;     init_txcb_bye:                            1
;     init_txcb_port:                           1
;     init_ws_copy_narrow:                      1
;     install_data_rx_handler:                  1
;     install_imm_data_nmi:                     1
;     install_reply_scout:                      1
;     install_saved_handler:                    1
;     install_tube_rx:                          1
;     intoff_disable_nmi_op:                    1
;     inx4:                                     1
;     is_dec_digit_only:                        1
;     issue_svc_15:                             1
;     l0006:                                    1
;     l0063:                                    1
;     l0078:                                    1
;     l0085:                                    1
;     l00da:                                    1
;     l0104:                                    1
;     l026a:                                    1
;     l02a0:                                    1
;     l0351:                                    1
;     l072c:                                    1
;     l0a0e:                                    1
;     l0d07:                                    1
;     l0d1a:                                    1
;     l0d6f:                                    1
;     l0d70:                                    1
;     l0de6:                                    1
;     l0dfe:                                    1
;     l0e0b:                                    1
;     l0e16:                                    1
;     l0e32:                                    1
;     l0ef7:                                    1
;     l0f0c:                                    1
;     l0f0d:                                    1
;     l0f0e:                                    1
;     l0f13:                                    1
;     l0f14:                                    1
;     l0f16:                                    1
;     l0f2f:                                    1
;     l0f30:                                    1
;     l0fdf:                                    1
;     l0fe0:                                    1
;     l0ff0:                                    1
;     l1050:                                    1
;     l1072:                                    1
;     l1073:                                    1
;     l1074:                                    1
;     l10cb:                                    1
;     l10cd:                                    1
;     l10ce:                                    1
;     l10d1:                                    1
;     l10d6:                                    1
;     l2322:                                    1
;     l6f6e:                                    1
;     l7dfd:                                    1
;     language_entry:                           1
;     library_dir_prefix:                       1
;     listen_jmp_hi:                            1
;     load_reply_and_classify:                  1
;     load_text_ptr_and_parse:                  1
;     lookup_cat_slot_data:                     1
;     loop_c06df:                               1
;     loop_c83da:                               1
;     loop_c8ae6:                               1
;     loop_c8b1a:                               1
;     loop_c8b2d:                               1
;     loop_c8b40:                               1
;     loop_c8b6f:                               1
;     loop_c8bb5:                               1
;     loop_c8bbf:                               1
;     loop_c8bfb:                               1
;     loop_c8c3a:                               1
;     loop_c8c75:                               1
;     loop_c8d10:                               1
;     loop_c8d21:                               1
;     loop_c8da3:                               1
;     loop_c8db6:                               1
;     loop_c8dd9:                               1
;     loop_c8e71:                               1
;     loop_c8ed5:                               1
;     loop_c8eff:                               1
;     loop_c8f11:                               1
;     loop_c8f29:                               1
;     loop_c8f75:                               1
;     loop_c8f97:                               1
;     loop_c8fa1:                               1
;     loop_c8fbb:                               1
;     loop_c9139:                               1
;     loop_c9267:                               1
;     loop_c9292:                               1
;     loop_c9315:                               1
;     loop_c931e:                               1
;     loop_c933b:                               1
;     loop_c9387:                               1
;     loop_c93dc:                               1
;     loop_c9462:                               1
;     loop_c94a7:                               1
;     loop_c94e4:                               1
;     loop_c950b:                               1
;     loop_c9547:                               1
;     loop_c9614:                               1
;     loop_c9652:                               1
;     loop_c9676:                               1
;     loop_c9693:                               1
;     loop_c96ae:                               1
;     loop_c96d1:                               1
;     loop_c971f:                               1
;     loop_c977f:                               1
;     loop_c9850:                               1
;     loop_c9889:                               1
;     loop_c98af:                               1
;     loop_c98c4:                               1
;     loop_c98e3:                               1
;     loop_c98f5:                               1
;     loop_c9907:                               1
;     loop_c995d:                               1
;     loop_c9978:                               1
;     loop_c998d:                               1
;     loop_c998f:                               1
;     loop_c99a3:                               1
;     loop_c99b9:                               1
;     loop_c99d7:                               1
;     loop_c9a1b:                               1
;     loop_c9a2c:                               1
;     loop_c9a62:                               1
;     loop_c9a75:                               1
;     loop_c9a99:                               1
;     loop_c9aab:                               1
;     loop_c9ab9:                               1
;     loop_c9b01:                               1
;     loop_c9b18:                               1
;     loop_c9b66:                               1
;     loop_c9b73:                               1
;     loop_c9b8d:                               1
;     loop_c9ba4:                               1
;     loop_c9bc6:                               1
;     loop_c9bd9:                               1
;     loop_c9c27:                               1
;     loop_c9c4f:                               1
;     loop_c9c85:                               1
;     loop_c9d1e:                               1
;     loop_c9e0d:                               1
;     loop_c9ed6:                               1
;     loop_c9f15:                               1
;     loop_c9f2c:                               1
;     loop_c9f7a:                               1
;     loop_c9fc0:                               1
;     loop_c9fdf:                               1
;     loop_c9fe8:                               1
;     loop_ca035:                               1
;     loop_ca04f:                               1
;     loop_ca132:                               1
;     loop_ca14d:                               1
;     loop_ca158:                               1
;     loop_ca16f:                               1
;     loop_ca18c:                               1
;     loop_ca190:                               1
;     loop_ca1ca:                               1
;     loop_ca205:                               1
;     loop_ca20d:                               1
;     loop_ca218:                               1
;     loop_ca229:                               1
;     loop_ca22d:                               1
;     loop_ca254:                               1
;     loop_ca28a:                               1
;     loop_ca290:                               1
;     loop_ca4e6:                               1
;     loop_ca4fa:                               1
;     loop_ca573:                               1
;     loop_ca583:                               1
;     loop_ca878:                               1
;     loop_ca8a0:                               1
;     loop_ca8de:                               1
;     loop_ca8fd:                               1
;     loop_ca93d:                               1
;     loop_ca950:                               1
;     loop_ca9f4:                               1
;     loop_caa0b:                               1
;     loop_caa18:                               1
;     loop_cab77:                               1
;     loop_cab96:                               1
;     loop_cac5d:                               1
;     loop_cac9d:                               1
;     loop_cad17:                               1
;     loop_cae0a:                               1
;     loop_cae5d:                               1
;     loop_caea9:                               1
;     loop_caeb7:                               1
;     loop_caef5:                               1
;     loop_caf7d:                               1
;     loop_cafa0:                               1
;     loop_caffb:                               1
;     loop_cb012:                               1
;     loop_cb02a:                               1
;     loop_cb0e4:                               1
;     loop_cb14b:                               1
;     loop_cb155:                               1
;     loop_cb167:                               1
;     loop_cb1ec:                               1
;     loop_cb204:                               1
;     loop_cb22f:                               1
;     loop_cb27c:                               1
;     loop_cb2c6:                               1
;     loop_cb2fe:                               1
;     loop_cb32b:                               1
;     loop_cb383:                               1
;     loop_cb399:                               1
;     loop_cb3c2:                               1
;     loop_cb3ed:                               1
;     loop_cb412:                               1
;     loop_cb43c:                               1
;     loop_cb44c:                               1
;     loop_cb4bc:                               1
;     loop_cb4cf:                               1
;     loop_cb4fd:                               1
;     loop_cb5de:                               1
;     loop_cb662:                               1
;     loop_cb711:                               1
;     loop_cb72b:                               1
;     loop_cb735:                               1
;     loop_cb7ae:                               1
;     loop_cb953:                               1
;     loop_cb9b2:                               1
;     loop_cba0d:                               1
;     loop_cba25:                               1
;     loop_cba52:                               1
;     loop_cba63:                               1
;     loop_cba7b:                               1
;     loop_cba85:                               1
;     loop_cbaa7:                               1
;     loop_cbaaf:                               1
;     loop_cbae4:                               1
;     loop_cbb41:                               1
;     loop_cbb4c:                               1
;     loop_cbb5a:                               1
;     loop_cbb87:                               1
;     loop_cbb8a:                               1
;     loop_cbbb5:                               1
;     loop_cbbd7:                               1
;     loop_cbbfe:                               1
;     loop_cbc1b:                               1
;     loop_cbc2e:                               1
;     loop_cbc3d:                               1
;     loop_cbc4a:                               1
;     loop_cbc6b:                               1
;     loop_cbc7b:                               1
;     loop_cbe9a:                               1
;     loop_cbeb4:                               1
;     mj:                                       1
;     netv:                                     1
;     next_rom_page:                            1
;     next_scout_byte:                          1
;     nfs_temp:                                 1
;     nmi_code_base:                            1
;     nmi_data_rx_bulk:                         1
;     nmi_data_rx_skip:                         1
;     nmi_data_tx:                              1
;     nmi_final_ack_validate:                   1
;     nmi_reply_validate:                       1
;     nmi_rx_scout:                             1
;     nmi_workspace_start:                      1
;     notify_new_fs:                            1
;     open_and_read_file:                       1
;     osbyte_mode_read_codes:                   1
;     osbyte_x0_y0:                             1
;     osbyte_yff:                               1
;     oscli:                                    1
;     oseven:                                   1
;     osgbpb:                                   1
;     osrdsc:                                   1
;     osrdsc_ptr_hi:                            1
;     osword_claim_codes:                       1
;     osword_dispatch_lo_table:                 1
;     osword_handler_hi_table:                  1
;     osword_handler_lo_table:                  1
;     osword_setup_handler:                     1
;     pass_send_cmd:                            1
;     poll_r2_osword_result:                    1
;     poll_r4_copro_ack:                        1
;     prep_send_tx_cb:                          1
;     print_file_server_is:                     1
;     print_fs_info_newline:                    1
;     print_hex_nybble:                         1
;     print_load_exec_addrs:                    1
;     print_num_no_leading:                     1
;     prot_bit_encode_table:                    1
;     ps_tx_header_template:                    1
;     push_osword_handler_addr:                 1
;     pydis_start:                              1
;     raise_escape_error:                       1
;     read_osargs_params:                       1
;     read_osbyte_to_ws:                        1
;     read_osbyte_to_ws_x0:                     1
;     read_osgbpb_ctrl_blk:                     1
;     read_rdln_ctrl_block:                     1
;     read_second_rx_byte:                      1
;     read_sr2_between_pairs:                   1
;     reloc_p4_src:                             1
;     reloc_p5_src:                             1
;     reloc_p6_src:                             1
;     reloc_zp_src:                             1
;     reset_enter_listen:                       1
;     restore_catalog_entry:                    1
;     restore_romsel_rts:                       1
;     restore_x_and_return:                     1
;     retreat_y_by_4:                           1
;     return_1:                                 1
;     return_11:                                1
;     return_13:                                1
;     return_14:                                1
;     return_16:                                1
;     return_17:                                1
;     return_18:                                1
;     return_19:                                1
;     return_2:                                 1
;     return_20:                                1
;     return_22:                                1
;     return_25:                                1
;     return_28:                                1
;     return_29:                                1
;     return_30:                                1
;     return_31:                                1
;     return_32:                                1
;     return_33:                                1
;     return_34:                                1
;     return_6:                                 1
;     return_8:                                 1
;     return_rx_complete:                       1
;     roff_off_string:                          1
;     rom_header:                               1
;     rom_header_byte1:                         1
;     rom_header_byte2:                         1
;     rom_type:                                 1
;     rotate_prot_mask:                         1
;     rx_error_reset:                           1
;     rx_palette_txcb_template:                 1
;     rx_tube_data:                             1
;     scan_copyright_end:                       1
;     scan_fcb_flags:                           1
;     scan_nfs_port_list:                       1
;     scan_pass_prompt:                         1
;     scan_port_list:                           1
;     scan_remote_keys:                         1
;     scout_discard:                            1
;     scout_loop_rda:                           1
;     scout_loop_second:                        1
;     scout_match_port:                         1
;     scout_page_overflow:                      1
;     scout_reject:                             1
;     send_data_rx_ack:                         1
;     send_osargs_result:                       1
;     send_osfile_ctrl_blk:                     1
;     send_osgbpb_result:                       1
;     send_request_nowrite:                     1
;     send_rom_page_bytes:                      1
;     send_xfer_addr_bytes:                     1
;     serialise_palette_entry:                  1
;     service_entry:                            1
;     service_handler:                          1
;     service_handler_lo:                       1
;     set_rx_buf_len_hi:                        1
;     set_text_and_xfer_ptr:                    1
;     set_tx_reply_flag:                        1
;     setup_cb1_sr_tx:                          1
;     setup_data_xfer:                          1
;     setup_pass_txbuf:                         1
;     setup_unicast_xfer:                       1
;     skip_buf_ptr_update:                      1
;     skip_one_and_advance5:                    1
;     skip_param_read:                          1
;     skip_r3_flush:                            1
;     skip_tube_update:                         1
;     start_data_tx:                            1
;     store_buf_ptr_lo:                         1
;     store_osword_pb_ptr:                      1
;     store_ptr_at_ws_y:                        1
;     store_ws_page_count:                      1
;     store_xfer_end_addr:                      1
;     string_buf_done:                          1
;     strnh:                                    1
;     sub_cbe5e:                                1
;     svc_dispatch_hi:                          1
;     svc_dispatch_lo:                          1
;     test_tube_release:                        1
;     tube_begin:                               1
;     tube_brk_send_loop:                       1
;     tube_claim_default:                       1
;     tube_cmd_lo:                              1
;     tube_ctrl_values:                         1
;     tube_data_ptr_hi:                         1
;     tube_data_register_4:                     1
;     tube_escape_check:                        1
;     tube_handle_wrch:                         1
;     tube_osbyte_reply_block:                  1
;     tube_osbyte_send_y:                       1
;     tube_osfind_close:                        1
;     tube_osword_read:                         1
;     tube_osword_write:                        1
;     tube_osword_write_lp:                     1
;     tube_page4_vectors:                       1
;     tube_poll_r2:                             1
;     tube_rdch_reply:                          1
;     tube_rdln_send_line:                      1
;     tube_rdln_send_loop:                      1
;     tube_release_claim:                       1
;     tube_reset_stack:                         1
;     tube_return_main:                         1
;     tube_send_error_byte:                     1
;     tube_send_error_num:                      1
;     tube_send_zero_r2:                        1
;     tube_sendw_complete:                      1
;     tube_transfer_setup:                      1
;     tube_tx_inc_operand:                      1
;     tube_tx_sr1_operand:                      1
;     tx_check_tdra_ready:                      1
;     tx_ctrl_exit:                             1
;     tx_ctrl_range_check:                      1
;     tx_data_start:                            1
;     tx_done_exit:                             1
;     tx_done_fire_event:                       1
;     tx_econet_txcb_template:                  1
;     tx_error:                                 1
;     tx_fifo_not_ready:                        1
;     tx_fifo_write:                            1
;     tx_imm_op_setup:                          1
;     tx_last_data:                             1
;     tx_line_idle_check:                       1
;     tx_line_jammed:                           1
;     tx_no_clock_error:                        1
;     tx_prepare:                               1
;     tx_src_net:                               1
;     tx_store_error:                           1
;     tx_tdra_error:                            1
;     txcb_copy_carry_clr:                      1
;     txcb_copy_carry_set:                      1
;     txcb_dest:                                1
;     txcb_init_template:                       1
;     txcb_pos:                                 1
;     update_addr_from_offset1:                 1
;     update_addr_from_offset9:                 1
;     vdu_screen_mode:                          1
;     write_error_num_and_str:                  1
;     write_ps_slot_link_addr:                  1
;     write_second_tx_byte:                     1
;     write_two_bytes_inc_y:                    1
;     ws_copy_vclr_entry:                       1
;     ws_init_data:                             1

; Automatically generated labels:
;     c06ef
;     c802d
;     c8052
;     c87e8
;     c88f7
;     c8a29
;     c8a2e
;     c8a32
;     c8a49
;     c8a50
;     c8a58
;     c8a65
;     c8a68
;     c8a90
;     c8ab2
;     c8ac3
;     c8af3
;     c8b28
;     c8b9d
;     c8ba3
;     c8bab
;     c8bd5
;     c8be5
;     c8beb
;     c8bf5
;     c8c07
;     c8c14
;     c8c19
;     c8c1b
;     c8c24
;     c8c68
;     c8c72
;     c8c8d
;     c8ccf
;     c8cd5
;     c8cff
;     c8d1b
;     c8d9c
;     c8dc7
;     c8de0
;     c8def
;     c8e9d
;     c8f23
;     c8f2f
;     c8fa4
;     c900a
;     c912c
;     c913f
;     c9157
;     c9169
;     c9174
;     c9184
;     c9186
;     c919a
;     c91c6
;     c91cf
;     c91e5
;     c91e7
;     c91fd
;     c9215
;     c9221
;     c9230
;     c9253
;     c9263
;     c926f
;     c92cd
;     c932a
;     c9344
;     c934f
;     c935d
;     c938e
;     c939a
;     c93a8
;     c93da
;     c93f1
;     c93f8
;     c9428
;     c944e
;     c9472
;     c94bf
;     c94c5
;     c94ee
;     c94f1
;     c94fa
;     c9506
;     c952f
;     c953b
;     c9545
;     c9570
;     c9573
;     c95d8
;     c95de
;     c95f1
;     c9604
;     c9620
;     c9633
;     c963b
;     c965e
;     c9670
;     c9672
;     c9682
;     c9684
;     c9699
;     c96e5
;     c96e8
;     c970a
;     c970d
;     c9717
;     c972b
;     c9752
;     c978f
;     c9831
;     c983a
;     c9856
;     c985e
;     c9869
;     c986d
;     c9896
;     c98a3
;     c98b4
;     c98c9
;     c98d6
;     c98de
;     c98ed
;     c9912
;     c9938
;     c9955
;     c995b
;     c99af
;     c99b4
;     c99f8
;     c9a05
;     c9a0b
;     c9a0e
;     c9a1e
;     c9a52
;     c9a84
;     c9a8e
;     c9ab7
;     c9ac0
;     c9add
;     c9ae9
;     c9b0e
;     c9b23
;     c9b2a
;     c9b2f
;     c9b35
;     c9b3a
;     c9b44
;     c9b7f
;     c9b80
;     c9b99
;     c9ba6
;     c9bc1
;     c9bc9
;     c9be9
;     c9bf4
;     c9c3d
;     c9c40
;     c9c5c
;     c9c7e
;     c9cb6
;     c9cc8
;     c9cd3
;     c9cdf
;     c9ce1
;     c9ce3
;     c9ce6
;     c9d5f
;     c9d71
;     c9d75
;     c9d7b
;     c9d7e
;     c9d97
;     c9d9d
;     c9daf
;     c9db2
;     c9dc6
;     c9dc9
;     c9dce
;     c9dd3
;     c9dfd
;     c9dff
;     c9e19
;     c9e1c
;     c9e36
;     c9e39
;     c9e44
;     c9e83
;     c9e86
;     c9ee1
;     c9eea
;     c9ef8
;     c9f40
;     c9f43
;     c9f55
;     c9f6a
;     c9f78
;     c9f8c
;     c9fcd
;     c9fda
;     c9ff7
;     ca033
;     ca058
;     ca083
;     ca0a5
;     ca0ad
;     ca0b1
;     ca0dd
;     ca0df
;     ca0f1
;     ca11b
;     ca12a
;     ca141
;     ca152
;     ca164
;     ca16d
;     ca175
;     ca179
;     ca18a
;     ca18b
;     ca191
;     ca19f
;     ca1a6
;     ca1b2
;     ca1d2
;     ca1ee
;     ca1f1
;     ca22b
;     ca242
;     ca252
;     ca265
;     ca281
;     ca2d7
;     ca2eb
;     ca301
;     ca30f
;     ca316
;     ca32c
;     ca33a
;     ca34d
;     ca363
;     ca371
;     ca39c
;     ca3cb
;     ca50f
;     ca526
;     ca589
;     ca594
;     ca6fb
;     ca701
;     ca88c
;     ca8c0
;     ca8e6
;     ca926
;     ca959
;     ca97a
;     ca9e9
;     ca9f2
;     caa1c
;     caa24
;     caa78
;     caa8d
;     caa8f
;     caa95
;     caa97
;     caa9b
;     caa9f
;     caaea
;     cab21
;     cab24
;     cab63
;     cab72
;     caba3
;     caba5
;     cabcc
;     cabe1
;     cabfe
;     cac1e
;     cac2d
;     cac38
;     cac55
;     cad0e
;     cad1d
;     cad84
;     cada0
;     cadd1
;     caddb
;     cae15
;     cae3d
;     cae72
;     cae7d
;     caec6
;     caec9
;     caecd
;     caed0
;     caedf
;     caee9
;     caf05
;     caf07
;     caf20
;     caf3a
;     caf3c
;     caf3f
;     caf52
;     caf8d
;     cafad
;     cafd8
;     cb005
;     cb008
;     cb038
;     cb04b
;     cb06d
;     cb075
;     cb08a
;     cb092
;     cb095
;     cb0b6
;     cb0f4
;     cb0f8
;     cb120
;     cb12f
;     cb184
;     cb18d
;     cb1e1
;     cb1e4
;     cb212
;     cb23d
;     cb243
;     cb278
;     cb288
;     cb2b8
;     cb2bb
;     cb2d1
;     cb2d3
;     cb2e9
;     cb2fa
;     cb319
;     cb34d
;     cb380
;     cb387
;     cb38c
;     cb395
;     cb3db
;     cb3f6
;     cb3fa
;     cb3fc
;     cb40b
;     cb411
;     cb465
;     cb467
;     cb473
;     cb4b1
;     cb50b
;     cb548
;     cb54e
;     cb553
;     cb557
;     cb56b
;     cb58f
;     cb596
;     cb5a0
;     cb5aa
;     cb5ab
;     cb5b2
;     cb5c1
;     cb62f
;     cb657
;     cb675
;     cb678
;     cb6cc
;     cb6f2
;     cb716
;     cb720
;     cb73a
;     cb73d
;     cb757
;     cb78e
;     cb7b9
;     cb7bf
;     cb7ee
;     cb819
;     cb82a
;     cb87d
;     cb88b
;     cb8dd
;     cb8f1
;     cb910
;     cb960
;     cb969
;     cb995
;     cb9a1
;     cb9b0
;     cb9b8
;     cb9c5
;     cb9d2
;     cb9d8
;     cb9df
;     cb9e4
;     cb9ef
;     cba1e
;     cba37
;     cba3e
;     cba45
;     cba50
;     cba9b
;     cbab1
;     cbac0
;     cbac9
;     cbb39
;     cbb53
;     cbb61
;     cbb80
;     cbbab
;     cbbaf
;     cbbb6
;     cbbe3
;     cbbe9
;     cbc03
;     cbc51
;     cbc66
;     cbe6f
;     l0006
;     l0063
;     l0078
;     l0085
;     l00ad
;     l00ae
;     l00af
;     l00b6
;     l00cc
;     l00d0
;     l00da
;     l0102
;     l0103
;     l0104
;     l0106
;     l0128
;     l026a
;     l028d
;     l02a0
;     l0351
;     l0355
;     l072c
;     l072e
;     l0a0e
;     l0d07
;     l0d1a
;     l0d2e
;     l0d2f
;     l0d30
;     l0d31
;     l0d42
;     l0d43
;     l0d44
;     l0d61
;     l0d63
;     l0d6b
;     l0d6c
;     l0d6d
;     l0d6e
;     l0d6f
;     l0d70
;     l0d72
;     l0de6
;     l0df0
;     l0dfa
;     l0dfe
;     l0e00
;     l0e01
;     l0e02
;     l0e03
;     l0e04
;     l0e05
;     l0e06
;     l0e07
;     l0e09
;     l0e0a
;     l0e0b
;     l0e16
;     l0e2f
;     l0e30
;     l0e31
;     l0e32
;     l0e38
;     l0ef7
;     l0f00
;     l0f01
;     l0f02
;     l0f03
;     l0f04
;     l0f05
;     l0f06
;     l0f07
;     l0f08
;     l0f09
;     l0f0a
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
;     l0f2f
;     l0f30
;     l0fdc
;     l0fdd
;     l0fde
;     l0fdf
;     l0fe0
;     l0ff0
;     l1000
;     l1010
;     l1020
;     l1030
;     l1040
;     l1050
;     l1060
;     l1070
;     l1071
;     l1072
;     l1073
;     l1074
;     l1078
;     l1088
;     l1098
;     l10a8
;     l10b8
;     l10c8
;     l10c9
;     l10ca
;     l10cb
;     l10cc
;     l10cd
;     l10ce
;     l10cf
;     l10d0
;     l10d1
;     l10d4
;     l10d5
;     l10d6
;     l10d7
;     l10d8
;     l10d9
;     l10f3
;     l2322
;     l6f6e
;     l7dfd
;     loop_c06df
;     loop_c83da
;     loop_c8ae6
;     loop_c8b1a
;     loop_c8b2d
;     loop_c8b40
;     loop_c8b6f
;     loop_c8bb5
;     loop_c8bbf
;     loop_c8bfb
;     loop_c8c3a
;     loop_c8c75
;     loop_c8d10
;     loop_c8d21
;     loop_c8da3
;     loop_c8db6
;     loop_c8dd9
;     loop_c8e71
;     loop_c8ed5
;     loop_c8eff
;     loop_c8f11
;     loop_c8f29
;     loop_c8f75
;     loop_c8f97
;     loop_c8fa1
;     loop_c8fbb
;     loop_c9139
;     loop_c9267
;     loop_c9292
;     loop_c9315
;     loop_c931e
;     loop_c933b
;     loop_c9387
;     loop_c93dc
;     loop_c9462
;     loop_c94a7
;     loop_c94e4
;     loop_c950b
;     loop_c9547
;     loop_c9614
;     loop_c9652
;     loop_c9676
;     loop_c9693
;     loop_c96ae
;     loop_c96d1
;     loop_c971f
;     loop_c977f
;     loop_c9850
;     loop_c9889
;     loop_c98af
;     loop_c98c4
;     loop_c98e3
;     loop_c98f5
;     loop_c9907
;     loop_c995d
;     loop_c9978
;     loop_c998d
;     loop_c998f
;     loop_c99a3
;     loop_c99b9
;     loop_c99d7
;     loop_c9a1b
;     loop_c9a2c
;     loop_c9a62
;     loop_c9a75
;     loop_c9a99
;     loop_c9aab
;     loop_c9ab9
;     loop_c9b01
;     loop_c9b18
;     loop_c9b66
;     loop_c9b73
;     loop_c9b8d
;     loop_c9ba4
;     loop_c9bc6
;     loop_c9bd9
;     loop_c9c27
;     loop_c9c4f
;     loop_c9c85
;     loop_c9d1e
;     loop_c9e0d
;     loop_c9ed6
;     loop_c9f15
;     loop_c9f2c
;     loop_c9f7a
;     loop_c9fc0
;     loop_c9fdf
;     loop_c9fe8
;     loop_ca035
;     loop_ca04f
;     loop_ca132
;     loop_ca14d
;     loop_ca158
;     loop_ca16f
;     loop_ca18c
;     loop_ca190
;     loop_ca1ca
;     loop_ca205
;     loop_ca20d
;     loop_ca218
;     loop_ca229
;     loop_ca22d
;     loop_ca254
;     loop_ca28a
;     loop_ca290
;     loop_ca4e6
;     loop_ca4fa
;     loop_ca573
;     loop_ca583
;     loop_ca878
;     loop_ca8a0
;     loop_ca8de
;     loop_ca8fd
;     loop_ca93d
;     loop_ca950
;     loop_ca9f4
;     loop_caa0b
;     loop_caa18
;     loop_cab77
;     loop_cab96
;     loop_cac5d
;     loop_cac9d
;     loop_cad17
;     loop_cae0a
;     loop_cae5d
;     loop_caea9
;     loop_caeb7
;     loop_caef5
;     loop_caf7d
;     loop_cafa0
;     loop_caffb
;     loop_cb012
;     loop_cb02a
;     loop_cb0e4
;     loop_cb14b
;     loop_cb155
;     loop_cb167
;     loop_cb1ec
;     loop_cb204
;     loop_cb22f
;     loop_cb27c
;     loop_cb2c6
;     loop_cb2fe
;     loop_cb32b
;     loop_cb383
;     loop_cb399
;     loop_cb3c2
;     loop_cb3ed
;     loop_cb412
;     loop_cb43c
;     loop_cb44c
;     loop_cb4bc
;     loop_cb4cf
;     loop_cb4fd
;     loop_cb5de
;     loop_cb662
;     loop_cb711
;     loop_cb72b
;     loop_cb735
;     loop_cb7ae
;     loop_cb953
;     loop_cb9b2
;     loop_cba0d
;     loop_cba25
;     loop_cba52
;     loop_cba63
;     loop_cba7b
;     loop_cba85
;     loop_cbaa7
;     loop_cbaaf
;     loop_cbae4
;     loop_cbb41
;     loop_cbb4c
;     loop_cbb5a
;     loop_cbb87
;     loop_cbb8a
;     loop_cbbb5
;     loop_cbbd7
;     loop_cbbfe
;     loop_cbc1b
;     loop_cbc2e
;     loop_cbc3d
;     loop_cbc4a
;     loop_cbc6b
;     loop_cbc7b
;     loop_cbe9a
;     loop_cbeb4
;     return_1
;     return_10
;     return_11
;     return_12
;     return_13
;     return_14
;     return_15
;     return_16
;     return_17
;     return_18
;     return_19
;     return_2
;     return_20
;     return_21
;     return_22
;     return_23
;     return_24
;     return_25
;     return_26
;     return_27
;     return_28
;     return_29
;     return_3
;     return_30
;     return_31
;     return_32
;     return_33
;     return_34
;     return_35
;     return_4
;     return_5
;     return_6
;     return_7
;     return_8
;     return_9
;     sub_cbe5e

; Stats:
;     Total size (Code + Data) = 16384 bytes
;     Code                     = 13767 bytes (84%)
;     Data                     = 2617 bytes (16%)
;
;     Number of instructions   = 6741
;     Number of data bytes     = 1414 bytes
;     Number of data words     = 0 bytes
;     Number of string bytes   = 1203 bytes
;     Number of strings        = 150
