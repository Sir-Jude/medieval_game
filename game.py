# Python imports
from abc import ABC, abstractmethod
from time import sleep
from os import system
import random
# Custom imports
import weapons
import armors
import characters
import boss

system("clear")
print("Welcome, heros!")
print("You are on the quest to defeat the great and powerful Markus, the Master of Python!")

fighters = []
# MENU
for i in range(1, 4):
    if i == 1:
        fighter_name = input("You, what is your name? ").title()
    elif i == 2:
        fighter_name = input("And you there, which is your name? ").title()
    else:
        fighter_name = input("And finally you, how are you known? ").title()

    fighter_person = input(
        f"""
And what are you {fighter_name}?
[1] Warrior
[2] Magician
[3] Archer
[4] Smith
-> """
    )
    if fighter_person == "1":
        fighter_person = "Warrior"
    elif fighter_person == "2":
        fighter_person = "Magician"
    elif fighter_person == "3":
        fighter_person = "Archer"
    elif fighter_person == "4":
        fighter_person = "Smith"
    system("clear")

    fighter_weapon = input(
        f"""
{fighter_name} the {fighter_person}, what are you going to fight with?
[1] Sword
[2] Axe
[3] Stick
[4] Wand
[5] Spear
[6] Bow
-> """
    )
    if fighter_weapon == "1":
        fighter_weapon = "Sword"
    elif fighter_weapon == "2":
        fighter_weapon = "Axe"
    elif fighter_weapon == "3":
        fighter_weapon = "Stick"
    elif fighter_weapon == "4":
        fighter_weapon = "Wand"
    elif fighter_weapon == "5":
        fighter_weapon = "Spear"
    elif fighter_weapon == "6":
        fighter_weapon = "Bow"
    system("clear")

    fighter_armor = input(
        f"""
{fighter_name} the {fighter_person}, you have just a {fighter_weapon}.
How do you plan to defend yourself {fighter_name}?
[1] Cloak
[2] Helmet
[3] Round shield
[4] Roman shield
[5] Leather armor
[6] Metal armor
-> """
    )
    if fighter_armor == "1":
        fighter_armor = "Cloak"
    elif fighter_armor == "2":
        fighter_armor = "Helmet"
    elif fighter_armor == "3":
        fighter_armor = "Round Shield"
    elif fighter_armor == "4":
        fighter_armor = "Roman Shield"
    elif fighter_armor == "5":
        fighter_armor = "Leather Armor"
    elif fighter_armor == "6":
        fighter_armor = "Metal Armor"
    

    fighters.append(characters.character_factory(
            fighter_person,
            fighter_name,
            fighter_weapon,
            fighter_armor
        ))

    print(f"Thank you {fighter_name} the {fighter_person} for your enlistment!")
    sleep(1)
    system("clear")
    if len(fighters) < 3:
        print(f"Now we have {len(fighters)} heroes enlisted:\n")
        for fighter in fighters:    
            print(fighter)
        print(f"\nWe need {3-len(fighters)} more heroes...")

# The list of fighter
system("clear")
print("So we have...\n")
for fighter in fighters:    
    print(fighter)
    sleep(0.5)
input("\nAre you ready to face Markus the Beast, Master of Python? ") 
system("clear")

# Arena/battle engine
enemy = boss.FinalBoss()
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
        battle = False

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