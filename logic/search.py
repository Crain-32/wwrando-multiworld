import copy

from classes.area import Area, Exit
from classes.gameitem import GameItem
from classes.location import Location
from classes.requirement import Requirement
from classes.world import World
from data.extras import *
from logic.spoilerlog import generate_spoiler_log

called = 0

def evaluate_requirement(world: World, requirement: Requirement, owned_items: list[GameItem]) -> bool:
    if requirement.type == REQUIREMENT_OR:
        return any(
            map((lambda args: evaluate_requirement(world, args, owned_items) == True), requirement.args)
        )

    elif requirement.type == REQUIREMENT_AND:
        return all(
            map((lambda args: evaluate_requirement(world, args, owned_items) == True), requirement.args)
        )

    elif requirement.type == REQUIREMENT_NOT:
        return not evaluate_requirement(world, requirement.args[0], owned_items)

    elif requirement.type == REQUIREMENT_CAN_ACCESS:
        return world.area_entries[requirement.args[0]].is_accessible

    elif requirement.type == REQUIREMENT_SETTING:
        return bool(world.world_settings.progressive_categories[requirement.args[0]])

    elif requirement.type == REQUIREMENT_MACRO:
        return evaluate_requirement(world, world.macros[requirement.args[0]].expression, owned_items)

    elif requirement.type == REQUIREMENT_HAS_ITEM:
        if len(requirement.args) > 1:
            return False
        if isinstance(requirement.args[0], str):
            requirement.args[0] = item_id_dict[requirement.args[0]]
        if requirement.args[0] == item_id_dict["Nothing"]:
            return True
        game_item = GameItem(game_item_id=requirement.args[0], world_id=world.world_id)
        return any(map(game_item.soft_equality, owned_items))

    elif requirement.type == REQUIREMENT_COUNT:
        expected_count = int(requirement.args[0])
        if isinstance(requirement.args[1], str):
            requirement.args[1] = item_id_dict[requirement.args[1]]
        expected_item_id = int(requirement.args[1])
        if expected_item_id == item_id_dict["Nothing"]:
            return True
        else:
            expected_item = GameItem(game_item_id=expected_item_id, world_id=world.world_id)
            return len([item for item in owned_items if expected_item.soft_equality(item)]) >= expected_count

    elif requirement.type is None:
        raise RuntimeError(f"Requirement was 'None': {requirement} for World {world}")
    return False

def explore(worlds: list[World], items: list[list[GameItem]], area: Area, exits_to_try: list[Exit], locations_to_try: list[Location]) -> list[Location]:

    for exit_connection in area.exits.values():
        connect_area = worlds[exit_connection.world_id].area_entries[exit_connection.name]

        if not connect_area.is_accessible:
            if evaluate_requirement(worlds[exit_connection.world_id], exit_connection.requirement, items[exit_connection.world_id]):
                connect_area.is_accessible = True
                worlds[exit_connection.world_id].area_entries[connect_area.name] = connect_area
                # Potentially giving duplicates, this provides duplicates, refactor to reduce overhead
                locations_to_try = explore(worlds, items, connect_area, exits_to_try, locations_to_try)
            else:
                exits_to_try.insert(0, exit_connection)

    for location in area.locations:
        #See comment about duplicates
        if location not in locations_to_try:
            locations_to_try.append(location)
    return locations_to_try


def search(search_mode: str, worlds: list[World], input_items: list[GameItem], world_id = -1):
    assumed_items = list()
    for world in worlds:
        assumed_items.append(world.starting_items.copy())
        world_input_items = [item for item in input_items if item.world_id == world.world_id]
        assumed_items[world.world_id].extend(world_input_items)

    if search_mode == SEARCH_GENERATE_PLAYTHROUGH:
        worlds[0].assumed_items = copy.deepcopy(assumed_items)

    accessible_locations = []
    exits_to_try = []
    locations_to_try = []
    for world in worlds:
        if world_id == -1 or world_id == world.world_id:

            for exit_connection in world.area_entries["Root"].exits.values():
                exits_to_try.append(exit_connection)

            for area_entry in world.area_entries.values():
                area_entry.is_accessible = False
                world.area_entries[area_entry.name] = area_entry

    sphere = 0
    something_found = True
    while something_found:
        something_found = False
        for exit_connection in exits_to_try:
            if evaluate_requirement(worlds[exit_connection.world_id], exit_connection.requirement, assumed_items[exit_connection.world_id]):
                something_found = True
                exits_to_try.remove(exit_connection)
                connected_area = worlds[exit_connection.world_id].area_entries[exit_connection.name]
                if not connected_area.is_accessible:
                    connected_area.is_accessible = True
                    worlds[exit_connection.world_id].area_entries[exit_connection.name] = connected_area
                    locations_to_try = explore(worlds, assumed_items, connected_area, exits_to_try, locations_to_try)

        accessible_this_iteration = []
        for location in locations_to_try:
            if evaluate_requirement(worlds[location.world_id], location.requirement, assumed_items[location.world_id]):
                something_found = True
                accessible_this_iteration.append(location)
                locations_to_try.remove(location)

        if search_mode == SEARCH_GENERATE_PLAYTHROUGH:
            worlds[0].play_through_spheres.append(list())

        for location in accessible_this_iteration:
            accessible_locations.append(location)
            if location.current_item.game_item_id != item_id_dict['Nothing']:
                assumed_items[location.current_item.world_id].append(GameItem(game_item_id=location.current_item.game_item_id, world_id=location.current_item.world_id))
                if search_mode == SEARCH_GENERATE_PLAYTHROUGH and location.logical:
                    worlds[0].play_through_spheres[sphere].append(location)
                    worlds[0].assumed_items[location.current_item.world_id].append(GameItem(game_item_id=location.current_item.game_item_id, world_id=location.current_item.world_id))
        sphere += 1

    return accessible_locations

def get_accessible_locations(worlds: list[World], assumed_items: list[GameItem], allowed_locations: list[Location], world_to_search= -1) -> list[Location]:
    accessible_locations = search(SEARCH_ACCESSIBLE_LOCATIONS, worlds, assumed_items, world_to_search)
    return [location for location in accessible_locations
                if location.current_item.game_item_id == item_id_dict["Nothing"]
                and Location.partial_list_comparison(allowed_locations, location)]

def game_beatable(worlds):
    accessible_locations = search(SEARCH_ACCESSIBLE_LOCATIONS, worlds, [])
    worlds_beatable = [location for location in accessible_locations
                       if location.current_item.game_item_id == item_id_dict["GameBeatable"]]
    return len(worlds) == len(worlds_beatable)

# Whittle down the playthrough to only the items which are required to beat the game
def pare_down_playthrough(worlds: list[World]) -> list[World]:
    playthrough_spheres = worlds[0].play_through_spheres
    for sphere in range(0, len(playthrough_spheres)):
        for location in playthrough_spheres[sphere]:
            new_location = copy.deepcopy(location)
            new_location.current_item = GameItem(item_id_dict['Nothing'], location.world_id)
            worlds[location.world_id].location_entries.remove(location)
            worlds[location.world_id].location_entries.append(new_location)
            if not game_beatable(worlds):
                playthrough_spheres[sphere].remove(location)
            worlds[location.world_id].location_entries.remove(new_location)
            worlds[location.world_id].location_entries.append(location)
    worlds[0].play_through_spheres = playthrough_spheres
    return worlds

def generate_playthrough(worlds: list[World]):
    search(SEARCH_GENERATE_PLAYTHROUGH, worlds, [])
    dump_object(worlds[0].assumed_items, "assumed_by_search")
    worlds = pare_down_playthrough(worlds)
    generate_spoiler_log(worlds)


def locations_reachable(worlds: list[World], items: list[GameItem],
                        locations_to_check: list[Location], world_to_search: int) -> bool:
    accessible_locations = search(SEARCH_ACCESSIBLE_LOCATIONS, worlds, items, world_to_search)

    if len(locations_to_check) < len(accessible_locations):
        return False

    return all(
            map(
                (lambda loc: loc in accessible_locations),
                locations_to_check
                )
            )

