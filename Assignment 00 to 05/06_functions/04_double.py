# Fill out the double(num) function to return the result of multiplying num by 2. 
# We've written a main() function for you which asks the user for a number, 
# calls your code for double(num) , and prints the result.

def double_it(num):
  user_val = num * 2

  return user_val

def main():
  user_input = int(input("Enter the value "))
  print("Here is your value " + str(double_it(user_input)))

if __name__ == "__main__":
  main()