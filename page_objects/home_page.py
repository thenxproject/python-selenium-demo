from page_objects.base_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utility.browser import Browser


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__()
        self.browser = browser
        self.at_checker = (By.CSS_SELECTOR, "[title='Search']")
        self.url = "https://google.com"
        self.search_textbox = (By.CSS_SELECTOR, "[title='Search']")
        self.search_button = (By.CSS_SELECTOR, "[aria-label='Google Search']")
        self.signin_button = (By.CLASS_NAME, "gb_id")

    def set_search_textbox(self, text: str):
        self.browser.set_text(self.search_textbox, text)

    def click_search_button(self):
        self.browser.click(self.search_button)


