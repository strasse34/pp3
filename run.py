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
    day = get_day(date)
    check_format(day, date, current_year)


def check_format(day, date, current_year):
    """
    check format of provided date
    """
    get_current_year()
    get_day(date)
    try:
        if date[2] != '.' or date[5] != '.':
            print("Invalid date format! Please provide date according to the format (dd.mm.yyyy)!")
            get_date()
        elif int(date[0:2]) > 31 or int(date[0:2]) == 0:
            print("Invalid date format! Day must be a number in range: 1-31 !")
        elif int(date[3:5]) > 12 or int(date[3:5]) == 0:
            print("Invalid date format! Month must be a number in range: 1-12 !")
            get_date()
        elif int(date[6:10]) < int(current_year):
            print(f"Invalid date format! Year must be equal or greather than {current_year}.")
            get_date()
        else:
            print(f"You selected this date: {day}, {date}")
    except ValueError:
        print("Invalid date format! Please Try again!")
        get_date()
   


def get_current_year():
    """
    getting current year to check not belong to the past
    """
    current_year = datetime.date.today().year
    return current_year

def get_day(date):
    """
    getting day according to the user date entery
    """
    day = datetime.datetime.strptime(date, "%d.%m.%Y").strftime("%A")
    return day



get_date()
