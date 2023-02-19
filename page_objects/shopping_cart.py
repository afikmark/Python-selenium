from dataclasses import dataclass

from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from enums.locators import Locators


@dataclass(frozen=True)
class ShoppingCartElements:
    product_names: str = '.product-name a'


class ShoppingCart(BasePage):
    def __init__(self, driver):
        super(ShoppingCart, self).__init__(driver)

    @property
    def shopping_cart(self):
        return {
            'product names': self.find_elements(by=Locators.CSS, selector=ShoppingCartElements.product_names)
        }

    def get_element(self, element: str) -> list[WebElement] | WebElement:
        return self.shopping_cart[f"{element.lower()}"]

    def get_product_names(self) -> list[str]:
        product_names_elements = self.get_element('product names')
        for product in product_names_elements:
            yield product.text
