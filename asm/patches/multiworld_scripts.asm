.open "sys/main.dol"
.org @NextFreeSpace

; Basically is a multiplayer struct we work with. Just in... Assembly...
; byte worldId
; byte itemId
; byte stageId
; bool eventHappenFlag
; pointer* pointerStorage

.global world_id
world_id:
  nop
.global item_id
item_id:
  nop
.global event_happen_flag
event_happen_flag:
  nop
.global stage_id_pointer
stage_id_pointer:
  nop


.global custom_write_item_world_id
custom_write_item_world_id:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)

  lis r5, item_id@ha
  addi r5, r5, item_id@l
  andi. r0, r0, 0x0000; Otherwise we'll scan a non-zero byte.
  stw r0, 0x0(r5)

  lis r5, world_id@ha
  addi r5, r5, world_id@l
  lha r0, 0x1DC(r30)
  rlwinm r0, r0, 0x18, 0x18, 0x1f
  stw r0, 0x0(r5)


  lha r0, 0x1E0(r30)
  rlwinm r4, r0, 0x18, 0x18, 0x1f

  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr

.global adjust_salvage_chests
adjust_salvage_chests:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)


  stb r29, 0x34 (r3)
  lha r29, 0x1E0 (r21)
  rlwinm r29, r29, 0x18, 0x18, 0x1F
  stb r29, 0x36 (r3)
  lbz r29, 0x34 (r3)

  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr

.global store_salvage_world_id ; 0x80480338? checkOrder Entry?
store_salvage_world_id:        ; R3 has to have the Item Id.
  mulli r0, r4, 0x38           ; R4 is set after return
  add r3, r3, r0               ; R5 see above

  lis r5, item_id@ha
  addi r5, r5, item_id@l
  andi. r4, r4, 0x0000; Otherwise we'll scan a non-zero byte.
  stw r4, 0x0(r5)

  lis r5, world_id@ha
  addi r5, r5, world_id@l
  lbz r4, 0x36 (r3)
  stw r4, 0x0 (r5)

  lbz r3, 0x34 (r3)

  blr

.global get_item_detour
get_item_detour:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)

  lis r12, item_id@ha
  addi r12, r12, item_id@l
  stb r3, 0x3(r12)

  lis r12, world_id@ha
  addi r12, r12, world_id@l
  lbz r12, 0x3(r12)

.global inject_world_id
  inject_world_id:
  cmpwi r12, 0x01          ; This World's ID needs to be inject here
  beq give_item_to_player  ; Jump to giving item
  cmpwi r12, 0x00          ; Compare the Item's World ID to Zero. Handles Normal Items
  bne skip_giving_item     ; This needs to jump to *after* the item giving function resolves

  give_item_to_player:
  rlwinm r0, r3, 0x2, 0x16, 0x1d
  lis r3, -0x7fc7
  subi r3, r3, 0x7738
  lwzx r12, r3, r0
  mtctr r12
  bctrl

  skip_giving_item:
  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr

.global mark_switch_stage_event
  mark_switch_stage_event:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)
  stw r31, 0x0C (sp)
  stw r30, 0x08 (sp)

  li r30, 1
  lis r31, event_happen_flag@ha
  addi r31, r31, event_happen_flag@l
  stb r30, 0x0(r31)

  lis r31, stage_id_pointer@ha
  addi r31, r31, stage_id_pointer@l
  stw r3, 0x0(r31)

  lwz r31, 0x0C (sp)
  lwz r30, 0x8 (sp)

  srawi r0, r31, 0x5
  rlwinm r0, r0, 0x2, 0x0, 0x1D
  add r5, r30, r0
  lwz r4, 0x4(r5)
  li r3, 0x1
  rlwinm r0, r31, 0x0, 0x1B, 0x1F
  slw r0, r3, r0
  or r0, r4, r0
  stw r0, 0x4(r5)

  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr

.global mark_tbox_stage_event
  mark_tbox_stage_event:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)
  stw r29, 0x0C (sp)
  stw r28, 0x08 (sp)

  li r28, 2
  lis r29, event_happen_flag@ha
  addi r29, r29, event_happen_flag@l
  stb r28, 0x0(r29)

  lis r29, stage_id_pointer@ha
  addi r29, r29, stage_id_pointer@l
  stw r3, 0x0(r29)

  lwz r29, 0x0C (sp)
  lwz r28, 0x8 (sp)

  lwz r3, 0x0 (r30)
  li r0, 0x1
  slw r0, r0, r31
  or r0, r3, r0
  stw r0, 0x0(r30)
  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr

.global mark_story_event
  mark_story_event:
  stwu sp, -0x10 (sp)
  stw r6, 0x14 (sp)
  stw r31, 0x0C (sp)
  stw r30, 0x08 (sp)

  li r30, 3
  lis r31, event_happen_flag@ha
  addi r31, r31, event_happen_flag@l
  stb r30, 0x0(r31)

  rlwinm r6, r4, 0x18, 0x18, 0x1f
  lbzx r5, r3, r6
  rlwinm r0, r4, 0x0, 0x18, 0x1f
  or r0, r5, r0
  stbx r0, r3, r6

  add r30, r3, r6
  lis r31, stage_id_pointer@ha
  addi r31, r31, stage_id_pointer@l
  stw r30, 0x0(r31)


  lwz r31, 0x0C (sp)
  lwz r30, 0x8 (sp)
  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr


.org 0x8005C298 ; "dSv_memBit_c::onSwitch"
 bl mark_switch_stage_event
 nop
 nop
 nop
 nop
 nop
 nop
 nop
 nop

.org 0x8005C15C ; "dSv_memBit_c::onTbox"
 bl mark_tbox_stage_event
 nop
 nop
 nop
 nop

.org 0x8005CB04 ; "dSv_event_c::onEventBit"
  mflr r6
  bl mark_story_event
; It kills Korl for some reason.


.org 0x800C2E08
  bl get_item_detour
  nop
  nop
  nop
  nop
  nop
.close



.open "files/rels/d_a_tbox.rel" ; Treasure Chests
.org 0x2764 ; In actionOpenWait__8daTbox_cFv
  bl custom_write_item_world_id
.close

.open "sys/main.dol" ; Store World ID for Salvage Chests
.org 0x800CCAA4
  bl adjust_salvage_chests
.close

.open "files/rels/d_a_salvage.rel"
.org 0xb34 ; in checkOrder__11daSalvage_cFv
  bl store_salvage_world_id
.close


.open "files/rels/d_a_boss_item.rel"
.org 0x1C4 ; In daBossItem_Create 0x805D_A030
  bl mark_story_event ; SHORT TERM FOR TESTING, THIS IS NOT SAFE
  ;lbz r4, 0x00B2(r30) ; This should be the equivalent of 0x00FFFF00 for the mask? Lower is Item ID, upper is World ID
.close
