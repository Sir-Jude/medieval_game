from abc import ABC


class Armor(ABC):
    def __init__(self, name, defence, armor_type):
        self.name = name
        self.defence = defence
        self.armor_type = armor_type

def armor_factory(armor):
    if armor.lower() == "cloack":
        return Armor("cloack", 5, "light")
    elif armor.lower() == "helmet":
        return Armor("helmet", 10, "heavy")
    elif armor.lower() == "round shield":
        return Armor("round shield", 15, "light")
    elif armor.lower() == "roman shield":
        return Armor("roman shield", 20, "heavy")
    elif armor.lower() == "leather armor":
        return Armor("leather armor", 15, "light")
    elif armor.lower() == "metal armor":
        return Armor("metal armor", 20, "heavy")
    else:
        raise ValueError(f"Invalid armor type: {armor}")
