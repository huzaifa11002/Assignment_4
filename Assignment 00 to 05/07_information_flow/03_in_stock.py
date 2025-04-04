# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter 
# and returns how many of that fruit are in her inventory. Write code in main() which will:

def num_in_stock(fruit: str) -> int:
    if fruit == "apple":
        return 5
    elif fruit == "banana":
        return 10
    elif fruit == "orange":
        return 8
    else:
        return 0
    
def main():
    fruit = input("Enter the name of the fruit: ").lower()
    quantity = num_in_stock(fruit)
    print(f"There are {quantity} {fruit}s in stock.")

if __name__ == "__main__":
    main()