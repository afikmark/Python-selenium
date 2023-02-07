from selenium.common import NoSuchElementException
from functools import cached_property
from page_objects.base_page import BasePage


class ResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @cached_property
    def elements(self):
        return {
            'result_links': self.find_elements(by='css', selector='article .entry-title a')
        }

    def get_results(self) -> iter:
        """
        goes over the result page title elements
        returns an iterator object that holds
         the text of each title
        """
        try:
            results_container = self.elements['result_links']
            for result in results_container:
                yield result.text
        except NoSuchElementException:
            print("No such element")

