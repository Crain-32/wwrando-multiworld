"""
This should take the input settings and filter the input items as needed.
Not the biggest fan of Gym's implementation, might combine his with lago's
"""
import itertools

from classes.settings import Settings, START_WITH_SWORD, SWORDLESS

base_item_pool = [
  0x21, # Tingle Tuner
  0x22, # Wind Waker
  0x24, # Spoils Bag
  0x25, # Grappling Hook
  0x28, # Power Bracelets
  0x29, # Iron Boots
  0x2C, # Bait Bag
  0x2D, # Boomerang
  0x2F, # Hookshot
  0x30, # Delivery Bag
  0x31, # Bombs
  0x33, # Skull Hammer
  0x34, # Deku Leaf

  0x61, # Triforce Shard 1
  0x62, # Triforce Shard 2
  0x63, # Triforce Shard 3
  0x64, # Triforce Shard 4
  0x65, # Triforce Shard 5
  0x66, # Triforce Shard 6
  0x67, # Triforce Shard 7
  0x68, # Triforce Shard 8

  0x69, # Nayru's Pearl
  0x6A, # Din's Pearl
  0x6B, # Farore's Pearl

  0x6D, # Wind's Requiem
  0x6E, # Ballad of Gales
  0x6F, # Command Melody
  0x70, # Earth God's Lyric
  0x71, # Wind God's Aria
  0x72, # Song of Passing

  0x78, # Boat's Sail

  0x99, # Note to Mom
  0x9A, # Maggie's Letter
  0x9B, # Moblin's Letter
  0x9C, # Cabana Deed

  0xA3, # Dragon Tingle Statue
  0xA4, # Forbidden Tingle Statue
  0xA5, # Goddess Tingle Statue
  0xA6, # Earth Tingle Statue
  0xA7, # Wind Tingle Statue

  0xAD, # Progressive Bomb Bag
  0xAD, # Progressive Bomb Bag
  0xAF, # Progressive Quiver
  0xAF, # Progressive Quiver
  0xB2, # Magic Meter Upgrade

  0xDB  # Ghost Ship Chart
] + \
  [
    0x3B, # Progressive Shield
    0x3B  # Progressive Shield
  ] + \
  [
    0x27, # Progressive Bow
    0x27, # Progressive Bow
    0x27  # Progressive Bow
  ] + \
  [
    0xAB, # Progressive Wallet
    0xAB  # Progressive Wallet
  ] + \
  [
    0x23, # Picto Box
    0x23  # Deluxe Picto Box
  ] + \
  [ 0x50 ] * 4  # 4 Empty Bottles

dungeons = {
  "DragonRoostCavernKeys": [
    0x14, # Big Key
  ] + [0x13] * 4,  # Small Keys
  "DragonRoostCavernExtras": [
    0x1B, # Map
    0x1C  # Compass
  ],
  "ForbiddenWoodsKeys": [
    0x40, # Big Key
    0x1D  # Small Keys
  ],
  "ForbiddenWoodsExtras": [
    0x41, # Map
    0x5A # Compass
  ],
  "TowerOfTheGodsKeys": [
    0x5C, # Big Key
  ] + [0x5B] * 2, # Small Keys
  "TowerOfTheGodsExtras": [
    0x5D, # Map
    0x5E  # Compass
  ],
  "ForsakenFortressKeys": [
  ],
  "ForsakenFortressExtras": [
    0x5F, # Map
    0x60  # Compass
  ],
  "EarthTempleKeys": [
    0x74, # Big Key
  ] + [0x73] * 3, # Small Keys
  "EarthTempleExtras": [
    0x75, # Map
    0x76  # Compass
  ],
  "WindTempleKeys": [
    0x81, # Big Key
  ] + [0x77] * 2, # Small Keys
  "WindTempleExtras": [
    0x84, # Map
    0x85  # Compass
  ]
}
dungeon_key_item_values = set(itertools.chain(*dungeons.values()))

swords = [
  0x38,
  0x38,
  0x38,
  0x38
]
normal_starting_items = [
  0x22, # Wind Waker
  0x6D, # Wind's Requiem
  0x3B, # Hero's Shield
  0x72, # Song of Passing
  0x6E, # Ballad of Gales
  0x78  # Boat's Sail
]

charts = [
  0XC2, # SubmarineChart
  0XC3, # BeedlesChart
  0XC4, # PlatformChart
  0XC5, # LightRingChart
  0XC6, # SecretCaveChart
  0XC7, # SeaHeartsChart
  0XC8, # IslandHeartsChart
  0XC9, # GreatFairyChart
  0XCA, # OctoChart
  0XCB, # INcredibleChart
  0XCC, # TreasureChart7
  0XCD, # TreasureChart27
  0XCE, # TreasureChart21
  0XCF, # TreasureChart13
  0XD0, # TreasureChart32
  0XD1, # TreasureChart19
  0XD2, # TreasureChart41
  0XD3, # TreasureChart26
  0XD4, # TreasureChart8
  0XD5, # TreasureChart37
  0XD6, # TreasureChart25
  0XD7, # TreasureChart17
  0XD8, # TreasureChart36
  0XD9, # TreasureChart22
  0XDA, # TreasureChart9
  # GhostShipChart Is in Base Item Pool
  0XDC, # TinglesChart
  0XDD, # TreasureChart14
  0XDE, # TreasureChart10
  0XDF, # TreasureChart40
  0XE0, # TreasureChart3
  0XE1, # TreasureChart4
  0XE2, # TreasureChart28
  0XE3, # TreasureChart16
  0XE4, # TreasureChart18
  0XE5, # TreasureChart34
  0XE6, # TreasureChart29
  0XE7, # TreasureChart1
  0XE8, # TreasureChart35
  0XE9, # TreasureChart12
  0XEA, # TreasureChart6
  0XEB, # TreasureChart24
  0XEC, # TreasureChart39
  0XED, # TreasureChart38
  0XEE, # TreasureChart2
  0XEF, # TreasureChart33
  0XF0, # TreasureChart31
  0XF1, # TreasureChart23
  0XF2, # TreasureChart5
  0XF3, # TreasureChart20
  0XF4, # TreasureChart30
  0XF5, # TreasureChart15
  0XF6, # TreasureChart11
  0XF7, # TriforceChart8
  0XF8, # TriforceChart7
  0XF9, # TriforceChart6
  0XFA, # TriforceChart5
  0XFB, # TriforceChart4
  0XFC, # TriforceChart3
  0XFD, # TriforceChart2
  0XFE # TriforceChart1
]
def generate_game_item_pool(settings: Settings, starting_items: list[int]) -> list[int]:
    item_pool = base_item_pool.copy()
    item_pool.extend(list(itertools.chain.from_iterable(dungeons.values())))
    if settings.sword_mode != SWORDLESS:
      item_pool += swords

    item_pool += [0x08] * (3 - settings.starting_hcs)
    item_pool += [0x07] * (44 - settings.starting_pohs)
    item_pool.extend(charts)
    item_pool = remove_starting_items(item_pool, starting_items)
    return item_pool

def generate_starting_items(settings: Settings) -> list[int]:
    starting_items = normal_starting_items.copy()
    if settings.sword_mode == START_WITH_SWORD:
      starting_items += [0x38] # Hero's Sword

    starting_items += settings.starting_gear
    return starting_items

def remove_starting_items(base_pool: list[int], starting_items: list[int]) -> list[int]:
    removed_starting_items = list()
    incomplete = True
    while incomplete:
      incomplete = False
      for item in base_pool:
        if item in starting_items:
          incomplete = True
          removed_starting_items.append(item)
          starting_items.remove(item)
          base_pool.remove(item)
      if len(starting_items) == 0:
        incomplete = False
    starting_items.extend(removed_starting_items)
    return base_pool