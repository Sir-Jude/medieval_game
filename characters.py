import random
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
        self.defense_points = 20
        self.attack_points = 20
        

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