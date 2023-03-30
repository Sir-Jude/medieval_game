# Python imports
from abc import ABC, abstractmethod
from time import sleep
from os import system
import random
# Custom imports
import weapons
import armors
from characters import Character, character_factory
import boss

system("clear")
print("Welcome, heros!")
print("You are on the quest to defeat the great and powerful Markus, the Master of Python!")

fighters = []

# MENU
for num in range(0, 3):
    fighters.append(character_factory())
    fighters[num].get_name(num+1)
    fighters[num].get_class()
    fighters[num].get_weapon()
    fighters[num].get_armor()

    print(f"Thank you {fighters[num].name} the {fighters[num].person} for your enlistment!")
    sleep(1)
    system("clear")
    if len(fighters) < 3:
        print(f"Now we have {len(fighters)} heroes enlisted:\n")
        for fighter in fighters:    
            print(fighter)
        print(f"\nWe need {3-len(fighters)} more heroes...")

# The list of fighter
enemy = boss.FinalBoss()
system("clear")
print("So we have...\n")
for fighter in fighters:    
    print(fighter)
    sleep(0.5)
sleep(0.3)
print("\n VS\n")
print(enemy)
input("\nAre you ready for battle ")
system("clear")

# Arena/battle engine
battle = True
turn = 0
print ("Let the fighting begin!\n")

while battle == True:
    if len(fighters) == 0: # Sopping the game if there are no more fighters left
        print("All Heroes are dead!\nMarkus the Beast kill you all!")
        break

    input("Are you ready for next turn? ")

    # Game turn
    turn += 1
    print(f"\n   --------------- Round {turn}: ---------------\n")

    # Character's turn
    for fighter in fighters:
        def_power = enemy.defend()
        att_power = fighter.attack()
        if (def_power - att_power) > 0:
            damage = 0
        else:
            damage = def_power - att_power
        print(f"{fighter.name} ({fighter.health}hp) attacks {enemy.name} with his {fighter.weapon.name}({att_power}).")
        print(f"{enemy.name} the Beast lost {damage} hp, and now has {enemy.health+damage}hp left.")
        enemy.health = enemy.health + damage
        sleep(0.5)

    # Checking if the boss is dead.
    if enemy.health <= 0:
        print("The heroes won!")
        break

    # Boss turn
    print()
    fighter = fighters[random.randint(0, len(fighters)-1)] # Random victim chose 
    def_power = fighter.defend()
    att_power = enemy.attack()
    if (def_power - att_power) > 0:
            damage = 0
    else:
        damage = def_power - att_power
    print(f"{enemy.name} ({enemy.health}hp) attacks {fighter.name} with his Krav Maga and brute force ({att_power}).")
    print(f"{fighter.name} the {fighter.person} lost {damage} hp and now has {fighter.health+damage} hp.")
    fighter.health = fighter.health + damage

    # Checking if someone is dead.
    if fighter.health <= 0:
        print(f"\n{fighter.name} the {fighter.person} is dead!")
        fighters.remove(fighter) # Removing the dead fighter from the list
    print()