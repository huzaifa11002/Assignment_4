# This program counts the number of times each number appears in a list. 
# It uses a dictionary to keep track of the information.

def user_inputs():
    """
    Get user input and save in List
    
    """
    num_list : list = []
    while True:
        user = input("Enter a number or skip for blank input ")

        if user == "":
            break
    
        num = int(user)
        num_list.append(num)
    return num_list

def count_appear(input_list):
  """
  Count the number of times each number appears in the list
  
  """
  num_dict = {}

  for num in input_list:
    if num not in num_dict:
      num_dict[num] = 1
    else:
      num_dict[num] += 1
  
  return num_dict

def num_print(num_dict):
  """
  Print the number of times each number appears in the list
  
  """
  print("")
  for num in num_dict:
    print(f"{num} appear {num_dict[num]} times")

def main():

  user_input : list = user_inputs()
  num_dict = count_appear(user_input)
  num_print(num_dict)

if __name__ == "__main__":
  main()