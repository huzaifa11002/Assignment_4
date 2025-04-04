# Fill out the function count_even(List)

def list_of_int():

  num_list = []
  user_input = input("Enter the number or press enter to stop it ")
  while user_input != "":
    num_list.append(int(user_input))
    user_input = input("Enter the next number or press enter to stop it ")
  
  return num_list

def count_even(num_list):
  count = 0
  for i in range(len(num_list)):
    num = num_list[i]
    if num % 2 == 0:
      count += 1

  print(count) 

def main():
  
  num_list: list = list_of_int()
  count_even(num_list)

if __name__ == "__main__":
  main()