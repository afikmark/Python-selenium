import allure
import pytest

from enums.sort import SortProducts
from .base_test import TestBase
from urls import ui_constants as uic
from decorators.decorators import default_logging
from enums.page_elements import NavBarElements


@allure.epic("Shopping cart")
@allure.story("Shopping cart feature functionality tests")
@allure.severity(allure.severity_level.CRITICAL)
class TestShoppingCart(TestBase):

    @default_logging
    @allure.title("Shopping cart test")
    @allure.description("Test adding items to the shopping cart")
    def test_add_to_cart(self, driver, nav_bar, store_page, products_page, base_page, shopping_cart, checkout_page):
        """
        1. Navigate to Home page
        2. Navigate to Men category
        3. Sort price from high to low
        4. Add the first four items to the shopping cart
        """
        with allure.step(f"Navigate to Home page: {uic.HOME_PAGE}"):
            base_page.go(uic.HOME_PAGE)
        with allure.step(f"Navigate to {NavBarElements.MEN.value} category "):
            nav_bar.navigate(NavBarElements.MEN)
        with allure.step(f"Sort price from high to low"):
            store_page.sort_products(SortProducts.HIGH.value)
        products = []
        with allure.step("Add the first four products to the shopping cart"):
            for i in range(0, 4):
                # click on product
                store_page.click_product(index=i)
                # add to cart
                products_page.add_to_cart()
                products.append(products_page.get_product_name())
                # go back to products list
                base_page.navigate_back()
        with allure.step("Compare items added to products in the shopping cart"):
            nav_bar.navigate(NavBarElements.SHOPPING_CART)
            shopping_cart_products = list(shopping_cart.get_product_names())
            compare_list = [product for product in shopping_cart_products if product in products]
            assert compare_list, f"expected {products} got {shopping_cart_products}"

    @pytest.fixture
    def billing_form_inputs(self) ->dict:
        return {'First name': 'afik', 'Last name': 'mark', 'Company': 'Afikim', 'Country': 'Israel', 'Street address': 'Herzel', 'Apartment': 'apartment',
                'City': 'rehovot', 'State': 'israel state', 'Post code': '11110', 'Phone': '055959576', 'Email address': 'a@gmail.com', 'Order notes': 'order notes'}

    def test_buy_product(self, nav_bar, store_page, base_page, products_page, shopping_cart, checkout_page, billing_form_inputs):
        with allure.step("Pre-requisites steps: add a product to the shopping cart"):
            with allure.step(f"Navigate to Home page: {uic.HOME_PAGE}"):
                base_page.go(uic.HOME_PAGE)
            with allure.step(f"Navigate to {NavBarElements.STORE.value} category "):
                nav_bar.navigate(NavBarElements.STORE)
            with allure.step("Add the first product"):
                store_page.click_product(index=0)
                products_page.add_to_cart()
            with allure.step(f"Navigate to {NavBarElements.SHOPPING_CART.value}"):
                nav_bar.navigate(NavBarElements.SHOPPING_CART)
            with allure.step("Choose shipping method"):
                shopping_cart.select_shipping_method(1)
            with allure.step("Click on Checkout"):
                shopping_cart.click_checkout()
        with allure.step("Test the check out page"):
            with allure.step("Fill billing form"):
                checkout_page.fill_billing_form(billing_form_inputs)
            with allure.step("Click on 'Place Order' button"):
                checkout_page.place_order()
            with allure.step("assert error message"):
                expected = 'Invalid payment method.'
                assert expected == checkout_page.get_errors(), f"expected {expected} got {checkout_page.get_errors()[0]} "
