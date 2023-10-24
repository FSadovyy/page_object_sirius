import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose one: '--browser_name=chrome', '--browser_name=firefox'")

    parser.addoption('--valid_email',
                     action='store',
                     default=None,
                     help="Paste valid email for testing (optional). For example: '--valid_email=mycompany@yandex.ru'")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = OptionsChrome()
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = OptionsFirefox()
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def valid_email(request):
    return request.config.getoption("valid_email")




