import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from enum import Enum
from enums.locators import Locators
from utils.logger import logger
from .base_page import BasePage
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass(frozen=True)
class NavBarElements:
    home: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Home")]'
    store: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Store")]'
    men: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Men")]'
    women: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Women")]'
    accessories: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Accessories")]'
    about: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"About")]'
    contact_us: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Contact Us")]'
    shopping_cart: str = '.ast-header-woo-cart #ast-site-header-cart'
    shopping_cart_total: str = '.ast-header-woo-cart .ast-woo-header-cart-info-wrap .woocommerce-Price-amount.amount'


class NavBar(BasePage):
    def __init__(self, driver):
        super(NavBar, self).__init__(driver)

    @property
    def navbar(self) -> dict:
        return {
            'home': self.find_element(by=Locators.XPATH, selector=NavBarElements.home),
            'store': self.find_element(by=Locators.XPATH, selector=NavBarElements.store),
            'men': self.find_element(by=Locators.XPATH, selector=NavBarElements.men),
            'women': self.find_element(by=Locators.XPATH, selector=NavBarElements.women),
            'accessories': self.find_element(by=Locators.XPATH, selector=NavBarElements.accessories),
            'about': self.find_element(by=Locators.XPATH, selector=NavBarElements.about),
            'contact us': self.find_element(by=Locators.XPATH, selector=NavBarElements.contact_us),
            'shopping cart': self.find_element(by=Locators.CSS, selector=NavBarElements.shopping_cart),
            'cart total': self.find_element(by=Locators.CSS, selector=NavBarElements.shopping_cart_total)
        }

    def get_element(self, category: Enum | str) -> WebElement:
        return self.navbar[f"{category.lower()}"]

    @allure.step("Navigate to category: {0}")
    def navigate(self, category: Enum):
        if not category:
            pytest.exit("please use a valid selector")
        try:
            self.click(self.get_element(category.value))
        except (KeyError, NoSuchElementException, AttributeError) as e:
            logger.exception(e)

    def get_cart_total(self) -> str:
        """
        Returns shopping cart current total amount
        """
        return self.get_element('cart total').text
