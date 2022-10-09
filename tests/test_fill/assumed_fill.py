import unittest

from logic.fill import assumed_fill

from tests.utils.world_util import *
from tests.utils.settings_util import *

class SingleWorldAssumedFill(unittest.TestCase):

    def test_single_item_fill(self):
        test_areas = {area.name: area for area in generate_test_areas(0)}
        test_areas["Root"] = generate_test_area(0, "Root", "Area1")
        test_areas["Root"].locations = []
        base_world = World(settings=Settings(build_default_settings()), world_id=0)
        base_world.area_entries = test_areas
        base_world.item_pool = []
        base_world.starting_items = []
        base_world.location_entries = [loc for area in list(base_world.area_entries.values()) for loc in area.locations]
        logical_locations = list(filter((lambda loc: loc.is_logical_location()),base_world.location_entries))
        self.assertEqual(3, len(logical_locations))
        logical_item = GameItem(game_item_id=1, world_id=0)

        base_world = assumed_fill([base_world], [logical_item], logical_locations, RandomProxy())[0]
        self.assertEqual(6, len(base_world.location_entries))


class RandomProxy:
    def __init__(self):
        pass

    def shuffle(self, obj):
        return obj