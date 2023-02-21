from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
from enums.locators import Locators
from enums.page_elements import ShoppingCartElements


class ShoppingCart(BasePage):
    def __init__(self, driver):
        super(ShoppingCart, self).__init__(driver)

    @property
    def shopping_cart(self):
        return {
            'product names': self.find_elements(by=Locators.CSS, selector='.product-name a')
        }

    def get_element(self, element: str) -> list[WebElement] | WebElement:
        return self.shopping_cart[f"{element}"]

    def get_product_names(self) -> list[str]:
        product_names_elements = self.get_element(ShoppingCartElements.PRODUCT_NAMES)
        for product in product_names_elements:
            yield product.text
