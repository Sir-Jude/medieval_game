import random
from time import sleep
import weapon
import armor



class Character:
    def __init__(self, person, name, skill, health, weapon=None, armor=None):
        self.person = person
        self.name = name
        self.skill = skill
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.defence_points = 15
        self.attack_points = 15
        

    def attack(self, weapon):
        self.distraction = int(
            random(0, 11)
        )  # distraction can take til 100% from attack_points
        if weapon:
            if weapon.skill == self.skill:
                self.attack_points += weapon.damage - self.distraction + 5
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "close" and self.skill == "distant":
                self.attack_points += weapon.damage - self.distraction -2
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "close" and self.skill == "magic":
                self.attack_points += weapon.damage - self.distraction - 5
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "distant" and self.skill == "close":
                self.attack_points += weapon.damage - self.distraction -2
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "distant" and self.skill == "magic":
                self.attack_points += weapon.damage - self.distraction -5
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "magic" and self.skill == "close":
                self.attack_points += weapon.damage - self.distraction -5
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "magic" and self.skill == "distant":
                self.attack_points += weapon.damage - self.distraction -2
                # a proper weapon can add til 50% from attack_points
        return self.attack_points

    def defend(self, armor):
        self.distraction = int(
            random(0, 11)
        )  # distraction can take til 100% from defence_points
        if armor:
            if armor == "Shield":
                self.defence_points += armor.defence - self.distraction - 5
                # wrong armor can take til 50% from defence_points
            elif armor == "Cloak":
                self.defence_points += armor.defence - self.distraction - 5
                # wrong armor can take til 50% from defence_points
            elif armor == "Helmet":
                self.defence_points += armor.defence - self.distraction
                # wrong armor can take til 50% from defence_points
        return self.defence_points

    def get_info(self):

        return f"Name: {self.name}, the Great\nHealth: {self.health}\nDamage: {((self.weapon).damage)}"


class Magician(Character):
    def __init__(self, name, health, weapon, armor=None):
        super().__init__(name, health)
        self.weapon = weapon
        self.armor = armor
        self.defence_points = 10
        self.attack_points = 10

    def attack(self, weapon):
        self.distraction = int(
            random(0, 11)
        )  # distraction can take til 100% from attack_points
        if weapon:
            if weapon.skill == "Spell":
                self.attack_points += weapon.damage - self.distraction + 5
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "Sword":
                self.attack_points += weapon.damage - self.distraction - 5
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "Bow":
                self.attack_points += weapon.damage - self.distraction
                # wrong weapon can take til 50% from attack_points
        return self.attack_points

    def defend(self, armor):
        self.distraction = int(
            random(0, 11)
        )  # distraction can take til 100% from defence_points
        if armor:
            if armor.skill == "Shield":
                self.defence_points += armor.defence - self.distraction
                # wrong armor can take til 50% from defence_points
            elif armor.skill == "Cloak":
                self.defence_points += armor.defence - self.distraction + 5
                # a proper armor can add til 50% from defence_points
            elif armor.skill == "Helmet":
                self.defence_points += armor.defence - self.distraction - 5
                # wrong armor can take til 50% from defence_points
        return self.defence_points

    def get_info(self):
        return f"Name: {self.name}, the Mage\nHealth: {self.health}\nDamage: {((self.weapon).damage)}"


class Archer(Character):
    def __init__(self, name, health, weapon, armor=None):
        super().__init__(name, health)
        self.weapon = weapon
        self.armor = armor
        self.defence_points = 10
        self.attack_points = 10

    def attack(self, weapon):
        self.distraction = int(
            random(0, 11)
        )  # distraction can take til 100% from attack_points
        if weapon:
            if weapon.skill == "Spell":
                self.attack_points += weapon.damage - self.distraction - 5
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "Sword":
                self.attack_points += weapon.damage - self.distraction + 4
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "Bow":
                self.attack_points += weapon.damage - self.distraction + 10
                # wrong weapon can take til 50% from attack_points
        return self.attack_points

    def defend(self, armor):
        self.distraction = int(
            random(0, 11)
        )  # distraction can take til 100% from defence_points
        if armor:
            if armor.skill == "Shield":
                self.defence_points += armor.defence - self.distraction + 10
                # wrong armor can take til 50% from defence_points
            if armor.skill == "Cloak":
                self.defence_points += armor.defence - self.distraction + 3
                # a proper armor can add til 50% from defence_points
            if armor.skill == "Helmet":
                self.defence_points += armor.defence - self.distraction - 3
                # wrong armor can take til 50% from defence_points
        return self.defence_points


def character_factory(character):
    if character.lower() == "warrior":
        return Character("warrior", name=None, health=10)
    elif character.lower() == "magician":
        return Character("magician", name=None, health=10)
    elif character.lower() == "archer":
        return Character("archer", name=None, health=10)
    elif character.lower() == "smith":
        return Character("smith", name=None, health=10)