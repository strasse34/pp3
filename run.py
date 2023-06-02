# import gspread
# from google.oauth2.service_account import Credentials
import datetime
# import sys

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('to_do_list')


# def get_date():
#     """
#     This function get date from user according to provided format using try-except.
#     In case of value error, loop repeat untile getting required date format.
#     """
#     while True:
#         entered_date = input("Step 1: setting date\nPlease set a date (dd.mm.yyyy): ")

#         try:
#             date_validation = datetime.datetime.strptime(entered_date, "%d.%m.%Y")
#             selected_date = date_validation.strftime("%d.%m.%Y")
#             day_of_week = date_validation.strftime("%A")
#             print(f"\nYou seleceted this date: {day_of_week}, {selected_date}")
#             break

#         except ValueError:
#             print("\nInvalid date format! Please provide the date in the format dd.mm.yyyy!\n")
#             continue

#     get_date_confirmation()
#     date = [selected_date, day_of_week]
#     return date


def get_time():
    """
    Getting time for the job that user want to add to the list
    """
    while True:
        entered_time = input("Please pick a time (Example: 14:30): ")
        
        try:
            time_validation = datetime.datetime.strptime(entered_time, "%H:%M")
            print(f"\nYou seleceted this time: {entered_time}")
            break

        except ValueError:
            print("\nInvalid time format! Please provide the time in the format hh:mm !\n")
            continue

    # get_time_confirmation()
    print(entered_time)
    return entered_time


get_time()


# def get_date_confirmation():
#     confirmation = input("Do you confirm it? (y/n): ")
#     if confirmation.lower() == 'y':
#         print('Step 2: setting time')
#         get_time()
#     else:
#         print("pleaes set another date!")    
#         get_date()


# def get_time_confirmation():
#     confirmation = input("Do you confirm it? (y/n): ")
#     if confirmation.lower() == 'y':
#         print('Step 3: selecting a title')
#         get_title()
#     else:
#         print("pleaes set another time!")    
#         get_time()


# def update_worksheet(event):
#     """
#     Updating the user worksheet in google sheet with new to do list.
#     """
#     print("Saving date ...\n")
#     user_worksheet = SHEET.worksheet("josef_123")
#     user_worksheet.append_row(event)
#     print("New event successfully saved!\n")


# def collect_event_date():
#     event = confirmed_date
#     event.append(confirmed_time)
#     event.append(confirmed_title)
#     print(event)
#     return event


# confirmed_date = get_date()
# confirmed_time = get_time()
# confirmed_title = get_title()
# event = collect_event_date()
# update_worksheet(event)
