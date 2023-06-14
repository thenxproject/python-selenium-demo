
from utility.base_object import *

home_page.go()
assert home_page.at()
home_page.set_search_textbox("Star Trek")
assert home_page.get_search_textbox() == "Star Trek"
assert home_page.get_signin_button_text() == "Sign in"
assert home_page.get_search_button_text() == "Google Search"
home_page.click_search_button()

browser.quit()