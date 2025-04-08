def user_inputs():
  name:str = str(input("Enter the name of Super Hero ")).capitalize()
  color:str = str(input("Enter the color name "))
  object_name:str = str(input("Enter the object name "))
  food:str = str(input("Enter the food name "))
  animal:str = str(input("Enter the animal name "))
  print("Our story make more interesting 😆")
  cloth:str = str(input("Enter the silly cloth name "))
  place:str = str(input("Enter the place name ")).capitalize()
  noun:str = str(input("Enter the plural noun "))
  vehicle:str = str(input("Enter the vehicle name ")).capitalize()
  print("😆😆 One More!!")
  random_word:str = str(input("Enter the random exclaimed word[ex:What the Hell, Ohh Shit!] ")).capitalize()

  return name, color, object_name, food, animal, cloth, place, noun, vehicle, random_word 

def madlib(name, color, object_name, food, animal, cloth, place, noun, vehicle, random_word):
  print(f"""
“A Day as a Superhero 🦸‍♂️”

One morning, {name} woke up to find a {color} {object_name} stuck to their hand. At first, they thought it was from a dream about eating {food}, but nope — it was real!

Suddenly, a {animal} burst into the room wearing sunglasses and shouted,
“{name}, you are now a superhero!”

{name} blinked twice and said, “Did I eat expired {food} last night?”

But the animal wasn’t joking. It handed {name} a sparkly cape and a pair of {cloth}. “Your mission,” it said, “is to save {place} from an army of evil {noun}!”

Without hesitation, {name} jumped out the window, landed in a {vehicle}, and yelled, “To {place} we go!”

What happened next is classified… but it involved dancing pineapples, a kazoo, and someone shouting “{random_word}” very dramatically.
  """)

def main():
  print("\nMake your own Super Hero Funny Story")
  print("------------------------------------\n")
  print("You gave me only 10 inputs and I will ready your story\n")
  get_user_inputs = user_inputs()
  print("\nHere is your own stroy")
  print("------------------------\n")
  madlib(*get_user_inputs)


if __name__ == "__main__":
  main()