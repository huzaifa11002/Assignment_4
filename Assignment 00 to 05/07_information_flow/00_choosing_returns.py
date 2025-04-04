# There are times where we want to return different things from a function based on some condition. To practice this idea, 
# imagine that we want to check if someone is an adult. We might check their age and return different 
# things depending on how old they are!

def check_age(age)-> str:
    if age >= 18:
        return "You are Adult"
    else:
        return "You are Minor"

def main():
    user_age = int(input("Enter your age: "))
    result = check_age(user_age)
    print(result)

if __name__ == "__main__":
    main()