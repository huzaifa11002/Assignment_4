from random import randint

def computer_guess(x):
  low = 1
  high = x
  answer : str = ''

  while answer != 'c':
    if low != high:
      guess_num : int = randint(low,high)
    else:
      guess_num = low
    
    answer :str = str(input(f"Is {guess_num} too Low(L), too High(H), or Correct(C). ")).lower()

    if answer == "h":
      high = guess_num - 1
    elif answer == "l":
      low = guess_num + 1
  
  print("\nCongrats!!! Your guess is correct.")

def main():
  computer_guess(100)

if __name__ == "__main__":
  main()
