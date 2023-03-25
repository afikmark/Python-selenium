from enums.locators import Locators
from .base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from enum import Enum
from enums.page_elements import StorePageElements
from .dropdown.dropdown import DropDown


class StorePage(BasePage):
    def __init__(self, driver):
        super(StorePage, self).__init__(driver)

    @property
    def store(self) -> dict:
        return {
            'product links': self.find_elements(by=Locators.CSS, selector='.products.columns-4 li .astra-shop-summary-wrap a'),
            'order by': self.find_element(by=Locators.CSS, selector='select[name=orderby]')
        }

    def get_element(self, element: str) -> list[WebElement] | WebElement:
        return self.store[f"{element}"]

    def click_product_by_name(self, product_name: str):
        """
        Receives product name in the shop
        Clicks on it.
        """
        products = self.get_element(StorePageElements.PRODUCT_LINKS.value)
        try:
            for product in products:
                if product.text == product_name:
                    self.click(product)
                    break
        except ValueError as e:
            print(e)

    def click_product_by_index(self, index: int):
        """
        Receives product index
        Click on the product link
        according to location in the products container
        """
        products = self.get_element(StorePageElements.PRODUCT_LINKS.value)
        try:
            self.click(products[index])
        except IndexError as e:
            print("Wrong index number, item not found", e)

    def sort_products(self, sort_by):
        order_by_selector = self.get_element(StorePageElements.ORDER_BY.value)
        order_by_drop_down = DropDown(order_by_selector)
        order_by_drop_down.select_text(sort_by.value)
