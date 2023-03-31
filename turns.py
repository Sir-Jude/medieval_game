# Python imports
from time import sleep
import random

# Custom imports


class HeroTurn:
    def __init__(self, fighter, enemy):
        self.fighter = fighter
        self.enemy = enemy

    def hero_result(self):
        def_power = self.enemy.defend()
        att_power = self.fighter.attack()
        if (def_power - att_power) > 0:
            damage = 0
        else:
            damage = def_power - att_power
        print(
            f"{self.fighter.name} ({self.fighter.health}hp) attacks {self.enemy.name} with his {self.fighter.weapon.name}({att_power})."
        )
        print(
            f"{self.enemy.name} the Beast lost {abs(damage)} hp, and now has {self.enemy.health+damage}hp left."
        )
        self.enemy.health += damage
        sleep(1)


class BossTurn:
    def __init__(self, fighters, enemy):
        self.fighters = fighters
        self.enemy = enemy
        
    def boss_result(self):
        fighter = self.fighters[
            random.randint(0, len(self.fighters) - 1)
        ]  # Random victim chose
        def_power = fighter.defend()
        att_power = self.enemy.attack()
        if (def_power - att_power) > 0:
            damage = 0
        else:
            damage = def_power - att_power
        print(
            f"{self.enemy.name} ({self.enemy.health}hp) attacks {fighter.name} with his Krav Maga and brute force ({att_power})."
        )
        print(
            f"{fighter.name} the {fighter.person} lost {abs(damage)} hp and now has {fighter.health+damage} hp."
        )
        fighter.health += damage
