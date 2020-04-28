import smtplib
import time
from email.mime.text import MIMEText
from datetime import datetime, timedelta, date
from itertools import islice
from notify_run import Notify ## Install it `pip install notify-run`



##  Check for days, If date right and if not i will send emails  
def check_day():
    try:
        today_date = "today_date.txt"
        tmr_date = "tmr_date.txt"
        accessMode = "r"
            

        with open(today_date, accessMode) as today:
            today_file = today.readline()
        
        with open(tmr_date, accessMode) as tmr:
            tmr_file = tmr.readline()



        if today_file == str(date.today()) or tmr_file == str(date.today()):
            login()
        elif today_file == "" or tmr_file == "":
            login()
        elif tmr_file != str(date.today()):
            send_email()
    except FileNotFoundError:
        input("Please create a file called 'tmr_date.txt' and 'today_date.txt'\n\n(Press Enter To Leave!) ")
    

## Checks password right
def login():
    user_password = input("Please type your password: ") ## Here is your pass-code. If it's right the file will be written in tomorrow's date

    if user_password.lower() == "password": ##do not forget change this one too! 
        input("Glad to hear that you are alive!\ncome back tmr!\n\n(Press Enter To Leave!) ")
        add_day()

    elif user_password.lower != "password": ##and this!
        def retry():
            for password in range(3):
                user_password_again = input("Password is wrong, Please type your password: ")
                if user_password_again.lower() == "password" :
                    return "Logged in"
                    break

        if retry() != "Logged in" :
            print("\n\nSeems you dead, RIP i'm going to send emails now\n\n")
            send_email()
            input("\n\nEmails, Sent!\n\n(Press Enter To Leave!) ")

## Adds day on today's date to check next time when you open
def add_day():
    EndDate = date.today() + timedelta(days=1) ##It will add one more day on today's date so feel free to change "days" if you want it add 2 days or more instead.
    try:
        today_date = "today_date.txt"
        tmr_date = "tmr_date.txt"
        accessMode = "w"
        
        today = open(today_date, accessMode)
        tmr = open(tmr_date, accessMode)
        today.write(str(date.today()))
        tmr.write(str(EndDate))
    except:
        print("There is an error!")
    finally:
        today.close()
        tmr.close()
            
## Sends emails to people you mentioned after you die
def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("YOUR_USERNAME@gmail.com", "YOUR_PASSWORD") # Type your email and password here to login
    s.set_debuglevel(1)
    msg = MIMEText("""Hey, Test""") # Type your message here
    sender = 'YOUR_USERNAME@gmail.com' # Again, type your email here
    recipients = ['YOU_FRIEND_EMAIL@gmail.com', 'YOUR_FAMILY_EMAIL@hotmail.com', 'YOUR_TEACHER@yahoo.com'] # Type people to send them the email here
    msg['Subject'] = "I'm dead" # Subject of the email
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.sendmail(sender, recipients, msg.as_string())







            


## Enable it when you are on phone, due its useless on PC because script run on startup only but on phone it will be run most of time

## To make it works, install it inside your termux type `pip install notify-run` then type `notify-run register` and go to link and subscribe inside your browser and keep it open whole day (the borwser and the script)

# def check_notify():
#     notify = Notify()
#     notify.send('Dead Man\'s Switch App\nDo not forget to Check Your Dead Man\'s switch app')

#     time.sleep(60) ## Time in seconds - Checks Every 60 Seconds

# while True:
#     check_notify()





## Start the app
check_day()


