from random_word import RandomWords

def hangman():
  words = RandomWords()

  word = words.get_random_word()
  letters = set(word)
  used_alphabets = set()
  attempts = 7
  print("\nLets Play Hangman Game...!")
  print("--------------------------\n")

  while len(letters) > 0 and attempts > 0:

    print("Remaining Attempts" , attempts)
    print("Used Letters", ','.join(sorted(used_alphabets)))

    word_list = [letter if letter in used_alphabets else '_' for letter in word]
    print("Current Word" , ' '.join(word_list))

    user_letter = input("\nEnter the letter ").lower()
    if len(user_letter) != 1 or not user_letter.isalpha():
      print("Please enter a valid letter")
      continue

    if user_letter in used_alphabets:
      print("You are already used. Please try new letter.")
      continue

    used_alphabets.add(user_letter)

    if user_letter in letters:
      letters.remove(user_letter)
    else:
      attempts -= 1

  if attempts == 0:
    print("You Lost the game. Actuall Word is", word)
  else:
    print("Congrats!! You Won. You guessed right word", word)


def main():
  hangman()

if __name__ == "__main__":
  main()
