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
romsel                                      = 65072
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
rom_svc_num                             = &00a9
l00ae                                   = &00ae
l00af                                   = &00af
fs_load_addr                            = &00b0
fs_load_addr_hi                         = &00b1
fs_load_addr_2                          = &00b2
l00b3                                   = &00b3
l00b4                                   = &00b4
l00b5                                   = &00b5
l00b6                                   = &00b6
l00b7                                   = &00b7
fs_error_ptr                            = &00b8
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
l00ef                                   = &00ef
l00f0                                   = &00f0
l00f1                                   = &00f1
os_text_ptr                             = &00f2
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
l0d60                                   = &0d60
printer_buf_ptr                         = &0d61
tx_clear_flag                           = &0d62
prot_status                             = &0d63
rx_flags                                = &0d64
saved_jsr_mask                          = &0d65
econet_init_flag                        = &0d66
tube_flag                               = &0d67
l0dda                                   = &0dda
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
l0e0c                                   = &0e0c
fs_reply_status                         = &0e0d
fs_target_stn                           = &0e0e
fs_cmd_ptr                              = &0e10
l0e11                                   = &0e11
l0e16                                   = &0e16
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
l0fc5                                   = &0fc5
l0fc6                                   = &0fc6
fs_putb_buf                             = &0fdc
fs_getb_buf                             = &0fdd
l0fde                                   = &0fde
l0fdf                                   = &0fdf
l0fe0                                   = &0fe0
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

    org &8000

; Sideways ROM header
; NFS ROM 3.34 disassembly (Acorn Econet filing system)
; 
; NMI handler architecture
; ========================
; The NFS ROM uses self-modifying code to implement a state machine for
; ADLC communication. An NMI workspace shim is copied to $0D00 at init.
; 
; NMI entry ($0D00):
;   BIT $FE18       ; INTOFF -- immediately disable further NMIs
;   PHA / TYA / PHA ; save A, Y
;   LDA #$nn        ; page in NFS ROM bank (self-modified at init)
;   STA $FE30
;   JMP $xxxx       ; self-modifying target at $0D0C/$0D0D
; 
; set_nmi_vector ($0D0E): stores A->$0D0C (low), Y->$0D0D (high)
;   Falls through to nmi_rti.
; 
; nmi_rti ($0D14):
;   LDA $F4         ; restore original ROM bank
;   STA $FE30
;   PLA / TAY / PLA ; restore Y, A
;   BIT $FE20       ; INTON -- re-enable NMIs
;   RTI
; 
; NMI handler chain for outbound transmission (four-way handshake):
;   $96F6: RX scout (idle listen, default handler)
;   $9C48: INACTIVE polling (pre-TX, waits for idle line)
;   $9D4C: TX data (2 bytes per NMI, tight loop if IRQ persists)
;   $9D88: TX_LAST_DATA (close frame)
;   $9D94: TX completion (switch to RX: CR1=$82)
;   $9DB2: RX reply scout (check AP, read dest_stn)
;   $9DC8: RX reply continuation (read dest_net, validate)
;   $9DE3: RX reply validation (read src_stn/net, check FV)
;   $9E24: TX scout ACK (write dest/src addr, TX_LAST_DATA)
;   $9EDD: Four-way handshake data phase
; 
; NMI handler chain for inbound reception (scout -> data):
;   $96F6: RX scout (idle listen)
;   $9715: RX scout second byte (dest_net, install $9747)
;   $9747: Scout data loop (read body in pairs, detect FV)
;   $9771: Scout completion (disable PSE, read last byte)
;   $995E: TX scout ACK
;   $9839: RX data frame (AP check, validate dest_stn/net)
;   $984F: RX data frame (validate src_net=0)
;   $9865: RX data frame (skip ctrl/port bytes)
;   $989A: RX data bulk read (read payload into buffer)
;   $98CE: RX data completion (disable PSE, check FV, read last)
;   $995E: TX final ACK
; 
; Key ADLC register values:
;   CR1=$C1: full reset (TX_RESET|RX_RESET|AC)
;   CR1=$82: RX listen (TX_RESET|RIE)
;   CR1=$44: TX active (RX_RESET|TIE)
;   CR2=$67: clear all status (CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
;   CR2=$E7: TX prepare (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
;   CR2=$3F: TX last data (CLR_RX_ST|TX_LAST_DATA|FLAG_IDLE|FC_TDRA|2_1_BYTE|PSE)
;   CR2=$A7: TX in handshake (RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE)
; &8000 referenced 1 time by &048b[2]
.pydis_start
.rom_header
.language_entry
l8001 = rom_header+1
l8002 = rom_header+2
    jmp language_handler                                              ; 8000: 4c 99 80    L..

; &8001 referenced 1 time by &0490[2]
; &8002 referenced 1 time by &0495[2]
; &8003 referenced 1 time by &049a[2]
.service_entry
l8004 = service_entry+1
    jmp service_handler                                               ; 8003: 4c af 80    L..

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
.l800d
l8014 = l800d+7
    equs "(C)ROFF", 0                                                 ; 800d: 28 43 29... (C)
; &8014 referenced 1 time by &842d
    equb &0d, &18                                                     ; 8015: 0d 18       ..
    equs "'1;;CO"                                                     ; 8017: 27 31 3b... '1;
    equb 1, 0, &34                                                    ; 801d: 01 00 34    ..4
; Dispatch table: low bytes of (handler_address - 1)
; Each entry stores the low byte of a handler address minus 1,
; for use with the PHA/PHA/RTS dispatch trick at $809F.
; See dispatch_hi ($8044) for the corresponding high bytes.
; Indexed by service number (1-13), language reason (14-18),
; or *NET command (33-36), with a base offset added by the caller.
; &8020 referenced 1 time by &80a8
.dispatch_lo
    equb 3                                                            ; 8020: 03          .
    equb <(return_2-1)                                                ; 8021: 44          D
    equb <(svc_abs_workspace-1)                                       ; 8022: 6e          n
    equb <(svc_private_workspace-1)                                   ; 8023: 77          w
    equb <(svc_autoboot-1)                                            ; 8024: d0          .
    equb <(svc_star_command-1)                                        ; 8025: 71          q
    equb <(svc_unknown_irq-1)                                         ; 8026: 6b          k
    equb <(return_2-1)                                                ; 8027: 44          D
    equb <(dispatch_net_cmd-1)                                        ; 8028: 68          h
    equb <(osword_fs_entry-1)                                         ; 8029: f6          .
    equb <(svc_help-1)                                                ; 802a: bb          .
    equb <(return_2-1)                                                ; 802b: 44          D
    equb <(svc_nmi_claim-1)                                           ; 802c: 68          h
    equb <(svc_nmi_release-1)                                         ; 802d: 65          e
    equb <(insert_remote_key-1)                                       ; 802e: 49          I
    equb <(remote_boot_handler-1)                                     ; 802f: fb          .
    equb <(save_palette_vdu-1)                                        ; 8030: 90          .
    equb <(execute_at_0100-1)                                         ; 8031: 29          )
    equb <(remote_validated-1)                                        ; 8032: 39          9
    equb <(opt_handler-1)                                             ; 8033: a0          .
    equb <(eof_handler-1)                                             ; 8034: 1e          .
    equb <(fscv_star_handler-1)                                       ; 8035: 91          .
    equb <(fscv_star_handler-1)                                       ; 8036: 91          .
    equb <(fscv_star_handler-1)                                       ; 8037: 91          .
    equb <(cat_handler-1)                                             ; 8038: fc          .
    equb <(fscv_shutdown-1)                                           ; 8039: fc          .
    equb <(fscv_read_handles-1)                                       ; 803a: d9          .
    equb <(print_dir_name-1)                                          ; 803b: 72          r
    equb <(copy_handles_and_boot-1)                                   ; 803c: 1e          .
    equb <(copy_handles-1)                                            ; 803d: 1f          .
    equb <(set_csd_handle-1)                                          ; 803e: fb          .
    equb <(notify_and_exec-1)                                         ; 803f: 83          .
    equb <(set_lib_handle-1)                                          ; 8040: f6          .
    equb <(net1_read_handle-1)                                        ; 8041: ae          .
    equb <(net2_read_handle_entry-1)                                  ; 8042: c8          .
    equb <(net3_close_handle-1)                                       ; 8043: de          .
; Dispatch table: high bytes of (handler_address - 1)
; Paired with dispatch_lo ($8020). Together they form a table of
; 37 handler addresses, used via the PHA/PHA/RTS trick at $809F.
; &8044 referenced 1 time by &80a4
.dispatch_hi
    equb <(net4_resume_remote-1)                                      ; 8044: f1          .
    equb >(return_2-1)                                                ; 8045: 81          .
    equb >(svc_abs_workspace-1)                                       ; 8046: 82          .
    equb >(svc_private_workspace-1)                                   ; 8047: 82          .
    equb >(svc_autoboot-1)                                            ; 8048: 81          .
    equb >(svc_star_command-1)                                        ; 8049: 81          .
    equb >(svc_unknown_irq-1)                                         ; 804a: 96          .
    equb >(return_2-1)                                                ; 804b: 81          .
    equb >(dispatch_net_cmd-1)                                        ; 804c: 80          .
    equb >(osword_fs_entry-1)                                         ; 804d: 8d          .
    equb >(svc_help-1)                                                ; 804e: 81          .
    equb >(return_2-1)                                                ; 804f: 81          .
    equb >(svc_nmi_claim-1)                                           ; 8050: 96          .
    equb >(svc_nmi_release-1)                                         ; 8051: 96          .
    equb >(insert_remote_key-1)                                       ; 8052: 91          .
    equb >(remote_boot_handler-1)                                     ; 8053: 90          .
    equb >(save_palette_vdu-1)                                        ; 8054: 92          .
    equb >(execute_at_0100-1)                                         ; 8055: 91          .
    equb >(remote_validated-1)                                        ; 8056: 91          .
    equb >(opt_handler-1)                                             ; 8057: 89          .
    equb >(eof_handler-1)                                             ; 8058: 88          .
    equb >(fscv_star_handler-1)                                       ; 8059: 8b          .
    equb >(fscv_star_handler-1)                                       ; 805a: 8b          .
    equb >(fscv_star_handler-1)                                       ; 805b: 8b          .
    equb >(cat_handler-1)                                             ; 805c: 8b          .
    equb >(fscv_shutdown-1)                                           ; 805d: 82          .
    equb >(fscv_read_handles-1)                                       ; 805e: 85          .
    equb >(print_dir_name-1)                                          ; 805f: 8d          .
    equb >(copy_handles_and_boot-1)                                   ; 8060: 8d          .
    equb >(copy_handles-1)                                            ; 8061: 8d          .
    equb >(set_csd_handle-1)                                          ; 8062: 8c          .
    equb >(notify_and_exec-1)                                         ; 8063: 8d          .
    equb >(set_lib_handle-1)                                          ; 8064: 8c          .
    equb >(net1_read_handle-1)                                        ; 8065: 8d          .
    equb >(net2_read_handle_entry-1)                                  ; 8066: 8d          .
    equb >(net3_close_handle-1)                                       ; 8067: 8d          .
    equb >(net4_resume_remote-1)                                      ; 8068: 8d          .

; *NET command dispatcher
; Parses the character after *NET as '1'-'4', maps to table
; indices 33-36 via base offset Y=$20, and dispatches via $809F.
; Characters outside '1'-'4' fall through to return_1 (RTS).
.dispatch_net_cmd
    lda l00ef                                                         ; 8069: a5 ef       ..             ; Read command character following *NET
    sbc #&31 ; '1'                                                    ; 806b: e9 31       .1             ; Subtract ASCII '1' to get 0-based command index
    bmi return_1                                                      ; 806d: 30 3f       0?
    cmp #4                                                            ; 806f: c9 04       ..
    bcs return_1                                                      ; 8071: b0 3b       .;
    tax                                                               ; 8073: aa          .
    tya                                                               ; 8074: 98          .
    ldy #&20 ; ' '                                                    ; 8075: a0 20       .              ; Y=$20: base offset for *NET commands (index 33+)
    bne dispatch                                                      ; 8077: d0 26       .&             ; ALWAYS branch

; Forward unrecognised * command to fileserver (COMERR)
; Copies command text from (fs_crc_lo) to $0F05+ via copy_filename,
; prepares an FS command with function code 0, and sends it to the
; fileserver to request decoding. The server returns a command code
; indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
; 5=load-as-command). This mechanism allows the fileserver to extend
; the client's command set without ROM updates. Called from the "I."
; and catch-all entries in the command match table at $8BD6, and
; from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
; in), returns without sending.
; &8079 referenced 1 time by &8d1c
.forward_star_cmd
    jsr copy_filename                                                 ; 8079: 20 63 8d     c.
    tay                                                               ; 807c: a8          .              ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 807d: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    ldx fs_cmd_csd                                                    ; 8080: ae 03 0f    ...            ; X=depends on function
    beq return_1                                                      ; 8083: f0 29       .)
    lda fs_cmd_data                                                   ; 8085: ad 05 0f    ...            ; A=function code (0-7)
    ldy #&16                                                          ; 8088: a0 16       ..             ; Y=depends on function
    bne dispatch                                                      ; 808a: d0 13       ..             ; ALWAYS branch

; ***************************************************************************************
; FSCV dispatch entry
; 
; Entered via the extended vector table when the MOS calls FSCV.
; Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
; and dispatches codes 0-7 via the shared dispatch table at $8020
; with base offset Y=$12 (table indices 19-26).
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
    jsr save_fscv_args                                                ; 808c: 20 08 85     ..            ; Store A/X/Y in FS workspace
    cmp #8                                                            ; 808f: c9 08       ..             ; Function code >= 8? Return (unsupported)
    bcs return_1                                                      ; 8091: b0 1b       ..
    tax                                                               ; 8093: aa          .
    tya                                                               ; 8094: 98          .
    ldy #&12                                                          ; 8095: a0 12       ..             ; Y=$12: base offset for FSCV dispatch (indices 19+)
    bne dispatch                                                      ; 8097: d0 06       ..             ; ALWAYS branch

; Language entry dispatcher
; Called when the NFS ROM is entered as a language. X = reason code
; (0-4). Dispatches via table indices 14-18 (base offset Y=$0D).
; &8099 referenced 1 time by &8000
.language_handler
    cpx #5                                                            ; 8099: e0 05       ..
    bcs return_1                                                      ; 809b: b0 11       ..
    ldy #&0d                                                          ; 809d: a0 0d       ..             ; Y=$0D: base offset for language handlers (index 14+)
; PHA/PHA/RTS computed dispatch
; X = command index within caller's group (e.g. service number)
; Y = base offset into dispatch table (0, $0D, $20, etc.)
; The loop adds Y+1 to X, so final X = command index + base + 1.
; Then high and low bytes of (handler-1) are pushed onto the stack,
; and RTS pops them and jumps to handler_address.
; 
; This is a standard 6502 trick: RTS increments the popped address
; by 1 before jumping, so the table stores (address - 1) to
; compensate. Multiple callers share one table via different Y
; base offsets.
; &809f referenced 5 times by &8077, &808a, &8097, &80a1, &8139
.dispatch
    inx                                                               ; 809f: e8          .              ; Add base offset Y to index X (loop: X += Y+1)
    dey                                                               ; 80a0: 88          .
    bpl dispatch                                                      ; 80a1: 10 fc       ..
    tay                                                               ; 80a3: a8          .
    lda dispatch_hi,x                                                 ; 80a4: bd 44 80    .D.            ; Load high byte of (handler - 1) from table
    pha                                                               ; 80a7: 48          H              ; Push high byte onto stack
    lda dispatch_lo,x                                                 ; 80a8: bd 20 80    . .            ; Load low byte of (handler - 1) from table
    pha                                                               ; 80ab: 48          H              ; Push low byte onto stack
    ldx fs_options                                                    ; 80ac: a6 bb       ..             ; Restore X (fileserver options) for use by handler
; &80ae referenced 6 times by &806d, &8071, &8083, &8091, &809b, &80b7
.return_1
    rts                                                               ; 80ae: 60          `              ; RTS pops address, adds 1, jumps to handler

; Service handler entry
; Intercepts three special service calls before normal dispatch:
;   $FE: Tube init — explode character definitions (OSBYTE $14, X=6)
;   $FF: Full init — set up WRCHV/RDCHV/BRKV/EVNTV, copy NMI handler
;        code from ROM to RAM pages $04-$06, copy workspace init to
;        $0016-$0076, then fall through to select NFS.
;   $12 with Y=5: Select NFS as active filing system.
; All other service calls dispatch via dispatch_service ($8127).
; &80af referenced 1 time by &8003
.service_handler
    cmp #&fe                                                          ; 80af: c9 fe       ..
    bcc c811f                                                         ; 80b1: 90 6c       .l
    bne init_vectors_and_copy                                         ; 80b3: d0 13       ..
    cpy #0                                                            ; 80b5: c0 00       ..
    beq return_1                                                      ; 80b7: f0 f5       ..
    stx zp_temp_11                                                    ; 80b9: 86 11       ..
    sty zp_temp_10                                                    ; 80bb: 84 10       ..
    ldx #6                                                            ; 80bd: a2 06       ..
    lda #osbyte_explode_chars                                         ; 80bf: a9 14       ..
    jsr osbyte                                                        ; 80c1: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
    ldx zp_temp_11                                                    ; 80c4: a6 11       ..
    bne c811b                                                         ; 80c6: d0 53       .S
; NFS initialisation (service $FF: full reset)
; Sets up OS vectors for Tube co-processor support:
;   WRCHV = $051C (page 5 — WRCH handler)
;   RDCHV = $04E7 (page 4 — RDCH handler)
;   BRKV  = $0016 (workspace — BRK/error handler)
;   EVNTV = $06E8 (page 6 — event handler)
; Writes $8E to Tube control register ($FEE0).
; Then copies 3 pages of Tube host code from ROM ($934C/$944C/$954C)
; to RAM ($0400/$0500/$0600), calls tube_post_init ($0414), and copies
; 97 bytes of workspace init from ROM ($9307) to $0016-$0076.
; &80c8 referenced 1 time by &80b3
.init_vectors_and_copy
    lda #&1c                                                          ; 80c8: a9 1c       ..             ; Set WRCHV = $051C (Tube WRCH handler)
    sta wrchv                                                         ; 80ca: 8d 0e 02    ...
    lda #5                                                            ; 80cd: a9 05       ..
    sta wrchv+1                                                       ; 80cf: 8d 0f 02    ...
    lda #&e7                                                          ; 80d2: a9 e7       ..             ; Set RDCHV = $04E7 (Tube RDCH handler)
    sta rdchv                                                         ; 80d4: 8d 10 02    ...
    lda #4                                                            ; 80d7: a9 04       ..
    sta rdchv+1                                                       ; 80d9: 8d 11 02    ...
    lda #&16                                                          ; 80dc: a9 16       ..             ; Set BRKV = $0016 (BRK handler in workspace)
    sta brkv                                                          ; 80de: 8d 02 02    ...
    lda #0                                                            ; 80e1: a9 00       ..
    sta brkv+1                                                        ; 80e3: 8d 03 02    ...
    lda #&e8                                                          ; 80e6: a9 e8       ..             ; Set EVNTV = $06E8 (event handler in page 6)
    sta evntv                                                         ; 80e8: 8d 20 02    . .
    lda #6                                                            ; 80eb: a9 06       ..
    sta evntv+1                                                       ; 80ed: 8d 21 02    .!.
    lda #&8e                                                          ; 80f0: a9 8e       ..             ; Write $8E to Tube control register
    sta tube_status_1_and_tube_control                                ; 80f2: 8d e0 fe    ...
    sty zp_temp_10                                                    ; 80f5: 84 10       ..
    ldy #0                                                            ; 80f7: a0 00       ..
; Copy NMI handler code from ROM to RAM pages $04-$06
; &80f9 referenced 1 time by &810c
.loop_c80f9
    lda c934c,y                                                       ; 80f9: b9 4c 93    .L.
    sta tube_code_page4,y                                             ; 80fc: 99 00 04    ...
    lda l944c,y                                                       ; 80ff: b9 4c 94    .L.
    sta tube_dispatch_table,y                                         ; 8102: 99 00 05    ...
    lda c954c,y                                                       ; 8105: b9 4c 95    .L.
    sta tube_code_page6,y                                             ; 8108: 99 00 06    ...
    dey                                                               ; 810b: 88          .
    bne loop_c80f9                                                    ; 810c: d0 eb       ..
    jsr tube_post_init                                                ; 810e: 20 14 04     ..
    ldx #&60 ; '`'                                                    ; 8111: a2 60       .`
; Copy NMI workspace initialiser from ROM to $0016-$0076
; &8113 referenced 1 time by &8119
.loop_c8113
    lda c9307,x                                                       ; 8113: bd 07 93    ...
    sta nmi_workspace_start,x                                         ; 8116: 95 16       ..
    dex                                                               ; 8118: ca          .
    bpl loop_c8113                                                    ; 8119: 10 f8       ..
; &811b referenced 1 time by &80c6
.c811b
    ldy zp_temp_10                                                    ; 811b: a4 10       ..
    lda #0                                                            ; 811d: a9 00       ..
; &811f referenced 1 time by &80b1
.c811f
    cmp #&12                                                          ; 811f: c9 12       ..
    bne dispatch_service                                              ; 8121: d0 04       ..
    cpy #5                                                            ; 8123: c0 05       ..
    beq select_nfs                                                    ; 8125: f0 5d       .]
; Service call dispatcher
; Dispatches MOS service calls 0-12 via the shared dispatch table.
; Uses base offset Y=0, so table index = service number + 1.
; Service numbers >= 13 are ignored (branch to return_2).
; Called via JSR $809F rather than fall-through, so it returns
; to $813C to restore saved registers.
; &8127 referenced 1 time by &8121
.dispatch_service
    cmp #&0d                                                          ; 8127: c9 0d       ..
    bcs return_2                                                      ; 8129: b0 1a       ..
    tax                                                               ; 812b: aa          .
    lda fs_temp_ce                                                    ; 812c: a5 ce       ..
    pha                                                               ; 812e: 48          H
    lda fs_temp_cd                                                    ; 812f: a5 cd       ..
    pha                                                               ; 8131: 48          H
    stx fs_temp_ce                                                    ; 8132: 86 ce       ..
    sty fs_temp_cd                                                    ; 8134: 84 cd       ..
    tya                                                               ; 8136: 98          .
    ldy #0                                                            ; 8137: a0 00       ..             ; Y=0: base offset for service calls (index 1+)
    jsr dispatch                                                      ; 8139: 20 9f 80     ..            ; JSR to dispatcher (returns here after handler completes)
    ldx fs_temp_ce                                                    ; 813c: a6 ce       ..
    pla                                                               ; 813e: 68          h
    sta fs_temp_cd                                                    ; 813f: 85 cd       ..
    pla                                                               ; 8141: 68          h
    sta fs_temp_ce                                                    ; 8142: 85 ce       ..
    txa                                                               ; 8144: 8a          .
; &8145 referenced 2 times by &8129, &814a
.return_2
    rts                                                               ; 8145: 60          `

; Resume after remote operation / *ROFF handler (NROFF)
; Checks byte 4 of (net_rx_ptr): if non-zero, the keyboard was
; disabled during a remote operation (peek/poke/boot). Clears
; the flag, re-enables the keyboard via OSBYTE $C9, and sends
; function $0A to notify completion. Also handles *ROFF and the
; triple-plus escape sequence (+++), which resets system masks
; via OSBYTE $CE and returns control to the MOS, providing an
; escape route when a remote session becomes unresponsive.
; &8146 referenced 2 times by &817b, &8df2
.resume_after_remote
    ldy #4                                                            ; 8146: a0 04       ..
    lda (net_rx_ptr),y                                                ; 8148: b1 9c       ..
    beq return_2                                                      ; 814a: f0 f9       ..
    lda #0                                                            ; 814c: a9 00       ..
    tax                                                               ; 814e: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 814f: 91 9c       ..
    tay                                                               ; 8151: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 8152: a9 c9       ..
    jsr osbyte                                                        ; 8154: 20 f4 ff     ..            ; Enable keyboard (for Econet)
    lda #&0a                                                          ; 8157: a9 0a       ..
    jsr setup_tx_and_send                                             ; 8159: 20 4b 90     K.
; &815c referenced 1 time by &911b
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 815c: 86 9e       ..
    lda #&ce                                                          ; 815e: a9 ce       ..
; &8160 referenced 1 time by &816b
.loop_c8160
    ldx nfs_workspace                                                 ; 8160: a6 9e       ..
    ldy #&7f                                                          ; 8162: a0 7f       ..
    jsr osbyte                                                        ; 8164: 20 f4 ff     ..
    adc #1                                                            ; 8167: 69 01       i.
    cmp #&d0                                                          ; 8169: c9 d0       ..
    beq loop_c8160                                                    ; 816b: f0 f3       ..
    lda #0                                                            ; 816d: a9 00       ..
    sta nfs_workspace                                                 ; 816f: 85 9e       ..
    rts                                                               ; 8171: 60          `

; Service 4: unrecognised * command
; Matches the command text against ROM string table entries:
;   X=8: matches "ROFF" at $8010 (within copyright string) → *ROFF
;        (log off from fileserver) — jumps to resume_after_remote
;   X=1: matches "NET" at $8009 (ROM title) → *NET (select NFS)
;        — falls through to select_nfs
; If neither matches, returns with the service call unclaimed.
.svc_star_command
    ldx #8                                                            ; 8172: a2 08       ..
    jsr match_rom_string                                              ; 8174: 20 9b 81     ..
    bne c817d                                                         ; 8177: d0 04       ..
    sta fs_temp_ce                                                    ; 8179: 85 ce       ..
    beq resume_after_remote                                           ; 817b: f0 c9       ..             ; ALWAYS branch

; &817d referenced 1 time by &8177
.c817d
    ldx #1                                                            ; 817d: a2 01       ..
    jsr match_rom_string                                              ; 817f: 20 9b 81     ..
    bne c81c9                                                         ; 8182: d0 45       .E
; Select NFS as active filing system (INIT)
; Reached from service $12 (select FS) with Y=5, or when *NET command
; selects NFS. Notifies the current FS of shutdown via FSCV A=6 —
; this triggers the outgoing FS to save its context back to its
; workspace page, allowing restoration if re-selected later (the
; FSDIE handoff mechanism). Then sets up the standard OS vector
; indirections (FILEV through FSCV) to NFS entry points, claims the
; extended vector table entries, and issues service $0F (vectors
; claimed) to notify other ROMs. If fs_temp_cd is zero (auto-boot
; not inhibited), injects the synthetic command "I .BOOT" through
; the command decoder to trigger auto-boot login.
; &8184 referenced 1 time by &8125
.select_nfs
    jsr call_fscv_shutdown                                            ; 8184: 20 cc 81     ..
    sec                                                               ; 8187: 38          8
    ror fs_temp_cd                                                    ; 8188: 66 cd       f.
    jsr issue_vectors_claimed                                         ; 818a: 20 2e 82     ..
    ldy #&1d                                                          ; 818d: a0 1d       ..
; &818f referenced 1 time by &8197
.loop_c818f
    lda (net_rx_ptr),y                                                ; 818f: b1 9c       ..
    sta fs_state_deb,y                                                ; 8191: 99 eb 0d    ...
    dey                                                               ; 8194: 88          .
    cpy #&14                                                          ; 8195: c0 14       ..
    bne loop_c818f                                                    ; 8197: d0 f6       ..
    beq setup_fs_vectors                                              ; 8199: f0 7c       .|             ; ALWAYS branch

; Match command text against ROM string table
; Compares characters from (os_text_ptr)+Y against bytes starting
; at binary_version+X ($8008+X). Input is uppercased via AND $DF.
; Returns with Z=1 if the ROM string's NUL terminator was reached
; (match), or Z=0 if a mismatch was found. On match, Y points
; past the matched text; on return, skips trailing spaces.
; &819b referenced 2 times by &8174, &817f
.match_rom_string
    ldy fs_temp_cd                                                    ; 819b: a4 cd       ..
; &819d referenced 1 time by &81aa
.loop_c819d
    lda (os_text_ptr),y                                               ; 819d: b1 f2       ..
    and #&df                                                          ; 819f: 29 df       ).
    beq cmd_name_matched                                              ; 81a1: f0 09       ..
    cmp binary_version,x                                              ; 81a3: dd 08 80    ...
    bne cmd_name_matched                                              ; 81a6: d0 04       ..
    iny                                                               ; 81a8: c8          .
    inx                                                               ; 81a9: e8          .
    bne loop_c819d                                                    ; 81aa: d0 f1       ..
; &81ac referenced 2 times by &81a1, &81a6
.cmd_name_matched
    lda binary_version,x                                              ; 81ac: bd 08 80    ...
    beq skip_cmd_spaces                                               ; 81af: f0 02       ..
    rts                                                               ; 81b1: 60          `

; &81b2 referenced 1 time by &81b7
.loop_c81b2
    iny                                                               ; 81b2: c8          .
; &81b3 referenced 1 time by &81af
.skip_cmd_spaces
    lda (os_text_ptr),y                                               ; 81b3: b1 f2       ..
    cmp #&20 ; ' '                                                    ; 81b5: c9 20       .
    beq loop_c81b2                                                    ; 81b7: f0 f9       ..
    eor #&0d                                                          ; 81b9: 49 0d       I.
    rts                                                               ; 81bb: 60          `

; Service 9: *HELP
; Prints the ROM identification string using print_inline.
.svc_help
    jsr print_inline                                                  ; 81bc: 20 3b 85     ;.
    equs &0d, "NFS 3.34", &0d                                         ; 81bf: 0d 4e 46... .NF

; &81c9 referenced 2 times by &8182, &81de
.c81c9
    ldy fs_temp_cd                                                    ; 81c9: a4 cd       ..
    rts                                                               ; 81cb: 60          `

; Notify filing system of shutdown
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; &81cc referenced 2 times by &8184, &81d1
.call_fscv_shutdown
    lda #6                                                            ; 81cc: a9 06       ..
    jmp (fscv)                                                        ; 81ce: 6c 1e 02    l..

; Service 3: auto-boot
; Notifies current FS of shutdown via FSCV A=6. Scans keyboard
; (OSBYTE $7A): if no key is pressed, auto-boot proceeds; if the
; 'N' key is pressed (matrix address $55), the boot is declined
; and the key is forgotten via OSBYTE $78. Any other key also
; declines. Prints "Econet Station <n>" and checks the ADLC SR2
; for the network clock signal — prints "No Clock" if absent (no
; network communication possible without it). Then falls through
; to set up NFS vectors (selecting NFS as the filing system).
.svc_autoboot
    jsr call_fscv_shutdown                                            ; 81d1: 20 cc 81     ..
    lda #osbyte_scan_keyboard_from_16                                 ; 81d4: a9 7a       .z
    jsr osbyte                                                        ; 81d6: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 81d9: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi c81e6                                                         ; 81da: 30 0a       0.
    eor #&55 ; 'U'                                                    ; 81dc: 49 55       IU
    bne c81c9                                                         ; 81de: d0 e9       ..
    tay                                                               ; 81e0: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 81e1: a9 78       .x
    jsr osbyte                                                        ; 81e3: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; &81e6 referenced 1 time by &81da
.c81e6
    jsr print_inline                                                  ; 81e6: 20 3b 85     ;.
    equs "Econet Station "                                            ; 81e9: 45 63 6f... Eco

    lda tx_clear_flag                                                 ; 81f8: ad 62 0d    .b.
    jsr print_decimal                                                 ; 81fb: 20 af 85     ..
    lda #&20 ; ' '                                                    ; 81fe: a9 20       .
    bit econet_control23_or_status2                                   ; 8200: 2c a1 fe    ,..
    beq c8212                                                         ; 8203: f0 0d       ..
    jsr print_inline                                                  ; 8205: 20 3b 85     ;.
    equs " No Clock"                                                  ; 8208: 20 4e 6f...  No

    nop                                                               ; 8211: ea          .
; &8212 referenced 1 time by &8203
.c8212
    jsr print_inline                                                  ; 8212: 20 3b 85     ;.
    equs &0d, &0d                                                     ; 8215: 0d 0d       ..

; Set up filing system vectors
; Copies 14 bytes from fs_vector_addrs ($824D) into FILEV-FSCV ($0212).
; These set all 7 filing system vectors to the standard extended vector
; dispatch addresses ($FF1B, $FF1E, $FF21, $FF24, $FF27, $FF2A, $FF2D).
; Then calls setup_rom_ptrs_netv to install the extended vector table
; entries with the actual NFS handler addresses, and issues service
; requests to notify other ROMs.
; &8217 referenced 1 time by &8199
.setup_fs_vectors
    ldy #&0d                                                          ; 8217: a0 0d       ..             ; Copy 14 bytes: FS vector addresses → FILEV-FSCV
; &8219 referenced 1 time by &8220
.loop_c8219
    lda fs_vector_addrs,y                                             ; 8219: b9 4d 82    .M.
    sta filev,y                                                       ; 821c: 99 12 02    ...
    dey                                                               ; 821f: 88          .
    bpl loop_c8219                                                    ; 8220: 10 f7       ..
    jsr setup_rom_ptrs_netv                                           ; 8222: 20 d1 82     ..
    ldy #&1b                                                          ; 8225: a0 1b       ..
    ldx #7                                                            ; 8227: a2 07       ..
    jsr store_rom_ptr_pair                                            ; 8229: 20 e5 82     ..
    stx fs_temp_ce                                                    ; 822c: 86 ce       ..
; Issue 'vectors claimed' service and optionally auto-boot
; Issues service $0F (vectors claimed) via OSBYTE $8F, then
; service $0A. If fs_temp_cd is zero (auto-boot not inhibited),
; sets up the command string "I .BOOT" at $8245 and jumps to
; the FSCV 3 unrecognised-command handler (which matches against
; the command table at $8BD6). The "I." prefix triggers the
; catch-all entry which forwards the command to the fileserver.
; &822e referenced 1 time by &818a
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 822e: a9 8f       ..
    ldx #&0f                                                          ; 8230: a2 0f       ..
    jsr osbyte                                                        ; 8232: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 8235: a2 0a       ..
    jsr osbyte                                                        ; 8237: 20 f4 ff     ..
    ldx fs_temp_cd                                                    ; 823a: a6 cd       ..
    bne return_3                                                      ; 823c: d0 37       .7
    ldx #&45 ; 'E'                                                    ; 823e: a2 45       .E
; &8240 referenced 2 times by &82e5, &82eb
.c8240
    ldy #&82                                                          ; 8240: a0 82       ..
    jmp fscv_star_handler                                             ; 8242: 4c 92 8b    L..

    equs "I .BOOT"                                                    ; 8245: 49 20 2e... I .
    equb &0d                                                          ; 824c: 0d          .
; &824d referenced 1 time by &8219
.fs_vector_addrs
    equb &1b, &ff, &1e, &ff, &21, &ff, &24, &ff, &27, &ff, &2a, &ff   ; 824d: 1b ff 1e... ...
    equb &2d, &ff, &94, &86,   0, &e1, &88,   0, &85, &84,   0, &a2   ; 8259: 2d ff 94... -..
    equb &83,   0, &ea, &89,   0, &49, &89,   0, &8c, &80             ; 8265: 83 00 ea... ...

; Service 1: claim absolute workspace
; Claims pages up to $10 for NMI workspace ($0D), FS state ($0E),
; and FS command buffer ($0F). If Y >= $10, workspace already
; allocated — returns unchanged.
.svc_abs_workspace
    cpy #&10                                                          ; 826f: c0 10       ..
    bcs return_3                                                      ; 8271: b0 02       ..
    ldy #&10                                                          ; 8273: a0 10       ..
; &8275 referenced 2 times by &823c, &8271
.return_3
    rts                                                               ; 8275: 60          `

    equb 7, &90                                                       ; 8276: 07 90       ..

; Service 2: claim private workspace and initialise NFS
; Y = next available workspace page on entry.
; Sets up net_rx_ptr (Y) and nfs_workspace (Y+1) page pointers.
; On soft break (OSBYTE $FD returns 0): skips FS state init,
; preserving existing login state, file server selection, and
; control block configuration — this is why pressing BREAK
; keeps the user logged in.
; On power-up/CTRL-BREAK (result non-zero):
;   - Sets FS server station to $FE (FS, the default; no server)
;   - Sets printer server to $EB (PS, the default)
;   - Clears FS handles, OPT byte, message flag, SEQNOS
;   - Initialises all RXCBs with $3F flag (available)
; In both cases: reads station ID from $FE18 (only valid during
; reset), calls adlc_init, enables user-level RX (LFLAG=$40).
.svc_private_workspace
    sty net_rx_ptr_hi                                                 ; 8278: 84 9d       ..
    iny                                                               ; 827a: c8          .
    sty nfs_workspace_hi                                              ; 827b: 84 9f       ..
    lda #0                                                            ; 827d: a9 00       ..
    ldy #4                                                            ; 827f: a0 04       ..
    sta (net_rx_ptr),y                                                ; 8281: 91 9c       ..
    ldy #&ff                                                          ; 8283: a0 ff       ..
    sta net_rx_ptr                                                    ; 8285: 85 9c       ..
    sta nfs_workspace                                                 ; 8287: 85 9e       ..
    sta fs_temp_cd                                                    ; 8289: 85 cd       ..
    sta tx_ctrl_status                                                ; 828b: 8d 3a 0d    .:.
    tax                                                               ; 828e: aa          .              ; X=&00
    lda #osbyte_read_write_last_break_type                            ; 828f: a9 fd       ..             ; OSBYTE $FD: read type of last reset
    jsr osbyte                                                        ; 8291: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 8294: 8a          .              ; X=value of type of last reset
    beq c82c3                                                         ; 8295: f0 2c       .,             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 8297: a0 15       ..
    lda #&fe                                                          ; 8299: a9 fe       ..
    sta fs_server_stn                                                 ; 829b: 8d 00 0e    ...            ; Station $FE = no server selected
    sta (net_rx_ptr),y                                                ; 829e: 91 9c       ..
    ldy #2                                                            ; 82a0: a0 02       ..
    lda #&eb                                                          ; 82a2: a9 eb       ..
    sta (nfs_workspace),y                                             ; 82a4: 91 9e       ..
    iny                                                               ; 82a6: c8          .              ; Y=&03
    lda #0                                                            ; 82a7: a9 00       ..
    sta fs_server_net                                                 ; 82a9: 8d 01 0e    ...
    sta (nfs_workspace),y                                             ; 82ac: 91 9e       ..
    sta prot_status                                                   ; 82ae: 8d 63 0d    .c.
    sta fs_messages_flag                                              ; 82b1: 8d 06 0e    ...
; &82b4 referenced 1 time by &82c1
.loop_c82b4
    lda fs_temp_cd                                                    ; 82b4: a5 cd       ..
    jsr calc_handle_offset                                            ; 82b6: 20 b7 8d     ..
    bcs c82c3                                                         ; 82b9: b0 08       ..
    lda #&3f ; '?'                                                    ; 82bb: a9 3f       .?
    sta (nfs_workspace),y                                             ; 82bd: 91 9e       ..
    inc fs_temp_cd                                                    ; 82bf: e6 cd       ..
    bne loop_c82b4                                                    ; 82c1: d0 f1       ..
; &82c3 referenced 2 times by &8295, &82b9
.c82c3
    lda station_id_disable_net_nmis                                   ; 82c3: ad 18 fe    ...            ; Read station ID (also INTOFF)
    sta tx_clear_flag                                                 ; 82c6: 8d 62 0d    .b.
    jsr trampoline_adlc_init                                          ; 82c9: 20 63 96     c.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 82cc: a9 40       .@
    sta rx_status_flags                                               ; 82ce: 8d 38 0d    .8.
; Set up ROM pointer table and NETV
; Reads the ROM pointer table base address via OSBYTE $A8, stores
; it in osrdsc_ptr ($F6). Sets NETV low byte to $36. Then copies
; one 3-byte extended vector entry (addr=$9007, rom=current) into
; the ROM pointer table at offset $36, installing osword_dispatch
; as the NETV handler.
; &82d1 referenced 1 time by &8222
.setup_rom_ptrs_netv
    lda #osbyte_read_rom_ptr_table_low                                ; 82d1: a9 a8       ..
    ldx #0                                                            ; 82d3: a2 00       ..
    ldy #&ff                                                          ; 82d5: a0 ff       ..
    jsr osbyte                                                        ; 82d7: 20 f4 ff     ..            ; Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 82da: 86 f6       ..             ; X=value of address of ROM pointer table (low byte)
    sty l00f7                                                         ; 82dc: 84 f7       ..             ; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 82de: a0 36       .6
    sty netv                                                          ; 82e0: 8c 24 02    .$.
    ldx #1                                                            ; 82e3: a2 01       ..
; &82e5 referenced 2 times by &8229, &82f7
.store_rom_ptr_pair
    lda c8240,y                                                       ; 82e5: b9 40 82    .@.
    sta (osrdsc_ptr),y                                                ; 82e8: 91 f6       ..
    iny                                                               ; 82ea: c8          .
    lda c8240,y                                                       ; 82eb: b9 40 82    .@.
    sta (osrdsc_ptr),y                                                ; 82ee: 91 f6       ..
    iny                                                               ; 82f0: c8          .
    lda romsel_copy                                                   ; 82f1: a5 f4       ..
    sta (osrdsc_ptr),y                                                ; 82f3: 91 f6       ..
    iny                                                               ; 82f5: c8          .
    dex                                                               ; 82f6: ca          .
    bne store_rom_ptr_pair                                            ; 82f7: d0 ec       ..
    ldy nfs_workspace_hi                                              ; 82f9: a4 9f       ..
    iny                                                               ; 82fb: c8          .
    rts                                                               ; 82fc: 60          `

; FSCV 6: Filing system shutdown / save state (FSDIE)
; Called when another filing system (e.g. DFS) is selected. Saves
; the current NFS context (FSLOCN station number, URD/CSD/LIB
; handles, OPT byte, etc.) from page $0E into the dynamic workspace
; backup area. This allows the state to be restored when *NET is
; re-issued later, without losing the login session. Finally calls
; OSBYTE $77 (FXSPEX: close SPOOL and EXEC files) to avoid leaving
; dangling file handles across the FS switch.
.fscv_shutdown
    ldy #&1d                                                          ; 82fd: a0 1d       ..
; &82ff referenced 1 time by &8307
.loop_c82ff
    lda fs_state_deb,y                                                ; 82ff: b9 eb 0d    ...
    sta (net_rx_ptr),y                                                ; 8302: 91 9c       ..
    dey                                                               ; 8304: 88          .
    cpy #&14                                                          ; 8305: c0 14       ..
    bne loop_c82ff                                                    ; 8307: d0 f6       ..
    lda #osbyte_printer_driver_going_dormant                          ; 8309: a9 7b       .{
    jmp osbyte                                                        ; 830b: 4c f4 ff    L..            ; Printer driver going dormant

; &830e referenced 1 time by &8381
.init_tx_ctrl_data
    lda #&90                                                          ; 830e: a9 90       ..
; &8310 referenced 2 times by &880e, &8f78
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 8310: 20 1c 83     ..
    sta l00c1                                                         ; 8313: 85 c1       ..
    lda #3                                                            ; 8315: a9 03       ..
    sta l00c4                                                         ; 8317: 85 c4       ..
    dec l00c0                                                         ; 8319: c6 c0       ..
    rts                                                               ; 831b: 60          `

; Initialise TX control block at $00C0 from template
; Copies 12 bytes from tx_ctrl_template ($8334) to $00C0.
; For the first 2 bytes (Y=0,1), also copies the fileserver
; station/network from $0E00/$0E01 to $00C2/$00C3.
; The template sets up: control=$80, port=$99 (FS command port),
; command data length=$0F, plus padding bytes.
; &831c referenced 3 times by &8310, &8370, &83b9
.init_tx_ctrl_block
    pha                                                               ; 831c: 48          H
    ldy #&0b                                                          ; 831d: a0 0b       ..
; &831f referenced 1 time by &8330
.loop_c831f
    lda tx_ctrl_template,y                                            ; 831f: b9 34 83    .4.
    sta l00c0,y                                                       ; 8322: 99 c0 00    ...
    cpy #2                                                            ; 8325: c0 02       ..
    bpl c832f                                                         ; 8327: 10 06       ..
    lda fs_server_stn,y                                               ; 8329: b9 00 0e    ...
    sta l00c2,y                                                       ; 832c: 99 c2 00    ...
; &832f referenced 1 time by &8327
.c832f
    dey                                                               ; 832f: 88          .
    bpl loop_c831f                                                    ; 8330: 10 ed       ..
    pla                                                               ; 8332: 68          h
    rts                                                               ; 8333: 60          `

; TX control block template (TXTAB, 12 bytes)
; $00C0: $80 (control flag)    $00C1: $99 (port — FS command port)
; $00C2: server station        $00C3: server network
; $00C4: $00 (data low)        $00C5: $0F (data high — buffer page)
; $00C6-$00CB: $FF (FILLER)
; The $FF padding in the address fields is a recurring pattern:
; Econet control blocks use 4-byte addresses but NFS only needs
; 2-byte addresses, so the upper two bytes are filled with $FF.
; &8334 referenced 1 time by &831f
.tx_ctrl_template
    equb &80, &99, 0, 0, 0, &0f                                       ; 8334: 80 99 00... ...
; &833a referenced 3 times by &888f, &8969, &915d
.l833a
    equb &ff, &ff, &ff, &0f, &ff, &ff                                 ; 833a: ff ff ff... ...

; &8340 referenced 1 time by &8a3b
.prepare_cmd_with_flag
    pha                                                               ; 8340: 48          H
    lda #&2a ; '*'                                                    ; 8341: a9 2a       .*
    sec                                                               ; 8343: 38          8
    bcs c835a                                                         ; 8344: b0 14       ..             ; ALWAYS branch

; &8346 referenced 2 times by &86d7, &8780
.prepare_cmd_clv
    clv                                                               ; 8346: b8          .
    bvc c8359                                                         ; 8347: 50 10       P.             ; ALWAYS branch

; *BYE handler (logoff)
; Closes any open *SPOOL and *EXEC files via OSBYTE $77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=$17 (FCBYE: logoff code).
; Dispatched from the command match table at $8BD6 for "BYE".
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 8349: a9 77       .w
    jsr osbyte                                                        ; 834b: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #&17                                                          ; 834e: a0 17       ..             ; Y=function code for HDRFN
; ***************************************************************************************
; Prepare FS command buffer (12 references)
; 
; Builds the 5-byte FS protocol header at $0F00:
;   $0F00 HDRREP = reply port (set downstream, typically $90/PREPLY)
;   $0F01 HDRFN  = Y parameter (function code)
;   $0F02 HDRURD = URD handle (from $0E02)
;   $0F03 HDRCSD = CSD handle (from $0E03)
;   $0F04 HDRLIB = LIB handle (from $0E04)
; Command-specific data follows at $0F05 (TXBUF). Also clears V flag.
; Called before building specific FS commands for transmission.
; 
; On Entry:
;     Y: function code for HDRFN
;     X: preserved through header build
; 
; On Exit:
;     A: 0 on success (from build_send_fs_cmd)
;     X: 0 on success, $D6 on not-found
;     Y: 1 (offset past command code in reply)
; ***************************************************************************************
; &8350 referenced 12 times by &807d, &8834, &88aa, &88fc, &8923, &8996, &89c0, &8a9a, &8b50, &8c18, &8c4f, &8cc8
.prepare_fs_cmd
    clv                                                               ; 8350: b8          .
; &8351 referenced 2 times by &8892, &896c
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 8351: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 8354: 8d 02 0f    ...
    lda #&2a ; '*'                                                    ; 8357: a9 2a       .*
; &8359 referenced 1 time by &8347
.c8359
    clc                                                               ; 8359: 18          .
; &835a referenced 1 time by &8344
.c835a
    sty fs_cmd_y_param                                                ; 835a: 8c 01 0f    ...
    sta fs_error_ptr                                                  ; 835d: 85 b8       ..
    ldy #1                                                            ; 835f: a0 01       ..
; &8361 referenced 1 time by &8368
.loop_c8361
    lda fs_csd_handle,y                                               ; 8361: b9 03 0e    ...            ; A=timeout period for FS reply
    sta fs_cmd_csd,y                                                  ; 8364: 99 03 0f    ...
    dey                                                               ; 8367: 88          .              ; Y=function code
    bpl loop_c8361                                                    ; 8368: 10 f7       ..
; ***************************************************************************************
; Build and send FS command (DOFSOP)
; 
; Sets reply port to $90 (PREPLY) at $0F00, initialises the TX
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
; command code to read the return code. Error $D6 ("not found")
; is detected via ADC #($100-$D6) with C=0 -- if the return code
; was exactly $D6, the result wraps to zero (Z=1). This is a
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
;     X: 0 on success, $D6 on not-found
;     Y: 1 (offset past command code in reply)
; ***************************************************************************************
; &836a referenced 1 time by &8af3
.build_send_fs_cmd
    php                                                               ; 836a: 08          .
    lda #&90                                                          ; 836b: a9 90       ..
    sta fs_cmd_type                                                   ; 836d: 8d 00 0f    ...
    jsr init_tx_ctrl_block                                            ; 8370: 20 1c 83     ..
    txa                                                               ; 8373: 8a          .
    adc #5                                                            ; 8374: 69 05       i.
    sta l00c8                                                         ; 8376: 85 c8       ..
    plp                                                               ; 8378: 28          (
    bcs c8397                                                         ; 8379: b0 1c       ..
    php                                                               ; 837b: 08          .
    jsr setup_tx_ptr_c0                                               ; 837c: 20 44 86     D.
    plp                                                               ; 837f: 28          (
; &8380 referenced 2 times by &8790, &8a77
.send_fs_reply_cmd
    php                                                               ; 8380: 08          .
    jsr init_tx_ctrl_data                                             ; 8381: 20 0e 83     ..
    lda fs_error_ptr                                                  ; 8384: a5 b8       ..
    jsr send_to_fs                                                    ; 8386: 20 4a 84     J.
    plp                                                               ; 8389: 28          (
; &838a referenced 1 time by &83a0
.loop_c838a
    iny                                                               ; 838a: c8          .
    lda (l00c4),y                                                     ; 838b: b1 c4       ..
    tax                                                               ; 838d: aa          .
    beq return_1                                                      ; 838e: f0 06       ..
    bvc c8394                                                         ; 8390: 50 02       P.
    adc #&2a ; '*'                                                    ; 8392: 69 2a       i*
; &8394 referenced 1 time by &8390
.c8394
    bne store_fs_error                                                ; 8394: d0 6c       .l
; &8396 referenced 1 time by &838e
.return_1
    rts                                                               ; 8396: 60          `

; &8397 referenced 1 time by &8379
.c8397
    pla                                                               ; 8397: 68          h
    ldx #&c0                                                          ; 8398: a2 c0       ..
    iny                                                               ; 839a: c8          .
    jsr econet_tx_retry                                               ; 839b: 20 48 92     H.
    sta l00b3                                                         ; 839e: 85 b3       ..
    bcc loop_c838a                                                    ; 83a0: 90 e8       ..
.bputv_handler
    clc                                                               ; 83a2: 18          .
; ***************************************************************************************
; Handle BPUT/BGET file byte I/O
; 
; BPUTV enters at $83A2 (CLC; fall through) and BGETV enters
; at $8485 (SEC; JSR here). The carry flag is preserved via
; PHP/PLP through the call chain and tested later (BCS) to
; select byte-stream transmission (BSXMIT) vs normal FS
; transmission (FSXMIT) -- a control-flow encoding using
; processor flags to avoid an extra flag variable.
; 
; BSXMIT uses handle=0 for print stream transactions (which
; sidestep the SEQNOS sequence number manipulation) and non-zero
; handles for file operations. After transmission, the high
; pointer bytes of the CB are reset to $FF -- "The BGET/PUT byte
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
; &83a3 referenced 1 time by &8486
.handle_bput_bget
    pha                                                               ; 83a3: 48          H
    sta l0fdf                                                         ; 83a4: 8d df 0f    ...
    txa                                                               ; 83a7: 8a          .
    pha                                                               ; 83a8: 48          H
    tya                                                               ; 83a9: 98          .
    pha                                                               ; 83aa: 48          H
    php                                                               ; 83ab: 08          .
    jsr handle_to_mask_clc                                            ; 83ac: 20 89 85     ..
    sty l0fde                                                         ; 83af: 8c de 0f    ...
    sty l00cf                                                         ; 83b2: 84 cf       ..
    ldy #&90                                                          ; 83b4: a0 90       ..
    sty fs_putb_buf                                                   ; 83b6: 8c dc 0f    ...
    jsr init_tx_ctrl_block                                            ; 83b9: 20 1c 83     ..
    lda #&dc                                                          ; 83bc: a9 dc       ..
    sta l00c4                                                         ; 83be: 85 c4       ..
    lda #&e0                                                          ; 83c0: a9 e0       ..
    sta l00c8                                                         ; 83c2: 85 c8       ..
    iny                                                               ; 83c4: c8          .
    ldx #9                                                            ; 83c5: a2 09       ..
    plp                                                               ; 83c7: 28          (
    bcc store_retry_count                                             ; 83c8: 90 01       ..
    dex                                                               ; 83ca: ca          .              ; X=&08
; &83cb referenced 1 time by &83c8
.store_retry_count
    stx fs_getb_buf                                                   ; 83cb: 8e dd 0f    ...
    lda l0fde                                                         ; 83ce: ad de 0f    ...
    ldx #&c0                                                          ; 83d1: a2 c0       ..
    jsr econet_tx_retry                                               ; 83d3: 20 48 92     H.
    ldx fs_getb_buf                                                   ; 83d6: ae dd 0f    ...
    beq update_sequence_return                                        ; 83d9: f0 40       .@
    ldy #&1f                                                          ; 83db: a0 1f       ..
; &83dd referenced 1 time by &83e4
.loop_c83dd
    lda fs_putb_buf,y                                                 ; 83dd: b9 dc 0f    ...
    sta l0fe0,y                                                       ; 83e0: 99 e0 0f    ...
    dey                                                               ; 83e3: 88          .
    bpl loop_c83dd                                                    ; 83e4: 10 f7       ..
    tax                                                               ; 83e6: aa          .              ; X=File handle
    lda #osbyte_read_write_spool_file_handle                          ; 83e7: a9 c7       ..
    jsr osbyte                                                        ; 83e9: 20 f4 ff     ..            ; Read/Write *SPOOL file handle
    txa                                                               ; 83ec: 8a          .              ; X=value of *SPOOL file handle
    jsr handle_to_mask_a                                              ; 83ed: 20 88 85     ..
    cpy l00cf                                                         ; 83f0: c4 cf       ..
    bne c83fb                                                         ; 83f2: d0 07       ..
    ldx #<(l8444)                                                     ; 83f4: a2 44       .D
    ldy #>(l8444)                                                     ; 83f6: a0 84       ..
    jsr oscli                                                         ; 83f8: 20 f7 ff     ..
; &83fb referenced 1 time by &83f2
.c83fb
    lda #&e0                                                          ; 83fb: a9 e0       ..
    sta l00c4                                                         ; 83fd: 85 c4       ..
    ldx fs_getb_buf                                                   ; 83ff: ae dd 0f    ...
; Handle fileserver error replies (FSERR)
; The fileserver returns errors as: zero command code + error number +
; CR-terminated message string. This routine converts the reply buffer
; in-place to a standard MOS BRK error packet by:
;   1. Storing the error code at fs_last_error ($0E09)
;   2. Normalizing error codes below $A8 to $A8 (the standard FS error
;      number), since the MOS error space below $A8 has other meanings
;   3. Scanning for the CR terminator and replacing it with $00
;   4. JMPing indirect through (l00c4) to execute the buffer as a BRK
;      instruction — the zero command code serves as the BRK opcode
; N.B. This relies on the fileserver always returning a zero command
; code in position 0 of the reply buffer.
; &8402 referenced 1 time by &8394
.store_fs_error
    stx fs_last_error                                                 ; 8402: 8e 09 0e    ...
    ldy #1                                                            ; 8405: a0 01       ..
    cpx #&a8                                                          ; 8407: e0 a8       ..
    bcs c840f                                                         ; 8409: b0 04       ..
    lda #&a8                                                          ; 840b: a9 a8       ..
    sta (l00c4),y                                                     ; 840d: 91 c4       ..
; &840f referenced 2 times by &8409, &8414
.c840f
    iny                                                               ; 840f: c8          .
    lda #&0d                                                          ; 8410: a9 0d       ..
    eor (l00c4),y                                                     ; 8412: 51 c4       Q.
    bne c840f                                                         ; 8414: d0 f9       ..
    sta (l00c4),y                                                     ; 8416: 91 c4       ..
    jmp (l00c4)                                                       ; 8418: 6c c4 00    l..

; &841b referenced 1 time by &83d9
.update_sequence_return
    sta fs_sequence_nos                                               ; 841b: 8d 08 0e    ...
    pla                                                               ; 841e: 68          h
    tay                                                               ; 841f: a8          .
    pla                                                               ; 8420: 68          h
    tax                                                               ; 8421: aa          .
    pla                                                               ; 8422: 68          h
    rts                                                               ; 8423: 60          `

; &8424 referenced 1 time by &8477
.c8424
    lda #8                                                            ; 8424: a9 08       ..
    bne set_listen_offset                                             ; 8426: d0 04       ..             ; ALWAYS branch

; &8428 referenced 1 time by &868d
.c8428
    lda (net_tx_ptr,x)                                                ; 8428: a1 9a       ..
; &842a referenced 2 times by &8483, &89b8
.c842a
    and #7                                                            ; 842a: 29 07       ).
; &842c referenced 1 time by &8426
.set_listen_offset
    tax                                                               ; 842c: aa          .
    ldy l8014,x                                                       ; 842d: bc 14 80    ...
    ldx #0                                                            ; 8430: a2 00       ..
    stx l0100                                                         ; 8432: 8e 00 01    ...
; &8435 referenced 1 time by &843f
.loop_c8435
    lda error_msg_table,y                                             ; 8435: b9 af 84    ...
    sta l0101,x                                                       ; 8438: 9d 01 01    ...
    beq c8441                                                         ; 843b: f0 04       ..
    inx                                                               ; 843d: e8          .
    iny                                                               ; 843e: c8          .
    bne loop_c8435                                                    ; 843f: d0 f4       ..
; &8441 referenced 1 time by &843b
.c8441
    jmp l0100                                                         ; 8441: 4c 00 01    L..

.l8444
    equs "SP."                                                        ; 8444: 53 50 2e    SP.
    equb &0d                                                          ; 8447: 0d          .

; &8448 referenced 3 times by &8730, &8fbb, &927d
.send_to_fs_star
    lda #&2a ; '*'                                                    ; 8448: a9 2a       .*
; Send command to fileserver and handle reply (WAITFS)
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
; &844a referenced 2 times by &8386, &881a
.send_to_fs
    pha                                                               ; 844a: 48          H
    lda rx_status_flags                                               ; 844b: ad 38 0d    .8.
    pha                                                               ; 844e: 48          H
    ora #&80                                                          ; 844f: 09 80       ..
    sta rx_status_flags                                               ; 8451: 8d 38 0d    .8.
    lda #0                                                            ; 8454: a9 00       ..
    pha                                                               ; 8456: 48          H
    pha                                                               ; 8457: 48          H
    tay                                                               ; 8458: a8          .              ; Y=&00
    tsx                                                               ; 8459: ba          .
; &845a referenced 3 times by &8464, &8469, &846e
.c845a
    lda (net_tx_ptr),y                                                ; 845a: b1 9a       ..
    bmi fs_wait_cleanup                                               ; 845c: 30 12       0.
    jsr check_escape                                                  ; 845e: 20 7a 84     z.
    dec l0101,x                                                       ; 8461: de 01 01    ...
    bne c845a                                                         ; 8464: d0 f4       ..
    dec l0102,x                                                       ; 8466: de 02 01    ...
    bne c845a                                                         ; 8469: d0 ef       ..
    dec l0104,x                                                       ; 846b: de 04 01    ...
    bne c845a                                                         ; 846e: d0 ea       ..
; &8470 referenced 1 time by &845c
.fs_wait_cleanup
    pla                                                               ; 8470: 68          h
    pla                                                               ; 8471: 68          h
    pla                                                               ; 8472: 68          h
    sta rx_status_flags                                               ; 8473: 8d 38 0d    .8.
    pla                                                               ; 8476: 68          h
    beq c8424                                                         ; 8477: f0 ab       ..
    rts                                                               ; 8479: 60          `

; Check and handle escape condition (ESC)
; Two-level escape gating: the MOS escape flag ($FF bit 7) is ANDed
; with the software enable flag ESCAP. Both must have bit 7 set for
; escape to fire. ESCAP is set non-zero during data port operations
; (LOADOP stores the data port $90, serving double duty as both the
; port number and the escape-enable flag). ESCAP is disabled via LSR
; in the ENTER routine, which clears bit 7 — PHP/PLP around the LSR
; preserves the carry flag since ENTER is called from contexts where
; carry has semantic meaning (e.g., PUTBYT vs BGET distinction).
; This architecture allows escape between retransmission attempts
; but prevents interruption during critical FS transactions. If
; escape fires: acknowledges via OSBYTE $7E, then checks whether
; the failing handle is the current SPOOL or EXEC handle (OSBYTE
; $C6/$C7); if so, issues "*SP." or "*E." via OSCLI to gracefully
; close the channel before raising the error — preventing the system
; from continuing to spool output to a broken file handle.
; &847a referenced 2 times by &845e, &8674
.check_escape
    lda #osbyte_acknowledge_escape                                    ; 847a: a9 7e       .~
    bit l00ff                                                         ; 847c: 24 ff       $.
    bpl return_2                                                      ; 847e: 10 23       .#
    jsr osbyte                                                        ; 8480: 20 f4 ff     ..            ; Clear escape condition and perform escape effects
    bne c842a                                                         ; 8483: d0 a5       ..
.bgetv_handler
    sec                                                               ; 8485: 38          8
    jsr handle_bput_bget                                              ; 8486: 20 a3 83     ..            ; Handle BPUT/BGET file byte I/O
    sec                                                               ; 8489: 38          8
    lda #&fe                                                          ; 848a: a9 fe       ..
    bit l0fdf                                                         ; 848c: 2c df 0f    ,..
    bvs return_2                                                      ; 848f: 70 12       p.
    clc                                                               ; 8491: 18          .
    bmi c849b                                                         ; 8492: 30 07       0.
    lda l00cf                                                         ; 8494: a5 cf       ..
    jsr clear_fs_flag                                                 ; 8496: 20 df 85     ..
    bcc c84a0                                                         ; 8499: 90 05       ..
; &849b referenced 1 time by &8492
.c849b
    lda l00cf                                                         ; 849b: a5 cf       ..
    jsr set_fs_flag                                                   ; 849d: 20 e4 85     ..
; &84a0 referenced 1 time by &8499
.c84a0
    lda l0fde                                                         ; 84a0: ad de 0f    ...
; &84a3 referenced 2 times by &847e, &848f
.return_2
    rts                                                               ; 84a3: 60          `

; &84a4 referenced 1 time by &8760
.add_5_to_y
    iny                                                               ; 84a4: c8          .
; &84a5 referenced 1 time by &8a4d
.add_4_to_y
    iny                                                               ; 84a5: c8          .
    iny                                                               ; 84a6: c8          .
    iny                                                               ; 84a7: c8          .
    iny                                                               ; 84a8: c8          .
    rts                                                               ; 84a9: 60          `

; &84aa referenced 1 time by &874f
.sub_4_from_y
    dey                                                               ; 84aa: 88          .
; &84ab referenced 2 times by &885c, &8a55
.sub_3_from_y
    dey                                                               ; 84ab: 88          .
    dey                                                               ; 84ac: 88          .
    dey                                                               ; 84ad: 88          .
    rts                                                               ; 84ae: 60          `

; Econet error message table (ERRTAB, 8 entries)
; Each entry: error number byte followed by NUL-terminated string.
;   $A0: "Line Jammed"     $A1: "Net Error"
;   $A2: "Not listening"   $A3: "No Clock"
;   $A4: "Bad Txcb"        $11: "Escape"
;   $CB: "Bad Option"      $A5: "No reply"
; Indexed by the low 3 bits of the TXCB flag byte (AND #$07),
; which encode the specific Econet failure reason. The NREPLY
; and NLISTN routines build a MOS BRK error block at $100 on the
; stack page: NREPLY fires when the fileserver does not respond
; within the timeout period; NLISTN fires when the destination
; station actively refused the connection.
; Indexed via the error dispatch at c8424/c842c.
; &84af referenced 1 time by &8435
.error_msg_table
    equb &a0                                                          ; 84af: a0          .
    equs "Line Jammed"                                                ; 84b0: 4c 69 6e... Lin
    equb 0, &a1                                                       ; 84bb: 00 a1       ..
    equs "Net Error"                                                  ; 84bd: 4e 65 74... Net
    equb 0, &a2                                                       ; 84c6: 00 a2       ..
    equs "Not listening"                                              ; 84c8: 4e 6f 74... Not
    equb 0, &a3                                                       ; 84d5: 00 a3       ..
    equs "No Clock"                                                   ; 84d7: 4e 6f 20... No
    equb 0, &a4                                                       ; 84df: 00 a4       ..
    equs "Bad Txcb"                                                   ; 84e1: 42 61 64... Bad
    equb 0, &11                                                       ; 84e9: 00 11       ..
    equs "Escape"                                                     ; 84eb: 45 73 63... Esc
    equb 0, &cb                                                       ; 84f1: 00 cb       ..
    equs "Bad Option"                                                 ; 84f3: 42 61 64... Bad
    equb 0, &a5                                                       ; 84fd: 00 a5       ..
    equs "No reply"                                                   ; 84ff: 4e 6f 20... No
    equb 0                                                            ; 8507: 00          .

; Save FSCV/vector arguments
; Stores A, X, Y into the filing system workspace. Called at the
; start of every FS vector handler (FILEV, ARGSV, BGETV, BPUTV,
; GBPBV, FINDV, FSCV). NFS repurposes CFS/RFS workspace locations:
;   $BD (fs_last_byte_flag) = A (function code / command)
;   $BB (fs_options)        = X (control block ptr low)
;   $BC (fs_block_offset)   = Y (control block ptr high)
;   $BE/$BF (fs_crc_lo/hi)  = X/Y (duplicate for indexed access)
; &8508 referenced 6 times by &808c, &8694, &88e1, &8949, &89ea, &8b92
.save_fscv_args
    sta fs_last_byte_flag                                             ; 8508: 85 bd       ..
    stx fs_options                                                    ; 850a: 86 bb       ..
    sty fs_block_offset                                               ; 850c: 84 bc       ..
    stx fs_crc_lo                                                     ; 850e: 86 be       ..
    sty fs_crc_hi                                                     ; 8510: 84 bf       ..
    rts                                                               ; 8512: 60          `

; Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)
; Reads attribute byte at offset $0E from the parameter block,
; masks to 6 bits, then falls through to the shared bitmask
; builder. Converts fileserver protection format (5-6 bits) to
; BBC OSFILE attribute format (8 bits) via the lookup table at
; $8530. The two formats use different bit layouts for file
; protection attributes.
; &8513 referenced 2 times by &886e, &8899
.decode_attribs_6bit
    ldy #&0e                                                          ; 8513: a0 0e       ..
    lda (fs_options),y                                                ; 8515: b1 bb       ..
    and #&3f ; '?'                                                    ; 8517: 29 3f       )?
    ldx #4                                                            ; 8519: a2 04       ..
    bne c8521                                                         ; 851b: d0 04       ..             ; ALWAYS branch

; Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)
; Masks A to 5 bits and builds an access bitmask via the
; lookup table at $8530. Each input bit position maps to a
; different output bit via the table. The conversion is done
; by iterating through the source bits and OR-ing in the
; corresponding destination bits from the table, translating
; between BBC (8-bit) and fileserver (5-bit) protection formats.
; &851d referenced 2 times by &879b, &88b6
.decode_attribs_5bit
    and #&1f                                                          ; 851d: 29 1f       ).
    ldx #&ff                                                          ; 851f: a2 ff       ..
; &8521 referenced 1 time by &851b
.c8521
    sta fs_error_ptr                                                  ; 8521: 85 b8       ..
    lda #0                                                            ; 8523: a9 00       ..
; &8525 referenced 1 time by &852d
.loop_c8525
    inx                                                               ; 8525: e8          .
    lsr fs_error_ptr                                                  ; 8526: 46 b8       F.
    bcc c852d                                                         ; 8528: 90 03       ..
    ora access_bit_table,x                                            ; 852a: 1d 30 85    .0.
; &852d referenced 1 time by &8528
.c852d
    bne loop_c8525                                                    ; 852d: d0 f6       ..
    rts                                                               ; 852f: 60          `

; &8530 referenced 1 time by &852a
.access_bit_table
    equb &50, &20, 5, 2, &88, 4, 8, &80, &10, 1, 2                    ; 8530: 50 20 05... P .

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
; &853b referenced 13 times by &81bc, &81e6, &8205, &8212, &8c20, &8c2a, &8c38, &8c43, &8c5d, &8c6e, &8c81, &8c95, &8ca2
.print_inline
    pla                                                               ; 853b: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 853c: 85 b0       ..
    pla                                                               ; 853e: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 853f: 85 b1       ..
    ldy #0                                                            ; 8541: a0 00       ..
; &8543 referenced 1 time by &8550
.loop_c8543
    inc fs_load_addr                                                  ; 8543: e6 b0       ..             ; Advance pointer past return address / to next char
    bne c8549                                                         ; 8545: d0 02       ..
    inc fs_load_addr_hi                                               ; 8547: e6 b1       ..
; &8549 referenced 1 time by &8545
.c8549
    lda (fs_load_addr),y                                              ; 8549: b1 b0       ..             ; Load next byte from inline string
    bmi c8552                                                         ; 854b: 30 05       0.             ; Bit 7 set? Done — this byte is the next opcode
    jsr osasci                                                        ; 854d: 20 e3 ff     ..            ; Write character
    bne loop_c8543                                                    ; 8550: d0 f1       ..
; &8552 referenced 1 time by &854b
.c8552
    jmp (fs_load_addr)                                                ; 8552: 6c b0 00    l..            ; Jump to address of high-bit byte (resumes code after string)

; Skip leading spaces in parameter block
; Advances Y past space characters in (fs_options),Y.
; Returns with the first non-space character in A.
; Sets carry if the character is >= 'A' (alphabetic).
; &8555 referenced 3 times by &855a, &8c0c, &8d06
.skip_spaces
    lda (fs_options),y                                                ; 8555: b1 bb       ..
    iny                                                               ; 8557: c8          .
    cmp #&20 ; ' '                                                    ; 8558: c9 20       .
    beq skip_spaces                                                   ; 855a: f0 f9       ..
    dey                                                               ; 855c: 88          .
    cmp #&41 ; 'A'                                                    ; 855d: c9 41       .A
    rts                                                               ; 855f: 60          `

; ***************************************************************************************
; Parse decimal number from (fs_options),Y (DECIN)
; 
; Reads ASCII digits and accumulates in $B2 (fs_load_addr_2).
; Multiplication by 10 uses the identity: n*10 = n*8 + n*2,
; computed as ASL $B2 (x2), then A = $B2*4 via two ASLs,
; then ADC $B2 gives x10.
; Terminates on "." (pathname separator), control chars, or space.
; The delimiter handling was revised to support dot-separated path
; components (e.g. "1.$.PROG") -- originally stopped on any char
; >= $40 (any letter), but the revision allows numbers followed
; by dots.
; 
; On Entry:
;     Y: offset into (fs_options) buffer
; 
; On Exit:
;     A: parsed value (accumulated in $B2)
;     X: corrupted
;     Y: offset past last digit parsed
; ***************************************************************************************
; &8560 referenced 2 times by &8d0d, &8d13
.parse_decimal
    tax                                                               ; 8560: aa          .
    lda #0                                                            ; 8561: a9 00       ..
    sta fs_load_addr_2                                                ; 8563: 85 b2       ..
; &8565 referenced 1 time by &8582
.loop_c8565
    lda (fs_options),y                                                ; 8565: b1 bb       ..
    cmp #&40 ; '@'                                                    ; 8567: c9 40       .@
    bcs c8584                                                         ; 8569: b0 19       ..
    cmp #&2e ; '.'                                                    ; 856b: c9 2e       ..
    beq c8585                                                         ; 856d: f0 16       ..
    bmi c8584                                                         ; 856f: 30 13       0.
    and #&0f                                                          ; 8571: 29 0f       ).
    sta l00b3                                                         ; 8573: 85 b3       ..
    asl fs_load_addr_2                                                ; 8575: 06 b2       ..
    lda fs_load_addr_2                                                ; 8577: a5 b2       ..
    asl a                                                             ; 8579: 0a          .
    asl a                                                             ; 857a: 0a          .
    adc fs_load_addr_2                                                ; 857b: 65 b2       e.
    adc l00b3                                                         ; 857d: 65 b3       e.
    sta fs_load_addr_2                                                ; 857f: 85 b2       ..
    iny                                                               ; 8581: c8          .
    bne loop_c8565                                                    ; 8582: d0 e1       ..
; &8584 referenced 2 times by &8569, &856f
.c8584
    clc                                                               ; 8584: 18          .
; &8585 referenced 1 time by &856d
.c8585
    lda fs_load_addr_2                                                ; 8585: a5 b2       ..
    rts                                                               ; 8587: 60          `

; &8588 referenced 3 times by &83ed, &8a05, &8ecc
.handle_to_mask_a
    tay                                                               ; 8588: a8          .
; &8589 referenced 3 times by &83ac, &8822, &88ec
.handle_to_mask_clc
    clc                                                               ; 8589: 18          .
; ***************************************************************************************
; Convert file handle to bitmask (Y2FS)
; 
; Converts fileserver handles to single-bit masks segregated inside
; the BBC. NFS handles occupy the $20-$27 range (base HAND=$20),
; which cannot collide with local filing system or cassette handles
; -- the MOS routes OSFIND/OSBGET/OSBPUT to the correct filing
; system based on the handle value alone. The power-of-two encoding
; allows the EOF hint byte to track up to 8 files simultaneously
; with one bit per file, and enables fast set operations (ORA to
; add, EOR to toggle, AND to test) without loops. Handle 0 passes
; through unchanged (means "no file"). The bit-shift conversion loop
; has a built-in validity check: if the handle is out of range, the
; repeated ASL shifts all bits out, leaving A=0, which is converted
; to Y=$FF as a sentinel -- bad handles fail gracefully rather than
; indexing into garbage.
; Three entry points: $858A (direct), $8589 (CLC first), $8588 (TAY first).
; 
; On Entry:
;     Y: handle number
;     C: 0: convert, 1 with Y=0: skip, 1 with Y!=0: convert
; 
; On Exit:
;     A: preserved
;     X: preserved
;     Y: bitmask (single bit set) or $FF if handle invalid
; ***************************************************************************************
; &858a referenced 1 time by &894d
.handle_to_mask
    pha                                                               ; 858a: 48          H
    txa                                                               ; 858b: 8a          .
    pha                                                               ; 858c: 48          H
    tya                                                               ; 858d: 98          .
    bcc c8592                                                         ; 858e: 90 02       ..
    beq c85a1                                                         ; 8590: f0 0f       ..
; &8592 referenced 1 time by &858e
.c8592
    sec                                                               ; 8592: 38          8
    sbc #&1f                                                          ; 8593: e9 1f       ..
    tax                                                               ; 8595: aa          .
    lda #1                                                            ; 8596: a9 01       ..
; &8598 referenced 1 time by &859a
.loop_c8598
    asl a                                                             ; 8598: 0a          .
    dex                                                               ; 8599: ca          .
    bne loop_c8598                                                    ; 859a: d0 fc       ..
    ror a                                                             ; 859c: 6a          j
    tay                                                               ; 859d: a8          .
    bne c85a1                                                         ; 859e: d0 01       ..
    dey                                                               ; 85a0: 88          .
; &85a1 referenced 2 times by &8590, &859e
.c85a1
    pla                                                               ; 85a1: 68          h
    tax                                                               ; 85a2: aa          .
    pla                                                               ; 85a3: 68          h
    rts                                                               ; 85a4: 60          `

; ***************************************************************************************
; Convert bitmask to handle number (FS2A)
; 
; Inverse of Y2FS. Converts from the power-of-two FS format
; back to a sequential handle number by counting right shifts
; until A=0. Adds $1E to convert the 1-based bit position to
; a handle number (handles start at $1F+1 = $20). Used when
; receiving handle values from the fileserver in reply packets.
; 
; On Entry:
;     A: single-bit bitmask
; 
; On Exit:
;     A: handle number ($20-$27)
;     X: corrupted
;     Y: preserved
; ***************************************************************************************
; &85a5 referenced 2 times by &8980, &8ee6
.mask_to_handle
    ldx #0                                                            ; 85a5: a2 00       ..
; &85a7 referenced 1 time by &85a9
.loop_c85a7
    inx                                                               ; 85a7: e8          .
    lsr a                                                             ; 85a8: 4a          J
    bne loop_c85a7                                                    ; 85a9: d0 fc       ..
    txa                                                               ; 85ab: 8a          .
    adc #&1e                                                          ; 85ac: 69 1e       i.
    rts                                                               ; 85ae: 60          `

; Print byte as 3-digit decimal number
; Prints A as a decimal number using repeated subtraction
; for each digit position (100, 10, 1). Leading zeros are
; printed (no suppression). Used to display station numbers.
; &85af referenced 2 times by &81fb, &8c27
.print_decimal
    tay                                                               ; 85af: a8          .
    lda #&64 ; 'd'                                                    ; 85b0: a9 64       .d
    jsr print_decimal_digit                                           ; 85b2: 20 bc 85     ..
    lda #&0a                                                          ; 85b5: a9 0a       ..
    jsr print_decimal_digit                                           ; 85b7: 20 bc 85     ..
    lda #1                                                            ; 85ba: a9 01       ..
; Print one decimal digit by repeated subtraction
; Divides Y by A using repeated subtraction. Prints the
; quotient as an ASCII digit ('0'-'9'). Returns with the
; remainder in Y. X starts at $2F ('0'-1) and increments
; once per subtraction, giving the ASCII digit directly.
; &85bc referenced 2 times by &85b2, &85b7
.print_decimal_digit
    sta fs_error_ptr                                                  ; 85bc: 85 b8       ..
    tya                                                               ; 85be: 98          .
    ldx #&2f ; '/'                                                    ; 85bf: a2 2f       ./
    sec                                                               ; 85c1: 38          8
; &85c2 referenced 1 time by &85c5
.loop_c85c2
    inx                                                               ; 85c2: e8          .
    sbc fs_error_ptr                                                  ; 85c3: e5 b8       ..
    bcs loop_c85c2                                                    ; 85c5: b0 fb       ..
    adc fs_error_ptr                                                  ; 85c7: 65 b8       e.
    tay                                                               ; 85c9: a8          .
    txa                                                               ; 85ca: 8a          .
; &85cb referenced 1 time by &85fe
.c85cb
    jmp osasci                                                        ; 85cb: 4c e3 ff    L..            ; Write character

; ***************************************************************************************
; Compare two 4-byte addresses
; 
; Compares bytes at $B0-$B3 against $B4-$B7 using EOR.
; Used by the OSFILE save handler to compare the current
; transfer address ($C8-$CB, copied to $B0) against the end
; address ($B4-$B7) during multi-block file data transfers.
; 
; On Exit:
;     A: corrupted (EOR result)
;     X: corrupted
;     Y: preserved
; ***************************************************************************************
; &85ce referenced 2 times by &8716, &87c9
.compare_addresses
    ldx #4                                                            ; 85ce: a2 04       ..
; &85d0 referenced 1 time by &85d7
.loop_c85d0
    lda l00af,x                                                       ; 85d0: b5 af       ..
    eor l00b3,x                                                       ; 85d2: 55 b3       U.
    bne return_3                                                      ; 85d4: d0 03       ..
    dex                                                               ; 85d6: ca          .
    bne loop_c85d0                                                    ; 85d7: d0 f7       ..
; &85d9 referenced 1 time by &85d4
.return_3
    rts                                                               ; 85d9: 60          `

.fscv_read_handles
    ldx #&20 ; ' '                                                    ; 85da: a2 20       .
    ldy #&27 ; '''                                                    ; 85dc: a0 27       .'
; &85de referenced 1 time by &8603
.return_4
    rts                                                               ; 85de: 60          `

; Clear bit(s) in FS flags ($0E07)
; Inverts A (EOR #$FF), then ANDs into fs_work_0e07 to clear
; the specified bits. Falls through to set_fs_flag to store.
; &85df referenced 3 times by &8496, &883d, &8a81
.clear_fs_flag
    eor #&ff                                                          ; 85df: 49 ff       I.
    and fs_eof_flags                                                  ; 85e1: 2d 07 0e    -..
; Set bit(s) in FS flags ($0E07)
; ORs A into fs_work_0e07 (EOF hint byte). Each bit represents
; one of up to 8 open file handles. When clear, the file is
; definitely NOT at EOF. When set, the fileserver must be queried
; to confirm EOF status. This negative-cache optimisation avoids
; expensive network round-trips for the common case. The hint is
; cleared when the file pointer is updated (since seeking away
; from EOF invalidates the hint) and set after BGET/OPEN/EOF
; operations that might have reached the end.
; &85e4 referenced 5 times by &849d, &8929, &8975, &899c, &8a84
.set_fs_flag
    ora fs_eof_flags                                                  ; 85e4: 0d 07 0e    ...
    sta fs_eof_flags                                                  ; 85e7: 8d 07 0e    ...
    rts                                                               ; 85ea: 60          `

; Print byte as two hex digits
; Prints the high nibble first (via 4× LSR), then the low
; nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
; and output via OSASCI.
; &85eb referenced 2 times by &8639, &8c6b
.print_hex
    pha                                                               ; 85eb: 48          H
    lsr a                                                             ; 85ec: 4a          J
    lsr a                                                             ; 85ed: 4a          J
    lsr a                                                             ; 85ee: 4a          J
    lsr a                                                             ; 85ef: 4a          J
    jsr print_hex_nibble                                              ; 85f0: 20 f6 85     ..
    pla                                                               ; 85f3: 68          h
    and #&0f                                                          ; 85f4: 29 0f       ).
; &85f6 referenced 1 time by &85f0
.print_hex_nibble
    ora #&30 ; '0'                                                    ; 85f6: 09 30       .0
    cmp #&3a ; ':'                                                    ; 85f8: c9 3a       .:
    bcc c85fe                                                         ; 85fa: 90 02       ..
    adc #6                                                            ; 85fc: 69 06       i.
; &85fe referenced 2 times by &85fa, &8642
.c85fe
    bne c85cb                                                         ; 85fe: d0 cb       ..
; Print file catalogue line
; Displays a formatted catalogue entry: filename (padded to 12
; chars with spaces), load address (4 hex bytes at offset 5-2),
; exec address (4 hex bytes at offset 9-6), and file length
; (3 hex bytes at offset $0C-$0A), followed by a newline.
; Data is read from (fs_crc_lo) for the filename and from
; (fs_options) for the numeric fields. Returns immediately
; if fs_work_0e06 is zero (no info available).
; &8600 referenced 2 times by &8703, &8783
.print_file_info
    ldy fs_messages_flag                                              ; 8600: ac 06 0e    ...
    beq return_4                                                      ; 8603: f0 d9       ..
    ldy #0                                                            ; 8605: a0 00       ..
; &8607 referenced 1 time by &8615
.loop_c8607
    lda (fs_crc_lo),y                                                 ; 8607: b1 be       ..
    cmp #&0d                                                          ; 8609: c9 0d       ..
    beq pad_filename_spaces                                           ; 860b: f0 0a       ..
    cmp #&20 ; ' '                                                    ; 860d: c9 20       .
    beq pad_filename_spaces                                           ; 860f: f0 06       ..
    jsr osasci                                                        ; 8611: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8614: c8          .
    bne loop_c8607                                                    ; 8615: d0 f0       ..
; &8617 referenced 3 times by &860b, &860f, &861d
.pad_filename_spaces
    jsr print_space                                                   ; 8617: 20 40 86     @.
    iny                                                               ; 861a: c8          .
    cpy #&0c                                                          ; 861b: c0 0c       ..
    bcc pad_filename_spaces                                           ; 861d: 90 f8       ..
    ldy #5                                                            ; 861f: a0 05       ..
    jsr print_hex_bytes                                               ; 8621: 20 35 86     5.
    jsr print_exec_and_len                                            ; 8624: 20 2a 86     *.
    jmp osnewl                                                        ; 8627: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &862a referenced 1 time by &8624
.print_exec_and_len
    ldy #9                                                            ; 862a: a0 09       ..
    jsr print_hex_bytes                                               ; 862c: 20 35 86     5.
    ldy #&0c                                                          ; 862f: a0 0c       ..
    ldx #3                                                            ; 8631: a2 03       ..
    bne c8637                                                         ; 8633: d0 02       ..             ; ALWAYS branch

; &8635 referenced 2 times by &8621, &862c
.print_hex_bytes
    ldx #4                                                            ; 8635: a2 04       ..
; &8637 referenced 2 times by &8633, &863e
.c8637
    lda (fs_options),y                                                ; 8637: b1 bb       ..
    jsr print_hex                                                     ; 8639: 20 eb 85     ..
    dey                                                               ; 863c: 88          .
    dex                                                               ; 863d: ca          .
    bne c8637                                                         ; 863e: d0 f7       ..
; &8640 referenced 2 times by &8617, &8d5c
.print_space
    lda #&20 ; ' '                                                    ; 8640: a9 20       .
    bne c85fe                                                         ; 8642: d0 ba       ..             ; ALWAYS branch

; Set up TX pointer to control block at $00C0
; Points net_tx_ptr to $00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; &8644 referenced 2 times by &837c, &8809
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 8644: a2 c0       ..
    stx net_tx_ptr                                                    ; 8646: 86 9a       ..
    ldx #0                                                            ; 8648: a2 00       ..
    stx net_tx_ptr_hi                                                 ; 864a: 86 9b       ..
; Transmit and poll for result (full retry)
; Sets A=$FF (retry count) and Y=$60 (timeout parameter).
; Falls through to tx_poll_core.
; &864c referenced 3 times by &9001, &905b, &925b
.tx_poll_ff
    lda #&ff                                                          ; 864c: a9 ff       ..
; &864e referenced 1 time by &8fa4
.tx_poll_timeout
    ldy #&60 ; '`'                                                    ; 864e: a0 60       .`             ; Y=timeout parameter ($60 = standard)
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
; Two entry points: setup_tx_ptr_c0 ($8644) always uses the
; standard TXCB; tx_poll_core ($8650) is general-purpose.
; 
; On Entry:
;     A: retry count ($FF = full retry)
;     Y: timeout parameter ($60 = standard)
; 
; On Exit:
;     A: entry A (retry count, restored from stack)
;     X: 0
;     Y: 0
; ***************************************************************************************
; &8650 referenced 1 time by &8fe6
.tx_poll_core
    pha                                                               ; 8650: 48          H
    tya                                                               ; 8651: 98          .
    pha                                                               ; 8652: 48          H
    ldx #0                                                            ; 8653: a2 00       ..
    lda (net_tx_ptr,x)                                                ; 8655: a1 9a       ..
; &8657 referenced 1 time by &868a
.c8657
    sta (net_tx_ptr,x)                                                ; 8657: 81 9a       ..
    pha                                                               ; 8659: 48          H
; &865a referenced 1 time by &865d
.loop_c865a
    asl tx_ctrl_status                                                ; 865a: 0e 3a 0d    .:.
    bcc loop_c865a                                                    ; 865d: 90 fb       ..
    lda net_tx_ptr                                                    ; 865f: a5 9a       ..
    sta nmi_tx_block                                                  ; 8661: 85 a0       ..
    lda net_tx_ptr_hi                                                 ; 8663: a5 9b       ..
    sta nmi_tx_block_hi                                               ; 8665: 85 a1       ..
    jsr trampoline_tx_setup                                           ; 8667: 20 60 96     `.
; &866a referenced 1 time by &866c
.loop_c866a
    lda (net_tx_ptr,x)                                                ; 866a: a1 9a       ..
    bmi loop_c866a                                                    ; 866c: 30 fc       0.
    asl a                                                             ; 866e: 0a          .
    bpl c8690                                                         ; 866f: 10 1f       ..
    asl a                                                             ; 8671: 0a          .
    beq c868c                                                         ; 8672: f0 18       ..
    jsr check_escape                                                  ; 8674: 20 7a 84     z.
    pla                                                               ; 8677: 68          h
    tax                                                               ; 8678: aa          .
    pla                                                               ; 8679: 68          h
    tay                                                               ; 867a: a8          .
    pla                                                               ; 867b: 68          h
    beq c868c                                                         ; 867c: f0 0e       ..
    sbc #1                                                            ; 867e: e9 01       ..
    pha                                                               ; 8680: 48          H
    tya                                                               ; 8681: 98          .
    pha                                                               ; 8682: 48          H
    txa                                                               ; 8683: 8a          .
; &8684 referenced 2 times by &8685, &8688
.delay_1ms
    dex                                                               ; 8684: ca          .
    bne delay_1ms                                                     ; 8685: d0 fd       ..
    dey                                                               ; 8687: 88          .
    bne delay_1ms                                                     ; 8688: d0 fa       ..
    beq c8657                                                         ; 868a: f0 cb       ..             ; ALWAYS branch

; &868c referenced 2 times by &8672, &867c
.c868c
    tax                                                               ; 868c: aa          .
    jmp c8428                                                         ; 868d: 4c 28 84    L(.

; &8690 referenced 1 time by &866f
.c8690
    pla                                                               ; 8690: 68          h
    pla                                                               ; 8691: 68          h
    pla                                                               ; 8692: 68          h
    rts                                                               ; 8693: 60          `

; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Saves A/X/Y, copies the filename pointer from the parameter block
; to os_text_ptr, then uses GSINIT/GSREAD to parse the filename into
; $0FC5+. Sets fs_crc_lo/hi to point at the parsed filename buffer.
; Dispatches by function code A:
;   A=$FF: load file (send_fs_examine at $86D0)
;   A=$00: save file (filev_save at $8746)
;   A=$01-$06: attribute operations (filev_attrib_dispatch at $8844)
;   Other: restore_args_return (unsupported, no-op)
; 
; On Entry:
;     A: function code ($FF=load, $00=save, $01-$06=attrs)
;     X: parameter block address low byte
;     Y: parameter block address high byte
; 
; On Exit:
;     A: restored
;     X: restored
;     Y: restored
; ***************************************************************************************
.filev_handler
    jsr save_fscv_args                                                ; 8694: 20 08 85     ..
    ldy #1                                                            ; 8697: a0 01       ..
; &8699 referenced 1 time by &869f
.loop_c8699
    lda (fs_options),y                                                ; 8699: b1 bb       ..
    sta os_text_ptr,y                                                 ; 869b: 99 f2 00    ...
    dey                                                               ; 869e: 88          .
    bpl loop_c8699                                                    ; 869f: 10 f8       ..
    iny                                                               ; 86a1: c8          .
    ldx #&ff                                                          ; 86a2: a2 ff       ..
    clc                                                               ; 86a4: 18          .
    jsr gsinit                                                        ; 86a5: 20 c2 ff     ..
; &86a8 referenced 1 time by &86b1
.loop_c86a8
    jsr gsread                                                        ; 86a8: 20 c5 ff     ..
    bcs c86b3                                                         ; 86ab: b0 06       ..
    inx                                                               ; 86ad: e8          .
    sta l0fc5,x                                                       ; 86ae: 9d c5 0f    ...
    bcc loop_c86a8                                                    ; 86b1: 90 f5       ..             ; ALWAYS branch

; &86b3 referenced 1 time by &86ab
.c86b3
    lda #&0d                                                          ; 86b3: a9 0d       ..
    sta l0fc6,x                                                       ; 86b5: 9d c6 0f    ...
    lda #&c5                                                          ; 86b8: a9 c5       ..
    sta fs_crc_lo                                                     ; 86ba: 85 be       ..
    lda #&0f                                                          ; 86bc: a9 0f       ..
    sta fs_crc_hi                                                     ; 86be: 85 bf       ..
    lda fs_last_byte_flag                                             ; 86c0: a5 bd       ..
    bpl c8741                                                         ; 86c2: 10 7d       .}
    cmp #&ff                                                          ; 86c4: c9 ff       ..
    beq c86cb                                                         ; 86c6: f0 03       ..
    jmp restore_args_return                                           ; 86c8: 4c 2c 89    L,.

; &86cb referenced 1 time by &86c6
.c86cb
    jsr copy_filename                                                 ; 86cb: 20 63 8d     c.
    ldy #2                                                            ; 86ce: a0 02       ..
; Send FS examine command
; Sends FS command $03 (FCEXAM: examine file) to the fileserver.
; Sets $0F02=$03 and error pointer to '*'. Called for OSFILE $FF
; (load file) with the filename already in the command buffer.
; The FS reply contains load/exec addresses and file length which
; are used to set up the data transfer. The header URD field
; is repurposed to carry the Econet data port number (PLDATA=$92)
; for the subsequent block data transfer.
; &86d0 referenced 1 time by &8d90
.send_fs_examine
    lda #&92                                                          ; 86d0: a9 92       ..
    sta fs_cmd_urd                                                    ; 86d2: 8d 02 0f    ...
    lda #&2a ; '*'                                                    ; 86d5: a9 2a       .*
    jsr prepare_cmd_clv                                               ; 86d7: 20 46 83     F.
    ldy #6                                                            ; 86da: a0 06       ..
    lda (fs_options),y                                                ; 86dc: b1 bb       ..
    bne c86e8                                                         ; 86de: d0 08       ..
    jsr copy_load_addr_from_params                                    ; 86e0: 20 ad 87     ..
    jsr copy_reply_to_params                                          ; 86e3: 20 ba 87     ..
    bcc c86ee                                                         ; 86e6: 90 06       ..
; &86e8 referenced 1 time by &86de
.c86e8
    jsr copy_reply_to_params                                          ; 86e8: 20 ba 87     ..
    jsr copy_load_addr_from_params                                    ; 86eb: 20 ad 87     ..
; &86ee referenced 1 time by &86e6
.c86ee
    ldy #4                                                            ; 86ee: a0 04       ..
; &86f0 referenced 1 time by &86fb
.loop_c86f0
    lda fs_load_addr,x                                                ; 86f0: b5 b0       ..
    sta l00c8,x                                                       ; 86f2: 95 c8       ..
    adc l0f0d,x                                                       ; 86f4: 7d 0d 0f    }..
    sta l00b4,x                                                       ; 86f7: 95 b4       ..
    inx                                                               ; 86f9: e8          .
    dey                                                               ; 86fa: 88          .
    bne loop_c86f0                                                    ; 86fb: d0 f3       ..
    sec                                                               ; 86fd: 38          8
    sbc l0f10                                                         ; 86fe: ed 10 0f    ...
    sta l00b7                                                         ; 8701: 85 b7       ..
    jsr print_file_info                                               ; 8703: 20 00 86     ..
    jsr send_data_blocks                                              ; 8706: 20 16 87     ..
    ldx #2                                                            ; 8709: a2 02       ..
; &870b referenced 1 time by &8712
.loop_c870b
    lda l0f10,x                                                       ; 870b: bd 10 0f    ...
    sta fs_cmd_data,x                                                 ; 870e: 9d 05 0f    ...
    dex                                                               ; 8711: ca          .
    bpl loop_c870b                                                    ; 8712: 10 f7       ..
    bmi c878c                                                         ; 8714: 30 76       0v             ; ALWAYS branch

; Send file data in multi-block chunks
; Repeatedly sends $80-byte (128-byte) blocks of file data to the
; fileserver using command $7F. Compares current address ($C8-$CB)
; against end address ($B4-$B7) via compare_addresses, and loops
; until the entire file has been transferred. Each block is sent
; via send_to_fs_star.
; &8716 referenced 2 times by &8706, &8a70
.send_data_blocks
    jsr compare_addresses                                             ; 8716: 20 ce 85     ..            ; Compare two 4-byte addresses
    beq return_5                                                      ; 8719: f0 25       .%
    lda #&92                                                          ; 871b: a9 92       ..
    sta l00c1                                                         ; 871d: 85 c1       ..
; &871f referenced 1 time by &873b
.loop_c871f
    ldx #3                                                            ; 871f: a2 03       ..
; &8721 referenced 1 time by &872a
.loop_c8721
    lda l00c8,x                                                       ; 8721: b5 c8       ..
    sta l00c4,x                                                       ; 8723: 95 c4       ..
    lda l00b4,x                                                       ; 8725: b5 b4       ..
    sta l00c8,x                                                       ; 8727: 95 c8       ..
    dex                                                               ; 8729: ca          .
    bpl loop_c8721                                                    ; 872a: 10 f5       ..
    lda #&7f                                                          ; 872c: a9 7f       ..
    sta l00c0                                                         ; 872e: 85 c0       ..
    jsr send_to_fs_star                                               ; 8730: 20 48 84     H.
    ldy #3                                                            ; 8733: a0 03       ..
; &8735 referenced 1 time by &873e
.loop_c8735
    lda l00c8,y                                                       ; 8735: b9 c8 00    ...
    eor l00b4,y                                                       ; 8738: 59 b4 00    Y..
    bne loop_c871f                                                    ; 873b: d0 e2       ..
    dey                                                               ; 873d: 88          .
    bpl loop_c8735                                                    ; 873e: 10 f5       ..
; &8740 referenced 1 time by &8719
.return_5
    rts                                                               ; 8740: 60          `

; &8741 referenced 1 time by &86c2
.c8741
    beq filev_save                                                    ; 8741: f0 03       ..
    jmp filev_attrib_dispatch                                         ; 8743: 4c 44 88    LD.

; OSFILE save handler (A=$00)
; Copies 4-byte load/exec/length addresses from the parameter block
; to the FS command buffer, along with the filename. Sends FS
; command $91 with function $14 to initiate the save, then
; calls print_file_info to display the filename being saved.
; Handles both host and Tube-based data sources.
; When receiving the save acknowledgement, the RX low pointer is
; incremented by 1 to skip the command code (CC) byte, which
; indicates the FS type and must be preserved. N.B. this assumes
; the RX buffer does not cross a page boundary.
; &8746 referenced 1 time by &8741
.filev_save
    ldx #4                                                            ; 8746: a2 04       ..
    ldy #&0e                                                          ; 8748: a0 0e       ..
; &874a referenced 1 time by &8764
.loop_c874a
    lda (fs_options),y                                                ; 874a: b1 bb       ..
    sta port_ws_offset,y                                              ; 874c: 99 a6 00    ...
    jsr sub_4_from_y                                                  ; 874f: 20 aa 84     ..
    sbc (fs_options),y                                                ; 8752: f1 bb       ..
    sta fs_cmd_csd,y                                                  ; 8754: 99 03 0f    ...
    pha                                                               ; 8757: 48          H
    lda (fs_options),y                                                ; 8758: b1 bb       ..
    sta port_ws_offset,y                                              ; 875a: 99 a6 00    ...
    pla                                                               ; 875d: 68          h
    sta (fs_options),y                                                ; 875e: 91 bb       ..
    jsr add_5_to_y                                                    ; 8760: 20 a4 84     ..
    dex                                                               ; 8763: ca          .
    bne loop_c874a                                                    ; 8764: d0 e4       ..
    ldy #9                                                            ; 8766: a0 09       ..
; &8768 referenced 1 time by &876e
.loop_c8768
    lda (fs_options),y                                                ; 8768: b1 bb       ..
    sta fs_cmd_csd,y                                                  ; 876a: 99 03 0f    ...
    dey                                                               ; 876d: 88          .
    bne loop_c8768                                                    ; 876e: d0 f8       ..
    lda #&91                                                          ; 8770: a9 91       ..
    sta fs_cmd_urd                                                    ; 8772: 8d 02 0f    ...
    sta fs_error_ptr                                                  ; 8775: 85 b8       ..
    ldx #&0b                                                          ; 8777: a2 0b       ..
    jsr copy_string_to_cmd                                            ; 8779: 20 65 8d     e.
    ldy #1                                                            ; 877c: a0 01       ..
    lda #&14                                                          ; 877e: a9 14       ..
    jsr prepare_cmd_clv                                               ; 8780: 20 46 83     F.
    jsr print_file_info                                               ; 8783: 20 00 86     ..
    lda fs_cmd_data                                                   ; 8786: ad 05 0f    ...
    jsr transfer_file_blocks                                          ; 8789: 20 c8 87     ..
; &878c referenced 1 time by &8714
.c878c
    lda #&2a ; '*'                                                    ; 878c: a9 2a       .*
    sta fs_error_ptr                                                  ; 878e: 85 b8       ..
    jsr send_fs_reply_cmd                                             ; 8790: 20 80 83     ..
    stx l0f08                                                         ; 8793: 8e 08 0f    ...
    ldy #&0e                                                          ; 8796: a0 0e       ..
    lda fs_cmd_data                                                   ; 8798: ad 05 0f    ...
    jsr decode_attribs_5bit                                           ; 879b: 20 1d 85     ..
    beq c87a3                                                         ; 879e: f0 03       ..
; &87a0 referenced 1 time by &87a8
.loop_c87a0
    lda l0ef7,y                                                       ; 87a0: b9 f7 0e    ...
; &87a3 referenced 1 time by &879e
.c87a3
    sta (fs_options),y                                                ; 87a3: 91 bb       ..
    iny                                                               ; 87a5: c8          .
    cpy #&12                                                          ; 87a6: c0 12       ..
    bne loop_c87a0                                                    ; 87a8: d0 f6       ..
    jmp restore_args_return                                           ; 87aa: 4c 2c 89    L,.

; Copy load address from parameter block
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to $AE-$B3 (local workspace).
; &87ad referenced 2 times by &86e0, &86eb
.copy_load_addr_from_params
    ldy #5                                                            ; 87ad: a0 05       ..
; &87af referenced 1 time by &87b7
.loop_c87af
    lda (fs_options),y                                                ; 87af: b1 bb       ..
    sta l00ae,y                                                       ; 87b1: 99 ae 00    ...
    dey                                                               ; 87b4: 88          .
    cpy #2                                                            ; 87b5: c0 02       ..
    bcs loop_c87af                                                    ; 87b7: b0 f6       ..
    rts                                                               ; 87b9: 60          `

; Copy FS reply data to parameter block
; Copies bytes from the FS command reply buffer ($0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; &87ba referenced 2 times by &86e3, &86e8
.copy_reply_to_params
    ldy #&0d                                                          ; 87ba: a0 0d       ..
    txa                                                               ; 87bc: 8a          .
; &87bd referenced 1 time by &87c5
.loop_c87bd
    sta (fs_options),y                                                ; 87bd: 91 bb       ..
    lda fs_cmd_urd,y                                                  ; 87bf: b9 02 0f    ...
    dey                                                               ; 87c2: 88          .
    cpy #2                                                            ; 87c3: c0 02       ..
    bcs loop_c87bd                                                    ; 87c5: b0 f6       ..
    rts                                                               ; 87c7: 60          `

; Multi-block file data transfer
; Manages the transfer of file data in chunks between the local
; machine and the fileserver. Entry conditions: WORK ($B0-$B3) and
; WORK+4 ($B4-$B7) hold the low and high addresses of the data
; being sent/received. Sets up source ($C4-$C7) and destination
; ($C8-$CB) from the FS reply, sends $80-byte (128-byte) blocks
; with command $91, and continues until all data has been
; transferred. Handles address overflow and Tube co-processor
; transfers. For SAVE, WORK+8 holds the port on which to receive
; byte-level ACKs for each data block (flow control).
; &87c8 referenced 2 times by &8789, &8a6b
.transfer_file_blocks
    pha                                                               ; 87c8: 48          H
    jsr compare_addresses                                             ; 87c9: 20 ce 85     ..            ; Compare two 4-byte addresses
    beq c8840                                                         ; 87cc: f0 72       .r
; &87ce referenced 1 time by &881d
.c87ce
    ldx #0                                                            ; 87ce: a2 00       ..
    ldy #4                                                            ; 87d0: a0 04       ..
    stx l0f08                                                         ; 87d2: 8e 08 0f    ...
    stx l0f09                                                         ; 87d5: 8e 09 0f    ...
    clc                                                               ; 87d8: 18          .
; &87d9 referenced 1 time by &87e6
.loop_c87d9
    lda fs_load_addr,x                                                ; 87d9: b5 b0       ..
    sta l00c4,x                                                       ; 87db: 95 c4       ..
    adc l0f06,x                                                       ; 87dd: 7d 06 0f    }..
    sta l00c8,x                                                       ; 87e0: 95 c8       ..
    sta fs_load_addr,x                                                ; 87e2: 95 b0       ..
    inx                                                               ; 87e4: e8          .
    dey                                                               ; 87e5: 88          .
    bne loop_c87d9                                                    ; 87e6: d0 f1       ..
    bcs c87f7                                                         ; 87e8: b0 0d       ..
    sec                                                               ; 87ea: 38          8
; &87eb referenced 1 time by &87f3
.loop_c87eb
    lda fs_load_addr,y                                                ; 87eb: b9 b0 00    ...
    sbc l00b4,y                                                       ; 87ee: f9 b4 00    ...
    iny                                                               ; 87f1: c8          .
    dex                                                               ; 87f2: ca          .
    bne loop_c87eb                                                    ; 87f3: d0 f6       ..
    bcc c8800                                                         ; 87f5: 90 09       ..
; &87f7 referenced 1 time by &87e8
.c87f7
    ldx #3                                                            ; 87f7: a2 03       ..
; &87f9 referenced 1 time by &87fe
.loop_c87f9
    lda l00b4,x                                                       ; 87f9: b5 b4       ..
    sta l00c8,x                                                       ; 87fb: 95 c8       ..
    dex                                                               ; 87fd: ca          .
    bpl loop_c87f9                                                    ; 87fe: 10 f9       ..
; &8800 referenced 1 time by &87f5
.c8800
    pla                                                               ; 8800: 68          h
    pha                                                               ; 8801: 48          H
    php                                                               ; 8802: 08          .
    sta l00c1                                                         ; 8803: 85 c1       ..
    lda #&80                                                          ; 8805: a9 80       ..
    sta l00c0                                                         ; 8807: 85 c0       ..
    jsr setup_tx_ptr_c0                                               ; 8809: 20 44 86     D.
    lda fs_error_ptr                                                  ; 880c: a5 b8       ..
    jsr init_tx_ctrl_port                                             ; 880e: 20 10 83     ..
    plp                                                               ; 8811: 28          (
    bcs c8840                                                         ; 8812: b0 2c       .,
    lda #&91                                                          ; 8814: a9 91       ..
    sta l00c1                                                         ; 8816: 85 c1       ..
    lda #&2a ; '*'                                                    ; 8818: a9 2a       .*
    jsr send_to_fs                                                    ; 881a: 20 4a 84     J.
    bne c87ce                                                         ; 881d: d0 af       ..
; FSCV 1: EOF handler
; Checks whether a file handle has reached end-of-file. Converts
; the handle via handle_to_mask_clc, tests the result against the
; EOF hint byte ($0E07). If the hint bit is clear, returns X=0
; immediately (definitely not at EOF — no network call needed).
; If the hint bit is set, sends FS command $11 (FCEOF) to query
; the fileserver for definitive EOF status. Returns X=$FF if at
; EOF, X=$00 if not. This two-level check avoids an expensive
; network round-trip when the file is known to not be at EOF.
.eof_handler
    pha                                                               ; 881f: 48          H
    sty fs_block_offset                                               ; 8820: 84 bc       ..
    jsr handle_to_mask_clc                                            ; 8822: 20 89 85     ..
    tya                                                               ; 8825: 98          .
    and fs_eof_flags                                                  ; 8826: 2d 07 0e    -..
    tax                                                               ; 8829: aa          .
    beq c8840                                                         ; 882a: f0 14       ..
    pha                                                               ; 882c: 48          H
    sty fs_cmd_data                                                   ; 882d: 8c 05 0f    ...
    ldy #&11                                                          ; 8830: a0 11       ..             ; Y=function code for HDRFN
    ldx #1                                                            ; 8832: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8834: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    pla                                                               ; 8837: 68          h
    ldx fs_cmd_data                                                   ; 8838: ae 05 0f    ...
    bne c8840                                                         ; 883b: d0 03       ..
    jsr clear_fs_flag                                                 ; 883d: 20 df 85     ..
; &8840 referenced 4 times by &87cc, &8812, &882a, &883b
.c8840
    pla                                                               ; 8840: 68          h
    ldy fs_block_offset                                               ; 8841: a4 bc       ..
    rts                                                               ; 8843: 60          `

; FILEV attribute dispatch (A=1-6)
; Dispatches OSFILE operations by function code:
;   A=1: write catalogue info (load/exec/length/attrs) — FS $14
;   A=2: write load address only
;   A=3: write exec address only
;   A=4: write file attributes
;   A=5: read catalogue info, returns type in A — FS $12
;   A=6: delete named object — FS $14 (FCDEL)
;   A>=7: falls through to restore_args_return (no-op)
; Each handler builds the appropriate FS command, sends it to
; the fileserver, and copies the reply into the parameter block.
; The control block layout uses dual-purpose fields: the 'data
; start' field doubles as 'length' and 'data end' doubles as
; 'protection' depending on whether reading or writing attrs.
; &8844 referenced 1 time by &8743
.filev_attrib_dispatch
    sta fs_cmd_data                                                   ; 8844: 8d 05 0f    ...
    cmp #6                                                            ; 8847: c9 06       ..
    beq c888a                                                         ; 8849: f0 3f       .?
    bcs c8895                                                         ; 884b: b0 48       .H
    cmp #5                                                            ; 884d: c9 05       ..
    beq c88a3                                                         ; 884f: f0 52       .R
    cmp #4                                                            ; 8851: c9 04       ..
    beq c8899                                                         ; 8853: f0 44       .D
    cmp #1                                                            ; 8855: c9 01       ..
    beq get_file_protection                                           ; 8857: f0 15       ..
    asl a                                                             ; 8859: 0a          .
    asl a                                                             ; 885a: 0a          .
    tay                                                               ; 885b: a8          .
    jsr sub_3_from_y                                                  ; 885c: 20 ab 84     ..
    ldx #3                                                            ; 885f: a2 03       ..
; &8861 referenced 1 time by &8868
.loop_c8861
    lda (fs_options),y                                                ; 8861: b1 bb       ..
    sta l0f06,x                                                       ; 8863: 9d 06 0f    ...
    dey                                                               ; 8866: 88          .
    dex                                                               ; 8867: ca          .
    bpl loop_c8861                                                    ; 8868: 10 f7       ..
    ldx #5                                                            ; 886a: a2 05       ..
    bne copy_filename_to_cmd                                          ; 886c: d0 15       ..             ; ALWAYS branch

; &886e referenced 1 time by &8857
.get_file_protection
    jsr decode_attribs_6bit                                           ; 886e: 20 13 85     ..
    sta l0f0e                                                         ; 8871: 8d 0e 0f    ...
    ldy #9                                                            ; 8874: a0 09       ..
    ldx #8                                                            ; 8876: a2 08       ..
; &8878 referenced 1 time by &887f
.loop_c8878
    lda (fs_options),y                                                ; 8878: b1 bb       ..
    sta fs_cmd_data,x                                                 ; 887a: 9d 05 0f    ...
    dey                                                               ; 887d: 88          .
    dex                                                               ; 887e: ca          .
    bne loop_c8878                                                    ; 887f: d0 f7       ..
    ldx #&0a                                                          ; 8881: a2 0a       ..
; &8883 referenced 2 times by &886c, &88a1
.copy_filename_to_cmd
    jsr copy_string_to_cmd                                            ; 8883: 20 65 8d     e.
    ldy #&13                                                          ; 8886: a0 13       ..
    bne c888f                                                         ; 8888: d0 05       ..             ; ALWAYS branch

; &888a referenced 1 time by &8849
.c888a
    jsr copy_filename                                                 ; 888a: 20 63 8d     c.
    ldy #&14                                                          ; 888d: a0 14       ..
; &888f referenced 1 time by &8888
.c888f
    bit l833a                                                         ; 888f: 2c 3a 83    ,:.
    jsr prepare_fs_cmd_v                                              ; 8892: 20 51 83     Q.
; &8895 referenced 1 time by &884b
.c8895
    bcs c88df                                                         ; 8895: b0 48       .H
    bcc c8910                                                         ; 8897: 90 77       .w             ; ALWAYS branch

; &8899 referenced 1 time by &8853
.c8899
    jsr decode_attribs_6bit                                           ; 8899: 20 13 85     ..
    sta l0f06                                                         ; 889c: 8d 06 0f    ...
    ldx #2                                                            ; 889f: a2 02       ..
    bne copy_filename_to_cmd                                          ; 88a1: d0 e0       ..             ; ALWAYS branch

; &88a3 referenced 1 time by &884f
.c88a3
    ldx #1                                                            ; 88a3: a2 01       ..
    jsr copy_string_to_cmd                                            ; 88a5: 20 65 8d     e.
    ldy #&12                                                          ; 88a8: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 88aa: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    lda l0f11                                                         ; 88ad: ad 11 0f    ...
    stx l0f11                                                         ; 88b0: 8e 11 0f    ...            ; X=0 on success, $D6 on not-found
    stx l0f14                                                         ; 88b3: 8e 14 0f    ...
    jsr decode_attribs_5bit                                           ; 88b6: 20 1d 85     ..
    ldx fs_cmd_data                                                   ; 88b9: ae 05 0f    ...
    beq c88de                                                         ; 88bc: f0 20       .
    ldy #&0e                                                          ; 88be: a0 0e       ..
    sta (fs_options),y                                                ; 88c0: 91 bb       ..
    dey                                                               ; 88c2: 88          .              ; Y=&0d
    ldx #&0c                                                          ; 88c3: a2 0c       ..
; &88c5 referenced 1 time by &88cc
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 88c5: bd 05 0f    ...
    sta (fs_options),y                                                ; 88c8: 91 bb       ..
    dey                                                               ; 88ca: 88          .
    dex                                                               ; 88cb: ca          .
    bne copy_fs_reply_to_cb                                           ; 88cc: d0 f7       ..
    inx                                                               ; 88ce: e8          .
    inx                                                               ; 88cf: e8          .
    ldy #&11                                                          ; 88d0: a0 11       ..
; &88d2 referenced 1 time by &88d9
.loop_c88d2
    lda l0f12,x                                                       ; 88d2: bd 12 0f    ...
    sta (fs_options),y                                                ; 88d5: 91 bb       ..
    dey                                                               ; 88d7: 88          .
    dex                                                               ; 88d8: ca          .
    bpl loop_c88d2                                                    ; 88d9: 10 f7       ..
    ldx fs_cmd_data                                                   ; 88db: ae 05 0f    ...
; &88de referenced 1 time by &88bc
.c88de
    txa                                                               ; 88de: 8a          .
; &88df referenced 1 time by &8895
.c88df
    bpl c892e                                                         ; 88df: 10 4d       .M
; ***************************************************************************************
; ARGSV handler (OSARGS entry point)
; 
;   A=0, Y=0: return filing system number (10 = network FS)
;   A=0, Y>0: read file pointer via FS command $0A (FCRDSE)
;   A=1, Y>0: write file pointer via FS command $14 (FCWRSE)
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
    jsr save_fscv_args                                                ; 88e1: 20 08 85     ..
    cmp #3                                                            ; 88e4: c9 03       ..
    bcs restore_args_return                                           ; 88e6: b0 44       .D
    cpy #0                                                            ; 88e8: c0 00       ..
    beq c8933                                                         ; 88ea: f0 47       .G
    jsr handle_to_mask_clc                                            ; 88ec: 20 89 85     ..
    sty fs_cmd_data                                                   ; 88ef: 8c 05 0f    ...
    lsr a                                                             ; 88f2: 4a          J
    sta l0f06                                                         ; 88f3: 8d 06 0f    ...
    bcs save_args_handle                                              ; 88f6: b0 1a       ..
    ldy #&0c                                                          ; 88f8: a0 0c       ..             ; Y=function code for HDRFN
    ldx #2                                                            ; 88fa: a2 02       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 88fc: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 88ff: 85 bd       ..             ; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 8901: a6 bb       ..
    ldy #2                                                            ; 8903: a0 02       ..
    sta l0003,x                                                       ; 8905: 95 03       ..
; &8907 referenced 1 time by &890e
.loop_c8907
    lda fs_cmd_data,y                                                 ; 8907: b9 05 0f    ...
    sta l0002,x                                                       ; 890a: 95 02       ..
    dex                                                               ; 890c: ca          .
    dey                                                               ; 890d: 88          .
    bpl loop_c8907                                                    ; 890e: 10 f7       ..
; &8910 referenced 1 time by &8897
.c8910
    bcc restore_args_return                                           ; 8910: 90 1a       ..
; &8912 referenced 1 time by &88f6
.save_args_handle
    tya                                                               ; 8912: 98          .
    pha                                                               ; 8913: 48          H
    ldy #3                                                            ; 8914: a0 03       ..
; &8916 referenced 1 time by &891d
.loop_c8916
    lda l0003,x                                                       ; 8916: b5 03       ..
    sta l0f07,y                                                       ; 8918: 99 07 0f    ...
    dex                                                               ; 891b: ca          .
    dey                                                               ; 891c: 88          .
    bpl loop_c8916                                                    ; 891d: 10 f7       ..
    ldy #&0d                                                          ; 891f: a0 0d       ..             ; Y=function code for HDRFN
    ldx #5                                                            ; 8921: a2 05       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8923: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    stx fs_last_byte_flag                                             ; 8926: 86 bd       ..             ; X=0 on success, $D6 on not-found
    pla                                                               ; 8928: 68          h
    jsr set_fs_flag                                                   ; 8929: 20 e4 85     ..
; Restore arguments and return
; Common exit point for FS vector handlers. Reloads A from
; fs_last_byte_flag ($BD), X from fs_options ($BB), and Y from
; fs_block_offset ($BC) — the values saved at entry by
; save_fscv_args — and returns to the caller.
; &892c referenced 8 times by &86c8, &87aa, &88e6, &8910, &893b, &899f, &89f5, &8cff
.restore_args_return
    lda fs_last_byte_flag                                             ; 892c: a5 bd       ..
; &892e referenced 5 times by &88df, &8938, &8947, &896f, &8983
.c892e
    ldx fs_options                                                    ; 892e: a6 bb       ..
    ldy fs_block_offset                                               ; 8930: a4 bc       ..
    rts                                                               ; 8932: 60          `

; &8933 referenced 1 time by &88ea
.c8933
    tay                                                               ; 8933: a8          .
    bne c893a                                                         ; 8934: d0 04       ..
    lda #5                                                            ; 8936: a9 05       ..
    bne c892e                                                         ; 8938: d0 f4       ..             ; ALWAYS branch

; &893a referenced 1 time by &8934
.c893a
    lsr a                                                             ; 893a: 4a          J
    bne restore_args_return                                           ; 893b: d0 ef       ..
; &893d referenced 1 time by &8943
.loop_c893d
    lda l0e0b,y                                                       ; 893d: b9 0b 0e    ...
    sta (fs_options),y                                                ; 8940: 91 bb       ..
    dey                                                               ; 8942: 88          .
    bpl loop_c893d                                                    ; 8943: 10 f8       ..
; &8945 referenced 3 times by &8955, &8a95, &8b32
.c8945
    lda #0                                                            ; 8945: a9 00       ..             ; A=operation (0=close, $40=read, $80=write, $C0=R/W)
    bpl c892e                                                         ; 8947: 10 e5       ..             ; ALWAYS branch

; ***************************************************************************************
; FINDV handler (OSFIND entry point)
; 
;   A=0: close file -- delegates to close_handle ($8985)
;   A>0: open file -- modes $40=read, $80=write/update, $C0=read/write
; For open: the mode byte is converted to the fileserver's two-flag
; format by flipping bit 7 (EOR #$80) and shifting. This produces
; Flag 1 (read/write direction) and Flag 2 (create/existing),
; matching the fileserver protocol. After a successful open, the
; new handle's bit is OR'd into the EOF hint byte (marks it as
; "might be at EOF, query the server"), and into the sequence
; number tracking byte for the byte-stream protocol.
; 
; On Entry:
;     A: operation (0=close, $40=read, $80=write, $C0=R/W)
;     X: filename pointer low (open)
;     Y: file handle (close) or filename pointer high (open)
; 
; On Exit:
;     A: handle on open, 0 on close-all, restored on close-one
;     X: restored
;     Y: restored
; ***************************************************************************************
.findv_handler
    jsr save_fscv_args                                                ; 8949: 20 08 85     ..
    sec                                                               ; 894c: 38          8
    jsr handle_to_mask                                                ; 894d: 20 8a 85     ..            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 8950: aa          .              ; A=preserved
    beq close_handle                                                  ; 8951: f0 32       .2
    and #&3f ; '?'                                                    ; 8953: 29 3f       )?
    bne c8945                                                         ; 8955: d0 ee       ..
    txa                                                               ; 8957: 8a          .
    eor #&80                                                          ; 8958: 49 80       I.
    asl a                                                             ; 895a: 0a          .
    sta fs_cmd_data                                                   ; 895b: 8d 05 0f    ...
    rol a                                                             ; 895e: 2a          *
    sta l0f06                                                         ; 895f: 8d 06 0f    ...
    ldx #2                                                            ; 8962: a2 02       ..
    jsr copy_string_to_cmd                                            ; 8964: 20 65 8d     e.
    ldy #6                                                            ; 8967: a0 06       ..
    bit l833a                                                         ; 8969: 2c 3a 83    ,:.
    jsr prepare_fs_cmd_v                                              ; 896c: 20 51 83     Q.
    bcs c892e                                                         ; 896f: b0 bd       ..
    lda fs_cmd_data                                                   ; 8971: ad 05 0f    ...
    tax                                                               ; 8974: aa          .
    jsr set_fs_flag                                                   ; 8975: 20 e4 85     ..
    txa                                                               ; 8978: 8a          .
    ora fs_sequence_nos                                               ; 8979: 0d 08 0e    ...
    sta fs_sequence_nos                                               ; 897c: 8d 08 0e    ...
    txa                                                               ; 897f: 8a          .              ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8980: 20 a5 85     ..            ; Convert bitmask to handle number (FS2A)
    bne c892e                                                         ; 8983: d0 a9       ..
; Close file handle(s) (CLOSE)
;   Y=0: close all files — first calls OSBYTE $77 (close SPOOL and
;        EXEC files) to coordinate with the MOS before sending the
;        close-all command to the fileserver. This ensures locally-
;        managed file handles are released before the server-side
;        handles are invalidated, preventing the MOS from writing to
;        a closed spool file.
;   Y>0: close single handle — sends FS close command and clears
;        the handle's bit in both the EOF hint byte and the sequence
;        number tracking byte.
; &8985 referenced 1 time by &8951
.close_handle
    tya                                                               ; 8985: 98          .              ; Y=preserved
    bne close_single_handle                                           ; 8986: d0 07       ..
    lda #osbyte_close_spool_exec                                      ; 8988: a9 77       .w
    jsr osbyte                                                        ; 898a: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 898d: a0 00       ..
; &898f referenced 1 time by &8986
.close_single_handle
    sty fs_cmd_data                                                   ; 898f: 8c 05 0f    ...
    ldx #1                                                            ; 8992: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 8994: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8996: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 8999: ad 05 0f    ...
    jsr set_fs_flag                                                   ; 899c: 20 e4 85     ..
; &899f referenced 1 time by &89c8
.c899f
    bcc restore_args_return                                           ; 899f: 90 8b       ..
; FSCV 0: *OPT handler (OPTION)
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in $0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command $16 (FCOPT)
; Other combinations generate error $CB (OPTER: "bad option").
.opt_handler
    cpx #4                                                            ; 89a1: e0 04       ..
    bne c89a9                                                         ; 89a3: d0 04       ..
    cpy #4                                                            ; 89a5: c0 04       ..
    bcc c89bb                                                         ; 89a7: 90 12       ..
; &89a9 referenced 1 time by &89a3
.c89a9
    cpx #1                                                            ; 89a9: e0 01       ..
    bne c89b6                                                         ; 89ab: d0 09       ..
    cpy #2                                                            ; 89ad: c0 02       ..
    bcs c89b6                                                         ; 89af: b0 05       ..
    sty fs_messages_flag                                              ; 89b1: 8c 06 0e    ...
    bcc c89c8                                                         ; 89b4: 90 12       ..             ; ALWAYS branch

; &89b6 referenced 2 times by &89ab, &89af
.c89b6
    lda #7                                                            ; 89b6: a9 07       ..
    jmp c842a                                                         ; 89b8: 4c 2a 84    L*.

; &89bb referenced 1 time by &89a7
.c89bb
    sty fs_cmd_data                                                   ; 89bb: 8c 05 0f    ...
    ldy #&16                                                          ; 89be: a0 16       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89c0: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 89c3: a4 bc       ..
    sty fs_boot_option                                                ; 89c5: 8c 05 0e    ...
; &89c8 referenced 1 time by &89b4
.c89c8
    bcc c899f                                                         ; 89c8: 90 d5       ..
; &89ca referenced 1 time by &8a89
.adjust_addrs_9
    ldy #9                                                            ; 89ca: a0 09       ..
    jsr adjust_addrs_clc                                              ; 89cc: 20 d1 89     ..
; &89cf referenced 1 time by &8b79
.adjust_addrs_1
    ldy #1                                                            ; 89cf: a0 01       ..
; &89d1 referenced 1 time by &89cc
.adjust_addrs_clc
    clc                                                               ; 89d1: 18          .
; Bidirectional 4-byte address adjustment
; Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
;   If fs_load_addr_2 ($B2) is positive: adds fs_lib_handle+X values
;   If fs_load_addr_2 ($B2) is negative: subtracts fs_lib_handle+X
; Starting offset X=$FC means it reads from $0E06-$0E09 area.
; Used to convert between absolute and relative file positions.
; &89d2 referenced 2 times by &8a8f, &8b85
.adjust_addrs
    ldx #&fc                                                          ; 89d2: a2 fc       ..
; &89d4 referenced 1 time by &89e7
.loop_c89d4
    lda (fs_options),y                                                ; 89d4: b1 bb       ..
    bit fs_load_addr_2                                                ; 89d6: 24 b2       $.
    bmi c89e0                                                         ; 89d8: 30 06       0.
    adc fs_cmd_context,x                                              ; 89da: 7d 0a 0e    }..
    jmp c89e3                                                         ; 89dd: 4c e3 89    L..

; &89e0 referenced 1 time by &89d8
.c89e0
    sbc fs_cmd_context,x                                              ; 89e0: fd 0a 0e    ...
; &89e3 referenced 1 time by &89dd
.c89e3
    sta (fs_options),y                                                ; 89e3: 91 bb       ..
    iny                                                               ; 89e5: c8          .
    inx                                                               ; 89e6: e8          .
    bne loop_c89d4                                                    ; 89e7: d0 eb       ..
    rts                                                               ; 89e9: 60          `

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
    jsr save_fscv_args                                                ; 89ea: 20 08 85     ..
    tax                                                               ; 89ed: aa          .
    beq c89f5                                                         ; 89ee: f0 05       ..
    dex                                                               ; 89f0: ca          .
    cpx #8                                                            ; 89f1: e0 08       ..
    bcc c89f8                                                         ; 89f3: 90 03       ..
; &89f5 referenced 1 time by &89ee
.c89f5
    jmp restore_args_return                                           ; 89f5: 4c 2c 89    L,.

; &89f8 referenced 1 time by &89f3
.c89f8
    txa                                                               ; 89f8: 8a          .
    ldy #0                                                            ; 89f9: a0 00       ..
    pha                                                               ; 89fb: 48          H
    cmp #4                                                            ; 89fc: c9 04       ..
    bcc c8a03                                                         ; 89fe: 90 03       ..
    jmp osgbpb_info                                                   ; 8a00: 4c ad 8a    L..

; &8a03 referenced 1 time by &89fe
.c8a03
    lda (fs_options),y                                                ; 8a03: b1 bb       ..
    jsr handle_to_mask_a                                              ; 8a05: 20 88 85     ..
    sty fs_cmd_data                                                   ; 8a08: 8c 05 0f    ...
    ldy #&0b                                                          ; 8a0b: a0 0b       ..
    ldx #6                                                            ; 8a0d: a2 06       ..
; &8a0f referenced 1 time by &8a1b
.loop_c8a0f
    lda (fs_options),y                                                ; 8a0f: b1 bb       ..
    sta l0f06,x                                                       ; 8a11: 9d 06 0f    ...
    dey                                                               ; 8a14: 88          .
    cpy #8                                                            ; 8a15: c0 08       ..
    bne c8a1a                                                         ; 8a17: d0 01       ..
    dey                                                               ; 8a19: 88          .
; &8a1a referenced 1 time by &8a17
.c8a1a
    dex                                                               ; 8a1a: ca          .
    bne loop_c8a0f                                                    ; 8a1b: d0 f2       ..
    pla                                                               ; 8a1d: 68          h
    lsr a                                                             ; 8a1e: 4a          J
    pha                                                               ; 8a1f: 48          H
    bcc c8a23                                                         ; 8a20: 90 01       ..
    inx                                                               ; 8a22: e8          .
; &8a23 referenced 1 time by &8a20
.c8a23
    stx l0f06                                                         ; 8a23: 8e 06 0f    ...
    ldy #&0b                                                          ; 8a26: a0 0b       ..
    ldx #&91                                                          ; 8a28: a2 91       ..
    pla                                                               ; 8a2a: 68          h
    pha                                                               ; 8a2b: 48          H
    beq c8a31                                                         ; 8a2c: f0 03       ..
    ldx #&92                                                          ; 8a2e: a2 92       ..
    dey                                                               ; 8a30: 88          .              ; Y=&0a
; &8a31 referenced 1 time by &8a2c
.c8a31
    stx fs_cmd_urd                                                    ; 8a31: 8e 02 0f    ...
    stx fs_error_ptr                                                  ; 8a34: 86 b8       ..
    ldx #8                                                            ; 8a36: a2 08       ..
    lda fs_cmd_data                                                   ; 8a38: ad 05 0f    ...
    jsr prepare_cmd_with_flag                                         ; 8a3b: 20 40 83     @.
    lda l00b3                                                         ; 8a3e: a5 b3       ..
    sta fs_sequence_nos                                               ; 8a40: 8d 08 0e    ...
    ldx #4                                                            ; 8a43: a2 04       ..
; &8a45 referenced 1 time by &8a59
.loop_c8a45
    lda (fs_options),y                                                ; 8a45: b1 bb       ..
    sta l00af,y                                                       ; 8a47: 99 af 00    ...
    sta l00c7,y                                                       ; 8a4a: 99 c7 00    ...
    jsr add_4_to_y                                                    ; 8a4d: 20 a5 84     ..
    adc (fs_options),y                                                ; 8a50: 71 bb       q.
    sta l00af,y                                                       ; 8a52: 99 af 00    ...
    jsr sub_3_from_y                                                  ; 8a55: 20 ab 84     ..
    dex                                                               ; 8a58: ca          .
    bne loop_c8a45                                                    ; 8a59: d0 ea       ..
    inx                                                               ; 8a5b: e8          .
; &8a5c referenced 1 time by &8a63
.loop_c8a5c
    lda fs_cmd_csd,x                                                  ; 8a5c: bd 03 0f    ...
    sta l0f06,x                                                       ; 8a5f: 9d 06 0f    ...
    dex                                                               ; 8a62: ca          .
    bpl loop_c8a5c                                                    ; 8a63: 10 f7       ..
    pla                                                               ; 8a65: 68          h
    bne c8a70                                                         ; 8a66: d0 08       ..
    lda fs_cmd_urd                                                    ; 8a68: ad 02 0f    ...
    jsr transfer_file_blocks                                          ; 8a6b: 20 c8 87     ..
    bne c8a73                                                         ; 8a6e: d0 03       ..
; &8a70 referenced 1 time by &8a66
.c8a70
    jsr send_data_blocks                                              ; 8a70: 20 16 87     ..
; &8a73 referenced 1 time by &8a6e
.c8a73
    lda #&2a ; '*'                                                    ; 8a73: a9 2a       .*
    sta fs_error_ptr                                                  ; 8a75: 85 b8       ..
    jsr send_fs_reply_cmd                                             ; 8a77: 20 80 83     ..
    lda (fs_options,x)                                                ; 8a7a: a1 bb       ..
    bit fs_cmd_data                                                   ; 8a7c: 2c 05 0f    ,..
    bmi c8a84                                                         ; 8a7f: 30 03       0.
    jsr clear_fs_flag                                                 ; 8a81: 20 df 85     ..
; &8a84 referenced 1 time by &8a7f
.c8a84
    jsr set_fs_flag                                                   ; 8a84: 20 e4 85     ..
    stx fs_load_addr_2                                                ; 8a87: 86 b2       ..
    jsr adjust_addrs_9                                                ; 8a89: 20 ca 89     ..
    dec fs_load_addr_2                                                ; 8a8c: c6 b2       ..
    sec                                                               ; 8a8e: 38          8
    jsr adjust_addrs                                                  ; 8a8f: 20 d2 89     ..
    asl fs_cmd_data                                                   ; 8a92: 0e 05 0f    ...
    jmp c8945                                                         ; 8a95: 4c 45 89    LE.

; &8a98 referenced 1 time by &8ac8
.c8a98
    ldy #&15                                                          ; 8a98: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8a9a: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8a9d: ad 05 0e    ...
    sta l0f16                                                         ; 8aa0: 8d 16 0f    ...
    stx fs_load_addr                                                  ; 8aa3: 86 b0       ..             ; X=0 on success, $D6 on not-found
    stx fs_load_addr_hi                                               ; 8aa5: 86 b1       ..
    lda #&12                                                          ; 8aa7: a9 12       ..
    sta fs_load_addr_2                                                ; 8aa9: 85 b2       ..
    bne copy_reply_to_caller                                          ; 8aab: d0 4e       .N             ; ALWAYS branch

; OSGBPB 5-8 info handler (OSINFO)
; Handles the "messy interface tacked onto OSGBPB" (original source).
; Checks whether the destination address is in Tube space by comparing
; the high bytes against TBFLAG. If in Tube space, data must be
; copied via the Tube FIFO registers (with delays to accommodate the
; slow 16032 co-processor) instead of direct memory access.
; &8aad referenced 1 time by &8a00
.osgbpb_info
    ldy #4                                                            ; 8aad: a0 04       ..
    lda tx_in_progress                                                ; 8aaf: ad 52 0d    .R.
    beq c8abb                                                         ; 8ab2: f0 07       ..
    cmp (fs_options),y                                                ; 8ab4: d1 bb       ..
    bne c8abb                                                         ; 8ab6: d0 03       ..
    dey                                                               ; 8ab8: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8ab9: f1 bb       ..
; &8abb referenced 2 times by &8ab2, &8ab6
.c8abb
    sta fs_temp_ce                                                    ; 8abb: 85 ce       ..
; &8abd referenced 1 time by &8ac3
.loop_c8abd
    lda (fs_options),y                                                ; 8abd: b1 bb       ..
    sta fs_last_byte_flag,y                                           ; 8abf: 99 bd 00    ...
    dey                                                               ; 8ac2: 88          .
    bne loop_c8abd                                                    ; 8ac3: d0 f8       ..
    pla                                                               ; 8ac5: 68          h
    and #3                                                            ; 8ac6: 29 03       ).
    beq c8a98                                                         ; 8ac8: f0 ce       ..
    lsr a                                                             ; 8aca: 4a          J
    beq c8acf                                                         ; 8acb: f0 02       ..
    bcs c8b35                                                         ; 8acd: b0 66       .f
; &8acf referenced 1 time by &8acb
.c8acf
    tay                                                               ; 8acf: a8          .              ; Y=function code
    lda fs_csd_handle,y                                               ; 8ad0: b9 03 0e    ...
    sta fs_cmd_csd                                                    ; 8ad3: 8d 03 0f    ...
    lda fs_lib_handle                                                 ; 8ad6: ad 04 0e    ...
    sta fs_cmd_lib                                                    ; 8ad9: 8d 04 0f    ...
    lda fs_urd_handle                                                 ; 8adc: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 8adf: 8d 02 0f    ...
    ldx #&12                                                          ; 8ae2: a2 12       ..             ; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8ae4: 8e 01 0f    ...
    lda #&0d                                                          ; 8ae7: a9 0d       ..
    sta l0f06                                                         ; 8ae9: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8aec: 85 b2       ..
    lsr a                                                             ; 8aee: 4a          J              ; A=timeout period for FS reply
    sta fs_cmd_data                                                   ; 8aef: 8d 05 0f    ...
    clc                                                               ; 8af2: 18          .
    jsr build_send_fs_cmd                                             ; 8af3: 20 6a 83     j.            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8af6: 86 b1       ..             ; X=0 on success, $D6 on not-found
    inx                                                               ; 8af8: e8          .
    stx fs_load_addr                                                  ; 8af9: 86 b0       ..
; &8afb referenced 2 times by &8aab, &8b6e
.copy_reply_to_caller
    lda fs_temp_ce                                                    ; 8afb: a5 ce       ..
    bne c8b10                                                         ; 8afd: d0 11       ..
    ldx fs_load_addr                                                  ; 8aff: a6 b0       ..
    ldy fs_load_addr_hi                                               ; 8b01: a4 b1       ..
; &8b03 referenced 1 time by &8b0c
.loop_c8b03
    lda fs_cmd_data,x                                                 ; 8b03: bd 05 0f    ...
    sta (fs_crc_lo),y                                                 ; 8b06: 91 be       ..
    inx                                                               ; 8b08: e8          .
    iny                                                               ; 8b09: c8          .
    dec fs_load_addr_2                                                ; 8b0a: c6 b2       ..
    bne loop_c8b03                                                    ; 8b0c: d0 f5       ..
    beq c8b32                                                         ; 8b0e: f0 22       ."             ; ALWAYS branch

; &8b10 referenced 1 time by &8afd
.c8b10
    jsr tube_claim_loop                                               ; 8b10: 20 8a 8b     ..
    lda #1                                                            ; 8b13: a9 01       ..
    ldx fs_options                                                    ; 8b15: a6 bb       ..
    ldy fs_block_offset                                               ; 8b17: a4 bc       ..
    inx                                                               ; 8b19: e8          .
    bne c8b1d                                                         ; 8b1a: d0 01       ..
    iny                                                               ; 8b1c: c8          .
; &8b1d referenced 1 time by &8b1a
.c8b1d
    jsr tube_addr_claim                                               ; 8b1d: 20 06 04     ..
    ldx fs_load_addr                                                  ; 8b20: a6 b0       ..
; &8b22 referenced 1 time by &8b2b
.loop_c8b22
    lda fs_cmd_data,x                                                 ; 8b22: bd 05 0f    ...
    sta tube_data_register_3                                          ; 8b25: 8d e5 fe    ...
    inx                                                               ; 8b28: e8          .
    dec fs_load_addr_2                                                ; 8b29: c6 b2       ..
    bne loop_c8b22                                                    ; 8b2b: d0 f5       ..
    lda #&83                                                          ; 8b2d: a9 83       ..
    jsr tube_addr_claim                                               ; 8b2f: 20 06 04     ..
; &8b32 referenced 2 times by &8b0e, &8b88
.c8b32
    jmp c8945                                                         ; 8b32: 4c 45 89    LE.

; &8b35 referenced 1 time by &8acd
.c8b35
    ldy #9                                                            ; 8b35: a0 09       ..
    lda (fs_options),y                                                ; 8b37: b1 bb       ..
    sta l0f06                                                         ; 8b39: 8d 06 0f    ...
    ldy #5                                                            ; 8b3c: a0 05       ..
    lda (fs_options),y                                                ; 8b3e: b1 bb       ..
    sta l0f07                                                         ; 8b40: 8d 07 0f    ...
    ldx #&0d                                                          ; 8b43: a2 0d       ..             ; X=preserved through header build
    stx l0f08                                                         ; 8b45: 8e 08 0f    ...
    ldy #2                                                            ; 8b48: a0 02       ..
    sty fs_load_addr                                                  ; 8b4a: 84 b0       ..
    sty fs_cmd_data                                                   ; 8b4c: 8c 05 0f    ...
    iny                                                               ; 8b4f: c8          .              ; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8b50: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8b53: 86 b1       ..             ; X=0 on success, $D6 on not-found
    lda l0f06                                                         ; 8b55: ad 06 0f    ...
    sta (fs_options,x)                                                ; 8b58: 81 bb       ..
    lda fs_cmd_data                                                   ; 8b5a: ad 05 0f    ...
    ldy #9                                                            ; 8b5d: a0 09       ..
    adc (fs_options),y                                                ; 8b5f: 71 bb       q.
    sta (fs_options),y                                                ; 8b61: 91 bb       ..
    lda l00c8                                                         ; 8b63: a5 c8       ..
    sbc #7                                                            ; 8b65: e9 07       ..
    sta l0f06                                                         ; 8b67: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8b6a: 85 b2       ..
    beq c8b71                                                         ; 8b6c: f0 03       ..
    jsr copy_reply_to_caller                                          ; 8b6e: 20 fb 8a     ..
; &8b71 referenced 1 time by &8b6c
.c8b71
    ldx #2                                                            ; 8b71: a2 02       ..
; &8b73 referenced 1 time by &8b77
.loop_c8b73
    sta l0f07,x                                                       ; 8b73: 9d 07 0f    ...
    dex                                                               ; 8b76: ca          .
    bpl loop_c8b73                                                    ; 8b77: 10 fa       ..
    jsr adjust_addrs_1                                                ; 8b79: 20 cf 89     ..
    sec                                                               ; 8b7c: 38          8
    dec fs_load_addr_2                                                ; 8b7d: c6 b2       ..
    lda fs_cmd_data                                                   ; 8b7f: ad 05 0f    ...
    sta l0f06                                                         ; 8b82: 8d 06 0f    ...
    jsr adjust_addrs                                                  ; 8b85: 20 d2 89     ..
    beq c8b32                                                         ; 8b88: f0 a8       ..
; &8b8a referenced 3 times by &8b10, &8b8f, &8da0
.tube_claim_loop
    lda #&c3                                                          ; 8b8a: a9 c3       ..
    jsr tube_addr_claim                                               ; 8b8c: 20 06 04     ..
    bcc tube_claim_loop                                               ; 8b8f: 90 f9       ..
    rts                                                               ; 8b91: 60          `

; FSCV 2/3/4: unrecognised * command handler (DECODE)
; CLI parser originally by Roger Wilson (later Sophie Wilson,
; co-designer of ARM). Matches command text against the table
; at $8BD6 using case-insensitive comparison with abbreviation
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
; &8b92 referenced 1 time by &8242
.fscv_star_handler
    jsr save_fscv_args                                                ; 8b92: 20 08 85     ..
    ldx #&ff                                                          ; 8b95: a2 ff       ..
; &8b97 referenced 1 time by &8bb2
.loop_c8b97
    ldy #&ff                                                          ; 8b97: a0 ff       ..
; &8b99 referenced 1 time by &8ba4
.loop_c8b99
    iny                                                               ; 8b99: c8          .
    inx                                                               ; 8b9a: e8          .
; &8b9b referenced 1 time by &8bb6
.loop_c8b9b
    lda fs_cmd_match_table,x                                          ; 8b9b: bd d6 8b    ...
    bmi c8bb8                                                         ; 8b9e: 30 18       0.
    eor (fs_crc_lo),y                                                 ; 8ba0: 51 be       Q.
    and #&df                                                          ; 8ba2: 29 df       ).
    beq loop_c8b99                                                    ; 8ba4: f0 f3       ..
    dex                                                               ; 8ba6: ca          .
; &8ba7 referenced 1 time by &8bab
.loop_c8ba7
    inx                                                               ; 8ba7: e8          .
    lda fs_cmd_match_table,x                                          ; 8ba8: bd d6 8b    ...
    bpl loop_c8ba7                                                    ; 8bab: 10 fa       ..
    lda (fs_crc_lo),y                                                 ; 8bad: b1 be       ..
    inx                                                               ; 8baf: e8          .
    cmp #&2e ; '.'                                                    ; 8bb0: c9 2e       ..
    bne loop_c8b97                                                    ; 8bb2: d0 e3       ..
    iny                                                               ; 8bb4: c8          .
    dex                                                               ; 8bb5: ca          .
    bcs loop_c8b9b                                                    ; 8bb6: b0 e3       ..
; &8bb8 referenced 1 time by &8b9e
.c8bb8
    pha                                                               ; 8bb8: 48          H
    lda l8bd7,x                                                       ; 8bb9: bd d7 8b    ...
    pha                                                               ; 8bbc: 48          H
    clc                                                               ; 8bbd: 18          .
    tya                                                               ; 8bbe: 98          .
    ldx fs_crc_hi                                                     ; 8bbf: a6 bf       ..
    adc fs_crc_lo                                                     ; 8bc1: 65 be       e.
    sta l0e0b                                                         ; 8bc3: 8d 0b 0e    ...
    sta fs_cmd_ptr                                                    ; 8bc6: 8d 10 0e    ...
    bcc c8bcc                                                         ; 8bc9: 90 01       ..
    inx                                                               ; 8bcb: e8          .
; &8bcc referenced 1 time by &8bc9
.c8bcc
    stx l0e0c                                                         ; 8bcc: 8e 0c 0e    ...
    stx l0e11                                                         ; 8bcf: 8e 11 0e    ...
    stx l0e16                                                         ; 8bd2: 8e 16 0e    ...
    rts                                                               ; 8bd5: 60          `

; FS command match table (COMTAB)
; Format: command letters (bit 7 clear), then dispatch address
; as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
; adds 1 to the stored (address-1). Matching is case-insensitive
; (AND $DF) and supports '.' abbreviation (standard Acorn pattern).
; 
; Entries:
;   "I."     → $8079 (forward_star_cmd) — placed first as a fudge
;              to catch *I. abbreviation before matching *I AM
;   "I AM"   → $8D06 (i_am_handler: parse station.net, logon)
;   "EX "    → $8BF2 (ex_handler: extended catalogue)
;   "EX"\r   → $8BF2 (same, exact match at end of line)
;   "BYE"\r  → $8349 (bye_handler: logoff)
;   <catch-all> → $8079 (forward anything else to FS)
; &8bd6 referenced 2 times by &8b9b, &8ba8
.fs_cmd_match_table
    equb &49                                                          ; 8bd6: 49          I
; &8bd7 referenced 1 time by &8bb9
.l8bd7
    equb &2e, &80                                                     ; 8bd7: 2e 80       ..
    equs "xI AM"                                                      ; 8bd9: 78 49 20... xI
    equb &8d, 5                                                       ; 8bde: 8d 05       ..
    equs "EX "                                                        ; 8be0: 45 58 20    EX
    equb &8b, &f1, &45, &58, &0d, &8b, &f1                            ; 8be3: 8b f1 45... ..E
    equs "BYE"                                                        ; 8bea: 42 59 45    BYE
    equb &0d, &83, &48, &80, &78                                      ; 8bed: 0d 83 48... ..H

; *EX handler (extended catalogue)
; Sets column width $B6=$50 (80 columns, one file per line with
; full details) and $B7=$01, then branches into cat_handler at
; $8C07, bypassing cat_handler's default 20-column setup.
.ex_handler
    dey                                                               ; 8bf2: 88          .
    ldx #1                                                            ; 8bf3: a2 01       ..
    stx l00b7                                                         ; 8bf5: 86 b7       ..
    ldx #&50 ; 'P'                                                    ; 8bf7: a2 50       .P
    stx l00b6                                                         ; 8bf9: 86 b6       ..
    bne c8c07                                                         ; 8bfb: d0 0a       ..             ; ALWAYS branch

; *CAT handler (directory catalogue)
; Sets column width $B6=$14 (20 columns, four files per 80-column
; line) and $B7=$03. The catalogue protocol is multi-step: first
; sends FCUSER ($15: read user environment) to get CSD, disc, and
; library names, then sends FCREAD ($12: examine) repeatedly to
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
;   - Directory entries: CRFLAG ($CF) cycles 0-3 for multi-column
;     layout; at count 0 a newline is printed, others get spaces.
;     *EX sets CRFLAG=$FF to force one entry per line.
.cat_handler
    ldx #&14                                                          ; 8bfd: a2 14       ..
    stx l00b6                                                         ; 8bff: 86 b6       ..
    ldx #3                                                            ; 8c01: a2 03       ..
    stx l00b7                                                         ; 8c03: 86 b7       ..
    ldy #0                                                            ; 8c05: a0 00       ..
; &8c07 referenced 1 time by &8bfb
.c8c07
    lda #6                                                            ; 8c07: a9 06       ..
    sta fs_cmd_data                                                   ; 8c09: 8d 05 0f    ...
    jsr skip_spaces                                                   ; 8c0c: 20 55 85     U.
    sty l00b3                                                         ; 8c0f: 84 b3       ..
    ldx #1                                                            ; 8c11: a2 01       ..
    jsr copy_string_from_offset                                       ; 8c13: 20 67 8d     g.
    ldy #&12                                                          ; 8c16: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c18: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c1b: a2 03       ..
    jsr print_reply_bytes                                             ; 8c1d: 20 4f 8d     O.
    jsr print_inline                                                  ; 8c20: 20 3b 85     ;.
    equs "("                                                          ; 8c23: 28          (

    lda l0f13                                                         ; 8c24: ad 13 0f    ...
    jsr print_decimal                                                 ; 8c27: 20 af 85     ..
    jsr print_inline                                                  ; 8c2a: 20 3b 85     ;.
    equs ")"                                                          ; 8c2d: 29          )

    ldx #5                                                            ; 8c2e: a2 05       ..
    jsr print_spaces                                                  ; 8c30: 20 5c 8d     \.
    ldx l0f12                                                         ; 8c33: ae 12 0f    ...
    bne c8c43                                                         ; 8c36: d0 0b       ..
    jsr print_inline                                                  ; 8c38: 20 3b 85     ;.
    equs "Owner", &0d                                                 ; 8c3b: 4f 77 6e... Own

    bne c8c4d                                                         ; 8c41: d0 0a       ..
; &8c43 referenced 1 time by &8c36
.c8c43
    jsr print_inline                                                  ; 8c43: 20 3b 85     ;.
    equs "Public", &0d                                                ; 8c46: 50 75 62... Pub

; &8c4d referenced 1 time by &8c41
.c8c4d
    ldy #&15                                                          ; 8c4d: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c4f: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8c52: e8          .
    ldy #&10                                                          ; 8c53: a0 10       ..
    jsr print_reply_counted                                           ; 8c55: 20 51 8d     Q.
    ldx #4                                                            ; 8c58: a2 04       ..
    jsr print_spaces                                                  ; 8c5a: 20 5c 8d     \.
    jsr print_inline                                                  ; 8c5d: 20 3b 85     ;.
    equs "Option "                                                    ; 8c60: 4f 70 74... Opt

    lda fs_boot_option                                                ; 8c67: ad 05 0e    ...
    tax                                                               ; 8c6a: aa          .
    jsr print_hex                                                     ; 8c6b: 20 eb 85     ..
    jsr print_inline                                                  ; 8c6e: 20 3b 85     ;.
    equs " ("                                                         ; 8c71: 20 28        (

    ldy option_name_offsets,x                                         ; 8c73: bc 4b 8d    .K.
; &8c76 referenced 1 time by &8c7f
.loop_c8c76
    lda option_name_strings,y                                         ; 8c76: b9 3a 8d    .:.
    beq c8c81                                                         ; 8c79: f0 06       ..
    jsr osasci                                                        ; 8c7b: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8c7e: c8          .
    bne loop_c8c76                                                    ; 8c7f: d0 f5       ..
; &8c81 referenced 1 time by &8c79
.c8c81
    jsr print_inline                                                  ; 8c81: 20 3b 85     ;.
    equs ")", &0d, "Dir. "                                            ; 8c84: 29 0d 44... ).D

    ldx #&11                                                          ; 8c8b: a2 11       ..
    jsr print_reply_bytes                                             ; 8c8d: 20 4f 8d     O.
    ldx #5                                                            ; 8c90: a2 05       ..
    jsr print_spaces                                                  ; 8c92: 20 5c 8d     \.
    jsr print_inline                                                  ; 8c95: 20 3b 85     ;.
    equs "Lib. "                                                      ; 8c98: 4c 69 62... Lib

    ldx #&1b                                                          ; 8c9d: a2 1b       ..
    jsr print_reply_bytes                                             ; 8c9f: 20 4f 8d     O.
    jsr print_inline                                                  ; 8ca2: 20 3b 85     ;.
    equs &0d, &0d                                                     ; 8ca5: 0d 0d       ..

    sty l0f06                                                         ; 8ca7: 8c 06 0f    ...
    sty l00b4                                                         ; 8caa: 84 b4       ..
    txa                                                               ; 8cac: 8a          .
    eor #&ff                                                          ; 8cad: 49 ff       I.
; &8caf referenced 1 time by &8cb3
.loop_c8caf
    sec                                                               ; 8caf: 38          8
    sbc l00b6                                                         ; 8cb0: e5 b6       ..
    iny                                                               ; 8cb2: c8          .
    bcs loop_c8caf                                                    ; 8cb3: b0 fa       ..
    sty l0f07                                                         ; 8cb5: 8c 07 0f    ...
    sty l00b5                                                         ; 8cb8: 84 b5       ..
; &8cba referenced 1 time by &8ce5
.c8cba
    ldy l00b3                                                         ; 8cba: a4 b3       ..
    ldx l00b7                                                         ; 8cbc: a6 b7       ..
    stx fs_cmd_data                                                   ; 8cbe: 8e 05 0f    ...
    ldx #3                                                            ; 8cc1: a2 03       ..
    jsr copy_string_from_offset                                       ; 8cc3: 20 67 8d     g.
    ldy #3                                                            ; 8cc6: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cc8: 20 50 83     P.            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 8ccb: ad 05 0f    ...
    beq c8cff                                                         ; 8cce: f0 2f       ./
    ldx #2                                                            ; 8cd0: a2 02       ..
    jsr print_dir_from_offset                                         ; 8cd2: 20 75 8d     u.
    clc                                                               ; 8cd5: 18          .
    lda l00b4                                                         ; 8cd6: a5 b4       ..
    adc fs_cmd_data                                                   ; 8cd8: 6d 05 0f    m..
    sta l0f06                                                         ; 8cdb: 8d 06 0f    ...
    sta l00b4                                                         ; 8cde: 85 b4       ..
    lda l00b5                                                         ; 8ce0: a5 b5       ..
    sta l0f07                                                         ; 8ce2: 8d 07 0f    ...
    bne c8cba                                                         ; 8ce5: d0 d3       ..
    jmp l212e                                                         ; 8ce7: 4c 2e 21    L.!

; Boot command strings for auto-boot
; The four boot options use OSCLI strings at offsets within page $8C:
;   Option 0 (Off):  offset $F6 → $8CF6 = bare CR (empty command)
;   Option 1 (Load): offset $E7 → $8CE7 = "L.!BOOT" (dual-purpose:
;       the JMP $212E instruction at $8CE7 has opcode $4C='L' and
;       operand bytes $2E='.' $21='!', forming the string "L.!")
;   Option 2 (Run):  offset $E9 → $8CE9 = "!BOOT" (bare filename = *RUN)
;   Option 3 (Exec): offset $EF → $8CEF = "E.!BOOT"
; 
; This is a classic BBC ROM space optimisation: the JMP instruction's
; bytes serve double duty as both executable code and ASCII text.
.boot_cmd_strings
    equs "BOOT"                                                       ; 8cea: 42 4f 4f... BOO
    equb &0d                                                          ; 8cee: 0d          .
    equs "E.!BOOT"                                                    ; 8cef: 45 2e 21... E.!
    equb &0d                                                          ; 8cf6: 0d          .

; Set library handle
; Stores Y into $0E04 (library directory handle in FS workspace).
; Falls through to c8cff (JMP c892c) if Y is non-zero.
.set_lib_handle
    sty fs_lib_handle                                                 ; 8cf7: 8c 04 0e    ...
    bne c8cff                                                         ; 8cfa: d0 03       ..
; Set CSD handle
; Stores Y into $0E03 (current selected directory handle).
; Falls through to c8cff (JMP c892c).
.set_csd_handle
    sty fs_csd_handle                                                 ; 8cfc: 8c 03 0e    ...
; &8cff referenced 3 times by &8cce, &8cfa, &8d2d
.c8cff
    jmp restore_args_return                                           ; 8cff: 4c 2c 89    L,.

; Boot option → OSCLI string offset table
; Four bytes indexed by the boot option value (0-3). Each byte
; is the low byte of a pointer into page $8C, where the OSCLI
; command string for that boot option lives. See boot_cmd_strings.
; &8d02 referenced 1 time by &8d32
.boot_option_offsets
    equb &f6, &e7, &e9, &ef                                           ; 8d02: f6 e7 e9... ...

; "I AM" command handler
; Dispatched from the command match table when the user types
; "*I AM <station>" or "*I AM <station>.<network>".
; Parses the station number (and optional network number after '.')
; using skip_spaces and parse_decimal. Stores the results in:
;   $0E00 = station number (or fileserver station)
;   $0E01 = network number
; Then forwards the command to the fileserver via forward_star_cmd.
.i_am_handler
    jsr skip_spaces                                                   ; 8d06: 20 55 85     U.
    bcs c8d1c                                                         ; 8d09: b0 11       ..
    lda #0                                                            ; 8d0b: a9 00       ..
    jsr parse_decimal                                                 ; 8d0d: 20 60 85     `.            ; Parse decimal number from (fs_options),Y (DECIN)
    bcc c8d16                                                         ; 8d10: 90 04       ..
    iny                                                               ; 8d12: c8          .              ; Y=offset into (fs_options) buffer
    jsr parse_decimal                                                 ; 8d13: 20 60 85     `.            ; Parse decimal number from (fs_options),Y (DECIN)
; &8d16 referenced 1 time by &8d10
.c8d16
    sta fs_server_stn                                                 ; 8d16: 8d 00 0e    ...            ; A=parsed value (accumulated in $B2)
    stx fs_server_net                                                 ; 8d19: 8e 01 0e    ...            ; X=corrupted
; &8d1c referenced 1 time by &8d09
.c8d1c
    jmp forward_star_cmd                                              ; 8d1c: 4c 79 80    Ly.

; Copy FS reply handles to workspace and execute boot command
; SEC entry (LOGIN): copies 4 bytes from $0F05-$0F08 (FS reply) to
; $0E02-$0E05 (URD, CSD, LIB handles and boot option), then
; looks up the boot option in boot_option_offsets to get the
; OSCLI command string and executes it via JMP oscli.
; The carry flag distinguishes LOGIN (SEC) from SDISC (CLC) — both
; share the handle-copying code, but only LOGIN executes the boot
; command. This use of the carry flag to select behaviour between
; two callers avoids duplicating the handle-copy loop.
.copy_handles_and_boot
    sec                                                               ; 8d1f: 38          8
; Copy FS reply handles to workspace (no boot)
; CLC entry (SDISC): copies handles only, then jumps to c8cff.
; Called when the FS reply contains updated handle values
; but no boot action is needed.
.copy_handles
    ldx #3                                                            ; 8d20: a2 03       ..
    bcc c8d2a                                                         ; 8d22: 90 06       ..
; &8d24 referenced 1 time by &8d2b
.loop_c8d24
    lda fs_cmd_data,x                                                 ; 8d24: bd 05 0f    ...
    sta fs_urd_handle,x                                               ; 8d27: 9d 02 0e    ...
; &8d2a referenced 1 time by &8d22
.c8d2a
    dex                                                               ; 8d2a: ca          .
    bpl loop_c8d24                                                    ; 8d2b: 10 f7       ..
    bcc c8cff                                                         ; 8d2d: 90 d0       ..
    ldy fs_boot_option                                                ; 8d2f: ac 05 0e    ...
    ldx boot_option_offsets,y                                         ; 8d32: be 02 8d    ...
    ldy #&8c                                                          ; 8d35: a0 8c       ..
    jmp oscli                                                         ; 8d37: 4c f7 ff    L..

; Option name strings
; Null-terminated strings for the four boot option names:
;   "Off", "Load", "Run", "Exec"
; Used by cat_handler to display the current boot option setting.
; &8d3a referenced 1 time by &8c76
.option_name_strings
    equs "Off"                                                        ; 8d3a: 4f 66 66    Off
    equb 0                                                            ; 8d3d: 00          .
    equs "Load"                                                       ; 8d3e: 4c 6f 61... Loa
    equb 0                                                            ; 8d42: 00          .
    equs "Run"                                                        ; 8d43: 52 75 6e    Run
    equb 0                                                            ; 8d46: 00          .
    equs "Exec"                                                       ; 8d47: 45 78 65... Exe
; Option name offsets
; Four-byte table of offsets into option_name_strings:
;   0, 4, 9, $0D — one per boot option value (0-3).
; &8d4b referenced 1 time by &8c73
.option_name_offsets
    equb 0, 4, 9, &0d                                                 ; 8d4b: 00 04 09... ...

; Print reply buffer bytes
; Prints Y characters from the FS reply buffer ($0F05+X) to
; the screen via OSASCI. X = starting offset, Y = count.
; Used by cat_handler to display directory and library names.
; &8d4f referenced 3 times by &8c1d, &8c8d, &8c9f
.print_reply_bytes
    ldy #&0a                                                          ; 8d4f: a0 0a       ..
; &8d51 referenced 2 times by &8c55, &8d59
.print_reply_counted
    lda fs_cmd_data,x                                                 ; 8d51: bd 05 0f    ...
    jsr osasci                                                        ; 8d54: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8d57: e8          .
    dey                                                               ; 8d58: 88          .
    bne print_reply_counted                                           ; 8d59: d0 f6       ..
    rts                                                               ; 8d5b: 60          `

; Print spaces
; Prints X space characters via print_space. Used by cat_handler
; to align columns in the directory listing.
; &8d5c referenced 4 times by &8c30, &8c5a, &8c92, &8d60
.print_spaces
    jsr print_space                                                   ; 8d5c: 20 40 86     @.
    dex                                                               ; 8d5f: ca          .
    bne print_spaces                                                  ; 8d60: d0 fa       ..
    rts                                                               ; 8d62: 60          `

; Copy filename to FS command buffer
; Entry with X=0: copies from (fs_crc_lo),Y to $0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; &8d63 referenced 3 times by &8079, &86cb, &888a
.copy_filename
    ldx #0                                                            ; 8d63: a2 00       ..
; Copy string to FS command buffer
; Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
; to $0F05+X, stopping when a CR ($0D) is encountered. The CR
; itself is also copied. Returns with X pointing past the last
; byte written.
; &8d65 referenced 4 times by &8779, &8883, &88a5, &8964
.copy_string_to_cmd
    ldy #0                                                            ; 8d65: a0 00       ..
; &8d67 referenced 3 times by &8c13, &8cc3, &8d70
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d67: b1 be       ..
    sta fs_cmd_data,x                                                 ; 8d69: 9d 05 0f    ...
    inx                                                               ; 8d6c: e8          .
    iny                                                               ; 8d6d: c8          .
    eor #&0d                                                          ; 8d6e: 49 0d       I.
    bne copy_string_from_offset                                       ; 8d70: d0 f5       ..
; &8d72 referenced 1 time by &8d78
.return_6
    rts                                                               ; 8d72: 60          `

; Print directory name from reply buffer
; Prints characters from the FS reply buffer ($0F05+X onwards).
; Null bytes ($00) are replaced with CR ($0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by cat_handler to display Dir. and Lib. paths.
.print_dir_name
    ldx #0                                                            ; 8d73: a2 00       ..
; &8d75 referenced 2 times by &8cd2, &8d82
.print_dir_from_offset
    lda fs_cmd_data,x                                                 ; 8d75: bd 05 0f    ...
    bmi return_6                                                      ; 8d78: 30 f8       0.
    bne c8d7e                                                         ; 8d7a: d0 02       ..
    lda #&0d                                                          ; 8d7c: a9 0d       ..
; &8d7e referenced 1 time by &8d7a
.c8d7e
    jsr osasci                                                        ; 8d7e: 20 e3 ff     ..            ; Write character 13
    inx                                                               ; 8d81: e8          .
    bne print_dir_from_offset                                         ; 8d82: d0 f1       ..
; Send FS load-as-command and execute response
; Sets up an FS command with function code $05 (FCCMND: load as
; command) using send_fs_examine. If a Tube co-processor is
; present (tx_in_progress != 0), transfers the response data
; to the Tube via tube_addr_claim. Otherwise jumps via the
; indirect pointer at ($0F09) to execute at the load address.
.notify_and_exec
    ldx #&0e                                                          ; 8d84: a2 0e       ..
    stx fs_block_offset                                               ; 8d86: 86 bc       ..
    lda #&10                                                          ; 8d88: a9 10       ..
    sta fs_options                                                    ; 8d8a: 85 bb       ..
    ldx #&4a ; 'J'                                                    ; 8d8c: a2 4a       .J
    ldy #5                                                            ; 8d8e: a0 05       ..
    jsr send_fs_examine                                               ; 8d90: 20 d0 86     ..
    lda tx_in_progress                                                ; 8d93: ad 52 0d    .R.
    beq c8dac                                                         ; 8d96: f0 14       ..
    adc l0f0b                                                         ; 8d98: 6d 0b 0f    m..
    adc l0f0c                                                         ; 8d9b: 6d 0c 0f    m..
    bcs c8dac                                                         ; 8d9e: b0 0c       ..
    jsr tube_claim_loop                                               ; 8da0: 20 8a 8b     ..
    ldx #9                                                            ; 8da3: a2 09       ..
    ldy #&0f                                                          ; 8da5: a0 0f       ..
    lda #4                                                            ; 8da7: a9 04       ..
    jmp tube_addr_claim                                               ; 8da9: 4c 06 04    L..

; &8dac referenced 2 times by &8d96, &8d9e
.c8dac
    jmp (l0f09)                                                       ; 8dac: 6c 09 0f    l..

; *NET1: read file handle from received packet
; Reads a file handle byte from offset $6F in the RX buffer
; (net_rx_ptr), stores it in $F0, then falls through to the
; common handle workspace cleanup at c8dda (clear fs_temp_ce).
.net1_read_handle
    ldy #&6f ; 'o'                                                    ; 8daf: a0 6f       .o
    lda (net_rx_ptr),y                                                ; 8db1: b1 9c       ..
    sta l00f0                                                         ; 8db3: 85 f0       ..
    bcc c8dda                                                         ; 8db5: 90 23       .#
; Calculate handle workspace offset
; Converts a file handle number (in A) to a byte offset (in Y)
; into the NFS handle workspace. The calculation is A*12:
;   ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
;   ADC stack (A*8 + A*4 = A*12).
; Validates that the offset is < $48 (max 6 handles × 12 bytes
; per handle entry = 72 bytes). If invalid (>= $48), returns
; with C set and Y=0, A=0 as an error indicator.
; &8db7 referenced 5 times by &82b6, &8dcb, &8de1, &8f01, &8f1a
.calc_handle_offset
    asl a                                                             ; 8db7: 0a          .
    asl a                                                             ; 8db8: 0a          .
    pha                                                               ; 8db9: 48          H
    asl a                                                             ; 8dba: 0a          .
    tsx                                                               ; 8dbb: ba          .
    adc l0101,x                                                       ; 8dbc: 7d 01 01    }..
    tay                                                               ; 8dbf: a8          .
    pla                                                               ; 8dc0: 68          h
    cmp #&48 ; 'H'                                                    ; 8dc1: c9 48       .H
    bcc return_7                                                      ; 8dc3: 90 03       ..
    ldy #0                                                            ; 8dc5: a0 00       ..
    tya                                                               ; 8dc7: 98          .              ; A=&00
; &8dc8 referenced 1 time by &8dc3
.return_7
    rts                                                               ; 8dc8: 60          `

; *NET2: read handle entry from workspace
; Looks up the handle in $F0 via calc_handle_offset. If the
; workspace slot contains $3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears fs_temp_ce on exit.
.net2_read_handle_entry
    lda l00f0                                                         ; 8dc9: a5 f0       ..
    jsr calc_handle_offset                                            ; 8dcb: 20 b7 8d     ..
    bcs c8dd6                                                         ; 8dce: b0 06       ..
    lda (nfs_workspace),y                                             ; 8dd0: b1 9e       ..
    cmp #&3f ; '?'                                                    ; 8dd2: c9 3f       .?
    bne c8dd8                                                         ; 8dd4: d0 02       ..
; &8dd6 referenced 2 times by &8dce, &8de4
.c8dd6
    lda #0                                                            ; 8dd6: a9 00       ..
; &8dd8 referenced 1 time by &8dd4
.c8dd8
    sta l00f0                                                         ; 8dd8: 85 f0       ..
; &8dda referenced 3 times by &8db5, &8df0, &8df5
.c8dda
    lda #0                                                            ; 8dda: a9 00       ..
    sta fs_temp_ce                                                    ; 8ddc: 85 ce       ..
    rts                                                               ; 8dde: 60          `

; *NET3: close handle (mark as unused)
; Looks up the handle in $F0 via calc_handle_offset. Writes
; $3F ('?') to mark the handle slot as closed in the NFS
; workspace. Preserves the carry flag state across the write
; using ROL/ROR on rx_status_flags. Clears fs_temp_ce on exit.
.net3_close_handle
    lda l00f0                                                         ; 8ddf: a5 f0       ..
    jsr calc_handle_offset                                            ; 8de1: 20 b7 8d     ..
    bcs c8dd6                                                         ; 8de4: b0 f0       ..
    rol rx_status_flags                                               ; 8de6: 2e 38 0d    .8.
    lda #&3f ; '?'                                                    ; 8de9: a9 3f       .?
    sta (nfs_workspace),y                                             ; 8deb: 91 9e       ..
    ror rx_status_flags                                               ; 8ded: 6e 38 0d    n8.
    bcc c8dda                                                         ; 8df0: 90 e8       ..
; *NET4: resume after remote operation
; Calls resume_after_remote ($8146) to re-enable the keyboard
; and send a completion notification. The BVC always branches
; to c8dda (clear fs_temp_ce) since resume_after_remote
; returns with V clear (from CLV in prepare_cmd_clv).
.net4_resume_remote
    jsr resume_after_remote                                           ; 8df2: 20 46 81     F.
    bvc c8dda                                                         ; 8df5: 50 e3       P.
; Filing system OSWORD entry
; Subtracts $0F from the command code in $EF, giving a 0-4 index
; for OSWORD calls $0F-$13 (15-19). Falls through to the
; PHA/PHA/RTS dispatch at $8E01.
.osword_fs_entry
    lda l00ef                                                         ; 8df7: a5 ef       ..             ; Command code from $EF
    sbc #&0f                                                          ; 8df9: e9 0f       ..             ; Subtract $0F: OSWORD $0F-$13 become indices 0-4
    bmi return_8                                                      ; 8dfb: 30 35       05
    cmp #5                                                            ; 8dfd: c9 05       ..
    bcs return_8                                                      ; 8dff: b0 31       .1
; PHA/PHA/RTS dispatch for filing system OSWORDs
; X = OSWORD number - $0F (0-4). Dispatches via the 5-entry table
; at $8E18 (low) / $8E1D (high).
.fs_osword_dispatch
    tax                                                               ; 8e01: aa          .
    lda fs_osword_tbl_hi,x                                            ; 8e02: bd 1d 8e    ...
    pha                                                               ; 8e05: 48          H
    lda fs_osword_tbl_lo,x                                            ; 8e06: bd 18 8e    ...
    pha                                                               ; 8e09: 48          H
    ldy #2                                                            ; 8e0a: a0 02       ..
; &8e0c referenced 1 time by &8e12
.loop_c8e0c
    lda fs_last_byte_flag,y                                           ; 8e0c: b9 bd 00    ...
    sta (net_rx_ptr),y                                                ; 8e0f: 91 9c       ..
    dey                                                               ; 8e11: 88          .
    bpl loop_c8e0c                                                    ; 8e12: 10 f8       ..
    iny                                                               ; 8e14: c8          .
    lda (l00f0),y                                                     ; 8e15: b1 f0       ..
    rts                                                               ; 8e17: 60          `

; &8e18 referenced 1 time by &8e06
.fs_osword_tbl_lo
    equb <(osword_0f_handler-1)                                       ; 8e18: 32          2              ; Dispatch table: low bytes for OSWORD $0F-$13 handlers
    equb <(osword_10_handler-1)                                       ; 8e19: ef          .
    equb <(osword_11_handler-1)                                       ; 8e1a: 52          R
    equb <(osword_12_handler-1)                                       ; 8e1b: 7a          z
    equb <(econet_tx_rx-1)                                            ; 8e1c: 71          q
; &8e1d referenced 1 time by &8e02
.fs_osword_tbl_hi
    equb >(osword_0f_handler-1)                                       ; 8e1d: 8e          .              ; Dispatch table: high bytes for OSWORD $0F-$13 handlers
    equb >(osword_10_handler-1)                                       ; 8e1e: 8e          .
    equb >(osword_11_handler-1)                                       ; 8e1f: 8e          .
    equb >(osword_12_handler-1)                                       ; 8e20: 8e          .
    equb >(econet_tx_rx-1)                                            ; 8e21: 8f          .

; Bidirectional block copy between OSWORD param block and workspace.
; C=1: copy X+1 bytes from ($F0),Y to (fs_crc_lo),Y (param to workspace)
; C=0: copy X+1 bytes from (fs_crc_lo),Y to ($F0),Y (workspace to param)
; &8e22 referenced 5 times by &8e30, &8e46, &8e62, &8e96, &8f31
.copy_param_block
    bcc c8e2a                                                         ; 8e22: 90 06       ..
    lda (l00f0),y                                                     ; 8e24: b1 f0       ..
    sta (fs_crc_lo),y                                                 ; 8e26: 91 be       ..
    bcs c8e2e                                                         ; 8e28: b0 04       ..             ; ALWAYS branch

; &8e2a referenced 1 time by &8e22
.c8e2a
    lda (fs_crc_lo),y                                                 ; 8e2a: b1 be       ..
    sta (l00f0),y                                                     ; 8e2c: 91 f0       ..
; &8e2e referenced 1 time by &8e28
.c8e2e
    iny                                                               ; 8e2e: c8          .
    dex                                                               ; 8e2f: ca          .
    bpl copy_param_block                                              ; 8e30: 10 f0       ..
; &8e32 referenced 2 times by &8dfb, &8dff
.return_8
    rts                                                               ; 8e32: 60          `

; ***************************************************************************************
; OSWORD $0F handler: initiate transmit (CALLTX)
; 
; Checks the TX semaphore (TXCLR at $0D62) via ASL -- if carry is
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
;     Y: $FF
; ***************************************************************************************
.osword_0f_handler
    asl tx_ctrl_status                                                ; 8e33: 0e 3a 0d    .:.
    bcc c8e4f                                                         ; 8e36: 90 17       ..
    lda net_rx_ptr_hi                                                 ; 8e38: a5 9d       ..
    sta fs_crc_hi                                                     ; 8e3a: 85 bf       ..
    sta nmi_tx_block_hi                                               ; 8e3c: 85 a1       ..
    lda #&6f ; 'o'                                                    ; 8e3e: a9 6f       .o
    sta fs_crc_lo                                                     ; 8e40: 85 be       ..
    sta nmi_tx_block                                                  ; 8e42: 85 a0       ..
    ldx #&0f                                                          ; 8e44: a2 0f       ..
    jsr copy_param_block                                              ; 8e46: 20 22 8e     ".
    jsr trampoline_tx_setup                                           ; 8e49: 20 60 96     `.
    jmp c8f48                                                         ; 8e4c: 4c 48 8f    LH.

; &8e4f referenced 1 time by &8e36
.c8e4f
    sec                                                               ; 8e4f: 38          8
    tya                                                               ; 8e50: 98          .
    bcs c8e75                                                         ; 8e51: b0 22       ."             ; ALWAYS branch

; OSWORD $11 handler: read JSR arguments (READRA)
; Copies the JSR (remote procedure call) argument buffer from the
; static workspace page back to the caller's OSWORD parameter block.
; Reads the buffer size from workspace offset JSRSIZ, then copies
; that many bytes. After the copy, clears the old LSTAT byte via
; CLRJSR to reset the protection status. Also provides READRB as
; a sub-entry ($8E6A) to return just the buffer size and args size
; without copying the data.
.osword_11_handler
    lda net_rx_ptr_hi                                                 ; 8e53: a5 9d       ..
    sta fs_crc_hi                                                     ; 8e55: 85 bf       ..
    ldy #&7f                                                          ; 8e57: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8e59: b1 9c       ..
    iny                                                               ; 8e5b: c8          .              ; Y=&80
    sty fs_crc_lo                                                     ; 8e5c: 84 be       ..
    tax                                                               ; 8e5e: aa          .
    dex                                                               ; 8e5f: ca          .
    ldy #0                                                            ; 8e60: a0 00       ..
    jsr copy_param_block                                              ; 8e62: 20 22 8e     ".
    jsr clear_jsr_protection                                          ; 8e65: 20 d6 92     ..
    bcc c8eac                                                         ; 8e68: 90 42       .B
; &8e6a referenced 1 time by &8ebd
.read_args_size
    ldy #&7f                                                          ; 8e6a: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8e6c: b1 9c       ..
    ldy #1                                                            ; 8e6e: a0 01       ..
    sta (l00f0),y                                                     ; 8e70: 91 f0       ..
    iny                                                               ; 8e72: c8          .              ; Y=&02
    lda #&80                                                          ; 8e73: a9 80       ..
; &8e75 referenced 1 time by &8e51
.c8e75
    sta (l00f0),y                                                     ; 8e75: 91 f0       ..
    bcs c8ee1                                                         ; 8e77: b0 68       .h
; &8e79 referenced 1 time by &8e8d
.l8e79
    equb &ff, 1                                                       ; 8e79: ff 01       ..

; OSWORD $12 handler: read/set state information (RS)
; Dispatches on the sub-function code (0-9):
;   0: read FS station (FSLOCN at $0E00)
;   1: set FS station
;   2: read printer server station (PSLOCN)
;   3: set printer server station
;   4: read protection masks (LSTAT at $D63)
;   5: set protection masks
;   6: read context handles (URD/CSD/LIB, converted from
;      internal single-bit form back to handle numbers)
;   7: set context handles (converted to internal form)
;   8: read local station number
;   9: read JSR arguments buffer size
; Even-numbered sub-functions read; odd-numbered ones write.
; Uses the bidirectional copy at $8E22 for station read/set.
.osword_12_handler
    cmp #6                                                            ; 8e7b: c9 06       ..
    bcs c8eb7                                                         ; 8e7d: b0 38       .8
    cmp #4                                                            ; 8e7f: c9 04       ..
    bcs c8e9b                                                         ; 8e81: b0 18       ..
    lsr a                                                             ; 8e83: 4a          J
    ldx #&0d                                                          ; 8e84: a2 0d       ..
    tay                                                               ; 8e86: a8          .
    beq c8e8b                                                         ; 8e87: f0 02       ..
    ldx nfs_workspace_hi                                              ; 8e89: a6 9f       ..
; &8e8b referenced 1 time by &8e87
.c8e8b
    stx fs_crc_hi                                                     ; 8e8b: 86 bf       ..
    lda l8e79,y                                                       ; 8e8d: b9 79 8e    .y.
    sta fs_crc_lo                                                     ; 8e90: 85 be       ..
    ldx #1                                                            ; 8e92: a2 01       ..
    ldy #1                                                            ; 8e94: a0 01       ..
    jsr copy_param_block                                              ; 8e96: 20 22 8e     ".
    bne c8eac                                                         ; 8e99: d0 11       ..
; &8e9b referenced 1 time by &8e81
.c8e9b
    lsr a                                                             ; 8e9b: 4a          J
    iny                                                               ; 8e9c: c8          .
    lda (l00f0),y                                                     ; 8e9d: b1 f0       ..
    bcs c8ea6                                                         ; 8e9f: b0 05       ..
    lda prot_status                                                   ; 8ea1: ad 63 0d    .c.
    sta (l00f0),y                                                     ; 8ea4: 91 f0       ..
; &8ea6 referenced 1 time by &8e9f
.c8ea6
    sta prot_status                                                   ; 8ea6: 8d 63 0d    .c.
    sta rx_ctrl_copy                                                  ; 8ea9: 8d 3b 0d    .;.
; &8eac referenced 2 times by &8e68, &8e99
.c8eac
    sec                                                               ; 8eac: 38          8
    bcs c8ee1                                                         ; 8ead: b0 32       .2             ; ALWAYS branch

; &8eaf referenced 1 time by &8eb9
.loop_c8eaf
    lda tx_clear_flag                                                 ; 8eaf: ad 62 0d    .b.
    iny                                                               ; 8eb2: c8          .
    sta (l00f0),y                                                     ; 8eb3: 91 f0       ..
    bcs c8ee1                                                         ; 8eb5: b0 2a       .*
; &8eb7 referenced 1 time by &8e7d
.c8eb7
    cmp #8                                                            ; 8eb7: c9 08       ..
    beq loop_c8eaf                                                    ; 8eb9: f0 f4       ..
    cmp #9                                                            ; 8ebb: c9 09       ..
    beq read_args_size                                                ; 8ebd: f0 ab       ..
    bpl c8edb                                                         ; 8ebf: 10 1a       ..
    ldy #3                                                            ; 8ec1: a0 03       ..
    lsr a                                                             ; 8ec3: 4a          J
    bcc c8ee3                                                         ; 8ec4: 90 1d       ..
    sty fs_temp_cd                                                    ; 8ec6: 84 cd       ..
; &8ec8 referenced 1 time by &8ed7
.loop_c8ec8
    ldy fs_temp_cd                                                    ; 8ec8: a4 cd       ..
    lda (l00f0),y                                                     ; 8eca: b1 f0       ..
    jsr handle_to_mask_a                                              ; 8ecc: 20 88 85     ..
    tya                                                               ; 8ecf: 98          .
    ldy fs_temp_cd                                                    ; 8ed0: a4 cd       ..
    sta fs_server_net,y                                               ; 8ed2: 99 01 0e    ...
    dec fs_temp_cd                                                    ; 8ed5: c6 cd       ..
    bne loop_c8ec8                                                    ; 8ed7: d0 ef       ..
    beq c8f48                                                         ; 8ed9: f0 6d       .m             ; ALWAYS branch

; &8edb referenced 1 time by &8ebf
.c8edb
    iny                                                               ; 8edb: c8          .
    lda fs_last_error                                                 ; 8edc: ad 09 0e    ...
    sta (l00f0),y                                                     ; 8edf: 91 f0       ..
; &8ee1 referenced 3 times by &8e77, &8ead, &8eb5
.c8ee1
    bcs c8f48                                                         ; 8ee1: b0 65       .e
; &8ee3 referenced 2 times by &8ec4, &8eec
.c8ee3
    lda fs_server_net,y                                               ; 8ee3: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8ee6: 20 a5 85     ..            ; Convert bitmask to handle number (FS2A)
    sta (l00f0),y                                                     ; 8ee9: 91 f0       ..             ; A=handle number ($20-$27); Y=preserved
    dey                                                               ; 8eeb: 88          .              ; Y=parameter block address high byte
    bne c8ee3                                                         ; 8eec: d0 f5       ..
    beq c8f48                                                         ; 8eee: f0 58       .X             ; ALWAYS branch

; ***************************************************************************************
; OSWORD $10 handler: open/read RX control block (OPENRX)
; 
; If the first byte of the caller's parameter block is zero, scans
; for a free RXCB (flag byte = $3F = deleted) starting from RXCB #3
; (RXCBs 0-2 are dedicated: printer, remote, FS). Returns the RXCB
; number in the first byte, or zero if none free. If the first byte
; is non-zero, reads the specified RXCB's data back into the caller's
; parameter block (12 bytes) and then deletes the RXCB by setting
; its flag byte to $3F -- a consume-once semantic so user code reads
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
;     Y: $FF
; ***************************************************************************************
.osword_10_handler
    ldx nfs_workspace_hi                                              ; 8ef0: a6 9f       ..
    stx fs_crc_hi                                                     ; 8ef2: 86 bf       ..
    sty fs_crc_lo                                                     ; 8ef4: 84 be       ..
    ror rx_status_flags                                               ; 8ef6: 6e 38 0d    n8.
    lda (l00f0),y                                                     ; 8ef9: b1 f0       ..
    sta fs_last_byte_flag                                             ; 8efb: 85 bd       ..
    bne c8f1a                                                         ; 8efd: d0 1b       ..
    lda #3                                                            ; 8eff: a9 03       ..
; &8f01 referenced 1 time by &8f13
.loop_c8f01
    jsr calc_handle_offset                                            ; 8f01: 20 b7 8d     ..
    bcs c8f43                                                         ; 8f04: b0 3d       .=
    lsr a                                                             ; 8f06: 4a          J
    lsr a                                                             ; 8f07: 4a          J
    tax                                                               ; 8f08: aa          .
    lda (fs_crc_lo),y                                                 ; 8f09: b1 be       ..
    beq c8f43                                                         ; 8f0b: f0 36       .6
    cmp #&3f ; '?'                                                    ; 8f0d: c9 3f       .?
    beq c8f15                                                         ; 8f0f: f0 04       ..
    inx                                                               ; 8f11: e8          .
    txa                                                               ; 8f12: 8a          .
    bne loop_c8f01                                                    ; 8f13: d0 ec       ..
; &8f15 referenced 1 time by &8f0f
.c8f15
    txa                                                               ; 8f15: 8a          .
    ldx #0                                                            ; 8f16: a2 00       ..
    sta (l00f0,x)                                                     ; 8f18: 81 f0       ..
; &8f1a referenced 1 time by &8efd
.c8f1a
    jsr calc_handle_offset                                            ; 8f1a: 20 b7 8d     ..
    bcs c8f43                                                         ; 8f1d: b0 24       .$
    dey                                                               ; 8f1f: 88          .
    sty fs_crc_lo                                                     ; 8f20: 84 be       ..
    lda #&c0                                                          ; 8f22: a9 c0       ..
    ldy #1                                                            ; 8f24: a0 01       ..
    ldx #&0b                                                          ; 8f26: a2 0b       ..
    cpy fs_last_byte_flag                                             ; 8f28: c4 bd       ..
    adc (fs_crc_lo),y                                                 ; 8f2a: 71 be       q.
    beq c8f31                                                         ; 8f2c: f0 03       ..
    bmi c8f3e                                                         ; 8f2e: 30 0e       0.
; &8f30 referenced 1 time by &8f40
.loop_c8f30
    clc                                                               ; 8f30: 18          .
; &8f31 referenced 1 time by &8f2c
.c8f31
    jsr copy_param_block                                              ; 8f31: 20 22 8e     ".
    bcs c8f45                                                         ; 8f34: b0 0f       ..
    lda #&3f ; '?'                                                    ; 8f36: a9 3f       .?
    ldy #1                                                            ; 8f38: a0 01       ..
    sta (fs_crc_lo),y                                                 ; 8f3a: 91 be       ..
    bne c8f45                                                         ; 8f3c: d0 07       ..             ; ALWAYS branch

; &8f3e referenced 1 time by &8f2e
.c8f3e
    adc #1                                                            ; 8f3e: 69 01       i.
    bne loop_c8f30                                                    ; 8f40: d0 ee       ..
    dey                                                               ; 8f42: 88          .
; &8f43 referenced 3 times by &8f04, &8f0b, &8f1d
.c8f43
    sta (l00f0),y                                                     ; 8f43: 91 f0       ..
; &8f45 referenced 2 times by &8f34, &8f3c
.c8f45
    rol rx_status_flags                                               ; 8f45: 2e 38 0d    .8.
; &8f48 referenced 6 times by &8e4c, &8ed9, &8ee1, &8eee, &8fbe, &9004
.c8f48
    ldy #0                                                            ; 8f48: a0 00       ..
    sty fs_temp_ce                                                    ; 8f4a: 84 ce       ..
    ldy #2                                                            ; 8f4c: a0 02       ..
; &8f4e referenced 1 time by &8f54
.loop_c8f4e
    lda (net_rx_ptr),y                                                ; 8f4e: b1 9c       ..
    sta fs_last_byte_flag,y                                           ; 8f50: 99 bd 00    ...
    dey                                                               ; 8f53: 88          .
    bpl loop_c8f4e                                                    ; 8f54: 10 f8       ..
    rts                                                               ; 8f56: 60          `

; Set up RX buffer pointers in NFS workspace
; Calculates the start address of the RX data area ($F0+1) and stores
; it at workspace offset $28. Also reads the data length from ($F0)+1
; and adds it to $F0 to compute the end address at offset $2C.
; &8f57 referenced 1 time by &8f8a
.setup_rx_buffer_ptrs
    ldy #&28 ; '('                                                    ; 8f57: a0 28       .(
    lda l00f0                                                         ; 8f59: a5 f0       ..
    adc #1                                                            ; 8f5b: 69 01       i.
    jsr store_16bit_at_y                                              ; 8f5d: 20 68 8f     h.
    ldy #1                                                            ; 8f60: a0 01       ..
    lda (l00f0),y                                                     ; 8f62: b1 f0       ..
    ldy #&2c ; ','                                                    ; 8f64: a0 2c       .,
    adc l00f0                                                         ; 8f66: 65 f0       e.
; &8f68 referenced 1 time by &8f5d
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8f68: 91 9e       ..
    iny                                                               ; 8f6a: c8          .
    lda l00f1                                                         ; 8f6b: a5 f1       ..
    adc #0                                                            ; 8f6d: 69 00       i.
    sta (nfs_workspace),y                                             ; 8f6f: 91 9e       ..
    rts                                                               ; 8f71: 60          `

; Econet transmit/receive handler
; A=0: Initialise TX control block from ROM template at $8310
;      (zero entries substituted from NMI workspace $0DDA), transmit
;      it, set up RX control block, and receive reply.
; A>=1: Handle transmit result (branch to cleanup at $8F48).
.econet_tx_rx
    cmp #1                                                            ; 8f72: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs c8fc0                                                         ; 8f74: b0 4a       .J
    ldy #&2f ; '/'                                                    ; 8f76: a0 2f       ./
; &8f78 referenced 1 time by &8f85
.loop_c8f78
    lda init_tx_ctrl_port,y                                           ; 8f78: b9 10 83    ...            ; Load from ROM template (zero = use NMI workspace value)
    bne c8f80                                                         ; 8f7b: d0 03       ..
    lda l0dda,y                                                       ; 8f7d: b9 da 0d    ...
; &8f80 referenced 1 time by &8f7b
.c8f80
    sta (nfs_workspace),y                                             ; 8f80: 91 9e       ..
    dey                                                               ; 8f82: 88          .
    cpy #&23 ; '#'                                                    ; 8f83: c0 23       .#
    bne loop_c8f78                                                    ; 8f85: d0 f1       ..
    iny                                                               ; 8f87: c8          .
    sty net_tx_ptr                                                    ; 8f88: 84 9a       ..
    jsr setup_rx_buffer_ptrs                                          ; 8f8a: 20 57 8f     W.
    ldy #2                                                            ; 8f8d: a0 02       ..
    lda #&90                                                          ; 8f8f: a9 90       ..
    sta (l00f0),y                                                     ; 8f91: 91 f0       ..
    iny                                                               ; 8f93: c8          .              ; Y=&03
    iny                                                               ; 8f94: c8          .              ; Y=&04
; &8f95 referenced 1 time by &8f9d
.loop_c8f95
    lda l0dfe,y                                                       ; 8f95: b9 fe 0d    ...
    sta (l00f0),y                                                     ; 8f98: 91 f0       ..
    iny                                                               ; 8f9a: c8          .
    cpy #7                                                            ; 8f9b: c0 07       ..
    bne loop_c8f95                                                    ; 8f9d: d0 f6       ..
    lda nfs_workspace_hi                                              ; 8f9f: a5 9f       ..
    sta net_tx_ptr_hi                                                 ; 8fa1: 85 9b       ..
    cli                                                               ; 8fa3: 58          X              ; Enable interrupts before transmit
    jsr tx_poll_timeout                                               ; 8fa4: 20 4e 86     N.
    ldy #&2c ; ','                                                    ; 8fa7: a0 2c       .,
    lda #&ff                                                          ; 8fa9: a9 ff       ..             ; Dest station = $FFFF (accept reply from any station)
    sta (nfs_workspace),y                                             ; 8fab: 91 9e       ..
    iny                                                               ; 8fad: c8          .              ; Y=&2d
    sta (nfs_workspace),y                                             ; 8fae: 91 9e       ..
    ldy #&25 ; '%'                                                    ; 8fb0: a0 25       .%
    lda #&90                                                          ; 8fb2: a9 90       ..
    sta (nfs_workspace),y                                             ; 8fb4: 91 9e       ..
    dey                                                               ; 8fb6: 88          .              ; Y=&24
    lda #&7f                                                          ; 8fb7: a9 7f       ..
    sta (nfs_workspace),y                                             ; 8fb9: 91 9e       ..
    jsr send_to_fs_star                                               ; 8fbb: 20 48 84     H.            ; Initiate receive with timeout
    bne c8f48                                                         ; 8fbe: d0 88       ..             ; Non-zero = error/timeout: jump to cleanup
; &8fc0 referenced 1 time by &8f74
.c8fc0
    php                                                               ; 8fc0: 08          .
    ldy #1                                                            ; 8fc1: a0 01       ..
    lda (l00f0),y                                                     ; 8fc3: b1 f0       ..
    tax                                                               ; 8fc5: aa          .
    iny                                                               ; 8fc6: c8          .              ; Y=&02
    lda (l00f0),y                                                     ; 8fc7: b1 f0       ..
    iny                                                               ; 8fc9: c8          .              ; Y=&03
    sty fs_crc_lo                                                     ; 8fca: 84 be       ..
    ldy #&72 ; 'r'                                                    ; 8fcc: a0 72       .r
    sta (net_rx_ptr),y                                                ; 8fce: 91 9c       ..
    dey                                                               ; 8fd0: 88          .              ; Y=&71
    txa                                                               ; 8fd1: 8a          .
    sta (net_rx_ptr),y                                                ; 8fd2: 91 9c       ..
    plp                                                               ; 8fd4: 28          (
    bne c8ff5                                                         ; 8fd5: d0 1e       ..
; &8fd7 referenced 1 time by &8ff1
.loop_c8fd7
    ldy fs_crc_lo                                                     ; 8fd7: a4 be       ..             ; Receive data blocks until command byte = $00 or $0D
    inc fs_crc_lo                                                     ; 8fd9: e6 be       ..
    lda (l00f0),y                                                     ; 8fdb: b1 f0       ..
    ldy #&7d ; '}'                                                    ; 8fdd: a0 7d       .}
    sta (net_rx_ptr),y                                                ; 8fdf: 91 9c       ..
    pha                                                               ; 8fe1: 48          H
    jsr ctrl_block_setup_alt                                          ; 8fe2: 20 59 91     Y.
    cli                                                               ; 8fe5: 58          X
    jsr tx_poll_core                                                  ; 8fe6: 20 50 86     P.            ; Core transmit and poll routine (XMIT)
; &8fe9 referenced 1 time by &8fea
.loop_c8fe9
    dex                                                               ; 8fe9: ca          .
    bne loop_c8fe9                                                    ; 8fea: d0 fd       ..
    pla                                                               ; 8fec: 68          h
    beq c8ff3                                                         ; 8fed: f0 04       ..
    eor #&0d                                                          ; 8fef: 49 0d       I.             ; Test for end-of-data marker ($0D)
    bne loop_c8fd7                                                    ; 8ff1: d0 e4       ..
; &8ff3 referenced 1 time by &8fed
.c8ff3
    beq c9004                                                         ; 8ff3: f0 0f       ..
; &8ff5 referenced 1 time by &8fd5
.c8ff5
    jsr ctrl_block_setup_alt                                          ; 8ff5: 20 59 91     Y.
    ldy #&7b ; '{'                                                    ; 8ff8: a0 7b       .{
    lda (net_rx_ptr),y                                                ; 8ffa: b1 9c       ..
    adc #3                                                            ; 8ffc: 69 03       i.
    sta (net_rx_ptr),y                                                ; 8ffe: 91 9c       ..
    cli                                                               ; 9000: 58          X
    jsr tx_poll_ff                                                    ; 9001: 20 4c 86     L.
; &9004 referenced 1 time by &8ff3
.c9004
    jmp c8f48                                                         ; 9004: 4c 48 8f    LH.

; ***************************************************************************************
; NETVEC dispatch handler (ENTRY)
; 
; Indirected from NETVEC at $0224. Saves all registers and flags,
; retrieves the reason code from the stacked A, and dispatches to
; one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
; $9020. Reason codes >= 9 are ignored.
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
    php                                                               ; 9007: 08          .
    pha                                                               ; 9008: 48          H
    txa                                                               ; 9009: 8a          .
    pha                                                               ; 900a: 48          H
    tya                                                               ; 900b: 98          .
    pha                                                               ; 900c: 48          H
    tsx                                                               ; 900d: ba          .
    lda l0103,x                                                       ; 900e: bd 03 01    ...            ; Retrieve original A (function code) from stack
    cmp #9                                                            ; 9011: c9 09       ..
    bcs c9019                                                         ; 9013: b0 04       ..
    tax                                                               ; 9015: aa          .
    jsr osword_trampoline                                             ; 9016: 20 20 90      .
; &9019 referenced 1 time by &9013
.c9019
    pla                                                               ; 9019: 68          h
    tay                                                               ; 901a: a8          .
    pla                                                               ; 901b: 68          h
    tax                                                               ; 901c: aa          .
    pla                                                               ; 901d: 68          h
    plp                                                               ; 901e: 28          (
    rts                                                               ; 901f: 60          `

; &9020 referenced 1 time by &9016
.osword_trampoline
    lda osword_tbl_hi,x                                               ; 9020: bd 34 90    .4.            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 9023: 48          H
    lda osword_tbl_lo,x                                               ; 9024: bd 2b 90    .+.
    pha                                                               ; 9027: 48          H
    lda l00ef                                                         ; 9028: a5 ef       ..
    rts                                                               ; 902a: 60          `

; &902b referenced 1 time by &9024
.osword_tbl_lo
    equb <(return_2-1)                                                ; 902b: 44          D
    equb <(remote_print_handler-1)                                    ; 902c: c6          .
    equb <(remote_print_handler-1)                                    ; 902d: c6          .
    equb <(remote_print_handler-1)                                    ; 902e: c6          .
    equb <(net_write_char-1)                                          ; 902f: 3c          <
    equb <(remote_display_setup-1)                                    ; 9030: b4          .
    equb <(return_2-1)                                                ; 9031: 44          D
    equb <(remote_cmd_dispatch-1)                                     ; 9032: 62          b
    equb <(remote_cmd_data-1)                                         ; 9033: cc          .
; &9034 referenced 1 time by &9020
.osword_tbl_hi
    equb >(return_2-1)                                                ; 9034: 81          .
    equb >(remote_print_handler-1)                                    ; 9035: 91          .
    equb >(remote_print_handler-1)                                    ; 9036: 91          .
    equb >(remote_print_handler-1)                                    ; 9037: 91          .
    equb >(net_write_char-1)                                          ; 9038: 90          .
    equb >(remote_display_setup-1)                                    ; 9039: 91          .
    equb >(return_2-1)                                                ; 903a: 81          .
    equb >(remote_cmd_dispatch-1)                                     ; 903b: 90          .
    equb >(remote_cmd_data-1)                                         ; 903c: 90          .

; ***************************************************************************************
; Fn 4: net write character (NWRCH)
; 
; Writes a character (passed in Y) to the screen via OSWRITCH.
; Before the write, uses TSX to reach into the stack and zero the
; carry flag in the caller's saved processor status byte -- ROR
; followed by ASL on the stacked P byte ($0106,X) shifts carry
; out and back in as zero. This ensures the calling code's PLP
; restores carry=0, signalling "character accepted" without needing
; a separate CLC/PHP sequence. A classic 6502 trick for modifying
; return flags without touching the actual processor status.
; 
; On Entry:
;     Y: character to write
; 
; On Exit:
;     A: $3F
;     X: 0
;     Y: 0
; ***************************************************************************************
.net_write_char
    tsx                                                               ; 903d: ba          .
    ror l0106,x                                                       ; 903e: 7e 06 01    ~..            ; ROR/ASL on stacked P: zeros carry to signal success
    asl l0106,x                                                       ; 9041: 1e 06 01    ...
    tya                                                               ; 9044: 98          .
    ldy #&da                                                          ; 9045: a0 da       ..
    sta (nfs_workspace),y                                             ; 9047: 91 9e       ..
    lda #0                                                            ; 9049: a9 00       ..
; Set up TX control block and send
; Builds a TX control block at (nfs_workspace)+$0C from the current
; workspace state, then initiates transmission via the ADLC TX path.
; This is the common send routine used after command data has been
; prepared. The exact control block layout and field mapping need
; further analysis.
; &904b referenced 3 times by &8159, &9092, &90f3
.setup_tx_and_send
    ldy #&d9                                                          ; 904b: a0 d9       ..
    sta (nfs_workspace),y                                             ; 904d: 91 9e       ..
    lda #&80                                                          ; 904f: a9 80       ..
    ldy #&0c                                                          ; 9051: a0 0c       ..
    sta (nfs_workspace),y                                             ; 9053: 91 9e       ..
    sty net_tx_ptr                                                    ; 9055: 84 9a       ..
    ldx nfs_workspace_hi                                              ; 9057: a6 9f       ..
    stx net_tx_ptr_hi                                                 ; 9059: 86 9b       ..
    jsr tx_poll_ff                                                    ; 905b: 20 4c 86     L.
    lda #&3f ; '?'                                                    ; 905e: a9 3f       .?
    sta (net_tx_ptr,x)                                                ; 9060: 81 9a       ..
    rts                                                               ; 9062: 60          `

; Fn 7: remote OSBYTE handler (NBYTE)
; Full RPC mechanism for OSBYTE calls across the network. When a
; machine is remoted, OSBYTE/OSWORD calls that affect terminal-side
; hardware (keyboard scanning, flash rates, etc.) must be indirected
; across the net. OSBYTE calls are classified into three categories:
;   Y>0 (NCTBPL table): executed on BOTH machines (flash rates etc.)
;   Y<0 (NCTBMI table): executed on terminal only, result sent back
;   Y=0: not recognised, passed through unhandled
; Results returned via stack manipulation: the saved processor status
; byte at $0106 has V-flag (bit 6) forced on to tell the MOS the
; call was claimed (preventing dispatch to other ROMs), and the I-bit
; (bit 2) forced on to disable interrupts during register restoration,
; preventing race conditions. The carry flag in the saved P is also
; manipulated via ROR/ASL to zero it, signaling success to the caller.
; OSBYTE $81 (INKEY) gets special handling as it must read the
; terminal's keyboard.
.remote_cmd_dispatch
    ldy l00f1                                                         ; 9063: a4 f1       ..
    cmp #&81                                                          ; 9065: c9 81       ..
    beq c907c                                                         ; 9067: f0 13       ..
    ldy #1                                                            ; 9069: a0 01       ..
    ldx #7                                                            ; 906b: a2 07       ..
    jsr match_osbyte_code                                             ; 906d: 20 b5 90     ..
    beq c907c                                                         ; 9070: f0 0a       ..
    dey                                                               ; 9072: 88          .
    dey                                                               ; 9073: 88          .
    ldx #&0e                                                          ; 9074: a2 0e       ..
    jsr match_osbyte_code                                             ; 9076: 20 b5 90     ..
    beq c907c                                                         ; 9079: f0 01       ..
    iny                                                               ; 907b: c8          .
; &907c referenced 3 times by &9067, &9070, &9079
.c907c
    ldx #2                                                            ; 907c: a2 02       ..
    tya                                                               ; 907e: 98          .
    beq return_9                                                      ; 907f: f0 33       .3
    php                                                               ; 9081: 08          .
    bpl c9085                                                         ; 9082: 10 01       ..
    inx                                                               ; 9084: e8          .              ; X=&03
; &9085 referenced 1 time by &9082
.c9085
    ldy #&dc                                                          ; 9085: a0 dc       ..
; &9087 referenced 1 time by &908f
.loop_c9087
    lda l0015,y                                                       ; 9087: b9 15 00    ...
    sta (nfs_workspace),y                                             ; 908a: 91 9e       ..
    dey                                                               ; 908c: 88          .
    cpy #&da                                                          ; 908d: c0 da       ..
    bpl loop_c9087                                                    ; 908f: 10 f6       ..
    txa                                                               ; 9091: 8a          .
    jsr setup_tx_and_send                                             ; 9092: 20 4b 90     K.
    plp                                                               ; 9095: 28          (
    bpl return_9                                                      ; 9096: 10 1c       ..
    lda #&7f                                                          ; 9098: a9 7f       ..
    sta (net_tx_ptr,x)                                                ; 909a: 81 9a       ..
; &909c referenced 1 time by &909e
.loop_c909c
    lda (net_tx_ptr,x)                                                ; 909c: a1 9a       ..
    bpl loop_c909c                                                    ; 909e: 10 fc       ..
    tsx                                                               ; 90a0: ba          .
    ldy #&dd                                                          ; 90a1: a0 dd       ..
    lda (nfs_workspace),y                                             ; 90a3: b1 9e       ..
    ora #&44 ; 'D'                                                    ; 90a5: 09 44       .D
    bne c90ad                                                         ; 90a7: d0 04       ..             ; ALWAYS branch

; &90a9 referenced 1 time by &90b2
.loop_c90a9
    dey                                                               ; 90a9: 88          .
    dex                                                               ; 90aa: ca          .
    lda (nfs_workspace),y                                             ; 90ab: b1 9e       ..
; &90ad referenced 1 time by &90a7
.c90ad
    sta l0106,x                                                       ; 90ad: 9d 06 01    ...
    cpy #&da                                                          ; 90b0: c0 da       ..
    bne loop_c90a9                                                    ; 90b2: d0 f5       ..
; &90b4 referenced 2 times by &907f, &9096
.return_9
    rts                                                               ; 90b4: 60          `

; &90b5 referenced 3 times by &906d, &9076, &90bb
.match_osbyte_code
    cmp l90be,x                                                       ; 90b5: dd be 90    ...
    beq return_10                                                     ; 90b8: f0 03       ..
    dex                                                               ; 90ba: ca          .
    bpl match_osbyte_code                                             ; 90bb: 10 f8       ..
; &90bd referenced 1 time by &90b8
.return_10
    rts                                                               ; 90bd: 60          `

; &90be referenced 1 time by &90b5
.l90be
    equb   4,   9, &0a, &14, &9a, &9b, &9c, &e2, &0b, &0c, &0f, &79   ; 90be: 04 09 0a... ...
    equb &7a, &e3, &e4                                                ; 90ca: 7a e3 e4    z..

; Fn 8: remote OSWORD handler (NWORD)
; Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
; envelope). Unlike NBYTE which returns results, NWORD is entirely
; fire-and-forget — no return path is implemented. The developer
; explicitly noted this was acceptable since sound/envelope commands
; don't return meaningful results. Copies up to 14 parameter bytes
; from the RX buffer to workspace, tags the message as RWORD, and
; transmits.
.remote_cmd_data
    ldy #&0e                                                          ; 90cd: a0 0e       ..
    cmp #7                                                            ; 90cf: c9 07       ..
    beq c90d7                                                         ; 90d1: f0 04       ..
    cmp #8                                                            ; 90d3: c9 08       ..
    bne return_11                                                     ; 90d5: d0 24       .$
; &90d7 referenced 1 time by &90d1
.c90d7
    ldx #&db                                                          ; 90d7: a2 db       ..
    stx nfs_workspace                                                 ; 90d9: 86 9e       ..
; &90db referenced 1 time by &90e0
.loop_c90db
    lda (l00f0),y                                                     ; 90db: b1 f0       ..
    sta (nfs_workspace),y                                             ; 90dd: 91 9e       ..
    dey                                                               ; 90df: 88          .
    bpl loop_c90db                                                    ; 90e0: 10 f9       ..
    iny                                                               ; 90e2: c8          .
    dec nfs_workspace                                                 ; 90e3: c6 9e       ..
    lda l00ef                                                         ; 90e5: a5 ef       ..
    sta (nfs_workspace),y                                             ; 90e7: 91 9e       ..
    sty nfs_workspace                                                 ; 90e9: 84 9e       ..
    ldy #&14                                                          ; 90eb: a0 14       ..
    lda #&e9                                                          ; 90ed: a9 e9       ..
    sta (nfs_workspace),y                                             ; 90ef: 91 9e       ..
    lda #1                                                            ; 90f1: a9 01       ..
    jsr setup_tx_and_send                                             ; 90f3: 20 4b 90     K.
    stx nfs_workspace                                                 ; 90f6: 86 9e       ..
    jsr ctrl_block_setup_alt                                          ; 90f8: 20 59 91     Y.
; &90fb referenced 1 time by &90d5
.return_11
    rts                                                               ; 90fb: 60          `

; Remote boot/execute handler
; Validates byte 4 of the RX control block (must be zero), copies the
; 2-byte execution address from RX offsets $80/$81 into NFS workspace,
; sets up a control block, disables keyboard (OSBYTE $C9), then falls
; through to execute_at_0100.
.remote_boot_handler
    ldy #4                                                            ; 90fc: a0 04       ..
    lda (net_rx_ptr),y                                                ; 90fe: b1 9c       ..
    beq c9105                                                         ; 9100: f0 03       ..
; &9102 referenced 1 time by &9148
.c9102
    jmp clear_jsr_protection                                          ; 9102: 4c d6 92    L..

; &9105 referenced 2 times by &9100, &913e
.c9105
    ora #9                                                            ; 9105: 09 09       ..
    sta (net_rx_ptr),y                                                ; 9107: 91 9c       ..
    ldx #&80                                                          ; 9109: a2 80       ..
    ldy #&80                                                          ; 910b: a0 80       ..
    lda (net_rx_ptr),y                                                ; 910d: b1 9c       ..
    pha                                                               ; 910f: 48          H
    iny                                                               ; 9110: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 9111: b1 9c       ..
    ldy #&0f                                                          ; 9113: a0 0f       ..
    sta (nfs_workspace),y                                             ; 9115: 91 9e       ..
    dey                                                               ; 9117: 88          .              ; Y=&0e
    pla                                                               ; 9118: 68          h
    sta (nfs_workspace),y                                             ; 9119: 91 9e       ..
    jsr clear_osbyte_ce_cf                                            ; 911b: 20 5c 81     \.
    jsr ctrl_block_setup                                              ; 911e: 20 62 91     b.
    ldx #1                                                            ; 9121: a2 01       ..
    ldy #0                                                            ; 9123: a0 00       ..
    lda #osbyte_read_write_econet_keyboard_disable                    ; 9125: a9 c9       ..
    jsr osbyte                                                        ; 9127: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; Execute downloaded code at $0100
; Zeroes $0100-$0102 (safe BRK default), restores the protection mask,
; and JMP $0100 to execute code received over the network.
.execute_at_0100
    ldx #2                                                            ; 912a: a2 02       ..
    lda #0                                                            ; 912c: a9 00       ..
; &912e referenced 1 time by &9132
.loop_c912e
    sta l0100,x                                                       ; 912e: 9d 00 01    ...
    dex                                                               ; 9131: ca          .
    bpl loop_c912e                                                    ; 9132: 10 fa       ..
    jsr clear_jsr_protection                                          ; 9134: 20 d6 92     ..
    jmp l0100                                                         ; 9137: 4c 00 01    L..

; Remote operation with source validation (REMOT)
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
.remote_validated
    ldy #4                                                            ; 913a: a0 04       ..
    lda (net_rx_ptr),y                                                ; 913c: b1 9c       ..
    beq c9105                                                         ; 913e: f0 c5       ..
    ldy #&80                                                          ; 9140: a0 80       ..
    lda (net_rx_ptr),y                                                ; 9142: b1 9c       ..
    ldy #&0e                                                          ; 9144: a0 0e       ..
    cmp (nfs_workspace),y                                             ; 9146: d1 9e       ..
    bne c9102                                                         ; 9148: d0 b8       ..
; Insert remote keypress
; Reads a character from RX block offset $82 and inserts it into
; keyboard input buffer 0 via OSBYTE $99.
.insert_remote_key
    ldy #&82                                                          ; 914a: a0 82       ..
    lda (net_rx_ptr),y                                                ; 914c: b1 9c       ..
    tay                                                               ; 914e: a8          .
    ldx #0                                                            ; 914f: a2 00       ..
    jsr clear_jsr_protection                                          ; 9151: 20 d6 92     ..
    lda #osbyte_insert_input_buffer                                   ; 9154: a9 99       ..
    jmp osbyte                                                        ; 9156: 4c f4 ff    L..            ; Insert character Y into input buffer X

; Alternate entry into control block setup
; Sets X=$0D, Y=$7C. Tests bit 6 of $833A to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; &9159 referenced 3 times by &8fe2, &8ff5, &90f8
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 9159: a2 0d       ..
    ldy #&7c ; '|'                                                    ; 915b: a0 7c       .|
    bit l833a                                                         ; 915d: 2c 3a 83    ,:.
    bvs c9167                                                         ; 9160: 70 05       p.
; Control block setup — main entry
; Sets X=$1A, Y=$17, clears V (stores to nfs_workspace).
; Reads the template table at $918E indexed by X, storing each
; value into the target workspace at offset Y. Both X and Y
; are decremented on each iteration.
; 
; Template sentinel values:
;   $FE = stop (end of template for this entry path)
;   $FD = skip (leave existing value unchanged)
;   $FC = use page high byte of target pointer
; &9162 referenced 1 time by &911e
.ctrl_block_setup
    ldy #&17                                                          ; 9162: a0 17       ..
    ldx #&1a                                                          ; 9164: a2 1a       ..
; &9166 referenced 1 time by &922b
.ctrl_block_setup_clv
    clv                                                               ; 9166: b8          .
; &9167 referenced 2 times by &9160, &9188
.c9167
    lda ctrl_block_template,x                                         ; 9167: bd 8e 91    ...            ; Load template byte from ctrl_block_template[X]
    cmp #&fe                                                          ; 916a: c9 fe       ..
    beq c918a                                                         ; 916c: f0 1c       ..
    cmp #&fd                                                          ; 916e: c9 fd       ..
    beq c9186                                                         ; 9170: f0 14       ..
    cmp #&fc                                                          ; 9172: c9 fc       ..
    bne c917e                                                         ; 9174: d0 08       ..
    lda net_rx_ptr_hi                                                 ; 9176: a5 9d       ..
    bvs c917c                                                         ; 9178: 70 02       p.
    lda nfs_workspace_hi                                              ; 917a: a5 9f       ..
; &917c referenced 1 time by &9178
.c917c
    sta net_tx_ptr_hi                                                 ; 917c: 85 9b       ..
; &917e referenced 1 time by &9174
.c917e
    bvs c9184                                                         ; 917e: 70 04       p.
    sta (nfs_workspace),y                                             ; 9180: 91 9e       ..
    bvc c9186                                                         ; 9182: 50 02       P.             ; ALWAYS branch

; &9184 referenced 1 time by &917e
.c9184
    sta (net_rx_ptr),y                                                ; 9184: 91 9c       ..
; &9186 referenced 2 times by &9170, &9182
.c9186
    dey                                                               ; 9186: 88          .
    dex                                                               ; 9187: ca          .
    bpl c9167                                                         ; 9188: 10 dd       ..
; &918a referenced 1 time by &916c
.c918a
    iny                                                               ; 918a: c8          .
    sty net_tx_ptr                                                    ; 918b: 84 9a       ..
    rts                                                               ; 918d: 60          `

; Control block initialisation template
; Read by the loop at $9167, indexed by X from a starting value
; down to 0. Values are stored into either (nfs_workspace) or
; (net_rx_ptr) at offset Y, depending on the V flag.
; 
; Two entry paths read different slices of this table:
;   ctrl_block_setup:   X=$1A (26) down, Y=$17 (23) down, V=0
;   ctrl_block_setup_alt: X=$0D (13) down, Y=$7C (124) down, V from BIT $833A
; 
; Sentinel values:
;   $FE = stop processing
;   $FD = skip this offset (decrement Y but don't store)
;   $FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)
; &918e referenced 1 time by &9167
.ctrl_block_template
    equb &85,   0, &fd, &fd, &7d, &fc, &ff, &ff, &7e, &fc, &ff, &ff   ; 918e: 85 00 fd... ...
    equb   0,   0, &fe, &80, &93, &fd, &fd, &d9, &fc, &ff, &ff, &de   ; 919a: 00 00 fe... ...
    equb &fc, &ff, &ff, &fe, &d1, &fd, &fd, &1f, &fd, &ff, &ff, &fd   ; 91a6: fc ff ff... ...
    equb &fd, &ff, &ff                                                ; 91b2: fd ff ff    ...

; Fn 5: printer selection changed (SELECT)
; Called when the printer selection changes. Compares the new
; selection (in PARMX) against the network printer (buffer 4).
; If it matches, initialises the printer buffer pointer (PBUFFP)
; and sets the initial flag byte ($41). Otherwise just updates
; the printer status flags (PFLAGS).
.remote_display_setup
    lda #0                                                            ; 91b5: a9 00       ..
    dex                                                               ; 91b7: ca          .
    cpx l00f0                                                         ; 91b8: e4 f0       ..
    bne c91c3                                                         ; 91ba: d0 07       ..
    lda #&1f                                                          ; 91bc: a9 1f       ..
    sta printer_buf_ptr                                               ; 91be: 8d 61 0d    .a.
    lda #&43 ; 'C'                                                    ; 91c1: a9 43       .C
; &91c3 referenced 1 time by &91ba
.c91c3
    sta l0d60                                                         ; 91c3: 8d 60 0d    .`.
; &91c6 referenced 2 times by &91c9, &91dd
.return_12
    rts                                                               ; 91c6: 60          `

; Fn 1/2/3: network printer handler (PRINT)
; Handles network printer output. Reason 1 = chars in buffer (extract
; from MOS buffer 3 and accumulate), reason 2 = Ctrl-B (start print),
; reason 3 = Ctrl-C (end print). The printer status byte PFLAGS uses:
;   bit 7 = sequence number (toggles per packet for dup detection)
;   bit 6 = always 1 (validity marker)
;   bit 0 = 0 when print active
; Print streams reuse the BSXMIT (byte-stream transmit) code with
; handle=0, which causes the AND SEQNOS to produce zero and sidestep
; per-file sequence tracking. After transmission, TXCB pointer bytes
; are filled with $FF to prevent stale values corrupting subsequent
; BGET/BPUT operations (a historically significant bug fix).
; N.B. The printer and REMOTE facility share the same dynamically
; allocated static workspace page via WORKP1 ($9E,$9F) — care must
; be taken to never leave the pointer corrupted, as corruption would
; cause one subsystem to overwrite the other's data.
; Only handles buffer 4 (network printer); others are ignored.
.remote_print_handler
    cpy #4                                                            ; 91c7: c0 04       ..
    bne return_12                                                     ; 91c9: d0 fb       ..
    txa                                                               ; 91cb: 8a          .
    dex                                                               ; 91cc: ca          .
    bne c91f5                                                         ; 91cd: d0 26       .&
    tsx                                                               ; 91cf: ba          .
    ora l0106,x                                                       ; 91d0: 1d 06 01    ...
    sta l0106,x                                                       ; 91d3: 9d 06 01    ...
; &91d6 referenced 2 times by &91e5, &91ea
.c91d6
    lda #osbyte_read_buffer                                           ; 91d6: a9 91       ..
    ldx #buffer_printer                                               ; 91d8: a2 03       ..
    jsr osbyte                                                        ; 91da: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_12                                                     ; 91dd: b0 e7       ..
    tya                                                               ; 91df: 98          .              ; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 91e0: 20 ec 91     ..
    cpy #&6e ; 'n'                                                    ; 91e3: c0 6e       .n
    bcc c91d6                                                         ; 91e5: 90 ef       ..
    jsr flush_output_block                                            ; 91e7: 20 17 92     ..
    bne c91d6                                                         ; 91ea: d0 ea       ..
; Store output byte to network buffer
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; &91ec referenced 2 times by &91e0, &91f6
.store_output_byte
    ldy printer_buf_ptr                                               ; 91ec: ac 61 0d    .a.
    sta (net_rx_ptr),y                                                ; 91ef: 91 9c       ..
    inc printer_buf_ptr                                               ; 91f1: ee 61 0d    .a.
    rts                                                               ; 91f4: 60          `

; &91f5 referenced 1 time by &91cd
.c91f5
    pha                                                               ; 91f5: 48          H
    jsr store_output_byte                                             ; 91f6: 20 ec 91     ..
    eor l0d60                                                         ; 91f9: 4d 60 0d    M`.
    ror a                                                             ; 91fc: 6a          j
    bcc c920e                                                         ; 91fd: 90 0f       ..
    lda l0d60                                                         ; 91ff: ad 60 0d    .`.
    ror a                                                             ; 9202: 6a          j
    bcc c920b                                                         ; 9203: 90 06       ..
    rol a                                                             ; 9205: 2a          *
    and #&7f                                                          ; 9206: 29 7f       ).
    sta l0d60                                                         ; 9208: 8d 60 0d    .`.
; &920b referenced 1 time by &9203
.c920b
    jsr flush_output_block                                            ; 920b: 20 17 92     ..
; &920e referenced 1 time by &91fd
.c920e
    ror l0d60                                                         ; 920e: 6e 60 0d    n`.
    pla                                                               ; 9211: 68          h
    ror a                                                             ; 9212: 6a          j
    rol l0d60                                                         ; 9213: 2e 60 0d    .`.
    rts                                                               ; 9216: 60          `

; Flush output block
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; &9217 referenced 2 times by &91e7, &920b
.flush_output_block
    ldy #8                                                            ; 9217: a0 08       ..
    lda printer_buf_ptr                                               ; 9219: ad 61 0d    .a.
    sta (nfs_workspace),y                                             ; 921c: 91 9e       ..
    lda net_rx_ptr_hi                                                 ; 921e: a5 9d       ..
    iny                                                               ; 9220: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 9221: 91 9e       ..
    ldy #5                                                            ; 9223: a0 05       ..
    sta (nfs_workspace),y                                             ; 9225: 91 9e       ..
    ldy #&0b                                                          ; 9227: a0 0b       ..
    ldx #&26 ; '&'                                                    ; 9229: a2 26       .&
    jsr ctrl_block_setup_clv                                          ; 922b: 20 66 91     f.
    dey                                                               ; 922e: 88          .
    lda l0d60                                                         ; 922f: ad 60 0d    .`.
    pha                                                               ; 9232: 48          H
    rol a                                                             ; 9233: 2a          *
    pla                                                               ; 9234: 68          h
    eor #&80                                                          ; 9235: 49 80       I.
    sta l0d60                                                         ; 9237: 8d 60 0d    .`.
    rol a                                                             ; 923a: 2a          *
    sta (nfs_workspace),y                                             ; 923b: 91 9e       ..
    ldy #&1f                                                          ; 923d: a0 1f       ..
    sty printer_buf_ptr                                               ; 923f: 8c 61 0d    .a.
    lda #0                                                            ; 9242: a9 00       ..
    tax                                                               ; 9244: aa          .              ; X=&00
    ldy nfs_workspace_hi                                              ; 9245: a4 9f       ..
    cli                                                               ; 9247: 58          X
; Transmit with retry loop (XMITFS/XMITFY)
; Calls the low-level transmit routine (BRIANX) with FSTRY ($FF = 255)
; retries and FSDELY ($60 = 96) ms delay between attempts. On each
; iteration, checks the result code: zero means success, non-zero
; means retry. After all retries exhausted, reports a 'Net error'.
; Entry point XMITFY allows a custom delay in Y.
; &9248 referenced 2 times by &839b, &83d3
.econet_tx_retry
    stx net_tx_ptr                                                    ; 9248: 86 9a       ..
    sty net_tx_ptr_hi                                                 ; 924a: 84 9b       ..
    pha                                                               ; 924c: 48          H
    and fs_sequence_nos                                               ; 924d: 2d 08 0e    -..
    beq c9254                                                         ; 9250: f0 02       ..
    lda #1                                                            ; 9252: a9 01       ..
; &9254 referenced 1 time by &9250
.c9254
    ldy #0                                                            ; 9254: a0 00       ..
    ora (net_tx_ptr),y                                                ; 9256: 11 9a       ..
    pha                                                               ; 9258: 48          H
    sta (net_tx_ptr),y                                                ; 9259: 91 9a       ..
    jsr tx_poll_ff                                                    ; 925b: 20 4c 86     L.
    lda #&ff                                                          ; 925e: a9 ff       ..
    ldy #8                                                            ; 9260: a0 08       ..
    sta (net_tx_ptr),y                                                ; 9262: 91 9a       ..
    iny                                                               ; 9264: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 9265: 91 9a       ..
    pla                                                               ; 9267: 68          h
    tax                                                               ; 9268: aa          .
    ldy #&d1                                                          ; 9269: a0 d1       ..
    pla                                                               ; 926b: 68          h
    pha                                                               ; 926c: 48          H
    beq c9271                                                         ; 926d: f0 02       ..
    ldy #&90                                                          ; 926f: a0 90       ..
; &9271 referenced 1 time by &926d
.c9271
    tya                                                               ; 9271: 98          .
    ldy #1                                                            ; 9272: a0 01       ..
    sta (net_tx_ptr),y                                                ; 9274: 91 9a       ..
    txa                                                               ; 9276: 8a          .
    dey                                                               ; 9277: 88          .              ; Y=&00
    pha                                                               ; 9278: 48          H
; &9279 referenced 1 time by &9285
.loop_c9279
    lda #&7f                                                          ; 9279: a9 7f       ..
    sta (net_tx_ptr),y                                                ; 927b: 91 9a       ..
    jsr send_to_fs_star                                               ; 927d: 20 48 84     H.
    pla                                                               ; 9280: 68          h
    pha                                                               ; 9281: 48          H
    eor (net_tx_ptr),y                                                ; 9282: 51 9a       Q.
    ror a                                                             ; 9284: 6a          j
    bcs loop_c9279                                                    ; 9285: b0 f2       ..
    pla                                                               ; 9287: 68          h
    pla                                                               ; 9288: 68          h
    tax                                                               ; 9289: aa          .
    inx                                                               ; 928a: e8          .
    beq return_13                                                     ; 928b: f0 03       ..
    eor fs_sequence_nos                                               ; 928d: 4d 08 0e    M..
; &9290 referenced 1 time by &928b
.return_13
    rts                                                               ; 9290: 60          `

; Save palette and VDU state (CVIEW)
; Part of the VIEW facility (second iteration, started 27/7/82).
; Uses dynamically allocated buffer store. The WORKP1 pointer
; ($9E,$9F) serves double duty: non-zero indicates data ready AND
; provides the buffer address — an efficient use of scarce zero-
; page space. This code must be user-transparent as the NFS may not
; be the dominant filing system.
; Reads all 16 palette entries using OSWORD $0B (read palette) and
; stores the results. Then reads cursor position (OSBYTE $85),
; shadow RAM allocation (OSBYTE $C2), and screen start address
; (OSBYTE $C3) using the 3-entry table at $9304 (osbyte_vdu_table).
; On completion, restores the JSR buffer protection bits (LSTAT)
; from OLDJSR to re-enable JSR reception, which was disabled during
; the screen data capture to prevent interference.
.save_palette_vdu
    lda fs_load_addr_2                                                ; 9291: a5 b2       ..
    pha                                                               ; 9293: 48          H
    lda #&e9                                                          ; 9294: a9 e9       ..
    sta nfs_workspace                                                 ; 9296: 85 9e       ..
    ldy #0                                                            ; 9298: a0 00       ..
    sty fs_load_addr_2                                                ; 929a: 84 b2       ..
    lda l0350                                                         ; 929c: ad 50 03    .P.
    sta (nfs_workspace),y                                             ; 929f: 91 9e       ..
    inc nfs_workspace                                                 ; 92a1: e6 9e       ..
    lda l0351                                                         ; 92a3: ad 51 03    .Q.
    pha                                                               ; 92a6: 48          H
    tya                                                               ; 92a7: 98          .              ; A=&00
; &92a8 referenced 1 time by &92c7
.loop_c92a8
    sta (nfs_workspace),y                                             ; 92a8: 91 9e       ..
    ldx nfs_workspace                                                 ; 92aa: a6 9e       ..
    ldy nfs_workspace_hi                                              ; 92ac: a4 9f       ..
    lda #osword_read_palette                                          ; 92ae: a9 0b       ..
    jsr osword                                                        ; 92b0: 20 f1 ff     ..            ; Read palette
    pla                                                               ; 92b3: 68          h
    ldy #0                                                            ; 92b4: a0 00       ..
    sta (nfs_workspace),y                                             ; 92b6: 91 9e       ..
    iny                                                               ; 92b8: c8          .              ; Y=&01
    lda (nfs_workspace),y                                             ; 92b9: b1 9e       ..
    pha                                                               ; 92bb: 48          H
    ldx nfs_workspace                                                 ; 92bc: a6 9e       ..
    inc nfs_workspace                                                 ; 92be: e6 9e       ..
    inc fs_load_addr_2                                                ; 92c0: e6 b2       ..
    dey                                                               ; 92c2: 88          .              ; Y=&00
    lda fs_load_addr_2                                                ; 92c3: a5 b2       ..
    cpx #&f9                                                          ; 92c5: e0 f9       ..
    bne loop_c92a8                                                    ; 92c7: d0 df       ..
    pla                                                               ; 92c9: 68          h
    sty fs_load_addr_2                                                ; 92ca: 84 b2       ..
    inc nfs_workspace                                                 ; 92cc: e6 9e       ..
    jsr save_vdu_state                                                ; 92ce: 20 dd 92     ..
    inc nfs_workspace                                                 ; 92d1: e6 9e       ..
    pla                                                               ; 92d3: 68          h
    sta fs_load_addr_2                                                ; 92d4: 85 b2       ..
; &92d6 referenced 4 times by &8e65, &9102, &9134, &9151
.clear_jsr_protection
    lda rx_ctrl_copy                                                  ; 92d6: ad 3b 0d    .;.
    sta prot_status                                                   ; 92d9: 8d 63 0d    .c.
    rts                                                               ; 92dc: 60          `

; Save VDU workspace state
; Stores the cursor position value from $0355 into NFS workspace,
; then reads cursor position (OSBYTE $85), shadow RAM (OSBYTE $C2),
; and screen start (OSBYTE $C3) via read_vdu_osbyte, storing
; each result into consecutive workspace bytes.
; &92dd referenced 1 time by &92ce
.save_vdu_state
    lda l0355                                                         ; 92dd: ad 55 03    .U.
    sta (nfs_workspace),y                                             ; 92e0: 91 9e       ..
    tax                                                               ; 92e2: aa          .
    jsr read_vdu_osbyte                                               ; 92e3: 20 f0 92     ..
    inc nfs_workspace                                                 ; 92e6: e6 9e       ..
    tya                                                               ; 92e8: 98          .
    sta (nfs_workspace,x)                                             ; 92e9: 81 9e       ..
    jsr read_vdu_osbyte_x0                                            ; 92eb: 20 ee 92     ..
; &92ee referenced 1 time by &92eb
.read_vdu_osbyte_x0
    ldx #0                                                            ; 92ee: a2 00       ..
; &92f0 referenced 1 time by &92e3
.read_vdu_osbyte
    ldy fs_load_addr_2                                                ; 92f0: a4 b2       ..
    inc fs_load_addr_2                                                ; 92f2: e6 b2       ..
    inc nfs_workspace                                                 ; 92f4: e6 9e       ..
    lda osbyte_vdu_table,y                                            ; 92f6: b9 04 93    ...
    ldy #&ff                                                          ; 92f9: a0 ff       ..
    jsr osbyte                                                        ; 92fb: 20 f4 ff     ..
    txa                                                               ; 92fe: 8a          .
    ldx #0                                                            ; 92ff: a2 00       ..
    sta (nfs_workspace,x)                                             ; 9301: 81 9e       ..
    rts                                                               ; 9303: 60          `

; Table of 3 OSBYTE codes used by save_palette_vdu_state ($9291):
;   $85 = read cursor position
;   $C2 = read shadow RAM allocation
;   $C3 = read screen start address
; &9304 referenced 1 time by &92f6
.osbyte_vdu_table
    equb &85, &c2, &c3                                                ; 9304: 85 c2 c3    ...
; &9307 referenced 1 time by &8113
.c9307

; Move 1: &9307 to &16 for length 69
    org &16
; Tube BRK handler (BRKV target) — reference: NFS11 NEWBR
; Sends error information to the Tube co-processor via R2 and R4:
;   1. Sends $FF to R4 (WRIFOR) to signal error
;   2. Reads R2 data (flush any pending byte)
;   3. Sends $00 via R2, then error number from ($FD),0
;   4. Loops sending error string bytes via R2 until zero terminator
;   5. Falls through to tube_reset_stack → tube_main_loop
; The main loop continuously polls R1 for WRCH requests (forwarded
; to OSWRITCH $FFCB) and R2 for command bytes (dispatched via the
; 14-entry table at $0500). The R2 command byte is stored at $55
; before dispatch via JMP ($0500).
; &9307 referenced 1 time by &8116
.nmi_workspace_start
.tube_brk_handler
    lda #&ff                                                          ; 9307: a9 ff       ..  :0016[1]
    jsr tube_send_r4                                                  ; 9309: 20 d9 06     .. :0018[1]
    lda tube_data_register_2                                          ; 930c: ad e3 fe    ... :001b[1]
    lda #0                                                            ; 930f: a9 00       ..  :001e[1]
    jsr tube_send_r2                                                  ; 9311: 20 d0 06     .. :0020[1]
    tay                                                               ; 9314: a8          .   :0023[1]
    lda (l00fd),y                                                     ; 9315: b1 fd       ..  :0024[1]
    jsr tube_send_r2                                                  ; 9317: 20 d0 06     .. :0026[1]
; &931a referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 931a: c8          .   :0029[1]
    lda (l00fd),y                                                     ; 931b: b1 fd       ..  :002a[1]
    jsr tube_send_r2                                                  ; 931d: 20 d0 06     .. :002c[1]
    tax                                                               ; 9320: aa          .   :002f[1]
    bne tube_brk_send_loop                                            ; 9321: d0 f7       ..  :0030[1]
.tube_reset_stack
    ldx #&ff                                                          ; 9323: a2 ff       ..  :0032[1]
    txs                                                               ; 9325: 9a          .   :0034[1]
    cli                                                               ; 9326: 58          X   :0035[1]
; &9327 referenced 2 times by &04ec[2], &053a[3]
.c0036
    stx zp_temp_11                                                    ; 9327: 86 11       ..  :0036[1]
    sty zp_temp_10                                                    ; 9329: 84 10       ..  :0038[1]
; &932b referenced 7 times by &0048[1], &05ae[3], &05d5[3], &0623[4], &0638[4], &06a0[4], &06cd[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; 932b: 2c e0 fe    ,.. :003a[1]
    bpl tube_poll_r2                                                  ; 932e: 10 06       ..  :003d[1]
; &9330 referenced 1 time by &004d[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; 9330: ad e1 fe    ... :003f[1]
    jsr nvwrch                                                        ; 9333: 20 cb ff     .. :0042[1]   ; Write character
; &9336 referenced 1 time by &003d[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 9336: 2c e2 fe    ,.. :0045[1]
    bpl tube_main_loop                                                ; 9339: 10 f0       ..  :0048[1]
    bit tube_status_1_and_tube_control                                ; 933b: 2c e0 fe    ,.. :004a[1]
    bmi tube_handle_wrch                                              ; 933e: 30 f0       0.  :004d[1]
    ldx tube_data_register_2                                          ; 9340: ae e3 fe    ... :004f[1]
    stx l0055                                                         ; 9343: 86 55       .U  :0052[1]
.tube_dispatch_cmd
l0055 = tube_dispatch_cmd+1
    jmp (tube_dispatch_table)                                         ; 9345: 6c 00 05    l.. :0054[1]

; &9346 referenced 1 time by &0052[1]
; &9348 referenced 2 times by &0478[2], &0493[2]
.tube_transfer_addr
    equb 0                                                            ; 9348: 00          .   :0057[1]
; &9349 referenced 2 times by &047c[2], &0498[2]
.l0058
    equb &80                                                          ; 9349: 80          .   :0058[1]
; &934a referenced 1 time by &04a2[2]
.l0059
    equb 0                                                            ; 934a: 00          .   :0059[1]
; &934b referenced 1 time by &04a0[2]
.l005a
    equb 0                                                            ; 934b: 00          .   :005a[1]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock nmi_workspace_start, *, c9307

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear nmi_workspace_start, &005b

    ; Set the program counter to the next position in the binary file.
    org c9307 + (* - nmi_workspace_start)

.c934c

; Move 2: &934c to &0400 for length 256
    org &0400
; Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)
; Copied from ROM at $934C during init. The first 28 bytes ($0400-$041B)
; overlap with the end of the ZP block (the same ROM bytes serve both
; the ZP copy at $005B-$0076 and this page at $0400-$041B). Contains:
;   $0400: JMP $0473 (BEGIN — CLI parser / startup entry)
;   $0403: JMP $06E2 (tube_escape_check)
;   $0406: tube_addr_claim — Tube address claim protocol (ADRR)
;   $0414: tube_post_init — called after ROM→RAM copy
;   $0473: BEGIN — startup/CLI entry, break type check
;   $04E7: tube_rdch_handler — RDCHV target
;   $04EF: tube_restore_regs — restore X,Y, dispatch entry 6
;   $04F7: tube_read_r2 — poll R2 status, read data byte to A
; &934c referenced 1 time by &80fc
.tube_code_page4
    jmp c0473                                                         ; 934c: 4c 73 04    Ls. :0400[2]

.tube_escape_entry
    jmp tube_escape_check                                             ; 934f: 4c e2 06    L.. :0403[2]

; &9352 referenced 10 times by &04bc[2], &04e4[2], &8b1d, &8b2f, &8b8c, &8da9, &99f0, &9a3d, &9f98, &9fa0
.tube_addr_claim
    cmp #&80                                                          ; 9352: c9 80       ..  :0406[2]
    bcc c0426                                                         ; 9354: 90 1c       ..  :0408[2]
    cmp #&c0                                                          ; 9356: c9 c0       ..  :040a[2]
    bcs c0419                                                         ; 9358: b0 0b       ..  :040c[2]
    ora #&40 ; '@'                                                    ; 935a: 09 40       .@  :040e[2]
    cmp l0015                                                         ; 935c: c5 15       ..  :0410[2]
    bne return_14                                                     ; 935e: d0 11       ..  :0412[2]
; &9360 referenced 1 time by &810e
.tube_post_init
    lda #&80                                                          ; 9360: a9 80       ..  :0414[2]
    sta l0014                                                         ; 9362: 85 14       ..  :0416[2]
    rts                                                               ; 9364: 60          `   :0418[2]

; &9365 referenced 1 time by &040c[2]
.c0419
    asl l0014                                                         ; 9365: 06 14       ..  :0419[2]
    bcs c0423                                                         ; 9367: b0 06       ..  :041b[2]
    cmp l0015                                                         ; 9369: c5 15       ..  :041d[2]
    beq return_14                                                     ; 936b: f0 04       ..  :041f[2]
    clc                                                               ; 936d: 18          .   :0421[2]
    rts                                                               ; 936e: 60          `   :0422[2]

; &936f referenced 1 time by &041b[2]
.c0423
    sta l0015                                                         ; 936f: 85 15       ..  :0423[2]
; &9371 referenced 2 times by &0412[2], &041f[2]
.return_14
    rts                                                               ; 9371: 60          `   :0425[2]

; &9372 referenced 1 time by &0408[2]
.c0426
    sty l0013                                                         ; 9372: 84 13       ..  :0426[2]
    stx l0012                                                         ; 9374: 86 12       ..  :0428[2]
    jsr tube_send_r4                                                  ; 9376: 20 d9 06     .. :042a[2]
    tax                                                               ; 9379: aa          .   :042d[2]
    ldy #3                                                            ; 937a: a0 03       ..  :042e[2]
; &937c referenced 1 time by &0436[2]
.loop_c0430
    lda (l0012),y                                                     ; 937c: b1 12       ..  :0430[2]
    jsr tube_send_r4                                                  ; 937e: 20 d9 06     .. :0432[2]
    dey                                                               ; 9381: 88          .   :0435[2]
    bpl loop_c0430                                                    ; 9382: 10 f8       ..  :0436[2]
    ldy #8                                                            ; 9384: a0 08       ..  :0438[2]
    sty tube_status_1_and_tube_control                                ; 9386: 8c e0 fe    ... :043a[2]
    ldy #&10                                                          ; 9389: a0 10       ..  :043d[2]
    cpx #2                                                            ; 938b: e0 02       ..  :043f[2]
    bcc c0445                                                         ; 938d: 90 02       ..  :0441[2]
    ldy #&90                                                          ; 938f: a0 90       ..  :0443[2]
; &9391 referenced 1 time by &0441[2]
.c0445
    sty tube_status_1_and_tube_control                                ; 9391: 8c e0 fe    ... :0445[2]
    jsr tube_send_r4                                                  ; 9394: 20 d9 06     .. :0448[2]
    ldy #&88                                                          ; 9397: a0 88       ..  :044b[2]
    txa                                                               ; 9399: 8a          .   :044d[2]
    beq c0464                                                         ; 939a: f0 14       ..  :044e[2]
    cmp #2                                                            ; 939c: c9 02       ..  :0450[2]
    beq c0464                                                         ; 939e: f0 10       ..  :0452[2]
    sty tube_status_1_and_tube_control                                ; 93a0: 8c e0 fe    ... :0454[2]
    cmp #4                                                            ; 93a3: c9 04       ..  :0457[2]
    bne return_15                                                     ; 93a5: d0 17       ..  :0459[2]
    pla                                                               ; 93a7: 68          h   :045b[2]
    pla                                                               ; 93a8: 68          h   :045c[2]
; &93a9 referenced 1 time by &04b8[2]
.c045d
    lda #&80                                                          ; 93a9: a9 80       ..  :045d[2]
    sta l0014                                                         ; 93ab: 85 14       ..  :045f[2]
    jmp tube_reply_byte                                               ; 93ad: 4c cd 05    L.. :0461[2]

; &93b0 referenced 3 times by &044e[2], &0452[2], &0467[2]
.c0464
    bit tube_status_register_4_and_cpu_control                        ; 93b0: 2c e6 fe    ,.. :0464[2]
    bvc c0464                                                         ; 93b3: 50 fb       P.  :0467[2]
    bit tube_data_register_3                                          ; 93b5: 2c e5 fe    ,.. :0469[2]
    bit tube_data_register_3                                          ; 93b8: 2c e5 fe    ,.. :046c[2]
    sty tube_status_1_and_tube_control                                ; 93bb: 8c e0 fe    ... :046f[2]
; &93be referenced 1 time by &0459[2]
.return_15
    rts                                                               ; 93be: 60          `   :0472[2]

; &93bf referenced 1 time by &0400[2]
.c0473
    cli                                                               ; 93bf: 58          X   :0473[2]
    php                                                               ; 93c0: 08          .   :0474[2]
    pha                                                               ; 93c1: 48          H   :0475[2]
    ldy #0                                                            ; 93c2: a0 00       ..  :0476[2]
    sty tube_transfer_addr                                            ; 93c4: 84 57       .W  :0478[2]
    lda #&80                                                          ; 93c6: a9 80       ..  :047a[2]
    sta l0058                                                         ; 93c8: 85 58       .X  :047c[2]
    sta l0001                                                         ; 93ca: 85 01       ..  :047e[2]
    lda #&20 ; ' '                                                    ; 93cc: a9 20       .   :0480[2]
    and rom_type                                                      ; 93ce: 2d 06 80    -.. :0482[2]
    beq c04a0                                                         ; 93d1: f0 19       ..  :0485[2]
    ldx copyright_offset                                              ; 93d3: ae 07 80    ... :0487[2]
; &93d6 referenced 1 time by &048e[2]
.loop_c048a
    inx                                                               ; 93d6: e8          .   :048a[2]
    lda rom_header,x                                                  ; 93d7: bd 00 80    ... :048b[2]
    bne loop_c048a                                                    ; 93da: d0 fa       ..  :048e[2]
    lda l8001,x                                                       ; 93dc: bd 01 80    ... :0490[2]
    sta tube_transfer_addr                                            ; 93df: 85 57       .W  :0493[2]
    lda l8002,x                                                       ; 93e1: bd 02 80    ... :0495[2]
    sta l0058                                                         ; 93e4: 85 58       .X  :0498[2]
    ldy service_entry,x                                               ; 93e6: bc 03 80    ... :049a[2]
    lda l8004,x                                                       ; 93e9: bd 04 80    ... :049d[2]
; &93ec referenced 1 time by &0485[2]
.c04a0
    sta l005a                                                         ; 93ec: 85 5a       .Z  :04a0[2]
    sty l0059                                                         ; 93ee: 84 59       .Y  :04a2[2]
    pla                                                               ; 93f0: 68          h   :04a4[2]
    plp                                                               ; 93f1: 28          (   :04a5[2]
    bcs c04ba                                                         ; 93f2: b0 12       ..  :04a6[2]
    tax                                                               ; 93f4: aa          .   :04a8[2]
    bne c04ae                                                         ; 93f5: d0 03       ..  :04a9[2]
    jmp tube_reply_ack                                                ; 93f7: 4c cb 05    L.. :04ab[2]

; &93fa referenced 1 time by &04a9[2]
.c04ae
    ldx #0                                                            ; 93fa: a2 00       ..  :04ae[2]
    ldy #&ff                                                          ; 93fc: a0 ff       ..  :04b0[2]
    lda #osbyte_read_write_last_break_type                            ; 93fe: a9 fd       ..  :04b2[2]
    jsr osbyte                                                        ; 9400: 20 f4 ff     .. :04b4[2]   ; Read type of last reset
    txa                                                               ; 9403: 8a          .   :04b7[2]   ; X=value of type of last reset
    beq c045d                                                         ; 9404: f0 a3       ..  :04b8[2]
; &9406 referenced 2 times by &04a6[2], &04bf[2]
.c04ba
    lda #&ff                                                          ; 9406: a9 ff       ..  :04ba[2]
    jsr tube_addr_claim                                               ; 9408: 20 06 04     .. :04bc[2]
    bcc c04ba                                                         ; 940b: 90 f9       ..  :04bf[2]
    lda #1                                                            ; 940d: a9 01       ..  :04c1[2]
    jsr tube_setup_transfer                                           ; 940f: 20 e0 04     .. :04c3[2]
    ldy #0                                                            ; 9412: a0 00       ..  :04c6[2]
    sty l0000                                                         ; 9414: 84 00       ..  :04c8[2]
    ldx #&40 ; '@'                                                    ; 9416: a2 40       .@  :04ca[2]
; &9418 referenced 2 times by &04d7[2], &04dc[2]
.c04cc
    lda (l0000),y                                                     ; 9418: b1 00       ..  :04cc[2]
    sta tube_data_register_3                                          ; 941a: 8d e5 fe    ... :04ce[2]
; &941d referenced 1 time by &04d4[2]
.loop_c04d1
    bit tube_status_register_3                                        ; 941d: 2c e4 fe    ,.. :04d1[2]
    bvc loop_c04d1                                                    ; 9420: 50 fb       P.  :04d4[2]
    iny                                                               ; 9422: c8          .   :04d6[2]
    bne c04cc                                                         ; 9423: d0 f3       ..  :04d7[2]
    inc l0001                                                         ; 9425: e6 01       ..  :04d9[2]
    dex                                                               ; 9427: ca          .   :04db[2]
    bne c04cc                                                         ; 9428: d0 ee       ..  :04dc[2]
    lda #4                                                            ; 942a: a9 04       ..  :04de[2]
; &942c referenced 1 time by &04c3[2]
.tube_setup_transfer
    ldy #0                                                            ; 942c: a0 00       ..  :04e0[2]
    ldx #&57 ; 'W'                                                    ; 942e: a2 57       .W  :04e2[2]
    jmp tube_addr_claim                                               ; 9430: 4c 06 04    L.. :04e4[2]

.tube_rdch_handler
    lda #1                                                            ; 9433: a9 01       ..  :04e7[2]
    jsr tube_send_r2                                                  ; 9435: 20 d0 06     .. :04e9[2]
    jmp c0036                                                         ; 9438: 4c 36 00    L6. :04ec[2]

.tube_restore_regs
    ldy zp_temp_10                                                    ; 943b: a4 10       ..  :04ef[2]
    ldx zp_temp_11                                                    ; 943d: a6 11       ..  :04f1[2]
    jsr tube_read_r2                                                  ; 943f: 20 f7 04     .. :04f3[2]
    asl a                                                             ; 9442: 0a          .   :04f6[2]
; &9443 referenced 22 times by &04f3[2], &04fa[2], &0543[3], &0547[3], &0550[3], &0569[3], &0580[3], &058c[3], &0592[3], &059b[3], &05b5[3], &05da[3], &05eb[3], &0604[4], &060c[4], &0626[4], &062a[4], &063b[4], &063f[4], &0643[4], &065d[4], &06a5[4]
.tube_read_r2
    bit tube_status_register_2                                        ; 9443: 2c e2 fe    ,.. :04f7[2]
    bpl tube_read_r2                                                  ; 9446: 10 fb       ..  :04fa[2]
    lda tube_data_register_2                                          ; 9448: ad e3 fe    ... :04fc[2]
    rts                                                               ; 944b: 60          `   :04ff[2]


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, c934c

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &0500

    ; Set the program counter to the next position in the binary file.
    org c934c + (* - tube_code_page4)

.l944c

; Move 3: &944c to &0500 for length 256
    org &0500
; Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)
; Copied from ROM at $944C during init. Contains:
;   $0500: tube_dispatch_table — 14-entry handler address table
;   $051C: tube_wrch_handler — WRCHV target
;   $051F: tube_send_and_poll — send byte via R2, poll for reply
;   $0527: tube_poll_r1_wrch — service R1 WRCH while waiting for R2
;   $053D: tube_release_return — restore regs and RTS
;   $0543: tube_osbput — write byte to file
;   $0550: tube_osbget — read byte from file
;   $055B: tube_osrdch — read character
;   $0569: tube_osfind — open file
;   $0580: tube_osfind_close — close file (A=0)
;   $058C: tube_osargs — file argument read/write
;   $05B1: tube_read_string — read CR-terminated string into $0700
;   $05C5: tube_oscli — execute * command
;   $05CB: tube_reply_ack — send $7F acknowledge
;   $05CD: tube_reply_byte — send byte and return to main loop
;   $05D8: tube_osfile — whole file operation
; &944c referenced 2 times by &0054[1], &8102
.tube_dispatch_table
    equb &5b, 5, &c5, 5, &26, 6, &3b, 6, &5d, 6, &a3, 6, &ef, 4       ; 944c: 5b 05 c5... [.. :0500[3]
    equb &3d, 5, &8c, 5, &50, 5, &43, 5, &69, 5, &d8, 5,   2, 6       ; 945a: 3d 05 8c... =.. :050e[3]

.tube_wrch_handler
    pha                                                               ; 9468: 48          H   :051c[3]
    lda #0                                                            ; 9469: a9 00       ..  :051d[3]
.tube_send_and_poll
    jsr tube_send_r2                                                  ; 946b: 20 d0 06     .. :051f[3]
; &946e referenced 2 times by &052a[3], &0532[3]
.c0522
    bit tube_status_register_2                                        ; 946e: 2c e2 fe    ,.. :0522[3]
    bvs c0535                                                         ; 9471: 70 0e       p.  :0525[3]
.tube_poll_r1_wrch
    bit tube_status_1_and_tube_control                                ; 9473: 2c e0 fe    ,.. :0527[3]
    bpl c0522                                                         ; 9476: 10 f6       ..  :052a[3]
    lda tube_data_register_1                                          ; 9478: ad e1 fe    ... :052c[3]
    jsr nvwrch                                                        ; 947b: 20 cb ff     .. :052f[3]   ; Write character
.tube_resume_poll
    jmp c0522                                                         ; 947e: 4c 22 05    L". :0532[3]

; &9481 referenced 1 time by &0525[3]
.c0535
    pla                                                               ; 9481: 68          h   :0535[3]
    sta tube_data_register_2                                          ; 9482: 8d e3 fe    ... :0536[3]
    pha                                                               ; 9485: 48          H   :0539[3]
    jmp c0036                                                         ; 9486: 4c 36 00    L6. :053a[3]

.tube_release_return
    ldx zp_temp_11                                                    ; 9489: a6 11       ..  :053d[3]
    ldy zp_temp_10                                                    ; 948b: a4 10       ..  :053f[3]
    pla                                                               ; 948d: 68          h   :0541[3]
    rts                                                               ; 948e: 60          `   :0542[3]

.tube_osbput
    jsr tube_read_r2                                                  ; 948f: 20 f7 04     .. :0543[3]
    tay                                                               ; 9492: a8          .   :0546[3]
    jsr tube_read_r2                                                  ; 9493: 20 f7 04     .. :0547[3]
    jsr osbput                                                        ; 9496: 20 d4 ff     .. :054a[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 9499: 4c cb 05    L.. :054d[3]

.tube_osbget
    jsr tube_read_r2                                                  ; 949c: 20 f7 04     .. :0550[3]
    tay                                                               ; 949f: a8          .   :0553[3]   ; Y=file handle
    jsr osbget                                                        ; 94a0: 20 d7 ff     .. :0554[3]   ; Read a single byte from an open file Y
    pha                                                               ; 94a3: 48          H   :0557[3]
    jmp c055f                                                         ; 94a4: 4c 5f 05    L_. :0558[3]

.tube_osrdch
    jsr nvrdch                                                        ; 94a7: 20 c8 ff     .. :055b[3]   ; Read a character from the current input stream
    pha                                                               ; 94aa: 48          H   :055e[3]   ; A=character read
; &94ab referenced 1 time by &0558[3]
.c055f
    ora #&80                                                          ; 94ab: 09 80       ..  :055f[3]
.tube_rdch_reply
    ror a                                                             ; 94ad: 6a          j   :0561[3]
    jsr tube_send_r2                                                  ; 94ae: 20 d0 06     .. :0562[3]
    pla                                                               ; 94b1: 68          h   :0565[3]
    jmp tube_reply_byte                                               ; 94b2: 4c cd 05    L.. :0566[3]

.tube_osfind
    jsr tube_read_r2                                                  ; 94b5: 20 f7 04     .. :0569[3]
    beq tube_osfind_close                                             ; 94b8: f0 12       ..  :056c[3]
    pha                                                               ; 94ba: 48          H   :056e[3]
    jsr tube_read_string                                              ; 94bb: 20 b1 05     .. :056f[3]
    pla                                                               ; 94be: 68          h   :0572[3]
    jsr osfind                                                        ; 94bf: 20 ce ff     .. :0573[3]   ; Open or close file(s)
    pha                                                               ; 94c2: 48          H   :0576[3]
    lda #&ff                                                          ; 94c3: a9 ff       ..  :0577[3]
    jsr tube_send_r2                                                  ; 94c5: 20 d0 06     .. :0579[3]
    pla                                                               ; 94c8: 68          h   :057c[3]
    jmp tube_reply_byte                                               ; 94c9: 4c cd 05    L.. :057d[3]

; &94cc referenced 1 time by &056c[3]
.tube_osfind_close
    jsr tube_read_r2                                                  ; 94cc: 20 f7 04     .. :0580[3]
    tay                                                               ; 94cf: a8          .   :0583[3]
    lda #osfind_close                                                 ; 94d0: a9 00       ..  :0584[3]
    jsr osfind                                                        ; 94d2: 20 ce ff     .. :0586[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94d5: 4c cb 05    L.. :0589[3]

.tube_osargs
    jsr tube_read_r2                                                  ; 94d8: 20 f7 04     .. :058c[3]
    tay                                                               ; 94db: a8          .   :058f[3]
.tube_read_params
    ldx #3                                                            ; 94dc: a2 03       ..  :0590[3]
; &94de referenced 1 time by &0598[3]
.loop_c0592
    jsr tube_read_r2                                                  ; 94de: 20 f7 04     .. :0592[3]
    sta l0000,x                                                       ; 94e1: 95 00       ..  :0595[3]
    dex                                                               ; 94e3: ca          .   :0597[3]
    bpl loop_c0592                                                    ; 94e4: 10 f8       ..  :0598[3]
    inx                                                               ; 94e6: e8          .   :059a[3]
    jsr tube_read_r2                                                  ; 94e7: 20 f7 04     .. :059b[3]
    jsr osargs                                                        ; 94ea: 20 da ff     .. :059e[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 94ed: 20 d0 06     .. :05a1[3]
    ldx #3                                                            ; 94f0: a2 03       ..  :05a4[3]
; &94f2 referenced 1 time by &05ac[3]
.loop_c05a6
    lda l0000,x                                                       ; 94f2: b5 00       ..  :05a6[3]
    jsr tube_send_r2                                                  ; 94f4: 20 d0 06     .. :05a8[3]
    dex                                                               ; 94f7: ca          .   :05ab[3]
    bpl loop_c05a6                                                    ; 94f8: 10 f8       ..  :05ac[3]
    jmp tube_main_loop                                                ; 94fa: 4c 3a 00    L:. :05ae[3]

; &94fd referenced 3 times by &056f[3], &05c5[3], &05e2[3]
.tube_read_string
    ldx #0                                                            ; 94fd: a2 00       ..  :05b1[3]
    ldy #0                                                            ; 94ff: a0 00       ..  :05b3[3]
; &9501 referenced 1 time by &05c0[3]
.loop_c05b5
    jsr tube_read_r2                                                  ; 9501: 20 f7 04     .. :05b5[3]
    sta l0700,y                                                       ; 9504: 99 00 07    ... :05b8[3]
    iny                                                               ; 9507: c8          .   :05bb[3]
    beq c05c2                                                         ; 9508: f0 04       ..  :05bc[3]
    cmp #&0d                                                          ; 950a: c9 0d       ..  :05be[3]
    bne loop_c05b5                                                    ; 950c: d0 f3       ..  :05c0[3]
; &950e referenced 1 time by &05bc[3]
.c05c2
    ldy #7                                                            ; 950e: a0 07       ..  :05c2[3]
    rts                                                               ; 9510: 60          `   :05c4[3]

.tube_oscli
    jsr tube_read_string                                              ; 9511: 20 b1 05     .. :05c5[3]
    jsr oscli                                                         ; 9514: 20 f7 ff     .. :05c8[3]
; &9517 referenced 3 times by &04ab[2], &054d[3], &0589[3]
.tube_reply_ack
    lda #&7f                                                          ; 9517: a9 7f       ..  :05cb[3]
; &9519 referenced 5 times by &0461[2], &0566[3], &057d[3], &05d0[3], &06b8[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 9519: 2c e2 fe    ,.. :05cd[3]
    bvc tube_reply_byte                                               ; 951c: 50 fb       P.  :05d0[3]
    sta tube_data_register_2                                          ; 951e: 8d e3 fe    ... :05d2[3]
; &9521 referenced 1 time by &0600[4]
.c05d5
    jmp tube_main_loop                                                ; 9521: 4c 3a 00    L:. :05d5[3]

.tube_osfile
    ldx #&10                                                          ; 9524: a2 10       ..  :05d8[3]
; &9526 referenced 1 time by &05e0[3]
.loop_c05da
    jsr tube_read_r2                                                  ; 9526: 20 f7 04     .. :05da[3]
    sta l0001,x                                                       ; 9529: 95 01       ..  :05dd[3]
    dex                                                               ; 952b: ca          .   :05df[3]
    bne loop_c05da                                                    ; 952c: d0 f8       ..  :05e0[3]
    jsr tube_read_string                                              ; 952e: 20 b1 05     .. :05e2[3]
    stx l0000                                                         ; 9531: 86 00       ..  :05e5[3]
    sty l0001                                                         ; 9533: 84 01       ..  :05e7[3]
    ldy #0                                                            ; 9535: a0 00       ..  :05e9[3]
    jsr tube_read_r2                                                  ; 9537: 20 f7 04     .. :05eb[3]
    jsr osfile                                                        ; 953a: 20 dd ff     .. :05ee[3]
    ora #&80                                                          ; 953d: 09 80       ..  :05f1[3]
    jsr tube_send_r2                                                  ; 953f: 20 d0 06     .. :05f3[3]
    ldx #&10                                                          ; 9542: a2 10       ..  :05f6[3]
; &9544 referenced 1 time by &05fe[3]
.loop_c05f8
    lda l0001,x                                                       ; 9544: b5 01       ..  :05f8[3]
    jsr tube_send_r2                                                  ; 9546: 20 d0 06     .. :05fa[3]
    dex                                                               ; 9549: ca          .   :05fd[3]
    bne loop_c05f8                                                    ; 954a: d0 f8       ..  :05fe[3]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_dispatch_table, *, l944c

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_dispatch_table, &0600

    ; Set the program counter to the next position in the binary file.
    org l944c + (* - tube_dispatch_table)

.c954c

; Move 4: &954c to &0600 for length 256
    org &0600
; Tube host code page 6 — reference: NFS13 (GBPB-ESCA)
; Copied from ROM at $954C during init. $0600-$0601 is the tail
; of tube_osfile (BEQ to tube_reply_byte when done). Contains:
;   $0602: tube_osgbpb — multi-byte file I/O
;   $0626: tube_osbyte_short — 2-param OSBYTE (returns X)
;   $063B: tube_osbyte_long — 3-param OSBYTE (returns carry+Y+X)
;   $065D: tube_osword — variable-length OSWORD (buffer at $0130)
;   $06A3: tube_osword_rdln — OSWORD 0 (read line, 5-byte params)
;   $06BB: tube_rdln_send_line — send input line from $0700
;   $06D0: tube_send_r2 — poll R2 status, write A to R2 data
;   $06D9: tube_send_r4 — poll R4 status, write A to R4 data
;   $06E2: tube_escape_check — check $FF, forward escape to R1
;   $06E8: tube_event_handler — EVNTV: forward event (A,X,Y) via R1
;   $06F7: tube_send_r1 — poll R1 status, write A to R1 data
; &954c referenced 1 time by &8108
.tube_code_page6
    beq c05d5                                                         ; 954c: f0 d3       ..  :0600[4]
.tube_osgbpb
    ldx #&0c                                                          ; 954e: a2 0c       ..  :0602[4]
; &9550 referenced 1 time by &060a[4]
.loop_c0604
    jsr tube_read_r2                                                  ; 9550: 20 f7 04     .. :0604[4]
    sta l0000,x                                                       ; 9553: 95 00       ..  :0607[4]
    dex                                                               ; 9555: ca          .   :0609[4]
    bpl loop_c0604                                                    ; 9556: 10 f8       ..  :060a[4]
    jsr tube_read_r2                                                  ; 9558: 20 f7 04     .. :060c[4]
    inx                                                               ; 955b: e8          .   :060f[4]
    ldy #0                                                            ; 955c: a0 00       ..  :0610[4]
    jsr osgbpb                                                        ; 955e: 20 d1 ff     .. :0612[4]   ; Read or write multiple bytes to an open file
    ror a                                                             ; 9561: 6a          j   :0615[4]
    jsr tube_send_r2                                                  ; 9562: 20 d0 06     .. :0616[4]
    ldx #&0c                                                          ; 9565: a2 0c       ..  :0619[4]
; &9567 referenced 1 time by &0621[4]
.loop_c061b
    lda l0000,x                                                       ; 9567: b5 00       ..  :061b[4]
    jsr tube_send_r2                                                  ; 9569: 20 d0 06     .. :061d[4]
    dex                                                               ; 956c: ca          .   :0620[4]
    bpl loop_c061b                                                    ; 956d: 10 f8       ..  :0621[4]
    jmp tube_main_loop                                                ; 956f: 4c 3a 00    L:. :0623[4]

.tube_osbyte_short
    jsr tube_read_r2                                                  ; 9572: 20 f7 04     .. :0626[4]
    tax                                                               ; 9575: aa          .   :0629[4]
    jsr tube_read_r2                                                  ; 9576: 20 f7 04     .. :062a[4]
    jsr osbyte                                                        ; 9579: 20 f4 ff     .. :062d[4]
; &957c referenced 2 times by &0633[4], &065b[4]
.tube_osbyte_send_x
    bit tube_status_register_2                                        ; 957c: 2c e2 fe    ,.. :0630[4]
    bvc tube_osbyte_send_x                                            ; 957f: 50 fb       P.  :0633[4]
    stx tube_data_register_2                                          ; 9581: 8e e3 fe    ... :0635[4]
; &9584 referenced 1 time by &064b[4]
.loop_c0638
    jmp tube_main_loop                                                ; 9584: 4c 3a 00    L:. :0638[4]

.tube_osbyte_long
    jsr tube_read_r2                                                  ; 9587: 20 f7 04     .. :063b[4]
    tax                                                               ; 958a: aa          .   :063e[4]
    jsr tube_read_r2                                                  ; 958b: 20 f7 04     .. :063f[4]
    tay                                                               ; 958e: a8          .   :0642[4]
    jsr tube_read_r2                                                  ; 958f: 20 f7 04     .. :0643[4]
    jsr osbyte                                                        ; 9592: 20 f4 ff     .. :0646[4]
    eor #&9d                                                          ; 9595: 49 9d       I.  :0649[4]
    beq loop_c0638                                                    ; 9597: f0 eb       ..  :064b[4]
    lda #&40 ; '@'                                                    ; 9599: a9 40       .@  :064d[4]
    ror a                                                             ; 959b: 6a          j   :064f[4]
    jsr tube_send_r2                                                  ; 959c: 20 d0 06     .. :0650[4]
; &959f referenced 1 time by &0656[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 959f: 2c e2 fe    ,.. :0653[4]
    bvc tube_osbyte_send_y                                            ; 95a2: 50 fb       P.  :0656[4]
    sty tube_data_register_2                                          ; 95a4: 8c e3 fe    ... :0658[4]
    bvs tube_osbyte_send_x                                            ; 95a7: 70 d3       p.  :065b[4]   ; ALWAYS branch

.tube_osword
    jsr tube_read_r2                                                  ; 95a9: 20 f7 04     .. :065d[4]
    tay                                                               ; 95ac: a8          .   :0660[4]
; &95ad referenced 1 time by &0664[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 95ad: 2c e2 fe    ,.. :0661[4]
    bpl tube_osword_read                                              ; 95b0: 10 fb       ..  :0664[4]
    ldx tube_data_register_2                                          ; 95b2: ae e3 fe    ... :0666[4]
    dex                                                               ; 95b5: ca          .   :0669[4]
    bmi c067b                                                         ; 95b6: 30 0f       0.  :066a[4]
; &95b8 referenced 2 times by &066f[4], &0678[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 95b8: 2c e2 fe    ,.. :066c[4]
    bpl tube_osword_read_lp                                           ; 95bb: 10 fb       ..  :066f[4]
    lda tube_data_register_2                                          ; 95bd: ad e3 fe    ... :0671[4]
    sta l0130,x                                                       ; 95c0: 9d 30 01    .0. :0674[4]
    dex                                                               ; 95c3: ca          .   :0677[4]
    bpl tube_osword_read_lp                                           ; 95c4: 10 f2       ..  :0678[4]
    tya                                                               ; 95c6: 98          .   :067a[4]
; &95c7 referenced 1 time by &066a[4]
.c067b
    ldx #<(l0130)                                                     ; 95c7: a2 30       .0  :067b[4]
    ldy #>(l0130)                                                     ; 95c9: a0 01       ..  :067d[4]
    jsr osword                                                        ; 95cb: 20 f1 ff     .. :067f[4]
    lda #&ff                                                          ; 95ce: a9 ff       ..  :0682[4]
    jsr tube_send_r2                                                  ; 95d0: 20 d0 06     .. :0684[4]
; &95d3 referenced 1 time by &068a[4]
.loop_c0687
    bit tube_status_register_2                                        ; 95d3: 2c e2 fe    ,.. :0687[4]
    bpl loop_c0687                                                    ; 95d6: 10 fb       ..  :068a[4]
    ldx tube_data_register_2                                          ; 95d8: ae e3 fe    ... :068c[4]
    dex                                                               ; 95db: ca          .   :068f[4]
    bmi tube_return_main                                              ; 95dc: 30 0e       0.  :0690[4]
; &95de referenced 1 time by &069e[4]
.tube_osword_write
    ldy l0130,x                                                       ; 95de: bc 30 01    .0. :0692[4]
; &95e1 referenced 1 time by &0698[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95e1: 2c e2 fe    ,.. :0695[4]
    bvc tube_osword_write_lp                                          ; 95e4: 50 fb       P.  :0698[4]
    sty tube_data_register_2                                          ; 95e6: 8c e3 fe    ... :069a[4]
    dex                                                               ; 95e9: ca          .   :069d[4]
    bpl tube_osword_write                                             ; 95ea: 10 f2       ..  :069e[4]
; &95ec referenced 1 time by &0690[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95ec: 4c 3a 00    L:. :06a0[4]

.tube_osword_rdln
    ldx #4                                                            ; 95ef: a2 04       ..  :06a3[4]
; &95f1 referenced 1 time by &06ab[4]
.loop_c06a5
    jsr tube_read_r2                                                  ; 95f1: 20 f7 04     .. :06a5[4]
    sta l0000,x                                                       ; 95f4: 95 00       ..  :06a8[4]
    dex                                                               ; 95f6: ca          .   :06aa[4]
    bpl loop_c06a5                                                    ; 95f7: 10 f8       ..  :06ab[4]
    inx                                                               ; 95f9: e8          .   :06ad[4]
    ldy #0                                                            ; 95fa: a0 00       ..  :06ae[4]
    txa                                                               ; 95fc: 8a          .   :06b0[4]
    jsr osword                                                        ; 95fd: 20 f1 ff     .. :06b1[4]
    bcc tube_rdln_send_line                                           ; 9600: 90 05       ..  :06b4[4]
    lda #&ff                                                          ; 9602: a9 ff       ..  :06b6[4]
    jmp tube_reply_byte                                               ; 9604: 4c cd 05    L.. :06b8[4]

; &9607 referenced 1 time by &06b4[4]
.tube_rdln_send_line
    ldx #0                                                            ; 9607: a2 00       ..  :06bb[4]
    lda #&7f                                                          ; 9609: a9 7f       ..  :06bd[4]
    jsr tube_send_r2                                                  ; 960b: 20 d0 06     .. :06bf[4]
; &960e referenced 1 time by &06cb[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 960e: bd 00 07    ... :06c2[4]
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 9611: 20 d0 06     .. :06c5[4]
    inx                                                               ; 9614: e8          .   :06c8[4]
    cmp #&0d                                                          ; 9615: c9 0d       ..  :06c9[4]
    bne tube_rdln_send_loop                                           ; 9617: d0 f5       ..  :06cb[4]
    jmp tube_main_loop                                                ; 9619: 4c 3a 00    L:. :06cd[4]

; &961c referenced 18 times by &0020[1], &0026[1], &002c[1], &04e9[2], &051f[3], &0562[3], &0579[3], &05a1[3], &05a8[3], &05f3[3], &05fa[3], &0616[4], &061d[4], &0650[4], &0684[4], &06bf[4], &06c5[4], &06d3[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 961c: 2c e2 fe    ,.. :06d0[4]
    bvc tube_send_r2                                                  ; 961f: 50 fb       P.  :06d3[4]
    sta tube_data_register_2                                          ; 9621: 8d e3 fe    ... :06d5[4]
    rts                                                               ; 9624: 60          `   :06d8[4]

; &9625 referenced 5 times by &0018[1], &042a[2], &0432[2], &0448[2], &06dc[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 9625: 2c e6 fe    ,.. :06d9[4]
    bvc tube_send_r4                                                  ; 9628: 50 fb       P.  :06dc[4]
    sta tube_data_register_4                                          ; 962a: 8d e7 fe    ... :06de[4]
    rts                                                               ; 962d: 60          `   :06e1[4]

; &962e referenced 1 time by &0403[2]
.tube_escape_check
    lda l00ff                                                         ; 962e: a5 ff       ..  :06e2[4]
    sec                                                               ; 9630: 38          8   :06e4[4]
    ror a                                                             ; 9631: 6a          j   :06e5[4]
    bmi tube_send_r1                                                  ; 9632: 30 0f       0.  :06e6[4]
.tube_event_handler
    pha                                                               ; 9634: 48          H   :06e8[4]
    lda #0                                                            ; 9635: a9 00       ..  :06e9[4]
    jsr tube_send_r1                                                  ; 9637: 20 f7 06     .. :06eb[4]
    tya                                                               ; 963a: 98          .   :06ee[4]
    jsr tube_send_r1                                                  ; 963b: 20 f7 06     .. :06ef[4]
    txa                                                               ; 963e: 8a          .   :06f2[4]
    jsr tube_send_r1                                                  ; 963f: 20 f7 06     .. :06f3[4]
    pla                                                               ; 9642: 68          h   :06f6[4]
; &9643 referenced 5 times by &06e6[4], &06eb[4], &06ef[4], &06f3[4], &06fa[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 9643: 2c e0 fe    ,.. :06f7[4]
    bvc tube_send_r1                                                  ; 9646: 50 fb       P.  :06fa[4]
    sta tube_data_register_1                                          ; 9648: 8d e1 fe    ... :06fc[4]
    rts                                                               ; 964b: 60          `   :06ff[4]


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page6, *, c954c

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page6, &0700

    ; Set the program counter to the next position in the binary file.
    org c954c + (* - tube_code_page6)

    equb &60, &ff, &42, &ff, 0, &ff, &77, &ff, &ff, &ff, &df, &ff     ; 964c: 60 ff 42... `.B
    equb   0, &ff,   0, &ff, 0, &ff,   4, &ff                         ; 9658: 00 ff 00... ...

; &9660 referenced 2 times by &8667, &8e49
.trampoline_tx_setup
    jmp c9be4                                                         ; 9660: 4c e4 9b    L..

; &9663 referenced 1 time by &82c9
.trampoline_adlc_init
    jmp adlc_init                                                     ; 9663: 4c 6f 96    Lo.

.svc_nmi_release
    jmp save_econet_state                                             ; 9666: 4c 9d 96    L..

.svc_nmi_claim
    jmp restore_econet_state                                          ; 9669: 4c b4 96    L..

.svc_unknown_irq
    jmp c9b52                                                         ; 966c: 4c 52 9b    LR.

; ADLC initialisation
; Reads station ID (INTOFF side effect), performs full ADLC reset,
; checks for Tube presence (OSBYTE $EA), then falls through to
; adlc_init_workspace.
; &966f referenced 1 time by &9663
.adlc_init
    bit station_id_disable_net_nmis                                   ; 966f: 2c 18 fe    ,..
    jsr adlc_full_reset                                               ; 9672: 20 dc 96     ..
    lda #osbyte_read_tube_presence                                    ; 9675: a9 ea       ..
    ldx #0                                                            ; 9677: a2 00       ..
    ldy #&ff                                                          ; 9679: a0 ff       ..
    jsr osbyte                                                        ; 967b: 20 f4 ff     ..            ; Read Tube present flag
    stx tx_in_progress                                                ; 967e: 8e 52 0d    .R.            ; X=value of Tube present flag
; Initialise NMI workspace
; Copies NMI shim from ROM to $0D00, stores current ROM bank number
; into shim self-modifying code, sets TX status to $80 (idle/complete),
; saves station ID from $FE18 into TX scout buffer, re-enables NMIs
; by reading $FE20.
; &9681 referenced 1 time by &96ca
.adlc_init_workspace
    jsr install_nmi_shim                                              ; 9681: 20 cd 96     ..
    lda romsel_copy                                                   ; 9684: a5 f4       ..
    sta nmi_shim_07                                                   ; 9686: 8d 07 0d    ...
    lda #&80                                                          ; 9689: a9 80       ..
    sta tx_ctrl_status                                                ; 968b: 8d 3a 0d    .:.
    lda station_id_disable_net_nmis                                   ; 968e: ad 18 fe    ...
    sta tx_src_stn                                                    ; 9691: 8d 22 0d    .".
    lda #0                                                            ; 9694: a9 00       ..
    sta tx_src_net                                                    ; 9696: 8d 23 0d    .#.
    bit video_ula_control                                             ; 9699: 2c 20 fe    , .
    rts                                                               ; 969c: 60          `

; Save Econet state to RX control block
; Stores rx_status_flags, protection_mask, and tx_in_progress
; to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.
; &969d referenced 1 time by &9666
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 969d: 2c 18 fe    ,..
    ldy #8                                                            ; 96a0: a0 08       ..
    lda rx_status_flags                                               ; 96a2: ad 38 0d    .8.
    sta (net_rx_ptr),y                                                ; 96a5: 91 9c       ..
    iny                                                               ; 96a7: c8          .              ; Y=&09
    lda prot_status                                                   ; 96a8: ad 63 0d    .c.
    sta (net_rx_ptr),y                                                ; 96ab: 91 9c       ..
    iny                                                               ; 96ad: c8          .              ; Y=&0a
    lda tx_in_progress                                                ; 96ae: ad 52 0d    .R.
    sta (net_rx_ptr),y                                                ; 96b1: 91 9c       ..
    rts                                                               ; 96b3: 60          `

; Restore Econet state from RX control block
; Loads rx_status_flags, protection_mask, and tx_in_progress
; from (net_rx_ptr) at offsets 8-10, then reinitialises via
; adlc_init_workspace.
; &96b4 referenced 1 time by &9669
.restore_econet_state
    bit station_id_disable_net_nmis                                   ; 96b4: 2c 18 fe    ,..
    ldy #8                                                            ; 96b7: a0 08       ..
    lda (net_rx_ptr),y                                                ; 96b9: b1 9c       ..
    sta rx_status_flags                                               ; 96bb: 8d 38 0d    .8.
    iny                                                               ; 96be: c8          .              ; Y=&09
    lda (net_rx_ptr),y                                                ; 96bf: b1 9c       ..
    sta prot_status                                                   ; 96c1: 8d 63 0d    .c.
    iny                                                               ; 96c4: c8          .              ; Y=&0a
    lda (net_rx_ptr),y                                                ; 96c5: b1 9c       ..
    sta tx_in_progress                                                ; 96c7: 8d 52 0d    .R.
    jmp adlc_init_workspace                                           ; 96ca: 4c 81 96    L..

; Copy NMI shim from ROM ($9FCA) to RAM ($0D00)
; Copies 32 bytes. Interrupts are enabled during the copy.
; &96cd referenced 1 time by &9681
.install_nmi_shim
    php                                                               ; 96cd: 08          .
    cli                                                               ; 96ce: 58          X
    ldy #&20 ; ' '                                                    ; 96cf: a0 20       .
; &96d1 referenced 1 time by &96d8
.loop_c96d1
    lda nmi_shim_rom_src,y                                            ; 96d1: b9 ca 9f    ...
    sta l0cff,y                                                       ; 96d4: 99 ff 0c    ...
    dey                                                               ; 96d7: 88          .
    bne loop_c96d1                                                    ; 96d8: d0 f7       ..
    plp                                                               ; 96da: 28          (
    rts                                                               ; 96db: 60          `

; ADLC full reset
; Aborts all activity and returns to idle RX listen mode.
; &96dc referenced 3 times by &9672, &973e, &9894
.adlc_full_reset
    lda #&c1                                                          ; 96dc: a9 c1       ..             ; CR1=$C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 96de: 8d a0 fe    ...
    lda #&1e                                                          ; 96e1: a9 1e       ..             ; CR4=$1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding
    sta econet_data_terminate_frame                                   ; 96e3: 8d a3 fe    ...
    lda #0                                                            ; 96e6: a9 00       ..             ; CR3=$00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 96e8: 8d a1 fe    ...
; Enter RX listen mode
; TX held in reset, RX active with interrupts. Clears all status.
; &96eb referenced 1 time by &9a40
.adlc_rx_listen
    lda #&82                                                          ; 96eb: a9 82       ..             ; CR1=$82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 96ed: 8d a0 fe    ...
    lda #&67 ; 'g'                                                    ; 96f0: a9 67       .g             ; CR2=$67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 96f2: 8d a1 fe    ...
    rts                                                               ; 96f5: 60          `

; NMI RX scout handler (initial byte)
; Default NMI handler for incoming scout frames. Checks if the frame
; is addressed to us or is a broadcast. Installed as the NMI target
; during idle RX listen mode.
; Tests SR2 bit0 (AP = Address Present) to detect incoming data.
; Reads the first byte (destination station) from the RX FIFO and
; compares against our station ID. Reading $FE18 also disables NMIs
; (INTOFF side effect).
; &96f6 referenced 1 time by &9fd6
.nmi_rx_scout
    lda #1                                                            ; 96f6: a9 01       ..             ; A=$01: mask for SR2 bit0 (AP = Address Present)
    bit econet_control23_or_status2                                   ; 96f8: 2c a1 fe    ,..            ; BIT SR2: Z = A AND SR2 -- tests if AP is set
    beq scout_error                                                   ; 96fb: f0 3a       .:             ; AP not set, no incoming data -- check for errors
    lda econet_data_continue_frame                                    ; 96fd: ad a2 fe    ...            ; Read first RX byte (destination station address)
    cmp station_id_disable_net_nmis                                   ; 9700: cd 18 fe    ...            ; Compare to our station ID ($FE18 read = INTOFF, disables NMIs)
    beq c970e                                                         ; 9703: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 9705: c9 ff       ..             ; Check for broadcast address ($FF)
    bne scout_reject                                                  ; 9707: d0 1a       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 9709: a9 40       .@             ; Flag $40 = broadcast frame
    sta tx_flags                                                      ; 970b: 8d 4a 0d    .J.
; &970e referenced 1 time by &9703
.c970e
    lda #&15                                                          ; 970e: a9 15       ..             ; Install next NMI handler at $9715 (RX scout second byte)
    ldy #&97                                                          ; 9710: a0 97       ..
    jmp set_nmi_vector                                                ; 9712: 4c 0e 0d    L..

; RX scout second byte handler
; Reads the second byte of an incoming scout (destination network).
; Checks for network match: 0 = local network (accept), $FF = broadcast
; (accept and flag), anything else = reject.
; Installs the scout data reading loop handler at $9747.
.nmi_rx_scout_net
    bit econet_control23_or_status2                                   ; 9715: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl scout_error                                                   ; 9718: 10 1d       ..             ; No RDA -- check errors
    lda econet_data_continue_frame                                    ; 971a: ad a2 fe    ...            ; Read destination network byte
    beq c972b                                                         ; 971d: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 971f: 49 ff       I.             ; EOR $FF: test if network = $FF (broadcast)
    beq c972e                                                         ; 9721: f0 0b       ..             ; Broadcast network -- accept
; &9723 referenced 1 time by &9707
.scout_reject
    lda #&a2                                                          ; 9723: a9 a2       ..             ; Reject: wrong network. CR1=$A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 9725: 8d a0 fe    ...
    jmp discard_after_reset                                           ; 9728: 4c 43 9a    LC.

; &972b referenced 1 time by &971d
.c972b
    sta tx_flags                                                      ; 972b: 8d 4a 0d    .J.            ; Network = $FF broadcast: clear $0D4A
; &972e referenced 1 time by &9721
.c972e
    sta port_buf_len                                                  ; 972e: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #&47 ; 'G'                                                    ; 9730: a9 47       .G             ; Install scout data reading loop at $9747
    ldy #&97                                                          ; 9732: a0 97       ..
    jmp set_nmi_vector                                                ; 9734: 4c 0e 0d    L..

; Scout error/discard handler
; Reached when the scout data loop sees no RDA (BPL at $974C) or
; when scout completion finds unexpected SR2 state.
; If SR2 & $81 is non-zero (AP or RDA still active), performs full
; ADLC reset and discards. If zero (clean end), discards via $9A40.
; This path is a common landing for any unexpected ADLC state during
; scout reception.
; &9737 referenced 5 times by &96fb, &9718, &974c, &9780, &9782
.scout_error
    lda econet_control23_or_status2                                   ; 9737: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 973a: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 973c: f0 06       ..             ; Neither set -- clean end, discard via $9A40
    jsr adlc_full_reset                                               ; 973e: 20 dc 96     ..            ; Unexpected data/status: full ADLC reset
    jmp discard_after_reset                                           ; 9741: 4c 43 9a    LC.            ; Discard and return to idle

; &9744 referenced 1 time by &973c
.scout_discard
    jmp discard_listen                                                ; 9744: 4c 40 9a    L@.

; Scout data reading loop
; Reads the body of a scout frame, two bytes per iteration. Stores
; bytes at $0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
; Between each pair it checks SR2:
;   - SR2 & $81 tested at entry ($974A): AP|RDA bits
;     - Neither set (BEQ) -> discard ($9744 -> $9A40)
;     - AP without RDA (BPL) -> error ($9737)
;     - RDA set (BMI) -> read byte
;   - After first byte ($9755): full SR2 tested
;     - SR2 non-zero (BNE) -> scout completion ($9771)
;       This is the FV detection point: when FV is set (by inline refill
;       of the last byte during the preceding RX FIFO read), SR2 is
;       non-zero and the branch is taken.
;     - SR2 = 0 -> read second byte and loop
;   - After second byte ($9769): re-test SR2 & $81 for next pair
;     - RDA set (BMI) -> loop back to $974E
;     - Neither set -> RTI, wait for next NMI
; The loop ends at Y=$0C (12 bytes max in scout buffer).
    ldy port_buf_len                                                  ; 9747: a4 a2       ..             ; Y = buffer offset
    lda econet_control23_or_status2                                   ; 9749: ad a1 fe    ...            ; Read SR2
; &974c referenced 1 time by &976c
.scout_loop_rda
    bpl scout_error                                                   ; 974c: 10 e9       ..             ; No RDA -- error handler $9737
    lda econet_data_continue_frame                                    ; 974e: ad a2 fe    ...            ; Read data byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9751: 99 3d 0d    .=.            ; Store at $0D3D+Y (scout buffer)
    iny                                                               ; 9754: c8          .              ; Advance buffer index
    lda econet_control23_or_status2                                   ; 9755: ad a1 fe    ...            ; Read SR2 again (FV detection point)
    bmi scout_loop_second                                             ; 9758: 30 02       0.             ; RDA set -- more data, read second byte
    bne scout_complete                                                ; 975a: d0 15       ..             ; SR2 non-zero (FV or other) -- scout completion
; &975c referenced 1 time by &9758
.scout_loop_second
    lda econet_data_continue_frame                                    ; 975c: ad a2 fe    ...            ; Read second byte of pair
    sta rx_src_stn,y                                                  ; 975f: 99 3d 0d    .=.            ; Store at $0D3D+Y
    iny                                                               ; 9762: c8          .              ; Advance and check buffer limit
    cpy #&0c                                                          ; 9763: c0 0c       ..
    beq scout_complete                                                ; 9765: f0 0a       ..             ; Buffer full (Y=12) -- force completion
    sty port_buf_len                                                  ; 9767: 84 a2       ..             ; Save Y for next iteration
    lda econet_control23_or_status2                                   ; 9769: ad a1 fe    ...            ; Read SR2 for next pair
    bne scout_loop_rda                                                ; 976c: d0 de       ..             ; SR2 non-zero -- loop back for more bytes
    jmp nmi_rti                                                       ; 976e: 4c 14 0d    L..            ; SR2 = 0 -- RTI, wait for next NMI

; Scout completion handler
; Reached from the scout data loop when SR2 is non-zero (FV detected).
; Disables PSE to allow individual SR2 bit testing:
;   CR1=$00 (clear all enables)
;   CR2=$84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
; Then checks FV (bit1) and RDA (bit7):
;   - No FV (BEQ) -> error $9737 (not a valid frame end)
;   - FV set, no RDA (BPL) -> error $9737 (missing last byte)
;   - FV set, RDA set -> read last byte, process scout
; After reading the last byte, the complete scout buffer ($0D3D-$0D48)
; contains: src_stn, src_net, ctrl, port [, extra_data...].
; The port byte at $0D40 determines further processing:
;   - Port = 0 -> immediate operation ($9A59)
;   - Port non-zero -> check if it matches an open receive block
; &9771 referenced 2 times by &975a, &9765
.scout_complete
    lda #0                                                            ; 9771: a9 00       ..             ; CR1=$00: disable all interrupts
    sta econet_control1_or_status1                                    ; 9773: 8d a0 fe    ...
    lda #&84                                                          ; 9776: a9 84       ..             ; CR2=$84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 9778: 8d a1 fe    ...
    lda #2                                                            ; 977b: a9 02       ..             ; A=$02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 977d: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 9780: f0 b5       ..             ; No FV -- not a valid frame end, error
    bpl scout_error                                                   ; 9782: 10 b3       ..             ; FV set but no RDA -- missing last byte, error
    lda econet_data_continue_frame                                    ; 9784: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9787: 99 3d 0d    .=.            ; Store last byte at $0D3D+Y
    lda #&44 ; 'D'                                                    ; 978a: a9 44       .D             ; CR1=$44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 978c: 8d a0 fe    ...
    lda rx_port                                                       ; 978f: ad 40 0d    .@.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 9792: d0 06       ..             ; Port non-zero -- look for matching receive block
    jmp immediate_op                                                  ; 9794: 4c 59 9a    LY.            ; Port = 0 -- immediate operation handler

; &9797 referenced 3 times by &97e2, &97e7, &9819
.scout_no_match
    jmp rx_error                                                      ; 9797: 4c 8a 98    L..

; &979a referenced 1 time by &9792
.scout_match_port
    bit tx_flags                                                      ; 979a: 2c 4a 0d    ,J.
    bvc c97a4                                                         ; 979d: 50 05       P.
    lda #7                                                            ; 979f: a9 07       ..
    sta econet_control23_or_status2                                   ; 97a1: 8d a1 fe    ...
; &97a4 referenced 1 time by &979d
.c97a4
    bit rx_status_flags                                               ; 97a4: 2c 38 0d    ,8.
    bpl c97e4                                                         ; 97a7: 10 3b       .;
    lda #&c0                                                          ; 97a9: a9 c0       ..
    sta port_ws_offset                                                ; 97ab: 85 a6       ..
    lda #0                                                            ; 97ad: a9 00       ..
    sta rx_buf_offset                                                 ; 97af: 85 a7       ..
; &97b1 referenced 1 time by &97de
.c97b1
    ldy #0                                                            ; 97b1: a0 00       ..
; &97b3 referenced 1 time by &97f1
.c97b3
    lda (port_ws_offset),y                                            ; 97b3: b1 a6       ..
    beq c97e0                                                         ; 97b5: f0 29       .)
    cmp #&7f                                                          ; 97b7: c9 7f       ..
    bne c97d7                                                         ; 97b9: d0 1c       ..
    iny                                                               ; 97bb: c8          .
    lda (port_ws_offset),y                                            ; 97bc: b1 a6       ..
    beq c97c5                                                         ; 97be: f0 05       ..
    cmp rx_port                                                       ; 97c0: cd 40 0d    .@.
    bne c97d7                                                         ; 97c3: d0 12       ..
; &97c5 referenced 1 time by &97be
.c97c5
    iny                                                               ; 97c5: c8          .
    lda (port_ws_offset),y                                            ; 97c6: b1 a6       ..
    beq c97cf                                                         ; 97c8: f0 05       ..
    cmp rx_src_stn                                                    ; 97ca: cd 3d 0d    .=.
    bne c97d7                                                         ; 97cd: d0 08       ..
; &97cf referenced 1 time by &97c8
.c97cf
    iny                                                               ; 97cf: c8          .
    lda (port_ws_offset),y                                            ; 97d0: b1 a6       ..
    cmp rx_src_net                                                    ; 97d2: cd 3e 0d    .>.
    beq c97f3                                                         ; 97d5: f0 1c       ..
; &97d7 referenced 3 times by &97b9, &97c3, &97cd
.c97d7
    lda port_ws_offset                                                ; 97d7: a5 a6       ..
    clc                                                               ; 97d9: 18          .
    adc #&0c                                                          ; 97da: 69 0c       i.
    sta port_ws_offset                                                ; 97dc: 85 a6       ..
    bcc c97b1                                                         ; 97de: 90 d1       ..
; &97e0 referenced 1 time by &97b5
.c97e0
    lda rx_buf_offset                                                 ; 97e0: a5 a7       ..
    bne scout_no_match                                                ; 97e2: d0 b3       ..
; &97e4 referenced 1 time by &97a7
.c97e4
    bit rx_status_flags                                               ; 97e4: 2c 38 0d    ,8.
    bvc scout_no_match                                                ; 97e7: 50 ae       P.
    lda nfs_workspace_hi                                              ; 97e9: a5 9f       ..
    sta rx_buf_offset                                                 ; 97eb: 85 a7       ..
    ldy #0                                                            ; 97ed: a0 00       ..
    sty port_ws_offset                                                ; 97ef: 84 a6       ..
    beq c97b3                                                         ; 97f1: f0 c0       ..             ; ALWAYS branch

; &97f3 referenced 1 time by &97d5
.c97f3
    bit tx_flags                                                      ; 97f3: 2c 4a 0d    ,J.
    bvc c97fb                                                         ; 97f6: 50 03       P.
    jmp c9a4a                                                         ; 97f8: 4c 4a 9a    LJ.

; &97fb referenced 1 time by &97f6
.c97fb
    lda #3                                                            ; 97fb: a9 03       ..
    sta scout_status                                                  ; 97fd: 8d 5c 0d    .\.
    lda nmi_tx_block                                                  ; 9800: a5 a0       ..
    pha                                                               ; 9802: 48          H
    lda nmi_tx_block_hi                                               ; 9803: a5 a1       ..
    pha                                                               ; 9805: 48          H
    lda port_ws_offset                                                ; 9806: a5 a6       ..
    sta nmi_tx_block                                                  ; 9808: 85 a0       ..
    lda rx_buf_offset                                                 ; 980a: a5 a7       ..
    sta nmi_tx_block_hi                                               ; 980c: 85 a1       ..
    jsr tx_calc_transfer                                              ; 980e: 20 5b 9f     [.
    pla                                                               ; 9811: 68          h
    sta nmi_tx_block_hi                                               ; 9812: 85 a1       ..
    pla                                                               ; 9814: 68          h
    sta nmi_tx_block                                                  ; 9815: 85 a0       ..
    bcs c981c                                                         ; 9817: b0 03       ..
    jmp scout_no_match                                                ; 9819: 4c 97 97    L..

; &981c referenced 1 time by &9817
.c981c
    lda #&44 ; 'D'                                                    ; 981c: a9 44       .D
    sta econet_control1_or_status1                                    ; 981e: 8d a0 fe    ...
    lda #&a7                                                          ; 9821: a9 a7       ..
    sta econet_control23_or_status2                                   ; 9823: 8d a1 fe    ...
    lda #&2d ; '-'                                                    ; 9826: a9 2d       .-
    ldy #&98                                                          ; 9828: a0 98       ..
    jmp ack_tx_write_dest                                             ; 982a: 4c 74 99    Lt.

.data_rx_setup
    lda #&82                                                          ; 982d: a9 82       ..             ; CR1=$82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 982f: 8d a0 fe    ...
    lda #&39 ; '9'                                                    ; 9832: a9 39       .9
    ldy #&98                                                          ; 9834: a0 98       ..
    jmp set_nmi_vector                                                ; 9836: 4c 0e 0d    L..

; Data frame RX handler (four-way handshake)
; Receives the data frame after the scout ACK has been sent.
; First checks AP (Address Present) for the start of the data frame.
; Reads and validates the first two address bytes (dest_stn, dest_net)
; against our station address, then installs continuation handlers
; to read the remaining data payload into the open port buffer.
; 
; Handler chain: $9839 (AP+addr check) -> $984F (net=0 check) ->
; $9865 (skip ctrl+port) -> $989A (bulk data read) -> $98CE (completion)
.nmi_data_rx
    lda #1                                                            ; 9839: a9 01       ..             ; Read SR2 for AP check
    bit econet_control23_or_status2                                   ; 983b: 2c a1 fe    ,..
    beq rx_error                                                      ; 983e: f0 4a       .J
    lda econet_data_continue_frame                                    ; 9840: ad a2 fe    ...
    cmp station_id_disable_net_nmis                                   ; 9843: cd 18 fe    ...
    bne rx_error                                                      ; 9846: d0 42       .B
    lda #&4f ; 'O'                                                    ; 9848: a9 4f       .O
    ldy #&98                                                          ; 984a: a0 98       ..
    jmp set_nmi_vector                                                ; 984c: 4c 0e 0d    L..

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 984f: 2c a1 fe    ,..            ; Validate source network = 0
    bpl rx_error                                                      ; 9852: 10 36       .6
    lda econet_data_continue_frame                                    ; 9854: ad a2 fe    ...
    bne rx_error                                                      ; 9857: d0 31       .1
    lda #&65 ; 'e'                                                    ; 9859: a9 65       .e
    ldy #&98                                                          ; 985b: a0 98       ..
    bit econet_control1_or_status1                                    ; 985d: 2c a0 fe    ,..
    bmi nmi_data_rx_skip                                              ; 9860: 30 03       0.
    jmp set_nmi_vector                                                ; 9862: 4c 0e 0d    L..

; &9865 referenced 1 time by &9860
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 9865: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl rx_error                                                      ; 9868: 10 20       .
    lda econet_data_continue_frame                                    ; 986a: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 986d: ad a2 fe    ...            ; Discard port byte
; &9870 referenced 1 time by &9f2f
.c9870
    lda #2                                                            ; 9870: a9 02       ..
    bit tx_flags                                                      ; 9872: 2c 4a 0d    ,J.
    bne c9883                                                         ; 9875: d0 0c       ..
    lda #&9a                                                          ; 9877: a9 9a       ..
    ldy #&98                                                          ; 9879: a0 98       ..
    bit econet_control1_or_status1                                    ; 987b: 2c a0 fe    ,..
    bmi nmi_data_rx_bulk                                              ; 987e: 30 1a       0.
    jmp set_nmi_vector                                                ; 9880: 4c 0e 0d    L..

; &9883 referenced 1 time by &9875
.c9883
    lda #&f7                                                          ; 9883: a9 f7       ..
    ldy #&98                                                          ; 9885: a0 98       ..
    jmp set_nmi_vector                                                ; 9887: 4c 0e 0d    L..

; &988a referenced 12 times by &9797, &983e, &9846, &9852, &9857, &9868, &98ad, &98df, &98e5, &9930, &99b8, &9a8c
.rx_error
    lda tx_flags                                                      ; 988a: ad 4a 0d    .J.
    bpl rx_error_reset                                                ; 988d: 10 05       ..
    lda #&41 ; 'A'                                                    ; 988f: a9 41       .A
    jmp tx_store_result                                               ; 9891: 4c 3f 9f    L?.

; &9894 referenced 1 time by &988d
.rx_error_reset
    jsr adlc_full_reset                                               ; 9894: 20 dc 96     ..
    jmp discard_reset_listen                                          ; 9897: 4c 34 9a    L4.

; Data frame bulk read loop
; Reads data payload bytes from the RX FIFO and stores them into
; the open port buffer at (open_port_buf),Y. Reads bytes in pairs
; (like the scout data loop), checking SR2 between each pair.
; SR2 non-zero (FV or other) -> frame completion at $98CE.
; SR2 = 0 -> RTI, wait for next NMI to continue.
; &989a referenced 1 time by &987e
.nmi_data_rx_bulk
    ldy port_buf_len                                                  ; 989a: a4 a2       ..             ; Y = buffer offset, resume from last position
    lda econet_control23_or_status2                                   ; 989c: ad a1 fe    ...            ; Read SR2 for next pair
; &989f referenced 1 time by &98c9
.c989f
    bpl data_rx_complete                                              ; 989f: 10 2d       .-
    lda econet_data_continue_frame                                    ; 98a1: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 98a4: 91 a4       ..
    iny                                                               ; 98a6: c8          .
    bne c98af                                                         ; 98a7: d0 06       ..
    inc open_port_buf_hi                                              ; 98a9: e6 a5       ..
    dec port_buf_len_hi                                               ; 98ab: c6 a3       ..
    beq rx_error                                                      ; 98ad: f0 db       ..
; &98af referenced 1 time by &98a7
.c98af
    lda econet_control23_or_status2                                   ; 98af: ad a1 fe    ...
    bmi c98b6                                                         ; 98b2: 30 02       0.
    bne data_rx_complete                                              ; 98b4: d0 18       ..
; &98b6 referenced 1 time by &98b2
.c98b6
    lda econet_data_continue_frame                                    ; 98b6: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 98b9: 91 a4       ..
    iny                                                               ; 98bb: c8          .
    sty port_buf_len                                                  ; 98bc: 84 a2       ..
    bne c98c6                                                         ; 98be: d0 06       ..
    inc open_port_buf_hi                                              ; 98c0: e6 a5       ..
    dec port_buf_len_hi                                               ; 98c2: c6 a3       ..
    beq data_rx_complete                                              ; 98c4: f0 08       ..
; &98c6 referenced 1 time by &98be
.c98c6
    lda econet_control23_or_status2                                   ; 98c6: ad a1 fe    ...
    bne c989f                                                         ; 98c9: d0 d4       ..
    jmp nmi_rti                                                       ; 98cb: 4c 14 0d    L..

; Data frame completion
; Reached when SR2 non-zero during data RX (FV detected).
; Same pattern as scout completion ($9771): disables PSE (CR1=$00,
; CR2=$84), then tests FV and RDA. If FV+RDA, reads the last byte.
; If extra data available and buffer space remains, stores it.
; Proceeds to send the final ACK via $995E.
; &98ce referenced 3 times by &989f, &98b4, &98c4
.data_rx_complete
    lda #0                                                            ; 98ce: a9 00       ..             ; CR1=$00: disable all interrupts
    sta econet_control1_or_status1                                    ; 98d0: 8d a0 fe    ...
    lda #&84                                                          ; 98d3: a9 84       ..             ; CR2=$84: disable PSE for individual bit testing
    sta econet_control23_or_status2                                   ; 98d5: 8d a1 fe    ...
    sty port_buf_len                                                  ; 98d8: 84 a2       ..
    lda #2                                                            ; 98da: a9 02       ..             ; A=$02: FV mask
    bit econet_control23_or_status2                                   ; 98dc: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq rx_error                                                      ; 98df: f0 a9       ..             ; No FV -- error
    bpl c98f4                                                         ; 98e1: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 98e3: a5 a3       ..
    beq rx_error                                                      ; 98e5: f0 a3       ..
    lda econet_data_continue_frame                                    ; 98e7: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 98ea: a4 a2       ..
    sta (open_port_buf),y                                             ; 98ec: 91 a4       ..
    inc port_buf_len                                                  ; 98ee: e6 a2       ..
    bne c98f4                                                         ; 98f0: d0 02       ..
    inc open_port_buf_hi                                              ; 98f2: e6 a5       ..
; &98f4 referenced 2 times by &98e1, &98f0
.c98f4
    jmp ack_tx                                                        ; 98f4: 4c 5e 99    L^.

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 98f7: ad a1 fe    ...
; &98fa referenced 1 time by &992b
.c98fa
    bpl data_rx_tube_complete                                         ; 98fa: 10 37       .7
    lda econet_data_continue_frame                                    ; 98fc: ad a2 fe    ...
    inc port_buf_len                                                  ; 98ff: e6 a2       ..
    sta tube_data_register_3                                          ; 9901: 8d e5 fe    ...
    bne c9912                                                         ; 9904: d0 0c       ..
    inc port_buf_len_hi                                               ; 9906: e6 a3       ..
    bne c9912                                                         ; 9908: d0 08       ..
    inc open_port_buf                                                 ; 990a: e6 a4       ..
    bne c9912                                                         ; 990c: d0 04       ..
    inc open_port_buf_hi                                              ; 990e: e6 a5       ..
    beq data_rx_tube_error                                            ; 9910: f0 1e       ..
; &9912 referenced 3 times by &9904, &9908, &990c
.c9912
    lda econet_data_continue_frame                                    ; 9912: ad a2 fe    ...
    sta tube_data_register_3                                          ; 9915: 8d e5 fe    ...
    inc port_buf_len                                                  ; 9918: e6 a2       ..
    bne c9928                                                         ; 991a: d0 0c       ..
    inc port_buf_len_hi                                               ; 991c: e6 a3       ..
    bne c9928                                                         ; 991e: d0 08       ..
    inc open_port_buf                                                 ; 9920: e6 a4       ..
    bne c9928                                                         ; 9922: d0 04       ..
    inc open_port_buf_hi                                              ; 9924: e6 a5       ..
    beq data_rx_tube_complete                                         ; 9926: f0 0b       ..
; &9928 referenced 3 times by &991a, &991e, &9922
.c9928
    lda econet_control23_or_status2                                   ; 9928: ad a1 fe    ...
    bne c98fa                                                         ; 992b: d0 cd       ..
    jmp nmi_rti                                                       ; 992d: 4c 14 0d    L..

; &9930 referenced 3 times by &9910, &9942, &994e
.data_rx_tube_error
    jmp rx_error                                                      ; 9930: 4c 8a 98    L..

; &9933 referenced 2 times by &98fa, &9926
.data_rx_tube_complete
    lda #0                                                            ; 9933: a9 00       ..
    sta econet_control1_or_status1                                    ; 9935: 8d a0 fe    ...
    lda #&84                                                          ; 9938: a9 84       ..
    sta econet_control23_or_status2                                   ; 993a: 8d a1 fe    ...
    lda #2                                                            ; 993d: a9 02       ..
    bit econet_control23_or_status2                                   ; 993f: 2c a1 fe    ,..
    beq data_rx_tube_error                                            ; 9942: f0 ec       ..
    bpl ack_tx                                                        ; 9944: 10 18       ..
    lda port_buf_len                                                  ; 9946: a5 a2       ..
    ora port_buf_len_hi                                               ; 9948: 05 a3       ..
    ora open_port_buf                                                 ; 994a: 05 a4       ..
    ora open_port_buf_hi                                              ; 994c: 05 a5       ..
    beq data_rx_tube_error                                            ; 994e: f0 e0       ..
    lda econet_data_continue_frame                                    ; 9950: ad a2 fe    ...
    sta rx_extra_byte                                                 ; 9953: 8d 5d 0d    .].
    lda #&20 ; ' '                                                    ; 9956: a9 20       .
    ora tx_flags                                                      ; 9958: 0d 4a 0d    .J.
    sta tx_flags                                                      ; 995b: 8d 4a 0d    .J.
; ACK transmission
; Sends a scout ACK or final ACK frame as part of the four-way handshake.
; If bit7 of $0D4A is set, this is a final ACK -> completion ($9F39).
; Otherwise, configures for TX (CR1=$44, CR2=$A7) and sends the ACK
; frame (dst_stn, dst_net from $0D3D, src_stn from $FE18, src_net=0).
; The ACK frame has no data payload -- just address bytes.
; 
; After writing the address bytes to the TX FIFO, installs the next
; NMI handler from $0D4B/$0D4C (saved by the scout/data RX handler)
; and sends TX_LAST_DATA (CR2=$3F) to close the frame.
; &995e referenced 2 times by &98f4, &9944
.ack_tx
    lda tx_flags                                                      ; 995e: ad 4a 0d    .J.
    bpl ack_tx_configure                                              ; 9961: 10 03       ..
    jmp tx_result_ok                                                  ; 9963: 4c 39 9f    L9.

; &9966 referenced 1 time by &9961
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 9966: a9 44       .D             ; CR1=$44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 9968: 8d a0 fe    ...
    lda #&a7                                                          ; 996b: a9 a7       ..             ; CR2=$A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 996d: 8d a1 fe    ...
    lda #&bb                                                          ; 9970: a9 bb       ..             ; Install saved next handler ($99BB for scout ACK)
    ldy #&99                                                          ; 9972: a0 99       ..
; &9974 referenced 1 time by &982a
.ack_tx_write_dest
    sta nmi_next_lo                                                   ; 9974: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 9977: 8c 4c 0d    .L.
    lda rx_src_stn                                                    ; 997a: ad 3d 0d    .=.            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 997d: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc c99b8                                                         ; 9980: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9982: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda rx_src_net                                                    ; 9985: ad 3e 0d    .>.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9988: 8d a2 fe    ...
    lda #&92                                                          ; 998b: a9 92       ..             ; Install handler at $9992 (write src addr)
    ldy #&99                                                          ; 998d: a0 99       ..
    jmp set_nmi_vector                                                ; 998f: 4c 0e 0d    L..

; ACK TX continuation
; Writes source station and network to TX FIFO, completing the 4-byte
; ACK frame. Then sends TX_LAST_DATA (CR2=$3F) to close the frame.
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 9992: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9995: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc c99b8                                                         ; 9998: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 999a: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 999d: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 999f: 8d a2 fe    ...
    lda tx_flags                                                      ; 99a2: ad 4a 0d    .J.
    bmi c99b5                                                         ; 99a5: 30 0e       0.
    lda #&3f ; '?'                                                    ; 99a7: a9 3f       .?             ; CR2=$3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 99a9: 8d a1 fe    ...
    lda nmi_next_lo                                                   ; 99ac: ad 4b 0d    .K.            ; Install saved handler from $0D4B/$0D4C
    ldy nmi_next_hi                                                   ; 99af: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 99b2: 4c 0e 0d    L..

; &99b5 referenced 1 time by &99a5
.c99b5
    jmp data_tx_begin                                                 ; 99b5: 4c 3b 9e    L;.

; &99b8 referenced 2 times by &9980, &9998
.c99b8
    jmp rx_error                                                      ; 99b8: 4c 8a 98    L..

; Post-ACK scout processing
; Called after the scout ACK has been transmitted. Processes the
; received scout data stored in the buffer at $0D3D-$0D48.
; Checks the port byte ($0D40) against open receive blocks to
; find a matching listener. If a match is found, sets up the
; data RX handler chain for the four-way handshake data phase.
; If no match, discards the frame.
.post_ack_scout
    lda rx_port                                                       ; 99bb: ad 40 0d    .@.
    bne c99c3                                                         ; 99be: d0 03       ..
    jmp c9b12                                                         ; 99c0: 4c 12 9b    L..

; &99c3 referenced 1 time by &99be
.c99c3
    lda #2                                                            ; 99c3: a9 02       ..
    bit tx_flags                                                      ; 99c5: 2c 4a 0d    ,J.
    beq c9a07                                                         ; 99c8: f0 3d       .=
    clc                                                               ; 99ca: 18          .
    php                                                               ; 99cb: 08          .
    ldy #8                                                            ; 99cc: a0 08       ..
; &99ce referenced 1 time by &99da
.loop_c99ce
    lda (port_ws_offset),y                                            ; 99ce: b1 a6       ..
    plp                                                               ; 99d0: 28          (
    adc net_tx_ptr,y                                                  ; 99d1: 79 9a 00    y..
    sta (port_ws_offset),y                                            ; 99d4: 91 a6       ..
    iny                                                               ; 99d6: c8          .
    php                                                               ; 99d7: 08          .
    cpy #&0c                                                          ; 99d8: c0 0c       ..
    bcc loop_c99ce                                                    ; 99da: 90 f2       ..
    plp                                                               ; 99dc: 28          (
    lda #&20 ; ' '                                                    ; 99dd: a9 20       .
    bit tx_flags                                                      ; 99df: 2c 4a 0d    ,J.
    beq c9a04                                                         ; 99e2: f0 20       .
    txa                                                               ; 99e4: 8a          .
    pha                                                               ; 99e5: 48          H
    lda #8                                                            ; 99e6: a9 08       ..
    clc                                                               ; 99e8: 18          .
    adc port_ws_offset                                                ; 99e9: 65 a6       e.
    tax                                                               ; 99eb: aa          .
    ldy rx_buf_offset                                                 ; 99ec: a4 a7       ..
    lda #1                                                            ; 99ee: a9 01       ..
    jsr tube_addr_claim                                               ; 99f0: 20 06 04     ..
    lda rx_extra_byte                                                 ; 99f3: ad 5d 0d    .].
    sta tube_data_register_3                                          ; 99f6: 8d e5 fe    ...
    pla                                                               ; 99f9: 68          h
    tax                                                               ; 99fa: aa          .
    ldy #8                                                            ; 99fb: a0 08       ..
    lda (port_ws_offset),y                                            ; 99fd: b1 a6       ..
    sec                                                               ; 99ff: 38          8
    adc #0                                                            ; 9a00: 69 00       i.
    sta (port_ws_offset),y                                            ; 9a02: 91 a6       ..
; &9a04 referenced 1 time by &99e2
.c9a04
    jmp c9a19                                                         ; 9a04: 4c 19 9a    L..

; &9a07 referenced 1 time by &99c8
.c9a07
    lda port_buf_len                                                  ; 9a07: a5 a2       ..
    clc                                                               ; 9a09: 18          .
    adc open_port_buf                                                 ; 9a0a: 65 a4       e.
    bcc c9a10                                                         ; 9a0c: 90 02       ..
; &9a0e referenced 1 time by &9a87
.c9a0e
    inc open_port_buf_hi                                              ; 9a0e: e6 a5       ..
; &9a10 referenced 1 time by &9a0c
.c9a10
    ldy #8                                                            ; 9a10: a0 08       ..
    sta (port_ws_offset),y                                            ; 9a12: 91 a6       ..
    iny                                                               ; 9a14: c8          .              ; Y=&09
.sub_c9a15
l9a16 = sub_c9a15+1
    lda open_port_buf_hi                                              ; 9a15: a5 a5       ..
; &9a16 referenced 1 time by &9a83
    sta (port_ws_offset),y                                            ; 9a17: 91 a6       ..
; &9a19 referenced 2 times by &9a04, &9a56
.c9a19
    lda rx_src_net                                                    ; 9a19: ad 3e 0d    .>.
    ldy #3                                                            ; 9a1c: a0 03       ..
    sta (port_ws_offset),y                                            ; 9a1e: 91 a6       ..
    dey                                                               ; 9a20: 88          .              ; Y=&02
    lda rx_src_stn                                                    ; 9a21: ad 3d 0d    .=.
    sta (port_ws_offset),y                                            ; 9a24: 91 a6       ..
    dey                                                               ; 9a26: 88          .              ; Y=&01
    lda rx_port                                                       ; 9a27: ad 40 0d    .@.
    sta (port_ws_offset),y                                            ; 9a2a: 91 a6       ..
    dey                                                               ; 9a2c: 88          .              ; Y=&00
    lda rx_ctrl                                                       ; 9a2d: ad 3f 0d    .?.
    ora #&80                                                          ; 9a30: 09 80       ..
    sta (port_ws_offset),y                                            ; 9a32: 91 a6       ..
; Discard with full ADLC reset
; Performs adlc_full_reset (CR1=$C1, reset both TX and RX sections),
; then falls through to discard_after_reset. Used when the ADLC is
; in an unexpected state and needs a hard reset before returning
; to idle listen mode. 5 references — the main error recovery path.
; &9a34 referenced 4 times by &9897, &9b4f, &9e93, &9f48
.discard_reset_listen
    lda #2                                                            ; 9a34: a9 02       ..
    bit tx_flags                                                      ; 9a36: 2c 4a 0d    ,J.
    beq discard_listen                                                ; 9a39: f0 05       ..
    lda #&82                                                          ; 9a3b: a9 82       ..
    jsr tube_addr_claim                                               ; 9a3d: 20 06 04     ..
; Discard frame (gentle)
; Sends RX_DISCONTINUE (CR1=$A2: RIE|RX_DISCONTINUE) to abort the
; current frame reception without a full reset, then falls through
; to discard_after_reset. Used for clean rejection of frames that
; are correctly formatted but not for us (wrong station/network).
; &9a40 referenced 2 times by &9744, &9a39
.discard_listen
    jsr adlc_rx_listen                                                ; 9a40: 20 eb 96     ..
; Return to idle listen after reset/discard
; Just calls adlc_rx_listen (CR1=$82, CR2=$67) to re-enter idle
; RX mode, then RTI. The simplest of the three discard paths —
; used as the tail of both discard_reset_listen and discard_listen.
; &9a43 referenced 2 times by &9728, &9741
.discard_after_reset
    lda #&f6                                                          ; 9a43: a9 f6       ..
    ldy #&96                                                          ; 9a45: a0 96       ..
    jmp set_nmi_vector                                                ; 9a47: 4c 0e 0d    L..

; &9a4a referenced 1 time by &97f8
.c9a4a
    ldy #4                                                            ; 9a4a: a0 04       ..
; &9a4c referenced 1 time by &9a54
.loop_c9a4c
    lda rx_src_stn,y                                                  ; 9a4c: b9 3d 0d    .=.
    sta (port_ws_offset),y                                            ; 9a4f: 91 a6       ..
    iny                                                               ; 9a51: c8          .
    cpy #&0c                                                          ; 9a52: c0 0c       ..
    bne loop_c9a4c                                                    ; 9a54: d0 f6       ..
    jmp c9a19                                                         ; 9a56: 4c 19 9a    L..

; Immediate operation handler (port = 0)
; Handles immediate (non-data-transfer) operations received via
; scout frames with port byte = 0. The control byte ($0D3F)
; determines the operation type:
;   $81 = PEEK (read memory)
;   $82 = POKE (write memory)
;   $83 = JSR (remote procedure call)
;   $84 = user procedure
;   $85 = OS procedure
;   $86 = HALT
;   $87 = CONTINUE
; The protection mask (LSTAT at $D63) controls which operations
; are permitted — each bit enables or disables an operation type.
; If the operation is not permitted by the mask, it is silently
; ignored. LSTAT can be read/set via OSWORD $12 sub-functions 4/5.
; &9a59 referenced 1 time by &9794
.immediate_op
    ldy rx_ctrl                                                       ; 9a59: ac 3f 0d    .?.
    cpy #&81                                                          ; 9a5c: c0 81       ..
    bcc c9a8c                                                         ; 9a5e: 90 2c       .,
    cpy #&89                                                          ; 9a60: c0 89       ..
    bcs c9a8c                                                         ; 9a62: b0 28       .(
    cpy #&87                                                          ; 9a64: c0 87       ..
    bcs c9a80                                                         ; 9a66: b0 18       ..
    lda rx_src_stn                                                    ; 9a68: ad 3d 0d    .=.
    cmp #&f0                                                          ; 9a6b: c9 f0       ..
    bcs c9a80                                                         ; 9a6d: b0 11       ..
    tya                                                               ; 9a6f: 98          .
    sec                                                               ; 9a70: 38          8
    sbc #&81                                                          ; 9a71: e9 81       ..
    tay                                                               ; 9a73: a8          .
    lda prot_status                                                   ; 9a74: ad 63 0d    .c.
; &9a77 referenced 1 time by &9a79
.loop_c9a77
    ror a                                                             ; 9a77: 6a          j
    dey                                                               ; 9a78: 88          .
    bpl loop_c9a77                                                    ; 9a79: 10 fc       ..
    bcc c9a80                                                         ; 9a7b: 90 03       ..
    jmp c9b4f                                                         ; 9a7d: 4c 4f 9b    LO.

; &9a80 referenced 3 times by &9a66, &9a6d, &9a7b
.c9a80
    ldy rx_ctrl                                                       ; 9a80: ac 3f 0d    .?.
    lda l9a16,y                                                       ; 9a83: b9 16 9a    ...
    pha                                                               ; 9a86: 48          H
    lda c9a0e,y                                                       ; 9a87: b9 0e 9a    ...
    pha                                                               ; 9a8a: 48          H
    rts                                                               ; 9a8b: 60          `

; &9a8c referenced 2 times by &9a5e, &9a62
.c9a8c
    jmp rx_error                                                      ; 9a8c: 4c 8a 98    L..

    equb &da, &bc, &9e, &9e, &9e,   0,   0, &c7, &9a, &9a, &9a, &9a   ; 9a8f: da bc 9e... ...
    equb &9a, &9b, &9b, &9a, &a9,   0, &85, &a4, &a9, &82, &85, &a2   ; 9a9b: 9a 9b 9b... ...
    equb &a9,   1, &85, &a3, &a5, &9d, &85, &a5, &a0,   3, &b9, &41   ; 9aa7: a9 01 85... ...
    equb &0d, &99, &58, &0d, &88, &10, &f7, &4c, &1c, &98, &a9, &3d   ; 9ab3: 0d 99 58... ..X
    equb &85, &a6, &a9, &0d, &85, &a7, &4c, &fb, &97, &a9,   1, &85   ; 9abf: 85 a6 a9... ...
    equb &a3, &a9, &fc, &85, &a2, &a9, &21, &85, &a4, &a9, &7f, &85   ; 9acb: a3 a9 fc... ...
    equb &a5, &4c, &f9, &9a, &a5, &a0, &48, &a5, &a1, &48, &a9, &3d   ; 9ad7: a5 4c f9... .L.
    equb &85, &a0, &a9, &0d, &85, &a1, &a9,   2, &8d, &5c, &0d, &20   ; 9ae3: 85 a0 a9... ...
    equb &5b, &9f, &68, &85, &a1, &68, &85, &a0, &90, &56, &ad, &4a   ; 9aef: 5b 9f 68... [.h
    equb &0d,   9, &80, &8d, &4a, &0d, &a9, &44, &8d, &a0, &fe, &a9   ; 9afb: 0d 09 80... ...
    equb &a7, &8d, &a1, &fe, &a9, &2f, &a0                            ; 9b07: a7 8d a1... ...
; &9b0e referenced 1 time by &9b8c
.l9b0e
    equb &9b, &4c, &74, &99                                           ; 9b0e: 9b 4c 74... .Lt

; &9b12 referenced 1 time by &99c0
.c9b12
l9b13 = c9b12+1
    ldy rx_ctrl                                                       ; 9b12: ac 3f 0d    .?.
; &9b13 referenced 1 time by &9b88
    cpy #&82                                                          ; 9b15: c0 82       ..
    beq c9b4f                                                         ; 9b17: f0 36       .6
    lda port_buf_len                                                  ; 9b19: a5 a2       ..
    clc                                                               ; 9b1b: 18          .
    adc #&80                                                          ; 9b1c: 69 80       i.
    ldy #&7f                                                          ; 9b1e: a0 7f       ..
    sta (net_rx_ptr),y                                                ; 9b20: 91 9c       ..
    ldy #&80                                                          ; 9b22: a0 80       ..
    lda rx_src_stn                                                    ; 9b24: ad 3d 0d    .=.
    sta (net_rx_ptr),y                                                ; 9b27: 91 9c       ..
    iny                                                               ; 9b29: c8          .              ; Y=&81
    lda rx_src_net                                                    ; 9b2a: ad 3e 0d    .>.
    sta (net_rx_ptr),y                                                ; 9b2d: 91 9c       ..
    lda rx_ctrl                                                       ; 9b2f: ad 3f 0d    .?.
    sta tx_work_57                                                    ; 9b32: 8d 57 0d    .W.
    lda #&84                                                          ; 9b35: a9 84       ..
    sta system_via_ier                                                ; 9b37: 8d 4e fe    .N.
    lda system_via_acr                                                ; 9b3a: ad 4b fe    .K.
    and #&1c                                                          ; 9b3d: 29 1c       ).
    sta tx_work_51                                                    ; 9b3f: 8d 51 0d    .Q.
    lda system_via_acr                                                ; 9b42: ad 4b fe    .K.
    and #&e3                                                          ; 9b45: 29 e3       ).
    ora #8                                                            ; 9b47: 09 08       ..
    sta system_via_acr                                                ; 9b49: 8d 4b fe    .K.
    bit system_via_sr                                                 ; 9b4c: 2c 4a fe    ,J.
; &9b4f referenced 2 times by &9a7d, &9b17
.c9b4f
    jmp discard_reset_listen                                          ; 9b4f: 4c 34 9a    L4.

; &9b52 referenced 1 time by &966c
.c9b52
    lda #4                                                            ; 9b52: a9 04       ..
    bit system_via_ifr                                                ; 9b54: 2c 4d fe    ,M.
    bne c9b5c                                                         ; 9b57: d0 03       ..
    lda #5                                                            ; 9b59: a9 05       ..
    rts                                                               ; 9b5b: 60          `

; &9b5c referenced 1 time by &9b57
.c9b5c
    txa                                                               ; 9b5c: 8a          .
    pha                                                               ; 9b5d: 48          H
    tya                                                               ; 9b5e: 98          .
    pha                                                               ; 9b5f: 48          H
    lda system_via_acr                                                ; 9b60: ad 4b fe    .K.
    and #&e3                                                          ; 9b63: 29 e3       ).
    ora tx_work_51                                                    ; 9b65: 0d 51 0d    .Q.
    sta system_via_acr                                                ; 9b68: 8d 4b fe    .K.
    lda system_via_sr                                                 ; 9b6b: ad 4a fe    .J.
    lda #4                                                            ; 9b6e: a9 04       ..
    sta system_via_ifr                                                ; 9b70: 8d 4d fe    .M.
    sta system_via_ier                                                ; 9b73: 8d 4e fe    .N.
    ldy tx_work_57                                                    ; 9b76: ac 57 0d    .W.
    cpy #&86                                                          ; 9b79: c0 86       ..
    bcs c9b88                                                         ; 9b7b: b0 0b       ..
    lda prot_status                                                   ; 9b7d: ad 63 0d    .c.
    sta rx_ctrl_copy                                                  ; 9b80: 8d 3b 0d    .;.
    ora #&1c                                                          ; 9b83: 09 1c       ..
    sta prot_status                                                   ; 9b85: 8d 63 0d    .c.
; &9b88 referenced 1 time by &9b7b
.c9b88
    lda l9b13,y                                                       ; 9b88: b9 13 9b    ...
    pha                                                               ; 9b8b: 48          H
    lda l9b0e,y                                                       ; 9b8c: b9 0e 9b    ...
    pha                                                               ; 9b8f: 48          H
    rts                                                               ; 9b90: 60          `

    equb &9a, &a3, &b1, &bd, &d4, &9b, &9b, &9b, &9b, &9b, &a9, &9b   ; 9b91: 9a a3 b1... ...
    equb &48, &a9, &dc                                                ; 9b9d: 48 a9 dc    H..
    equs "HlX"                                                        ; 9ba0: 48 6c 58    HlX
    equb &0d, &a0,   8, &ae, &58, &0d, &ad, &59, &0d, &20, &bf, &ff   ; 9ba3: 0d a0 08... ...
    equb &4c, &dd, &9b, &ae, &58, &0d, &ac, &59, &0d, &20,   0, &80   ; 9baf: 4c dd 9b... L..
    equb &4c, &dd, &9b, &a9,   4, &2c, &38, &0d, &d0, &18, &0d, &38   ; 9bbb: 4c dd 9b... L..
    equb &0d, &8d, &38, &0d, &a9,   4                                 ; 9bc7: 0d 8d 38... ..8
    equs "X,8"                                                        ; 9bcd: 58 2c 38    X,8
    equb &0d, &d0, &fb, &f0,   8, &ad, &38, &0d, &29, &fb, &8d, &38   ; 9bd0: 0d d0 fb... ...
    equb &0d, &68, &a8, &68, &aa, &a9,   0, &60                       ; 9bdc: 0d 68 a8... .h.

; &9be4 referenced 1 time by &9660
.c9be4
    txa                                                               ; 9be4: 8a          .
    pha                                                               ; 9be5: 48          H
    ldy #2                                                            ; 9be6: a0 02       ..
    lda (nmi_tx_block),y                                              ; 9be8: b1 a0       ..
    sta tx_dst_stn                                                    ; 9bea: 8d 20 0d    . .
    iny                                                               ; 9bed: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 9bee: b1 a0       ..
    sta tx_dst_net                                                    ; 9bf0: 8d 21 0d    .!.
    ldy #0                                                            ; 9bf3: a0 00       ..
    lda (nmi_tx_block),y                                              ; 9bf5: b1 a0       ..
    bmi c9bfc                                                         ; 9bf7: 30 03       0.
    jmp tx_active_start                                               ; 9bf9: 4c 84 9c    L..

; &9bfc referenced 1 time by &9bf7
.c9bfc
    sta tx_ctrl_byte                                                  ; 9bfc: 8d 24 0d    .$.
    tax                                                               ; 9bff: aa          .
    iny                                                               ; 9c00: c8          .
    lda (nmi_tx_block),y                                              ; 9c01: b1 a0       ..
    sta tx_port                                                       ; 9c03: 8d 25 0d    .%.
    bne c9c37                                                         ; 9c06: d0 2f       ./
    cpx #&83                                                          ; 9c08: e0 83       ..
    bcs c9c27                                                         ; 9c0a: b0 1b       ..
    sec                                                               ; 9c0c: 38          8
    php                                                               ; 9c0d: 08          .
    ldy #8                                                            ; 9c0e: a0 08       ..
; &9c10 referenced 1 time by &9c24
.loop_c9c10
    lda (nmi_tx_block),y                                              ; 9c10: b1 a0       ..
    dey                                                               ; 9c12: 88          .
    dey                                                               ; 9c13: 88          .
    dey                                                               ; 9c14: 88          .
    dey                                                               ; 9c15: 88          .
    plp                                                               ; 9c16: 28          (
    sbc (nmi_tx_block),y                                              ; 9c17: f1 a0       ..
    sta tx_data_start,y                                               ; 9c19: 99 26 0d    .&.
    iny                                                               ; 9c1c: c8          .
    iny                                                               ; 9c1d: c8          .
    iny                                                               ; 9c1e: c8          .
    iny                                                               ; 9c1f: c8          .
    iny                                                               ; 9c20: c8          .
    php                                                               ; 9c21: 08          .
    cpy #&0c                                                          ; 9c22: c0 0c       ..
    bcc loop_c9c10                                                    ; 9c24: 90 ea       ..
    plp                                                               ; 9c26: 28          (
; &9c27 referenced 1 time by &9c0a
.c9c27
    cpx #&89                                                          ; 9c27: e0 89       ..
    bcs tx_active_start                                               ; 9c29: b0 59       .Y
    ldy #&0c                                                          ; 9c2b: a0 0c       ..
; &9c2d referenced 1 time by &9c35
.loop_c9c2d
    lda (nmi_tx_block),y                                              ; 9c2d: b1 a0       ..
    sta nmi_shim_1a,y                                                 ; 9c2f: 99 1a 0d    ...
    iny                                                               ; 9c32: c8          .
    cpy #&10                                                          ; 9c33: c0 10       ..
    bcc loop_c9c2d                                                    ; 9c35: 90 f6       ..
; &9c37 referenced 1 time by &9c06
.c9c37
    lda #&20 ; ' '                                                    ; 9c37: a9 20       .
    bit econet_control23_or_status2                                   ; 9c39: 2c a1 fe    ,..
    bne c9c94                                                         ; 9c3c: d0 56       .V
    lda #&fd                                                          ; 9c3e: a9 fd       ..
    pha                                                               ; 9c40: 48          H
    lda #6                                                            ; 9c41: a9 06       ..
    sta tx_length                                                     ; 9c43: 8d 50 0d    .P.
    lda #0                                                            ; 9c46: a9 00       ..
; INACTIVE polling loop
; Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
; attempting transmission. Uses a 3-byte timeout counter on the stack.
; The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
; never appears.
; The CTS check at $9C66-$9C6B works because CR2=$67 has RTS=0, so
; cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.
.inactive_poll
    sta tx_index                                                      ; 9c48: 8d 4f 0d    .O.
    pha                                                               ; 9c4b: 48          H
    pha                                                               ; 9c4c: 48          H
    ldy #&e7                                                          ; 9c4d: a0 e7       ..             ; Y=$E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &9c4f referenced 3 times by &9c75, &9c7a, &9c7f
.c9c4f
    lda #4                                                            ; 9c4f: a9 04       ..             ; A=$04: INACTIVE mask for SR2 bit2
    php                                                               ; 9c51: 08          .
    sei                                                               ; 9c52: 78          x
; &9c53 referenced 1 time by &9ccf
.c9c53
    bit station_id_disable_net_nmis                                   ; 9c53: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
    bit station_id_disable_net_nmis                                   ; 9c56: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
.sub_c9c59
l9c5b = sub_c9c59+2
    bit econet_control23_or_status2                                   ; 9c59: 2c a1 fe    ,..            ; BIT SR2: Z = $04 AND SR2 -- tests INACTIVE
; &9c5b referenced 1 time by &9ccb
    beq c9c6d                                                         ; 9c5c: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 9c5e: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 9c61: a9 67       .g             ; CR2=$67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9c63: 8d a1 fe    ...
    lda #&10                                                          ; 9c66: a9 10       ..             ; A=$10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 9c68: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 9c6b: d0 35       .5             ; CTS set -- clock hardware detected, start TX
; &9c6d referenced 1 time by &9c5c
.c9c6d
    bit video_ula_control                                             ; 9c6d: 2c 20 fe    , .            ; INTON -- re-enable NMIs ($FE20 read)
    plp                                                               ; 9c70: 28          (
    tsx                                                               ; 9c71: ba          .              ; 3-byte timeout counter on stack
    inc l0101,x                                                       ; 9c72: fe 01 01    ...
    bne c9c4f                                                         ; 9c75: d0 d8       ..
    inc l0102,x                                                       ; 9c77: fe 02 01    ...
    bne c9c4f                                                         ; 9c7a: d0 d3       ..
    inc l0103,x                                                       ; 9c7c: fe 03 01    ...
    bne c9c4f                                                         ; 9c7f: d0 ce       ..
    jmp tx_line_jammed                                                ; 9c81: 4c 88 9c    L..

; TX_ACTIVE branch (A=$44 = CR1 value for TX active)
; &9c84 referenced 2 times by &9bf9, &9c29
.tx_active_start
    lda #&44 ; 'D'                                                    ; 9c84: a9 44       .D
    bne c9c96                                                         ; 9c86: d0 0e       ..             ; ALWAYS branch

; Timeout error: writes CR2=$07 to abort, cleans stack,
; returns error $40 ("Line Jammed").
; &9c88 referenced 1 time by &9c81
.tx_line_jammed
    lda #7                                                            ; 9c88: a9 07       ..             ; CR2=$07: FC_TDRA | 2_1_BYTE | PSE (abort TX)
    sta econet_control23_or_status2                                   ; 9c8a: 8d a1 fe    ...
    pla                                                               ; 9c8d: 68          h
    pla                                                               ; 9c8e: 68          h
    pla                                                               ; 9c8f: 68          h
    lda #&40 ; '@'                                                    ; 9c90: a9 40       .@             ; Error $40 = 'Line Jammed'
    bne c9c96                                                         ; 9c92: d0 02       ..             ; ALWAYS branch

; &9c94 referenced 1 time by &9c3c
.c9c94
    lda #&43 ; 'C'                                                    ; 9c94: a9 43       .C
; &9c96 referenced 2 times by &9c86, &9c92
.c9c96
    ldy #0                                                            ; 9c96: a0 00       ..
    sta (nmi_tx_block),y                                              ; 9c98: 91 a0       ..
    lda #&80                                                          ; 9c9a: a9 80       ..
    sta tx_ctrl_status                                                ; 9c9c: 8d 3a 0d    .:.
    pla                                                               ; 9c9f: 68          h
    tax                                                               ; 9ca0: aa          .
    rts                                                               ; 9ca1: 60          `

; TX preparation
; Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
; installs NMI TX handler at $9D4C, and re-enables NMIs.
; &9ca2 referenced 1 time by &9c6b
.tx_prepare
    sty econet_control23_or_status2                                   ; 9ca2: 8c a1 fe    ...            ; Write CR2 = Y ($E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
    ldx #&44 ; 'D'                                                    ; 9ca5: a2 44       .D             ; CR1=$44: RX_RESET | TIE (TX active, TX interrupts enabled)
    stx econet_control1_or_status1                                    ; 9ca7: 8e a0 fe    ...
    ldx #&4c ; 'L'                                                    ; 9caa: a2 4c       .L             ; Install NMI handler at $9D4C (TX data handler)
    ldy #&9d                                                          ; 9cac: a0 9d       ..
    stx nmi_jmp_lo                                                    ; 9cae: 8e 0c 0d    ...
    sty nmi_jmp_hi                                                    ; 9cb1: 8c 0d 0d    ...
    bit video_ula_control                                             ; 9cb4: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA ($FE20 read)
    lda tx_port                                                       ; 9cb7: ad 25 0d    .%.
    bne c9d16                                                         ; 9cba: d0 5a       .Z
    ldy tx_ctrl_byte                                                  ; 9cbc: ac 24 0d    .$.
    lda l9ed2,y                                                       ; 9cbf: b9 d2 9e    ...
    sta tx_flags                                                      ; 9cc2: 8d 4a 0d    .J.
    lda l9eca,y                                                       ; 9cc5: b9 ca 9e    ...
    sta tx_length                                                     ; 9cc8: 8d 50 0d    .P.
    lda l9c5b,y                                                       ; 9ccb: b9 5b 9c    .[.
    pha                                                               ; 9cce: 48          H
    lda c9c53,y                                                       ; 9ccf: b9 53 9c    .S.
    pha                                                               ; 9cd2: 48          H
    rts                                                               ; 9cd3: 60          `

    equb &e7, &eb, &0a, &0a, &0a, &44, &44, &e3, &9c, &9c, &9d, &9d   ; 9cd4: e7 eb 0a... ...
    equb &9d, &9d, &9d, &9c, &a9,   3, &d0, &25, &a9,   3, &d0,   2   ; 9ce0: 9d 9d 9d... ...
    equb &a9,   2, &8d, &5c, &0d, &18,   8, &a0, &0c, &b9, &1e, &0d   ; 9cec: a9 02 8d... ...
    equb &28, &71, &a0, &99, &1e, &0d, &c8,   8, &c0, &10, &90, &f1   ; 9cf8: 28 71 a0... (q.
    equs "( ["                                                        ; 9d04: 28 20 5b    ( [
    equb &9f, &4c, &45, &9d, &a9, 2, &8d, &5c, &0d, &20, &5b, &9f     ; 9d07: 9f 4c 45... .LE
    equb &4c, &45, &9d                                                ; 9d13: 4c 45 9d    LE.

; &9d16 referenced 1 time by &9cba
.c9d16
    lda tx_dst_stn                                                    ; 9d16: ad 20 0d    . .
    and tx_dst_net                                                    ; 9d19: 2d 21 0d    -!.
    cmp #&ff                                                          ; 9d1c: c9 ff       ..
    bne c9d38                                                         ; 9d1e: d0 18       ..
    lda #&0e                                                          ; 9d20: a9 0e       ..
    sta tx_length                                                     ; 9d22: 8d 50 0d    .P.
    lda #&40 ; '@'                                                    ; 9d25: a9 40       .@
    sta tx_flags                                                      ; 9d27: 8d 4a 0d    .J.
    ldy #4                                                            ; 9d2a: a0 04       ..
; &9d2c referenced 1 time by &9d34
.loop_c9d2c
    lda (nmi_tx_block),y                                              ; 9d2c: b1 a0       ..
    sta tx_src_stn,y                                                  ; 9d2e: 99 22 0d    .".
    iny                                                               ; 9d31: c8          .
    cpy #&0c                                                          ; 9d32: c0 0c       ..
    bcc loop_c9d2c                                                    ; 9d34: 90 f6       ..
    bcs c9d45                                                         ; 9d36: b0 0d       ..             ; ALWAYS branch

; &9d38 referenced 1 time by &9d1e
.c9d38
    lda #0                                                            ; 9d38: a9 00       ..
    sta tx_flags                                                      ; 9d3a: 8d 4a 0d    .J.
    lda #2                                                            ; 9d3d: a9 02       ..
    sta scout_status                                                  ; 9d3f: 8d 5c 0d    .\.
    jsr tx_calc_transfer                                              ; 9d42: 20 5b 9f     [.
; &9d45 referenced 1 time by &9d36
.c9d45
    plp                                                               ; 9d45: 28          (
    pla                                                               ; 9d46: 68          h
    pla                                                               ; 9d47: 68          h
    pla                                                               ; 9d48: 68          h
    pla                                                               ; 9d49: 68          h
    tax                                                               ; 9d4a: aa          .
    rts                                                               ; 9d4b: 60          `

; NMI TX data handler
; Writes 2 bytes per NMI invocation to the TX FIFO at $FEA2. Uses the
; BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
; After writing 2 bytes, checks if the frame is complete. If more data,
; tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
; without returning from NMI (tight loop). Otherwise returns via RTI.
.nmi_tx_data
    ldy tx_index                                                      ; 9d4c: ac 4f 0d    .O.            ; Load TX buffer index
    bit econet_control1_or_status1                                    ; 9d4f: 2c a0 fe    ,..            ; BIT SR1: V=bit6(TDRA), N=bit7(IRQ)
; &9d52 referenced 1 time by &9d6d
.loop_c9d52
    bvc c9d76                                                         ; 9d52: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 9d54: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 9d57: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 9d5a: c8          .
    lda tx_dst_stn,y                                                  ; 9d5b: b9 20 0d    . .
    iny                                                               ; 9d5e: c8          .
    sty tx_index                                                      ; 9d5f: 8c 4f 0d    .O.
    sta econet_data_continue_frame                                    ; 9d62: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy tx_length                                                     ; 9d65: cc 50 0d    .P.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 9d68: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA
    bit econet_control1_or_status1                                    ; 9d6a: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi loop_c9d52                                                    ; 9d6d: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 9d6f: 4c 14 0d    L..            ; RTI -- wait for next NMI

; TX error path
; &9d72 referenced 1 time by &9db7
.tx_error
    lda #&42 ; 'B'                                                    ; 9d72: a9 42       .B             ; Error $42
    bne c9d7d                                                         ; 9d74: d0 07       ..             ; ALWAYS branch

; &9d76 referenced 1 time by &9d52
.c9d76
    lda #&67 ; 'g'                                                    ; 9d76: a9 67       .g             ; CR2=$67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 9d78: 8d a1 fe    ...
    lda #&41 ; 'A'                                                    ; 9d7b: a9 41       .A             ; Error $41 (TDRA not ready)
; &9d7d referenced 1 time by &9d74
.c9d7d
    ldy station_id_disable_net_nmis                                   ; 9d7d: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &9d80 referenced 1 time by &9d83
.loop_c9d80
    pha                                                               ; 9d80: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 9d81: 68          h
    iny                                                               ; 9d82: c8          .
    bne loop_c9d80                                                    ; 9d83: d0 fb       ..
    jmp tx_store_result                                               ; 9d85: 4c 3f 9f    L?.            ; Jump to error handler

; TX_LAST_DATA and frame completion
; Signals end of TX frame by writing CR2=$3F (TX_LAST_DATA). Then installs
; the TX completion NMI handler at $9D94 which switches to RX mode.
; CR2=$3F = 0011_1111:
;   bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
;   bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
;   bit3: FLAG_IDLE -- send flags/idle after frame
;   bit2: FC_TDRA -- force clear TDRA
;   bit1: 2_1_BYTE -- two-byte transfer mode
;   bit0: PSE -- prioritised status enable
; Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)
; &9d88 referenced 1 time by &9d68
.tx_last_data
    lda #&3f ; '?'                                                    ; 9d88: a9 3f       .?             ; CR2=$3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 9d8a: 8d a1 fe    ...
    lda #&94                                                          ; 9d8d: a9 94       ..             ; Install NMI handler at $9D94 (TX completion)
    ldy #&9d                                                          ; 9d8f: a0 9d       ..
    jmp set_nmi_vector                                                ; 9d91: 4c 0e 0d    L..

; TX completion: switch to RX mode
; Called via NMI after the frame (including CRC and closing flag) has been
; fully transmitted. Switches from TX mode to RX mode by writing CR1=$82.
; CR1=$82 = 1000_0010: TX_RESET | RIE (listen for reply).
; Checks workspace flags to decide next action:
;   - bit6 set at $0D4A -> completion at $9F39
;   - bit0 set at $0D4A -> four-way handshake data phase at $9EDD
;   - Otherwise -> install RX reply handler at $9DB2
.nmi_tx_complete
    lda #&82                                                          ; 9d94: a9 82       ..             ; CR1=$82: TX_RESET | RIE (now in RX mode)
    sta econet_control1_or_status1                                    ; 9d96: 8d a0 fe    ...
    bit tx_flags                                                      ; 9d99: 2c 4a 0d    ,J.            ; Test workspace flags
    bvc c9da1                                                         ; 9d9c: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 9d9e: 4c 39 9f    L9.            ; bit6 set -- TX completion

; &9da1 referenced 1 time by &9d9c
.c9da1
    lda #1                                                            ; 9da1: a9 01       ..
    bit tx_flags                                                      ; 9da3: 2c 4a 0d    ,J.
    beq c9dab                                                         ; 9da6: f0 03       ..
    jmp handshake_await_ack                                           ; 9da8: 4c dd 9e    L..            ; bit0 set -- four-way handshake data phase

; &9dab referenced 1 time by &9da6
.c9dab
    lda #&b2                                                          ; 9dab: a9 b2       ..             ; Install RX reply handler at $9DB2
    ldy #&9d                                                          ; 9dad: a0 9d       ..
    jmp set_nmi_vector                                                ; 9daf: 4c 0e 0d    L..

; RX reply scout handler
; Handles reception of the reply scout frame after transmission.
; Checks SR2 bit0 (AP) for incoming data, reads the first byte
; (destination station) and compares to our station ID via $FE18
; (which also disables NMIs as a side effect).
.nmi_reply_scout
    lda #1                                                            ; 9db2: a9 01       ..             ; A=$01: AP mask for SR2
    bit econet_control23_or_status2                                   ; 9db4: 2c a1 fe    ,..            ; BIT SR2: test AP (Address Present)
    beq tx_error                                                      ; 9db7: f0 b9       ..             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9db9: ad a2 fe    ...            ; Read RX byte (destination station)
    cmp station_id_disable_net_nmis                                   ; 9dbc: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne reply_error                                                   ; 9dbf: d0 1d       ..             ; Not our station -- error/reject
    lda #&c8                                                          ; 9dc1: a9 c8       ..             ; Install next handler at $9DC8 (reply continuation)
    ldy #&9d                                                          ; 9dc3: a0 9d       ..
    jmp set_nmi_vector                                                ; 9dc5: 4c 0e 0d    L..

; RX reply continuation handler
; Reads the second byte of the reply scout (destination network) and
; validates it is zero (local network). Installs $9DE3 for the
; remaining two bytes (source station and network).
; Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at $9DD9.
; If IRQ is still set, falls through directly to $9DE3 without an RTI,
; avoiding NMI re-entry overhead for short frames where all bytes arrive
; in quick succession.
.nmi_reply_cont
    bit econet_control23_or_status2                                   ; 9dc8: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl reply_error                                                   ; 9dcb: 10 11       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9dcd: ad a2 fe    ...            ; Read destination network byte
    bne reply_error                                                   ; 9dd0: d0 0c       ..             ; Non-zero -- network mismatch, error
    lda #&e3                                                          ; 9dd2: a9 e3       ..             ; Install next handler at $9DE3 (reply validation)
    ldy #&9d                                                          ; 9dd4: a0 9d       ..
    bit econet_control1_or_status1                                    ; 9dd6: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 9dd9: 30 08       0.             ; IRQ set -- fall through to $9DE3 without RTI
    jmp set_nmi_vector                                                ; 9ddb: 4c 0e 0d    L..            ; IRQ not set -- install handler and RTI

; &9dde referenced 7 times by &9dbf, &9dcb, &9dd0, &9de6, &9dee, &9df6, &9dfd
.reply_error
    lda #&41 ; 'A'                                                    ; 9dde: a9 41       .A
    jmp tx_store_result                                               ; 9de0: 4c 3f 9f    L?.

; RX reply validation (Path 2 for FV/PSE interaction)
; Reads the source station and source network from the reply scout and
; validates them against the original TX destination ($0D20/$0D21).
; Sequence:
;   1. Check SR2 bit7 (RDA) at $9DE3 -- must see data available
;   2. Read source station at $9DE8, compare to $0D20 (tx_dst_stn)
;   3. Read source network at $9DF0, compare to $0D21 (tx_dst_net)
;   4. Check SR2 bit1 (FV) at $9DFA -- must see frame complete
; If all checks pass, the reply scout is valid and the ROM proceeds
; to send the scout ACK (CR2=$A7 for RTS, CR1=$44 for TX mode).
; &9de3 referenced 1 time by &9dd9
.nmi_reply_validate
    bit econet_control23_or_status2                                   ; 9de3: 2c a1 fe    ,..            ; BIT SR2: test RDA (bit7). Must be set for valid reply.
    bpl reply_error                                                   ; 9de6: 10 f6       ..             ; No RDA -- error (FV masking RDA via PSE would cause this)
    lda econet_data_continue_frame                                    ; 9de8: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9deb: cd 20 0d    . .            ; Compare to original TX destination station ($0D20)
    bne reply_error                                                   ; 9dee: d0 ee       ..             ; Mismatch -- not the expected reply, error
    lda econet_data_continue_frame                                    ; 9df0: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9df3: cd 21 0d    .!.            ; Compare to original TX destination network ($0D21)
    bne reply_error                                                   ; 9df6: d0 e6       ..             ; Mismatch -- error
    lda #2                                                            ; 9df8: a9 02       ..             ; A=$02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9dfa: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq reply_error                                                   ; 9dfd: f0 df       ..             ; No FV -- incomplete frame, error
    lda #&a7                                                          ; 9dff: a9 a7       ..             ; CR2=$A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)
    sta econet_control23_or_status2                                   ; 9e01: 8d a1 fe    ...
    lda #&44 ; 'D'                                                    ; 9e04: a9 44       .D             ; CR1=$44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 9e06: 8d a0 fe    ...
    lda #&dd                                                          ; 9e09: a9 dd       ..             ; Install next handler at $9EDD (four-way data phase) into $0D4B/$0D4C
    ldy #&9e                                                          ; 9e0b: a0 9e       ..
    sta nmi_next_lo                                                   ; 9e0d: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 9e10: 8c 4c 0d    .L.
    lda tx_dst_stn                                                    ; 9e13: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 9e16: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc data_tx_error                                                 ; 9e19: 50 73       Ps             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9e1b: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 9e1e: ad 21 0d    .!.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9e21: 8d a2 fe    ...
    lda #&2b ; '+'                                                    ; 9e24: a9 2b       .+             ; Install handler at $9E2B (write src addr for scout ACK)
    ldy #&9e                                                          ; 9e26: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e28: 4c 0e 0d    L..

; TX scout ACK: write source address
; Writes our station ID and network=0 to TX FIFO, completing the
; 4-byte scout ACK frame. Then proceeds to send the data frame.
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 9e2b: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9e2e: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc data_tx_error                                                 ; 9e31: 50 5b       P[             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9e33: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9e36: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 9e38: 8d a2 fe    ...
; &9e3b referenced 1 time by &99b5
.data_tx_begin
    lda #2                                                            ; 9e3b: a9 02       ..
    bit tx_flags                                                      ; 9e3d: 2c 4a 0d    ,J.
    bne c9e49                                                         ; 9e40: d0 07       ..
    lda #&50 ; 'P'                                                    ; 9e42: a9 50       .P
    ldy #&9e                                                          ; 9e44: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e46: 4c 0e 0d    L..

; &9e49 referenced 1 time by &9e40
.c9e49
    lda #&a4                                                          ; 9e49: a9 a4       ..
    ldy #&9e                                                          ; 9e4b: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e4d: 4c 0e 0d    L..

; TX data phase: send payload
; Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
; Same pattern as the NMI TX handler at $9D4C but reads from the port
; buffer instead of the TX workspace. Writes two bytes per iteration,
; checking SR1 IRQ between pairs for tight looping.
.nmi_data_tx
    ldy port_buf_len                                                  ; 9e50: a4 a2       ..             ; Y = buffer offset, resume from last position
    bit econet_control1_or_status1                                    ; 9e52: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
; &9e55 referenced 1 time by &9e78
.c9e55
    bvc data_tx_error                                                 ; 9e55: 50 37       P7             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 9e57: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 9e59: 8d a2 fe    ...
    iny                                                               ; 9e5c: c8          .
    bne c9e65                                                         ; 9e5d: d0 06       ..
    dec port_buf_len_hi                                               ; 9e5f: c6 a3       ..
    beq data_tx_last                                                  ; 9e61: f0 1a       ..
    inc open_port_buf_hi                                              ; 9e63: e6 a5       ..
; &9e65 referenced 1 time by &9e5d
.c9e65
    lda (open_port_buf),y                                             ; 9e65: b1 a4       ..
    sta econet_data_continue_frame                                    ; 9e67: 8d a2 fe    ...
    iny                                                               ; 9e6a: c8          .
    sty port_buf_len                                                  ; 9e6b: 84 a2       ..
    bne c9e75                                                         ; 9e6d: d0 06       ..
    dec port_buf_len_hi                                               ; 9e6f: c6 a3       ..
    beq data_tx_last                                                  ; 9e71: f0 0a       ..
    inc open_port_buf_hi                                              ; 9e73: e6 a5       ..
; &9e75 referenced 1 time by &9e6d
.c9e75
    bit econet_control1_or_status1                                    ; 9e75: 2c a0 fe    ,..
    bmi c9e55                                                         ; 9e78: 30 db       0.
    jmp nmi_rti                                                       ; 9e7a: 4c 14 0d    L..

; &9e7d referenced 4 times by &9e61, &9e71, &9ebd, &9ed3
.data_tx_last
    lda #&3f ; '?'                                                    ; 9e7d: a9 3f       .?             ; CR2=$3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 9e7f: 8d a1 fe    ...
    lda tx_flags                                                      ; 9e82: ad 4a 0d    .J.
    bpl install_saved_handler                                         ; 9e85: 10 14       ..
    lda #&34 ; '4'                                                    ; 9e87: a9 34       .4
    ldy #&9a                                                          ; 9e89: a0 9a       ..
    jmp set_nmi_vector                                                ; 9e8b: 4c 0e 0d    L..

; &9e8e referenced 4 times by &9e19, &9e31, &9e55, &9ea7
.data_tx_error
    lda tx_flags                                                      ; 9e8e: ad 4a 0d    .J.
    bpl c9e96                                                         ; 9e91: 10 03       ..
    jmp discard_reset_listen                                          ; 9e93: 4c 34 9a    L4.

; &9e96 referenced 1 time by &9e91
.c9e96
    lda #&41 ; 'A'                                                    ; 9e96: a9 41       .A
    jmp tx_store_result                                               ; 9e98: 4c 3f 9f    L?.

; &9e9b referenced 1 time by &9e85
.install_saved_handler
    lda nmi_next_lo                                                   ; 9e9b: ad 4b 0d    .K.
    ldy nmi_next_hi                                                   ; 9e9e: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 9ea1: 4c 0e 0d    L..

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 9ea4: 2c a0 fe    ,..
; &9ea7 referenced 1 time by &9ed8
.c9ea7
    bvc data_tx_error                                                 ; 9ea7: 50 e5       P.
    lda tube_data_register_3                                          ; 9ea9: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9eac: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9eaf: e6 a2       ..
    bne c9ebf                                                         ; 9eb1: d0 0c       ..
    inc port_buf_len_hi                                               ; 9eb3: e6 a3       ..
    bne c9ebf                                                         ; 9eb5: d0 08       ..
    inc open_port_buf                                                 ; 9eb7: e6 a4       ..
    bne c9ebf                                                         ; 9eb9: d0 04       ..
    inc open_port_buf_hi                                              ; 9ebb: e6 a5       ..
    beq data_tx_last                                                  ; 9ebd: f0 be       ..
; &9ebf referenced 3 times by &9eb1, &9eb5, &9eb9
.c9ebf
    lda tube_data_register_3                                          ; 9ebf: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9ec2: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9ec5: e6 a2       ..
    bne c9ed5                                                         ; 9ec7: d0 0c       ..
.sub_c9ec9
l9eca = sub_c9ec9+1
    inc port_buf_len_hi                                               ; 9ec9: e6 a3       ..
; &9eca referenced 1 time by &9cc5
    bne c9ed5                                                         ; 9ecb: d0 08       ..
    inc open_port_buf                                                 ; 9ecd: e6 a4       ..
    bne c9ed5                                                         ; 9ecf: d0 04       ..
.sub_c9ed1
l9ed2 = sub_c9ed1+1
    inc open_port_buf_hi                                              ; 9ed1: e6 a5       ..
; &9ed2 referenced 1 time by &9cbf
    beq data_tx_last                                                  ; 9ed3: f0 a8       ..
; &9ed5 referenced 3 times by &9ec7, &9ecb, &9ecf
.c9ed5
    bit econet_control1_or_status1                                    ; 9ed5: 2c a0 fe    ,..
    bmi c9ea7                                                         ; 9ed8: 30 cd       0.
    jmp nmi_rti                                                       ; 9eda: 4c 14 0d    L..

; Four-way handshake: switch to RX for final ACK
; After the data frame TX completes, switches to RX mode (CR1=$82)
; and installs $9EE9 to receive the final ACK from the remote station.
; &9edd referenced 1 time by &9da8
.handshake_await_ack
    lda #&82                                                          ; 9edd: a9 82       ..             ; CR1=$82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 9edf: 8d a0 fe    ...
    lda #&e9                                                          ; 9ee2: a9 e9       ..             ; Install handler at $9EE9 (RX final ACK)
    ldy #&9e                                                          ; 9ee4: a0 9e       ..
    jmp set_nmi_vector                                                ; 9ee6: 4c 0e 0d    L..

; RX final ACK handler
; Receives the final ACK in a four-way handshake. Same validation
; pattern as the reply scout handler ($9DB2-$9DE3):
;   $9EE9: Check AP, read dest_stn, compare to our station
;   $9EFF: Check RDA, read dest_net, validate = 0
;   $9F15: Check RDA, read src_stn/net, compare to TX dest
;   $9F32: Check FV for frame completion
; On success, stores result=0 at $9F39. On any failure, error $41.
.nmi_final_ack
    lda #1                                                            ; 9ee9: a9 01       ..             ; A=$01: AP mask
    bit econet_control23_or_status2                                   ; 9eeb: 2c a1 fe    ,..            ; BIT SR2: test AP
    beq tx_result_fail                                                ; 9eee: f0 4d       .M             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9ef0: ad a2 fe    ...            ; Read dest station
    cmp station_id_disable_net_nmis                                   ; 9ef3: cd 18 fe    ...            ; Compare to our station (INTOFF side effect)
    bne tx_result_fail                                                ; 9ef6: d0 45       .E             ; Not our station -- error
    lda #&ff                                                          ; 9ef8: a9 ff       ..             ; Install handler at $9EFF (final ACK continuation)
    ldy #&9e                                                          ; 9efa: a0 9e       ..
    jmp set_nmi_vector                                                ; 9efc: 4c 0e 0d    L..

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 9eff: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9f02: 10 39       .9             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9f04: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 9f07: d0 34       .4             ; Non-zero -- network mismatch, error
    lda #&15                                                          ; 9f09: a9 15       ..             ; Install handler at $9F15 (final ACK validation)
    ldy #&9f                                                          ; 9f0b: a0 9f       ..
    bit econet_control1_or_status1                                    ; 9f0d: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 9f10: 30 03       0.             ; IRQ set -- fall through to $9F15 without RTI
    jmp set_nmi_vector                                                ; 9f12: 4c 0e 0d    L..

; Final ACK validation
; Reads and validates src_stn and src_net against original TX dest.
; Then checks FV for frame completion.
; &9f15 referenced 1 time by &9f10
.nmi_final_ack_validate
    bit econet_control23_or_status2                                   ; 9f15: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9f18: 10 23       .#             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9f1a: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9f1d: cd 20 0d    . .            ; Compare to TX dest station ($0D20)
    bne tx_result_fail                                                ; 9f20: d0 1b       ..             ; Mismatch -- error
    lda econet_data_continue_frame                                    ; 9f22: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9f25: cd 21 0d    .!.            ; Compare to TX dest network ($0D21)
    bne tx_result_fail                                                ; 9f28: d0 13       ..             ; Mismatch -- error
    lda tx_flags                                                      ; 9f2a: ad 4a 0d    .J.
    bpl c9f32                                                         ; 9f2d: 10 03       ..
    jmp c9870                                                         ; 9f2f: 4c 70 98    Lp.

; &9f32 referenced 1 time by &9f2d
.c9f32
    lda #2                                                            ; 9f32: a9 02       ..             ; A=$02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9f34: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq tx_result_fail                                                ; 9f37: f0 04       ..             ; No FV -- error
; TX completion handler
; Stores result code 0 (success) into the first byte of the TX control
; block (nmi_tx_block),Y=0. Then sets $0D3A bit7 to signal completion
; and calls full ADLC reset + idle listen via $9A34.
; &9f39 referenced 2 times by &9963, &9d9e
.tx_result_ok
    lda #0                                                            ; 9f39: a9 00       ..             ; A=0: success result code
    beq tx_store_result                                               ; 9f3b: f0 02       ..             ; BEQ: always taken (A=0); ALWAYS branch

; &9f3d referenced 8 times by &9eee, &9ef6, &9f02, &9f07, &9f18, &9f20, &9f28, &9f37
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 9f3d: a9 41       .A
; TX error handler
; Stores error code (A) into the TX control block, sets $0D3A bit7
; for completion, and returns to idle via $9A34.
; Error codes: $00=success, $40=line jammed, $41=not listening,
; $42=net error.
; &9f3f referenced 5 times by &9891, &9d85, &9de0, &9e98, &9f3b
.tx_store_result
    ldy #0                                                            ; 9f3f: a0 00       ..             ; Y=0: index into TX control block
    sta (nmi_tx_block),y                                              ; 9f41: 91 a0       ..             ; Store result/error code at (nmi_tx_block),0
    lda #&80                                                          ; 9f43: a9 80       ..             ; $80: completion flag for $0D3A
    sta tx_ctrl_status                                                ; 9f45: 8d 3a 0d    .:.            ; Signal TX complete
    jmp discard_reset_listen                                          ; 9f48: 4c 34 9a    L4.            ; Full ADLC reset and return to idle listen

    equb &0e, &0e, &0a, &0a, &0a, 6, 6, &0a, &81, 0, 0, 0, 0, 1, 1    ; 9f4b: 0e 0e 0a... ...
    equb &81                                                          ; 9f5a: 81          .

; Calculate transfer size
; Computes the number of bytes actually transferred during a data
; frame reception. Subtracts the low pointer (LPTR, offset 4 in
; the RXCB) from the current buffer position to get the byte count,
; and stores it back into the RXCB's high pointer field (HPTR,
; offset 8). This tells the caller how much data was received.
; &9f5b referenced 2 times by &980e, &9d42
.tx_calc_transfer
    ldy #6                                                            ; 9f5b: a0 06       ..
    lda (nmi_tx_block),y                                              ; 9f5d: b1 a0       ..
    iny                                                               ; 9f5f: c8          .              ; Y=&07
    and (nmi_tx_block),y                                              ; 9f60: 31 a0       1.
    cmp #&ff                                                          ; 9f62: c9 ff       ..
    beq c9fa7                                                         ; 9f64: f0 41       .A
    lda tx_in_progress                                                ; 9f66: ad 52 0d    .R.
    beq c9fa7                                                         ; 9f69: f0 3c       .<
    lda tx_flags                                                      ; 9f6b: ad 4a 0d    .J.
    ora #2                                                            ; 9f6e: 09 02       ..
    sta tx_flags                                                      ; 9f70: 8d 4a 0d    .J.
    sec                                                               ; 9f73: 38          8
    php                                                               ; 9f74: 08          .
    ldy #4                                                            ; 9f75: a0 04       ..
; &9f77 referenced 1 time by &9f89
.loop_c9f77
    lda (nmi_tx_block),y                                              ; 9f77: b1 a0       ..
    iny                                                               ; 9f79: c8          .
    iny                                                               ; 9f7a: c8          .
    iny                                                               ; 9f7b: c8          .
    iny                                                               ; 9f7c: c8          .
    plp                                                               ; 9f7d: 28          (
    sbc (nmi_tx_block),y                                              ; 9f7e: f1 a0       ..
    sta net_tx_ptr,y                                                  ; 9f80: 99 9a 00    ...
    dey                                                               ; 9f83: 88          .
    dey                                                               ; 9f84: 88          .
    dey                                                               ; 9f85: 88          .
    php                                                               ; 9f86: 08          .
    cpy #8                                                            ; 9f87: c0 08       ..
    bcc loop_c9f77                                                    ; 9f89: 90 ec       ..
    plp                                                               ; 9f8b: 28          (
    txa                                                               ; 9f8c: 8a          .
    pha                                                               ; 9f8d: 48          H
    lda #4                                                            ; 9f8e: a9 04       ..
    clc                                                               ; 9f90: 18          .
    adc nmi_tx_block                                                  ; 9f91: 65 a0       e.
    tax                                                               ; 9f93: aa          .
    ldy nmi_tx_block_hi                                               ; 9f94: a4 a1       ..
    lda #&c2                                                          ; 9f96: a9 c2       ..
    jsr tube_addr_claim                                               ; 9f98: 20 06 04     ..
    bcc c9fa4                                                         ; 9f9b: 90 07       ..
    lda scout_status                                                  ; 9f9d: ad 5c 0d    .\.
    jsr tube_addr_claim                                               ; 9fa0: 20 06 04     ..
    sec                                                               ; 9fa3: 38          8
; &9fa4 referenced 1 time by &9f9b
.c9fa4
    pla                                                               ; 9fa4: 68          h
    tax                                                               ; 9fa5: aa          .
    rts                                                               ; 9fa6: 60          `

; &9fa7 referenced 2 times by &9f64, &9f69
.c9fa7
    ldy #4                                                            ; 9fa7: a0 04       ..
    lda (nmi_tx_block),y                                              ; 9fa9: b1 a0       ..
    ldy #8                                                            ; 9fab: a0 08       ..
    sec                                                               ; 9fad: 38          8
    sbc (nmi_tx_block),y                                              ; 9fae: f1 a0       ..
    sta port_buf_len                                                  ; 9fb0: 85 a2       ..
    ldy #5                                                            ; 9fb2: a0 05       ..
    lda (nmi_tx_block),y                                              ; 9fb4: b1 a0       ..
    sbc #0                                                            ; 9fb6: e9 00       ..
    sta open_port_buf_hi                                              ; 9fb8: 85 a5       ..
    ldy #8                                                            ; 9fba: a0 08       ..
    lda (nmi_tx_block),y                                              ; 9fbc: b1 a0       ..
    sta open_port_buf                                                 ; 9fbe: 85 a4       ..
    ldy #9                                                            ; 9fc0: a0 09       ..
    lda (nmi_tx_block),y                                              ; 9fc2: b1 a0       ..
    sec                                                               ; 9fc4: 38          8
    sbc open_port_buf_hi                                              ; 9fc5: e5 a5       ..
    sta port_buf_len_hi                                               ; 9fc7: 85 a3       ..
    sec                                                               ; 9fc9: 38          8
; &9fca referenced 1 time by &96d1
.nmi_shim_rom_src
    rts                                                               ; 9fca: 60          `

; Bootstrap NMI entry point (in ROM)
; An alternate NMI handler that lives in the ROM itself rather than
; in the RAM workspace at $0D00. Unlike the RAM shim (which uses a
; self-modifying JMP to dispatch to different handlers), this one
; hardcodes JMP nmi_rx_scout ($96F6). Used as the initial NMI handler
; before the workspace has been properly set up during initialisation.
; Same sequence as the RAM shim: BIT $FE18 (INTOFF), PHA, TYA, PHA,
; LDA romsel, STA $FE30, JMP $96F6.
.nmi_bootstrap_entry
    bit station_id_disable_net_nmis                                   ; 9fcb: 2c 18 fe    ,..
    pha                                                               ; 9fce: 48          H
    tya                                                               ; 9fcf: 98          .
    pha                                                               ; 9fd0: 48          H
    lda #0                                                            ; 9fd1: a9 00       ..
    sta romsel                                                        ; 9fd3: 8d 30 fe    .0.
    jmp nmi_rx_scout                                                  ; 9fd6: 4c f6 96    L..

; ROM copy of set_nmi_vector + nmi_rti
; A version of the NMI vector-setting subroutine and RTI sequence
; that lives in ROM. The RAM workspace copy at $0D0E/$0D14 is the
; one normally used at runtime; this ROM copy is used during early
; initialisation before the RAM workspace has been set up, and as
; the source for the initial copy to RAM.
.rom_set_nmi_vector
    sty nmi_jmp_hi                                                    ; 9fd9: 8c 0d 0d    ...
    sta nmi_jmp_lo                                                    ; 9fdc: 8d 0c 0d    ...
    lda romsel_copy                                                   ; 9fdf: a5 f4       ..
    sta romsel                                                        ; 9fe1: 8d 30 fe    .0.
    pla                                                               ; 9fe4: 68          h
    tay                                                               ; 9fe5: a8          .
    pla                                                               ; 9fe6: 68          h
    bit video_ula_control                                             ; 9fe7: 2c 20 fe    , .
    rti                                                               ; 9fea: 40          @

.rom_nmi_tail
    lda tx_flags                                                      ; 9feb: ad 4a 0d    .J.
    ora #2                                                            ; 9fee: 09 02       ..
    sta tx_flags                                                      ; 9ff0: 8d 4a 0d    .J.
    sec                                                               ; 9ff3: 38          8
    php                                                               ; 9ff4: 08          .
    ldy #4                                                            ; 9ff5: a0 04       ..
    lda (nmi_tx_block),y                                              ; 9ff7: b1 a0       ..
    iny                                                               ; 9ff9: c8          .              ; Y=&05
    iny                                                               ; 9ffa: c8          .              ; Y=&06
    iny                                                               ; 9ffb: c8          .              ; Y=&07
    iny                                                               ; 9ffc: c8          .              ; Y=&08
    plp                                                               ; 9ffd: 28          (
    sbc (nmi_tx_block),y                                              ; 9ffe: f1 a0       ..
.pydis_end

    assert <(cat_handler-1) == &fc
    assert <(copy_handles-1) == &1f
    assert <(copy_handles_and_boot-1) == &1e
    assert <(dispatch_net_cmd-1) == &68
    assert <(econet_tx_rx-1) == &71
    assert <(eof_handler-1) == &1e
    assert <(execute_at_0100-1) == &29
    assert <(fscv_read_handles-1) == &d9
    assert <(fscv_shutdown-1) == &fc
    assert <(fscv_star_handler-1) == &91
    assert <(insert_remote_key-1) == &49
    assert <(l0130) == &30
    assert <(l8444) == &44
    assert <(net1_read_handle-1) == &ae
    assert <(net2_read_handle_entry-1) == &c8
    assert <(net3_close_handle-1) == &de
    assert <(net4_resume_remote-1) == &f1
    assert <(net_write_char-1) == &3c
    assert <(notify_and_exec-1) == &83
    assert <(opt_handler-1) == &a0
    assert <(osword_0f_handler-1) == &32
    assert <(osword_10_handler-1) == &ef
    assert <(osword_11_handler-1) == &52
    assert <(osword_12_handler-1) == &7a
    assert <(osword_fs_entry-1) == &f6
    assert <(print_dir_name-1) == &72
    assert <(remote_boot_handler-1) == &fb
    assert <(remote_cmd_data-1) == &cc
    assert <(remote_cmd_dispatch-1) == &62
    assert <(remote_display_setup-1) == &b4
    assert <(remote_print_handler-1) == &c6
    assert <(remote_validated-1) == &39
    assert <(return_2-1) == &44
    assert <(save_palette_vdu-1) == &90
    assert <(set_csd_handle-1) == &fb
    assert <(set_lib_handle-1) == &f6
    assert <(svc_abs_workspace-1) == &6e
    assert <(svc_autoboot-1) == &d0
    assert <(svc_help-1) == &bb
    assert <(svc_nmi_claim-1) == &68
    assert <(svc_nmi_release-1) == &65
    assert <(svc_private_workspace-1) == &77
    assert <(svc_star_command-1) == &71
    assert <(svc_unknown_irq-1) == &6b
    assert >(cat_handler-1) == &8b
    assert >(copy_handles-1) == &8d
    assert >(copy_handles_and_boot-1) == &8d
    assert >(dispatch_net_cmd-1) == &80
    assert >(econet_tx_rx-1) == &8f
    assert >(eof_handler-1) == &88
    assert >(execute_at_0100-1) == &91
    assert >(fscv_read_handles-1) == &85
    assert >(fscv_shutdown-1) == &82
    assert >(fscv_star_handler-1) == &8b
    assert >(insert_remote_key-1) == &91
    assert >(l0130) == &01
    assert >(l8444) == &84
    assert >(net1_read_handle-1) == &8d
    assert >(net2_read_handle_entry-1) == &8d
    assert >(net3_close_handle-1) == &8d
    assert >(net4_resume_remote-1) == &8d
    assert >(net_write_char-1) == &90
    assert >(notify_and_exec-1) == &8d
    assert >(opt_handler-1) == &89
    assert >(osword_0f_handler-1) == &8e
    assert >(osword_10_handler-1) == &8e
    assert >(osword_11_handler-1) == &8e
    assert >(osword_12_handler-1) == &8e
    assert >(osword_fs_entry-1) == &8d
    assert >(print_dir_name-1) == &8d
    assert >(remote_boot_handler-1) == &90
    assert >(remote_cmd_data-1) == &90
    assert >(remote_cmd_dispatch-1) == &90
    assert >(remote_display_setup-1) == &91
    assert >(remote_print_handler-1) == &91
    assert >(remote_validated-1) == &91
    assert >(return_2-1) == &81
    assert >(save_palette_vdu-1) == &92
    assert >(set_csd_handle-1) == &8c
    assert >(set_lib_handle-1) == &8c
    assert >(svc_abs_workspace-1) == &82
    assert >(svc_autoboot-1) == &81
    assert >(svc_help-1) == &81
    assert >(svc_nmi_claim-1) == &96
    assert >(svc_nmi_release-1) == &96
    assert >(svc_private_workspace-1) == &82
    assert >(svc_star_command-1) == &81
    assert >(svc_unknown_irq-1) == &96
    assert copyright - rom_header == &0c

save pydis_start, pydis_end

; Label references by decreasing frequency:
;     nfs_workspace:                           53
;     econet_control23_or_status2:             44
;     fs_options:                              41
;     econet_data_continue_frame:              37
;     fs_cmd_data:                             36
;     net_rx_ptr:                              35
;     econet_control1_or_status1:              30
;     l00f0:                                   28
;     nmi_tx_block:                            27
;     tx_flags:                                26
;     fs_load_addr_2:                          23
;     net_tx_ptr:                              23
;     port_ws_offset:                          23
;     osbyte:                                  22
;     set_nmi_vector:                          22
;     tube_read_r2:                            22
;     fs_crc_lo:                               21
;     port_buf_len:                            18
;     tube_send_r2:                            18
;     l0f06:                                   15
;     station_id_disable_net_nmis:             15
;     fs_temp_cd:                              14
;     open_port_buf_hi:                        14
;     fs_load_addr:                            13
;     print_inline:                            13
;     fs_error_ptr:                            12
;     open_port_buf:                           12
;     prepare_fs_cmd:                          12
;     rx_error:                                12
;     rx_status_flags:                         12
;     tube_data_register_2:                    12
;     port_buf_len_hi:                         11
;     tube_status_register_2:                  11
;     fs_last_byte_flag:                       10
;     fs_temp_ce:                              10
;     l00c4:                                   10
;     nfs_workspace_hi:                        10
;     tube_addr_claim:                         10
;     l00c8:                                    9
;     prot_status:                              9
;     rx_src_stn:                               9
;     tube_data_register_3:                     9
;     tube_status_1_and_tube_control:           9
;     l0000:                                    8
;     l00b4:                                    8
;     l0d60:                                    8
;     restore_args_return:                      8
;     tx_result_fail:                           8
;     fs_block_offset:                          7
;     fs_cmd_urd:                               7
;     fs_crc_hi:                                7
;     l00b3:                                    7
;     reply_error:                              7
;     return_1:                                 7
;     tube_main_loop:                           7
;     tx_dst_stn:                               7
;     c8f48:                                    6
;     fs_cmd_csd:                               6
;     fs_load_addr_hi:                          6
;     fs_sequence_nos:                          6
;     net_tx_ptr_hi:                            6
;     nmi_rti:                                  6
;     nmi_tx_block_hi:                          6
;     osasci:                                   6
;     save_fscv_args:                           6
;     tx_ctrl_status:                           6
;     tx_in_progress:                           6
;     zp_temp_10:                               6
;     c892e:                                    5
;     calc_handle_offset:                       5
;     copy_param_block:                         5
;     dispatch:                                 5
;     l0001:                                    5
;     l0106:                                    5
;     l0f07:                                    5
;     net_rx_ptr_hi:                            5
;     printer_buf_ptr:                          5
;     rx_buf_offset:                            5
;     rx_ctrl:                                  5
;     scout_error:                              5
;     set_fs_flag:                              5
;     system_via_acr:                           5
;     tube_reply_byte:                          5
;     tube_send_r1:                             5
;     tube_send_r4:                             5
;     tx_dst_net:                               5
;     tx_store_result:                          5
;     zp_temp_11:                               5
;     c8840:                                    4
;     clear_jsr_protection:                     4
;     copy_string_to_cmd:                       4
;     data_tx_error:                            4
;     data_tx_last:                             4
;     discard_reset_listen:                     4
;     fs_boot_option:                           4
;     fs_eof_flags:                             4
;     fs_server_net:                            4
;     l0015:                                    4
;     l00b7:                                    4
;     l00c0:                                    4
;     l00c1:                                    4
;     l00cf:                                    4
;     l00ef:                                    4
;     l0100:                                    4
;     l0101:                                    4
;     nmi_next_hi:                              4
;     nmi_next_lo:                              4
;     osrdsc_ptr:                               4
;     print_spaces:                             4
;     return_2:                                 4
;     rx_port:                                  4
;     rx_src_net:                               4
;     tx_length:                                4
;     video_ula_control:                        4
;     adlc_full_reset:                          3
;     c0464:                                    3
;     c845a:                                    3
;     c8945:                                    3
;     c8cff:                                    3
;     c8dda:                                    3
;     c8ee1:                                    3
;     c8f43:                                    3
;     c907c:                                    3
;     c97d7:                                    3
;     c9912:                                    3
;     c9928:                                    3
;     c9a80:                                    3
;     c9c4f:                                    3
;     c9ebf:                                    3
;     c9ed5:                                    3
;     clear_fs_flag:                            3
;     copy_filename:                            3
;     copy_string_from_offset:                  3
;     ctrl_block_setup_alt:                     3
;     data_rx_complete:                         3
;     data_rx_tube_error:                       3
;     fs_csd_handle:                            3
;     fs_getb_buf:                              3
;     fs_messages_flag:                         3
;     fs_server_stn:                            3
;     fs_urd_handle:                            3
;     handle_to_mask_a:                         3
;     handle_to_mask_clc:                       3
;     init_tx_ctrl_block:                       3
;     l0014:                                    3
;     l00af:                                    3
;     l00b6:                                    3
;     l0f08:                                    3
;     l0fde:                                    3
;     l833a:                                    3
;     match_osbyte_code:                        3
;     os_text_ptr:                              3
;     oscli:                                    3
;     osword:                                   3
;     pad_filename_spaces:                      3
;     print_reply_bytes:                        3
;     return_3:                                 3
;     romsel_copy:                              3
;     rx_ctrl_copy:                             3
;     scout_no_match:                           3
;     scout_status:                             3
;     send_to_fs_star:                          3
;     setup_tx_and_send:                        3
;     skip_spaces:                              3
;     tube_claim_loop:                          3
;     tube_data_register_1:                     3
;     tube_read_string:                         3
;     tube_reply_ack:                           3
;     tx_clear_flag:                            3
;     tx_index:                                 3
;     tx_poll_ff:                               3
;     ack_tx:                                   2
;     adjust_addrs:                             2
;     binary_version:                           2
;     c0036:                                    2
;     c04ba:                                    2
;     c04cc:                                    2
;     c0522:                                    2
;     c81c9:                                    2
;     c8240:                                    2
;     c82c3:                                    2
;     c840f:                                    2
;     c842a:                                    2
;     c8584:                                    2
;     c85a1:                                    2
;     c85fe:                                    2
;     c8637:                                    2
;     c868c:                                    2
;     c89b6:                                    2
;     c8abb:                                    2
;     c8b32:                                    2
;     c8dac:                                    2
;     c8dd6:                                    2
;     c8eac:                                    2
;     c8ee3:                                    2
;     c8f45:                                    2
;     c9105:                                    2
;     c9167:                                    2
;     c9186:                                    2
;     c91d6:                                    2
;     c98f4:                                    2
;     c99b8:                                    2
;     c9a19:                                    2
;     c9a8c:                                    2
;     c9b4f:                                    2
;     c9c96:                                    2
;     c9fa7:                                    2
;     call_fscv_shutdown:                       2
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
;     flush_output_block:                       2
;     fs_cmd_context:                           2
;     fs_cmd_match_table:                       2
;     fs_cmd_y_param:                           2
;     fs_last_error:                            2
;     fs_lib_handle:                            2
;     fs_putb_buf:                              2
;     fs_state_deb:                             2
;     init_tx_ctrl_port:                        2
;     l0003:                                    2
;     l0012:                                    2
;     l0058:                                    2
;     l00b5:                                    2
;     l00f1:                                    2
;     l00fd:                                    2
;     l00ff:                                    2
;     l0102:                                    2
;     l0103:                                    2
;     l0130:                                    2
;     l0700:                                    2
;     l0e0b:                                    2
;     l0f09:                                    2
;     l0f10:                                    2
;     l0f11:                                    2
;     l0f12:                                    2
;     l0fdf:                                    2
;     mask_to_handle:                           2
;     match_rom_string:                         2
;     nmi_jmp_hi:                               2
;     nmi_jmp_lo:                               2
;     nvwrch:                                   2
;     osfind:                                   2
;     parse_decimal:                            2
;     prepare_cmd_clv:                          2
;     prepare_fs_cmd_v:                         2
;     print_decimal:                            2
;     print_decimal_digit:                      2
;     print_dir_from_offset:                    2
;     print_file_info:                          2
;     print_hex:                                2
;     print_hex_bytes:                          2
;     print_reply_counted:                      2
;     print_space:                              2
;     resume_after_remote:                      2
;     return_12:                                2
;     return_14:                                2
;     return_8:                                 2
;     return_9:                                 2
;     romsel:                                   2
;     rx_extra_byte:                            2
;     scout_complete:                           2
;     send_data_blocks:                         2
;     send_fs_reply_cmd:                        2
;     send_to_fs:                               2
;     setup_tx_ptr_c0:                          2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     sub_3_from_y:                             2
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
;     tx_calc_transfer:                         2
;     tx_ctrl_byte:                             2
;     tx_port:                                  2
;     tx_result_ok:                             2
;     tx_src_stn:                               2
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
;     adlc_init_workspace:                      1
;     adlc_rx_listen:                           1
;     boot_option_offsets:                      1
;     brkv:                                     1
;     build_send_fs_cmd:                        1
;     c0419:                                    1
;     c0423:                                    1
;     c0426:                                    1
;     c0445:                                    1
;     c045d:                                    1
;     c0473:                                    1
;     c04a0:                                    1
;     c04ae:                                    1
;     c0535:                                    1
;     c055f:                                    1
;     c05c2:                                    1
;     c05d5:                                    1
;     c067b:                                    1
;     c811b:                                    1
;     c811f:                                    1
;     c817d:                                    1
;     c81e6:                                    1
;     c8212:                                    1
;     c832f:                                    1
;     c8359:                                    1
;     c835a:                                    1
;     c8394:                                    1
;     c8397:                                    1
;     c83fb:                                    1
;     c8424:                                    1
;     c8428:                                    1
;     c8441:                                    1
;     c849b:                                    1
;     c84a0:                                    1
;     c8521:                                    1
;     c852d:                                    1
;     c8549:                                    1
;     c8552:                                    1
;     c8585:                                    1
;     c8592:                                    1
;     c85cb:                                    1
;     c8657:                                    1
;     c8690:                                    1
;     c86b3:                                    1
;     c86cb:                                    1
;     c86e8:                                    1
;     c86ee:                                    1
;     c8741:                                    1
;     c878c:                                    1
;     c87a3:                                    1
;     c87ce:                                    1
;     c87f7:                                    1
;     c8800:                                    1
;     c888a:                                    1
;     c888f:                                    1
;     c8895:                                    1
;     c8899:                                    1
;     c88a3:                                    1
;     c88de:                                    1
;     c88df:                                    1
;     c8910:                                    1
;     c8933:                                    1
;     c893a:                                    1
;     c899f:                                    1
;     c89a9:                                    1
;     c89bb:                                    1
;     c89c8:                                    1
;     c89e0:                                    1
;     c89e3:                                    1
;     c89f5:                                    1
;     c89f8:                                    1
;     c8a03:                                    1
;     c8a1a:                                    1
;     c8a23:                                    1
;     c8a31:                                    1
;     c8a70:                                    1
;     c8a73:                                    1
;     c8a84:                                    1
;     c8a98:                                    1
;     c8acf:                                    1
;     c8b10:                                    1
;     c8b1d:                                    1
;     c8b35:                                    1
;     c8b71:                                    1
;     c8bb8:                                    1
;     c8bcc:                                    1
;     c8c07:                                    1
;     c8c43:                                    1
;     c8c4d:                                    1
;     c8c81:                                    1
;     c8cba:                                    1
;     c8d16:                                    1
;     c8d1c:                                    1
;     c8d2a:                                    1
;     c8d7e:                                    1
;     c8dd8:                                    1
;     c8e2a:                                    1
;     c8e2e:                                    1
;     c8e4f:                                    1
;     c8e75:                                    1
;     c8e8b:                                    1
;     c8e9b:                                    1
;     c8ea6:                                    1
;     c8eb7:                                    1
;     c8edb:                                    1
;     c8f15:                                    1
;     c8f1a:                                    1
;     c8f31:                                    1
;     c8f3e:                                    1
;     c8f80:                                    1
;     c8fc0:                                    1
;     c8ff3:                                    1
;     c8ff5:                                    1
;     c9004:                                    1
;     c9019:                                    1
;     c9085:                                    1
;     c90ad:                                    1
;     c90d7:                                    1
;     c9102:                                    1
;     c917c:                                    1
;     c917e:                                    1
;     c9184:                                    1
;     c918a:                                    1
;     c91c3:                                    1
;     c91f5:                                    1
;     c920b:                                    1
;     c920e:                                    1
;     c9254:                                    1
;     c9271:                                    1
;     c9307:                                    1
;     c934c:                                    1
;     c954c:                                    1
;     c970e:                                    1
;     c972b:                                    1
;     c972e:                                    1
;     c97a4:                                    1
;     c97b1:                                    1
;     c97b3:                                    1
;     c97c5:                                    1
;     c97cf:                                    1
;     c97e0:                                    1
;     c97e4:                                    1
;     c97f3:                                    1
;     c97fb:                                    1
;     c981c:                                    1
;     c9870:                                    1
;     c9883:                                    1
;     c989f:                                    1
;     c98af:                                    1
;     c98b6:                                    1
;     c98c6:                                    1
;     c98fa:                                    1
;     c99b5:                                    1
;     c99c3:                                    1
;     c9a04:                                    1
;     c9a07:                                    1
;     c9a0e:                                    1
;     c9a10:                                    1
;     c9a4a:                                    1
;     c9b12:                                    1
;     c9b52:                                    1
;     c9b5c:                                    1
;     c9b88:                                    1
;     c9be4:                                    1
;     c9bfc:                                    1
;     c9c27:                                    1
;     c9c37:                                    1
;     c9c53:                                    1
;     c9c6d:                                    1
;     c9c94:                                    1
;     c9d16:                                    1
;     c9d38:                                    1
;     c9d45:                                    1
;     c9d76:                                    1
;     c9d7d:                                    1
;     c9da1:                                    1
;     c9dab:                                    1
;     c9e49:                                    1
;     c9e55:                                    1
;     c9e65:                                    1
;     c9e75:                                    1
;     c9e96:                                    1
;     c9ea7:                                    1
;     c9f32:                                    1
;     c9fa4:                                    1
;     clear_osbyte_ce_cf:                       1
;     close_handle:                             1
;     close_single_handle:                      1
;     copy_fs_reply_to_cb:                      1
;     copyright_offset:                         1
;     ctrl_block_setup:                         1
;     ctrl_block_setup_clv:                     1
;     ctrl_block_template:                      1
;     data_tx_begin:                            1
;     dispatch_hi:                              1
;     dispatch_lo:                              1
;     dispatch_service:                         1
;     econet_data_terminate_frame:              1
;     error_msg_table:                          1
;     evntv:                                    1
;     filev:                                    1
;     filev_attrib_dispatch:                    1
;     filev_save:                               1
;     forward_star_cmd:                         1
;     fs_cmd_lib:                               1
;     fs_cmd_ptr:                               1
;     fs_cmd_type:                              1
;     fs_osword_tbl_hi:                         1
;     fs_osword_tbl_lo:                         1
;     fs_vector_addrs:                          1
;     fs_wait_cleanup:                          1
;     fscv:                                     1
;     fscv_star_handler:                        1
;     get_file_protection:                      1
;     gsinit:                                   1
;     gsread:                                   1
;     handle_bput_bget:                         1
;     handle_to_mask:                           1
;     handshake_await_ack:                      1
;     immediate_op:                             1
;     init_tx_ctrl_data:                        1
;     init_vectors_and_copy:                    1
;     install_nmi_shim:                         1
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
;     l00f7:                                    1
;     l0104:                                    1
;     l0350:                                    1
;     l0351:                                    1
;     l0355:                                    1
;     l0cff:                                    1
;     l0dda:                                    1
;     l0dfe:                                    1
;     l0e0c:                                    1
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
;     l0fc5:                                    1
;     l0fc6:                                    1
;     l0fe0:                                    1
;     l212e:                                    1
;     l8001:                                    1
;     l8002:                                    1
;     l8004:                                    1
;     l8014:                                    1
;     l8bd7:                                    1
;     l8e79:                                    1
;     l90be:                                    1
;     l944c:                                    1
;     l9a16:                                    1
;     l9b0e:                                    1
;     l9b13:                                    1
;     l9c5b:                                    1
;     l9eca:                                    1
;     l9ed2:                                    1
;     language_entry:                           1
;     language_handler:                         1
;     loop_c0430:                               1
;     loop_c048a:                               1
;     loop_c04d1:                               1
;     loop_c0592:                               1
;     loop_c05a6:                               1
;     loop_c05b5:                               1
;     loop_c05da:                               1
;     loop_c05f8:                               1
;     loop_c0604:                               1
;     loop_c061b:                               1
;     loop_c0638:                               1
;     loop_c0687:                               1
;     loop_c06a5:                               1
;     loop_c80f9:                               1
;     loop_c8113:                               1
;     loop_c8160:                               1
;     loop_c818f:                               1
;     loop_c819d:                               1
;     loop_c81b2:                               1
;     loop_c8219:                               1
;     loop_c82b4:                               1
;     loop_c82ff:                               1
;     loop_c831f:                               1
;     loop_c8361:                               1
;     loop_c838a:                               1
;     loop_c83dd:                               1
;     loop_c8435:                               1
;     loop_c8525:                               1
;     loop_c8543:                               1
;     loop_c8565:                               1
;     loop_c8598:                               1
;     loop_c85a7:                               1
;     loop_c85c2:                               1
;     loop_c85d0:                               1
;     loop_c8607:                               1
;     loop_c865a:                               1
;     loop_c866a:                               1
;     loop_c8699:                               1
;     loop_c86a8:                               1
;     loop_c86f0:                               1
;     loop_c870b:                               1
;     loop_c871f:                               1
;     loop_c8721:                               1
;     loop_c8735:                               1
;     loop_c874a:                               1
;     loop_c8768:                               1
;     loop_c87a0:                               1
;     loop_c87af:                               1
;     loop_c87bd:                               1
;     loop_c87d9:                               1
;     loop_c87eb:                               1
;     loop_c87f9:                               1
;     loop_c8861:                               1
;     loop_c8878:                               1
;     loop_c88d2:                               1
;     loop_c8907:                               1
;     loop_c8916:                               1
;     loop_c893d:                               1
;     loop_c89d4:                               1
;     loop_c8a0f:                               1
;     loop_c8a45:                               1
;     loop_c8a5c:                               1
;     loop_c8abd:                               1
;     loop_c8b03:                               1
;     loop_c8b22:                               1
;     loop_c8b73:                               1
;     loop_c8b97:                               1
;     loop_c8b99:                               1
;     loop_c8b9b:                               1
;     loop_c8ba7:                               1
;     loop_c8c76:                               1
;     loop_c8caf:                               1
;     loop_c8d24:                               1
;     loop_c8e0c:                               1
;     loop_c8eaf:                               1
;     loop_c8ec8:                               1
;     loop_c8f01:                               1
;     loop_c8f30:                               1
;     loop_c8f4e:                               1
;     loop_c8f78:                               1
;     loop_c8f95:                               1
;     loop_c8fd7:                               1
;     loop_c8fe9:                               1
;     loop_c9087:                               1
;     loop_c909c:                               1
;     loop_c90a9:                               1
;     loop_c90db:                               1
;     loop_c912e:                               1
;     loop_c9279:                               1
;     loop_c92a8:                               1
;     loop_c96d1:                               1
;     loop_c99ce:                               1
;     loop_c9a4c:                               1
;     loop_c9a77:                               1
;     loop_c9c10:                               1
;     loop_c9c2d:                               1
;     loop_c9d2c:                               1
;     loop_c9d52:                               1
;     loop_c9d80:                               1
;     loop_c9f77:                               1
;     netv:                                     1
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
;     option_name_offsets:                      1
;     option_name_strings:                      1
;     osargs:                                   1
;     osbget:                                   1
;     osbput:                                   1
;     osbyte_vdu_table:                         1
;     osfile:                                   1
;     osgbpb:                                   1
;     osgbpb_info:                              1
;     osnewl:                                   1
;     osword_tbl_hi:                            1
;     osword_tbl_lo:                            1
;     osword_trampoline:                        1
;     prepare_cmd_with_flag:                    1
;     print_exec_and_len:                       1
;     print_hex_nibble:                         1
;     pydis_start:                              1
;     rdchv:                                    1
;     read_args_size:                           1
;     read_vdu_osbyte:                          1
;     read_vdu_osbyte_x0:                       1
;     restore_econet_state:                     1
;     return_10:                                1
;     return_11:                                1
;     return_13:                                1
;     return_15:                                1
;     return_4:                                 1
;     return_5:                                 1
;     return_6:                                 1
;     return_7:                                 1
;     rom_header:                               1
;     rom_type:                                 1
;     rx_error_reset:                           1
;     save_args_handle:                         1
;     save_econet_state:                        1
;     save_vdu_state:                           1
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
;     setup_fs_vectors:                         1
;     setup_rom_ptrs_netv:                      1
;     setup_rx_buffer_ptrs:                     1
;     skip_cmd_spaces:                          1
;     store_16bit_at_y:                         1
;     store_fs_error:                           1
;     store_retry_count:                        1
;     sub_4_from_y:                             1
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
;     tx_poll_timeout:                          1
;     tx_prepare:                               1
;     tx_src_net:                               1
;     update_sequence_return:                   1
;     wrchv:                                    1

; Automatically generated labels:
;     c0036
;     c0419
;     c0423
;     c0426
;     c0445
;     c045d
;     c0464
;     c0473
;     c04a0
;     c04ae
;     c04ba
;     c04cc
;     c0522
;     c0535
;     c055f
;     c05c2
;     c05d5
;     c067b
;     c811b
;     c811f
;     c817d
;     c81c9
;     c81e6
;     c8212
;     c8240
;     c82c3
;     c832f
;     c8359
;     c835a
;     c8394
;     c8397
;     c83fb
;     c840f
;     c8424
;     c8428
;     c842a
;     c8441
;     c845a
;     c849b
;     c84a0
;     c8521
;     c852d
;     c8549
;     c8552
;     c8584
;     c8585
;     c8592
;     c85a1
;     c85cb
;     c85fe
;     c8637
;     c8657
;     c868c
;     c8690
;     c86b3
;     c86cb
;     c86e8
;     c86ee
;     c8741
;     c878c
;     c87a3
;     c87ce
;     c87f7
;     c8800
;     c8840
;     c888a
;     c888f
;     c8895
;     c8899
;     c88a3
;     c88de
;     c88df
;     c8910
;     c892e
;     c8933
;     c893a
;     c8945
;     c899f
;     c89a9
;     c89b6
;     c89bb
;     c89c8
;     c89e0
;     c89e3
;     c89f5
;     c89f8
;     c8a03
;     c8a1a
;     c8a23
;     c8a31
;     c8a70
;     c8a73
;     c8a84
;     c8a98
;     c8abb
;     c8acf
;     c8b10
;     c8b1d
;     c8b32
;     c8b35
;     c8b71
;     c8bb8
;     c8bcc
;     c8c07
;     c8c43
;     c8c4d
;     c8c81
;     c8cba
;     c8cff
;     c8d16
;     c8d1c
;     c8d2a
;     c8d7e
;     c8dac
;     c8dd6
;     c8dd8
;     c8dda
;     c8e2a
;     c8e2e
;     c8e4f
;     c8e75
;     c8e8b
;     c8e9b
;     c8ea6
;     c8eac
;     c8eb7
;     c8edb
;     c8ee1
;     c8ee3
;     c8f15
;     c8f1a
;     c8f31
;     c8f3e
;     c8f43
;     c8f45
;     c8f48
;     c8f80
;     c8fc0
;     c8ff3
;     c8ff5
;     c9004
;     c9019
;     c907c
;     c9085
;     c90ad
;     c90d7
;     c9102
;     c9105
;     c9167
;     c917c
;     c917e
;     c9184
;     c9186
;     c918a
;     c91c3
;     c91d6
;     c91f5
;     c920b
;     c920e
;     c9254
;     c9271
;     c9307
;     c934c
;     c954c
;     c970e
;     c972b
;     c972e
;     c97a4
;     c97b1
;     c97b3
;     c97c5
;     c97cf
;     c97d7
;     c97e0
;     c97e4
;     c97f3
;     c97fb
;     c981c
;     c9870
;     c9883
;     c989f
;     c98af
;     c98b6
;     c98c6
;     c98f4
;     c98fa
;     c9912
;     c9928
;     c99b5
;     c99b8
;     c99c3
;     c9a04
;     c9a07
;     c9a0e
;     c9a10
;     c9a19
;     c9a4a
;     c9a80
;     c9a8c
;     c9b12
;     c9b4f
;     c9b52
;     c9b5c
;     c9b88
;     c9be4
;     c9bfc
;     c9c27
;     c9c37
;     c9c4f
;     c9c53
;     c9c6d
;     c9c94
;     c9c96
;     c9d16
;     c9d38
;     c9d45
;     c9d76
;     c9d7d
;     c9da1
;     c9dab
;     c9e49
;     c9e55
;     c9e65
;     c9e75
;     c9e96
;     c9ea7
;     c9ebf
;     c9ed5
;     c9f32
;     c9fa4
;     c9fa7
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
;     l00b6
;     l00b7
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
;     l00f7
;     l00fd
;     l00ff
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
;     l0d60
;     l0dda
;     l0dfe
;     l0e0b
;     l0e0c
;     l0e11
;     l0e16
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
;     l0fc5
;     l0fc6
;     l0fde
;     l0fdf
;     l0fe0
;     l212e
;     l8001
;     l8002
;     l8004
;     l800d
;     l8014
;     l833a
;     l8444
;     l8bd7
;     l8e79
;     l90be
;     l944c
;     l9a16
;     l9b0e
;     l9b13
;     l9c5b
;     l9eca
;     l9ed2
;     loop_c0430
;     loop_c048a
;     loop_c04d1
;     loop_c0592
;     loop_c05a6
;     loop_c05b5
;     loop_c05da
;     loop_c05f8
;     loop_c0604
;     loop_c061b
;     loop_c0638
;     loop_c0687
;     loop_c06a5
;     loop_c80f9
;     loop_c8113
;     loop_c8160
;     loop_c818f
;     loop_c819d
;     loop_c81b2
;     loop_c8219
;     loop_c82b4
;     loop_c82ff
;     loop_c831f
;     loop_c8361
;     loop_c838a
;     loop_c83dd
;     loop_c8435
;     loop_c8525
;     loop_c8543
;     loop_c8565
;     loop_c8598
;     loop_c85a7
;     loop_c85c2
;     loop_c85d0
;     loop_c8607
;     loop_c865a
;     loop_c866a
;     loop_c8699
;     loop_c86a8
;     loop_c86f0
;     loop_c870b
;     loop_c871f
;     loop_c8721
;     loop_c8735
;     loop_c874a
;     loop_c8768
;     loop_c87a0
;     loop_c87af
;     loop_c87bd
;     loop_c87d9
;     loop_c87eb
;     loop_c87f9
;     loop_c8861
;     loop_c8878
;     loop_c88d2
;     loop_c8907
;     loop_c8916
;     loop_c893d
;     loop_c89d4
;     loop_c8a0f
;     loop_c8a45
;     loop_c8a5c
;     loop_c8abd
;     loop_c8b03
;     loop_c8b22
;     loop_c8b73
;     loop_c8b97
;     loop_c8b99
;     loop_c8b9b
;     loop_c8ba7
;     loop_c8c76
;     loop_c8caf
;     loop_c8d24
;     loop_c8e0c
;     loop_c8eaf
;     loop_c8ec8
;     loop_c8f01
;     loop_c8f30
;     loop_c8f4e
;     loop_c8f78
;     loop_c8f95
;     loop_c8fd7
;     loop_c8fe9
;     loop_c9087
;     loop_c909c
;     loop_c90a9
;     loop_c90db
;     loop_c912e
;     loop_c9279
;     loop_c92a8
;     loop_c96d1
;     loop_c99ce
;     loop_c9a4c
;     loop_c9a77
;     loop_c9c10
;     loop_c9c2d
;     loop_c9d2c
;     loop_c9d52
;     loop_c9d80
;     loop_c9f77
;     return_1
;     return_10
;     return_11
;     return_12
;     return_13
;     return_14
;     return_15
;     return_2
;     return_3
;     return_4
;     return_5
;     return_6
;     return_7
;     return_8
;     return_9
;     sub_c9a15
;     sub_c9c59
;     sub_c9ec9
;     sub_c9ed1

; Stats:
;     Total size (Code + Data) = 8192 bytes
;     Code                     = 7358 bytes (90%)
;     Data                     = 834 bytes (10%)
;
;     Number of instructions   = 3549
;     Number of data bytes     = 615 bytes
;     Number of data words     = 0 bytes
;     Number of string bytes   = 219 bytes
;     Number of strings        = 38
