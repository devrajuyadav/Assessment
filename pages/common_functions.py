from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class CommonFunctions:

    def __init__(self, driver):
        self.driver = driver

    def tap_function(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()
        except TimeoutException as ex:
            print(" Element not found " + str(ex))

    def get_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException as ex:
            print(" Element not found " + str(ex))

    def enabled(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.is_enabled()
        except TimeoutException as ex:
            print(" Element not found " + str(ex))
