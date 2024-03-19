from sheets import *
from game_objects import *
from colorama import Fore

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
        print("Please enter your username\nEnter 'x' to abort\n")
        username = input("Your input : ")
        if username == "x":
            return "x"
        elif not username.isalpha():
            print(Fore.RED + "\nUsername must contain only alphabetic characters\n" + Fore.RESET)
        elif len(username.split(" "))>1:
            print(Fore.RED + "\nUsername must not contain spaces\n" + Fore.RESET)
        elif len(username)>15 or len(username)<5:
            print(Fore.RED + "\nUsername length must be between 5 and 15 characters\n" + Fore.RESET)
        elif check_username(username):
            print(Fore.RED + "\nUsername already exists\n" + Fore.RESET)
        else:
            username_entry = True
            player_username = username
    # Check Password - Register
    while username_entry and not password_entry:
        print("\nPlease enter your password\nEnter 'x' to abort\n")
        password = input("Your input : ")
        if password == "x":
            return "x"
        elif len(password.split(" "))>1:
            print(Fore.RED + "\nPassword must not contain spaces\n" + Fore.RESET)
        elif len(password)>15 or len(password)<5:
            print(Fore.RED + "\nPassword length must be between 5 and 15 characters\n" + Fore.RESET)
        else:
            password_entry = True
            create_new_user(player_username,password)
            print(Fore.LIGHTGREEN_EX + "\nYour account has created. Please log in.\n" + Fore.RESET)
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
        elif check_password(player_username,password):
            password_entry = True
            return player_username
        else:
            print(Fore.RED + "\nWrong Password!\n" + Fore.RESET)

def validate_balance(player,weapon_id,shop_type):
    """
    Checks if player has enough gold for the item and finishes purchase
    """
    required_gold = 0
    if shop_type == "weapon":
        required_gold = int(weapons.cell(weapon_id+1,5).value)
    else:
        required_gold = int(armors.cell(weapon_id+1,6).value)
    check_result = player.gold >= required_gold
    if check_result:
        player.gold -= required_gold
        print(Fore.LIGHTGREEN_EX + "Purchase successful!" + Fore.RESET)
    else:
        print(Fore.RED + "Not enough gold!" + Fore.RESET)
    return check_result


def validate_shop_question(player,item_id,shop_type):
    check_process = False
    while not check_process:
        check_input = input("Your input : ").lower()
        if check_input == "y" or check_input == "n":
            if check_input == "y":
                check_process = True
                purchase_result = validate_balance(player,item_id,shop_type)
                if purchase_result:
                    update_sheet_gold(player)
                    return True
            else:
                check_process = True
                print(Fore.MAGENTA + "Purchase cancelled!" + Fore.RESET)
                return False
        else:
            print(Fore.RED + "Wrong Input" + Fore.RESET)
