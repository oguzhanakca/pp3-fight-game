from sheets import *
from validation import *
from game_objects import *

def new_line_spaces():
    print("\n----------------------------------------------------\n")

def start_option():
    """
    Asks users whether they want to login or register
    """
    new_line_spaces()
    print("How would you like to proceed?")
    proceed = False
    player_username = ""
    while not proceed:
        new_line_spaces()
        account_option = input("1 - Login\n2 - Register\n3 - Exit Game\nYour Input : ")
        if account_option == "1":
            proceed = True
            new_line_spaces()
            player_username = login_check()
        elif account_option == "2":
            proceed = True
            new_line_spaces()
            player_username = register_check()
        elif account_option == "3":
            break
        else:
            new_line_spaces()
            print("Invalid Input")
        
    if player_username == "x":
        start_option()
    else:
        load_character(player_username)

def load_character(username):
    """
    Create Player's character with the data from sheets
    """
    # Get player data from sheets
    player_row = accounts.find(username).row
    player_health,player_weapon,player_armor,player_gold = [int(accounts.cell(player_row,3).value),accounts.cell(player_row,4).value,accounts.cell(player_row,5).value,accounts.cell(player_row,6).value]
    #Create Player
    player = Player(username.capitalize(),player_health,player_weapon,player_armor,player_gold)
    load_menu(player)

def load_menu(player):
    """
    Displays navigation menu that players decide what to do
    """
    valid_input = False
    while not valid_input:
        new_line_spaces()
        print("\nWhat would you like to do?")
        print("\n1 - Visit Shop\n2 - Hunt\n3 - Stats\n4 - Exit Game\n")
        menu_input = input("Your Input : ")
        if menu_input == 1:
            valid_input = True
            load_shop(player)
        elif menu_input == 2:
            valid_input = True
            load_hunt(player)
        elif menu_input == 3:
            load_stats(player)
        elif menu_input == 4:
            break
        else:
            print("Invalid Input")

def load_shop(player):
    """
    Displays weapons and armors that players can buy
    """

def load_hunt(player):
    """
    Displays the list of enemies
    """

def load_stats(player):
    """
    Displays player's stats
    """
    



