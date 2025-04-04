# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times
# to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

def message():
  message : str = str(input("Enter the message you want to print ")) 
  return message

def repeat_times():
  repeat_message : int = int(input("Enter the number you want to repeat message "))
  return repeat_message

def main():
  user_message = message()
  repeat_message = repeat_times()
  for _ in range(repeat_message):
    print(user_message)

if __name__ == "__main__":
  main()