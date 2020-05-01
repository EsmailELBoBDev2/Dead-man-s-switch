# Dead man's switch
An open source alt for https://www.deadmansswitch.net/ that written in python
___
**I'm done now from developing it** *so feel free to use it now*
## WTFrick is that ?
It's an app that sends emails to all people you select after you die in case you wanted to say last words or there is info like bank accouns or your PC password or anything you wanted to say
___
## How It Works:
First it will check date of your PC and if date is right (along with it's base64 as sort of security) it will ask you to add your password (that you will setup first time you open the app) then it will add one more day to the file to come back next day and do the same

**NOTE**: first time files **MUST** be empty (*today_date.txt, tmr_date.txt and tmr_date_hash.txt*) and do not play in files because if you did the app will send emails so just keep everything in place and if you want to move it just move the script with files
___
## How to use it:
All you need is python (of course) then install this package `pip install keyring` to ensure you not get errors and go to "send_email()" function and add your login data, email, your people who want to send them emails and the message itself and that's it you are ready to go :) — if you got any problems or ideas or anything do not think twice and open a issue ticket to help you
___
## If you want to run the script on startup:

* Linux: Open your statup manager (*Session and Startup in xfce4*) then click on add and type the name you want and the description you want then in command field type:
```
{Your Terminal Name's Here, EX: xfce4-terminal} --command "python3.8 script.py"
```
then move the script.py to your home dir


* Windows: Create a `.bat` file and type:
```
@echo off
start "{Name Your Want}" "{Your Script Dir}"
```
then move that file to startup folder or press win + r and type `shell:startup`
___
If you are getting error and can't login using your gmail then go to: https://myaccount.google.com/lesssecureapps then click to allow it
___
## If you want to run this script on your android phone (*wait unitl find a way for iPhones*) 
You need to install app like *termux* then run `pkg install python` then run `termux-setup-storage` and allow storage permission and now download my script into your downloads folder on phone not in SD card then on termux type `cd storage` then `cd downloads` then `python script.py` and do not forget to create the today_date.txt and tmr_date.txt files and better be empty
___
## This Script Under GNU GPL v3 License
