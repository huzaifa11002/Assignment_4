# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.")'
# until they type it correctly. Sometimes, especially in the midst of such uncertain times,we just need to be reminded 
# that we are resilient, capable, and strong; this little Python program may be able to help!

affrimation : str = "I am capable of doing anything"

def main():
  print("Type this affrimation: " + affrimation)
  feedback = input()

  while feedback != affrimation:
    print("This is not affrimation")
    print()
    print("Please type the given affrimation: " + affrimation)
    feedback = input()
  
  print("Thats Right!")

if __name__ == "__main__":
  main()