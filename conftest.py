import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="Chrome",
                     help="Choose browser: Chrome or Firefox")
    parser.addoption('--headless', action='store', default="false",
                     help="Choose headless mode: True of False")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")

    if browser_name == "Chrome":
        if headless == "True":
            options = Options()
            options.headless = True
            print("\nstart Chrome browser with headless for test..")
            browser = webdriver.Chrome(options=options)
        elif headless == "False":
            print("\nstart Chrome browser without headless for test..")
            browser = webdriver.Chrome()
        else:
            raise pytest.UsageError("--headless mode should be True of False")

    elif browser_name == "Firefox":
        if headless == "True":
            options = FirefoxOptions()
            options.add_argument("--headless")
            print("\nstart Firefox browser with headless for test..")
            browser = webdriver.Firefox(options=options)
        elif headless == "False":
            print("\nstart Firefox browser without headless for test..")
            browser = webdriver.Firefox()
        else:
            raise pytest.UsageError("--headless mode should be True of False")
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
