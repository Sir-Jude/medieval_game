from abc import ABC, abstractmethod
import random
from time import sleep

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
    
    
class Weapon(ABC):
    def __init__(self, name, damage, skill):
        self.name = name
        self.damage = damage
        self.skill = skill
    
    @abstractmethod
    def aim(self):
        pass

class Armor(ABC):
    def __init__(self, name, defence):
        self.name = name
        self.defence = defence

class Magician(Character):
    def __init__(self, name, health, weapon, armor=None):
        super().__init__(name, health)
        self.weapon = weapon
        self.defence_points = 10
        self.attack_points = 10
        self.armor = armor
        
    def attack(self, weapon):
        if  weapon.skill == "Spell":
            self.attack_points += 10
        elif weapon.skill == "Sword":
            self.attack_points -=5
        elif weapon.skill == "Bow":
            self.attack_points += 0
        
    def defend(self, armor):
        if armor:
            if armor == "Shield":
                self.defence_points += 5
            if armor == "Cloak":
                self.defence_points += 10 
            if armor == "Helmet":
                self.defence_points -= 3
        return 0
            
    def get_info(self):
        return f"Name: {self.name}, the Mage\nHealth: {self.health}\nDamage: {((self.weapon).damage)}"
        
        
# So as we are have 5 characters we need to replace numbers with values
class Sword(Weapon):
    def __init__(self, name, damage, skill):
        super().__init__(name)
        self.name = name
        self.damage = damage
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(51,88)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(19,45)

class Bow(Weapon):
    def __init__(self, name, damage, skill):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(60,70)
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(60,75)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(50,65)

class Stick(Weapon):
    def __init__(self, name, damage, skill):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(43,91)
        skill = skill

    def aim(self, hit):
        if hit == 1:
            self.damage = random.randint(70,100)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(20,45)
        else:
            self.damage = random.randint(10,90)

class Spear(Weapon):
    def __init__(self, name, damage, skill):
        super().__init__(name)
        self.name = name
        self.damage = damage
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(43,91)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(43,91)

class Axe(Weapon):
    def __init__(self, name, damage, skill):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(55,91)
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(55,91)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(35,70)