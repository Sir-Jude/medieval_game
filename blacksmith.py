from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Blacksmith(Character):
    def __init__(self, name, health, weapon, armor=None):
        super().__init__(name, health)
        self.weapon = weapon
        self.armor = armor
        self.defence_points = 20
        self.attack_points = 15

    def attack(self, weapon):
        self.distraction = int(
            random(0, 11)
        )  # distraction can take til 100% from attack_points
        if weapon:
            if weapon.skill == "Spell":
                self.attack_points += weapon.damage - self.distraction - 1
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "Sword":
                self.attack_points += weapon.damage - self.distraction + 10
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "Bow":
                self.attack_points += weapon.damage - self.distraction + 3
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
                self.defence_points += armor.defence - self.distraction - 3
                # a proper armor can add til 50% from defence_points
            if armor.skill == "Helmet":
                self.defence_points += armor.defence - self.distraction + 5
                # wrong armor can take til 50% from defence_points
        return self.defence_points