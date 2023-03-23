import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import logger
from decorators.decorators import retry
from enums.locators import Locators
from enum import Enum
from .dropdown.dropdown import DropDown
from .actions.actions import KeyBoardActions, MouseActions


class BasePage:
    def __init__(self, driver: webdriver):
        """
        This init method is used to create an instance of the BasePage class.
        It takes in a webdriver instance as a parameter and sets the self._driver and self._wait instance variables.
        The self._wait instance variable is initialized to a WebDriverWait object with the driver and a timeout of 10 seconds.
        """
        self._driver = driver
        self.mouse = MouseActions(driver)
        self.keyboard = KeyBoardActions(driver)
        self._wait = WebDriverWait(self._driver, 10)

    @retry
    def go(self, url: str):
        self._driver.get(url)
        is_success = self._driver.current_url == url
        return is_success

    def get_driver(self) -> webdriver:
        return self._driver

    def quit_driver(self) -> None:
        self._driver.quit()

    def drag_and_drop(self, source: WebElement, target: WebElement) -> None:
        """
        drags an element to another target element
        """
        source = self._wait.until(expected_conditions.element_to_be_clickable(source))
        self.mouse.action(source=source, target=target)

    def double_click(self, web_element: WebElement) -> None:
        """
        double clicks an element
        """
        element = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        self.mouse.action(element=element)

    def click(self, web_element: WebElement) -> None:
        """
        clicks on element if element is clickable
        if the clickable opens a new tab it is added to
        """
        element = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        element.click()

    @staticmethod
    def fill_text(web_element: WebElement, txt: str):
        """
        Receives input type web element and text value
        Wait until the element is visible
        clears the input
        send text input
        """
        web_element.clear()
        web_element.send_keys(txt)

    def find_element(self, by: Enum, selector: str) -> WebElement:
        """
        Receives css selector and locator type
        returns web element object
        """
        if not selector:
            pytest.exit("please use a valid selector")
        try:
            match by:
                case Locators.CSS:
                    return self._driver.find_element(by=By.CSS_SELECTOR, value=selector)
                case Locators.XPATH:
                    return self._driver.find_element(by=By.XPATH, value=selector)
                case _:
                    raise ValueError("Wrong locator type!")
        except NoSuchElementException as e:
            logger.exception(e)

    def find_elements(self, by: Enum, selector: str) -> list[WebElement]:
        """
        Receives css selector for a list/container
        returns a list of web elements
        """
        if not selector:
            pytest.exit("please use a valid selector")
        try:
            match by:
                case Locators.CSS:
                    return self._driver.find_elements(by=By.CSS_SELECTOR, value=selector)
                case Locators.XPATH:
                    return self._driver.find_elements(by=By.XPATH, value=selector)
                case _:
                    raise ValueError("Wrong locator type!")
        except NoSuchElementException as e:
            logger.exception(e)

    def explicit_wait_clickable(self, selector: str) -> None:
        """
        Receives css selector for an element
        wait until the element is clickable
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def explicit_wait_visibility(self, web_element: WebElement) -> None:
        """
        Receives web element
        wait until the element is visible
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.visibility_of(web_element))

    def explicit_wait_title_contains(self, title: str) -> None:
        """
        Receives string title and waits until the title exist in the Dom
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.title_contains(title))

    @staticmethod
    def select(web_element: WebElement, value):
        drop_down = DropDown()
        if isinstance(value, int):
            drop_down.select(web_element, index=value)
        if isinstance(value, str):
            drop_down.select(web_element, text=value)
        else:
            drop_down.select(web_element, value=value)

    def key_board_action(self, key_type, key_down=False):
        """Performs an action on the keyboard"""
        if key_down:
            self.keyboard.key_down_action(key_type)
        self.keyboard.action(key_type)


    @retry
    def navigate_back(self):
        current_url = self._driver.current_url
        self._driver.back()
        new_url = self._driver.current_url
        success = False if new_url == current_url else True
        return success
