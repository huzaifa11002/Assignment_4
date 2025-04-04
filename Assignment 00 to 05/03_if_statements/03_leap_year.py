# Write a program that reads a year from the user and tells 
# whether a given year is a leap year or not.

def main():
  user_input = int(input("Enter a year "))

  if user_input % 4 == 0:
      if user_input % 100 == 0:
          if user_input % 400 == 0:
            print(f"{user_input} is a Leap Year")
          else:
            print(f"{user_input} is not a Leap Year")
      else:
        print(f"{user_input} is a Leap Year")
  else:
        print(f"{user_input} is not a Leap Year")
  
if __name__ == "__main__":
  main()
