from .pages.register_page import RegisterPage
from .pages.success_page import SuccessPage
import time
import pytest

@pytest.mark.positive
@pytest.mark.eng
def test_can_register_to_main_testing(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    email = "work.tolarius@yandex.ru"
    page = RegisterPage(browser, link)
    page.open()
    page.switch_language_in_switcher()
    page.paste_last_name("Садовый")
    page.paste_first_name("Фёдор")
    page.paste_patronymic("Витальевич")
    page.paste_birth_date("12/11/2018")
    page.paste_email(email)
    page.paste_vosh_login("v00.000.000")
    page.paste_phone("88005553535")
    page.paste_snils("17246215558")
    page.paste_profession("Тестировщик")
    page.choose_country("RU")
    page.paste_city("Москва")
    page.paste_organisation("ГБОУ ЦО")
    page.paste_school("218")
    page.paste_grade("11")
    page.choose_main_testing()
    page.confirm_input_data()
    page.accept_user_agreement()
    page.know_the_rules()
    time.sleep(5)
    page.go_to_testing()
    page = SuccessPage(browser, browser.current_url)
    page.confirm_title("Автостесты. Основная олимпиада")
    page.confirm_message(email)