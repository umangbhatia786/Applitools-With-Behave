from selenium.webdriver.common.by import By
from features.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from features.pages.test_base import TestBase
from selenium.webdriver.common.keys import Keys

test_base = TestBase()

delay_min = 3  # sec
delay_medium = 5  # sec
delay_max = 9  # sec


class PageBase(Browser):

    def prepareDynamicXpath(self, xpathValue, substitutionValue):
        return xpathValue.replace("xxxxxx", substitutionValue)

    def enter_text(self, text, locator):
        self.driver.find_element(*locator).send_keys(text)

    def enter_text_advanced(self, text, locator1, locator2):
        self.driver.find_element(*locator1).find_element(*locator2).send_keys(text)

    def clear_text_advanced(self, text, locator1, locator2):
        self.driver.find_element(*locator1).find_element(*locator2).clear()

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def click_element_advanced(self, locator1, locator2):
        self.driver.find_element(*locator1).find_element(*locator2).click()

    def return_element_list(self, locator):
        return self.driver.find_elements(*locator)

    def return_element(self, locator):
        return self.driver.find_element(*locator)

    def navigate_url(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def wait_for_page_title(self, pagetitle):
        WebDriverWait(self.driver, delay_max).until(expected_conditions.title_contains(pagetitle))

    def wait_for_element_present(self, *locator):
        WebDriverWait(self.driver, delay_max).until(expected_conditions.visibility_of_element_located(*locator))

    def wait_for_text_present(self, *locator, eletxt):
        WebDriverWait(self.driver, delay_medium).until(
            expected_conditions.text_to_be_present_in_element(*locator, eletxt))

    def browser_click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def browser_navigate_url(self, address):
        self.driver.get(address)
