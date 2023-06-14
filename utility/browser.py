from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class Browser:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 5)

    def quit(self):
        self.driver.quit()

    def open_url(self, url: str):
        self.driver.get(url)

    def find_element(self, by) -> WebElement:
        return self.wait.until(visibility_of_element_located(by))

    def click_element(self, by):
        element = self.find_element(by)
        element.click()

    def get_text(self, by) -> str:
        element = self.find_element(by)
        return element.text

    def set_text(self, by, text: str):
        element = self.find_element(by)
        element.clear()
        element.send_keys(f"{text}{Keys.TAB}")

    def get_attribute(self, by, attribute: str) -> str:
        element = self.find_element(by)
        return element.get_attribute(attribute)

    def is_displayed(self, by) -> bool:
        element = self.find_element(by)
        return element.is_displayed()
