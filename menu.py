from abc import ABC, abstractmethod
import random
from time import sleep
import weapons
import armors
import characters
from os import system

print("Welcome, heros!")
print("You are on the quest to defeat the grat and powerful Markus, the Master of Python!\n")
fighters = []
# MENU
for i in range(0, 3):
    if i == 0:
        fighter_name = input("You, which is your name? ").title()
    elif i == 1:
        fighter_name = input("And you, which is your name? ").title()
    else:
        fighter_name = input("And finally you, how are you known? ").title()
    
    fighter_person = input(
        """
    And what are you?
    [1] warrior
    [2] magician
    [3] archer
    [4] smith
    -> """
    )
    if fighter_person == "1":
        fighter_person = "warrior"
    elif fighter_person == "2":
        fighter_person = "magician"
    elif fighter_person == "3":
        fighter_person = "archer"
    else:
        fighter_person = "smith"
    input(f"Mhm...a {fighter_person}...\n(Press Enter to continue)")
    system("clear")

    fighter_weapon = input(
        """
    What are you going to fight with?
    [1] sword
    [2] axe
    [3] stick
    [4] wand
    [5] spear
    [6] bow
    -> """
    )
    if fighter_weapon == "1":
        fighter_weapon = "sword"
    elif fighter_weapon == "2":
        fighter_weapon = "axe"
    elif fighter_weapon == "3":
        fighter_weapon = "stick"
    elif fighter_weapon == "4":
        fighter_weapon = "wand"
    elif fighter_weapon == "5":
        fighter_weapon = "spear"
    else:
        fighter_weapon = "bow"
    input("Press Enter to continue")
    system("clear")

    fighter_armor = input(
        """
    And finally, what are you using to defend yourself?
    [1] cloak
    [2] helmet
    [3] round shield
    [4] roman shield
    [5] leather armor
    [6] metal armor
    -> """
    )
    if fighter_armor == "1":
        fighter_armor = "cloak"
    elif fighter_armor == "2":
        fighter_armor = "helmet"
    elif fighter_armor == "3":
        fighter_armor = "round shield"
    elif fighter_armor == "4":
        fighter_armor = "roman shield"
    elif fighter_armor == "5":
        fighter_armor = "leather armor"
    else:
        fighter_armor = "metal armor"
    fighters.append(
        characters.character_factory(
            fighter_person, fighter_name, fighter_weapon, fighter_armor
        )
    )
    input("Press Enter to continue")
    system("clear")

print(fighters)

"""# The saved list of fighters as objects
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
    battle = False"""
