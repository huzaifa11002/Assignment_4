# Ask the user for two numbers, one at a time, and then print the result of dividing 
# the first number by the second and also the remainder of the division.

def main():
  divider:int =int(input("Enter the Divide number into an integer: "))
  divide_by:int = int(input("Enter the Divide by number into an integer: "))

  divided_value = divider // divide_by
  reminder = divider % divide_by

  print(f"{divider} ÷ {divide_by} = {divided_value} and the reminder is {reminder}")

if __name__ == "__main__":
  main()