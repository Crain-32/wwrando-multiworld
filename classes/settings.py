from dataclasses import dataclass, field

from data.extras import item_id_to_name_dict, capital_case_with_space

SWORDLESS = 0
START_WITH_SWORD = 1
NO_STARTING_SWORD = 2

@dataclass
class Settings:

    starting_gear: list[int] = field(default_factory=list)
    progressive_categories: dict[str, bool] = field(default_factory=dict)
    keylunacy: bool = False
    randomize_charts: bool = False
    race_mode: bool = True
    num_race_mode_dungeons: int = 3
    swordless: bool = False
    skip_rematch_bosses: bool = True
    sword_mode: int = START_WITH_SWORD
    starting_pohs: int = 0
    starting_hcs: int = 3

    def __post_init__(self):
        self.progressive_categories = {
        "Dungeon": True,
        "PuzzleSecretCave": True,
        "CombatSecretCave": True,
        "Mail": True,
        "GreatFairy": True,
        "ShortSidequest": True,
        "LongSidequest": True,
        "SpoilsTrading": True,
        "Minigame": True,
        "FreeGift": True,
        "Raft": True,
        "Submarine": True,
        "EyeReefChests": True,
        "BigOcto": True,
        "Gunboat": True,
        "SunkenTreasure": True,
        "TriforceChart": True,
        "TreasureChart": True,
        "ExpensivePurchase": True,
        "Misc": True,
        "TingleChest": True,
        "Battlesquid": True,
        "SavageLabyrinth": True,
        "IslandPuzzle": True,
        "Obscure": True,
        "SkipRefights": True,
        "Platform": True,
        "NoSword": False
    }

    def spoiler_representation(self, world_id: int) -> str:
        output = f"--- World {world_id} Settings ---\n"
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