from random import choice

def game():
  guess_value = ["r" , "p", "s"]
  bot = choice(guess_value)
  user_input : str = str(input("Enter your choice Rock(R), Paper(P), and Scissor(S) "))

  if user_input == bot:
    return "Tie..."
  
  if winner(user_input, bot):
    return "You Won!!"

  return "You Lose..."

def winner(user_input, bot):

  if (user_input == "r" and bot == "s") or (user_input == "p" and bot == "r") or (user_input == "s" and bot == "p"):
    return True

  return False

def main():
  print(game())

if __name__ == "__main__":
  main()