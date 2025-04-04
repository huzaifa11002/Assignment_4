# Write a program which asks a user for their age and lets them know 
# if they can or can't vote in the following three fictional countries.

Peturksbouipo = 16
Stanlau = 25
Mayengua = 48

def main():
  user_age : int = int(input("Enter your age "))

  if user_age >= Peturksbouipo:
    print("You are eligible of voting in Peturksbouipo.")
  else:
    print("You are not eligible of voting in Peturksbouipo because your age less than 16.")
  if user_age >= Stanlau:
    print("You are eligible of voting in Stanlau.")
  else:
    print("You are not eligible of voting in Stanlau because your age less than 25.")
  if user_age >= Mayengua:
    print("You are eligible of voting in Mayengua.")
  else:
    print("You are not eligible of voting in Mayengua because your age less than 48.")

if __name__ == "__main__":
  main()