import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from page_objects.contact_page import ContactUsPage
from page_objects.home_page import HomePage
from page_objects.nav_bar import NavBar
from page_objects.results_page import ResultsPage


class TestBase:
    @pytest.fixture
    def driver(self):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            return driver
        except TimeoutException:
            print("The request has timed out")

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
    def contact_page(self, driver) -> ContactUsPage:
        """
        returns contact us page
        """
        return ContactUsPage(driver)

    @pytest.fixture
    def nav_bar(self, driver) -> NavBar:
        """
        :returns NavBar Page
        """
        return NavBar(driver)
