from abc import ABC, abstractmethod
import random
from time import sleep
import weapons
import armors
import characters
import boss
from os import system

fighters = []
system("clear")
# MENU
for i in range(0,3):
    fighter_name  = input(f"Name of character {i+1}: ")
    fighter_person  = input("""
    Chose a character type:
    [1] warrior
    [2] magician
    [3] archer
    [4] smith
    -> """)
    if fighter_person == "1":
        fighter_person = "warrior"
    elif fighter_person == "2":
        fighter_person = "magician"
    elif fighter_person == "3":
        fighter_person = "archer"
    else:
        fighter_person = "smith"
    fighter_weapon  = input("""
    Chose the weapon:
    [1] sword
    [2] axe
    [3] stick
    [4] wand
    [5] spear
    [6] bow
    -> """)
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
    fighter_armor  = input("""
    Chose the armor:
    [1] cloak
    [2] helmet
    [3] round shield
    [4] roman shield
    [5] leather armor
    [6] metal armor
    -> """)
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
    fighters.append(characters.character_factory(fighter_person, fighter_name, fighter_weapon, fighter_armor))
    system("clear")

enemy = boss.FinalBoss()

# Arena/battle engine
battle = True
turn = 0
while battle == True:
    # Game turn
    turn += 1
    print(f"Game tun {turn}:")
    for person in fighters:
        # Character turn
        print("Before:",person.name, person.health, "- Boss", enemy.health)
        enemy.health = enemy.health + enemy.defend() - person.attack()
        print("After attack:",person.name, person.health, "- Boss", enemy.health)
        print()
    # Boss turn
    # Boss chose one victim
    person  = fighters[random.randint(0, len(fighters))]
    person.health = person.health + person.defend() - enemy.attack()
    print("After Boss attack:",person.name, person.health, "- Boss", enemy.health)
    print()

