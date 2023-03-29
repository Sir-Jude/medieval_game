import random
from time import sleep
import weapons
import armors



class Character:
    def __init__(self, person, name, skill, weapon=None, armor=None, health=10):
        self.person = person
        self.name = name
        self.skill = skill
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.defence_points = 15
        self.attack_points = 15
        

    def attack(self):
        self.distraction = random.randint(0, 11)
        # distraction can take til 100% from attack_points
        if self.weapon:
            if self.weapon.skill == self.skill:
                self.attack_points += self.weapon.damage - self.distraction + 5
                # wrong weapon can take til 50% from attack_points
            elif self.weapon.skill == "close" and self.skill == "distant":
                self.attack_points += self.weapon.damage - self.distraction -2
                # a proper weapon can add til 50% from attack_points
            elif self.weapon.skill == "close" and self.skill == "magic":
                self.attack_points += self.weapon.damage - self.distraction - 5
                # wrong weapon can take til 50% from attack_points
            elif self.weapon.skill == "distant" and self.skill == "close":
                self.attack_points += self.weapon.damage - self.distraction -2
                # wrong weapon can take til 50% from attack_points
            elif self.weapon.skill == "distant" and self.skill == "magic":
                self.attack_points += self.weapon.damage - self.distraction -5
                # a proper weapon can add til 50% from attack_points
            elif self.weapon.skill == "magic" and self.skill == "close":
                self.attack_points += self.weapon.damage - self.distraction -5
                # wrong weapon can take til 50% from attack_points
            elif self.weapon.skill == "magic" and self.skill == "distant":
                self.attack_points += self.weapon.damage - self.distraction -2
                # a proper weapon can add til 50% from attack_points
        return self.attack_points

    def defend(self):
        self.distraction = random.randint(0, 11)
        # distraction can take til 100% from defence_points
        if self.armor:
            if self.armor == "Shield":
                self.defence_points += self.armor.defence - self.distraction - 5
                # wrong armor can take til 50% from defence_points
            elif self.armor == "Cloak":
                self.defence_points += self.armor.defence - self.distraction - 5
                # wrong armor can take til 50% from defence_points
            elif self.armor == "Helmet":
                self.defence_points += self.armor.defence - self.distraction
                # wrong armor can take til 50% from defence_points
        return self.defence_points

    def __str__(self):

        return f"{self.name}, a great {self.person}, who will fight with a {self.weapon.name} and a {self.armor.name}."


def character_factory(character, name, weapon, armor):
    if character.lower() == "warrior":
        return Character("warrior", name, "close", weapons.weapon_factory(weapon), armors.armor_factory(armor))
    elif character.lower() == "magician":
        return Character("magician", name, "magic", weapons.weapon_factory(weapon), armors.armor_factory(armor))
    elif character.lower() == "archer":
        return Character("archer", name, "distant", weapons.weapon_factory(weapon), armors.armor_factory(armor))
    elif character.lower() == "smith":
        return Character("smith", name, "close", weapons.weapon_factory(weapon), armors.armor_factory(armor))