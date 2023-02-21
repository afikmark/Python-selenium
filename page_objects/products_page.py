from enums.page_elements import ProductsPageElements
from enums.locators import Locators
from .base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class ProductsPage(BasePage):
    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver)

    @property
    def products_page(self):
        return {
            'add to cart': self.find_element(by=Locators.CSS, selector='[type=submit][name=add-to-cart]'),
            'product name': self.find_element(by=Locators.CSS, selector='.entry-summary >h1')

        }

    @property
    def products_page_post_purchase(self):
        return {
            'message': self.find_element(by=Locators.CSS, selector='.woocommerce-notices-wrapper .woocommerce-message')
        }

    def get_element(self, element: str, post_purchase=False) -> list[WebElement] | WebElement:
        if post_purchase:
            return self.products_page_post_purchase[f"{element}"]
        return self.products_page[f"{element}"]

    def get_product_name(self) -> str:
        return self.get_element(ProductsPageElements.PRODUCT_NAME.value).text

    def add_to_cart(self):
        self.click(self.get_element(ProductsPageElements.ADD_TO_CART.value))

    def get_post_purchase_message(self) -> str:
        return self.get_element(ProductsPageElements.MESSAGE.value, post_purchase=True).text
