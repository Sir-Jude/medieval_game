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