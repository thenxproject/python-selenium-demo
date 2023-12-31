import selenium.webdriver.remote.webelement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

# Create the webdriver the proper driver can be downloaded from https://github.com/mozilla/geckodriver/releases
# Put the downloaded driver in the webdrivers folder and make sure the file name is correct
driver = webdriver.Firefox()

# opens the browser and goes to google
driver.get("https://www.google.com/")

wait = WebDriverWait(driver, 5)

# Finds the search box
search_box: WebElement = wait.until(visibility_of_element_located((By.CSS_SELECTOR, "[title='Search']")))

# Enters search text
search_box.send_keys("Star Trek")
search_box.send_keys(Keys.TAB)

assert search_box.get_attribute("value") == "Star Trek"

signin_button: WebElement = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".gb_Nd")))
assert signin_button.text == "Sign in"

search_button: WebElement = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".FPdoLc [aria-label='Google Search']")))
assert search_button.get_attribute("value") == "Google Search"
search_button.click()

driver.quit()
