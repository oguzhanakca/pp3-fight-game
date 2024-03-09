from sheets import *
from validation import *
from game_objects import *

def new_line_spaces():
    print("----------------------------------------------------")

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
        if player_username == "x" or player_username == "reg":
            start_option()
        else:
            load_character(player_username)
    

def load_character(username):
    """
    Create Player's character with the data from sheets
    """
    # Get player data from sheets
    new_line_spaces()
    print("Loading Character ...")
    player_row = accounts.find(username).row
    player_health,player_weapon,player_armor,player_gold = [int(accounts.cell(player_row,3).value),accounts.cell(player_row,4).value,accounts.cell(player_row,5).value,accounts.cell(player_row,6).value]
    #Create Player
    player = Player(username.capitalize(),int(player_health),player_weapon,player_armor,int(player_gold))
    #Create Player's Weapon
    equipped_weapon = player_weapon
    if equipped_weapon != "None":
        print("Loading Weapon ...")
        weapon_row = weapons.find(equipped_weapon).row
        equipped_weapon = Weapon(int(weapons.cell(weapon_row,1).value),weapons.cell(weapon_row,2).value,int(weapons.cell(weapon_row,3).value),int(weapons.cell(weapon_row,4).value))
        print("Weapon Loading completed.")
    print("Character Loading completed.")
    load_menu(player,equipped_weapon)

def load_menu(player,weapon):
    """
    Displays navigation menu that players decide what to do
    """
    valid_input = False
    while not valid_input:
        new_line_spaces()
        print(f"Welcome to Arena, {player.name}")
        print("\nWhat would you like to do?")
        print("\n1 - Visit Shop\n2 - Hunt\n3 - Stats\n4 - Exit Game\n")
        menu_input = input("Your Input : ")
        if menu_input == "1":
            valid_input = True
            shop_menu(player,weapon)
        elif menu_input == "2":
            valid_input = True
            load_hunt(player)
        elif menu_input == "3":
            valid_input = True
            load_stats(player)
        elif menu_input == "4":
            valid_input = True
            print("See you later !")
        else:
            print("Invalid Input")

def shop_menu(player,weapon):
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
            load_shop(player,weapon,"weapon")
        elif shop_input == "2":
            shop_process = True
            load_armor_shop(player)
        elif shop_input == "3":
            shop_process = True
            load_menu(player,weapon)
        else:
            print("Wrong Input")

def load_shop(player,weapon,shop_type):
    """
    Displays the items player can buy
    """
    # Check which shop will be viewed
    if shop_type == "weapon":
        all_items = weapons.get_all_values()
    shop_process = False
    input_check = True
    while not shop_process:
        new_line_spaces()
        print(f"Your current gold : {player.gold}")
        player_has_weapon = weapon != "None"
        # Print weapon or armors
        if shop_type == "weapon":
            print(f"Your current weapon : {weapon.name if player_has_weapon else weapon}\n")
            display_shop_items(all_items,shop_type)
        else:
            continue
        print("Enter the id number.")
        shop_input = input("Your input : ")
        try:
            item_id = int(shop_input)
        except ValueError:
            input_check = False
            print("Please enter a number")
        if input_check:
            if shop_type == "weapon":
                if item_id in range(1,7):
                    if player_has_weapon:
                        # Check if Player's weapon better than selected weapon
                        compare_weapons = weapon.id >= item_id
                        if compare_weapons:
                            print("The item you choose is worse or the same as the item you have.\nDo you still want to change your weapon?\nY/N")
                            check_input = input("Your input : ").lower()
                            check_process = False
                            # Validate option
                            while not check_process:
                                if check_input == "y" or check_input == "n":
                                    if check_input == "y":
                                        check_process = True
                                        purchase_result = validate_balance(player,item_id,shop_type)
                                        if purchase_result:
                                            if shop_type == "weapon":
                                                update_sheet_gold(player)
                                                update_player_weapon(player,item_id,weapon)
                                    else:
                                        check_process = True
                                        print("Purchase cancelled!")
                                else:
                                    print("Wrong Input")
                        else:
                            purchase_result = validate_balance(player,item_id,shop_type)
                            if purchase_result:
                                if shop_type == "weapon":
                                    update_sheet_gold(player)
                                    update_player_weapon(player,item_id,weapon)
                    else:
                        purchase_result = validate_balance(player,item_id,shop_type)
                        if purchase_result:
                            if shop_type == "weapon":
                                update_sheet_gold(player)
                                update_player_weapon(player,item_id,weapon)
                elif item_id == 7:
                    load_menu(player,weapon)
                else:
                    print("Please enter a number matching the Id")

def display_shop_items(shop_items,shop_type):
    """
    Prints shop content
    """
    if shop_type == "weapon":
        for i in range(0,7):
                print(f"{shop_items[i][0].capitalize()} - {shop_items[i][1].capitalize()}\t{shop_items[i][2].capitalize()}\t{shop_items[i][3].capitalize()}\t{shop_items[i][4].capitalize()}")
        print("7 - Leave shop")
    else:
        print("Armor Shop")
                
def update_player_weapon(player,weapon_id,weapon):
    """
    Updates the weapon of player and its stats
    """
    if weapon == "None":
        weapon = Weapon(int(weapons.cell(weapon_id+1,1).value),weapons.cell(weapon_id+1,2).value,int(weapons.cell(weapon_id+1,3).value),int(weapons.cell(weapon_id+1,4).value))
    else:
        weapon.id = int(weapons.cell(weapon_id+1,1).value)
        weapon.name = weapons.cell(weapon_id+1,2).value
        weapon.damage = int(weapons.cell(weapon_id+1,3).value)
        weapon.crit_rate = int(weapons.cell(weapon_id+1,4).value)
    player.weapon = weapon.name
    update_player_sheet(player,"weapon")

def load_armor_shop():
    """
    Shows the armors player can buy
    """


def load_hunt(player):
    """
    Displays the list of enemies
    """

def load_stats(player):
    """
    Displays player's stats
    """
    



