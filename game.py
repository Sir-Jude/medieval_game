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

class Cloack(Armor):
    def __init__(self, name, defence=10, skill="Cloack"):
        self.name = name
        self.defence = defence
        self.skill = skill

class Helmet(Armor):
    def __init__(self, name, defence=5, skill="Helmet"):
        self.name = name
        self.defence = defence
        self.skill = skill

class Magician(Character):
    def __init__(self, name, health, weapon, armor=None):
        super().__init__(name, health)
        self.weapon = weapon
        self.armor = armor
        self.defence_points = 10
        self.attack_points = 10
        
    def attack(self, weapon):
        self.distraction = int(random(0,11)) # distraction can take til 100% from attack_points
        if weapon:
            if  weapon.skill == "Spell":
                self.attack_points += (weapon.damage - self.distraction + 5)
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "Sword":
                self.attack_points += (weapon.damage - self.distraction - 5)
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "Bow":
                self.attack_points += (weapon.damage - self.distraction)
                # wrong weapon can take til 50% from attack_points
        return self.attack_points
    
    def defend(self, armor):
        self.distraction = int(random(0,11)) # distraction can take til 100% from defence_points
        if armor:
            if armor.skill == "Shield":
                self.defence_points += (armor.defence - self.distraction)
                # wrong armor can take til 50% from defence_points
            elif armor.skill == "Cloak":
                self.defence_points += (armor.defence - self.distraction + 5)
                # a proper armor can add til 50% from defence_points
            elif armor.skill == "Helmet":
                self.defence_points += (armor.defence - self.distraction - 5)
                # wrong armor can take til 50% from defence_points
        return self.defence_points
            
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
        self.distraction = int(random(0,11)) # distraction can take til 100% from attack_points
        if weapon:
            if weapon.skill == "Spell":
                self.attack_points += (weapon.damage - self.distraction - 5)
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "Sword":
                self.attack_points += (weapon.damage - self.distraction + 5)
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "Bow":
                self.attack_points -= (weapon.damage - self.distraction)
                # wrong weapon can take til 50% from attack_points
        return self.attack_points
        
    def defend(self, armor):
        self.distraction = int(random(0,11)) # distraction can take til 100% from defence_points
        if armor:
            if armor == "Shield":
                self.defence_points += (armor.defence - self.distraction - 5)
                # wrong armor can take til 50% from defence_points
            elif armor == "Cloak":
                self.defence_points += (armor.defence - self.distraction - 5)
                # wrong armor can take til 50% from defence_points
            elif armor == "Helmet":
                self.defence_points += (armor.defence - self.distraction)
                # wrong armor can take til 50% from defence_points
        return self.defence_points
            
    def get_info(self):

        return f"Name: {self.name}, the Great\nHealth: {self.health}\nDamage: {((self.weapon).damage)}"
        


class Archer(Character):
    def __init__(self, name, health, weapon, armor=None):
        super().__init__(name, health)
        self.weapon = weapon
        self.armor = armor
        self.defence_points = 10
        self.attack_points = 10

    def attack(self, weapon):
        self.distraction = int(random(0,11)) # distraction can take til 100% from attack_points
        if weapon:
            if  weapon.skill == "Spell":
                self.attack_points += (weapon.damage - self.distraction - 5)
                # a proper weapon can add til 50% from attack_points
            elif weapon.skill == "Sword":
                self.attack_points += (weapon.damage - self.distraction + 4)
                # wrong weapon can take til 50% from attack_points
            elif weapon.skill == "Bow":
                self.attack_points += (weapon.damage - self.distraction + 10)
                # wrong weapon can take til 50% from attack_points
        return self.attack_points
    
    def defend(self, armor):
        self.distraction = int(random(0,11)) # distraction can take til 100% from defence_points
        if armor:
            if armor.skill == "Shield":
                self.defence_points += (armor.defence - self.distraction + 10)
                # wrong armor can take til 50% from defence_points
            if armor.skill == "Cloak":
                self.defence_points += (armor.defence - self.distraction + 3)
                # a proper armor can add til 50% from defence_points
            if armor.skill == "Helmet":
                self.defence_points += (armor.defence - self.distraction - 3)
                # wrong armor can take til 50% from defence_points
        return self.defence_points    
    
# So as we are have 5 characters we need to replace numbers with values
class Sword(Weapon):
    def __init__(self, name, damage, skill="Sword"):
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
    def __init__(self, name, damage=random.randint(60,70), skill="Bow"):
        super().__init__(name)
        self.name = name
        self.damage = damage
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(60,75)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(50,65)

class Stick(Weapon):
    def __init__(self, name, damage, skill="Spell"):
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
    def __init__(self, name, damage, skill="Sword"):
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
    def __init__(self, name, damage, skill="Sword"):
        super().__init__(name)
        self.name = name
        self.damage = damage + random.randint(55,91)
        skill = skill

    def aim(self, hit):
        if hit == 1 or hit == 2:
            self.damage = random.randint(55,91)
        elif hit == 3 or hit == 4 or hit == 5:
            self.damage = random.randint(35,70)
        
