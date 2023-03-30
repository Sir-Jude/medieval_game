# Python imports
from abc import ABC, abstractmethod
from time import sleep
from os import system
import random

# Custom imports
import weapons
import armors
from characters import Character, character_factory
import boss

class HeroTurn:
    def __init__(self, fighters):
        self.fighters = fighters
    
    def damage_amount(self, def_power, att_power):
        if (def_power - att_power) > 0:
            return 0
        else:
            return def_power - att_power

    def hero_result(self, def_power, att_power, enemy):
        for fighter in self.fighters:
            damage = self.damage_amount(def_power, att_power)
            print(f"{fighter.name} ({fighter.health}hp) attacks {enemy.name} with his {fighter.weapon.name}({att_power}).")
            print(f"{enemy.name} the Beast lost {damage} hp, and now has {enemy.health+damage}hp left.")
            enemy.health = enemy.health + damage
            sleep(0.5)

    
class BossTurn:
    def __init__(self, fighters):
        self.fighters = fighters
        self.fighter = self.fighters[random.randint(0, len(self.fighters)-1)] # Random victim chose 
    
    def damage_amount(self, def_power, att_power):
        if (def_power - att_power) > 0:
            return 0
        else:
            return def_power - att_power
        
    def boss_result(self, def_power, att_power, enemy):
        damage = self.damage_amount(def_power, att_power)
        print(f"{enemy.name} ({enemy.health}hp) attacks {self.fighter.name} with his Krav Maga and brute force ({att_power}).")
        print(f"{self.fighter.name} the {self.fighter.person} lost {damage} hp and now has {self.fighter.health+damage} hp.")
        self.fighter.health = self.fighter.health + damage
        
    
    


    