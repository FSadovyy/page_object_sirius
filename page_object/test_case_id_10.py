from .pages.register_page import RegisterPage
import pytest

@pytest.mark.negative
@pytest.mark.eng
def test_clean_forms_when_rerfresh_page_en(browser, valid_email):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    page = RegisterPage(browser, link)
    page.open()
    page.switch_language_in_switcher()
    page.add_items_in_obligatory_forms(
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
    page.refresh()
    page.confirm_all_forms_are_empty()
    page.is_radiobutton_choosen("RADIOBUTTON_MAIN_TEST")
    page.is_radiobutton_choosen("RADIOBUTTON_EXTRA_TEST", "NO")
    page.all_checkbox_confirmed("NO")