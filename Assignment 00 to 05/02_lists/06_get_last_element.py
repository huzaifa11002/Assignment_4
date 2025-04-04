# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and 
# prints the last element in the list. The list is guaranteed to be non-empty, 
# but there are no guarantees on its length.


def last_element(my_list):
  length_of_list = len(my_list)
  index_find = length_of_list - 1
  print(my_list[index_find])

def elements():
  element = input("Please type your value to add in your list ")
  my_list = []

  while element != "":
    my_list.append(element)
    element = input("You want to add more and skip for blank input ")
  
  return my_list

def main():
  my_list = elements()
  last_element(my_list)


if __name__ == "__main__":
  main()