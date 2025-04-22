'''username = "gregorymulia"
password = "123456Abc"
'''
import sys
while True:
    choice = int(input("1 for register, 2 for login, 3 for exit"))
    if choice == 1:
        username = input("Make a new username")
        password = input("Make a new password")
        while len(password) < 7:
            password = input("New password has to be at least 7 characters long")
    elif choice == 2:
        login = False
        while not login:
            username_log = input("Type your username")
            password_log = input("Type your password")
            if username_log == username and password_log == password:
                login = True
                print(f"Welcome {username}")
                sys.exit()
    elif choice == 3:
        sys.exit()