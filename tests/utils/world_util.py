from classes.location import Location
from classes.world import World
from classes.requirement import Macro, Requirement
from classes.gameitem import GameItem
from classes.settings import Settings
from classes.area import Area, Exit
from logic.extras import *

location_count = 0
def generate_test_exit(exit_name: str, exit_world_id: int) -> Exit:
    return Exit(name=exit_name, requirement=Requirement(type=REQUIREMENT_HAS_ITEM, args=["Nothing"]), world_id=exit_world_id)


def generate_test_areas(area_world_id: int) -> list[Area]:
    return  [
            generate_test_area(area_world_id, "Area1", "Area2"),
            generate_test_area(area_world_id, "Area2", "Area3"),
            generate_test_area(area_world_id, "Area3", None)
            ]

def generate_test_area(world_id: int, area_name: str, exit_name: str, is_accessible=False) -> Area:
    if exit_name is not None:
        return Area(
            name=area_name,
            locations=[generate_logical_location(world_id, area_name), generate_illogical_location(world_id, area_name)],
            exits = {exit_name: generate_test_exit(exit_name, world_id)},
            is_accessible=is_accessible,
            world_id=world_id)
    else:
        return Area(
            name=area_name,
            locations=[generate_logical_location(world_id, area_name), generate_illogical_location(world_id, area_name)],
            exits = {},
            is_accessible=is_accessible,
            world_id=world_id)

def generate_logical_location(loc_world_id: int, area_name: str) -> Location:
    global location_count
    location_count += 1
    return Location(
        name=f"Location{location_count}",
        category_set=["TestLogical"],
        requirement=Requirement(type=REQUIREMENT_HAS_ITEM, args=["Nothing"]),
        world_id= loc_world_id,
        logical=True,
        area_name=area_name,
        filePaths=[]
    )

def generate_illogical_location(loc_world_id: int, area_name: str) -> Location:
    global location_count
    location_count += 1
    return Location(
        name=f"Location{location_count}",
        category_set=["TestIllogical"],
        requirement=Requirement(type=REQUIREMENT_HAS_ITEM, args=["Nothing"]),
        world_id= loc_world_id,
        logical=False,
        area_name=area_name,
        filePaths=[]
    )
