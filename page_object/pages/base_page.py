from selenium.common.exceptions import NoSuchElementException as no_element
from .locators import PageLocators

class BasePage:
    LANGUAGES = {
        "RU": PageLocators.RUSSIAN,
        "ENG": PageLocators.ENGLISH
    }

    def __init__(self, browser, url, timeout=5):
        self.url = url
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try: self.browser.find_element(how, what)
        except no_element:
            return False
        return True

    def refresh(self):
        self.browser.refresh()

    def assert_language(self, what_language):
        language = self.LANGUAGES[what_language]
        assert self.is_element_present(*language), \
            "Target language is not found"

    def switch_language_in_switcher(self, what_language="ENG"):
        assert self.is_element_present(*PageLocators.LANG_SWITCHER), \
            "Switcher is not presented"
        self.browser.find_element(*PageLocators.LANG_SWITCHER).click()
        self.assert_language(what_language)
        self.browser.find_element(*self.LANGUAGES[what_language]).click()


