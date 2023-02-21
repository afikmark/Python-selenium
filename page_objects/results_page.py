from selenium.common import NoSuchElementException
from utils.logger import logger
from enums.locators import Locators
from page_objects.base_page import BasePage

from selenium.webdriver.remote.webelement import WebElement
from enums.page_elements import ResultPageElements


class ResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def elements(self) -> dict:
        return {
            'result_links': self.find_elements(by=Locators.CSS, selector='article .entry-title a')
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
            results_container = self.get_element(ResultPageElements.RESULT_LINKS.value)
            for result in results_container:
                yield result.text
        except NoSuchElementException as e:
            logger.exception(e)
