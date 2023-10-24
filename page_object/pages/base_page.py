from selenium.common.exceptions import NoSuchElementException as no_element
from selenium.webdriver.common.by import By
from .locators import PageLocators

class BasePage:
    LANG_SWITCHER = '.lang_switcher'
    ENG = '.lang_switcher__flag-en'
    RU = '.lang_switcher__flag-ru'

    def __init__(self, browser, url, timeout=5):
        self.url = url
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def check_text(self, text, attribute):
        element = self.check_element(attribute)
        message = element.text
        assert message == text, \
            f'{attribute} contain wrong text: {message}'


    def check_element (self, locator):
        locator = getattr(self, locator)
        try: self.browser.find_element(By.CSS_SELECTOR, locator)
        except no_element:
            f"Element '{locator}' is not found"
        return self.browser.find_element(By.CSS_SELECTOR, locator)


    def open (self):
        self.browser.get(self.url)


    def refresh (self):
        self.browser.refresh()


    def switch_language_in_switcher(self, what_language="ENG"):
        element = self.check_element("LANG_SWITCHER")
        element.click()
        language = self.check_element(what_language)
        language.click()


