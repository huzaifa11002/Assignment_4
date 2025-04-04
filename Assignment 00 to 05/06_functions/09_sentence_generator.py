# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and,
# depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

def make_sentence(word: str, part_of_speech: int) -> str:
    if part_of_speech == 1:
        return f"The {word} jumped over the fence."
    elif part_of_speech == 2:
        return f"I love to {word} every morning."
    elif part_of_speech == 3:
        return f"This is a very {word} day."
    else:
        return "Invalid part of speech."

def main():
    word = input("Enter a word: ")
    print("Choose a part of speech: 1 (noun), 2 (verb), or 3 (adjective)")
    part_of_speech = int(input("Enter the part of speech (1, 2, or 3): "))
    sentence = make_sentence(word, part_of_speech)
    print(sentence)

if __name__ == "__main__":
  main()