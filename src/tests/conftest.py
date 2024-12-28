import json

import pytest
from selenium import webdriver

@pytest.fixture
def config():
    config_file = open("src/config.json")
    return json.load(config_file)

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use in the tests"
    )

@pytest.fixture
def browser(request):
    yield request.config.getoption("--browser")

@pytest.fixture(scope='function')
def driver(request, browser, config):

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if config["headless_mode"] is True:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif browser == "safari":
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
        driver.maximize_window()
    else:
        options = webdriver.ChromeOptions()
        if config["headless_mode"] is True:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

    yield driver

    driver.quit()