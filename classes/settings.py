from dataclasses import dataclass, field
from typing import List, Dict, AnyStr, OrderedDict, Any, Union

from logic.extras import item_id_to_name_dict, capital_case_with_space, item_id_dict

SWORDLESS = "Swordless"
START_WITH_SWORD = "Start with Hero's Sword"
NO_STARTING_SWORD = "No Starting Sword"


@dataclass
class Settings:
    starting_gear: List[int] = field(default_factory=list)
    progressive_categories: Dict[AnyStr, bool] = field(default_factory=dict)
    keylunacy: bool = False
    randomize_charts: bool = False
    race_mode: bool = True
    num_race_mode_dungeons: int = 3
    sword_mode: AnyStr = START_WITH_SWORD
    starting_pohs: int = 0
    starting_hcs: int = 3

    def __init__(self, options: OrderedDict[AnyStr, Union[bool, List[int], AnyStr]]):
        self.progressive_categories = {
            "Dungeon": options.get("progression_dungeons"),
            "PuzzleSecretCave": options.get("progression_puzzle_secret_caves"),
            "CombatSecretCave": options.get("progression_combat_secret_caves"),
            "Mail": options.get("progression_mail"),
            "GreatFairy": options.get("progression_great_fairies"),
            "ShortSidequest": options.get("progression_short_sidequests"),
            "LongSidequest": options.get("progression_long_sidequests"),
            "SpoilsTrading": options.get("progression_spoils_trading"),
            "Minigame": options.get("progression_minigames"),
            "FreeGift": options.get("progression_free_gifts"),
            "Raft": options.get("progression_platforms_rafts"),
            "Submarine": options.get("progression_submarines"),
            "EyeReefChests": options.get("progression_eye_reef_chests"),
            "BigOcto": options.get("progression_big_octos_gunboats"),
            "Gunboat": options.get("progression_big_octos_gunboats"),
            "SunkenTreasure": options.get("progression_triforce_charts") | options.get("progression_treasure_charts"),
            "TriforceChart": options.get("progression_triforce_charts"),
            "TreasureChart": options.get("progression_treasure_charts"),
            "ExpensivePurchase": options.get("progression_expensive_purchases"),
            "Misc": options.get("progression_misc"),
            "TingleChest": options.get("progression_tingle_chests"),
            "Battlesquid": options.get("progression_battlesquid"),
            "SavageLabyrinth": options.get("progression_savage_labyrinth"),
            "IslandPuzzle": options.get("progression_island_puzzles"),
            "Obscure": False,
            "SkipRefights": options.get("skip_rematch_bosses"),
            "Platform": options.get("progression_platforms_rafts"),
            "NoSword": (options.get("sword_mode") == NO_STARTING_SWORD)
        }
        self.keylunacy = False # options.get("keylunacy")
        self.race_mode = options.get("race_mode")
        self.num_race_mode_dungeons = int(options.get("num_race_mode_dungeons"))
        self.starting_hcs = int(options.get("starting_hcs"))
        self.starting_pohs = int(options.get("starting_pohs"))
        self.randomize_charts = options.get("randomize_charts")
        self.starting_gear = list(map((lambda prog_str_item_id: item_id_dict[prog_str_item_id.replace(" ", "")]),
                                      options.get("starting_gear")))
        starting_shards = int(options.get("num_starting_triforce_shards"))
        if starting_shards > 0:
            self.starting_gear.extend(
                list(
                    map((lambda shard: shard + item_id_dict["TriforceShard1"]),
                        range(starting_shards))
                )
            )
        self.multiworld = options.get("multiplayer") == "Multiworld"
        self.sword_mode = options.get("sword_mode")

    def spoiler_representation(self, world_id: int) -> AnyStr:
        output = f"--- World {world_id + 1} Settings ---\n"
        for key, val in self.progressive_categories.items():
            if key == "NoSword":
                continue
            if val:
                output += f"{capital_case_with_space(key)}\n"
        if self.sword_mode == SWORDLESS:
            output += "Swordless\n"
        elif self.sword_mode == START_WITH_SWORD:
            output += "Start with Sword\n"
        elif self.sword_mode == NO_STARTING_SWORD:
            output += "No Starting Sword\n"

        if len(self.starting_gear) > 0:
            output += "\nStarting Items:\n"
            for item in self.starting_gear:
                output += f"{item_id_to_name_dict[item]}\n"
        return output + "\n"
