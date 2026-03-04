users  = {'ravi@gmail.com',123456}

def email_exits(email):
    return email in users

def signup():
    email = input("Enter Email :")
    if email_exits(email):
        print("Account already exists. Redirecting To Login..\n")
        login()
        return
    name = input ("Enter Name:")
    password = input("Create Paasword:")
    users [email] = {
        "name" : name,
        "password" : password
    }
    print("Signup Successful")

def login():
    email = input("Enter email  :")
    if not email_exits(email):
        print("Account Does Not Exist. Redirecting To  Signup..\n")
        signup()
        return
    password = input("Enter Password:")
    if users[email]["password"] == password:
        print("Login Successful")
    else:
        print("Wrong Password")
    
    choice = input("Choose Login or signup :").lower()
    if choice == "login":
        login()
    elif choice == "signup":
        signup()