import os

import pytest
from selenium.common import TimeoutException
from page_objects.base_page import BasePage
from page_objects.contact_page import ContactUsPage
from page_objects.home_page import HomePage
from page_objects.nav_bar import NavBar
from page_objects.results_page import ResultsPage
from page_objects.shopping_cart import ShoppingCart
from page_objects.store_page import StorePage
from page_objects.products_page import ProductsPage
from .conftest import Drivers, create_driver
from utils.files import write
from selenium.webdriver.remote.webdriver import WebDriver


class TestBase:

    @pytest.fixture(scope="session")
    def driver(self) -> WebDriver:
        """
        Creates Webdriver according to webdriver type
        returns the driver as a fixture for all tests to use
        """
        try:
            driver = create_driver(Drivers.CHROME)
            if driver.name == Drivers.FIREFOX.value.lower():
                driver.maximize_window()
            return driver
        except TimeoutException:
            print("The request has timed out")

    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver: WebDriver):
        assert True
        yield
        driver.quit()

    @pytest.fixture
    def base_page(self, driver: WebDriver) -> BasePage:
        """
        :returns: base page
        """
        return BasePage(driver)

    @pytest.fixture
    def home_page(self, driver: WebDriver) -> HomePage:
        """
        :returns home page object
        """
        return HomePage(driver)

    @pytest.fixture
    def results_page(self, driver: WebDriver) -> ResultsPage:
        """
        :returns home page object
        """
        return ResultsPage(driver)

    @pytest.fixture
    def contact_page(self, driver: WebDriver) -> ContactUsPage:
        """
        returns contact us page
        """
        return ContactUsPage(driver)

    @pytest.fixture
    def nav_bar(self, driver: WebDriver) -> NavBar:
        """
        :returns NavBar Page
        """
        return NavBar(driver)

    @pytest.fixture
    def store_page(self, driver: WebDriver) -> StorePage:
        """
        :returns: Store Page
        """
        return StorePage(driver)

    @pytest.fixture
    def products_page(self, driver: WebDriver) -> ProductsPage:
        """
        :returns: Products Page
        """
        return ProductsPage(driver)

    @pytest.fixture
    def shopping_cart(self, driver: WebDriver) -> ShoppingCart:
        """
        :returns: Shopping cart Page
        """
        return ShoppingCart(driver)

    @pytest.fixture
    def result_path(self) -> str:
        return os.getcwd() + r'\allure-results'

    @pytest.fixture
    def relative_result_path(self) -> str:
        return os.path.abspath("..//") + r'\allure-results'

    @pytest.fixture(autouse=True)
    def test_details(self, driver: WebDriver) -> dict:
        """
        retrieve current driver information
        """
        return {
            'name': driver.name.capitalize(),
            'version': driver.capabilities['browserVersion'],
            'platform': driver.capabilities['platformName'].capitalize()
        }

    @pytest.fixture(autouse=True)
    def write_test_details(self, test_details: dict, result_path: str, relative_result_path: str) -> None:
        """
        Get current driver information and writes it to environment properties file in the allure-results path
        """
        try:
            info = f'Browser={test_details["name"]}\nVersion={test_details["version"]}\nPlatform={test_details["platform"]}'

            if not result_path:
                write(f'{relative_result_path}/environment.properties', info)

            else:
                write(f'{result_path}/environment.properties', info)
        except (FileNotFoundError, AttributeError) as e:
            print(e)
