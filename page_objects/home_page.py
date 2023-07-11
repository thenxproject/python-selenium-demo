from page_objects.base_pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__()
        self.browser = browser
        self.at_checker = (By.CSS_SELECTOR, "[title='Search']")
        self.url = "https://google.com"
        self.search_textbox = (By.CSS_SELECTOR, "[title='Search']")
        self.search_button = (By.CSS_SELECTOR, ".FPdoLc [aria-label='Google Search']")
        self.signin_button = (By.CLASS_NAME, "gb_Nd")

    def set_search_textbox(self, text: str):
        self.browser.set_text(self.search_textbox, text)

    def get_search_textbox(self) -> str:
        return self.browser.get_attribute(self.search_textbox, "value")

    def get_signin_button_text(self) -> str:
        return self.browser.get_text(self.signin_button)

    def click_search_button(self):
        self.browser.click_element(self.search_button)

    def get_search_button_text(self) -> str:
        return self.browser.get_attribute(self.search_button, "value")



