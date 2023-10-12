from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from .locators import RegisterPageLocators
import time

class RegisterPage (BasePage):
    def paste_last_name(self, text):
        element = RegisterPageLocators.LAST_NAME_FORM
        assert self.is_element_present(*element), "Last name form is not found"
        element = self.browser.find_element(*element)
        element.send_keys(text)

    def check_last_name_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.LAST_NAME_FORM)
        assert element.get_attribute("value") == "", \
            'Last name form must be empty'

    def paste_first_name(self, text):
        element=RegisterPageLocators.FIRST_NAME_FORM
        assert self.is_element_present(*element), "First name form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_first_name_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_FORM)
        assert element.get_attribute("value") == "", \
            'First name form must be empty'

    def paste_patronymic(self, text):
        element=RegisterPageLocators.PATRONYMIC_FORM
        assert self.is_element_present(*element), "Patronymic form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_patronymic_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.PATRONYMIC_FORM)
        assert element.get_attribute("value") == "", \
            'Patronymic form must be empty'

    def paste_birth_date(self, text):
        element=RegisterPageLocators.BIRTH_DATE_FORM
        assert self.is_element_present(*element), "Birth date form is not found"
        self.browser.find_element(*element).send_keys(text)
        time.sleep(3)

    def check_date_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.BIRTH_DATE_FORM)
        assert element.get_attribute("value") == "", \
            'Burth date form must be empty'

    def check_date_has_no_numbers(self):
        element = self.browser.find_element(*RegisterPageLocators.BIRTH_DATE_FORM)
        element.click()
        result = element.get_attribute("value")
        for index in range(len(result)):
            if index not in (2, 5, 10):
                assert result[index] in "0123456789", 'Burth date must contain only numbers'

    def paste_email(self, text):
        element=RegisterPageLocators.EMAIL_FORM
        assert self.is_element_present(*element), "First name form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_email_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.EMAIL_FORM)
        assert element.get_attribute("value") == "", \
            'Email form must be empty'

    def paste_vosh_login(self, text):
        element=RegisterPageLocators.VOSH_LOGIN_FORM
        assert self.is_element_present(*element), "First name form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_vosh_login_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.VOSH_LOGIN_FORM)
        assert element.get_attribute("value") == "", \
            'Vosh login form must be empty'

    def paste_phone(self, text):
        element=RegisterPageLocators.PHONE_FORM
        assert self.is_element_present(*element), "First name form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_phone_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.PHONE_FORM)
        assert element.get_attribute("value") == "", \
            'Phone form must be empty'

    def paste_snils (self, text):
        element=RegisterPageLocators.SNILS_FORM
        assert self.is_element_present(*element), "First name form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_snils_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.SNILS_FORM)
        assert element.get_attribute("value") == "", \
            'SNILS form must be empty'

    def paste_profession (self, text):
        element=RegisterPageLocators.PROFESSION_FORM
        assert self.is_element_present(*element), "First name form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_profession_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.PROFESSION_FORM)
        assert element.get_attribute("value") == "", \
            'Profession form must be empty'

    def choose_country (self, value):
        element=RegisterPageLocators.COUNTRY_LIST
        assert self.is_element_present(*element), "First name form is not found"
        select = Select(self.browser.find_element(*element))
        select.select_by_value(value)

    def check_country_is_not_selected(self):
        element = self.browser.find_element(*RegisterPageLocators.COUNTRY_LIST)
        assert element.get_attribute("value") == "", \
            'Country must not be selected'

    def paste_city (self, text):
        element=RegisterPageLocators.CITY_FORM
        assert self.is_element_present(*element), "First name form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_city_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.CITY_FORM)
        assert element.get_attribute("value") == "", \
            'City form must be empty'

    def paste_organisation (self, text):
        element=RegisterPageLocators.ORGANISATION_FORM
        assert self.is_element_present(*element), "Organisation form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_organisation_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.ORGANISATION_FORM)
        assert element.get_attribute("value") == "", \
            'Organisation form must be empty'

    def paste_school (self, text):
        element=RegisterPageLocators.SCHOOL_FORM
        assert self.is_element_present(*element), "School form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_school_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.SCHOOL_FORM)
        assert element.get_attribute("value") == "", \
            'School form must be empty'

    def paste_grade (self, text):
        element = RegisterPageLocators.GRADE_FORM
        assert self.is_element_present(*element), "Grade form is not found"
        self.browser.find_element(*element).send_keys(text)

    def check_grade_is_empty(self):
        element = self.browser.find_element(*RegisterPageLocators.GRADE_FORM)
        assert element.get_attribute("value") == "", \
            'Grade form must be empty'

    def choose_main_testing(self):
        element = RegisterPageLocators.MAIN_RADIOBUTTON
        assert self.is_element_present(*element), "Main test radiobutton is not found"
        self.browser.find_element(*element).click()

    def is_maintest_button_choosen(self, choose="YES"):
        element = self.browser.find_element(*RegisterPageLocators.MAIN_RADIOBUTTON)
        if choose=="YES":
            assert "true" in element.get_attribute("class"), \
                'Main testing radiobutton must be choosen'
        if choose=="NO":
            assert "false" in element.get_attribute("class"), \
                'Main testing radiobutton must not be choosen'

    def choose_extra_testing(self):
        element = RegisterPageLocators.EXTRA_RADIOBUTTON
        assert self.is_element_present(*element), "Extra test radiobutton is not found"
        self.browser.find_element(*element).click()

    def is_extratest_button_choosen(self, choose="YES"):
        element = self.browser.find_element(*RegisterPageLocators.EXTRA_RADIOBUTTON)
        time.sleep(2)
        if choose=="YES":
            assert "true" in element.get_attribute("class"), \
                'Extra testing radiobutton must be choosen'
        if choose=="NO":
            assert "false" in element.get_attribute("class"), \
                'Extra testing radiobutton must not be choosen'

    def confirm_input_data(self):
        element = RegisterPageLocators.CONFIRM_DATA_CHECKBOX
        assert self.is_element_present(*element), 'Checkbox "Confirm input data" is not found'
        self.browser.find_element(*element).click()

    def is_input_data_choosen(self, choose="YES"):
        element = self.browser.find_element(*RegisterPageLocators.CONFIRM_DATA_CHECKBOX)
        unset = "ui-schema-auth-form__checkbox-unset"
        if choose=="YES":
            assert unset not in element.get_attribute("class"), \
                'Checkbox "Confirm input data" must be choosen'
        if choose=="NO":
            assert unset in element.get_attribute("class"), \
                'Checkbox "Confirm input data" must not be choosen'

    def accept_user_agreement(self):
        element = RegisterPageLocators.ACCEPT_AGREEMENT_CHECKBOX
        assert self.is_element_present(*element), 'Checkbox "Accept user agreement and consent personal data processing" is not found'
        self.browser.find_element(*element).click()

    def is_user_agreement_choosen(self, choose="YES"):
        element = self.browser.find_element(*RegisterPageLocators.ACCEPT_AGREEMENT_CHECKBOX)
        unset = "ui-schema-auth-form__checkbox-unset"
        if choose=="YES":
            assert unset not in element.get_attribute("class"), \
                'Checkbox "Accept user agreement and consent personal data processing" must be choosen'
        if choose=="NO":
            assert unset in element.get_attribute("class"), \
                'Checkbox "Accept user agreement and consent personal data processing" must not be choosen'

    def know_the_rules(self):
        element = RegisterPageLocators.FAMILIARIZED_RULES_CHECKBOX
        assert self.is_element_present(*element), 'Checkbox "Familiarized with the rules" is not found'
        self.browser.find_element(*element).click()

    def is_know_the_rules_choosen(self, choose="YES"):
        element = self.browser.find_element(*RegisterPageLocators.FAMILIARIZED_RULES_CHECKBOX)
        unset = "ui-schema-auth-form__checkbox-unset"
        if choose=="YES":
            assert unset not in element.get_attribute("class"), \
                'Checkbox "Familiarized with the rules" must be choosen'
        if choose=="NO":
            assert unset in element.get_attribute("class"), \
                'Checkbox "Familiarized with the rules" must not be choosen'

    def check_reg_button_is_active(self, choose="YES"):
        element = RegisterPageLocators.TO_TESTING_BUTTON
        assert self.is_element_present(*element), \
            'Button "To testing" is not found'
        element = self.browser.find_element(*element)
        if choose == "YES":
            assert element.is_enabled(), \
                'Button "To testing" is not enabled'
        if choose == "NO":
            assert element.is_enabled() is False, \
                'Button "To testing" must be disabled'

    def go_to_testing(self):
        element = RegisterPageLocators.TO_TESTING_BUTTON
        self.check_reg_button_is_active()
        self.browser.find_element(*element).click()
        time.sleep(3)

    def check_wrong_email_message(self):
        element = RegisterPageLocators.EMAIL_ERROR
        assert self.is_element_present(*element), \
            'Message "Неверный email" is not found'

    def check_wrong_login_message(self):
        element = RegisterPageLocators.LOGIN_ERROR
        assert self.is_element_present(*element), \
            'Message "Неверный ВОШ-логин. Попробуйте ещё раз" is not found'

    def check_snils_only_with_numbers_message(self):
        element = RegisterPageLocators.SNILS_NUMB_ERROR
        assert self.is_element_present(*element), \
            'Message "СНИЛС должен содержать только цифры" is not found'



    #def go_to_login_page(self):
        #login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link.click()
       # try:
           # alert = self.browser.switch_to.alert
           # alert.accept()
       # except: pass