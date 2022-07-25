import re
from collections import OrderedDict
from dataclasses import asdict
import json
from typing import AnyStr, List, Any, Dict, Generator

# Replaces the WorldLoadingError Enum Struct in World.hpp

NONE = "NONE"
DUPLICATE_MACRO_NAME = "DUPLICATE_MACRO_NAME"
MACRO_DOES_NOT_EXIST = "MACRO_DOES_NOT_EXIST"
REQUIREMENT_TYPE_DOES_NOT_EXIST = "REQUIREMENT_TYPE_DOES_NOT_EXIST"
MAPPING_MISMATCH = "MAPPING_MISMATCH"
GAME_ITEM_DOES_NOT_EXIST = "GAME_ITEM_DOES_NOT_EXIST"
AREA_DOES_NOT_EXIST = "AREA_DOES_NOT_EXIST"
LOCATION_DOES_NOT_EXIST = "LOCATION_DOES_NOT_EXIST"
EXIT_MISSING_KEY = "EXIT_MISSING_KEY"
OPTION_DOES_NOT_EXIST = "OPTION_DOES_NOT_EXIST"
INCORRECT_ARG_COUNT = "INCORRECT_ARG_COUNT"
EXPECTED_JSON_OBJECT = "EXPECTED_JSON_OBJECT"
AREA_MISSING_KEY = "AREA_MISSING_KEY"
LOCATION_MISSING_KEY = "LOCATION_MISSING_KEY"
MACRO_MISSING_KEY = "MACRO_MISSING_KEY"
REQUIREMENT_MISSING_KEY = "REQUIREMENT_MISSING_KEY"
INVALID_LOCATION_CATEGORY = "INVALID_LOCATION_CATEGORY"
INVALID_MODIFICATION_TYPE = "INVALID_MODIFICATION_TYPE"
INVALID_OFFSET_VALUE = "INVALID_OFFSET_VALUE"
INVALID_GAME_ITEM = "INVALID_GAME_ITEM"

# Replaces the RequirementType Enum in Requirement.hpp
REQUIREMENT_OR = "OR"
REQUIREMENT_AND = "AND"
REQUIREMENT_NOT = "NOT"
REQUIREMENT_HAS_ITEM = "HAS_ITEM"
REQUIREMENT_COUNT = "COUNT"
REQUIREMENT_CAN_ACCESS = "CAN_ACCESS"
REQUIREMENT_SETTING = "SETTING"
REQUIREMENT_MACRO = "MACRO"
REQUIREMENT_NONE = "NONE"

REQUIREMENT_TYPES = [
    REQUIREMENT_OR,
    REQUIREMENT_AND,
    REQUIREMENT_NOT,
    REQUIREMENT_HAS_ITEM,
    REQUIREMENT_COUNT,
    REQUIREMENT_CAN_ACCESS,
    REQUIREMENT_SETTING,
    REQUIREMENT_MACRO,
    REQUIREMENT_NONE
]

# Replaces the SearchMode Enum in Search.hpp
SEARCH_INVALID = "INVALID"
SEARCH_ACCESSIBLE_LOCATIONS = "AccessibleLocations"
SEARCH_GAME_BEATABLE = "GameBeatable"
SEARCH_ALL_LOCATIONS_REACHABLE = "AllLocationsReachable"
SEARCH_GENERATE_PLAYTHROUGH = "GeneratePlaythrough"

LOCATION_CATEGORY_MISC = "Misc"
LOCATION_CATEGORY_DUNGEON = "Dungeon"
LOCATION_CATEGORY_GREAT_FAIRY = "GreatFairy"
LOCATION_CATEGORY_ISLAND_PUZZLE = "IslandPuzzle"
LOCATION_CATEGORY_SPOILS_TRADING = "SpoilsTrading"
LOCATION_CATEGORY_MAIL = "Mail"
LOCATION_CATEGORY_SAVAGE_LABYRINTH = "SavageLabyrinth"
LOCATION_CATEGORY_FREE_GIFT = "FreeGift"
LOCATION_CATEGORY_MINIGAME = "Minigame"
LOCATION_CATEGORY_BATTLE_SQUID = "BattleSquid"
LOCATION_CATEGORY_TINGLE_CHEST = "TingleChest"
LOCATION_CATEGORY_PUZZLE_SECRET_CAVES = "PuzzleSecretCaves"
LOCATION_CATEGORY_COMBAT_SECRET_CAVES = "CombatSecretCaves"
LOCATION_CATEGORY_PLATFORM = "Platform"
LOCATION_CATEGORY_RAFT = "Raft"
LOCATION_CATEGORY_EYE_REEF_CHESTS = "EyeReefChests"
LOCATION_CATEGORY_BIG_OCTO = "BigOcto"
LOCATION_CATEGORY_SUBMARINE = "Submarine"
LOCATION_CATEGORY_GUNBOAT = "Gunboat"
LOCATION_CATEGORY_LONG_SIDE_QUEST = "LongsideQuest"
LOCATION_CATEGORY_SHORT_SIDE_QUESTION = "ShortsideQuest"
LOCATION_CATEGORY_EXPENSIVE_PURCHASES = "ExpensivePurchases"
LOCATION_CATEGORY_SUNKEN_TREASURE = "SunkenTreasure"
LOCATION_CATEGORY_OBSCURE = "Obscure"
LOCATION_CATEGORY_JUNK = "Junk"
LOCATION_CATEGORY_OTHER = "Other"

#Replaces the GameItem map in GameItem.cpp
item_id_dict = {
    "Heart(Pickup)": 0x00,
    "GreenRupee": 0x01,
    "BlueRupee": 0x02,
    "YellowRupee": 0x03,
    "RedRupee": 0x04,
    "PurpleRupee": 0x05,
    "OrangeRupee": 0x06,
    "PieceOfHeart": 0x07,
    "HeartContainer": 0x08,
    "SmallMagicJar(Pickup)": 0x09,
    "LargeMagicJar(Pickup)": 0x0A,
    "5Bombs(Pickup)": 0x0B,
    "10Bombs(Pickup)": 0x0C,
    "20Bombs(Pickup)": 0x0D,
    "30Bombs(Pickup)": 0x0E,
    "SilverRupee": 0x0F,
    "10Arrows(Pickup)": 0x10,
    "20Arrows(Pickup)": 0x11,
    "30Arrows(Pickup)": 0x12,
    "DRCSmallKey": 0x13,
    "DRCBigKey": 0x14,
    "SmallKey": 0x15,
    "Fairy(Pickup)": 0x16,
    "YellowRupee(Joke Message)": 0x1A,
    "DRCDungeonMap": 0x1B,
    "DRCDungeonCompass": 0x1C,
    "FWSmallKey": 0x1D,
    "ThreeHearts(Pickup)": 0x1E,
    "JoyPendant": 0x1F,
    "Telescope": 0x20,
    "TingleTuner": 0x21,
    "WindWaker": 0x22,
    "ProgressivePictoBox": 0x23,
    "SpoilsBag": 0x24,
    "GrapplingHook": 0x25,
    "DeluxePictoBox": 0x26,
    "ProgressiveBow": 0x27,
    "PowerBracelets": 0x28,
    "IronBoots": 0x29,
    "MagicArmor": 0x2A,
    "BaitBag": 0x2C,
    "Boomerang": 0x2D,
    "Hookshot": 0x2F,
    "DeliveryBag": 0x30,
    "Bombs": 0x31,
    "Hero'sClothes": 0x32,
    "SkullHammer": 0x33,
    "DekuLeaf": 0x34,
    "FireandIceArrows": 0x35,
    "LightArrow": 0x36,
    "Hero'sNewClothes": 0x37,
    "ProgressiveSword": 0x38,
    "MasterSword(Powerless)": 0x39,
    "MasterSword(Half Power)": 0x3A,
    "ProgressiveShield": 0x3B,
    "MirrorShield": 0x3C,
    "RecoveredHero'sSword": 0x3D,
    "MasterSword(Full Power)": 0x3E,
    "PieceofHeart(Alternate Message)": 0x3F,
    "FWBigKey": 0x40,
    "FWDungeonMap": 0x41,
    "Pirate'sCharm": 0x42,
    "Hero'sCharm": 0x43,
    "SkullNecklace": 0x45,
    "BokoBabaSeed": 0x46,
    "GoldenFeather": 0x47,
    "Knight'sCrest": 0x48,
    "RedChuJelly": 0x49,
    "GreenChuJelly": 0x4A,
    "BlueChuJelly": 0x4B,
    "DungeonMap": 0x4C,
    "Compass": 0x4D,
    "BigKey": 0x4E,
    "EmptyBottle": 0x50,
    "RedPotion": 0x51,
    "GreenPotion": 0x52,
    "BluePotion": 0x53,
    "ElixirSoup(1/2)": 0x54,
    "ElixirSoup": 0x55,
    "BottledWater": 0x56,
    "FairyinBottle": 0x57,
    "ForestFirefly": 0x58,
    "ForestWater": 0x59,
    "FWDungeonCompass": 0x5A,
    "TotGSmallKey": 0x5B,
    "TotGBigKey": 0x5C,
    "TotGDungeonMap": 0x5D,
    "TotGDungeonCompass": 0x5E,
    "FFDungeonMap": 0x5F,
    "FFDungeonCompass": 0x60,
    "TriforceShard1": 0x61,
    "TriforceShard2": 0x62,
    "TriforceShard3": 0x63,
    "TriforceShard4": 0x64,
    "TriforceShard5": 0x65,
    "TriforceShard6": 0x66,
    "TriforceShard7": 0x67,
    "TriforceShard8": 0x68,
    "NayrusPearl": 0x69,
    "DinsPearl": 0x6A,
    "FaroresPearl": 0x6B,
    "WindsRequiem": 0x6D,
    "BalladOfGales": 0x6E,
    "CommandMelody": 0x6F,
    "EarthGodsLyric": 0x70,
    "WindGodsAria": 0x71,
    "SongOfPassing": 0x72,
    "ETSmallKey": 0x73,
    "ETBigKey": 0x74,
    "ETDungeonMap": 0x75,
    "ETDungeonCompass": 0x76,
    "WTSmallKey": 0x77,
    "BoatsSail": 0x78,
    "Triforce Chart 1 got deciphered": 0x79,
    "Triforce Chart 2 got deciphered": 0x7A,
    "Triforce Chart 3 got deciphered": 0x7B,
    "Triforce Chart 4 got deciphered": 0x7C,
    "Triforce Chart 5 got deciphered": 0x7D,
    "Triforce Chart 6 got deciphered": 0x7E,
    "Triforce Chart 7 got deciphered": 0x7F,
    "Triforce Chart 8 got deciphered": 0x80,
    "WTBigKey": 0x81,
    "All-PurposeBait": 0x82,
    "HyoiPear": 0x83,
    "WTDungeonMap": 0x84,
    "WTDungeonCompass": 0x85,
    "TownFlower": 0x8C,
    "SeaFlower": 0x8D,
    "ExoticFlower": 0x8E,
    "Hero'sFlag": 0x8F,
    "BigCatchFlag": 0x90,
    "BigSaleFlag": 0x91,
    "Pinwheel": 0x92,
    "SickleMoonFlag": 0x93,
    "SkullTowerIdol": 0x94,
    "FountainIdol": 0x95,
    "PostmanStatue": 0x96,
    "ShopGuruStatue": 0x97,
    "Father'sLetter": 0x98,
    "NoteToMom": 0x99,
    "MaggiesLetter": 0x9A,
    "MoblinsLetter": 0x9B,
    "CabanaDeed": 0x9C,
    "ComplimentaryID": 0x9D,
    "Fill-UpCoupon": 0x9E,
    "LegendaryPictograph": 0x9F,
    "DragonTingleStatue": 0xA3,
    "ForbiddenTingleStatue": 0XA4,
    "GoddessTingleStatue": 0XA5,
    "EarthTingleStatue": 0XA6,
    "WindTingleStatue": 0XA7,
    "HurricaneSpin": 0XAA,
    "ProgressiveWallet": 0XAB,
    "5000RupeeWallet": 0XAC,
    "ProgressiveBombBag": 0XAD,
    "99BombBombBag": 0XAE,
    "ProgressiveQuiver": 0XAF,
    "99ArrowQuiver": 0XB0,
    "Nothing": 0XB1,  # THIS REPLACES GameItem::NOTHING
    "MagicMeterUpgrade": 0XB2,
    "50 Rupees, reward for finding 1 Tingle Statue": 0XB3,
    "100 Rupees, reward for finding 2 Tingle Statues": 0XB4,
    "150 Rupees, reward for finding 3 Tingle Statues": 0XB5,
    "200 Rupees, reward for finding 4 Tingle Statues": 0XB6,
    "250 Rupees, reward for finding 5 Tingle Statues": 0XB7,
    "500 Rupees, reward for finding all Tingle Statues": 0XB8,
    "SubmarineChart": 0XC2,
    "Beedle'sChart": 0XC3,
    "PlatformChart": 0XC4,
    "LightRingChart": 0XC5,
    "SecretCaveChart": 0XC6,
    "SeaHeartsChart": 0XC7,
    "IslandHeartsChart": 0XC8,
    "GreatFairyChart": 0XC9,
    "OctoChart": 0XCA,
    "IN-credibleChart": 0XCB,
    "TreasureChart7": 0XCC,
    "TreasureChart27": 0XCD,
    "TreasureChart21": 0XCE,
    "TreasureChart13": 0XCF,
    "TreasureChart32": 0XD0,
    "TreasureChart19": 0XD1,
    "TreasureChart41": 0XD2,
    "TreasureChart26": 0XD3,
    "TreasureChart8": 0XD4,
    "TreasureChart37": 0XD5,
    "TreasureChart25": 0XD6,
    "TreasureChart17": 0XD7,
    "TreasureChart36": 0XD8,
    "TreasureChart22": 0XD9,
    "TreasureChart9": 0XDA,
    "GhostShipChart": 0XDB,
    "Tingle'sChart": 0XDC,
    "TreasureChart14": 0XDD,
    "TreasureChart10": 0XDE,
    "TreasureChart40": 0XDF,
    "TreasureChart3": 0XE0,
    "TreasureChart4": 0XE1,
    "TreasureChart28": 0XE2,
    "TreasureChart16": 0XE3,
    "TreasureChart18": 0XE4,
    "TreasureChart34": 0XE5,
    "TreasureChart29": 0XE6,
    "TreasureChart1": 0XE7,
    "TreasureChart35": 0XE8,
    "TreasureChart12": 0XE9,
    "TreasureChart6": 0XEA,
    "TreasureChart24": 0XEB,
    "TreasureChart39": 0XEC,
    "TreasureChart38": 0XED,
    "TreasureChart2": 0XEE,
    "TreasureChart33": 0XEF,
    "TreasureChart31": 0XF0,
    "TreasureChart23": 0XF1,
    "TreasureChart5": 0XF2,
    "TreasureChart20": 0XF3,
    "TreasureChart30": 0XF4,
    "TreasureChart15": 0XF5,
    "TreasureChart11": 0XF6,
    "TriforceChart8": 0XF7,
    "TriforceChart7": 0XF8,
    "TriforceChart6": 0XF9,
    "TriforceChart5": 0XFA,
    "TriforceChart4": 0XFB,
    "TriforceChart3": 0XFC,
    "TriforceChart2": 0XFD,
    "TriforceChart1": 0XFE,
    "GameBeatable": 0xFF
}

item_id_to_name_dict = {val: key for key, val in item_id_dict.items()}


DUNGEON_NAMES = [
    "DragonRoostCavern",
    "ForbiddenWoods",
    "TowerOfTheGods",
    "ForsakenFortress",
    "EarthTemple",
    "WindTemple",
]
DUNGEON_NAME_DICT = OrderedDict([
    ("DRC", "Dragon Roost Cavern"),
    ("FW", "Forbidden Woods"),
    ("TotG", "Tower of the Gods"),
    ("FF", "Forsaken Fortress"),
    ("ET", "Earth Temple"),
    ("WT", "Wind Temple"),
])

chart_macro_to_island = {
    "Chart for Island 1": "Forsaken Fortress Sunken Treasure",
    "Chart for Island 2": "Star Island Sunken Treasure",
    "Chart for Island 3": "Northern Fairy Sunken Treasure",
    "Chart for Island 4": "Gale Isle Sunken Treasure",
    "Chart for Island 5": "Crescent Moon Sunken Treasure",
    "Chart for Island 6": "Seven Star Sunken Treasure",
    "Chart for Island 7": "Overlook Sunken Treasure",
    "Chart for Island 8": "Four Eye Reef Sunken Treasure",
    "Chart for Island 9": "Mother And Child Sunken Treasure",
    "Chart for Island 10": "Spectacle Sunken Treasure",
    "Chart for Island 11": "Windfall Sunken Treasure",
    "Chart for Island 12": "Pawprint Sunken Treasure",
    "Chart for Island 13": "Dragoon Roost Island Sunken Treasure",
    "Chart for Island 14": "Flight Control Sunken Treasure",
    "Chart for Island 15": "Western Fairy Sunken Treasure",
    "Chart for Island 16": "Rock Spire Sunken Treasure",
    "Chart for Island 17": "Tingle Island Sunken Treasure",
    "Chart for Island 18": "Northern Triangle Sunken Treasure",
    "Chart for Island 19": "Eastern Fairy Sunken Treasure",
    "Chart for Island 20": "Fire Mountain Sunken Treasure",
    "Chart for Island 21": "Star Belt Archipelago Sunken Treasure",
    "Chart for Island 22": "Three Eye Reef Sunken Treasure",
    "Chart for Island 23": "Greatfish Sunken Treasure",
    "Chart for Island 24": "Cyclops Reef Sunken Treasure",
    "Chart for Island 25": "Six Eye Reef Sunken Treasure",
    "Chart for Island 26": "Tower Of The Gods Sunken Treasure",
    "Chart for Island 27": "Eastern Triangle Sunken Treasure",
    "Chart for Island 28": "Thorned Fairy Sunken Treasure",
    "Chart for Island 29": "Needle Rock Sunken Treasure",
    "Chart for Island 30": "Islet Of Steel Sunken Treasure",
    "Chart for Island 31": "Stone Watcher Sunken Treasure",
    "Chart for Island 32": "Southern Triangle Sunken Treasure",
    "Chart for Island 33": "Private Oasis Sunken Treasure",
    "Chart for Island 34": "Bomb Island Sunken Treasure",
    "Chart for Island 35": "Birds Peak Sunken Treasure",
    "Chart for Island 36": "Diamond Steppe Sunken Treasure",
    "Chart for Island 37": "Five Eye Reef Sunken Treasure",
    "Chart for Island 38": "Shark Island Sunken Treasure",
    "Chart for Island 39": "Southern Fairy Sunken Treasure",
    "Chart for Island 40": "Ice Ring Sunken Treasure",
    "Chart for Island 41": "Forest Haven Sunken Treasure",
    "Chart for Island 42": "Cliff Plateau Sunken Treasure",
    "Chart for Island 43": "Horseshoe Sunken Treasure",
    "Chart for Island 44": "Outset Sunken Treasure",
    "Chart for Island 45": "Headstone Sunken Treasure",
    "Chart for Island 46": "Two Eye Reef Sunken Treasure",
    "Chart for Island 47": "Angular Sunken Treasure",
    "Chart for Island 48": "Boating Course Sunken Treasure",
    "Chart for Island 49": "Five Star Sunken Treasure"
}


def parse_macro_requirement_list(macros, *requirement) -> List[int]:
    output: List[int] = list()
    for req in requirement:
        if req.type == REQUIREMENT_HAS_ITEM:
            if isinstance(req.args[0], str):
                output.append(item_id_dict[req.args[0]])
            else:
                output.append(req.args[0])
        elif req.type == REQUIREMENT_COUNT:
            if isinstance(req.args[1], str):
                output.append(item_id_dict[req.args[1]])
            else:
                output.append(req.args[1])
        elif req.type == REQUIREMENT_OR or req.type == REQUIREMENT_AND or req.type == REQUIREMENT_NOT:
            output += parse_macro_requirement_list(macros, *req.args)
        elif req.type == REQUIREMENT_MACRO:
            output += parse_macro_requirement_list(macros, macros[req.args[0]].expression)
    return output

def handle_lists(obj: list):
    result = []
    for thing in obj:
        if isinstance(thing, list):
            result.append(handle_lists(thing))
        else:
            result.append(asdict(thing))
    return result

# def dump_object(obj, filename: str, write_str: bool = False):
#     if isinstance(obj, list):
#         inp = handle_lists(obj)
#     elif write_str:
#         with open("./dump/" + filename + ".txt", 'w') as output:
#             output.write(str(obj))
#         return
#     else:
#         inp = asdict(obj)
#     with open("./dump/" + filename + ".json", 'w') as output:
#         json.dump(inp, output, indent='\t')

def capital_case_with_space(original_str: str) -> str:
    pattern = re.compile("[A-Z]([a-z]*)|([0-9]*)")
    matches = list(map((lambda m: m.group()), pattern.finditer(original_str)))
    if len(matches) > 0:
        return " ".join(matches).strip()
    else:
        return original_str
#
# def dump_simple_items(obj, filename: AnyStr) -> None:
#     output = list()
#     if isinstance(output, list):
#         output = [str(item) for item in obj]
#     else:
#         output.append(str(obj))
#     with open("./dump/" + filename + ".json", 'w') as output_file:
#         output_file.writelines(output)
#
# def dump_simple_world_locations(worlds: List[Any] | Any, output_filename: str) -> None:
#     output = list()
#     if isinstance(worlds, list):
#         for world in worlds:
#             output.extend(simple_loc_parse(world))
#     else:
#         output = simple_loc_parse(worlds)
#     with open("./dump/" + output_filename + ".json", 'w') as output_file:
#         json.dump(output, output_file, indent='\t')
#
# def dump_strings(input_string: AnyStr | List[AnyStr], output_filename: AnyStr) -> None:
#     if not isinstance(input_string, list):
#         input_string = [input_string]
#     input_string = [val + '\n' for val in input_string]
#     with open("./dump/" + output_filename + ".txt", 'w') as output_file:
#         output_file.writelines(input_string)

def simple_loc_parse(world):
    return [location.json_output() for location in world.location_entries]