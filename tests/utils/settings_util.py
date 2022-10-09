from collections import OrderedDict


def build_default_settings():
    settingsDict = OrderedDict()
    setattr(settingsDict, "get", inner_replacement)
    return settingsDict


def inner_replacement(x):
    if x == "multiworld":
        return "multiworld"
    elif x == "starting_gear":
        return []
    else:
        return True
