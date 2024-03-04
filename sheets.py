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
def check_username(username):
    """
    Checks if username exists in sheet
    """
    return username in accounts.col_values(1)

def register_username(username):
    print("Registered")