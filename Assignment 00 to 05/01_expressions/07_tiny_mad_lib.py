# Write a program which prompts the user for an adjective, then a noun, then a verb, 
# and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words 
# are eventually filled into the blanks of a word template to make an entertaining story! 
# We've provided you with the beginning of a sentence (the SENTENCE_START constant) '
# 'which will end in a user-inputted adjective, noun, and then verb.


def main():
  print("Make a story with your inputs")
  adjective :str = str(input("Enter the adjective "))
  noun : str = str(input("Enter the Noun "))
  verb : str = str(input("Enter the Verb "))

  print(f"""I had the weirdest day! I was walking down the street when suddenly, I saw..." {adjective} {noun} {verb}!""")
  
if __name__ == "__main__":
  main()