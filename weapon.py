from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    def __init__(self, name, damage, skill):
        self.name = name
        self.damage = damage
        self.skill = skill

    @abstractmethod
    def aim(self):
        pass


class Wand(Weapon):
    def __init__(self, name, damage=10, skill="Spell"):
        self.name = name
        self.damage = damage
        self.skill = skill


class Bow(Weapon):
    def __init__(self, name, damage=10, skill="Bow"):
        self.name = name
        self.damage = damage
        self.skill = skill


# So as we are have 5 characters we need to replace numbers with values
class Sword(Weapon):
    def __init__(self, name, damage, skill="Sword"):
        super().__init__(name)
        self.name = name
        self.damage = damage
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(51, 88)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(19, 45)


class Stick(Weapon):
    def __init__(self, name, damage, skill="Spell"):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(43, 91)
        skill = skill

    def aim(self, hit):
        if hit == 1:
            self.damage = random.randint(70, 100)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(20, 45)
        else:
            self.damage = random.randint(10, 90)


class Spear(Weapon):
    def __init__(self, name, damage, skill="Sword"):
        super().__init__(name)
        self.name = name
        self.damage = damage
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(43, 91)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(43, 91)


class Axe(Weapon):
    def __init__(self, name, damage, skill="Sword"):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(55, 91)
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(55, 91)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(35, 70)
