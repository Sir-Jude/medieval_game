# Python imports
from time import sleep
from os import system
import vlc
# Custom imports
from characters import character_factory
from boss import FinalBoss
from turns import HeroTurn, BossTurn
#image
from image import start, heroes_won, game_over

system("clear")
player = vlc.MediaPlayer("start.mp3")
player.play()
print(start)
input("ENTER ")
system("clear")
print("Welcome, heros!")
print("You are on the quest to defeat the great and powerful Markus, the Master of Python!\n")
fighters = []

# MENU
for num in range(0, 3):
    fighters.append(character_factory())
    fighters[num].get_name(num+1)
    fighters[num].get_class()
    fighters[num].get_weapon()
    fighters[num].get_armor()

    print(f"\nThank you {fighters[num].name} the {fighters[num].person} for your bravery!")
    sleep(1)
    system("clear")
    if len(fighters) < 3:
        print(f"Ok, now we have {len(fighters)} heroes enlisted:\n")
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
print("\n                           VS\n")
sleep(1)
print(enemy)

# Arena/battle engine
battle = True
turn = 0
player.stop()
print ("\nLet the fighting begin!\n")
player = vlc.MediaPlayer("battle.mp3")
player.play()
input("ENTER ")
system("clear")

while battle == True:
    # Game turn
    turn += 1
    print(f"\n   --------------- Round {turn}: ---------------\n")

    # Character's turn
    hero_turn = HeroTurn(fighters)
    for fighter in fighters:
        print(f"[{fighters.index(fighter)+1}] {fighter.name} - {fighter.health}hp")
    while True:
        fighter_choice = int(input("-> "))
        if fighter_choice in [i for i in range(1,len(fighters)+1)]:
            fighter = fighters[fighter_choice-1]
            break
        else:
            print(f"You must enter a number between 1 and {len(fighters)+1}")
    hero_turn = HeroTurn(fighter, enemy)
    hero_turn.hero_result()

    # Checking if the boss is dead.
    if enemy.health <= 0:
        player.stop()
        print("\nMarkus the Beast is dead!\nThe heroes has won!")
        input("ENTER ")
        system("clear")
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
        player.stop()
        print("\nAll Heroes are dead!\nMarkus the Beast has killed you all!")
        input("ENTER ")
        system("clear")
        player = vlc.MediaPlayer("game_over.mp3")
        player.play()
        print(game_over)
        input("ENTER ")
        player.stop()
        break
    
    input("Are you ready for next turn? ")
    system("clear")
    