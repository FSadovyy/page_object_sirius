from .pages.register_page import RegisterPage
import pytest

@pytest.mark.negative
@pytest.mark.ru
def test_can_register_to_main_testing(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.check_reg_button_is_active("NO")
