from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import SuccessPageLocators

class SuccessPage(BasePage):
    def confirm_title(self, test_title):
        element = SuccessPageLocators.TITLE
        assert self.is_element_present(*element), \
            "Title is not found"
        element = self.browser.find_element(*element)
        title = element.text
        assert title == test_title, "Wrong title"

    def confirm_message(self, email):
        element = SuccessPageLocators.MESSAGE
        assert self.is_element_present(*element), \
            "Success message is not found"
        message = self.browser.find_element(*element).text
        assert message.split(" ")[-1]==f"{email}", \
            "Wrong email in message"