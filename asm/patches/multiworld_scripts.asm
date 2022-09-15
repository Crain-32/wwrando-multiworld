.open "sys/main.dol"
.org @NextFreeSpace
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
store_salvage_world_id:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)


  lis r6, world_id@ha
  addi r6, r6, world_id@l
  lbz r0, 0x36 (r5)
  stw r0, 0x0 (r6)

  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
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


.global world_id
world_id:
  nop
.global item_id
item_id:
  nop


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

.org 0x800CCBDC
  bl store_salvage_world_id
.close

