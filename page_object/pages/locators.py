from selenium.webdriver.common.by import By

class PageLocators():
    LANG_SWITCHER = (By.CSS_SELECTOR, '.lang_switcher')
    LNG_ENGLISH =   (By.CSS_SELECTOR, '.lang_switcher__flag-en')
    LNG_RUSSIAN =   (By.CSS_SELECTOR, '.lang_switcher__flag-ru')

class RegisterPageLocators(PageLocators):
    BUTTON_TO_TESTING =           (By.CSS_SELECTOR, '.smt-register-form__register-btn')
    CHECKBOX_ACCEPT_AGREEMENT =   (By.CSS_SELECTOR, '.test-locator-sf-users-agreement-and-personal-data')
    CHECKBOX_CONFIRM_VERACITY =   (By.CSS_SELECTOR, '.test-locator-sf-confirmation-of-veracity')
    CHECKBOX_FAMILIARIZED_RULES = (By.CSS_SELECTOR, '.test-locator-sf-familiarized-with-the-rules')
    ERROR_EMAIL =                 (By.CSS_SELECTOR, '.test-locator-sf-email  .ui-schema-auth-form__error')
    ERROR_LOGIN =                 (By.CSS_SELECTOR, '.test-locator-sf-vosh-login-optional  .ui-schema-auth-form__error')
    ERROR_SNILS =                 (By.CSS_SELECTOR, '.test-locator-sf-snils-opt .ui-schema-auth-form__error')
    FORM_BIRTH_DATE =             (By.CSS_SELECTOR, '.ui-date-time-input-reset')
    FORM_CITY =                   (By.CSS_SELECTOR, '.test-locator-sf-school-city')
    FORM_EMAIL =                  (By.CSS_SELECTOR, '.test-locator-sf-email')
    FORM_FIRST_NAME =             (By.CSS_SELECTOR, '.test-locator-sf-firstName')
    FORM_GRADE =                  (By.CSS_SELECTOR, '.test-locator-sf-school-grade')
    FORM_LAST_NAME =              (By.CSS_SELECTOR, '.test-locator-sf-lastName')
    FORM_ORGANISATION =           (By.CSS_SELECTOR, '.test-locator-sf-school-organization')
    FORM_PATRONYMIC =             (By.CSS_SELECTOR, '.test-locator-sf-patronymic')
    FORM_PHONE =                  (By.CSS_SELECTOR, '.test-locator-sf-phone')
    FORM_PROFESSION =             (By.CSS_SELECTOR, '.test-locator-sf-profession')
    FORM_SCHOOL =                 (By.CSS_SELECTOR, '.test-locator-sf-school-school')
    FORM_SNILS =                  (By.CSS_SELECTOR, '.test-locator-sf-snils-opt')
    FORM_VOSH_LOGIN =             (By.CSS_SELECTOR, '.test-locator-sf-vosh-login-optional')
    LIST_COUNTRY =                (By.CSS_SELECTOR, '.ui-schema-auth-form__country-select')
    LIST_DATEKEEPER =             (By.CSS_SELECTOR, '.react-datepicker__month-container')
    RADIOBUTTON_EXTRA_TEST =      (By.CSS_SELECTOR, '[role="radiogroup"]:nth-child(2) .ui-schema-auth-form__enum-input-radio')
    RADIOBUTTON_MAIN_TEST =       (By.CSS_SELECTOR, '[role="radiogroup"]:nth-child(1) .ui-schema-auth-form__enum-input-radio')

class SuccessPageLocators(PageLocators):
    TEXT_MESSAGE = (By.CSS_SELECTOR, '.smt-auth-registration-panel__success-message')
    TEXT_TITLE =   (By.CSS_SELECTOR, '.text-xxl')








