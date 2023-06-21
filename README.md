# My To Do List
It is a python command-line interface app which runs in Code Institute mock terminal in Heroku. Users can keep their tasks with date, time, title and a short note through this app. The data is stored in a google sheet which has already been integrated with the app.<br>
[Here is live version of my project](link)<br>
![App in different screens](pic link)
#How does it work?
It is supper easy. App gets required information step by step. It instructs and helps users to add their information easily. If you are new user, you open an account and then start adding event/tasks. It takes about 1 minute to add one single event and save it. When you come next time, you just need to log in with your username and possword and then see what are upcomming events/tasks. Then you can exit or add a new task.
# Reatures
There are 8 features in this app. Each feature communicates with user and instruct user to do the right job. In some of features, user must provide information in a special format. Otherwise user receives error message and is redirected to previous feature. After providing correct information, app gets final confirmation from user and then take user to the next feature. I will explain each features below:
## Create Account feature
Those users who use the app for the first time, will be directed to this feature to open an account. They are asked to enter first and last name and set a username and password. The feature first check for the same username in data base, if could find anything, then user will be signed up and start adding first event/task.<br>
![Create Account function](screen shot link)
## Log in feature
If user has already an account, he/she just need to enter username and password, and log in to the account and starts adding new event/tasks. App checks username and password in data base, and when everything is fine, takes user to his/her account.<br>
![Log in function](screen shot link)
## Show Event List teature 
This feature checks all the enteries of a user and if user has an event/task in current date or in future date, list all of them after log in.<br>
![Show Event List function](screen shot link) 
## Get Date feature
This feature get date when task should be done. User should enter date according to proper date format which is dd.mm.yyyy, otherwise receives an error message.<br>
![Get Date function](screen shot link)
## Get Time feature 
This feature get time when task should be done. User should enter time according to proper time format which is hh:mm, otherwise receives an error message.<br>
![Get Time function](screen shot link)
## Get Title feature
User give a title for the event/task. But the title length should not be more than 20 charactors.<br>
![Get Title function](screen shot link)
## Get Note feature
User write a short explanation about the event/task using 150 charactors.<br>
![Get Note function](screen shot link) 
## Save Data feature 
When user provide with all required data, this feature once gathered all of them in one place and get the final user's confirmation. User has 3 options, save and exit, save and add another event, and exit without save.<br>
![Save Data function](screen shot link)
## Update Worksheet feature
If user select to save data, this feature uploads all data to google sheet in user's worksheet and make user sure that all data has been saved successfully.<br>
![Save Data function](screen shot link)

 







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
