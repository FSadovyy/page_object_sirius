from selenium.webdriver.common.by import By

class PageLocators():
    LANG_SWITCHER =   (By.CSS_SELECTOR, ".lang_switcher")
    ENGLISH = (By.XPATH, '//div[text()="Eng"]')
    RUSSIAN = (By.XPATH, '//div[text()="Рус"]')

class RegisterPageLocators(PageLocators):
    LAST_NAME_FORM =  (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[2]/label/div[2]/input')
    FIRST_NAME_FORM = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[3]/label/div[2]/input')
    PATRONYMIC_FORM = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[4]/label/div[2]/input')
    BIRTH_DATE_AREA = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]')
    BIRTH_DATE_FORM = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div[1]/div/div/input')
    DATEKEEPER =      (By.CSS_SELECTOR,".react-datepicker__month-container")
    EMAIL_FORM =      (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[6]/label/div[2]/input')
    VOSH_LOGIN_FORM = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[7]/label/div[2]/input')
    PHONE_FORM =      (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[8]/label/div[2]/input')
    SNILS_FORM =      (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[9]/label/div[2]/input')
    PROFESSION_FORM = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[10]/label/div[2]/input')
    COUNTRY_LIST =    (By.CSS_SELECTOR, ".ui-schema-auth-form__country-select")
    CITY_FORM =       (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[3]/label/div[2]/input')
    ORGANISATION_FORM = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[4]/label/div[2]/input')
    SCHOOL_FORM =       (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[5]/label/div[2]/input')
    GRADE_FORM =        (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[6]/label/div[2]/input')
    MAIN_RADIOBUTTON =  (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[1]/span[1]')
    EXTRA_RADIOBUTTON = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[2]/span[1]')
    CONFIRM_DATA_CHECKBOX =       (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[13]/div/label')
    ACCEPT_AGREEMENT_CHECKBOX =   (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/label')
    FAMILIARIZED_RULES_CHECKBOX = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[15]/div/label')
    TO_TESTING_BUTTON =           (By.CSS_SELECTOR, ".smt-register-form__register-btn")
    EMAIL_ERROR =                 (By.XPATH, '//div[text()="Неверный email"]')
    LOGIN_ERROR =                 (By.XPATH, '//div[text()="Неверный ВОШ-логин. Попробуйте ещё раз"]')
    SNILS_NUMB_ERROR =            (By.XPATH, '//div[text()="СНИЛС должен содержать только цифры"]')

class SuccessPageLocators(PageLocators):
    TITLE = (By.CSS_SELECTOR, ".text-xxl")
    MESSAGE = (By.CSS_SELECTOR, ".smt-auth-registration-panel__success-message")












    #LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    #LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    #REGISTER_FORM = (By.CSS_SELECTOR, "#login_form")
    #ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
