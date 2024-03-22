from sheets import *
from game_objects import *
from colorama import Fore


def check_username(username):
    """
    Checks if username exists in sheet
    """
    username_lowercase = username.lower()
    return username_lowercase in accounts.col_values(1)


def check_password(username, password):
    """
    Checks if user's password is correct
    """
    account_row = accounts.find(username.lower()).row
    account_password = accounts.cell(account_row, 2).value
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
        print("Please enter your username\nEnter 'x' to abort\n")
        username = input("Your input : ")
        if username == "x":
            return "x"
        elif not username.isalpha():
            print(Fore.RED)
            print("Username must contain only alphabetic characters")
            print(Fore.RESET)
        elif len(username.split(" ")) > 1:
            print(Fore.RED)
            print("Username must not contain spaces")
            print(Fore.RESET)
        elif len(username) > 15 or len(username) < 5:
            print(Fore.RED)
            print("Username length must be between 5 and 15 characters")
            print(Fore.RESET)
        elif check_username(username):
            print(Fore.RED + "Username already exists" + Fore.RESET)
        else:
            username_entry = True
            player_username = username
    # Check Password - Register
    while username_entry and not password_entry:
        print("\nPlease enter your password\nEnter 'x' to abort\n")
        password = input("Your input : ")
        if password == "x":
            return "x"
        elif len(password.split(" ")) > 1:
            print(Fore.RED)
            print("Password must not contain spaces")
            print(Fore.RESET)
        elif len(password) > 15 or len(password) < 5:
            print(Fore.RED)
            print("Password length must be between 5 and 15 characters")
            print(Fore.RESET)
        else:
            password_entry = True
            create_new_user(player_username, password)
            print(Fore.LIGHTGREEN_EX)
            print("Your account has created. Please log in.")
            print(Fore.RESET)
            return "reg"


def login_check():
    """
    Asks users their username for logging in
    """
    username_entry = False
    password_entry = False
    player_username = ""
    # Check Username - Login
    while not username_entry:
        print("Please enter your username\nEnter 'x' to abort")
        username = input("Your username : ")
        if username == "x":
            return "x"
        elif check_username(username):
            player_username = username
            username_entry = True
        else:
            print(Fore.RED + "\nWrong Username\n" + Fore.RESET)

    # Check Password - Login
    while username_entry and not password_entry:
        print("\nPlease enter your password\nEnter 'x' to abort")
        password = input("Your password : ")
        if password == "x":
            return "x"
        elif check_password(player_username, password):
            password_entry = True
            return player_username
        else:
            print(Fore.RED + "\nWrong Password!\n" + Fore.RESET)


def purchase(player, weapon_id, shop_type):
    """
    Checks if player has enough gold for the item and finishes purchase
    """
    required_gold = 0
    if shop_type == "weapon":
        required_gold = int(weapons.cell(weapon_id+1, 5).value)
    else:
        required_gold = int(armors.cell(weapon_id+1, 6).value)
    check_result = player.gold >= required_gold
    if check_result:
        player.gold -= required_gold
        print(Fore.LIGHTGREEN_EX + "Purchase successful!" + Fore.RESET)
    else:
        print(Fore.RED + "Not enough gold!" + Fore.RESET)
    return check_result


def shop_question(player, item_id, shop_type):
    check_process = False
    while not check_process:
        check_input = input("Your input : ").lower()
        if check_input == "y" or check_input == "n":
            if check_input == "y":
                check_process = True
                purchase_result = purchase(player, item_id, shop_type)
                if purchase_result:
                    sheet_gold(player)
                    return True
            else:
                check_process = True
                print(Fore.MAGENTA + "Purchase cancelled!" + Fore.RESET)
                return False
        else:
            print(Fore.RED + "Wrong Input" + Fore.RESET)
