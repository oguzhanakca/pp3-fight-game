from sheets import *
from validation import *
from game_objects import *
from colorama import Fore
import random

def new_line_spaces():
    print(Fore.CYAN + "----------------------------------------------------" + Fore.RESET)

def welcome():
    """
    Displays when users starts game.
    """
    message = "           _____  ______ _   _          \n     /\   |  __ \|  ____| \ | |   /\    \n    /  \  | |__) | |__  |  \| |  /  \   \n   / /\ \ |  _  /|  __| | . ` | / /\ \  \n  / ____ \| | \ \| |____| |\  |/ ____ \ \n /_/    \_\_|  \_\______|_| \_/_/    \_\\\n                                                                                "
    print(Fore.MAGENTA + message + Fore.RESET)
    start_option()

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
            print(Fore.RED + "\nInvalid Input\n" + Fore.RESET)
        
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
    print(Fore.LIGHTBLUE_EX + "Loading Character ..." + Fore.RESET)
    player_row = accounts.find(username).row
    player_weapon,player_armor,player_gold,player_feedback = [accounts.cell(player_row,3).value,accounts.cell(player_row,4).value,accounts.cell(player_row,5).value,accounts.cell(player_row,6).value]
    #Create Player
    player = Player(username.capitalize(),player_weapon,player_armor,int(player_gold),player_feedback)
    #Create Player's Gear
    weapon = player_weapon
    armor = player_armor
    # Check equipped gear
    if weapon != "None":
        print(Fore.LIGHTBLUE_EX + "Loading Weapon ..." + Fore.RESET)
        weapon = load_weapon(weapon)
        print(Fore.LIGHTBLUE_EX + "Weapon Loading completed." + Fore.RESET)
    if armor != "None":
        print(Fore.LIGHTBLUE_EX + "Loading Armor ..." + Fore.RESET)
        armor = load_armor(armor)
        print(Fore.LIGHTBLUE_EX + "Armor Loading completed." + Fore.RESET)
    stats = Stats(weapon,armor)
    print(Fore.LIGHTBLUE_EX + "Character Loading completed." + Fore.RESET)
    load_menu(player,weapon,armor,stats)

def load_weapon(weapon):
    weapon_row = weapons.find(weapon).row
    weapon = Weapon(int(weapons.cell(weapon_row,1).value),weapons.cell(weapon_row,2).value,int(weapons.cell(weapon_row,3).value),int(weapons.cell(weapon_row,4).value))
    return weapon

def load_armor(armor):
    armor_row = armors.find(armor).row
    armor = Armor(int(armors.cell(armor_row,1).value),armors.cell(armor_row,2).value,int(armors.cell(armor_row,3).value),int(armors.cell(armor_row,4).value),int(armors.cell(armor_row,5).value))
    return armor

def load_menu(player,weapon,armor,stats):
    """
    Displays navigation menu that players decide what to do
    """
    valid_input = False
    while not valid_input:
        new_line_spaces()
        print(f"Welcome to Arena, {player.name}")
        print("\nWhat would you like to do?")
        print("\n1 - Visit Shop\n2 - Enter Arena\n3 - Stats\n4 - How to play\n5 - Exit Game\n")
        menu_input = input("Your Input : ")
        if menu_input == "1":
            valid_input = True
            shop_menu(player,weapon,armor,stats)
        elif menu_input == "2":
            valid_input = True
            enter_arena(player,weapon,armor,stats)
        elif menu_input == "3":
            valid_input = True
            show_stats(player,weapon,armor,stats)
        elif menu_input == "4":
            valid_input = True
            how_to_play(player,weapon,armor,stats)
        elif menu_input == "5":
            valid_input = True
            print(Fore.CYAN + "See you later !" + Fore.RESET)
        else:
            print(Fore.RED + "\nInvalid Input\n" + Fore.RESET)

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
            print(Fore.RED + "\nWrong Input\n" + Fore.RESET)

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
        print(Fore.YELLOW + f"Your current gold : {player.gold}" + Fore.RESET)
        player_has_item = weapon != "None" if shop_type == "weapon" else armor != "None"
        # Display items
        if shop_type == "weapon":
            print(Fore.MAGENTA + f"Your current weapon : {player.weapon}\n" + Fore.RESET)
        else:
            print(Fore.MAGENTA + f"Your current armor : {player.armor}\n" + Fore.RESET)
        display_shop_items(all_items,shop_type)
        print("Enter the id number.")
        shop_input = input("Your input : ")
        # Check if user entered a numeric value
        if shop_input.isdigit():
            item_id = int(shop_input)
        else:
            print(Fore.RED + "\nPlease enter a number\n" + Fore.RESET)
            continue
        cancel_input = item_id == 8 if shop_type == "weapon" else item_id == 5
        input_range = item_id in range(1,8) if shop_type == "weapon" else item_id in range(1,5)
        # Check input
        if cancel_input:
            shop_process = True
            load_menu(player,weapon,armor,stats)
        elif input_range:
            if player_has_item:
                compare_items = weapon.id >= item_id if shop_type == "weapon" else armor.id >= item_id
                # Check if Player's weapon better than selected weapon
                if compare_items:
                    print(Fore.LIGHTCYAN_EX + f"The {shop_type} you choose is worse or the same as the {shop_type} you have.\nDo you still want to change your {shop_type}?\nY/N" + Fore.RESET)
                    # Validate option
                    check_result = validate_shop_question(player,item_id,shop_type)
                    if check_result:
                        if shop_type == "weapon":
                            weapon = update_player_weapon(player,item_id,weapon) 
                        else:
                            armor = update_player_armor(player,item_id,armor)
                        stats = Stats(weapon,armor)

                else:
                    purchase_result = validate_balance(player,item_id,shop_type)
                    if purchase_result:
                        update_sheet_gold(player)
                        if shop_type == "weapon":
                            weapon = update_player_weapon(player,item_id,weapon) 
                        else:
                            armor = update_player_armor(player,item_id,armor)
                        stats = Stats(weapon,armor)

            else:
                purchase_result = validate_balance(player,item_id,shop_type)
                if purchase_result:
                    update_sheet_gold(player)
                    if shop_type == "weapon":
                        weapon = update_player_weapon(player,item_id,weapon) 
                    else:
                        armor = update_player_armor(player,item_id,armor)
                    stats = Stats(weapon,armor)
        else:
            print(Fore.RED + "\nPlease enter a number matching the Id\n" + Fore.RESET)

def enter_arena(player,weapon,armor,stats):
    """
    Displays the list of enemies
    """

    print(Fore.LIGHTRED_EX + "Welcome to the Arena" + Fore.RESET)
    all_enemies = enemies.get_all_values()
    # Print enemy names
    display_enemies(all_enemies)
    print("Please enter the enemy id you want to face.")
    arena_process = False
    while not arena_process:
        enemy_id = input("Your input : ")
        if enemy_id.isdigit():
            if int(enemy_id) in range(1,9):
                arena_process = True
                # Create Enemy
                enemy = Enemy(all_enemies[int(enemy_id)][1],int(all_enemies[int(enemy_id)][2]),int(all_enemies[int(enemy_id)][3]),int(all_enemies[int(enemy_id)][4]),int(all_enemies[int(enemy_id)][5]),int(all_enemies[int(enemy_id)][6]),int(all_enemies[int(enemy_id)][7]))
                initiate_combat(player,weapon,armor,stats,enemy)
            elif enemy_id == "9":
                arena_process = True
                load_menu(player,weapon,armor,stats)
            else: print(Fore.RED + "\nWrong Input\n" + Fore.RESET)
        else:
            print(Fore.RED + "\nYou must enter a number!\n" + Fore.RESET)
    
def show_stats(player,weapon,armor,stats):
    """
    Displays player's stats
    """
    new_line_spaces()
    stats.view_stats()
    print("1 - Go back to menu")
    stats_process = True
    stats_input = input("Your input : ")
    while stats_process:
        if stats_input == "1":
            stats_process = False
            load_menu(player,weapon,armor,stats)
        else:
            print(Fore.RED + "\nWrong Input\n" + Fore.RESET)

def initiate_combat(player,weapon,armor,stats,enemy):
    """
    Combat Controller
    """
    #Create player and enemy
    player_combat = PlayerCombat(player.name,stats.damage(),stats.crit_rate(),stats.health(),stats.evasion(),stats.defence())
    enemy_combat = EnemyCombat(enemy.name,enemy.damage,enemy.defence,enemy.health,enemy.evasion,enemy.crit_rate,enemy.gold_drop)
    player_max_health = player_combat.health
    enemy_max_health = enemy_combat.health
    #Create combat
    combat = Combat()
    combat_status = "ongoing"
    round = 1
    #Start combat
    while combat_status == "ongoing":
        new_line_spaces()
        print(f"{player_combat.name} Health : {player_combat.health} / {player_max_health}")
        print(f"{enemy_combat.name} Health : {enemy_combat.health} / {enemy_max_health}")
        print(Fore.LIGHTYELLOW_EX + f"Round : {round}\n" + Fore.RESET)
        print("Choose your action\n1 - Attack\n2 - Special Attack\n3 - Run away")
        combat_input = input("Your input : ")
        if combat_input == "1":
            new_line_spaces()
            combat.attack(player_combat,enemy_combat)
            combat_status = combat.check_combat(player,player_combat,enemy_combat)
            if combat_status != "ongoing":
                break
        elif combat_input == "2":
            new_line_spaces()
            combat.special_attack(player_combat,enemy_combat)
            combat_status = combat.check_combat(player,player_combat,enemy_combat)
            if combat_status != "ongoing":
                break
        elif combat_input == "3":
            print(Fore.LIGHTBLUE_EX + "You are trying to run away..." + Fore.RESET)
            if random.randint(0,4)==1:
                combat_status = "escaped"
                print(Fore.GREEN + "You escaped successfully" + Fore.RESET)
                break
            else:
                print(Fore.RED + "\nYou couldn't run away.\n" + Fore.RESET)
        if enemy_combat.stunned:
            print(Fore.LIGHTGREEN_EX + f"{enemy_combat.name} is stunned!" + Fore.RESET)
            enemy_combat.stunned = False
        else:
            if round%3 == 2:
                print(f"{enemy_combat.name} is preparing to heal!")
                combat.attack(enemy_combat,player_combat)
            elif round%3 == 0:
                combat.heal(enemy_combat,enemy)
            else:
                combat.attack(enemy_combat,player_combat)
            combat_status = combat.check_combat(player,player_combat,enemy_combat)
            if combat_status != "ongoing":
                break
        round += 1
    if combat_status == "finished":
        proceed = False
        print(Fore.MAGENTA+"Would you like to give a feedback?\nY/N"+Fore.RESET)
        while not proceed:
            feedback_question = input("Your Input : ").lower()
            if feedback_question == "n":
                proceed = True
                print(Fore.CYAN + "See you later."+Fore.RESET)
            elif feedback_question == "y":
                if player.feedback_sent == "TRUE":
                    print(Fore.YELLOW + "You already provided a feedback."+Fore.RESET)
                    print(Fore.CYAN + "See you later."+Fore.RESET)
                else:
                    print(Fore.CYAN+"Enter your feedback"+Fore.RESET)
                    feedback_proceed = False
                    while not feedback_proceed:
                        message = input("Your Message : ")
                        if message.isspace() or len(message) == 0:
                            print(Fore.RED+"Please do not enter an empty message"+Fore.RESET)
                        else:    
                            feedback_proceed = True
                            send_feedback(player.name,message)
                            update_sheet_feedback(player)
                            print(Fore.GREEN + "Thank you for your feedback."+Fore.RESET)
                            print(Fore.CYAN + "See you later."+Fore.RESET)
                proceed = True
            else:
                print(Fore.RED + "Wrong Input!"+Fore.RESET)  
            
    elif combat_status == "killed" or combat_status == "defeated":
        update_sheet_gold(player)
        load_menu(player,weapon,armor,stats)
    else:
        load_menu(player,weapon,armor,stats)



def display_shop_items(shop_items,shop_type):
    """
    Prints shop content
    """
    if shop_type == "weapon":
        for i in range(0,8):
                print(f"{shop_items[i][0].capitalize()} - {shop_items[i][1].capitalize()}\t{shop_items[i][2].capitalize()}\t{shop_items[i][3].capitalize()}\t{shop_items[i][4].capitalize()}")
        print("8 - Leave shop")
    else:
        for i in range(0,5):
                print(f"{shop_items[i][0].capitalize()} - {shop_items[i][1].capitalize()}\t{shop_items[i][2].capitalize()}\t{shop_items[i][3].capitalize()}\t{shop_items[i][4].capitalize()}\t{shop_items[i][5].capitalize()}")
        print("5 - Leave shop")

def display_enemies(all_enemies):
    """
    Prints all enemies
    """
    for i in range(0,9):
        print(f"{all_enemies[i][0].capitalize()} - {all_enemies[i][1].capitalize()}")
    print("9 - Go back to menu")
                
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
    return weapon

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
    return armor

def how_to_play(player,weapon,armor,stats):
    """
    Prints how to play
    """
    new_line_spaces()
    print(Fore.MAGENTA + "Welcome to Arena.\nArena is a turn-based battle game that challenges players. You must advance against different enemies by making the right attacks at the right time.\n- Condition of beating game : To beat the game, you need to defeat the Demon King.\n- Progress : Improve your equipment with the gold you earn from defeating enemies.\n- Combat : You need to decide well which attack you should use or when you should run away. But be careful, escaping may not always be successful.\n- Combat Tips:\n1 - Be sure to have correct gear to face an enemy.\n2 - Think carefully before using your special attack. You need to use normal attack once before using your special attack. Escape attempt will not recover your special attack cooldown.\n3 - Enemies will try to recover their health every 3 turn. You can try to block it with your special attack.\nGood luck with your adventure.\nPS : Luck is also an important factor to win battles." + Fore.RESET)
    new_line_spaces()
    button_pressed = False
    while not button_pressed:
        print("1 - Go back to menu")
        player_input = input("Your input : ")
        if player_input == "1":
            button_pressed = True
            load_menu(player,weapon,armor,stats)
        else:
            print(Fore.RED + "\nWrong Input\n" + Fore.RESET)
    