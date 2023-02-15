from selenium.common import NoSuchElementException, TimeoutException
from functools import cached_property

from page_objects.base_page import BasePage
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass(frozen=True)
class HomePageElements:
    search_btn: str = '.ast-header-search[data-section]'
    search_bar: str = '.search-field[type=search]'


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @cached_property
    def elements(self) -> dict:
        return {
            'search_button': self.find_element(by='css', selector=HomePageElements.search_btn),
            'search_bar': self.find_element(by='css', selector=HomePageElements.search_bar),
        }

    def get_element(self, element: str) -> WebElement:
        return self.elements[element]

    def search(self, search_params: str):
        """
        :param search_params: str
        searches by given input
        """
        try:
            self.click(self.get_element('search_button'))
            self.fill_text(self.get_element('search_bar'), search_params)
            self.action('enter')
            self.explicit_wait_title_contains("Results")
        except (NoSuchElementException, TimeoutException) as e:
            print(e)

    def nav_contact_us(self):
        self.click(self.elements['contact_us_button'])
