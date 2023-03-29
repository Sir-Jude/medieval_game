from abc import ABC, abstractmethod
import random


class Weapon(ABC): 
    def __init__(self, name, damage, skill):
        self.name = name
        self.damage = damage
        self.skill = skill


class Sword(Weapon): # Good for Warrior, bad for Magician, nice for archer
    def __init__(self, name, damage, skill="close"):
        super().__init__(name)
        self.name = name
        self.damage = damage
        skill = skill


class Axe(Weapon):  # Best for Warrior, worse for Magician, bad for archer
    def __init__(self, name, damage, skill="close"):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(55, 91)
        skill = skill


class Stick(Weapon):  # bad for Warrior, good for Magician, good for archer
    def __init__(self, name, damage, skill="magic"):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(43, 91)
        skill = skill


class Wand(Weapon):
    def __init__(self, name, damage=10, skill="magic"):
        self.name = name
        self.damage = damage
        self.skill = skill


class Spear(Weapon):  
    def __init__(self, name, damage, skill="distant"):
        super().__init__(name)
        self.name = name
        self.damage = damage
        skill = skill


class Bow(Weapon):
    def __init__(self, name, damage=10, skill="distant"):
        self.name = name
        self.damage = damage
        self.skill = skill
