class Armor:
    """
    A class to create armor objects using a factory.
    
    Called from character.py to instantiate a armor object that will.

    ...

    Attributes
    ----------
    name : str
        the name of the armor
    defense : int
        the amount of defense the armor has
    skill : str
        the skill required to best use the armor

    Methods
    -------
    armor_factory(armor)
        takes in armor as an argument from character.py 
        and then instantiates a Armor object
    """
    def __init__(self, name, defense, skill):
        self.name = name
        self.defense = defense
        self.skill = skill

def armor_factory(armor):
    if armor.lower() == "cloak":
        return Armor("cloak", 7, "magic")
    elif armor.lower() == "helmet":
        return Armor("helmet", 10, "distant")
    elif armor.lower() == "round shield":
        return Armor("round shield", 15, "close")
    elif armor.lower() == "roman shield":
        return Armor("roman shield", 17, "close")
    elif armor.lower() == "leather armor":
        return Armor("leather armor", 15, "distant")
    elif armor.lower() == "metal armor":
        return Armor("metal armor", 17, "close")
