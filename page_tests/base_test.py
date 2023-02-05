import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

from ui_test_urls import ui_constants as uic
from page_objects.home_page import HomePage
from page_objects.results_page import ResultsPage


class TestBase:
    @pytest.fixture
    def driver(self):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.get(uic.HOME_PAGE_URL)
            return driver
        except TimeoutException:
            print("The request has timed out")

    @pytest.fixture
    def home_page_obj(self, driver) -> HomePage:
        """
        :returns home page object
        """
        return HomePage(driver)

    @pytest.fixture
    def results_page_obj(self, driver) -> ResultsPage:
        """
        :returns home page object
        """
        return ResultsPage(driver)

    @pytest.fixture
    def shoes(self):
        return ['ATID Black Shoes', 'ATID Yellow Shoes', 'ATID Red Shoes', 'ATID Blue Shoes', 'ATID Green Shoes']

    def test_search_atid(self, driver, home_page_obj, results_page_obj, shoes):
        """
        1.Navigate to atid store
        2.search for shoes
        3.compare results to expected results
        """
        search_input = 'Shoes'
        home_page_obj.search(search_input)
        actual_set = set(results_page_obj.get_results())
        is_eq = [x for x in shoes if x in actual_set]
        assert is_eq
