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

    def get_results(self) -> list[str]:
        """returns a list of the results on the page"""
        results = []
        try:
            results_container = self.elements['result_links']
            for result in results_container:
                results.append(result.text)
            return results
        except NoSuchElementException:
            print("No such element")
            self.quit_driver()
