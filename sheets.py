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
sh = gc.open("fight_game")
# Worksheets
accounts = sh.worksheet("accounts")
weapons = sh.worksheet("weapons")
armors = sh.worksheet("armors")
enemies = sh.worksheet("enemies")

