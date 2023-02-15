import os

import pytest
from selenium.common import TimeoutException
from page_objects.contact_page import ContactUsPage
from page_objects.home_page import HomePage
from page_objects.nav_bar import NavBar
from page_objects.results_page import ResultsPage
from .conftest import Drivers, create_driver


class TestBase:

    @pytest.fixture(scope="session")
    def driver(self):
        try:
            driver = create_driver(browser_type=Drivers.EDGE)
            if driver.name == Drivers.FIREFOX.value.lower():
                driver.maximize_window()
            return driver
        except TimeoutException:
            print("The request has timed out")

    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver):
        assert True
        yield
        driver.quit()

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

    @pytest.fixture(autouse=True)
    def test_details(self, driver):
        result_path = os.getcwd() + r'\allure-results'
        relative = os.path.abspath("..//") + r'\allure-results'
        try:
            details = {
                'name': driver.name.capitalize(),
                'version': driver.capabilities['browserVersion']
            }

            if not result_path:
                with open(f'{relative}\environment.properties', 'w') as f:
                    f.write(f'Browser={details["name"]}\nVersion={details["version"]}')
            else:
                with open(f'{result_path}\environment.properties', 'w') as f:
                    f.write(f'Browser={details["name"]}\nVersion={details["version"]}')
        except (FileNotFoundError, AttributeError) as e:
            print(e)
