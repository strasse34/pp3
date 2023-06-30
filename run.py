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
    print('\nWelcome to "My To Do List"!'
          '\n'
          '\nWhat is "My To Do List"?'
          '\nWith this small app, you can save your future tasks or events.'
          '\nYou provide date, time, title and a short note '
          'for each event/task.'
          '\nYou make an account and all data will be saved in your account.'
          '\nApp will provide you with the list of your upcomming '
          '\nevents/tasks while log in.'
          '\n'
          '\nHow to use?'
          '\nJust follow the inner app instructions and heat Enter key!')
    while True:
        answer = input('\nDo you have account? (y = Yes / n = No + Enter!)')
        if answer.lower() == 'n':
            print("\nOk, let's open an account!")
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
                        password = input("Password: ")
                        index = usernames.index(username)
                        first_name = data[index][2]
                        if password == data[index][1]:
                            login_success = True
                            break
                        else:
                            print('\nPassword is not matched with username! '
                                  'Please try again!')
                else:
                    print(f'\nWe do not have "{username}" in our data base! '
                          "Please try again!")
            if login_success:
                print(f'\nHi {first_name}. You have successfully loged in.\n'
                      'Loading your event(s) ... please wait! ...\n')
                time.sleep(3)
                show_event_list()
                get_date()
        else:
            print('\nIncorrect Value! Please enter correct value!\n')


def show_event_list():
    """
    This function provides users with the all the events which starts from
    current date after login.
    The function, get all the dates and compare with the current date.
    Then lists those which is in current date or after it.
    """
    date_sheet = SHEET.worksheet(username)
    all_data = date_sheet.get_all_values()
    headers = all_data[0]
    data_rows = all_data[1:]
    dates = [row[0] for row in data_rows]
    current_date = datetime.date.today()
    matched_data = []

    for date, row in zip(dates, data_rows):
        event_date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
        if event_date >= current_date:
            matched_data.append(row)

    if matched_data:
        matched_data.sort(key=lambda x: (
            datetime.datetime.strptime(x[0], "%d.%m.%Y")
        ))
        print("Your event list is as follows:\n")
        for data in matched_data:
            print("Date:", data[0])
            for header, value in zip(headers[1:], data[1:]):
                print(header + ":", value)
            print()
    else:
        print('You have no upcoming events.')

    while True:
        answer = input(
            '\nWhat do you want to do? (a = Add new event / e = Exit) '
        )
        if answer.lower() == 'a':
            get_date()
        elif answer.lower() == 'e':
            print('\nGoodbye!\n')
            exit()
        else:
            print('\nIncorrect Value! Please use "n" or "e"!')


def create_account():
    """
    This function get user information,
    add new worksheet in google sheet with provided username,
    and save all of information to his/her own worksheet.
    """
    while True:
        first_name = input('Please enter your first name: ').capitalize()
        if first_name.strip():
            break
        else:
            print("\nFirst name cannot be empty. Please try again.")
    while True:
        last_name = input('Please enter your last name: ').capitalize()
        if last_name.strip():
            break
        else:
            print("\nLast name cannot be empty. Please try again.")

    while True:
        global username
        while True:
            username = input('Please enter a username: ')
            if username.strip():
                break
            else:
                print("\nUsername cannot be empty. Please try again.")
        cred_sheet = SHEET.worksheet('cred')
        data = cred_sheet.get_all_values()
        usernames = [row[0] for row in data]
        if username not in usernames:
            while True:
                password = input('Please enter pssword: ')
                if password.strip():
                    break
                else:
                    print("\nPassword cannot be empty. Please try again.")
            break
        else:
            print('\nThe username is already selected. '
                  'Please try another one!')

    cred_sheet = SHEET.worksheet('cred')
    user_pass = [username, password, first_name, last_name]
    cred_sheet.append_row(user_pass)

    current_sheet = SHEET.worksheet('template')
    duplicated_sheet = current_sheet.duplicate()
    duplicated_sheet.update_title(username)

    print(f'\nCongratulations {first_name}! Your account has been set up.')
    time.sleep(2)
    print(
        '\nFor adding new event to "My To Do List", we need to take 5 steps.'
    )
    get_date()
    time.sleep(2)


def get_date():
    """
    This function gets a date from the user according to 
    the provided format using try-except.
    In case of a value error, the loop repeats until 
    getting the required date format.
    """
    while True:
        entered_date = input("\nStep 1: setting date\nPlease set a date (dd.mm.yyyy): ")
        try:
            date_validation = datetime.datetime.strptime(entered_date, "%d.%m.%Y")

            # Check if the entered date is a past or current date
            if date_validation.date() <= datetime.datetime.now().date():
                print("\nInvalid date! Please provide a future date.")
                continue

            selected_date = date_validation.strftime("%d.%m.%Y")
            day_of_week = date_validation.strftime("%A")
            print(f"\nYou selected this date: {day_of_week}, {selected_date}")
            break

        except ValueError:
            print("\nInvalid date format! Please provide the date in dd.mm.yyyy format!")
            continue

    while True:
        confirmation = input("Do you confirm it? (y/n): ")
        if confirmation.lower() == "y":
            event_data.append(entered_date)
            event_data.append(day_of_week)
            print("\nStep 2: setting time")
            get_time()
        elif confirmation.lower() == "n":
            get_date()
        else:
            print('\nIncorrect value! Please use "y" for Yes and "n" for No!\n')

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
            print("\nInvalid time format! "
                  "Please provide the time in hh:mm format!\n")
            continue
    while True:
        confirmation = input("Do you confirm it? (y/n): ")
        if confirmation.lower() == 'y':
            event_data.append(entered_time)
            print('\nStep 3: selecting a title')
            get_title()
        elif confirmation.lower() == 'n':
            print('\nStep 2: setting time')
            get_time()
        else:
            print('\nIncorrect Value! '
                  'Please use "y" for Yes and "n" for No!\n')


def get_title():
    """
    Getting Title for the event that user want to add to the list
    """
    entered_title = input(
        "Please give your event a title!(Max 20 chrachters): "
    )[:20]
    while True:
        answer = input(
            f'\nYou provided this title "{entered_title}". '
            'Are you sure? (y/n) '
        )
        if answer.lower() == 'y':
            event_data.append(entered_title)
            print('\nStep 4: adding note')
            get_note()
        elif answer.lower() == 'n':
            print('\nStep 3: selecting a title')
            get_title()
        else:
            print('\nIncorrect Value! '
                  'Please use "y" for Yes and "n" for No!\n')


def get_note():
    """
    Getting Note for the tiltle that user has already selected.
    """
    entered_note = input("Please add a short note to the title!"
                         "(Max 150 chrachters): \n")[:150]
    while True:
        answer = input(f'\nYou provided below note: '
                       f'\n\n"{entered_note}"\n\nAre you sure? (y/n) ')
        if answer.lower() == 'y':
            event_data.append(entered_note)
            print('\nStep 5: saving data')
            save_data()
        elif answer.lower() == 'n':
            print('\nStep 4: adding note')
            get_note()
        else:
            print('\nIncorrect Value! '
                  'Please use "y" for Yes and "n" for No!\n')


def save_data():
    """
    Getting user confirmation for saving data or
    leading user to exit or edit date.
    """
    print(f'\nYou provided below information for your event:'
          f'\nDate: {event_data[0]}\nDay: {event_data[1]}\nTime: '
          f'{event_data[2]}\nTitle: '
          f'{event_data[3]}\nNote: {event_data[4]}')
    time.sleep(5)
    while True:
        confirmation = input("\nPlease select one of the followings!"
                             "\n1 = Save and exit\n2 = Save and add another "
                             "event\n3 = Exit without saving\n")
        if confirmation.lower() == '1':
            update_worksheet(event_data)
            print('\nHave a nice day and goodbye!')
            exit()
        elif confirmation.lower() == '2':
            update_worksheet(event_data)
            event_data.clear()
            get_date()
        elif confirmation.lower() == '3':
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
    time.sleep(1)


event_data = []
user_login()
