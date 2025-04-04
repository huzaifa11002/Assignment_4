# Write a program to print terms in the Fibonacci sequence up to a maximum value.

max_term = 100

def main():
  curr_term = 0
  next_term = 1

  while curr_term <= max_term:
    print(curr_term)
    sum_of_terms = curr_term + next_term
    curr_term = next_term
    next_term = sum_of_terms

if __name__ == "__main__":
  main()