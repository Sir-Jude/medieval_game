import random
from time import sleep

class FinalBoss:
    def __init__(self, name="Markus", health=500, attack_points=25, defence_points=15):
        self.name = name
        self.health = health
        self.attack_points = attack_points
        self.defence_points = defence_points

    def attack(self):
        attak_power = random.randint(self.attack_points/2, self.attack_points)
        # Final boss can do a critical attacks someties
        if random.randint(0, 10) == 0:
            attak_power *= 2
            print(f"{self.name} did a critical attack!")
        return attak_power

    def defend(self):
        defence_power = random.randint(self.defence_points/2, self.defence_points)
        # Final boss can restore his health sometimes
        if random.randint(0, 10) == 0:
            self.health += 50
            print(f"{self.name} increased his health!")
        return defence_power

    def take_damage(self, damage):
        # Final boss can regenerate his healh sometimes
        if random.randint(0, 10) == 0:
            print(f"{self.name} regenerated some health!")
            self.health += 50
        self.health -= (damage - self.defence_points)
        return self.health
    
    def __str__(self):
        return f"{self.name} the Beast, who has {self.health} points of health and some unexpected skills."