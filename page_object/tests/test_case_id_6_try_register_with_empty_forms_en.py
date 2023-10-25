from pages.register_page import RegisterPage
import pytest

@pytest.mark.negative
@pytest.mark.eng
def test_try_register_with_empty_forms_en(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.switch_language_in_switcher()
    page.check_element_is_active("BUTTON_TO_TESTING", "NO")