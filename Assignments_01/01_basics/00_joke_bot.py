# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

question = "What do you want?"
joke = """
Customer: Brother, this shampoo says "gives volume"... does it really work?

Shopkeeper: Absolutely, sir! Use it once — your hair will have so much volume, even WiFi signals won’t reach through it!

Customer (trying not to laugh): Alright, give me the conditioner too.

Shopkeeper: Conditioner is free, sir — but on one condition...

Customer: What’s the condition?

Shopkeeper: After using the shampoo, to reduce the volume, you'll also need our Bluetooth-enabled comb!

"""

sorry = "I m only tell a joke"

def main():
  print(question)

  user_input = str(input("Type joke")).lower().strip()

  if "joke" in user_input:
    print(joke)
  
  else:
    print(sorry)

if __name__ == "__main__":
  main()