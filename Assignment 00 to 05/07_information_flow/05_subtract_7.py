# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function!

def subtract_seven(num: int) -> int:
    return num - 7

def main():
    num = 7
    result = subtract_seven(num)
    print("this should be zero: ", result)


if __name__ == "__main__":
    main()