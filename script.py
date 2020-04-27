import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta, date


def add_day():
    EndDate = date.today() + timedelta(days=1) # It will add one more day on today's date so feel free to change "days" if you want it add 2 days or more instead.

    fileName = "date.txt"
    accessMode = "w"

    myFile = open(fileName, accessMode)

    myFile.write(str(EndDate))

    myFile.close()
            

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



def check_day():
    try:
        fileName = "date.txt"
        accessMode = "r"
    
        with open(fileName, accessMode) as myFile:
            firstline = myFile.readline()
        if firstline == str(date.today()):
            login()
        elif firstline == "":
            login()
        elif str(date.today()) == str(date.today()):
            login()
        elif firstline != str(date.today()):
            send_email()
    except FileNotFoundError:
        input("Please create a file called 'date.txt'\n\n(Press Enter To Leave!) ")
    

def login():
    user_password = input("Please type your password: ") # Here is your pass-code. If it's right the file will be written in tomorrow's date

    if user_password.lower() == "password": #do not forget change this one too! 
        input("Glad to hear that you are alive!\ncome back tmr!\n\n(Press Enter To Leave!) ")
        add_day()

    elif user_password.lower != "password": #and this!
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

            

# Calling the function
check_day()

