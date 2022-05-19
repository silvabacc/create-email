import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import requests
import random
import re
import mmap
import os


class CreateEmail:
    def __init__(self):
        self.driver = None  # Will later be assigned in setTorBrowserSettings()
        self.username = self.createUserName()
        self.password = self.createPassword()
        self.setTorBrowserSettings()

    # Password sequeence generation
    # numberList is an list that contains the lookup numbers for the wordlist file (diceware.wordlist.txt)
    def createPassword(self):
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

        randomPassword = re.sub('\s+', '', password)
        return randomPassword

    # Username creation
    # Randomly receieve two words from the english dictionary and combine them
    def createUserName(self):
        word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' } 
        response = requests.get(word_site, headers=headers)
        WORDS = response.content.splitlines()
        byteUsername = WORDS[random.randint(
            0, 25487)] + WORDS[random.randint(0, 25487)]

        randomUsername = byteUsername.decode("utf-8")
        return randomUsername

    # Tor browser settings
    def setTorBrowserSettings(self):
        #Update these variables to your local machine's paths. 
        tor_exe_path = r'C:\...\Tor Browser\Browser\TorBrowser\Tor\tor.exe'
        profile_default_path = r'C:\...\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default'
        firefox_options_binary_location = r'C:\...\Mozilla Firefox\firefox.exe' #Default place is Program Files


        torexe = os.popen(tor_exe_path) 
        profile = FirefoxProfile(profile_default_path) 
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', '127.0.0.1')
        profile.set_preference('network.proxy.socks_port', 9050)
        profile.set_preference("network.proxy.socks_remote_dns", False)
        profile.update_preferences()

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = firefox_options_binary_location
        self.driver = webdriver.Firefox(firefox_profile=profile, options=firefox_options,
                                        executable_path='geckodriver-v0.27.0-win64/geckodriver.exe')

    # Open browser
    def runBrowser(self):
        self.driver.get("https://signup.live.com/?lic=1")

        # Check if the the elements with IDs MemberName and iSignupAction are loaded and present on the page
        self.waitForBrowser(['MemberName', 'iSignupAction'])

        # Fill in username signup field
        usernameElement = self.driver.find_element_by_id('MemberName')
        usernameElement.send_keys(self.username+"@hotmail.com")

        # Continue to the next page
        self.driver.find_element_by_id('iSignupAction').click()

        self.waitForBrowser(['PasswordInput', 'iSignupAction'])

        self.driver.find_element_by_id(
            'PasswordInput').send_keys(self.password)
        self.driver.find_element_by_id('iSignupAction').click()

        # Filling in personal details
        self.waitForBrowser(['FirstName', 'LastName', 'iSignupAction'])

        self.driver.find_element_by_id('FirstName').send_keys("noone")
        self.driver.find_element_by_id('LastName').send_keys("noone")
        self.driver.find_element_by_id('iSignupAction').click()

        self.waitForBrowser(['BirthDay', 'BirthMonth',
                             'BirthYear', 'iSignupAction'])

        selectBirthDay = self.driver.find_element_by_id('BirthDay')
        selectBirthMonth = self.driver.find_element_by_id('BirthMonth')
        selectBirthYear = self.driver.find_element_by_id('BirthYear')

        select_object = Select(selectBirthDay)
        select_object.select_by_index(1)

        select_object = Select(selectBirthMonth)
        select_object.select_by_index(1)

        select_object = Select(selectBirthYear)
        select_object.select_by_index(32)

        self.driver.find_element_by_id('iSignupAction').click()

        # Obtaining the email address
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'identity'))
            )
        except:
            print("Problem with finding domain, most likely to be @outlook.com")

        usernameWithDomain = self.driver.find_element_by_class_name(
            'identity').text

        # Human verification is needed to finish the signup process
        print("Human verification needed")

        # Information about the new email is printed
        print("New email account username: " + usernameWithDomain)
        print("Password: " + self.password)

    # Method to check if the web elements being used on the page are present
    # Takes a list of element ids (string) from the webpage and checks if it is present
    # Run this method before interacting with any elements
    def waitForBrowser(self, elements):
        for i in range(len(elements)):
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, elements[i]))
            )

            # Check if the element is clickable (for the signup buttons)
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, elements[i]))
            )


createEmail = CreateEmail()
createEmail.runBrowser()
