import random
import string

def generate_password(char):
  punctuations = ["!","@","#","$","%","&"]
  password = string.ascii_letters + string.digits + ''.join(punctuations)

  return ''.join(random.choice(password) for _ in range(char))

def main():
  user_input = int(input("Enter the length of the password "))
  generated = generate_password(user_input)
  print(f"Generated Password : {generated}")

if __name__ == "__main__":
  main()
  