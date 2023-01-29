import os
import re
from re import Match
from typing import TYPE_CHECKING

from classes.gameitem import junk_item_ids
from fs_helpers import *

if TYPE_CHECKING:
    from randomizer import Randomizer


def write_changed_items(randomizer: 'Randomizer', world_id: int = 0):
    locations = randomizer.worlds[world_id].location_entries
    for location in locations:
        for path in location.filePaths:
            if location.current_item.game_item_id == 0xB1:
                location.current_item.game_item_id = randomizer.rng.choice(junk_item_ids)
            if location.current_item.world_id == -1:
                location.current_item.world_id = world_id
            change_item(randomizer, path, location.current_item.game_item_id, (location.current_item.world_id + 1))


def change_item(randomizer: 'Randomizer', path: AnyStr, item_id: int, world_id: int = 0):
    rel_match: Match | None = re.search(r"^(rels/[^.]+\.rel)@([0-9A-F]{4})$", path)
    main_dol_match: Match | None = re.search(r"^main.dol@(8[0-9A-F]{7})$", path)
    custom_symbol_match: Match | None = re.search(r"^CustomSymbol:(.+)$", path)
    chest_match: Match | None = re.search(r"^([^/]+/[^/]+\.arc)(?:/Layer([0-9a-b]))?/Chest([0-9A-F]{3})$", path)
    event_match: Match | None = re.search(
        r"^([^/]+/[^/]+\.arc)/Event([0-9A-F]{3}):[^/]+/Actor([0-9A-F]{3})/Action([0-9A-F]{3})$", path)
    scob_match: Match | None = re.search(r"^([^/]+/[^/]+\.arc)(?:/Layer([0-9a-b]))?/ScalableObject([0-9A-F]{3})$", path)
    actor_match: Match | None = re.search(r"^([^/]+/[^/]+\.arc)(?:/Layer([0-9a-b]))?/Actor([0-9A-F]{3})$", path)
    inject_match: Match | None = re.search(r"^inject_(rels/[^.]+\.rel)@(.*)$", path)

    if rel_match:
        rel_path = rel_match.group(1)
        offset = int(rel_match.group(2), 16)
        path = os.path.join("files", rel_path)
        change_hardcoded_item_in_rel(randomizer, path, offset, item_id, world_id)
    elif main_dol_match:
        address = int(main_dol_match.group(1), 16)
        change_hardcoded_item_in_dol(randomizer, address, item_id, world_id)
    elif custom_symbol_match:
        custom_symbol = custom_symbol_match.group(1)
        found_custom_symbol = False
        for file_path, custom_symbols_for_file in randomizer.custom_symbols.items():
            if custom_symbol in custom_symbols_for_file:
                found_custom_symbol = True
                if file_path == "sys/main.dol":
                    address = custom_symbols_for_file[custom_symbol]
                    change_hardcoded_item_in_dol(randomizer, address, item_id, world_id)
                else:
                    offset = custom_symbols_for_file[custom_symbol]
                    change_hardcoded_item_in_rel(randomizer, file_path, offset, item_id, world_id)
                break
        if not found_custom_symbol:
            raise Exception("Invalid custom symbol: %s" % custom_symbol)
    elif chest_match:
        arc_path = "files/res/Stage/" + chest_match.group(1)
        if chest_match.group(2):
            layer = int(chest_match.group(2), 16)
        else:
            layer = None
        chest_index = int(chest_match.group(3), 16)
        change_chest_item(randomizer, arc_path, chest_index, layer, item_id, world_id)
    elif event_match:
        arc_path = "files/res/Stage/" + event_match.group(1)
        event_index = int(event_match.group(2), 16)
        actor_index = int(event_match.group(3), 16)
        action_index = int(event_match.group(4), 16)
        change_event_item(randomizer, arc_path, event_index, actor_index, action_index, item_id, world_id)
    elif scob_match:
        arc_path = "files/res/Stage/" + scob_match.group(1)
        if scob_match.group(2):
            layer = int(scob_match.group(2), 16)
        else:
            layer = None
        scob_index = int(scob_match.group(3), 16)
        change_scob_item(randomizer, arc_path, scob_index, layer, item_id, world_id)
    elif actor_match:
        arc_path = "files/res/Stage/" + actor_match.group(1)
        if actor_match.group(2):
            layer = int(actor_match.group(2), 16)
        else:
            layer = None
        actor_index = int(actor_match.group(3), 16)
        change_actor_item(randomizer, arc_path, actor_index, layer, item_id, world_id)
    elif inject_match:
        inject_world_id(randomizer, inject_match.group(1), inject_match.group(2), world_id)
    else:
        raise Exception("Invalid item path: " + path)

def inject_world_id(randomizer: 'Randomizer', rel_path: AnyStr, offset_symbol: AnyStr, world_id: int = 0):
    path = os.path.join("files", rel_path)
    rel = randomizer.get_rel(path)
    rel.write_data(write_u8, randomizer.custom_symbols[f"files/{rel_path}"][offset_symbol] + 3, world_id)


def change_hardcoded_item_in_dol(randomizer: 'Randomizer', address, item_id: int, world_id: int = 0):
    randomizer.dol.write_data(write_u8, address, item_id)


def change_hardcoded_item_in_rel(randomizer: 'Randomizer', path: AnyStr, offset: int, item_id: int, world_id: int = 0):
    rel = randomizer.get_rel(path)
    rel.write_data(write_u8, offset, item_id)


def change_chest_item(randomizer: 'Randomizer', arc_path: AnyStr, chest_index: int, layer: int, item_id: int,
                      world_id: int = 0):
    if arc_path.endswith("Stage.arc"):
        dzx = randomizer.get_arc(arc_path).get_file("stage.dzs")
    else:
        dzx = randomizer.get_arc(arc_path).get_file("room.dzr")
    chest = dzx.entries_by_type_and_layer("TRES", layer)[chest_index]
    chest.item_id = item_id
    chest.world_id = world_id
    chest.save_changes()


def change_event_item(randomizer: 'Randomizer', arc_path, event_index, actor_index, action_index, item_id: int,
                      world_id: int = 0):
    event_list = randomizer.get_arc(arc_path).get_file("event_list.dat")
    action = event_list.events[event_index].actors[actor_index].actions[action_index]

    if 0x6D <= item_id <= 0x72:  # Song
        action.name = "059get_dance"
        action.properties[0].value = [item_id - 0x6D]
    else:
        action.name = "011get_item"
        action.properties[0].value = [item_id]


def change_scob_item(randomizer: 'Randomizer', arc_path, scob_index, layer, item_id: int, world_id: int = 0):
    if arc_path.endswith("Stage.arc"):
        dzx = randomizer.get_arc(arc_path).get_file("stage.dzs")
    else:
        dzx = randomizer.get_arc(arc_path).get_file("room.dzr")
    scob = dzx.entries_by_type_and_layer("SCOB", layer)[scob_index]
    if scob.actor_class_name in ["d_a_salvage", "d_a_tag_kb_item"]:
        scob.item_id = item_id
        scob.world_id = 0x69
        scob.save_changes()
    else:
        raise Exception("%s/SCOB%03X is an unknown type of SCOB" % (arc_path, scob_index))


def change_actor_item(randomizer: 'Randomizer', arc_path, actor_index, layer, item_id: int, world_id: int = 0):
    if arc_path.endswith("Stage.arc"):
        dzx = randomizer.get_arc(arc_path).get_file("stage.dzs")
    else:
        dzx = randomizer.get_arc(arc_path).get_file("room.dzr")
    actr = dzx.entries_by_type_and_layer("ACTR", layer)[actor_index]
    if actr.actor_class_name == "d_a_item":
        actr.item_id = item_id
    elif actr.actor_class_name == "d_a_boss_item":
        actr.item_id = item_id
    else:
        raise Exception("%s/ACTR%03X is not an item" % (arc_path, actor_index))

    actr.save_changes()
