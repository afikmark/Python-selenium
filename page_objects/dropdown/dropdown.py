from abc import ABC, abstractmethod, abstractproperty
from decorators.decorators import default_logging
from selenium.webdriver.remote.webelement import WebElement
from ..select.select import DriverSelect


class DropDownObj(ABC):
    drop_down: WebElement

    @abstractmethod
    def get_drop_down_options(self):
        """
        This method is responsible for getting all options from dropdown
        """
        pass


class DropDown(DropDownObj):
    def __init__(self, drop_down_element):
        self.drop_down = drop_down_element
        self.driver_select = DriverSelect()

    @default_logging
    def select_index(self, index: int):
        self.driver_select.select_index(element=self.drop_down, index=index)

    @default_logging
    def select_value(self, value):
        self.driver_select.select_value(element=self.drop_down, value=value)

    @default_logging
    def select_text(self, text: str):
        self.driver_select.select_text(element=self.drop_down, text=text)

    def get_drop_down_options(self) -> list:
        """
        This method is responsible for getting all options from dropdown
        """
        return self.driver_select.get_options()
