# Python imports
from abc import ABC, abstractmethod
from time import sleep
from os import system
import random

# Custom imports
import weapons
import armors
import boss


class Character:
    def __init__(self, person=None, name=None, skill=None, weapon=None, armor=None, health=30):
        self.person = person
        self.name = name
        self.skill = skill
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.defense_points = 20
        self.attack_points = 20

    def get_name(self, num):
        # Name the character
        if num == 1:
            self.name = input("You, what is your name? ").title()
        elif num == 2:
            self.name = input("And you there, which is your name? ").title()
        elif num == 3:
            self.name = input("And finally you, how are you known? ").title()

    def get_class(self):
        personality = input(
            f"""And what are you {self.name}?
[1] Warrior
[2] Magician
[3] Archer
[4] Smith
-> """
        )
        if personality == "1":
            self.person = "Warrior"
            self.skill = "close"
        elif personality == "2":
            self.person = "Magician"
            self.skill = "magic"
        elif personality == "3":
            self.person = "Archer"
            self.skill = "distant"
        elif personality == "4":
            self.person = "Smith"
            self.skill = "close"

    def get_weapon(self):
        fighter_weapon = input(
            f"""Ok, {self.name} the {self.person}, what are you going to fight with?
[1] Sword
[2] Axe
[3] Stick
[4] Wand
[5] Spear
[6] Bow
-> """
        )
        if fighter_weapon == "1":
            self.weapon = weapons.weapon_factory("Sword")
        elif fighter_weapon == "2":
            self.weapon = weapons.weapon_factory("Axe")
        elif fighter_weapon == "3":
            self.weapon = weapons.weapon_factory("Stick")
        elif fighter_weapon == "4":
            self.weapon = weapons.weapon_factory("Wand")
        elif fighter_weapon == "5":
            self.weapon = weapons.weapon_factory("Spear")
        elif fighter_weapon == "6":
            self.weapon = weapons.weapon_factory("Bow")
    
    def get_armor(self):
        fighter_armor = input(
        f"""And how do you plan to defend yourself?
[1] Cloak
[2] Helmet
[3] Round shield
[4] Roman shield
[5] Leather armor
[6] Metal armor
-> """
    )
        if fighter_armor == "1":
            self.armor = armors.armor_factory("Cloak")
        elif fighter_armor == "2":
            self.armor = armors.armor_factory("Helmet")
        elif fighter_armor == "3":
            self.armor = armors.armor_factory("Round Shield")
        elif fighter_armor == "4":
            self.armor = armors.armor_factory("Roman Shield")
        elif fighter_armor == "5":
            self.armor = armors.armor_factory("Leather Armor")
        elif fighter_armor == "6":
            self.armor = armors.armor_factory("Metal Armor")

    def attack(self):
        self.distraction = random.randint(0, 11)
        # distraction can take up to 10 points from attack_power
        if self.weapon:
            if self.weapon.skill == self.skill:
                attack_power = self.attack_points + self.weapon.damage - self.distraction + 5
                # a proper weapon can add up to 5 to attack_power
            elif self.weapon.skill == "close" and self.skill == "distant":
                attack_power = self.attack_points + self.weapon.damage - self.distraction - 5
                # a totally wrong weapon can take up to 5 points from attack_power
            elif self.weapon.skill == "distant" and self.skill == "close":
                attack_power = self.attack_points + self.weapon.damage - self.distraction - 5
                # a totally wrong weapon can take up to 5 points from attack_power
            elif self.weapon.skill == "distant" and self.skill == "magic":
                attack_power = self.attack_points + self.weapon.damage - self.distraction -2
                # other weapons can take up to 2 points from attack_power
            elif self.weapon.skill == "magic" and self.skill == "distant":
                attack_power = self.attack_points + self.weapon.damage - self.distraction - 2
                # other weapons can take up to 2 points from attack_power
            else:
                attack_power = self.attack_points + self.weapon.damage - self.distraction
                # this is just a neutral situation
        return attack_power

    def defend(self):
        self.distraction = random.randint(0, 10)
        # distraction can take up to 10 points from defense_power
        if self.armor:
            if self.armor.skill == self.skill:
                defense_power = self.defense_points + self.armor.defense - self.distraction + 5
                # a proper armor can add up to 5 to defense_power
            elif self.armor.skill == "close" and self.skill == "distant":
                defense_power = self.defense_points + self.armor.defense - self.distraction - 5
                # a totally wrong armor can take up to 5 points from defense_power
            elif self.armor.skill == "distant" and self.skill == "close":
                defense_power = self.defense_points + self.armor.defense - self.distraction - 5
                # a totally wrong armor can take up to 5 points from defense_power
            elif self.armor.skill == "distant" and self.skill == "magic":
                defense_power = self.defense_points + self.armor.defense - self.distraction - 2
                # other armor can take up to 2 points from defense_power
            elif self.armor.skill == "magic" and self.skill == "distant":
                defense_power = self.defense_points + self.armor.defense - self.distraction - 2
                # other armor can take up to 2 points from defense_power
            else:
                defense_power = self.defense_points + self.armor.defense - self.distraction
                # this is just a neutral situation
        return defense_power

    def __str__(self):
        return f"{self.name}, a great {self.person}, who will fight with a {self.weapon.name} and a {self.armor.name}.\nHealth Points: {self.health} \nDefense  Points: {self.defense_points + self.armor.defense} \nAttack Points:{self.attack_points + self.weapon.damage}"


def character_factory():
    return Character()