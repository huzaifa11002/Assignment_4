# In the information flow lesson, we discussed using a variable storing a number as an example of scope. 
# We saw that changes we made to the number inside a function did not stay unless we returned it. 
# This is true for what we call immutable data types which include things like numbers and strings.


def three_copies(lists, data):
  for i in range(3):
    lists.append(data)

def main():
  user_data = input("Enter the message you want to copy")
  lists = []
  print("Before Run copy function" , lists)
  three_copies(lists, user_data)
  print("After Run copy function", lists)

if __name__ == "__main__":
  main()