# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def add_in_phonebook():
  """
  Add a name and number in phonebook.
  """
  phonebook = {}
  while True:
    name_input = input("Enter a name or skip for blank input ")
    if name_input == "":
      break
    else:
      number_input = input(f"Enter a number of {name_input} ")
      phonebook[name_input] = number_input

  return phonebook

def printing(phonebook):
  print("")
  for user_name in phonebook:
    print(f"{user_name} : {phonebook[user_name]}")

def search_number(phonebook):
  while True:
    search_input = input("Enter a name you want to find a number ")
    if search_input == "":
      break
    elif search_input not in phonebook:
      print(f"{search_input} not in your phonebook ")
    else:
      print(phonebook[search_input])

def main():
  phonebook = add_in_phonebook()
  printing(phonebook)
  search_number(phonebook)

if __name__ == "__main__":
  main()