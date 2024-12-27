import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.helper.pages_helper import PageObjectHelper

class LoginPage(PageObjectHelper):

    # Locators
    logo_login_page_locator = By.CLASS_NAME, "login_logo"
    input_user_locator = By.ID, "user-name"
    input_password_locator = By.ID, "password"
    btn_login_locator = By.ID, "login-button"

    # Error handling
    error_empty_user_locator = By.XPATH, "//h3[text()='Epic sadface: Username is required']"
    error_empty_password_locator = By.XPATH, "//h3[text()='Epic sadface: Password is required']"
    error_user_locked_out_locator = By.XPATH, "//h3[text()='Epic sadface: Sorry, this user has been locked out.']"
    error_invalid_user_and_password_locator = By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']"

    @classmethod
    @allure.step("Verify if is Login Page")
    def verify_if_is_login_page(self, driver):
        driver.get("https://www.saucedemo.com/")
        logo_login_page: WebElement = driver.find_element(*self.logo_login_page_locator)
        self.wait_until_element_is_visible(driver, logo_login_page)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="login-page",
            attachment_type=allure.attachment_type.PNG
        )

    @classmethod
    @allure.step("Fill username field")
    def fill_username_field(self, driver, user:str):
        input_user: WebElement = driver.find_element(*self.input_user_locator)
        self.clear_and_type_in_element(driver, input_user, user)

    @classmethod
    @allure.step("Fill password field")
    def fill_password_field(self, driver, password:str):
        input_password: WebElement = driver.find_element(*self.input_password_locator)
        self.clear_and_type_in_element(driver, input_password, password)

    @classmethod
    @allure.step("Click on Login button")
    def click_on_login_button(self, driver):
        btn_login: WebElement = driver.find_element(*self.btn_login_locator)
        self.click_on_element(driver, btn_login)

    @classmethod
    @allure.step("Verify if error message is showed: Username is required")
    def verify_if_error_message_is_showed__empty_username(self, driver):
        error_empty_user: WebElement = driver.find_element(*self.error_empty_user_locator)
        self.wait_until_element_is_visible(driver, error_empty_user)
        self.get_text_from_element_and_compare(driver, error_empty_user, 'Epic sadface: Username is required')

        allure.attach(
            driver.get_screenshot_as_png(),
            name="error-username-is-required",
            attachment_type=allure.attachment_type.PNG
        )

    @classmethod
    @allure.step("Verify if error message is showed: Password is required")
    def verify_if_error_message_is_showed__empty_password(self, driver):
        error_empty_password: WebElement = driver.find_element(*self.error_empty_password_locator)
        self.wait_until_element_is_visible(driver, error_empty_password)
        self.get_text_from_element_and_compare(driver, error_empty_password, 'Epic sadface: Password is required')

        allure.attach(
            driver.get_screenshot_as_png(),
            name="error-password-is-required",
            attachment_type=allure.attachment_type.PNG
        )

    @classmethod
    @allure.step("Verify if error message is showed: Sorry, this user has been locked out.")
    def verify_if_error_message_is_showed__user_locked_out(self, driver):
        error_user_locked_out: WebElement = driver.find_element(*self.error_user_locked_out_locator)
        self.wait_until_element_is_visible(driver, error_user_locked_out)
        self.get_text_from_element_and_compare(driver, error_user_locked_out, 'Epic sadface: Sorry, this user has been locked out.')

        allure.attach(
            driver.get_screenshot_as_png(),
            name="error-user-locked-out",
            attachment_type=allure.attachment_type.PNG
        )

    @classmethod
    @allure.step("Verify if error message is showed: Username and password do not match any user in this service")
    def verify_if_error_message_is_showed__user_or_password_invalids(self, driver):
        error_invalid_user_and_password: WebElement = driver.find_element(*self.error_invalid_user_and_password_locator)
        self.wait_until_element_is_visible(driver, error_invalid_user_and_password)
        self.get_text_from_element_and_compare(driver, error_invalid_user_and_password, 'Epic sadface: Username and password do not match any user in this service')

        allure.attach(
            driver.get_screenshot_as_png(),
            name="error-username-or-password-invalids",
            attachment_type=allure.attachment_type.PNG
        )