from .pages.register_page import RegisterPage
import pytest
import time

@pytest.mark.negative
@pytest.mark.ru
def test_can_register_to_main_testing(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.paste_birth_date("23.12.АБББ")
    page.paste_email("ru.y@")
    page.paste_vosh_login("vv00.000.000")
    page.paste_snils("Садовый")
    time.sleep(3)
    page.check_date_has_no_numbers()
    page.check_wrong_email_message()
    page.check_wrong_login_message()
    page.check_snils_only_with_numbers_message()
    page.check_reg_button_is_active("NO")