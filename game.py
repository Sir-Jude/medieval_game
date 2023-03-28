from abc import ABC, abstractmethod
import random
from time import sleep

class Carachter(ABC):
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
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    @abstractmethod
    def aim(self):
        pass

class Armor(ABC):
    def __init__(self, name, defence):
        self.name = name
        self.defence = defence
