# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. 
# It will repeat that process until the value is 100 or greater.

max_value = 100

def main():
  user_input :int = int(input("Enter the value of you want to double it ")) 

  while user_input < max_value:
    user_input = user_input * 2
    print(user_input)
    
if __name__ == "__main__":
  main()