import allure
import pytest
from .base_test import TestBase
from urls import ui_constants as uic
from decorators.decorators import default_logging


@allure.epic("Search")
@allure.story("Search feature functionality test")
@allure.severity(allure.severity_level.CRITICAL)
class TestSearch(TestBase):
    @pytest.fixture
    def shoes(self) -> list[str]:
        return ['ATID Black Shoes', 'ATID Yellow Shoes', 'ATID Red Shoes', 'ATID Blue Shoes', 'ATID Green Shoes']

    @default_logging
    @allure.description("Search for an item in the store")
    @allure.title("Test the search function")
    def test_search_atid(self, shoes, driver, home_page, results_page):
        """
        1.Navigate to atid store
        2.search for shoes
        3.compare results to expected results
        """
        search_input = "shoes"
        with allure.step(f"Navigate to atid store{uic.HOME_PAGE}"):
            driver.get(uic.HOME_PAGE)
        with allure.step(f"Search for: {search_input}"):
            home_page.search(search_input)
        with allure.step(f"""Compare results to expected results:
                                \n{shoes}"""):
            actual_set = set(results_page.get_results())
            is_eq = [x for x in shoes if x in actual_set]
            assert is_eq, f"expected list of shoes got {actual_set}"
