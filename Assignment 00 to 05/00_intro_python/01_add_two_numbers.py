# Write a Python program that takes two integer inputs from the user 
# and calculates their sum. The program should perform the following tasks:

# 1. Prompt the user to enter the first number.
# 2. Read the input and convert it to an integer.
# 3. Prompt the user to enter the second number.
# 4. Read the input and convert it to an integer.
# 5. Calculate the sum of the two numbers.
# 6. Print the total sum with an appropriate message.

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    sum = num1 + num2

    print("The sum of the two numbers is: ", sum)

if __name__ == "__main__":
    main()