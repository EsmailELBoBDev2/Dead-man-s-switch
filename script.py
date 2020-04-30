import smtplib, threading, os, time, getpass, base64, keyring ## Install it `pip install keyring`, if you are using KWallet please see: https://github.com/jaraco/keyring#installation---linux
from email.mime.text import MIMEText
from datetime import datetime, timedelta, date
## Install it `pip install notify-run`, it's what make me send you the notifications
# from notify_run import Notify 


##  Check for days, If date right and if not i will send emails  
def check_day():
    today_file = read_from_files("today_date.txt", "r")
    tmr_file = read_from_files("tmr_date.txt", "r")
    tmr_file_hash = read_from_files("tmr_date_hash.txt", "r")
            
    if today_file != str(date.today()):
        input("\n\nYou already checked today, Please come next day!\n\n(Press Enter To Leave!)\n\n")
        exit()
    elif tmr_file == str(date.today()) and tmr_file_hash == str(encrypt_date(date.today())):
        login()
    elif today_file == "" and tmr_file == "" and tmr_file_hash == "":
        login()
    else :
        send_email()


## Checks password right
def login():
    user_password_input = input("Please type your password(or `exit` to leave or press ctrl + c): ") ## Here is your pass-code. If it's right the file will be written in tomorrow's date

    if user_password_input == user_password(): ##do not forget change this one too! 
        input("\n\nGlad to hear that you are alive!\ncome back tmr!\n\n(Press Enter To Leave!)\n\n")
        add_day()
        check_day()

    elif user_password_input.lower() == "exit":
        kill = 'pkill -f ' + os.path.basename(__file__) ## `os.path.basename(__file__)` code gets current name of this script so no need to update the name here everytime you change the script's name
        os.system(kill)


    elif user_password_input != user_password(): ##and this!
        def retry_password():
            for password_again in range(3):
                user_password_again = input("Password is wrong, Please type your password: ")
                if user_password_again.lower() == user_password():
                    input("\n\nGlad to hear that you are alive!\ncome back tmr!\n\n(Press Enter To Leave!)\n\n")
                    add_day()
                    check_day()
                    return True
                    break
                elif user_password_again.lower() == "exit":
                    kill = 'pkill -f ' + os.path.basename(__file__) ## `os.path.basename(__file__)` code gets current name of this script so no need to update the name here everytime you change the script's name
                    return True
                    break

        if retry_password() != True:
            print("\n\nSeems you dead, RIP i'm going to send emails now\n\n")
            send_email()
            input("\n\nEmails, Sent!\n\n(Press Enter To Leave!)\n\n")
            check_day()


def user_password():
    app_name = 'Dead Man Swtich APP'
    user_name = getpass.getuser()

    if keyring.get_password(app_name, user_name) == None:
        user_password_input = input("I assume it's your first time here so please add your password(first time only): ")
        keyring.set_password(app_name, user_name, user_password_input)
        user_password = keyring.get_password(app_name, user_name)
        return user_password

    elif keyring.get_password(app_name, user_name) != None:
        user_password = keyring.get_password(app_name, user_name)
        return user_password    


## Adds day on today's date to check next time when you open
def add_day():
    # decrypt = base64.decodebytes(today_date)
    # decrypt2 = base64.decodebytes(end_date)
    today = write_to_files("today_date.txt", "w", str(date.today()))

    tmr_date_encrypt = str(encrypt_date(date.today() + timedelta(days=1)))
    tmr_hash = write_to_files("tmr_date_hash.txt", "w", tmr_date_encrypt)
    tmr = write_to_files("tmr_date.txt", "w", str(date.today() + timedelta(days=1)))


## To ensure safty of saved dates
def encrypt_date(data):
    day = str(data)
    day_date = day.encode('utf-8')
    encrypt = base64.b64encode(day_date)
    return encrypt.decode('utf-8')


# Read Dates from files 
def read_from_files(fileName, accessMode):
    try:
        with open(fileName, accessMode) as name:
            file = name.readline()
        return file
    except FileNotFoundError:
        input("Please create a file called 'tmr_date.txt', 'today_date.txt' and 'tmr_date_hash.txt'\n\n(Press Enter To Leave!)\n\n")
    except:
        input("\n\nOops, something went wrong\n\n(Press Enter To Leave!)\n\n")   


# Write Dates to files
def write_to_files(fileName, accessMode, data):
    try:
        file = open(fileName, accessMode)
        file.write(data)
    except:
        input("\n\nOops, something went wrong while writing date to files\n\n(Press Enter To Leave!)\n\n")    
    finally:
        file.close()



## Sends emails to people you mentioned after you die
def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("{YOUR EMAIL}@gmail.com", "{YOUR PASSWORD}") ##Type your email and password here
    s.set_debuglevel(1)
    msg = MIMEText("""BODY OF THE EMAIL (The message)""") ##Type your message here
    sender = '{YOUR EMAIL}@gmail.com' ##Again, type your email here
    recipients = ['{YOUR Friend}@gmail.com', '{Your Family}@hotmail.com', '{Your Teacher}@yahoo.com'] ##type people to send them the email here
    msg['Subject'] = "SUBJECT OF THE EMAIL (The Title/Name)" ##subject of the email
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.sendmail(sender, recipients, msg.as_string())




## Enable it when you are on phone, due its useless on PC because script run on startup only but on phone it will be run most of time
## To make it works, install it inside your termux type `pip install notify-run` then type `notify-run register` and go to link and subscribe inside your browser and keep it open whole day (the borwser and the script)
# def notify_repeter():
#     starttime = time.time()
#     while True:
#         notify = Notify()
#         notify.send('Dead Man\'s Switch App\nDo not forget to Check Your Dead Man\'s switch app')
#         time.sleep(21600.0 - ((time.time() - starttime) % 60.0)) # Time in seconds


# def notify_thereder():
#     notify_thread = threading.Thread(target=notify_repeter)
#     notify_thread.start()

## Start Notifications System
# notify_thereder()
## Start the app
check_day()

