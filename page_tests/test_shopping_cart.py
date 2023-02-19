import allure
from enums.sort import SortProducts
from .base_test import TestBase
from urls import ui_constants as uic


@allure.epic("Shopping cart")
@allure.story("Shopping cart feature functionality tests")
@allure.severity(allure.severity_level.CRITICAL)
class TestShoppingCart(TestBase):

    @allure.title("Shopping cart test")
    @allure.description("Test adding items to the shopping cart")
    @allure.step("Navigate to Home page, Navigate to Men category,"
                 "Sort price from high to low,"
                 "Add the first four products to the shopping cart"
                 "Compare items added to products in the shopping cart")
    def test_add_to_cart(self, driver, nav_bar, store_page, products_page, base_page, shopping_cart):
        """
        1. Navigate to Home page
        2. Navigate to Men category
        3. Sort price from high to low
        4. Add the first four items to the shopping cart
        """
        base_page.go(uic.HOME_PAGE)
        nav_bar.navigate('Men')
        store_page.sort_products(SortProducts.HIGH)
        products = []
        for i in range(0, 4):
            # click on product
            store_page.click_product(index=i)
            # add to cart
            products_page.add_to_cart()
            products.append(products_page.get_product_name())
            # go back to products list
            base_page.back()

        nav_bar.navigate('shopping cart')
        shopping_cart_products = list(shopping_cart.get_product_names())
        compare_list = [product for product in shopping_cart_products if product in products]
        assert compare_list, f"expected {products} got {shopping_cart_products}"
