# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_numbers(numbers):

  sum_of_numbers:int = 0
  for number in numbers:
    sum_of_numbers += number
  
  return sum_of_numbers

def main():
  num : list[int] = list([8, 12, 26, 34, 41, 59, 63, 73, 85, 97])
  print(add_numbers(num))

if __name__ == "__main__":
  main()