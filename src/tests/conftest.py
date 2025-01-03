import pytest
from selenium import webdriver

HEADLESS_MODE = True

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use in the tests"
    )

@pytest.fixture
def browser(request):
    yield request.config.getoption("--browser")

@pytest.fixture(scope='function')
def driver(request, browser):

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if HEADLESS_MODE is True:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif browser == "safari":
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
        driver.maximize_window()
    else:
        options = webdriver.ChromeOptions()
        if HEADLESS_MODE is True:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

    yield driver

    driver.quit()