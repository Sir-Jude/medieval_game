import random
from time import sleep

class FinalBoss:
    def __init__(self, name="Markus", health=500, attack_points=25, defence_points=50):
        self.name = name
        self._health = health
        self.attack_points = attack_points
        self.defence_points = defence_points

    def attack(self):
        # Final boss can do a critical attacks someties
        if random.randint(0, 10) == 0:
            self.attack_points *= 2
            print(f"{self.name} did a critical attack!")
        return self.attack_points

    def defend(self):
        # Final boss can defend himself better sometimes
        if random.randint(0, 10) == 0:
            self.defence_points += 100
            print(f"{self.name} increased his defense!")
        return self.defence_points

    def take_damage(self, damage):
        # Final boss can regenerate his healh sometimes
        if random.randint(0, 10) == 0:
            print(f"{self.name} regenerated some health!")
            self._health += 50
        self._health -= (damage - self.defence_points)
        return self._health

    def get_info(self):
        return f"Name: {self.name}\nHealth: {self._health}\nAttack: {self.attack_points}\nDefense: {self.defence_points}"
    
Markus = FinalBoss()
print(Markus.get_info())

Markus.attack()
Markus.defend()
Markus.take_damage(100)
print(Markus.get_info())

