import os

import allure
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
from page_objects.checkout_page import CheckOutPage
from .conftest import run_env, create_driver
from utils.files import write
from selenium.webdriver.remote.webdriver import WebDriver
from decorators.decorators import default_logging
from utils.logger import logger


class TestBase:

    @pytest.fixture(scope="session")
    def run_env(self):
        return run_env

    @pytest.fixture(scope="session")
    @default_logging
    def driver(self) -> WebDriver:
        """
        Creates Webdriver according to webdriver type
        returns the driver as a fixture for all tests to use
        """
        try:
            driver = create_driver()
            if driver.name == 'firefox':
                driver.maximize_window()
            return driver
        except (AttributeError, TimeoutException) as e:
            logger.exception(e)

    @pytest.fixture(autouse=True)
    def screenshot_on_failure(self, request, driver):
        """
        Check if test result is 'failed'
        capture screenshot and attach it to the test report in allure.
        """

        def finalizer():
            try:
                if request.node.rep_call.failed:
                    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=allure.attachment_type.PNG, body="Screenshot of the failed test")

                request.addfinalizer(finalizer)
            except AttributeError as e:
                logger.exception(e)

    @pytest.fixture(autouse=True)
    @default_logging
    def setup_teardown(self, driver: WebDriver):
        assert True
        logger.info("test started")
        yield
        logger.info("testing ended quitting driver")
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
    def checkout_page(self, driver: WebDriver) -> CheckOutPage:
        """
        :returns: Checkout Page
        """
        return CheckOutPage(driver)

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
        try:
            return {
                'name': driver.name.capitalize(),
                'version': driver.capabilities['browserVersion'],
                'platform': driver.capabilities['platformName'].capitalize()
            }
        except AttributeError as e:
            logger.exception(e)

    @pytest.fixture(autouse=True)
    @default_logging
    def write_test_details(self, test_details: dict, result_path: str, relative_result_path: str, run_env) -> None:
        """
        Get current driver information and writes it to environment properties file in the allure-results path
        """
        try:
            info = f'\nBrowser={test_details["name"]}\nVersion={test_details["version"]}\nPlatform={test_details["platform"]}'
            if run_env == "docker":
                test_result_path = relative_result_path
            else:
                test_result_path = result_path
            write(fr'{test_result_path}\environment.properties', info)
            logger.info(f"writing current driver details")

        except (FileNotFoundError, AttributeError) as e:
            logger.exception(e)
