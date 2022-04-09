import itertools
import os
from dataclasses import dataclass, field

from classes.area import Area
from classes.gameitem import GameItem, junk_item_check
from classes.location import Location
from classes.requirement import Macro, Requirement
from classes.settings import Settings
from data.extras import *
from logic.item_pool import generate_game_item_pool, generate_starting_items, dungeons
from wwrando_paths import DATA_PATH


@dataclass
class World:

    world_settings: Settings
    world_id: int
    starting_items: list[GameItem] = field(default_factory=list)
    item_pool: list[GameItem] = field(default_factory=list)
    area_entries: dict[str, Area] = field(default_factory=dict)
    location_entries: list[Location] = field(default_factory=list)
    macros: dict[str, Macro] = field(default_factory=dict)
    play_through_spheres: list[list[Location]] = field(default_factory=list)
    race_mode_dungeons: list[str] = field(default_factory=list)


    def __init__(self, settings: Settings, world_id: int):
        self.world_settings = settings
        self.world_id = world_id
        self.race_mode_dungeons = []
        self.play_through_spheres = []
        self.assumed_items = []

    def __hash__(self):
        return hash(self.world_id)

    def set_item_pools(self):
        starting_item_pool = generate_starting_items(self.world_settings)
        game_item_pool = generate_game_item_pool(self.world_settings, starting_item_pool)
        self.item_pool = list(
                            map(junk_item_check,
                                map(
                                (lambda item: GameItem(game_item_id=item, world_id=self.world_id)),
                                 game_item_pool
                                ))
                            )
        self.starting_items = [GameItem(game_item_id=item, world_id=self.world_id) for item in starting_item_pool]

    def change_world_id(self, different_id: int):
        self.world_id = different_id
        if 'starting_items' in self.__dict__.keys() and isinstance(self.starting_items, list):
            for item in self.starting_items:
                item.world_id = different_id
        if 'item_pool' in self.__dict__.keys() and isinstance(self.item_pool, list):
            for item in self.item_pool:
                item.world = different_id
        if 'area_entries' in self.__dict__.keys() and isinstance(self.area_entries, dict):
            for key, val in self.area_entries.items():
                val = val.set_world_id(different_id)
                self.area_entries[key] = val
        if 'location_entries' in self.__dict__.keys() and isinstance(self.location_entries, list):
            for loc in self.location_entries:
                loc.world_id = different_id


    def determine_chart_mappings(self, random_state):
        chart_mappings = [
         "TreasureChart25",
         "TreasureChart7",
         "TreasureChart24",
         "TriforceChart2",
         "TreasureChart11",
         "TriforceChart7",
         "TreasureChart13",
         "TreasureChart41",
         "TreasureChart29",
         "TreasureChart22",
         "TreasureChart18",
         "TreasureChart30",
         "TreasureChart39",
         "TreasureChart19",
         "TreasureChart8",
         "TreasureChart2",
         "TreasureChart10",
         "TreasureChart26",
         "TreasureChart3",
         "TreasureChart37",
         "TreasureChart27",
         "TreasureChart38",
         "TriforceChart1",
         "TreasureChart21",
         "TreasureChart6",
         "TreasureChart14",
         "TreasureChart34",
         "TreasureChart5",
         "TreasureChart28",
         "TreasureChart35",
         "TriforceChart3",
         "TriforceChart6",
         "TreasureChart1",
         "TreasureChart20",
         "TreasureChart36",
         "TreasureChart23",
         "TreasureChart12",
         "TreasureChart16",
         "TreasureChart4",
         "TreasureChart17",
         "TreasureChart31",
         "TriforceChart5",
         "TreasureChart9",
         "TriforceChart4",
         "TreasureChart40",
         "TriforceChart8",
         "TreasureChart15",
         "TreasureChart32",
         "TreasureChart33",
        ]
        if self.world_settings.randomize_charts:
            random_state.rng.shuffle(chart_mappings)

        for sector, chart in enumerate(chart_mappings):
            self._replace_macro_item(f"Chart for Island {sector + 1}", Requirement(REQUIREMENT_HAS_ITEM, [chart]))

    def determine_progression_locations(self):
        self.location_entries = self.determine_progression_locations_from_list(self.location_entries)

    def determine_progression_locations_from_list(self, location_list: list[Location])-> list[Location]:
        return list(
                    map(
                        (lambda logical: logical.make_logical()),
                         filter(
                             (lambda progressive:
                                World.location_category_cache(self._location_category_list(),
                                                              progressive.category_set) and "Multiworld" in progressive.category_set
                               ),
                             location_list
                         )
                    )
                )

    def determine_race_mode_dungeons(self, random_state):
        if self.world_settings.race_mode:
            shuffled_dungeons = DUNGEON_NAMES.copy()
            random_state.rng.shuffle(shuffled_dungeons)

            for index, dungeon_name in enumerate(shuffled_dungeons):
                if index < self.world_settings.num_race_mode_dungeons:
                    self.race_mode_dungeons += [dungeon_name]
                else:
                    self._set_dungeon_non_progressive(dungeon_name)

    def load_world(self, world_file="world.json", macro_file="Macros.json"):
        self.area_entries = World.load_parse_world(os.path.join(DATA_PATH, world_file), self.world_id)
        self.macros = {macro.name: macro for macro in World.load_parse_macros(os.path.join(DATA_PATH, macro_file))}
        self.location_entries = list(
            map(
                (lambda b: b.set_world_id(self.world_id)),
                itertools.chain.from_iterable(
                    list(
                        map(
                            (lambda a: a.get_locations()),
                            self.area_entries.values()
                            )
                        )
                    )
                )
            )


    def dump_world_graph(self, filename: str):
        with open("./dump/" + filename + ".dot", 'w') as world_dump:
            world_dump.write("digraph {\n\tcenter=true;\n")
            for area in self.area_entries.values():
                color = '"black"' if area.is_accessible else '"red"'
                world_dump.write(f'\t"{area.name}"[shape="plain" fontcolor={color}];\n')
                for exits in area.exits.values():
                    world_dump.write(f'\t"{area.name}"->"{exits.name}"\n')

                for location in area.locations:
                    world_dump.write(f'\t"{location.name}"[label=<{location.name}:<br/>{item_id_to_name_dict[location.current_item.game_item_id]}> shape="plain" fontcolor={color}];\n')
                    world_dump.write(f'\t"{area.name}" -> "{location.name}"[dir=forward colors={color}]\n')
            world_dump.write("}")


    @staticmethod
    def chart_leads_to_sunken_treasure(location: Location, item_prefix) -> bool:
        if LOCATION_CATEGORY_SUNKEN_TREASURE not in location.category_set:
            print(f"Non-sunken Location {location} passed into Sunken Treasure Check")
            return False
        # Not entirely certain what is happening here
        return True

    def set_location(self, loc_name: str, item_val: int, world_id: int):
        loc_list = list(filter((lambda loc_l: loc_name in loc_l.name), self.location_entries))
        if len(loc_list) == 0 or len(loc_list) > 1:
            raise RuntimeError(f"Could not find Location with name {loc_name}, found {loc_list} instead")
        loc = loc_list[0]
        self.location_entries.remove(loc)
        loc.current_item = GameItem(game_item_id=item_val, world_id=world_id)
        self.location_entries.append(loc)

    def get_dungeon_locations(self) -> list[Location]:
        dungeon_locations = []
        for dungeon_name in self.race_mode_dungeons:
            dungeon_locations.extend(
                self.get_specific_dungeon_locations(dungeon_name)
            )
        return dungeon_locations

    def get_specific_dungeon_locations(self, dungeon_name: str) -> list[Location]:
        if dungeon_name == "TowerOfTheGods":
            dungeon_name = "TOTG"
        return list(
                filter(
                    (lambda loc: dungeon_name in loc.name and "SunkenTreasure" not in loc.name),
                    self.location_entries)
                )

    def get_race_mode_bosses(self):
        boss_loc = []
        for dungeon_name in self.race_mode_dungeons:
            boss_loc.append(self.get_specific_dungeon_locations(dungeon_name)[-1])
        return boss_loc

    def get_dungeon_keys(self, dungeon_name: str) -> list[GameItem]:
        if dungeon_name == "ForsakenFortress":
            return []

        keys_value = dungeons[dungeon_name + "Keys"]
        dungeon_keys = list(
                        filter(
                            (lambda game_key: game_key.game_item_id in keys_value),
                            self.item_pool
                            ),
                        )
        for key in dungeon_keys:
            self.item_pool.remove(key)
        return dungeon_keys

    def get_dungeon_extras(self, dungeon_name: str) -> list[GameItem]:
        keys_value = dungeons[dungeon_name + "Extras"]
        dungeon_extras = list(
                            filter(
                            (lambda key: key.game_item_id in keys_value),
                            self.item_pool
                            ),
                        )
        for extra in dungeon_extras:
            self.item_pool.remove(extra)
        return dungeon_extras

    @staticmethod
    def load_parse_macros(macro_location: str) -> list[Macro]:
        with open(macro_location) as macros_loc:
            macro_file = json.load(macros_loc)
            macro_list = list(map(Macro.from_dict, macro_file["Macros"]))
            macro_names = [macro.name for macro in macro_list]
            if len(macro_names) != len(set(macro_names)):
                raise RuntimeError(f"Duplicate Macro Name Provided!\n {macro_names}")
            else:
                return macro_list

    @staticmethod
    def load_parse_world(world_location: str, world_id: int) -> dict[str, Area]:
        with open(world_location) as world_loc:
            area_file = json.load(world_loc)
            area_list = list(map((lambda create: Area.with_world_id(create, world_id)), area_file["Areas"]))
            return {area.name : area for area in area_list}


    def _set_dungeon_non_progressive(self, dungeon_name: str) -> None:
        location_entries = list()
        for location in self.location_entries:
            if dungeon_name in location.name:
                location.logical = False
            location_entries.append(location)
        self.location_entries = location_entries


    def _location_category_list(self) -> list[str]:
        return [key for key, val in self.world_settings.progressive_categories.items()
                if val == True] + ["DefeatGanondorf"]


    @staticmethod
    def location_category_cache(progressive_categories: list[str], categories: set[str]) -> bool:
        return all([location_cat in progressive_categories for location_cat in categories])

    def _replace_macro_item(self, macro_name: str, new_requirement: Requirement):
        macro = self.macros[macro_name]
        macro.expression = new_requirement
        self.macros[macro_name] = macro