from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class PageObjectHelper:

    def __init__(self, driver):
        self.driver = driver

    time: int = 10
    wait: WebDriverWait

    @classmethod
    def wait_until_element_is_visible(self, driver, element):
        self.wait = WebDriverWait(driver, timeout=self.time)
        self.wait.until(ec.visibility_of(element))

    @classmethod
    def clear_and_type_in_element(self, driver, element, text):
        self.wait_until_element_is_visible(driver, element)
        element.clear()
        element.send_keys(text)

    @classmethod
    def click_on_element(self, driver, element):
        self.wait_until_element_is_visible(driver, element)
        element.click()

    @classmethod
    def get_text_from_element_and_compare(self, driver, element, text):
        self.wait_until_element_is_visible(driver, element)
        text_element = element.text
        assert(text_element == element.text)
        print("")
        print("-----------------------------------------")
        print("Text obtained: " + text_element.upper())
        print("Text expected: " + text.upper())
        print("-----------------------------------------")