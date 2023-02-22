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
    CHECKOUT_BUTTON: str = 'checkout button'
    ORDER_TOTAL_AMOUNT: str = 'order total amount'
    SHIPPING_METHODS_RADIO_BTN: str = 'shipping methods radio_btn'
    SHIPPING_METHODS_RADIO_TEXT: str = 'shipping methods radio_text'


class StorePageElements(Enum):
    PRODUCT_LINKS: str = 'product links'
    ORDER_BY: str = 'order by'


class CheckOutElements(Enum):
    BILLING_INPUT_FIELDS: str = 'billing input fields'
    BILLING_SELECT_COUNTRY: str = 'billing select country'
    SHIP_TO_DIFFERENT_ADDRESS_CHECKBOX: str = 'ship to different address checkbox'
    ORDER_COMMENTS: str = 'order comments'
    PLACE_ORDER: str = 'place order'
    ERROR: str = 'error'
