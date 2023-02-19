from dataclasses import dataclass

from enums.locators import Locators
from .base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from enum import Enum


@dataclass(frozen=True)
class StorePageElements:
    products_links: str = '.products.columns-4 li .astra-shop-summary-wrap a'
    order_by: str = 'select[name=orderby]'


class StorePage(BasePage):
    def __init__(self, driver):
        super(StorePage, self).__init__(driver)

    @property
    def store(self) -> dict:
        return {
            'product links': self.find_elements(by=Locators.CSS, selector=StorePageElements.products_links),
            'order by': self.find_element(by=Locators.CSS, selector=StorePageElements.order_by)
        }

    def get_element(self, element: str) -> list[WebElement] | WebElement:
        return self.store[f"{element.lower()}"]

    def click_product(self, product_name: str):
        """
        Receives product name in the shop
        Clicks on it.
        """
        products = self.get_element('product links')
        try:
            for product in products:
                if product.text == product_name:
                    self.click(product)
                    break
        except ValueError as e:
            print(e)

    def click_product(self, index: int):
        """
        Receives product index
        Click on the product link
        according to location in the products container
        """
        products = self.get_element('product links')
        try:
            self.click(products[index])
        except IndexError as e:
            print("Wrong index number, item not found", e)

    def sort_products(self, sort_by: Enum):
        order_by_selector = self.get_element('order by')
        self.select(order_by_selector, sort_by.value)
