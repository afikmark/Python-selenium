from abc import ABC, abstractmethod
from decorators.decorators import default_logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement


class SelectObj(ABC):
    @abstractmethod
    def select_index(self, value):
        """
        This method is responsible for selecting an item from dropdown by index
        """


class DriverSelect(SelectObj):
    @default_logging
    def select_index(self, element: WebElement, index: int):
        """
        This method is responsible for selecting an item from the dropdown by index
        """
        selector = Select(element)
        selector.select_by_index(index)

    @default_logging
    def select_value(self, element: WebElement, value):
        """
        This method is responsible for selecting an item from the dropdown by value
        """
        selector = Select(element)
        selector.select_by_value(value)

    @default_logging
    def select_text(self, element: WebElement, text: str):
        """
        This method is responsible for selecting an item from the dropdown by visible text
        """
        selector = Select(element)
        selector.select_by_visible_text(text)

    @default_logging
    def get_options(self, element: WebElement) -> list:
        """
        Returns a list of all selected options
        """
        selector = Select(element)
        return selector.all_selected_options()
