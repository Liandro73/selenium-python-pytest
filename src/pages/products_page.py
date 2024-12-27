import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.helper.pages_helper import PageObjectHelper

class ProductsPage(PageObjectHelper):

    # Locators
    text_products_page_locator = By.XPATH, "//span[text()='Products']"

    @classmethod
    @allure.step("Verify if is Login Page")
    def verify_if_is_products_page(self, driver):
        text_products_page: WebElement = driver.find_element(*self.text_products_page_locator)
        self.wait_until_element_is_visible(driver, text_products_page)
        self.get_text_from_element_and_compare(driver, text_products_page, 'Products')

        allure.attach(
            driver.get_screenshot_as_png(),
            name="login-page",
            attachment_type=allure.attachment_type.PNG
        )