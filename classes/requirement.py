from __future__ import annotations
from dataclasses import dataclass

from logic.extras import *


@dataclass
class Requirement:
    type: AnyStr
    args: List

    @classmethod
    def from_dict(cls, dict_obj) -> Requirement:
        req_type = str(dict_obj["type"]).upper()
        if req_type not in REQUIREMENT_TYPES:
            raise RuntimeError(f"Invalid Type {req_type} passed in.")
        else:
            return cls(type=req_type, args=parse_element(req_type, dict_obj["args"]))


@dataclass
class Macro:
    name: AnyStr
    expression: Requirement

    @classmethod
    def from_dict(cls, dict_obj) -> Macro:
        return cls(
            name=dict_obj["Name"], expression=Requirement.from_dict(dict_obj["Expression"])
        )


def parse_element(req_type: AnyStr, json_args) -> List[Any]:
    if len(json_args) == 0:
        raise RuntimeError("At least one Argument is Required to Parse an Element")
    elif req_type == REQUIREMENT_OR or req_type == REQUIREMENT_AND:
        return list(map(Requirement.from_dict, json_args))
    elif req_type == REQUIREMENT_NOT:
        return [Requirement.from_dict(json_args[0])]
    elif req_type == REQUIREMENT_HAS_ITEM:
        return [item_id_dict[json_args[0]]]
    elif req_type == REQUIREMENT_COUNT:
        if len(json_args) != 2:
            raise RuntimeError("At least two Arguments are Required for COUNT")
        return [int(json_args[0]), json_args[1]]
    elif req_type == REQUIREMENT_CAN_ACCESS:
        return [json_args[0]]
    elif req_type == REQUIREMENT_SETTING:
        # Might need a reference to the toggled settings for this...
        return [json_args[0]]
    elif req_type == REQUIREMENT_MACRO:
        # Since we're using a dictionary for Macros, we'll just return the inner string.
        return [json_args[0]]
    else:
        raise RuntimeError(f"Invalid Type {req_type} passed into 'World.parse_element'")
