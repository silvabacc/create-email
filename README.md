# create-email
Browser email signup automation to quickly create new emails using outlook

# What does it do?
Using Selenium, this python script will open a browser and fully automate the signup process of emails. This script was made for me personally as I am someone who is constantly making emails to avoid having 'all my eggs in one basket', meaning if one email was comprised, the other emails and accounts are indepedent from eachother and should be secure

# What have I learned?
I have learned the fundamentals of using Selenium for automation of browser tasks. I learned about account security and reviewed algorithms to create passwords. I've learned a lot about HTML, CSS and JavaScript for websites and can gather information from websites as well as interact with the web elements.

# How did I create usernames and passwords
To create usernames, I used a online dictionary to receieve two random words and combined them together to create the username. Most of the time usernames in this manner are successful and won't need manually changing

To create passwords, I used the Diceware Passphrsae method found here: http://world.std.com/~reinhold/diceware.html. The method involves rolling a virtual die 5 times and recording each digit from the rolls. The recorded numbers are then used against a lookup table of words (found in the diceware.wordlist.txt file). Since it is a local file, the lookup is extremely quick

Anything above 15 characters is typically safe password. In my personal opinion, length matters more than complexity. The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

# What do I need to run this?
Python 3.6+
* Selenium - installed by pip here: https://selenium-python.readthedocs.io/installation.html or ``` pip install selenium ```
* WebDriver for Chrome

# How to use?
You can simply run the script and the singup process is automatically done. You can do this via the create-email.sh file or manually execute the script in terminal.

However, due to spammers, most email providers will have human verification and Microsoft Outlook provides the easier verification, reCAPTCHA. At the end, the script will display the username and password in terminal for you to see. However, once you close the teriminal, you will not be able to recover the username and password so make sure you keep note of the account information (or don't, who cares you can make another one)

# Why not use APIs?
From the research I have done, I could not find any email providers that allowed their APIs to create emails. 

# Improvements?
The biggest problem with automating the creation of emails is human verification. The script made here stops when human verification is required (which is the last step), so a big improvement to this script is handling human verification. Also having a GUI instead of text-based UI (console) is probably easier to run and read text off.
