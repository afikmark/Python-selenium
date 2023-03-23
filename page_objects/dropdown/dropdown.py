from abc import ABC, abstractmethod
from decorators.decorators import default_logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement


class DropDownObj(ABC):

    @abstractmethod
    def select(self, value):
        """
        This method is responsible for selecting an item from dropdown
        """


class DropDown(DropDownObj):
    @default_logging
    def select(self, element: WebElement, index: int):
        """
        This method is responsible for selecting an item from the dropdown by index
        """
        selector = Select(element)
        selector.select_by_index(index)

    @default_logging
    def select(self, element: WebElement, value):
        """
        This method is responsible for selecting an item from the dropdown by value
        """
        selector = Select(element)
        selector.select_by_value(value)

    @default_logging
    def select(self, element: WebElement, text: str):
        """
        This method is responsible for selecting an item from the dropdown by visible text
        """
        selector = Select(element)
        selector.select_by_visible_text(text)

