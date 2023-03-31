
class Weapon:
    """
    A class to create weapon objects using a factory.
    
    Called from character.py to instantiate a weapon object that will.

    ...

    Attributes
    ----------
    name : str
        the name of the weapon
    damage : int
        the amount of damage the weapon has
    skill : str
        the skill required to best use the weapon

    Methods
    -------
    weapon_factory(weapon)
        takes in weapon as an argument from character.py 
        and then instantiates a Weapon object
    """
    def __init__(self, name: str, damage: int, skill: str):
        self.name = name
        self.damage = damage
        self.skill = skill

def weapon_factory(weapon: str):
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



class SuperWeapon(Weapon):
    """
    A subclass of Weapon 
    Singleton Pattern 
    Is called by character.py

    Creates a special weapon that can be accessed by a cheat code
    """
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        super().__init__("Catapult", 100, "magic")

super_weapon = SuperWeapon()