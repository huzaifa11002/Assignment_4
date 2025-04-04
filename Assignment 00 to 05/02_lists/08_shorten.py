# Fill out the function shorten(lst) which removes elements from the end of lst, 
# which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written 
# a main() function for you which gets a list and passes it into your function once you run 
# the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free 
# to change it around to test your program.


MAX_LENGTH = 3

def shorten(my_list):
  while len(my_list) > MAX_LENGTH:
    print(f"You are exceed your list elements, here is your remove element '{my_list.pop()}'")

def elements():
  element = input("Please type your value to add in your list ")
  my_list = []

  while element != "":
    my_list.append(element)
    element = input("You want to add more and skip for blank input ")
  
  return my_list

def main():
  my_list = elements()
  shorten(my_list)