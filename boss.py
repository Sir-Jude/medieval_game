import random
from time import sleep

class FinalBoss:
    def __init__(self, name="Markus", health=500, attack_points=50, defense_points=20):
        self.name = name
        self.health = health
        self.attack_points = attack_points
        self.defense_points = defense_points

    def attack(self):
        attack_power = random.randint(int(self.attack_points/2), self.attack_points)
        # Final boss can do a critical attacks sometimes
        if random.randint(0, 20) == 0:
            attack_power *= 2
            print(f"{self.name} did a critical attack({attack_power})!!")
        return attack_power

    def defend(self):
        defense_power = random.randint(int(self.defense_points/2), self.defense_points)
        # Final boss can restore his health sometimes
        if random.randint(0, 20) == 0:
            self.health += 50
            print(f"{self.name} increased his health(+50)!!")
        return defense_power
    
    def __str__(self):
        return f"""
                    {self.name} the Beast

Who has {self.health} points of health and some unexpected skills.
His unprenetable defense is {self.defense_points} points and attacks with {self.attack_points} points of damage.
Be careful of he's critical attacks....
    """