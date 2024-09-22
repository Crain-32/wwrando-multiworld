.open "sys/main.dol"

 .org 0x80043238                 ; In dStage_dt_c_roomReLoader
 bl CreateHotest

 .org @NextFreeSpace
 .global CreateHotest
 CreateHotest:
                                 ; Since we have subroutines, we need to store our link register
 stwu sp, -0x10(sp)              ; Save the stack frame
 mflr r0                         ; Move the LR into r0 
 stw r0, 0x14(sp)                ; Store LR in the stack

                                 ; First we call bl	0x80328F8C since we overwrote this call.
 lis   r12, 0x8032               ; Load the upper 16 bits of the address 0x8032 into r12
 ori   r12, r12, 0x8F8C          ; Load the lower 16 bits of the address 0x8F6C into r12
 mtlr  r12                       ; Move the target address from r12 into the link register 
 blrl                            ; Branch to the address in the link register and link back

 bl CreateHotestFunc             ; We call our custom function stored in "includes/CreateHotestFunc.c"

 lwz r0, 0x14(sp)                ; Restore LR from the stack
 mtlr r0                         ; Move the value back into the LR
 addi sp, sp, 0x10               ; Restore the stack frame
 blr                             ; Return

.include "actors\CreateHotestFunc.c"
; Adjust Dolby Camera
.org 0x8022DEE8
li r5, 0x70 ; X
li r6, 0x85 ; Y

;.Change Running animation to have a closed mouth
.org 0x8035C772 ; offset 359772 (Running up / down slopes)
.byte 0x00
.byte 0x02
.org 0x8035C77A ; offset 35977A (Running)
.byte 0x00
.byte 0x02

;.Remove Wind Waker particle effects
.org 0x8014E030
nop

;. Fix Magic Armor lighting
.org 0x80123E80
  lis  r6, 0x37221222@ha
  addi r6, r6, 0x37221222@l

;.Change Wind Waker camera position
.org 0x803f91f8
  .float 0.426   ; x Eye position, where the camera is located, original value = 0.426
  .float 3.0    ; y original value = -13.479
  .float 6.372   ; z original value = 6.372
  .float 10.809  ; x Target position, where the camera is looking, original value = 31.809
  .float 20.14  ; y original value = -51.14
  .float 195.776 ; z original value = 195.776

;.Make hookshot chain invisible
.org 0x8038BD40 ; l_chainS3TCTEX in d_a_hookshot.o
  .space 0x200, 0xFF

;.Change trail colors
.org 0x803F6268 ; Boomerang trail color. (RGBA)
  .byte 0xA5
.org 0x803F6269
  .byte 0x8E
.org 0x803F626A
  .byte 0x6B
.org 0x803F626B
  .byte 0x50
.org 0x803F62AC ; Normal sword slash trail color. (RGBA)
  .byte 0xFF
.org 0x803F62AD
  .byte 0xFF
.org 0x803F62AE
  .byte 0xFF
.org 0x803F62AF
  .byte 0x00
.org 0x803F62B0 ; Elixir soup sword slash trail color. (RGBA)
  .byte 0xFF
.org 0x803F62B1
  .byte 0xFF
.org 0x803F62B2
  .byte 0xFF
.org 0x803F62B3
  .byte 0x00
.org 0x803F62B4 ; Parrying sword slash trail color. (RGBA)
  .byte 0xFF
.org 0x803F62B5
  .byte 0xFF
.org 0x803F62B6
  .byte 0xFF
.org 0x803F62B7
  .byte 0x00

;.Remove black and white effect from Hyrule
.org 0x80236204
  b 0x80236270

;.Make sail invisible
.org 0x800E93B8 ; daHo_packet_c::draw(void)
  blr
.close