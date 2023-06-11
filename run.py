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
    This function get Date from user according to provided format using try-except.
    In case of value error, loop repeat untile getting required date format.
    """
    while True:
        entered_date = input("\nStep 1: setting date\nPlease set a date (dd.mm.yyyy): ")

        try:
            date_validation = datetime.datetime.strptime(entered_date, "%d.%m.%Y")
            selected_date = date_validation.strftime("%d.%m.%Y")
            day_of_week = date_validation.strftime("%A")
            print(f"\nYou seleceted this date: {day_of_week}, {selected_date}")
            break

        except ValueError:
            print("\nInvalid date format! Please provide the date in the format dd.mm.yyyy!\n")
            continue

    get_date_confirmation()
    date = [selected_date, day_of_week]
    return date


def get_time():
    """
    Getting Time for the job that user want to add to the list.
    In case of value error, loop repeat untile getting required date format.
    """
    while True:
        entered_time = input("Please pick a time (Example: 14:30): ")
        
        try:
            time_validation = datetime.datetime.strptime(entered_time, "%H:%M")
            valid_time = time_validation.strftime("%H:%M")
            print(f"\nYou seleceted this time: {valid_time}")
            break

        except ValueError:
            print("\nInvalid time format! Please provide the time in the format hh:mm !\n")
            continue

    get_time_confirmation()
    return entered_time


def get_title():
    """
    Getting Title for the event that user want to add to the list
    """
    entered_title = input("Please give your event a title!(Max 20 chrachters) \n")[:20]
    print(f'You provided this title "{entered_title}".\n')
    answer = input('Are you sure? (y/n):')
    if answer.lower() == 'y':
        print('\nStep 4: adding note')
        get_note()
    elif answer.lower() == 'n':
        get_title()
    else:
        print('Please use "y" for yes and "n" for no')
        get_title()
        


def get_note():
    """
    Getting Note for the tiltle that user has already selected.
    """
    entered_note = input("Please add a short note to the title!(Max 150 chrachters) \n")[:150]
    print(f'You provided this note \n"{entered_note}"\n')
    answer = input('Are you sure? (y/n):')
    if answer.lower() == 'y':
        print('\nStep 5: saving data')
        save_date()
    elif answer.lower() == 'n':
        get_note()
    else:
        print('Please use "y" for yes and "n" for no')
        get_note()


def get_date_confirmation():
    """
    Getting confrimation of user about entered date
    """
    confirmation = input("Do you confirm it? (y/n): ")
    if confirmation.lower() == 'y':
        print('Step 2: setting time')
        get_time()
    elif confirmation.lower() == 'n':
        get_date()
    else:
        print('Please use "y" for yes and "n" for no')
        get_date_confirmation()


def get_time_confirmation():
    """
    Getting confrimation of user about entered time
    """
    confirmation = input("Do you confirm it? (y/n): y")
    if confirmation.lower() == 'y':
        print('\nStep 3: selecting a title')
        get_title()
    elif confirmation.lower() == 'n':
        get_time()
    else:
        print('Please use "y" for yes and "n" for no')
        get_date_confirmation()
        

def save_date():
    confirmation = input("Please select one of the followings!\ny = Yes\ne = Edit\nex = Exit\n")
    if confirmation.lower() == 'y':
        print('update_worksheet(event)')
    elif confirmation.lower() == 'e':
        print('edit_date()')
    elif confirmation.lower() == 'ex':
        print('Have a nice day and goodbye!')
        return
    else:
        print('please use a correct value!')
        save_date()
    


def update_worksheet(event):
    """
    Updating the user worksheet in google sheet with new to do list.
    """
    print("Saving date ...\n")
    user_worksheet = SHEET.worksheet("josef_123")
    user_worksheet.append_row(event)
    print("New event successfully saved!\n")


def collect_event_data():
    """
    Collecting all the confirmed data in a list for adding to the google sheet.
    """
    event = confirmed_date
    event.append(confirmed_time)
    event.append(confirmed_title)
    event.append(confirmed_note)
    print(event)
    return event



confirmed_date = get_date()
confirmed_time = get_time()
confirmed_title = get_title()
confirmed_note = get_note()
event = collect_event_data()
update_worksheet(event)
