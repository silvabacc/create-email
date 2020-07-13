#Generate the username and password in this cell
import requests
import secrets
import string
import random

#Password sequeence generation - creates 20 character password
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(20))

#Username creation
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()
byteUsername = WORDS[random.randint(0,25487)] + WORDS[random.randint(0,25487)]

randomUsername = byteUsername.decode("utf-8")
randomPassword = password

#Browser automation done in this cell
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Open browser
driver = webdriver.Chrome()
driver.get("https://signup.live.com/?lic=1")

def waitForBrowser(elements):
    error = False
    
    for i in range(len(elements)):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, elements[i]))
                )
            except:
                error = True
    
    if(error == True):
        print("Problem with elements: ")
        print(elements)
        
waitForBrowser(['MemberName','iSignupAction'])
    
#Fill in username signup field
username = driver.find_element_by_id('MemberName')
username.send_keys(randomUsername+"@hotmail.com")

#Continue to the next page
driver.find_element_by_id('iSignupAction').click()

waitForBrowser(['PasswordInput', 'iSignupAction'])

driver.find_element_by_id('PasswordInput').send_keys(randomPassword)
driver.find_element_by_id('iSignupAction').click()

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

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'identity'))
    )
except:
    print("Problem with finding domain, most likely to be @outlook.com")
    
randomUsername = driver.find_element_by_class_name('identity').text

print("Human verification needed")
print("New email account username: " + randomUsername)
print("Password: " + randomPassword)
