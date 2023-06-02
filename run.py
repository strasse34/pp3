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
    This function get date from user according to provided format using try-except.
    In case of value error, loop repeat untile getting required date format.
    """
    while True:
        entered_date = input("Date (dd.mm.yyyy): ")

        try:
            date_validation = datetime.datetime.strptime(entered_date, "%d.%m.%Y")
            selected_date = date_validation.strftime("%d.%m.%Y")
            day_of_week = date_validation.strftime("%A")
            print(f"\nYou seleceted this date: {day_of_week}, {selected_date}\n")
            break        
        except ValueError:
            print("\nInvalid date format! Please provide the date in the format dd.mm.yyyy!\n")
            return False
    


get_date()
