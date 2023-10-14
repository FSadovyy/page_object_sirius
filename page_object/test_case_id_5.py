from .pages.register_page import RegisterPage
import pytest

@pytest.mark.negative
@pytest.mark.ru
def test_try_register_with_empty_forms_ru(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.check_reg_button_is_active("NO")

