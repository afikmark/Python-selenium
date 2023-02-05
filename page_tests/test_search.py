import pytest

from .base_test import TestBase
from page_objects.home_page import HomePage
from page_objects.results_page import ResultsPage

class TestRegistration(TestBase):

    @pytest.fixture
    def home_page(self, driver) -> HomePage:
        """
        :returns home page object
        """
        return HomePage(driver)

    @pytest.fixture
    def results_page(self, driver) -> ResultsPage:
        """
        :returns home page object
        """
        return ResultsPage(driver)

    @pytest.fixture
    def shoes(self):
        return ['ATID Black Shoes', 'ATID Yellow Shoes', 'ATID Red Shoes', 'ATID Blue Shoes', 'ATID Green Shoes']

    def test_search_atid(self, driver, home_page, results_page, shoes):
        """
        1.Navigate to atid store
        2.search for shoes
        3.compare results to expected results
        """
        search_input = 'Shoes'
        home_page.search(search_input)
        actual_set = set(results_page.get_results())
        is_eq = [x for x in shoes if x in actual_set]
        assert is_eq
