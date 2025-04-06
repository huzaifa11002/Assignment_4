from random import randint

def main():
  score = 0
  print("\nWelcome to High-Low Game!")
  print("---------------------------")

  for i in range(5):
    print(f"Round {i+1}!!")

    user_number : int = randint(1,100)
    computer_number : int =  randint(1,100)

    print(f"This is your number {user_number}")
    user_input : str = str(input("Would you think about your number lower or higher than computer number? (type[lower or higher]) ")).lower().strip()

    while user_input != "higher" and user_input != "lower":
      user_input : str = str(input("Please enter either higher or lower ")).lower().strip()

    if (user_input == "lower" and user_number > computer_number) or (user_input == "higher" and user_number < computer_number):
      print(f"Congrats!!! Your Guess is Right... Computer number is {computer_number}")
      score +=1
      print(f"Your score is {score}\n")

    else:
      print(f"Aww, that's incorrect. Computer number is {computer_number}")
      print(f"Your score is {score}\n")
  
  if score == 5:
    print("Wow! You played perfectly!")
  elif score // 2:
    print("Good job, you played really well!")
  else:
    print("Better luck next time!")


if __name__ == "__main__":
  main()