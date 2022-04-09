import copy
import itertools
import os

from classes.gameitem import *
from classes.world import World
from logic.extras import item_id_dict, capital_case_with_space, chart_macro_to_island

def generate_spoiler_log(worlds: list[World], output_folder, output_file_name):
    with open(os.path.join(output_folder, ("WW" + output_file_name +"- Spoiler Log.txt")), 'w') as spoiler_log_file:
        for world in worlds:
            spoiler_log_file.write(world.world_settings.spoiler_representation(world.world_id + 1))
            if world.world_settings.race_mode:
                spoiler_log_file.write(f"Race Mode Dungeons for World {world.world_id + 1}\n")
                spoiler_log_file.write(f'{", ".join(world.race_mode_dungeons)}\n\n')

        # for sphere in range(0, len(worlds[0].play_through_spheres)):
        #     if len(worlds[0].play_through_spheres[sphere]) == 0:
        #         continue
        #     spoiler_log_file.write(f"Sphere: {sphere}\n")
        #
        #     for location in worlds[0].play_through_spheres[sphere]:
        #         spoiler_log_file.write(location.spoiler_representation() + '\n')
        # spoiler_log_file.write("\n")
        spoiler_log_file.write("All Locations: \n")
        required_items = list()
        for amount in range(len(worlds)):
            required_items.append(list())
        for world in worlds:
            for location in world.location_entries:
                if location.current_item.game_item_id != item_id_dict["Nothing"]:
                    required_items[location.current_item.world_id].append(location)
                    spoiler_log_file.write(location.spoiler_representation() + '\n')

        chart_locations = list()
        for x in range(len(worlds)):
            chart_locations.append(dict())
        sunken_treasures = copy.deepcopy(chart_locations)

        spoiler_log_file.write("\n")
        for world_id, required_items_in_world in enumerate(required_items):
            spoiler_log_file.write(f"World {world_id + 1} Potentially Major Items\n")
            item_type_groups = itertools.groupby(
                                sorted(
                                    map(
                                        (lambda g: g.set_item_type()),
                                        required_items_in_world),
                                    key=lambda i: i.current_item.item_type),
                                lambda l: l.current_item.item_type)

            for item_type, location_list in item_type_groups:
                location_list = list(sorted(location_list, key=lambda loc:item_id_to_name_dict[loc.current_item.game_item_id]))
                if len(location_list) == 0 or item_type == ITEM_IS_UNCATEGORIZED:
                    continue
                spoiler_log_file.write(f"{item_type_to_name[item_type]}\n")
                for location in location_list:
                    if item_type == ITEM_IS_TRIFORCE_CHART or item_type == ITEM_IS_TREASURE_CHART:
                        chart_locations[location.current_item.world_id][location.current_item.game_item_id] = location.spoiler_short_hand_loc_rep()
                    if "SunkenTreasure" in location.name:
                        sunken_treasures[location.world_id][capital_case_with_space(location.name)] = location.spoiler_short_hand_item_rep()
                    spoiler_log_file.write(f"{item_id_to_name_dict[location.current_item.game_item_id]}: {location.spoiler_short_hand_loc_rep()}\n")
                spoiler_log_file.write("\n")
        spoiler_log_file.write("\n")

        for world_id, world in enumerate(worlds):
            spoiler_log_file.write(f"Sunken Treasure and Charts for World {world_id + 1}\n")
            for chart_macro_name, chart_island in chart_macro_to_island.items():
                if chart_island in sunken_treasures[world_id]:
                    chart_macro = world.macros[chart_macro_name]
                    spoiler_log_file.write(f"{chart_island}:\n")
                    spoiler_log_file.write(f"\t{item_id_to_name_dict[chart_macro.expression.args[0]]} : {chart_locations[world_id][chart_macro.expression.args[0]]}\n")
                    spoiler_log_file.write(f"\tSunken Treasure: {sunken_treasures[world_id][chart_island]}\n")
            spoiler_log_file.write("\n")

