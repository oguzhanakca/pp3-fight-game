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
            print("See you later !")
            break
        else:
            new_line_spaces()
            print("Invalid Input")
        
    if player_username:
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
        menu_input = input("\nYour Input : ")
        if menu_input == "1":
            valid_input = True
            shop_menu(player)
        elif menu_input == "2":
            valid_input = True
            load_hunt(player)
        elif menu_input == "3":
            valid_input = True
            load_stats(player)
        elif menu_input == "4":
            break
        else:
            print("Invalid Input")

def shop_menu(player):
    """
    Asks players which shop they want to visit
    """
    new_line_spaces()
    shop_process = False
    print("Which shop do you want to visit?\n")
    print("1 - Weapon Shop\n2 - Armor Shop\n3 - Leave Shop\n")
    shop_input = input("Your input : ")
    while not shop_process:
        if shop_input == "1":
            shop_process = True
            load_weapon_shop(player)
        elif shop_input == "2":
            shop_process = True
            load_armor_shop(player)
        if shop_input == "3":
            shop_process = True
            load_menu(player)
        else:
            print("Wrong Input")

def load_weapon_shop(player):
    """
    Shows the weapons players can buy
    """
    new_line_spaces()
    print(f"Your current gold : {player.gold}\n")
    for row in range(1,8):
        print(f"{weapons.cell(row, 1).value.capitalize()} - {weapons.cell(row, 2).value.capitalize()}\t{weapons.cell(row, 3).value.capitalize()}\t{weapons.cell(row, 4).value.capitalize()}\t{weapons.cell(row, 5).value.capitalize()}\n")
    print("7 - Leave shop")
    # weapon_shop_input = input("Your input : ")
    # # Check if Player's weapon is better than the weapon they want to buy
    # # if player.weapon != "None":
    # #     player_weapon_row = weapons.find(player.weapon).row
    # #     player_weapon_id = int(weapons.cell(player_weapon_row,1))


    


def load_armor_shop():
    """
    Shows the armors players can buy
    """


def load_hunt(player):
    """
    Displays the list of enemies
    """

def load_stats(player):
    """
    Displays player's stats
    """
    



