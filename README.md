## My To Do List
It is a python command-line interface app which runs in Code Institute mock terminal in Heroku. Users can keep their tasks with date, time, title and a short note through this app. The data is stored in a google sheet which has already been integrated with the app.<br>
[Here is live version of my project](link)<br>
![App in different screens](pic link)
## How does it work?
It is supper easy. App gets required information step by step. It instructs and helps users to add their information easily. If you are new user, you open an account and then start adding event/tasks. It takes about 1 minute to add one single event and save it. When you come next time, you just need to log in with your username and possword and then see what are upcomming events/tasks. Then you can exit or add a new task.
## Features
There are 8 features in this app. Each feature communicates with user and instruct user to do the right job. In some of features, user must provide information in a special format. Otherwise user receives error message and is redirected to previous feature. After providing correct information, app gets final confirmation from user and then take user to the next feature. I will explain each features below:
### Create Account feature
Those users who use the app for the first time, will be directed to this feature to open an account. They are asked to enter first and last name and set a username and password. The feature first check for the same username in data base, if could find anything, then user will be signed up and start adding first event/task.<br>
![Create Account function](screen shot link)
### Log in feature
If user has already an account, he/she just need to enter username and password, and log in to the account and starts adding new event/tasks. App checks username and password in data base, and when everything is fine, takes user to his/her account.<br>
![Log in function](screen shot link)
### Show Event List teature 
This feature checks all the enteries of a user and if user has an event/task in current date or in future date, list all of them after log in.<br>
![Show Event List function](screen shot link) 
### Get Date feature
This feature get date when task should be done. User should enter date according to proper date format which is dd.mm.yyyy, otherwise receives an error message.<br>
![Get Date function](screen shot link)
### Get Time feature 
This feature get time when task should be done. User should enter time according to proper time format which is hh:mm, otherwise receives an error message.<br>
![Get Time function](screen shot link)
### Get Title feature
User give a title for the event/task. But the title length should not be more than 20 charactors.<br>
![Get Title function](screen shot link)
### Get Note feature
User write a short explanation about the event/task using 150 charactors.<br>
![Get Note function](screen shot link) 
### Save Data feature 
When user provide with all required data, this feature once gathered all of them in one place and get the final user's confirmation. User has 3 options, save and exit, save and add another event, and exit without save.<br>
![Save Data function](screen shot link)
### Update Worksheet feature
If user select to save data, this feature uploads all data to google sheet in user's worksheet and make user sure that all data has been saved successfully.<br>
![Save Data function](screen shot link)
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
## Testing
I have manualy tested this project as followings:<br>
- I passed through PEP8 Python Validator and confirmed that there are no errors.
- I gave correct and incorrect inputs to all the features manually in my lockal and Heroku terminal and got expected behavior from app.
## Bugs
### Solved Bugs
During developing this app, I fount some bugs and fixed them. But the last one and the most important one was this bug: users could sign up to a new accout with just empty input for first name, last name, username and password. I just added an if-else using strip() method to mentioned inputs and fixed the bugs.<br>
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
- Set the buildbacks to Python and NodeJS in that order
- Like the Heroku app to the repository
- Click on Deploy



 







![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
