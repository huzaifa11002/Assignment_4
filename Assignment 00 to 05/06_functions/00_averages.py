# Write a function that takes two numbers and finds the average between the two.

def average(val1:float, val2:float):
  
  sum = val1 + val2
  return sum / 2

def main():

  avg1 : float = average(0,10)
  avg2 : float = average(5,10)
  average_value : float = average(avg1, avg2)

  print(f"First Average Value is {avg1}")
  print(f"Second Average Value is {avg2}")
  print(f"Total Average Value is {average_value}")

if __name__ == "__main__":
  main() 