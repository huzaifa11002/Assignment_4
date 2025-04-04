# Simulate rolling two dice, three times. Prints the results of each die roll. 
# This program is used to show how variable scope works.

import random

diceNumber = 6

def dice_simulator():
    dice1 = random.randint(1, diceNumber)
    dice2 = random.randint(1, diceNumber)
    total = dice1 + dice2
    print(f"Total: {total}")

def main():
    diceNumber = 10
    dice_simulator()
    dice_simulator()
    dice_simulator()
    print(f"diceNumber: {diceNumber}")

if __name__ == "__main__":
    main()
    
