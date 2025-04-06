def access_element(lst, index):
  return lst[index]

def modify_element(lst, index, new_element):
  lst[index] = new_element
  return lst

def slice_element(lst, start, end):
  return lst[start:end]

def index_game():
  friends = ["Ayyan" , "Zain" , "Hamy" , "Babar" , "Yashfain"]
  print("Now, your list is lookalike")
  print(friends)
  print()

  print("Would you like to perform in this list ('Access' , 'Modify' , 'Slice')")
  user_input = str(input()).lower()
  
  if user_input == "access":
    index_number = int(input("Please enter a index number")) 
    print(access_element(friends, index_number))
  
  elif user_input == "modify":
    new_value = input("Enter a new value")
    index_number = int(input("Enter a index number do you want to replace new value"))
    print(modify_element(friends, index_number, new_value))

  else:
    start_index = int(input("Please enter a start index number")) 
    end_index = int(input("Please enter a end index number"))
    print(slice_element(friends, start_index, end_index)) 

if __name__ == "__main__":
  index_game()