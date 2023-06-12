import gspread
from google.oauth2.service_account import Credentials
import datetime
import sys
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('to_do_list')

user_pass = {}

def user_login():
    """
    This function does login process of users.
    It get username and password of users and check in user_pass dict.
    If usename and password exist in dict, user allowed to start program.
    """
    print('Welcome to "My To Do List"!')
    answer = input('Are you new user? (y/n) ')
    if answer.lower() == 'y':
        print('\n')
        create_account()
    elif answer.lower() == 'n':
        print('\n')
        login_success = False
        while not login_success:
            username = input('\nUsername: ')
            global user_pass
            if username in user_pass:
                while True:
                    password = input('Password:')
                    if user_pass[username] == password:
                        login_success = True
                        break
                    else:
                        print('Password is wrong! Please try again!')
            else:
                print('Username is wrong! Please try again!')
        if login_success:
            print('get_date()')
    else:
        print('Please type correct value!')


def create_account():
    """
    This function get user information,
    add new worksheet in google sheet with provided username,
    and save all of information to his/her own worksheet. 
    """
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    global username
    username = input('Please enter a username: ')
    password = input('Please enter pssword: ')
    current_sheet = SHEET.worksheet('template')
    duplicated_sheet = current_sheet.duplicate()
    duplicated_sheet.update_title(username)
    new_sheet = SHEET.worksheet(username)
    new_sheet.update_cell(1, 2, first_name)
    new_sheet.update_cell(2, 2, last_name)
    new_sheet.update_cell(3, 2, username)
    new_sheet.update_cell(4, 2, password)
    global user_pass
    user_pass[username] = password
    print(user_pass)
    print(f'\nCongratulations {first_name}! Your account has been set up.')
    time.sleep(2)
    print('\nFor adding new event to your "to do list", we need to take 5 steps.')
    get_date()
    time.sleep(2)



# def get_date():
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
    while True:
        confirmation = input("Do you confirm it? (y/n): ")
        if confirmation.lower() == 'y':
            event_data.append(entered_date)
            event_data.append(day_of_week)
            print(event_data)
            print('\nStep 2: setting time')
            get_time()
        elif confirmation.lower() == 'n':
            get_date()
        else:
            print('\nPlease use "y" for Yes and "n" for No!')
    

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
    while True:
        confirmation = input("Do you confirm it? (y/n): ")
        if confirmation.lower() == 'y':
            event_data.append(entered_time)
            print(event_data)
            print('\nStep 3: selecting a title')
            get_title()
        elif confirmation.lower() == 'n':
            print('\nStep 2: setting time')
            get_time()
        else:
            print('\nPlease use "y" for Yes and "n" for No!')
    


def get_title():
    """
    Getting Title for the event that user want to add to the list
    """
    entered_title = input("Please give your event a title!(Max 20 chrachters): ")[:20]
    answer = input(f'\nYou provided this title "{entered_title}". Sure? (y/n) ')
    if answer.lower() == 'y':
        event_data.append(entered_title)
        print(event_data)
        print('\nStep 4: adding note')
        get_note()
    elif answer.lower(event_data) == 'n':
        print('\nStep 3: selecting a title')
        get_title()
    else:
        print('Please use "y" for yes and "n" for no!')
        get_title()
    


def get_note():
    """
    Getting Note for the tiltle that user has already selected.
    """
    entered_note = input("Please add a short note to the title!(Max 150 chrachters): \n")[:150]
    answer = input(f'\nYou provided below note: \n\n"{entered_note}"\n\nSure? (y/n) ')
    if answer.lower() == 'y':
        event_data.append(entered_note)
        print(event_data)
        print('\nStep 5: saving data')
        save_date()
    elif answer.lower() == 'n':
        print('\nStep 4: adding note')
        get_note()
    else:
        print('\nPlease use "y" for yes and "n" for no!')
        get_note()
   


def save_date():
    """
    Getting user confirmation for saving data or leading user to exit or edit date.
    """
    date = event_data[0]
    day = event_data[1]
    time = event_data[2]
    title = event_data[3]
    note = event_data[4]
    print(f'\nYou provided below information for your event:\nDate: {date}\nDay: {day}\nTime: {time}\nTitle: {title}\nNote: {note}')
    confirmation = input("\nPlease select one of the followings! (s = Save event / e = Exit)")
    if confirmation.lower() == 's':
        update_worksheet(event_data)
    elif confirmation.lower() == 'e':
        print('\nHave a nice day and goodbye!')
        new_event = input("if you want to add a new event please hit Enter key!")
        if new_event == "":
            get_date()
    else:
        print('Please use a correct value!')
        save_date()



def update_worksheet(event_data):
    """
    Updating the user worksheet in google sheet with new to do list.
    """
    print("\nSaving date ...\n")
    time.sleep(3)
    user_worksheet = SHEET.worksheet(username)
    user_worksheet.append_row(event_data)
    print("New event successfully saved!\n")
    new_event = input('\nIf you want to add an other event please Enter!')
    if new_event == "":
        get_date()


event_data = []
user_login()
create_account()

