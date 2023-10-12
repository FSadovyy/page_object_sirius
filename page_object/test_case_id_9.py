from .pages.register_page import RegisterPage
from .pages.test_items import TestItems
import pytest

@pytest.mark.negative
@pytest.mark.ru
def test_can_register_to_main_testing(browser):
    link = 'https://uts.sirius.online//#/auth/register/qainternship'
    email = TestItems.TESTMAIL
    page = RegisterPage(browser, link)
    page.open()
    page.paste_last_name("Садовый")
    page.paste_first_name("Фёдор")
    page.paste_patronymic("Витальевич")
    page.paste_birth_date("12/11/2018")
    page.paste_email(email)
    page.paste_vosh_login("v00.000.000")
    page.paste_phone("88005553535")
    page.paste_snils(TestItems.TESTSNILS)
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
    page.refresh()
    page.check_last_name_is_empty()
    page.check_first_name_is_empty()
    page.check_patronymic_is_empty()
    page.check_date_is_empty()
    page.check_email_is_empty()
    page.check_vosh_login_is_empty()
    page.check_phone_is_empty()
    page.check_snils_is_empty()
    page.check_profession_is_empty()
    page.check_country_is_not_selected()
    page.check_city_is_empty()
    page.check_organisation_is_empty()
    page.check_school_is_empty()
    page.check_grade_is_empty()
    page.is_maintest_button_choosen()
    page.is_extratest_button_choosen("NO")
    page.is_input_data_choosen("NO")
    page.is_user_agreement_choosen("NO")
    page.is_know_the_rules_choosen("NO")