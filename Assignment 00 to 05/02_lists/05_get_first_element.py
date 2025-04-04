# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and 
# prints the first element in the list. The list is guaranteed to be non-empty. 
# We've written some code for you which prompts the user to input the list one element at a time.

def first_element(my_list):
  print(my_list[0])

def elements():
  element = input("Please type your value to add in your list ")
  my_list = []

  while element != "":
    my_list.append(element)
    element = input("You want to add more and skip for blank input ")
  
  return my_list

def main():
  my_list = elements()
  first_element(my_list)


if __name__ == "__main__":
  main()