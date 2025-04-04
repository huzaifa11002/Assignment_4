def main():
    element = input("Please type your value to add in your list ")
    my_list = []

    while element != "":
        my_list.append(element)
        element = input("You want to add more and skip for blank input ")

    print("Here is your List", my_list)

if __name__ == "__main__":
    main()