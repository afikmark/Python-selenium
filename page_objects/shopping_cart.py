from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
from enums.locators import Locators
from enums.page_elements import ShoppingCartElements
import time


class ShoppingCart(BasePage):
    def __init__(self, driver):
        super(ShoppingCart, self).__init__(driver)

    @property
    def shopping_cart(self) -> dict:
        return {
            'product names': self.find_elements(by=Locators.CSS, selector='.product-name a'),
            'checkout button': self.find_element(by=Locators.CSS, selector='a.checkout-button'),
            'order total amount': self.find_element(by=Locators.CSS, selector='.order-total .woocommerce-Price-amount bdi'),
            'shipping methods radio_btn': self.find_elements(by=Locators.CSS, selector='[data-title="Shipping"] ul#shipping_method [type=radio]'),
            'shipping methods radio_text': self.find_elements(by=Locators.CSS, selector='[data-title="Shipping"] ul#shipping_method label')
        }

    def get_element(self, element: str) -> list[WebElement] | WebElement:
        return self.shopping_cart[f"{element}"]

    def get_product_names(self) -> list[str]:
        product_names_elements = self.get_element(ShoppingCartElements.PRODUCT_NAMES)
        for product in product_names_elements:
            yield product.text

    def select_shipping_method(self, method: int):
        radio_btns = self.get_element(ShoppingCartElements.SHIPPING_METHODS_RADIO_BTN)
        self.click(radio_btns[method])

    def click_checkout(self):
        time.sleep(1.0) # replace with Explicit wait
        self.click(self.get_element(ShoppingCartElements.CHECKOUT_BUTTON))
