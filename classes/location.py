from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Set

from classes.gameitem import GameItem
from classes.requirement import Requirement, Macro
from logic.extras import *


@dataclass
class Location:
    name: str
    category_set: Set[AnyStr]
    area_name: str
    requirement: Requirement | List[Requirement]
    filePaths: List[str]
    current_item: GameItem = GameItem(game_item_id=item_id_dict["Nothing"])
    world_id: int = -1
    logical: bool = False

    @classmethod
    def from_dict(cls, dict_obj, area_name: str) -> Location:
        return cls(name=dict_obj["Name"],
                        category_set=set(dict_obj["Category"]),
                        requirement=Requirement.from_dict(dict_obj["Needs"]),
                        filePaths=dict_obj["Paths"],
                        area_name=area_name
                        )

    def is_logical_location(self) -> bool:
        return self.logical and self.name != "DefeatGanondorf"

    def make_logical(self) -> Location:
        self.logical = True
        return self

    def set_world_id(self, world_id: int) -> Location:
        self.world_id = world_id
        return self

    def spoiler_representation(self) -> AnyStr:
        return f"W{self.world_id + 1}: {self.name} - W{self.current_item.world_id + 1} {item_id_to_name_dict[self.current_item.game_item_id]}"

    def spoiler_short_hand_item_rep(self) -> AnyStr:
        return f"W{self.current_item.world_id + 1} {item_id_to_name_dict[self.current_item.game_item_id]}"

    def spoiler_short_hand_loc_rep(self) -> AnyStr:
        return f"W{self.world_id + 1} {self.name}"

    @staticmethod
    def partial_list_comparison(source_list: Iterable[Location], other_location: Location) -> bool:
        return any(map(other_location.similar, source_list))

    def similar(self, other: Location) -> bool:
        return self.name == other.name and self.world_id == other.world_id

    def set_item_type(self) -> Location:
        self.current_item = self.current_item.set_item_type()
        return self

    def json_output(self) -> Dict[AnyStr, AnyStr]:
        if self.current_item.world_id == -1:
            self.current_item.world_id = self.world_id
        return {
            "Name": self.name,
            "WorldId": self.world_id,
            "Item": item_id_to_name_dict[self.current_item.game_item_id],
            "ItemWorldId": self.current_item.world_id
        }

    def get_required_items(self, reference_macros: Dict[AnyStr, Macro]) -> List[int]:
        return list(parse_macro_requirement_list(reference_macros, *self.requirement))

    def __eq__(self, other: Location) -> bool:
        return self.name == other.name and self.world_id == other.world_id
