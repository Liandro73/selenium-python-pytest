import allure
import pytest

from src.pages.login_page import LoginPage as loginPage
from src.pages.products_page import ProductsPage as productsPage
from src.tests.conftest import driver, browser

@allure.suite("Login")
@allure.title("Login successfully")
@allure.description("This is a test about logging in Swag Labs - Successfully")
def test_login_successfully(driver, config, browser):
    allure.dynamic.tag("Login", browser)
    loginPage.verify_if_is_login_page(driver, config)
    loginPage.fill_username_field(driver, "standard_user")
    loginPage.fill_password_field(driver, "secret_sauce")
    loginPage.click_on_login_button(driver)
    productsPage.verify_if_is_products_page(driver)

@allure.suite("Login")
@allure.title("Login with empty username")
@allure.description("This is a test about logging in Swag Labs - Empty username")
def test_login_empty_username(driver, config, browser):
    allure.dynamic.tag("Login", browser)
    loginPage.verify_if_is_login_page(driver, config)
    loginPage.fill_username_field(driver, "")
    loginPage.fill_password_field(driver, "secret_sauce")
    loginPage.click_on_login_button(driver)
    loginPage.verify_if_error_message_is_showed__empty_username(driver)

@allure.suite("Login")
@allure.title("Login with empty password")
@allure.description("This is a test about logging in Swag Labs - Empty password")
def test_login_empty_password(driver, config, browser):
    allure.dynamic.tag("Login", browser)
    loginPage.verify_if_is_login_page(driver, config)
    loginPage.fill_username_field(driver, "standard_user")
    loginPage.fill_password_field(driver, "")
    loginPage.click_on_login_button(driver)
    loginPage.verify_if_error_message_is_showed__empty_password(driver)

@allure.suite("Login")
@allure.title("Login with user locked out")
@allure.description("This is a test about logging in Swag Labs - User locked out")
def test_login_user_locked_out(driver, config, browser):
    allure.dynamic.tag("Login", browser)
    loginPage.verify_if_is_login_page(driver, config)
    loginPage.fill_username_field(driver, "locked_out_user")
    loginPage.fill_password_field(driver, "secret_sauce")
    loginPage.click_on_login_button(driver)
    loginPage.verify_if_error_message_is_showed__user_locked_out(driver)

@allure.suite("Login")
@allure.title("Login with user invalid")
@allure.description("This is a test about logging in Swag Labs - User invalid")
def test_login_user_invalid(driver, config, browser):
    allure.dynamic.tag("Login", browser)
    loginPage.verify_if_is_login_page(driver, config)
    loginPage.fill_username_field(driver, "standard_user123")
    loginPage.fill_password_field(driver, "secret_sauce")
    loginPage.click_on_login_button(driver)
    loginPage.verify_if_error_message_is_showed__user_or_password_invalids(driver)

@allure.suite("Login")
@allure.title("Login with password invalid")
@allure.description("This is a test about logging in Swag Labs - Password invalid")
def test_login_password_invalid(driver, config, browser):
    allure.dynamic.tag("Login", browser)
    loginPage.verify_if_is_login_page(driver, config)
    loginPage.fill_username_field(driver, "standard_user123")
    loginPage.fill_password_field(driver, "secret_sauce123")
    loginPage.click_on_login_button(driver)
    loginPage.verify_if_error_message_is_showed__user_or_password_invalids(driver)