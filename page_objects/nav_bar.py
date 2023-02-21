import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from enums.locators import Locators
from utils.logger import logger
from .base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class NavBar(BasePage):
    def __init__(self, driver):
        super(NavBar, self).__init__(driver)

    @property
    def navbar(self) -> dict:
        return {
            'home': self.find_element(by=Locators.XPATH, selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Home")]'),
            'store': self.find_element(by=Locators.XPATH, selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Store")]'),
            'men': self.find_element(by=Locators.XPATH, selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Men")]'),
            'women': self.find_element(by=Locators.XPATH, selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Women")]'),
            'accessories': self.find_element(by=Locators.XPATH, selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Accessories")]'),
            'about': self.find_element(by=Locators.XPATH, selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"About")]'),
            'contact us': self.find_element(by=Locators.XPATH, selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Contact Us")]'),
            'shopping cart': self.find_element(by=Locators.CSS, selector='.ast-header-woo-cart #ast-site-header-cart'),
            'cart total': self.find_element(by=Locators.CSS, selector='.ast-header-woo-cart .ast-woo-header-cart-info-wrap .woocommerce-Price-amount.amount'
                                            )
        }

    def get_element(self, category: str) -> WebElement:
        return self.navbar[f"{category}"]

    @allure.step("Navigate to category: {0}")
    def navigate(self, category: str):
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
