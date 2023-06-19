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



def user_login():
    """
    This function does login process of users.
    It get username and password of users and check in user_pass dict.
    If usename and password exist in dict, user allowed to start program.
    """
    print('Welcome to "My To Do List"!')
    answer = input('Do you have account? (y/n) ')
    if answer.lower() == 'n':
        print('\n')
        print('\nPlease open an account!')
        create_account()
    elif answer.lower() == 'y':
        print('\n')
        login_success = False
        while not login_success:
            global username
            username = input('Username: ')
            cred_sheet = SHEET.worksheet('cred')
            data = cred_sheet.get_all_values()
            usernames = [row[0] for row in data]
            if username in usernames:
                correct_password = False
                while not correct_password:
                    password = input('Password: ')
                    index = usernames.index(username)
                    if password == data[index][1]:
                        login_success = True
                        break
                    else:
                        print('Password is wrong! Please try again!')
            else:
                print('Username is wrong! Please try again!')
        if login_success:
            print('\nYou have successfully loged in.')
            show_event_list()
            get_date()
    else:
        print('Please type correct value!')



def show_event_list():
    """
    This function provides users with the all the events which starts from current date after login.
    The function, get all the dates and compare with the current date.
    Then lists those which is in current date or after it.  
    """
    date_sheet = SHEET.worksheet(username)
    all_date = date_sheet.get_all_values()
    dates = [row[0] for row in all_date]
    the_date = datetime.date.today()
    current_date = the_date.strftime("%d.%m.%Y")
    matched_dates = []

    for date in dates:
        if date >= current_date:
            matched_dates.append(date)
        else:
            print('You have no event.')

    if matched_dates:
        print('Your event list is as follows:')
        for date in matched_dates:
            print(date)
    else:
        print('You have no upcoming events.')

    while True:
        answer = input('\nWhat do you want to do? (n = Add new event / e = Exit) ')
        if answer.lower() == 'n':
            get_date()
        elif answer.lower() == 'e':
            print('\nGoodbye!')
            exit()
        else:
            print('\nIncorrect Value!\nPlease use "n" or "e"!')




def create_account():
    """
    This function get user information,
    add new worksheet in google sheet with provided username,
    and save all of information to his/her own worksheet. 
    """
    first_name = input('Please enter your first name: ').capitalize()
    last_name = input('Please enter your last name: ').capitalize()
    
    while True:
        global username
        username = input('Please enter a username: ')
        cred_sheet = SHEET.worksheet('cred')
        data = cred_sheet.get_all_values()
        usernames = [row[0] for row in data]
        if username not in usernames:
            password = input('Please enter pssword: ')
            break
        else:
            print('The username is already selected. Please try another one!')
    
    cred_sheet = SHEET.worksheet('cred')
    user_pass = [username, password, first_name, last_name]
    print(user_pass)
    cred_sheet.append_row(user_pass)

    current_sheet = SHEET.worksheet('template')
    duplicated_sheet = current_sheet.duplicate()
    duplicated_sheet.update_title(username)
        
    print(f'\nCongratulations {first_name}! Your account has been set up.')
    time.sleep(2)
    print('\nFor adding new event to your "to do list", we need to take 5 steps.')
    get_date()
    time.sleep(2)



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
            print('\nIncorrect Value!\nPlease use "y" for Yes and "n" for No!')
    

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
            print('\nIncorrect Value!\nPlease use "y" for Yes and "n" for No!')
    


def get_title():
    """
    Getting Title for the event that user want to add to the list
    """
    
    entered_title = input("Please give your event a title!(Max 20 chrachters): ")[:20]
    while True:
        answer = input(f'\nYou provided this title "{entered_title}". Sure? (y/n) ')
        if answer.lower() == 'y':
            event_data.append(entered_title)
            print('\nStep 4: adding note')
            get_note()
        elif answer.lower() == 'n':
            print('\nStep 3: selecting a title')
            get_title()
        else:
            print('\nIncorrect Value!\nPlease use "y" for yes and "n" for no!')
        
            
    


def get_note():
    """
    Getting Note for the tiltle that user has already selected.
    """
    entered_note = input("Please add a short note to the title!(Max 150 chrachters): \n")[:150]
    while True:
        answer = input(f'\nYou provided below note: \n\n"{entered_note}"\n\nSure? (y/n) ')
        if answer.lower() == 'y':
            event_data.append(entered_note)
            print('\nStep 5: saving data')
            save_date()
        elif answer.lower() == 'n':
            print('\nStep 4: adding note')
            get_note()
        else:
            print('\nIncorrect Value!\nPlease use "y" for yes and "n" for no!')
      
            
                
   


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
    while True:
        confirmation = input("\nPlease select one of the followings!\ns = Save and exit\na = Save and add another event\ne = Exit without save\n")
        if confirmation.lower() == 's':
            update_worksheet(event_data)
            print('\nHave a nice day and goodbye!')
            exit()
        elif confirmation.lower() == 'a':
            update_worksheet(event_data)
            event_data.clear()
            get_date()
        elif confirmation.lower() == 'e':
            print('\nHave a nice day and goodbye!')
            exit()
        else:
            print('\nIncorrect Value! Please use a correct value!')
            



def update_worksheet(event_data):
    """
    Updating the user worksheet in google sheet with new to do list.
    """
    print("\nSaving date ... Please wait ...\n")
    time.sleep(3)
    user_worksheet = SHEET.worksheet(username)
    user_worksheet.append_row(event_data)
    print("The event was successfully saved!\n")



event_data = []
user_login()