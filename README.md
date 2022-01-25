# create-email
Personal browser email signup automation to quickly create new emails using outlook

# What does it do?
Using Selenium, this python script will open a browser and fully automate the signup process of emails. This script was made for me personally as I am someone who is constantly making emails to avoid having 'all my eggs in one basket', meaning if one email was comprised, the other emails and accounts are indepedent from eachother and should be secure

# What do I need to run this?
Python 3.6+
* Selenium - installed by pip here: https://selenium-python.readthedocs.io/installation.html or ``` pip install selenium ```
* Tor and Firefox
* WebDriver for Firefox

# How to use?
You can simply run the script and the singup process is automatically done. You can do this via the create-email.sh file or manually execute the script in terminal.

However, due to spammers, most email providers will have human verification and Microsoft Outlook provides the easier verification, reCAPTCHA. At the end, the script will display the username and password in terminal for you to see. However, once you close the teriminal, you will not be able to recover the username and password so make sure you keep note of the account information (or don't, who cares you can make another one)

You'll also need to change the directory paths in the script to match yours
