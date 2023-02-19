from dataclasses import dataclass

from enums.locators import Locators
from .base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


@dataclass(frozen=True)
class ProductsPageElements:
    add_to_cart: str = '[type=submit][name=add-to-cart]'
    message: str = '.woocommerce-notices-wrapper .woocommerce-message'
    product_name: str = '.entry-summary >h1'


class ProductsPage(BasePage):
    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver)

    @property
    def products_page(self):
        return {
            'add to cart': self.find_element(by=Locators.CSS, selector=ProductsPageElements.add_to_cart),
            'product name': self.find_element(by=Locators.CSS, selector=ProductsPageElements.product_name)

        }

    @property
    def products_page_post_purchase(self):
        return {
            'message': self.find_element(by=Locators.CSS, selector=ProductsPageElements.message)
        }

    def get_element(self, element: str, post_purchase=False) -> list[WebElement] | WebElement:
        if post_purchase:
            return self.products_page_post_purchase[f"{element.lower()}"]
        return self.products_page[f"{element.lower()}"]

    def get_product_name(self) -> str:
        return self.get_element('product name').text

    def add_to_cart(self):
        self.click(self.get_element('add to cart'))

    def get_post_purchase_message(self) -> str:
        return self.get_element('message').text
