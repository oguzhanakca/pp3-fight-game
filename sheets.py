import gspread
from google.oauth2.service_account import Credentials


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
    new_user_row = [username,password,10,"None","None",0]
    accounts.append_row(new_user_row)
