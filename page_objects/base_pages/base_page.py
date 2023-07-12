from utility.browser import Browser


class BasePage:
    def __init__(self, browser: Browser):
        self.at_checker = ()
        self.url = ""
        self.browser = browser

    def at(self) -> bool:
        return self.browser.is_displayed(self.at_checker)

    def go(self):
        self.browser.open_url(self.url)
