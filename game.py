from game_objects import *
from sheets import *


def load_character(username):
    """
    Create Player's character with the data from sheets
    """
    # Get player data from sheets
    player_row = accounts.find(username).row
    player_health,player_weapon,player_armor,player_gold = [int(accounts.cell(player_row,3).value),accounts.cell(player_row,4).value,accounts.cell(player_row,5).value,accounts.cell(player_row,6).value]
    #Create Player
    player = Player(username.capitalize(),player_health,player_weapon,player_armor,player_gold)

