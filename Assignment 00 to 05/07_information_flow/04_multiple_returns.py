# There are times where you are working with lots of different data within a function that you want to return. While generally, 
# we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

def user_info(name: str, age: int) -> tuple[str, int]:
    return name, age

def main():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    info = user_info(user_name, user_age)
    print(info)

if __name__ == "__main__":
    main()