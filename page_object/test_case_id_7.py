from .pages.register_page import RegisterPage
import pytest
import time

@pytest.mark.negative
@pytest.mark.ru
def test_try_register_with_wrong_forms_ru(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
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
    page.check_text("Неверный email",
                    "ERROR_EMAIL")
    page.check_text("СНИЛС должен содержать только цифры",
                    "ERROR_SNILS")
    page.check_text("Неверный ВОШ-логин. Попробуйте ещё раз",
                    "ERROR_LOGIN")
    page.check_element_is_active("BUTTON_TO_TESTING", "NO")