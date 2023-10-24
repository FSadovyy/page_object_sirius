from .pages.register_page import RegisterPage
from .pages.success_page import SuccessPage
import pytest

@pytest.mark.positive
@pytest.mark.eng
def test_can_register_to_main_testing_eng(browser, valid_email):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.switch_language_in_switcher()
    page.add_valid_items_in_obligatory_forms(
        "Садовый",
        "Фёдор",
        "Витальевич",
        "12/11/2018",
        valid_email,
        "v00.000.000",
        "88005553535",
        '17246215558',
        "Тестировщик",
        "RU",
        "Москва",
        "ГБОУ ЦО",
        "218",
        "11"
    )
    page.choose_radiobutton("RADIOBUTTON_MAIN_TEST")
    page.confirm_all_checkboxes()
    page.press_button("BUTTON_TO_TESTING")
    page = SuccessPage(browser, browser.current_url)
    page.check_text("Автостесты. Основная олимпиада", "TITLE")
    page.confirm_email(valid_email, "MESSAGE")