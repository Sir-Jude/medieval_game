
class Weapon: 
    def __init__(self, name, damage, skill):
        self.name = name
        self.damage = damage
        self.skill = skill

def weapon_factory(weapon):
    if weapon.lower() == "sword":
        return Weapon("Sword", 10, "close")
    elif weapon.lower() == "axe":
        return Weapon("Axe", 20, "close")
    elif weapon.lower() == "stick":
        return Weapon("Stick", 15, "magic")
    elif weapon.lower() == "wand":
        return Weapon("Wand", 10, "magic")
    elif weapon.lower() == "spear":
        return Weapon("Spear", 20, "distant")
    elif weapon.lower() == "bow":
        return Weapon("Bow", 10, "distant")
    else:
        raise ValueError(f"Invalid weapon type: {weapon}")
    