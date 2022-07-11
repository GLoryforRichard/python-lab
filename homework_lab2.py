"""
Student Number: 101370671
Sample Coding Questions 02 Week 01
First Name: Binye
Last Name: Liu
"""

# Q1 weapons array
from random import random, randrange
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Q2 Roll the dice (1-6) to choose which weapon
weaponRoll = randrange(0, 6)
print("You roll the weapon : {}".format(weapons[weaponRoll]))

# Q3&4  Evaluate weapons
if(weaponRoll != 0):
    print("Thank goodness you didn't roll the Fist...")
    if(weaponRoll <= 4):
        if(weaponRoll <= 2):
            print("You rolled a weak weapon, friend")
        else:
            print("Your weapon is meh")
    else:
        print("Nice weapon, friend!")
else:
    print("You roll the Fist...")
