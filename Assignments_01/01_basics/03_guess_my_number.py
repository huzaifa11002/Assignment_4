# Guess My Number

import random

def main():
  guessing_number:int = random.randint(1,99)

  while True:
    guessed_number:int = int(input("Enter the guessing number between (1-99)"))
    if guessed_number > guessing_number:
      print("Your Guessed number is too High")
    elif guessed_number < guessing_number:
      print("Your Guessed number is too Low")
    else:
      print("Congrats!!! Your Guessed number is Correct...")
      break

if __name__ == "__main__":
  main()