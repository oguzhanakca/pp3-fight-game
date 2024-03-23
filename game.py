from sheets import *
from validation import *
from game_objects import *
from colorama import Fore
import random
import os


def new_line_spaces():
    print(Fore.CYAN + "-----------------------------------------" + Fore.RESET)

def clear_screen():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')


def welcome():
    """
    Displays when users starts game.
    """
    message_1 = "           _____  ______ _   _          "
    message_2 = r"     /\   |  __ \|  ____| \ | |   /\    "
    message_3 = r"    /  \  | |__) | |__  |  \| |  /  \   "
    message_4 = r"   / /\ \ |  _  /|  __| | . ` | / /\ \  "
    message_5 = r"  / ____ \| | \ \| |____| |\  |/ ____ \ "
    message_6 = r" /_/    \_\_|  \_\______|_| \_/_/    \_\ "
    message_7 = ""
    print(Fore.MAGENTA + message_1)
    print(message_2)
    print(message_3)
    print(message_4)
    print(message_5)
    print(message_6)
    print(message_7 + Fore.RESET)
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
        print("1 - Login\n2 - Register\n3 - Exit Game")
        account_option = input("Your Input : ")
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
            clear_screen()
            load_character(player_username)


def load_character(username):
    """
    Create Player's character with the data from sheets
    """
    # Get player data from sheets
    new_line_spaces()
    print(Fore.LIGHTBLUE_EX + "Loading Character ..." + Fore.RESET)
    row = accounts.find(username).row
    weapon = accounts.cell(row, 3).value
    armor = accounts.cell(row, 4).value
    gold = accounts.cell(row, 5).value
    feedback = accounts.cell(row, 6).value
    name = username.capitalize()
    # Create Player
    player = Player(name, weapon, armor, int(gold), feedback)
    # Check equipped gear
    if weapon != "None":
        print(Fore.LIGHTBLUE_EX + "Loading Weapon ..." + Fore.RESET)
        weapon = load_weapon(weapon)
        print(Fore.LIGHTBLUE_EX + "Weapon Loading completed." + Fore.RESET)
    if armor != "None":
        print(Fore.LIGHTBLUE_EX + "Loading Armor ..." + Fore.RESET)
        armor = load_armor(armor)
        print(Fore.LIGHTBLUE_EX + "Armor Loading completed." + Fore.RESET)
    stats = Stats(weapon, armor)
    print(Fore.LIGHTBLUE_EX + "Character Loading completed." + Fore.RESET)
    load_menu(player, weapon, armor, stats)


def load_weapon(weapon):
    weapon_row = weapons.find(weapon).row
    num = int(weapons.cell(weapon_row, 1).value)
    name = weapons.cell(weapon_row, 2).value
    damage = int(weapons.cell(weapon_row, 3).value)
    rate = int(weapons.cell(weapon_row, 4).value)
    weapon = Weapon(num, name, damage, rate)
    return weapon


def load_armor(armor):
    armor_row = armors.find(armor).row
    num = int(armors.cell(armor_row, 1).value)
    name = armors.cell(armor_row, 2).value
    defence = int(armors.cell(armor_row, 3).value)
    evasion = int(armors.cell(armor_row, 4).value)
    health = int(armors.cell(armor_row, 5).value)
    armor = Armor(num, name, defence, evasion, health)
    return armor


def load_menu(player, weapon, armor, stats):
    """
    Displays navigation menu that players decide what to do
    """
    valid_input = False
    while not valid_input:
        new_line_spaces()
        print(f"Welcome to Arena, {player.name}")
        print("\nWhat would you like to do?")
        print("\n1 - Visit Shop\n2 - Enter Arena\n3 - Stats\n4 - How to play")
        print("5 - Exit Game")
        menu_input = input("Your Input : ")
        if menu_input == "1":
            valid_input = True
            shop_menu(player, weapon, armor, stats)
        elif menu_input == "2":
            valid_input = True
            enter_arena(player, weapon, armor, stats)
        elif menu_input == "3":
            valid_input = True
            show_stats(player, weapon, armor, stats)
        elif menu_input == "4":
            valid_input = True
            how_to_play(player, weapon, armor, stats)
        elif menu_input == "5":
            valid_input = True
            print(Fore.CYAN + "See you later !" + Fore.RESET)
        else:
            print(Fore.RED + "\nInvalid Input\n" + Fore.RESET)


def shop_menu(player, weapon, armor, stats):
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
            load_shop(player, weapon, armor, stats, "weapon")
        elif shop_input == "2":
            shop_process = True
            load_shop(player, weapon, armor, stats, "armor")
        elif shop_input == "3":
            shop_process = True
            load_menu(player, weapon, armor, stats)
        else:
            print(Fore.RED + "\nWrong Input\n" + Fore.RESET)


def load_shop(player, weapon, armor, stats, shop_type):
    """
    Displays the items player can buy and applies their decisions
    """
    clear_screen()
    if shop_type == "weapon":
        all_items = weapons.get_all_values()
    else:
        all_items = armors.get_all_values()
    shop_process = False
    while not shop_process:
        new_line_spaces()
        print(Fore.YELLOW + f"Your current gold : {player.gold}" + Fore.RESET)
        has_item = True
        if shop_type == "weapon":
            has_item = weapon != "None"
        else:
            has_item = armor != "None"
        # Display items
        if shop_type == "weapon":
            print(Fore.MAGENTA)
            print(f"Your current weapon : {player.weapon}\n")
            print(Fore.RESET)
        else:
            print(Fore.MAGENTA)
            print(f"Your current armor : {player.armor}\n")
            print(Fore.RESET)
        display_shop_items(all_items, shop_type)
        print("Enter the id number.")
        shop_input = input("Your input : ")
        # Check if user entered a numeric value
        if shop_input.isdigit():
            item_id = int(shop_input)
        else:
            print(Fore.RED + "\nPlease enter a number\n" + Fore.RESET)
            continue
        cancel_input = item_id == 8 if shop_type == "weapon" else item_id == 5
        input_range = False
        if shop_type == "weapon":
            input_range = item_id in range(1, 8)
        else:
            input_range = item_id in range(1, 5)
        # Check input
        if cancel_input:
            shop_process = True
            load_menu(player, weapon, armor, stats)
        elif input_range:
            if has_item:
                compare_items = False
                if shop_type == "weapon":
                    compare_items = weapon.id >= item_id
                else:
                    compare_items = armor.id >= item_id
                # Check if Player's weapon better than selected weapon
                if compare_items:
                    print(Fore.LIGHTCYAN_EX)
                    print(f"Your {shop_type} is better.Are you sure?\nY/N")
                    print(Fore.RESET)
                    # Validate option
                    check_result = shop_question(player, item_id, shop_type)
                    if check_result:
                        if shop_type == "weapon":
                            weapon = update_weapon(player, item_id, weapon)
                        else:
                            armor = update_armor(player, item_id, armor)
                        stats = Stats(weapon, armor)

                else:
                    purchase_result = purchase(player, item_id, shop_type)
                    if purchase_result:
                        sheet_gold(player)
                        if shop_type == "weapon":
                            weapon = update_weapon(player, item_id, weapon)
                        else:
                            armor = update_armor(player, item_id, armor)
                        stats = Stats(weapon, armor)

            else:
                purchase_result = purchase(player, item_id, shop_type)
                if purchase_result:
                    sheet_gold(player)
                    if shop_type == "weapon":
                        weapon = update_weapon(player, item_id, weapon)
                    else:
                        armor = update_armor(player, item_id, armor)
                    stats = Stats(weapon, armor)
        else:
            print(Fore.RED)
            print("\nPlease enter a number matching the Id\n")
            print(Fore.RESET)


def enter_arena(player, weapon, armor, stats):
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
            if int(enemy_id) in range(1, 9):
                arena_process = True
                # Create Enemy
                name = all_enemies[int(enemy_id)][1]
                damage = int(all_enemies[int(enemy_id)][2])
                defence = int(all_enemies[int(enemy_id)][3])
                hp = int(all_enemies[int(enemy_id)][4])
                eva = int(all_enemies[int(enemy_id)][5])
                rate = int(all_enemies[int(enemy_id)][6])
                drop = int(all_enemies[int(enemy_id)][7])
                enemy = Enemy(name, damage, defence, hp, eva, rate, drop)
                initiate_combat(player, weapon, armor, stats, enemy)
            elif enemy_id == "9":
                arena_process = True
                load_menu(player, weapon, armor, stats)
            else:
                print(Fore.RED + "\nWrong Input\n" + Fore.RESET)
        else:
            print(Fore.RED + "\nYou must enter a number!\n" + Fore.RESET)


def show_stats(player, weapon, armor, stats):
    """
    Displays player's stats
    """
    new_line_spaces()
    stats.view_stats()
    print("1 - Go back to menu")
    stats_process = True
    while stats_process:
        stats_input = input("Your input : ")
        if stats_input == "1":
            stats_process = False
            load_menu(player, weapon, armor, stats)
        else:
            print(Fore.RED + "\nWrong Input\n" + Fore.RESET)


def initiate_combat(player, weapon, armor, stats, enemy):
    """
    Combat Controller
    """
    clear_screen()
    # Create player combat object
    p_name = player.name
    p_dmg = stats.damage()
    p_rate = stats.crit_rate()
    p_hp = stats.health()
    p_eva = stats.evasion()
    p_def = stats.defence()
    p_combat = PlayerCombat(p_name, p_dmg, p_rate, p_hp, p_eva, p_def)
    # Create enemy combat object
    e_name = enemy.name
    e_dmg = enemy.dmg
    e_def = enemy.defence
    e_hp = enemy.hp
    e_eva = enemy.eva
    e_rate = enemy.crit_rate
    drop = enemy.drop
    e_combat = EnemyCombat(e_name, e_dmg, e_def, e_hp, e_eva, e_rate, drop)
    p_max_hp = p_combat.hp
    e_max_hp = e_combat.hp
    # Create combat object
    combat = Combat()
    combat_status = "ongoing"
    round = 1
    # Start combat
    while combat_status == "ongoing":
        new_line_spaces()
        print(f"{p_combat.name} Health : {p_combat.hp} / {p_max_hp}")
        print(f"{e_combat.name} Health : {e_combat.hp} / {e_max_hp}")
        print(Fore.LIGHTYELLOW_EX + f"Round : {round}\n" + Fore.RESET)
        print("Choose your action")
        print("1 - Attack\n2 - Special Attack\n3 - Run away")
        combat_input = input("Your input : ")
        if combat_input == "1":
            new_line_spaces()
            combat.attack(p_combat, e_combat)
            combat_status = combat.check_combat(player, p_combat, e_combat)
            if combat_status != "ongoing":
                break
        elif combat_input == "2":
            new_line_spaces()
            combat.special_attack(p_combat, e_combat)
            combat_status = combat.check_combat(player, p_combat, e_combat)
            if combat_status != "ongoing":
                break
        elif combat_input == "3":
            print(Fore.LIGHTBLUE_EX)
            print("You are trying to run away...")
            print(Fore.RESET)
            if random.randint(0, 4) == 1:
                combat_status = "escaped"
                print(Fore.GREEN + "You escaped successfully" + Fore.RESET)
                break
            else:
                print(Fore.RED + "\nYou couldn't run away.\n" + Fore.RESET)
        if e_combat.stunned:
            print(Fore.LIGHTGREEN_EX)
            print(f"{e_combat.name} is stunned!")
            print(Fore.RESET)
            e_combat.stunned = False
        else:
            if round % 3 == 2:
                print(f"{e_combat.name} is preparing to heal!")
                combat.attack(e_combat, p_combat)
            elif round % 3 == 0:
                combat.heal(e_combat, enemy)
            else:
                combat.attack(e_combat, p_combat)
            combat_status = combat.check_combat(player, p_combat, e_combat)
            if combat_status != "ongoing":
                break
        round += 1
    if combat_status == "finished":
        proceed = False
        print(Fore.MAGENTA)
        print("Would you like to give a feedback?\nY/N")
        print(Fore.RESET)
        while not proceed:
            feedback_question = input("Your Input : ").lower()
            if feedback_question == "n":
                proceed = True
                print(Fore.CYAN + "See you later."+Fore.RESET)
            elif feedback_question == "y":
                if player.feedback_sent == "TRUE":
                    print(Fore.YELLOW)
                    print("You already provided a feedback.")
                    print(Fore.RESET)
                    print(Fore.CYAN)
                    print("See you later.")
                    print(Fore.RESET)
                else:
                    print(Fore.CYAN+"Enter your feedback"+Fore.RESET)
                    feedback_proceed = False
                    while not feedback_proceed:
                        message = input("Your Message : ")
                        if message.isspace() or len(message) == 0:
                            print(Fore.RED)
                            print("Please do not enter an empty message")
                            print(Fore.RESET)
                        else:
                            feedback_proceed = True
                            send_feedback(player.name, message)
                            update_sheet_feedback(player)
                            print(Fore.GREEN)
                            print("Thank you for your feedback.")
                            print(Fore.RESET)
                            print(Fore.CYAN + "See you later."+Fore.RESET)
                proceed = True
            else:
                print(Fore.RED + "Wrong Input!"+Fore.RESET)
    elif combat_status == "killed" or combat_status == "defeated":
        sheet_gold(player)
        load_menu(player, weapon, armor, stats)
    else:
        load_menu(player, weapon, armor, stats)


def display_shop_items(shop_items, shop_type):
    """
    Prints shop content
    """
    if shop_type == "weapon":
        for i in range(0, 8):
            w_id = shop_items[i][0].capitalize()
            w_name = shop_items[i][1].capitalize()
            w_dmg = shop_items[i][2].capitalize()
            w_rate = shop_items[i][3].capitalize()
            w_price = shop_items[i][4].capitalize()
            print(f"{w_id} - {w_name}\t{w_dmg}\t{w_rate}\t{w_price}")
        print("8 - Leave shop")
    else:
        for i in range(0, 5):
            a_id = shop_items[i][0].capitalize()
            a_name = shop_items[i][1].capitalize()
            a_def = shop_items[i][2].capitalize()
            a_eva = shop_items[i][3].capitalize()
            a_hp = shop_items[i][4].capitalize()
            a_price = shop_items[i][5].capitalize()
            print(f"{a_id} - {a_name}\t{a_def}\t{a_eva}\t{a_hp}\t{a_price}")
        print("5 - Leave shop")


def display_enemies(all_enemies):
    """
    Prints all enemies
    """
    for i in range(0, 9):
        e_id = all_enemies[i][0].capitalize()
        e_name = all_enemies[i][1].capitalize()
        print(f"{e_id} - {e_name}")
    print("9 - Go back to menu")


def update_weapon(player, weapon_id, weapon):
    """
    Updates the weapon of player and its stats
    """
    if weapon == "None":
        w_id = int(weapons.cell(weapon_id+1, 1).value)
        w_name = weapons.cell(weapon_id+1, 2).value
        w_dmg = int(weapons.cell(weapon_id+1, 3).value)
        w_rate = int(weapons.cell(weapon_id+1, 4).value)
        weapon = Weapon(w_id, w_name, w_dmg, w_rate)
    else:
        weapon.id = int(weapons.cell(weapon_id+1, 1).value)
        weapon.name = weapons.cell(weapon_id+1, 2).value
        weapon.damage = int(weapons.cell(weapon_id+1, 3).value)
        weapon.crit_rate = int(weapons.cell(weapon_id+1, 4).value)
    player.weapon = weapon.name
    update_sheet(player, "weapon")
    return weapon


def update_armor(player, armor_id, armor):
    """
    Updates the armor of player and its stats
    """
    if armor == "None":
        a_id = int(armors.cell(armor_id+1, 1).value)
        a_name = armors.cell(armor_id+1, 2).value
        a_def = int(armors.cell(armor_id+1, 3).value)
        a_eva = int(armors.cell(armor_id+1, 4).value)
        a_hp = int(armors.cell(armor_id+1, 5).value)
        armor = Armor(a_id, a_name, a_def, a_eva, a_hp)
    else:
        armor.id = int(armors.cell(armor_id+1, 1).value)
        armor.name = armors.cell(armor_id+1, 2).value
        armor.defense = int(armors.cell(armor_id+1, 3).value)
        armor.evasion = int(armors.cell(armor_id+1, 4).value)
        armor.health = int(armors.cell(armor_id+1, 5).value)
    player.armor = armor.name
    update_sheet(player, "armor")
    return armor


def how_to_play(player, weapon, armor, stats):
    """
    Prints how to play
    """
    new_line_spaces()
    print(Fore.YELLOW)
    print("Welcome to Arena.")
    print("Arena is a turn-based battle game that challenges players.")
    print("To beat the game, you need to defeat the Demon King.")
    print("You will earn gold when you beat enemies.")
    print("Improve your equipment with the gold you earn.")
    print("- If you die, you will lose decent amount of gold.")
    print("You can either attack or attempt to run away.")
    print("But be careful, escape attempt may fail.")
    print("Tips:\n1 - Be sure to have correct gear to face an enemy.")
    print("2 - You must land an attack to activate special attack again.")
    print("3 - Block enemies recover with your special attack.")
    print("Good luck with your adventure.")
    print("PS : Luck is also an important factor to win battles.")
    print(Fore.RESET)
    new_line_spaces()
    button_pressed = False
    while not button_pressed:
        print("1 - Go back to menu")
        player_input = input("Your input : ")
        if player_input == "1":
            button_pressed = True
            load_menu(player, weapon, armor, stats)
        else:
            print(Fore.RED + "\nWrong Input\n" + Fore.RESET)
