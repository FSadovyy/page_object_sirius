from .pages.register_page import RegisterPage
import pytest
import time

@pytest.mark.negative
@pytest.mark.eng
def test_try_register_with_wrong_forms_en(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.switch_language_in_switcher()
    page.add_items_in_obligatory_forms(
        "",
        "",
        "",
        "23.12.АБББ",
        "ru.y@",
        "vv00.000.000",
        "",
        "Садовый",
        "",
        "",
        "",
        "",
        "",
        ""
    )

    time.sleep(3)
    page.check_data_has_no_numbers("FORM_BIRTH_DATE")
    page.check_text("Wrong email",
                    "ERROR_EMAIL")
    page.check_text("SNILS have to contains digits only",
                    "ERROR_SNILS")
    page.check_text("Vosh-login incorrect. Try again",
                    "ERROR_LOGIN")
    page.check_element_is_active("BUTTON_TO_TESTING", "NO")