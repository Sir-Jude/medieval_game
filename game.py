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
        self.armor = armor
        
    def attack(self, weapon):
        if  weapon.skill == "Spell":
            self.damage += 10
        elif weapon.skill == "Sword":
            self.damage -=5
        elif weapon.skill == "Bow":
            self.damage += 0
        
    def defend(self, armor):
        if armor:
            if armor == "Shield":
                self.armor += 5
            if armor == "Cloak":
                self.armor += 10 
            if armor == "Helmet":
                self.armor -=3
        return 0
            
    def get_info(self):
        return f"Name: {self.name}, the Mage\nHealth: {self.health}\nDamage: {((self.weapon).damage)}"
        
        