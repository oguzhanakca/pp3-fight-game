from sheets import *
from game_objects import *

def check_username(username):
    """
    Checks if username exists in sheet
    """
    return username.lower() in accounts.col_values(1)

def check_password(username,password):
    """
    Checks if user's password is correct
    """
    account_row = accounts.find(username).row
    account_password = accounts.cell(account_row,2).value
    return password == account_password


def register_check():
    """
    Get username and password input from users and check them before adding sheets
    """
    username_entry = False
    password_entry = False
    player_username = ""
    while not username_entry:
        username = input("Please enter your username\nEnter 'x' to abort\n")
        if username == "x":
            start_option()
            break
        elif not username.isalpha():
            print("Username must contain only alphabetic characters")
        elif len(username.split(" "))>1:
            print("Username must not contain spaces")
        elif len(username)>15 or len(username)<5:
            print("Username length must be between 5 and 15 characters")
        elif check_username(username):
            print("Username already exists")
        else:
            username_entry = True
            player_username = username

    while username_entry and not password_entry:
        password = input("Please enter your password\nEnter 'x' to abort\n")
        if password == "x":
            start_option()
            break
        elif len(password.split(" "))>1:
            print("Password must not contain spaces")
        elif len(password)>15 or len(password)<5:
            print("Password length must be between 5 and 15 characters")
        else:
            password_entry = True
            create_new_user(player_username,password)

    
def login_check():
    """
    Asks users their username for logging in
    """
    username_entry = False
    password_entry = False
    player_username = ""
    while not username_entry:
        username = input("Please enter your username\nEnter 'x' to abort\n")
        if username == "x":
            start_option()
            break
        elif check_username(username):
            print(f"Welcome to Arena, {username.capitalize()}")
            player_username = username
            username_entry = True
        else:
            print("Wrong Username")

    while username_entry and not password_entry:
        password = input("Please enter your password\nEnter 'x' to abort\n")
        if password == "x":
            start_option()
            break
        elif check_password(player_username,password):
            #load_character(player_username,password)
            password_entry = True
            print("Correct Password")
        else:
            print("Wrong Password!")

def start_option():
    """
    Asks users whether they want to login or register
    """
    print("\nHow would you like to proceed?\n")
    proceed = False
    while not proceed:
        account_option = input("1 - Login\n2 - Register\n3 - Exit Game\nYour Input : ")
        if account_option == "1":
            proceed = True
            login_check()
        elif account_option == "2":
            proceed = True
            register_check()
        elif account_option == "3":
            break
        else:
            print("Invalid Input")
    
