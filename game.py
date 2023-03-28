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


class Bow(Weapon):
    def __init__(self, name, damage=10, skill="Bow"):
        self.name = name
        self.damage = damage
        self.skill = skill
    

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
    

class Warrior(Character):
    def __init__(self, name, health, weapon, armor=None):
        super().__init__(name, health)
        self.weapon = weapon
        self.defence_points = 15
        self.attack_points = 15
        self.armor = armor
        
    def attack(self, weapon):
        if  weapon.skill == "Spell":
            self.attack_points += 0
        elif weapon.skill == "Sword":
            self.attack_points += 10
        elif weapon.skill == "Bow":
            self.attack_points -= 5 
        
    def defend(self, armor):
        if armor:
            if armor == "Shield":
                self.defence_points += 10
            if armor == "Cloak":
                self.defence_points -= 3
            if armor == "Helmet":
                self.defence_points += 5
        return 0
            
    def get_info(self):
        return f"Name: {self.name}, the Great Warrior\nHealth: {self.health}\nDamage: {((self.weapon).damage)}"
        