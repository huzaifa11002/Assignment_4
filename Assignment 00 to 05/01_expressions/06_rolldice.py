#Simulate rolling two dice, and prints results of each roll as well as the total.

from random import randint

dice_length = 6   # 6 is the large number of dice

def main():
  dice1 : int = int(randint(1, dice_length))
  dice2 : int = int(randint(1, dice_length))
  total : int = int(dice1 + dice2)

  print(f"First Dice rolling is {dice1}")
  print(f"Second Dice rolling is {dice2}")
  print(f"Total Dices value is {total}")

if __name__ == "__main__":
  main()