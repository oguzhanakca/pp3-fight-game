from sheets import *
from game_objects import *

def check_username(username):
    """
    Checks if username exists in sheet
    """
    username_lowercase = username.lower()
    return username_lowercase in accounts.col_values(1)

def check_password(username,password):
    """
    Checks if user's password is correct
    """
    account_row = accounts.find(username.lower()).row
    account_password = accounts.cell(account_row,2).value
    return password == account_password


def register_check():
    """
    Checks username and password before adding them to sheets
    """
    username_entry = False
    password_entry = False
    player_username = ""
    # Check Username - Register
    while not username_entry:
        username = input("Please enter your username\nEnter 'x' to abort\n")
        if username == "x":
            return "x"
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
    # Check Password - Register
    while username_entry and not password_entry:
        password = input("Please enter your password\nEnter 'x' to abort\n")
        if password == "x":
            return "x"
        elif len(password.split(" "))>1:
            print("Password must not contain spaces")
        elif len(password)>15 or len(password)<5:
            print("Password length must be between 5 and 15 characters")
        else:
            password_entry = True
            create_new_user(player_username,password)
            print("Your account has created. Please log in.")
            return "reg"

    
def login_check():
    """
    Asks users their username for logging in
    """
    username_entry = False
    password_entry = False
    player_username = ""
    #Check Username - Login
    while not username_entry:
        username = input("Please enter your username\nEnter 'x' to abort\n")
        if username == "x":
            return "x"
        elif check_username(username):
            player_username = username
            username_entry = True
        else:
            print("Wrong Username")

    # Check Password - Login
    while username_entry and not password_entry:
        password = input("Please enter your password\nEnter 'x' to abort\n")
        if password == "x":
            return "x"
        elif check_password(player_username,password):
            password_entry = True
            return player_username
        else:
            print("Wrong Password!")

def validate_weapon_purchase(player,weapon_id):
    """
    Checks if player has enough gold for the item and finishes purchase
    """
    required_gold = int(weapons.cell(weapon_id+1,5).value)
    check_result = player.gold >= required_gold
    if check_result:
        player.gold -= required_gold
        print("Purchase successful!")
    else:
        print("Not enough gold!")
    return check_result




