from enum import Enum


class HomePageElements(Enum):
    SEARCH_BUTTON: str = 'search_button'
    SEARCH_BAR: str = 'search_bar'


class ContactUsElements(Enum):
    NAME: str = 'name'
    EMAIL: str = 'email'
    SUBJECT: str = 'subject'
    MESSAGE: str = 'message'
    CONTINUE_BTN: str = 'continue_btn'
    SUBMISSION_MESSAGE: str = 'submission_message'
    CONTACT_SUBMISSION_PARAGRAPH: str = 'contact_submission_paragraph'


class NavBarElements(Enum):
    HOME: str = 'home'
    STORE: str = 'store'
    MEN: str = 'men'
    WOMEN: str = 'women'
    ACCESSORIES: str = 'accessories'
    ABOUT: str = 'about'
    CONTACT_US: str = 'contact us'
    SHOPPING_CART: str = 'shopping cart'
    CART_TOTAL: str = 'cart total'


class ProductsPageElements(Enum):
    ADD_TO_CART: str = 'add to cart'
    MESSAGE: str = 'message'
    PRODUCT_NAME: str = 'product name'


class ResultPageElements(Enum):
    RESULT_LINKS: str = 'result_links'


class ShoppingCartElements:
    PRODUCT_NAMES: str = 'product names'


class StorePageElements(Enum):
    PRODUCT_LINKS: str = 'product links'
    ORDER_BY: str = 'order by'
