import allure
import pytest

from .base_test import TestBase
from urls import ui_constants as uic


@allure.epic("Search")
@allure.story("Search feature functionality test")
@allure.severity(allure.severity_level.CRITICAL)
class TestSearch(TestBase):

    @pytest.fixture
    def shoes(self) -> list[str]:
        return ['ATID Black Shoes', 'ATID Yellow Shoes', 'ATID Red Shoes', 'ATID Blue Shoes', 'ATID Green Shoes']

    @allure.description("Search for an item in the store")
    @allure.title("test search")
    @allure.step("Navigate to atid store, search for shoes, compare results to expected result")
    def test_search_atid(self, shoes, driver, home_page, results_page):
        """
        1.Navigate to atid store
        2.search for shoes
        3.compare results to expected results
        """
        driver.get(uic.HOME_PAGE)
        search_input = "Shoes"
        home_page.search(search_input)
        actual_set = set(results_page.get_results())
        is_eq = [x for x in shoes if x in actual_set]
        assert is_eq, f"expected list of shoes got {actual_set}"
