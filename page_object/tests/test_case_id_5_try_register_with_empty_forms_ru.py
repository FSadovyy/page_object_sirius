from pages.register_page import RegisterPage
import pytest

@pytest.mark.negative
@pytest.mark.ru
def test_try_register_with_empty_forms_ru(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.check_element_is_active("BUTTON_TO_TESTING", "NO")

