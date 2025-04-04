# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. 
# The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

def ones_digit(num:int):
    ones_digit = num % 10
    print("The ones digit is", ones_digit)

def main():
    user_input :int = int(input("Enter the number "))
    ones_digit(user_input)

if __name__ == "__main__":
    main()