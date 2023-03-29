from abc import ABC, abstractmethod
import random
from time import sleep
import weapon
import armor
import character



# The saved list of fighters as objects
fighters = ["bob","bibi","mark"]

# Arena/battle engine
battle = True
while battle == True:
    # Game turn
    for person in fighters:
        # Character turn
        char_index = fighters.index(person)
        # Chose an enemy from the remains characters
        enemy = random.choice([e for e in fighters if fighters.index(e) != char_index])
        # Atack the enemy
        enemy.health = enemy.defend() - person.atack()
    battle = False

