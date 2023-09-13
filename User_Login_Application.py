
"""User Login Application / User Authentication Application - 
Take input from User 
Case 1: 'Sign up for New User' where take three inputs '1. Username , 2.Password , 3.Email' , 
Case 2: 'Login for Existing User' login will be successfull if and only if 'Username and Password' Match else print 'Wrong Credintials' , 
Case 3: 'Delete User' using username ,
Case 4: 'Exit' .....
Checks for duplicate usernames during the sign-up process."""

"""This program uses a dictionary (user_data) to store user information, including usernames as keys and corresponding passwords and emails as values. 
The program provides four options: sign up for a new user, login for an existing user, delete a user, and exit the program. 
It ensures that login credentials are correct during the login process."""

import sys

print("***** User Authentication Application *****")

# Dictionary to store user data (username, password, email)
user_data = {}

def sign_up():
    username = input("Enter a new username: ")
    password = input("Enter a password: ")
    email = input("Enter an email: ")

    if username in user_data:
        print("Username already exists. Please choose a different username.")
    else:
        user_data[username] = {'password': password, 'email': email}
        print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_data and user_data[username]['password'] == password:
        print("Login successful!")
    else:
        print("Wrong credentials. Please try again.")

def delete_user():
    username = input("Enter the username to delete: ")
    if username in user_data:
        del user_data[username]
        print("User deleted successfully!")
    else:
        print("User not found.")

while True:
    print("\nMenu:")
    print("1. Sign up for a new user")
    print("2. Login for an existing user")
    print("3. Delete user")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        login()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        print("Exiting the program.")
        sys.exit()
    else:
        print("Invalid choice. Please select a valid option.")
