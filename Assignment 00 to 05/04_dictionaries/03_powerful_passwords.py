# You want to be safe online and use different passwords for different websites. 
# However, you are forgetful at times and want to make a program that can match 
# which password belongs to which website without storing the actual password!

from hashlib import sha256

def login(email, stored_logins, password):

    if stored_logins[email] == hash_password(password):
        return True
    
    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "afridi112@yahoo.com" : hash_password("afridi"),
        "huzaifa112@hotmail.com" : hash_password("huzaifa"),
        "khan112@gmail.com" : hash_password("khan")
    }

    print("Authentication Required")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, stored_logins, password):
        print("Login Successful")

if __name__ == "__main__":
    main()
    

