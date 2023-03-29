class Armor:
    def __init__(self, name, defence, skill):
        self.name = name
        self.defence = defence
        self.skill = skill

def armor_factory(armor):
    if armor.lower() == "cloak":
        return Armor("cloak", 5, "magic")
    elif armor.lower() == "helmet":
        return Armor("helmet", 10, "distant")
    elif armor.lower() == "round shield":
        return Armor("round shield", 15, "close")
    elif armor.lower() == "roman shield":
        return Armor("roman shield", 20, "close")
    elif armor.lower() == "leather armor":
        return Armor("leather armor", 15, "distant")
    elif armor.lower() == "metal armor":
        return Armor("metal armor", 20, "close")
    else:
        raise ValueError(f"Invalid armor type: {armor}")
