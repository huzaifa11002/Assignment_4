# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the 
# third side (the hypotenuse) using the Pythagorean theorem!


from math import sqrt

def main():
  ab : float = float(input("Enter the length of AB"))
  ac : float = float(input("Enter the length of AC"))
  bc : float = sqrt(ab**2 + ac**2)
  print(bc)

if __name__ == "__main__":
  main()