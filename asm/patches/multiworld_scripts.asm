.open "sys/main.dol"
.org @NextFreeSpace
.global custom_write_item_world_id
custom_write_item_world_id:
stwu sp, -0x10 (sp)
mflr r0
stw r0, 0x14 (sp)
lis r5, world_id@ha
addi r5, r5, world_id@l
lha r0, 0x1DC(r30)
rlwinm r0, r0, 0x18, 0x18, 0x1f
stw r0, 0x0(r5)

lis r5, item_id@ha
addi r5, r5, item_id@l
lha r0, 0x1E0(r30)
rlwinm r4, r0, 0x18, 0x18, 0x1f
stw r4, 0x0(r5)

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

.org 0x803F60E0 ; Enable Developer Mode
.byte 1
.close


.open "files/rels/d_a_tbox.rel" ; Treasure chests
.org 0x2761 ; In actionOpenWait__8daTbox_cFv
  b custom_write_item_world_id
.close