import allure
from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException
from utils.logger import logger
from enums.locators import Locators
from page_objects.base_page import BasePage
from enums.page_elements import HomePageElements
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def elements(self) -> dict:
        return {
            'search_button': self.find_element(by=Locators.CSS, selector='.ast-header-search[data-section]'),
            'search_bar': self.find_element(by=Locators.CSS, selector='.search-field[type=search]'),
        }

    def get_element(self, element: str) -> WebElement:
        return self.elements[element]

    @allure.step("Click on the search button fill: {1}  submit the search")
    def search(self, search_params: str):
        """
        :param search_params: str
        searches by given input
        """
        try:
            self.click(self.get_element(HomePageElements.SEARCH_BUTTON.value))
            self.fill_text(self.get_element(HomePageElements.SEARCH_BAR.value), search_params)
            self.action('enter')
            self.explicit_wait_title_contains("Results")
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            logger.exception(e)

    def nav_contact_us(self):
        self.click(self.elements['contact_us_button'])
