# There's a small fruit shop nearby your house that you like to buy from. 
# Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. 
# Luckily you wrote down what fruits were available and how much one of each fruit costs.

def main():
  fruits: dict =  {"Apple":1.2, "Mango":2, "Kiwi" : 3, "Watermeolon": 5 }
  total_amount:float = 0
  for fruit in fruits:
    price = fruits[fruit]
    quantity = int(input(f"Enter a quantity of {fruit} do you want to buy? "))
    total_amount += (price * quantity)

  print(f"Total Amount of yours fruits is ${total_amount:.2f}")

if __name__ == "__main__":
  main()