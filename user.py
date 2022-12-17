
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


def register_user():
  
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")


    user = User(name, email, password)

    with open("users.txt", "a") as file:
        file.write(user.name + "," + user.email + "," + user.password + "\n")


def login_user():

    email = input("Enter your email: ")
    password = input("Enter your password: ")


    with open("users.txt") as file:
  
        for line in file:

            user_info = line.strip().split(",")


            if email == user_info[1] and password == user_info[2]:

                print("Login successful!")
                return

 
        print("Invalid email or password.")

choice = input("Do you want to register or login? (r/l): ")

if choice.lower() == "r":
    register_user()

elif choice.lower() == "l":
    login_user()
