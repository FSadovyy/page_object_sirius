from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import SuccessPageLocators

class SuccessPage(BasePage):
    MESSAGE = '.smt-auth-registration-panel__success-message'
    TITLE = '.text-xxl'

    def confirm_email(self, email, attribute):
        element = self.check_element(attribute).text.split(" ")[-1]
        assert element == f"{email}", \
            f"Wrong email in message: {element}"