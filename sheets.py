import gspread
from google.oauth2.service_account import Credentials

# Gspread implementation
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
CREDENTIALS = Credentials.from_service_account_file(
    'creds.json',
    scopes=SCOPES
)
gc = gspread.authorize(CREDENTIALS)
sh = gc.open("arena")
# Worksheets
accounts = sh.worksheet("accounts")
weapons = sh.worksheet("weapons")
armors = sh.worksheet("armors")
enemies = sh.worksheet("enemies")

#Functions
def create_new_user(username,password):
    """
    Add new data to account sheet
    """
    new_user_row = [username.lower(),password,10,"None","None",0]
    accounts.append_row(new_user_row)

def update_player_sheet(player,shop_type):
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