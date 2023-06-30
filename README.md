## My To Do List
It is a Python command-line interface app that runs in Code Institute mock terminal in Heroku. The users can keep their tasks with date, time, title and a short note through this app. The data is stored in a Google sheet which has already been integrated with the app.<br>
[Here is live version of my project](https://ci-to-do-list-7e3f284eb751.herokuapp.com//)<br>
## How does it work?
It is super easy. The app gets the required information step by step. It instructs and helps the users to add their information easily. If you are a new user, you open an account and then start adding events/tasks. It takes about 1 minute to add one single event and save it. When you come next time, you just need to log in with your username and password and then see what are upcoming events/tasks. Then you can exit or add a new task.
## Features
There are 9 features in this app. Each feature communicates with the user and instructs the user to do the right job. In some of the features, the user must provide information in a special format. Otherwise, the user receives an error message and is redirected to the previous feature. After providing correct information, the app gets final confirmation from the user and then takes the user to the next feature. I will explain each feature below:
### Create Account feature
Those users who use the app for the first time will be directed to this feature to open an account. They are asked to enter their first and last names and set a username and password. Firstly, the feature check for the same username in database, if could not find anything, then the user will be signed up and start adding the first event/task.<br>
![Create Account function](https://github.com/strasse34/pp3/blob/main/screenshots/create-account.png)
### Log in feature
If the user has already an account, he/she just need to enter a username and password, log in to the account, and starts adding new event/tasks. App checks username and password in database, and when everything is fine, takes the user to his/her account.<br>
![Log in function](https://github.com/strasse34/pp3/blob/main/screenshots/user-loggingin.png)
### Show Event List feature 
This feature checks all the entries of the user and if the user has an event/task on the current date or in a future date, lists all of them after logging in.<br>
![Show Event List function](https://github.com/strasse34/pp3/blob/main/screenshots/show-event-list.png) 
### Delete Account feature
This feature comes after Show Event List feature and gives the option of account deletion. Users can easily delete their account and associated data. When a user chooses to delete their account, all their information, including username, password, and personal details, is permanently removed from the system. Additionally, the user's individual worksheet, where they store their event data, is also deleted. <br>
![Delete Account function](https://github.com/strasse34/pp3/blob/main/screenshots/delete-account.png)
### Get Date feature
This feature gets the date when the event/task should be done. the user should enter the date according to the proper date format which is dd.mm.yyyy. Otherwise, the user receives an error message.<br>
![Get Date function](https://github.com/strasse34/pp3/blob/main/screenshots/get-date.png)
### Get Time feature 
This feature gets the time when task should be done. the user should enter the time according to the proper time format which is hh:mm. Otherwise, the user receives an error message.<br>
![Get Time function](https://github.com/strasse34/pp3/blob/main/screenshots/get-time.png)
### Get Title feature
The user gives a title for the event/task. But the title length should not be more than 20 characters.<br>
![Get Title function](https://github.com/strasse34/pp3/blob/main/screenshots/get-title.png)
### Get Note feature
The sser writes a short explanation about the event/task using 150 characters.<br>
![Get Note function](https://github.com/strasse34/pp3/blob/main/screenshots/get-note.png) 
### Save Data feature 
When the user provides all the required data, this feature once gathered all of them in one place and gets the final user's confirmation. The user has 3 options, save and exit, save and add another event, and exit without saving.<br>
![Save Data function](https://github.com/strasse34/pp3/blob/main/screenshots/save-data.png)
### Update Worksheet feature
If the user selects to save data, this feature uploads all data to Google sheet in user's worksheet and makes the user sure that all data has been saved successfully.<br>
![Save Data function](https://github.com/strasse34/pp3/blob/main/screenshots/update-worksheet.png)
## Data Model
The data model in this project represents the structure and organization of the to-do list events. The data is stored and managed using Google Sheets.<br>
### Event Data Structure
Each event in the to-do list consists of the following properties:<br>
- Date: The date of the event in the format dd.mm.yyyy.
- Day of Week: The day of the week corresponding to the event date.
- Time: The time of the event in the format hh:mm.
- Title: The title or description of the event, limited to a maximum of 20 characters.
- Note: A short note or additional information about the event, limited to a maximum of 150 characters.
### Google Sheets Integration
The project integrates with Google Sheets to store and manage the to-do list data. It uses the 'gspread library' and 'Google OAuth 2.0' authentication to access the Google Sheets API.
### Credentials
To access the Google Sheets API, the project requires valid credentials stored in a 'creds.json' file. The credentials should be obtained from the Google Cloud Console and granted appropriate permissions for accessing and modifying the target Google Sheets document.
## Dependencies and Libraries
This project relies on several dependencies and libraries to implement its functionality. These dependencies enable integration with Google Sheets, handling date and time, and performing other necessary operations. Here are the key dependencies and libraries used in this project:<br>
### gspread
'gspread' is a Python library that provides an easy-to-use interface for accessing Google Sheets. It allows the project to read, write, and manipulate data in Google Sheets.<br>
### google-auth and google-auth-oauthlib
The 'google-auth' and 'google-auth-oauthlib' libraries provide authentication and authorization functionality for interacting with Google APIs. In this project, they are specifically used for Google Sheets integration, enabling secure access to the Google Sheets API.<br>
### datetime
The 'datetime' module is a built-in Python module that provides classes for manipulating dates and times. It is used in this project to handle date and time-related operations, such as comparing dates and formatting them according to the required format.<br>
### sys
The 'sys' module is a built-in Python module that provides access to system-specific parameters and functions. It is used in this project to handle system-related operations, although its usage details are not explicitly mentioned in the provided code snippet.
### time
The 'time' module is a built-in Python module that provides various time-related functions. It is used in this project to introduce delays or pauses between certain operations, providing a smoother user experience.
### re
The 're' module in Python provides support for working with regular expressions. Regular expressions are powerful patterns that allow you to search, extract, and manipulate strings based on specific patterns of characters. With 're', you can perform operations such as searching, replacing, and splitting strings using these patterns. It's a valuable tool for tasks like data validation, text processing, and parsing.
## Testing
I have manually tested this project as followings:<br>
- I passed through PEP8 Python Validator and confirmed that there are no errors.
- I gave correct and incorrect inputs to all the features manually in my lockal and Heroku terminal and got the expected behavior from the app.
## Bugs
### Solved Bugs
During developing this app, I found some bugs and fixed them. But the last one and the most important one was this bug: users could sign up for a new account with just empty input for first name, last name, username, and password. I just added an if-else using strip() method to mentioned inputs and fixed the bugs.<br>
### Remaining Bugs
There are no remaining bugs.
## Validator Testing
### PEP8
No error were returned from PEP8online.com
## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.<br>
steps for deployment:<br>
- Fork or clone this repository
- Create a new Heroku app
- Set the build backs to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy
## Credit
- Code Institute for deployment terminal
- Internet free content for learning Python
