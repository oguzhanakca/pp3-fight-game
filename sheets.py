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
feedback = sh.worksheet("feedback")

#Functions
def create_new_user(username,password):
    """
    Add new data to account sheet
    """
    new_user_row = [username.lower(),password,"None","None",0,False]
    accounts.append_row(new_user_row)

def update_player_sheet(player,shop_type):
    """
    Updates player's weapon or armor in the sheet after player purchases something
    """
    account_username = player.name.lower()
    account_row = accounts.find(account_username).row
    if shop_type == "weapon":
        accounts.update_cell(account_row, 3, player.weapon)
    else:
        accounts.update_cell(account_row, 4, player.armor)

def update_sheet_gold(player):
    """
    Updates player's gold in the sheet after player purchases something
    """
    account_username = player.name.lower()
    account_row = accounts.find(account_username).row
    accounts.update_cell(account_row, 5, player.gold)

def update_sheet_feedback(player):
    """
    Updates player's feedback status in sheets
    """
    account_username = player.name.lower()
    account_row = accounts.find(account_username).row
    accounts.update_cell(account_row, 6, "TRUE")

def send_feedback(username,message):
    """
    Add new feedback data to sheets
    """
    feedback.append_row([username,message])