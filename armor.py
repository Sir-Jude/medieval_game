from abc import ABC


class Armor(ABC):
    def __init__(self, name, defence, armor_type):
        self.name = name
        self.defence = defence
        self.armor_type = armor_type

def armor_factory(armor):
    if armor.lower() == "cloack":
        return Armor("Cloack", 5, "light")
    elif armor.lower() == "helmet":
        return Armor("Helmet", 10, "heavy")
    elif armor.lower() == "round shield":
        return Armor("Round Shield", 15, "light")
    elif armor.lower() == "roman shield":
        return Armor("Roman Shield", 20, "heavy")
    elif armor.lower() == "leather armor":
        return Armor("Leather Armor", 15, "light")
    elif armor.lower() == "metal armor":
        return Armor("Metal Armor", 20, "heavy")
    else:
        raise ValueError(f"Invalid armor type: {armor}")
