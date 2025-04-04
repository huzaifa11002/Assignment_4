# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors 
# (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). 
#  Don't forget to call your function in main()!

def divisor_num(num:int):
  print("Here are the divisors of", num)
  for i in range(num):
    curr_val = i + 1
    if num % curr_val == 0:
      print(curr_val)

def main():
  user_input :int = int(input("Enter the number "))
  divisor_num(user_input) 

if __name__ == "__main__":
  main()