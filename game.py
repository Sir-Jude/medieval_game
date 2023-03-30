# Python imports
from time import sleep
from os import system
# Custom imports
from characters import character_factory
from boss import FinalBoss
from turns import HeroTurn, BossTurn
#image
from image import start, heroes_won, game_over

system("clear")
print(start)
sleep(2.5)
system("clear")
print("Welcome, heros!")
print("You are on the quest to defeat the great and powerful Markus, the Master of Python!")
print()
fighters = []

# MENU
for num in range(0, 3):
    fighters.append(character_factory())
    fighters[num].get_name(num+1)
    fighters[num].get_class()
    fighters[num].get_weapon()
    fighters[num].get_armor()

    print(f"\nThank you {fighters[num].name} the {fighters[num].person} for your enlistment!")
    sleep(1)
    system("clear")
    if len(fighters) < 3:
        print(f"Now we have {len(fighters)} heroes enlisted:\n")
        for fighter in fighters:    
            print(fighter)
        if len(fighters) == 2:
            print(f"\nWe need one last hero...")
        else:
            print(f"\nWe need {3-len(fighters)} more heroes...")

# The list of fighter
enemy = FinalBoss()
system("clear")
print("So we have...\n")
for fighter in fighters:    
    print(fighter)
    sleep(1)
print("      VS\n")
sleep(0.5)
print(enemy)
# input("\nAre you ready for battle? ")
# system("clear")

# Arena/battle engine
battle = True
turn = 0
print ("\nLet the fighting begin!\n")
sleep(1)
system("clear")

while battle == True:
    # Game turn
    turn += 1
    print(f"\n   --------------- Round {turn}: ---------------\n")

    # Character's turn
    hero_turn = HeroTurn(fighters)
    for fighter in fighters:
        hero_turn.hero_result(enemy.defend(), fighter.attack(), enemy, fighter)

    # Checking if the boss is dead.
    if enemy.health <= 0:
        print(heroes_won)
        break

    print()
    # Boss turn
    boss_turn = BossTurn(fighters)
    boss_turn.boss_result(fighter.defend(), enemy.attack(), enemy)

    # Checking if someone is dead.
    for fighter in fighters:
        if fighter.health <= 0:
            print(f"\n{fighter.name} the {fighter.person} is dead!")
            fighters.remove(fighter) # Removing the dead fighter from the list
        print()
    
    if len(fighters) == 0: # Sopping the game if there are no more fighters left
        print("All Heroes are dead!\nMarkus the Beast kill you all!")
        sleep(2.5)
        print(game_over)
        input()
        break
    
    input("Are you ready for next turn? ")
    system("clear")
    