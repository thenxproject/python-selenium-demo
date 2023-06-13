import selenium.webdriver.remote.webelement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from utility.base_object import *

home_page.go()
assert home_page.at()

# Create the webdriver the proper driver can be downloaded from https://github.com/mozilla/geckodriver/releases
# Put the downloaded driver in the webdrivers folder and make sure the file name is correct
#driver = webdriver.Firefox()

# opens the browser and goes to google

browser.quit()