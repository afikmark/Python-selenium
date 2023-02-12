from selenium.common import NoSuchElementException
from functools import cached_property
from page_objects.base_page import BasePage
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass(frozen=True)
class ResultPageElements:
    result_links: str = 'article .entry-title a'


class ResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @cached_property
    def elements(self):
        return {
            'result_links': self.find_elements(by='css', selector=ResultPageElements.result_links)
        }

    def get_element(self, element: str) -> list[WebElement]:
        return self.elements[element]

    def get_results(self) -> iter:
        """
        goes over the result page title elements
        returns an iterator object that holds
         the text of each title
        """
        try:
            results_container = self.get_element('result_links')
            for result in results_container:
                yield result.text
        except NoSuchElementException:
            print("No such element")
