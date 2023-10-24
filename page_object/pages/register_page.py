from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
import time

class RegisterPage (BasePage):
    BUTTON_TO_TESTING = '.smt-register-form__register-btn'
    CHECKBOX_ACCEPT_AGREEMENT = '.test-locator-sf-users-agreement-and-personal-data .ui-checkbox__input'
    CHECKBOX_CONFIRM_VERACITY = '.test-locator-sf-confirmation-of-veracity .ui-checkbox__input'
    CHECKBOX_FAMILIARIZED_RULES = '.test-locator-sf-familiarized-with-the-rules .ui-checkbox__input'
    ERROR_EMAIL = '.test-locator-sf-email  .ui-schema-auth-form__error'
    ERROR_LOGIN = '.test-locator-sf-vosh-login-optional  .ui-schema-auth-form__error'
    ERROR_SNILS = '.test-locator-sf-snils-opt .ui-schema-auth-form__error'
    FORM_BIRTH_DATE = '.test-locator-sf-birth-date .ui-date-time__input'
    FORM_CITY = '.test-locator-sf-school-city .ui-textinput__input'
    FORM_EMAIL = '.test-locator-sf-email .ui-textinput__input'
    FORM_FIRST_NAME = '.test-locator-sf-firstName .ui-textinput__input'
    FORM_GRADE = '.test-locator-sf-school-grade .ui-textinput__input'
    FORM_LAST_NAME = '.test-locator-sf-lastName .ui-textinput__input'
    FORM_ORGANISATION = '.test-locator-sf-school-organization .ui-textinput__input'
    FORM_PATRONYMIC = '.test-locator-sf-patronymic .ui-textinput__input'
    FORM_PHONE = '.test-locator-sf-phone .ui-textinput__input'
    FORM_PROFESSION = '.test-locator-sf-profession .ui-textinput__input'
    FORM_SCHOOL = '.test-locator-sf-school-school .ui-textinput__input'
    FORM_SNILS = '.test-locator-sf-snils-opt .ui-textinput__input'
    FORM_VOSH_LOGIN = '.test-locator-sf-vosh-login-optional .ui-textinput__input'
    FORM_COUNTRY = ".test-locator-sf-school-country .ui-schema-auth-form__country-select"
    LIST_DATEKEEPER = '.react-datepicker__month-container'
    RADIOBUTTON_EXTRA_TEST = '[role="radiogroup"]:nth-child(2) .ui-schema-auth-form__enum-input-radio'
    RADIOBUTTON_MAIN_TEST = '[role="radiogroup"]:nth-child(1) .ui-schema-auth-form__enum-input-radio'

    def add_valid_items_in_obligatory_forms(self, *args):
       obligatory_forms = [

        'FORM_LAST_NAME',
        'FORM_FIRST_NAME',
        'FORM_PATRONYMIC',
        'FORM_BIRTH_DATE',
        'FORM_EMAIL',
        'FORM_VOSH_LOGIN',
        'FORM_PHONE',
        'FORM_SNILS',
        'FORM_PROFESSION',
        'FORM_COUNTRY',
        'FORM_CITY',
        'FORM_ORGANISATION',
        'FORM_SCHOOL',
        'FORM_GRADE'

       ]

       for index in range(len (args)):
           self.paste_data_in_form(args[index],
                                   obligatory_forms[index]
                                   )


    def paste_data_in_form (self, text, locator):
        element = self.check_element (locator)
        if locator == "FORM_COUNTRY":
            select = Select(element)
            select.select_by_value(text)
        else:
            element.send_keys(text)
            if locator == "FORM_BIRTH_DATE":
                time.sleep(2)


    def confirm_all_checkboxes (self):
        boxes =  [
            'CHECKBOX_CONFIRM_VERACITY',
            'CHECKBOX_ACCEPT_AGREEMENT',
            'CHECKBOX_FAMILIARIZED_RULES'
                  ]

        for index in range(3):
            self.confirm_checkbox(boxes[index])



    def check_data_has_no_numbers(self, form):
        element = self.check_element(form)
        element.click()
        result = element.get_attribute("value")
        for index in range(len(result)):
            if (form == "Birth date form") and (index in (2, 5, 10)):
                continue
            else:
                assert result[index] in "0123456789", f'{form} must contain only numbers'


    def check_element_is_active (self, element, choose="YES"):
        if choose == "YES":
            assert element.is_enabled(), \
                f'{element} is not enabled'
        if choose == "NO":
            assert element.is_enabled() is False, \
                f'{element} must be disabled'


    def check_form_is_empty (self, form):
        element = self.check_element(form)
        assert element.get_attribute("value") == "", \
            f'{form} must be empty'


    def choose_radiobutton(self, button):
        element = self.check_element(button)
        element.click()


    def confirm_checkbox(self, checkbox_name):
        element = self.check_element(checkbox_name)
        element.click()


    def is_checkbox_confirmed (self, checkbox_name, choose="YES"):
        element = self.check_element(checkbox_name)
        unset = "ui-schema-auth-form__checkbox-unset"
        if choose=="YES":
            assert unset not in element.get_attribute("class"), \
                f'{checkbox_name} must be choosen'
        if choose=="NO":
            assert unset in element.get_attribute("class"), \
                f'{checkbox_name} must not be choosen'


    def is_radiobutton_choosen(self, button, choose="YES"):
        element = self.check_element(button)
        if button=="Extra testing":
            time.sleep(2)
        if choose=="YES":
            assert "true" in element.get_attribute("class"), \
                f'{button} must be choosen'
        if choose=="NO":
            assert "false" in element.get_attribute("class"), \
                f'{button} must not be choosen'


    def press_button(self, button):
        element = self.check_element(button)
        time.sleep(3)
        self.check_element_is_active(element)
        element.click()






