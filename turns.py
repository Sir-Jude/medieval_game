# Python imports
from time import sleep
import random

# Custom imports

class HeroTurn:
    def __init__(self, fighters):
        self.fighters = fighters

    def hero_result(self, def_power, att_power, enemy, fighter):
        if (def_power - att_power) > 0:
            damage = 0
        else:
            damage = def_power - att_power
        print(f"{fighter.name} ({fighter.health}hp) attacks {enemy.name} with his {fighter.weapon.name}({att_power}).")
        print(f"{enemy.name} the Beast lost {abs(damage)} hp, and now has {enemy.health+damage}hp left.")
        enemy.health = enemy.health + damage
        sleep(0.5)

    
class BossTurn:
    def __init__(self, fighters):
        self.fighters = fighters    
    
    def boss_result(self, def_power, att_power, enemy):
        fighter = self.fighters[random.randint(0, len(self.fighters)-1)] # Random victim chose 
        if (def_power - att_power) > 0:
                damage = 0
        else:
            damage = def_power - att_power
        print(f"{enemy.name} ({enemy.health}hp) attacks {fighter.name} with his Krav Maga and brute force ({att_power}).")
        print(f"{fighter.name} the {fighter.person} lost {abs(damage)} hp and now has {fighter.health+damage} hp.")
        fighter.health = fighter.health + damage
            
    
    


    