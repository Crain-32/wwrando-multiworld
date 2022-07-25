from dataclasses import dataclass
from typing import List, Dict, AnyStr
from logic.extras import parse_macro_requirement_list

from classes.location import Location
from classes.requirement import Requirement, Macro



@dataclass
class Exit:
    name: str
    requirement: Requirement
    world_id: int = -1

    @staticmethod
    def from_dict(dict_obj: dict[str, object]):
        return Exit(name=dict_obj["ConnectedArea"], requirement=Requirement.from_dict(dict_obj["Needs"]))


@dataclass
class Area:
    name: str
    locations: list[Location]
    exits: dict[str, Exit]
    is_accessible: bool = False
    world_id: int = -1

    @staticmethod
    def with_world_id(dict_obj: dict[str, object], world_id: int):
        area = Area.from_dict(dict_obj)
        return area.set_world_id(world_id)

    @staticmethod
    def from_dict(dict_obj: dict[str, object]):
        return Area(
            name=dict_obj["Name"],
            locations=list(map((lambda loc: Location.from_dict(loc, dict_obj["Name"])), dict_obj["Locations"])),
            exits={exits.name: exits for exits in list(map(Exit.from_dict, dict_obj["Exits"]))}
        )

    def set_world_id(self, world_id: int):
        self.world_id = world_id
        for name, exits in self.exits.items():
            exits.world_id = world_id
            self.exits[name] = exits
        self.locations = list(map((lambda loc: loc.set_world_id(world_id)), self.locations))
        return self

    def get_locations(self) -> list[Location]:
        return self.locations

    def get_required_item_id(self, referenced_macros: Dict[AnyStr, Macro], connected_areas: List[AnyStr]) -> List[int]:
        val = set()
        target_locations = list(filter(Location.is_logical_location, self.locations))
        for loc in target_locations:
            for item_id in parse_macro_requirement_list(referenced_macros, loc.requirement):
                val.add(item_id)
        for connected_name, connected_req in self.exits.items():
            if connected_name in connected_areas:
                for item_id in parse_macro_requirement_list(referenced_macros, connected_req.requirement):
                    val.add(item_id)
        return list(val)