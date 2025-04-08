from random import randint

def user_guess(x):
  random_num :int = randint(1,x)
  guess_number : int = 0
  while guess_number != random_num:
    guess_number:int = int(input(f"Enter the guess number between (1-{x}) "))
    if guess_number < random_num:
      print("Aww, your guess is incorrect. This is Low!")
    elif guess_number > random_num:
      print("Aww, your guess is incorrect. This is High!")
  
  print("Congrats!!! Your guess is correct.")

def main():
  user_guess(10)

if __name__ == "__main__":
  main()