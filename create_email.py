# Generate the username and password in this cell
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import requests
import random
import re
import mmap

# Username creation
# Randomly receieve two words from the english dictionary and combine them

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()
byteUsername = WORDS[random.randint(
    0, 25487)] + WORDS[random.randint(0, 25487)]

# Password sequeence generation
# numberList is an list that contains the lookup numbers for the wordlist file (diceware.wordlist.txt)

numberList = []
password = ""

# Loop that fills in the numberList array for the lookup
for i in range(5):
    number = ""
    for j in range(5):
        dieRoll = random.randint(1, 5)
        number = number + str(dieRoll)
    numberList.append(number)

# Open file with the wordlist containing memorable words
# Each word is given an number, which matches with one of the numbers in numberList
file_path = "diceware.wordlist.txt"
with open(file_path) as FileObj:
    for lines in FileObj:
        word = re.split(r'\t+', lines.rstrip('\t'))
        for i in range(len(numberList)):
            if(word[0] == numberList[i]):
                password = password + str(word[1]).title()

randomUsername = byteUsername.decode("utf-8")
randomPassword = re.sub('\s+', '', password)

# Browser automation done in this cell

# Open browser
driver = webdriver.Chrome()
driver.get("https://signup.live.com/?lic=1")

# Method to check if the web elements being used on the page are present
# Takes a list of element ids (string) from the webpage and checks if it is present
# Run this method before interacting with any elements


def waitForBrowser(elements):
    for i in range(len(elements)):
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, elements[i]))
        )

        # Check if the element is clickable (for the signup buttons)
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, elements[i]))
        )


# Check if the the elements with IDs MemberName and iSignupAction are loaded and present on the page
waitForBrowser(['MemberName', 'iSignupAction'])

# Fill in username signup field
username = driver.find_element_by_id('MemberName')
username.send_keys(randomUsername+"@hotmail.com")

# Continue to the next page
driver.find_element_by_id('iSignupAction').click()

waitForBrowser(['PasswordInput', 'iSignupAction'])

driver.find_element_by_id('PasswordInput').send_keys(randomPassword)
driver.find_element_by_id('iSignupAction').click()

# Filling in personal details
waitForBrowser(['FirstName', 'LastName', 'iSignupAction'])

driver.find_element_by_id('FirstName').send_keys("noone")
driver.find_element_by_id('LastName').send_keys("noone")
driver.find_element_by_id('iSignupAction').click()

waitForBrowser(['BirthDay', 'BirthMonth', 'BirthYear', 'iSignupAction'])

selectBirthDay = driver.find_element_by_id('BirthDay')
selectBirthMonth = driver.find_element_by_id('BirthMonth')
selectBirthYear = driver.find_element_by_id('BirthYear')

select_object = Select(selectBirthDay)
select_object.select_by_index(1)

select_object = Select(selectBirthMonth)
select_object.select_by_index(1)

select_object = Select(selectBirthYear)
select_object.select_by_index(32)

driver.find_element_by_id('iSignupAction').click()

# Obtaining the email address
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'identity'))
    )
except:
    print("Problem with finding domain, most likely to be @outlook.com")

randomUsername = driver.find_element_by_class_name('identity').text

# Human verification is needed to finish the signup process
print("Human verification needed")

# Information about the new email is printed
print("New email account username: " + randomUsername)
print("Password: " + randomPassword)
