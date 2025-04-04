# Implement the following function which takes in 3 integers as parameters:

def in_range(n: int, low: int, high: int) -> bool:
    if n >= low and n <= high:
      return True
    else:
      return False

print(in_range(10,1,10))