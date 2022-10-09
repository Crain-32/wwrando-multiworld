import itertools
from random import Random

from classes.gameitem import *
from classes.location import Location
from classes.world import World
from logic.extras import *
from logic.search import game_beatable, get_accessible_locations


def fill(worlds: List[World], random_state: Random):
    worlds = place_hardcoded_items(worlds)

    worlds = determine_major_items(worlds)
    worlds = place_race_mode_items(worlds, random_state)

    # Dungeon Items are not consistent, getting dumped after this function
    print(random_state.getstate())
    worlds = handle_dungeon_items(worlds, random_state)
    item_pool = get_item_pool(worlds)
    locations = get_location_pool(worlds)

    major_items = [item for item in item_pool
                   if item.major_item]
    for item in major_items:
        worlds[item.world_id].item_pool.remove(item)
    logical_locations = list(filter((lambda loc: loc.is_logical_location()), locations))  # Filter out Logical Locations

    if len(major_items) > len(logical_locations):
        print(f"Major Items amount: {len(major_items)}")
        print(f"Logical Locations: {len(logical_locations)}")
        print(f"Please Enable more Spots for Major Items")
        raise RuntimeWarning("Invalid amount of Items")

    worlds = assumed_fill(worlds, major_items, logical_locations, random_state)
    # remaining_logic_items = [list comprehension]

    # I can't remember why the assumed fill is twice yet, so I've removed it till the first one is stable
    # worlds = assumed_fill(worlds, major_items, item_pool, logical_locations, random_state)
    if not game_beatable(worlds):
        raise RuntimeWarning(f"The Game is not Beatable!")

    return worlds


def place_hardcoded_items(worlds) -> List[World]:
    for world in worlds:
        world.set_location("DefeatGanondorf", item_id_dict["GameBeatable"], world.world_id)
    return worlds


def determine_major_items(worlds: List[World]) -> List[World]:
    item_pool: List[GameItem] = get_item_pool(worlds)

    world_logical_item_ids: List[List[int]] = [world.required_items() for world in worlds]
    parsed_items: List[GameItem] = []
    for item in item_pool:
        if not item.junk_item and item.game_item_id in world_logical_item_ids[item.world_id]:
            item.major_item = True
        parsed_items.append(item)
    replaced_worlds = []
    for world_id in range(len(worlds)):
        world_items = list(filter((lambda by_id: by_id.world_id == world_id), parsed_items))
        world = worlds[world_id]
        world.item_pool = world_items
        replaced_worlds.append(world)
    return replaced_worlds


def generate_race_mode_items(race_mode_locations: List[Location], race_mode_items: List[GameItem],
                             selectable_items: List[GameItem], random_state: Random) -> List[GameItem]:
    random_state.shuffle(selectable_items)
    while len(selectable_items) != 0 and len(race_mode_items) < len(race_mode_locations):
        next_race_mode_item = random_state.choice(selectable_items)
        race_mode_items.append(next_race_mode_item)
        selectable_items.remove(next_race_mode_item)

    return race_mode_items


def place_race_mode_items(worlds: List[World], random_state: Random) -> List[World]:
    item_pool = get_item_pool(worlds)

    race_mode_locations = [boss for world in worlds for boss in world.get_race_mode_bosses()]

    triforce_shards = list(filter(is_triforce_shard, item_pool))
    race_mode_items = generate_race_mode_items(race_mode_locations, [], triforce_shards, random_state)

    if len(race_mode_items) < len(race_mode_locations):
        swords = list(filter(is_sword, item_pool))
        race_mode_items = generate_race_mode_items(race_mode_locations, race_mode_items, swords, random_state)

    if len(race_mode_items) < len(race_mode_locations):
        bows = list(filter(is_bow, item_pool))
        race_mode_items = generate_race_mode_items(race_mode_locations, race_mode_items, bows, random_state)

    if len(race_mode_items) < len(race_mode_locations):
        major_items = [item for item in item_pool if item.major_item]
        race_mode_items = generate_race_mode_items(race_mode_locations, race_mode_items, major_items, random_state)

    for item in race_mode_items:
        worlds[item.world_id].item_pool.remove(item)
    return assumed_fill(worlds, race_mode_items, race_mode_locations, random_state)


def handle_dungeon_items(worlds: List[World], random_state: Random) -> List[World]:
    for world in worlds:
        for dungeon_name in DUNGEON_NAMES:
            if not world.world_settings.keylunacy:
                dungeon_locations = [location for location in world.get_specific_dungeon_locations(dungeon_name)]

                logical_locations = list(filter((lambda loc: loc.current_item.game_item_id == item_id_dict["Nothing"] and loc.is_logical_location()),
                                                dungeon_locations))

                dungeon_keys = [keys for keys in world.get_dungeon_keys(dungeon_name)]
                if len(logical_locations) == 0 or len(dungeon_locations) <= len(dungeon_keys):
                    logical_locations = dungeon_locations

                worlds = assumed_fill(worlds, dungeon_keys, logical_locations, random_state, world.world_id)

                dungeon_extras = world.get_dungeon_extras(dungeon_name)
                total_dungeon_locations = world.get_specific_dungeon_locations(dungeon_name)
                unplaced_location = list(filter((lambda loc: loc.current_item.game_item_id == item_id_dict["Nothing"]),
                                                total_dungeon_locations))
                fast_fill(unplaced_location, dungeon_extras, random_state)
    return worlds


"""
    We deviate a bit from the original Assumed fill in that we don't pass in the "itemsNotPlaced" here. This is because
    in the `while len(logical_items) > 0:` loop we add in the world's item_pool. This is treated as our unplaced Items.

    Note: Starting Items are not included since those are handled in the Search Function
"""


def assumed_fill(worlds: List[World], logical_items: List[GameItem], logical_locations: List[Location],
                 random_state: Random, world_id=-1) -> List[World]:
    if len(logical_items) > len(logical_locations):
        raise RuntimeWarning(f"Tried to place {len(logical_items)} items for {len(logical_locations)} locations!")

    if world_id >= len(worlds):
        raise RuntimeWarning(f"Tried to select world id {world_id} with only {len(worlds)} worlds!")

    retries = 5
    unsuccessfulPlacement = True
    while unsuccessfulPlacement:
        if retries == 0:
            print(
                f"Ran out of Retries, attempting to forward fill {len(logical_locations)} locations with {len(logical_items)} items")
            worlds = forward_fill_until_more_free_space(worlds, logical_items, logical_locations, random_state)
            retries = 5
            continue
        retries -= 1
        unsuccessfulPlacement = False
        random_state.shuffle(logical_items)
        rollbacks: List[AnyStr] = []
        while len(logical_items) > 0:
            item_pool = get_item_pool(worlds)
            next_item = logical_items.pop()
            items_not_placed = logical_items.copy()
            items_not_placed.extend(item_pool.copy())  # Note, we already remove logical items
            # from the world's item pool before this function.

            accessible_locations = get_accessible_locations(worlds, items_not_placed, logical_locations, world_id)
            # The above is likely linked to the current issues because it finds the accessible locations and
            # updates them. However, testing hasn't proven this.

            if len(accessible_locations) == 0:
                print(f"No Accessible Locations to place {next_item}. Remaining Attempts this cycle: {retries}")
                # Current broken seeds don't seem to  call this, so I'm worried yet.
                for location in logical_locations:
                    worlds[location.world_id].area_entries[location.area_name].locations.remove(location)
                    if location.current_item.game_item_id != item_id_dict["Nothing"]:
                        logical_items.append(location.current_item)
                    location.current_item = GameItem(game_item_id=item_id_dict["Nothing"], world_id=location.world_id)
                    worlds[location.world_id].area_entries[location.area_name].locations.append(location)
                logical_items.append(next_item)
                rollbacks.clear()
                unsuccessfulPlacement = True
                break

            if next_item.chart_for_sunken_treasure:
                # Calculate Sunken Treasure Locations from the Logical_Locations, check if those all are the locations left.
                # If it is, then put them back in. This doesn't impact logic/access, so waiting for those to be stable
                # Before I implement it.
                pass

            random_state.shuffle(accessible_locations)
            location = accessible_locations.pop()

            worlds[location.world_id].location_entries.remove(location)  # We could use a dict [str, Location],
            # but this works just fine.
            worlds[location.world_id].area_entries[location.area_name].locations.remove(location)
            location.current_item = next_item
            rollbacks += [f"{location.name}-{location.world_id}"]
            worlds[location.world_id].location_entries.append(location)
            worlds[location.world_id].area_entries[location.area_name].locations.append(location)
    return worlds


"""
    I'm not 100% sure on this Function, but the currently failing Seeds don't even call this, so it's not a priority for
    the current iteration.
"""


def forward_fill_until_more_free_space(worlds: List[World], items_to_place: List[GameItem],
                                       input_locations: List[Location], random_state: Random, open_locations=2):
    allowed_locations = input_locations.copy()
    if len(allowed_locations) < len(items_to_place):
        raise RuntimeError(f"Tried to place {len(items_to_place)} items for {len(allowed_locations)} locations!")

    accessible_locations = get_accessible_locations(worlds, [], allowed_locations)

    if len(accessible_locations) == 0:
        raise RuntimeError(f"No accessible locations to place items!")

    forward_placed_items = []
    while len(accessible_locations) < (open_locations * len(worlds)):
        placeable_locations = list(
            filter((lambda loca: Location.partial_list_comparison(allowed_locations, loca)), accessible_locations))
        random_state.shuffle(items_to_place)
        original_size = len(forward_placed_items.copy())

        for item in items_to_place:
            forward_placed_items.append(item)
            access_locs = get_accessible_locations(worlds, forward_placed_items, placeable_locations)
            if len(access_locs) > 0:
                loc = random_state.choice(placeable_locations)
                placeable_locations.remove(loc)
                print(f"Item: {item_id_to_name_dict[item.game_item_id]}:W{item.world_id} opened up more space")
                worlds[loc.world_id].location_entries.remove(loc)
                worlds[loc.world_id].area_entries[loc.area_name].locations.remove(loc)
                loc.current_item = item
                worlds[loc.world_id].location_entries.append(loc)
                worlds[loc.world_id].area_entries[loc.area_name].locations.append(loc)
            else:
                forward_placed_items.remove(item)

        print(f"Size of Original {original_size} vs current {len(forward_placed_items)}")
        if len(forward_placed_items) == original_size:
            raise RuntimeError("No items opened up the forward fill")
        accessible_locations = get_accessible_locations(worlds, forward_placed_items, allowed_locations)

    for item in forward_placed_items:
        items_to_place.remove(item)

    return worlds


"""
    This function is used in the Race Mode Dungeons, I don't believe it works as intended, but it only handles compass
    and maps, which seem to work as intended, so I'm not worried about it.
"""


def fast_fill(locations: list[Location], items: list[GameItem], random_state: Random):
    open_locations = [location for location in locations if
                      location.current_item.game_item_id is item_id_dict["Nothing"]]
    if len(open_locations) < len(items):
        raise RuntimeWarning(f"Tried to place {len(items)} items for {len(open_locations)} locations!")

    while len(items) != 0 and len(open_locations) != 0:
        item = random_state.choice(items)
        location = random_state.choice(open_locations)
        location.current_item = item
        items.remove(item)
        open_locations.remove(location)
    return open_locations, items


"""
    This function is currently not in use, I already know it's current state would not work.
"""


def fill_the_rest(locations: list[Location], items: list[GameItem], random_state: Random):
    fast_fill(locations, items, random_state)

    for location in locations:
        if location.current_item is None:
            location.current_item = GameItem.random_junk(location.world_id, random_state)


"""
    A very nasty way to flatmap the nested lists
"""


def get_item_pool(worlds: list[World]) -> list[GameItem]:
    return list(itertools.chain.from_iterable(
        [world.item_pool for world in worlds]))


"""
    Same as above for Locations instead
"""


def get_location_pool(worlds: list[World]) -> list[Location]:
    return list(itertools.chain.from_iterable(
        [world.location_entries for world in worlds]))
