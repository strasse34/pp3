import gspread
from google.oauth2.service_account import Credentials
import datetime
import sys 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('to_do_list')



def get_date():
    """
    geting date from user according to the correct format.
    """
    date = input("Date(dd.mm.yyyy): ")
    current_year = get_current_year()
    check_format(date, current_year)


def check_format(date, current_year):
    """
    check format of provided date
    """
    get_current_year()
    if not date.isdigit():    
        print("Invalid data! Please provide only numbers and .!")
    elif len(date) != 10 or date[2] != '.' or date[5] != '.':
        print("Invalid data! Please provide date according to (dd.mm.yyyy!")
    elif int(date[0:2] > 31):
        print("Invalid data! Day must be equal or less than 31!")
    elif int(date[3:5] > 12):
        print("Invalid data! Month must be equal or less than 12!")
    elif int(date[6:10]) > int(current_year):
        print(f"Invalid data! Month must be equal to {current_year}")
    else:
        print(f"{date} was saved.")


def get_current_year():
    """
    gettin current year to check 
    """
    current_year = datetime.date.today().year
    return current_year


get_date()

