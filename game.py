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
        menu_input = input("\nYour Input : ")
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
            break
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
            load_weapon_shop(player,weapon)
        elif shop_input == "2":
            shop_process = True
            load_armor_shop(player)
        elif shop_input == "3":
            shop_process = True
            load_menu(player)
        else:
            print("Wrong Input")

def load_weapon_shop(player,weapon):
    """
    Shows the weapons player can buy
    """
    new_line_spaces()
    print("Weapon Shop loading ...")
    all_weapons = weapons.get_all_values()
    shop_process = False
    weapon_input_check = True
    while not shop_process:
        print(f"Your current gold : {player.gold}\n")
        player_has_weapon = weapon != "None"
        print(f"Your current weapon : {weapon.name if player_has_weapon else weapon}\n")
        # Print all weapons
        for i in range(0,7):
            print(f"{all_weapons[i][0].capitalize()} - {all_weapons[i][1].capitalize()}\t{all_weapons[i][2].capitalize()}\t{all_weapons[i][3].capitalize()}\t{all_weapons[i][4].capitalize()}\n")
        print("7 - Leave shop")
        print("Enter the id number.")
        weapon_shop_input = input("Your input : ")
        try:
            weapon_id = int(weapon_shop_input)
        except ValueError:
            weapon_input_check = False
            print("Please enter a number")
        if weapon_input_check:
            if weapon_id in range(1,7):
                if player_has_weapon:
                    # Check if Player's weapon better than selected weapon
                    compare_weapons = weapon.id >= weapon_id
                    if compare_weapons:
                        print("The weapon you choose is worse or the same as the weapon you have.\nDo you still want to change your weapon?\nY/N\n")
                        check_input = input("Your input : ").lower()
                        check_process = False
                        # Validate option
                        while not check_process:
                            if check_input == "y" or check_input == "n":
                                if check_input == "y":
                                    purchase_result = validate_weapon_purchase(player,weapon_id)
                                    if purchase_result:
                                        update_player_weapon(player,weapon_id,weapon)
                                        check_process = True
                                else:
                                    check_process = True
                                    print("Purchase cancelled!")
                            else:
                                print("Wrong Input")
                    else:
                        validate_weapon_purchase(player,weapon_id)
                        update_player_weapon(player,weapon_id,weapon)
                else:
                    purchase_result = validate_weapon_purchase(player,weapon_id)
                    if purchase_result:
                        update_player_weapon(player,weapon_id,weapon)
                        
            elif weapon_id == 7:
                load_menu(player,weapon)
            else:
                print("Please enter a number matching the Id")
                
                
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
    update_sheet_weapon(player)

def update_sheet_weapon(player):
    """
    Updates player's weapon in the sheet after player purchases a weapon
    """
    account_username = player.name.lower()
    account_row = accounts.find(account_username).row
    accounts.update_cell(account_row, 4, player.weapon)

def update_sheet_gold(player):
    """
    Updates player's gold in the sheet after player purchases something
    """
    account_username = player.name.lower()
    account_row = accounts.find(account_username).row
    accounts.update_cell(account_row, 6, player.gold)

def validate_weapon_purchase(player,weapon_id):
    """
    Checks if player has enough gold for the item and finishes purchase
    """
    required_gold = int(weapons.cell(weapon_id+1,5).value)
    check_result = player.gold >= required_gold
    if check_result:
        player.gold -= required_gold
        update_sheet_gold(player)
        print("Purchase successful!")
    else:
        print("Not enough gold!")
    return check_result
            


    


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
    



