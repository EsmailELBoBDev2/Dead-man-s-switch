# Dead man's switch
An open source alt for https://www.deadmansswitch.net/ that written in python
___
**I'm done from developing it** *so feel free to use it now*
## WTFrick is that ?
It's an app that sends emails to all people you select after you die in case you wanted to say last words or there is info like bank accounts or your PC password or anything you wanted to say
___
## How It Works:
First it will check date of your PC and if date is right (along with it's base64 as sort of "encryption" to avoide people change date) it will ask you to add your password (that you will setup first time you open the app) then it will add one more day to the file to come back next day and do the same thing over and over until you die!

**NOTE**: first time the file **MUST** be empty (*data.txt*) and do not play in files because if you did the app will send the emails so just keep everything in place and if you want to move it just move the script with the file
___
## How to use it:
All you need is python (of course) then install this package `pip install keyring` to ensure you get no errors and go to "send_email()" function and add your login data, email, your people who send them email when you die and the message itself and that's it you are ready to go :) — if you got any problems or ideas or anything do not think twice and open a issue ticket
___
## If you want to run the script on startup:

* Linux: Open your startup manager (*Session and Startup in xfce4*) then click on add and type the name you want and the description you want then in command field type:
```
{Your Terminal Name's Here, EX: xfce4-terminal} --command "python3.8 script.py" (*which* `script.py` *is the name of the script*)
```
then move the script.py to your home dir (*or where you want but do not forget to write full path*)


* Windows: Create a `.bat` file and type:
```
@echo off
start "{Name Your Want}" "{Your Script Dir}"
```
then move that file to startup folder or press win + r and type `shell:startup`
___
If you are getting error and can't login using your gmail go to: https://myaccount.google.com/lesssecureapps then click to allow it
___
## If you want to run this script on your android phone (*wait unitl find a way for iPhones*) 
You need to install app like *termux* then run `pkg install python` then run `termux-setup-storage` (*tested in termux app, did not test others*) and allow storage permission and now download my script into your downloads folder (*or any place you want but downloads folder is more easy to access*) in phone storage not in SD card (*again you could do it in your SD card but phone storage is more easy to access from the app*) then on termux type `cd storage` then `cd downloads` then `python script.py` (`script.py` *is the name of the script so if you changed the name do not forget to change it here too*) and do not forget to create the data.txt file and better be empty
___
## This Script Under GNU GPL v3 License
