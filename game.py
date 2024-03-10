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
    player_weapon,player_armor,player_gold = [accounts.cell(player_row,3).value,accounts.cell(player_row,4).value,accounts.cell(player_row,5).value]
    #Create Player
    player = Player(username.capitalize(),player_weapon,player_armor,int(player_gold))
    #Create Player's Gear
    equipped_weapon = player_weapon
    equipped_armor = player_armor
    # Check equipped gear
    if equipped_weapon != "None":
        print("Loading Weapon ...")
        weapon_row = weapons.find(equipped_weapon).row
        equipped_weapon = Weapon(int(weapons.cell(weapon_row,1).value),weapons.cell(weapon_row,2).value,int(weapons.cell(weapon_row,3).value),int(weapons.cell(weapon_row,4).value))
        print("Weapon Loading completed.")
    if equipped_armor != "None":
        print("Loading Armor ...")
        armor_row = armors.find(equipped_armor).row
        equipped_armor = Armor(int(armors.cell(armor_row,1).value),armors.cell(armor_row,2).value,int(armors.cell(armor_row,3).value),int(armors.cell(armor_row,4).value),int(armors.cell(armor_row,5).value))
        print("Armor Loading completed.")
    stats = Stats(equipped_weapon,equipped_armor)
    print("Character Loading completed.")
    load_menu(player,equipped_weapon,equipped_armor,stats)

def load_menu(player,weapon,armor,stats):
    """
    Displays navigation menu that players decide what to do
    """
    valid_input = False
    while not valid_input:
        new_line_spaces()
        print(f"Welcome to Arena, {player.name}")
        print("\nWhat would you like to do?")
        print("\n1 - Visit Shop\n2 - Enter Arena\n3 - Stats\n4 - Exit Game\n")
        menu_input = input("Your Input : ")
        if menu_input == "1":
            valid_input = True
            shop_menu(player,weapon,armor,stats)
        elif menu_input == "2":
            valid_input = True
            enter_arena(player,stats)
        elif menu_input == "3":
            valid_input = True
            show_stats(player,weapon,armor,stats)
        elif menu_input == "4":
            valid_input = True
            print("See you later !")
        else:
            print("Invalid Input")

def shop_menu(player,weapon,armor,stats):
    """
    Asks players which shop they want to visit
    """
    new_line_spaces()
    shop_process = False
    print("Which shop do you want to visit?\n")
    print("1 - Weapon Shop\n2 - Armor Shop\n3 - Leave Shop\n")
    while not shop_process:
        shop_input = input("Your input : ")
        if shop_input == "1":
            shop_process = True
            load_shop(player,weapon,armor,stats,"weapon")
        elif shop_input == "2":
            shop_process = True
            load_shop(player,weapon,armor,stats,"armor")
        elif shop_input == "3":
            shop_process = True
            load_menu(player,weapon,armor,stats)
        else:
            print("Wrong Input")

def load_shop(player,weapon,armor,stats,shop_type):
    """
    Displays the items player can buy and applies their decisions
    """
    if shop_type == "weapon":
        all_items = weapons.get_all_values()
    else:
        all_items = armors.get_all_values()
    shop_process = False
    while not shop_process:
        new_line_spaces()
        print(f"Your current gold : {player.gold}")
        player_has_item = weapon != "None" if shop_type == "weapon" else armor != "None"
        # Display items
        if shop_type == "weapon":
            print(f"Your current weapon : {player.weapon}\n")
        else:
            print(f"Your current armor : {player.armor}\n")
        display_shop_items(all_items,shop_type)
        print("Enter the id number.")
        shop_input = input("Your input : ")
        # Check if user entered a numeric value
        try:
            item_id = int(shop_input)
        except ValueError:
            print("Please enter a number")
            continue
        cancel_input = item_id == 7 if shop_type == "weapon" else item_id == 5
        input_range = item_id in range(1,7) if shop_type == "weapon" else item_id in range(1,5)
        # Check input
        if cancel_input:
            load_menu(player,weapon,armor,stats)
        elif input_range:
            if player_has_item:
                compare_items = weapon.id >= item_id if shop_type == "weapon" else armor.id >= item_id
                # Check if Player's weapon better than selected weapon
                if compare_items:
                    print(f"The {shop_type} you choose is worse or the same as the {shop_type} you have.\nDo you still want to change your {shop_type}?\nY/N")
                    check_input = input("Your input : ").lower()
                    # Validate option
                    check_result = validate_shop_question(player,item_id,shop_type,check_input)
                    if check_result:
                        update_player_weapon(player,item_id,weapon) if shop_type == "weapon" else update_player_armor(player,item_id,armor)
                        update_player_stats(weapon,armor,stats)
                else:
                    purchase_result = validate_balance(player,item_id,shop_type)
                    if purchase_result:
                        update_sheet_gold(player)
                        update_player_weapon(player,item_id,weapon) if shop_type == "weapon" else update_player_armor(player,item_id,armor)
                        update_player_stats(weapon,armor,stats)
            else:
                purchase_result = validate_balance(player,item_id,shop_type)
                if purchase_result:
                    update_sheet_gold(player)
                    update_player_weapon(player,item_id,weapon) if shop_type == "weapon" else update_player_armor(player,item_id,armor)
                    update_player_stats(weapon,armor,stats)

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
        for i in range(0,5):
                print(f"{shop_items[i][0].capitalize()} - {shop_items[i][1].capitalize()}\t{shop_items[i][2].capitalize()}\t{shop_items[i][3].capitalize()}\t{shop_items[i][4].capitalize()}\t{shop_items[i][5].capitalize()}")
        print("5 - Leave shop")
                
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

def update_player_armor(player,armor_id,armor):
    """
    Updates the armor of player and its stats
    """
    if armor == "None":
        armor = Armor(int(armors.cell(armor_id+1,1).value),armors.cell(armor_id+1,2).value,int(armors.cell(armor_id+1,3).value),int(armors.cell(armor_id+1,4).value),int(armors.cell(armor_id+1,5).value))
    else:
        armor.id = int(armors.cell(armor_id+1,1).value)
        armor.name = armors.cell(armor_id+1,2).value
        armor.defense = int(armors.cell(armor_id+1,3).value)
        armor.evasion = int(armors.cell(armor_id+1,4).value)
        armor.health = int(armors.cell(armor_id+1,5).value)
    player.armor = armor.name
    update_player_sheet(player,"armor")

def update_player_stats(weapon,armor,stats):
    """
    Updates player stats after changing weapon or armor
    """
    stats = Stats(weapon,armor)
    

def enter_arena(player):
    """
    Displays the list of enemies
    """

def show_stats(player,weapon,armor,stats):
    """
    Displays player's stats
    """
    new_line_spaces()
    stats.view_stats()
    print("1 - Go back to menu")
    stats_input = input("Your input : ")
    if stats_input == "1":
        load_menu(player,weapon,armor,stats)
    else:
        print("Wrong Input")

    



