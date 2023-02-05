from typing import Type
from multipledispatch import dispatch
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: webdriver):
        """
        This init method is used to create an instance of the BasePage class.
        It takes in a webdriver instance as a parameter and sets the self._driver and self._wait instance variables.
        The self._wait instance variable is initialized to a WebDriverWait object with the driver and a timeout of 10 seconds.
        """
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def get_driver(self):
        return self._driver

    def close_driver(self):
        self._driver.close()

    def click(self, web_element: WebElement):
        """
        clicks on element if element is clickable
        if the clickable opens a new tab it is added to
        window handles dictionary with tab title as key and the handle object
        as value
        """
        element = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        element.click()

    def fill_text(self, web_element: WebElement, txt: str):
        """
        Receives input type web element and text value
        Wait until the element is visible
        clears the input
        send text input
        """
        web_element.clear()
        web_element.send_keys(txt)

    def find_element(self, by, selector):
        """
        Receives css selector
        returns web element object
        """
        element = None
        if by == 'css':
            element = self._driver.find_element(by=By.CSS_SELECTOR, value=selector)
        elif by == 'xpath':
            element = self._driver.find_element(by=By.XPATH, value=selector)
        elif by == "link_text":
            element = self._driver.find_element(by=By.LINK_TEXT, value=selector)
        return element

    def find_elements(self, by, selector):
        """
        Receives css selector for a list/container
        returns a list of web elements
        """

        elements = None
        if by == 'css':
            elements = self._driver.find_elements(by=By.CSS_SELECTOR, value=selector)
        elif by == 'xpath':
            elements = self._driver.find_elements(by=By.XPATH, value=selector)
        return elements

    def explicit_wait_clickable(self, selector: str):
        """
        Receives css selector for an element
        wait until the element is clickable
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def explicit_wait_visibility(self, web_element: WebElement):
        """
        Receives web element
        wait until the element is visible
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.visibility_of(web_element))

    @staticmethod
    def select_by_index(web_element: WebElement, index: int):
        """
        Receives a web element of selector type and index number
        select an item in the selector element using the index given
        """
        selector = Select(web_element)
        selector.select_by_index(index)

    def action(self, key_type: str):
        """Performs an action on the keyboard"""
        action = ActionChains(self._driver)
        if key_type == 'enter':
            action.send_keys(Keys.ENTER).perform()

    def current_address(self):
        return self._driver.current_url
