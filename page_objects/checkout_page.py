import time

from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
from enums.locators import Locators
from enums.page_elements import CheckOutElements
from utils.forms import BillingForm
import re


class CheckOutPage(BasePage):
    def __init__(self, driver):
        super(CheckOutPage, self).__init__(driver)

    @property
    def checkout(self) -> dict:
        return {
            'billing input fields': self.find_elements(by=Locators.CSS, selector='.woocommerce-billing-fields__field-wrapper input'),
            'billing select country': self.find_element(by=Locators.CSS, selector='.woocommerce-billing-fields__field-wrapper select'),
            'ship to different address checkbox': self.find_element(by=Locators.CSS, selector='input#ship-to-different-address-checkbox[type=checkbox]'),
            'order comments': self.find_element(by=Locators.CSS, selector='textarea#order_comments'),
            'place order': self.find_element(by=Locators.CSS, selector='button#place_order[type=submit]')

        }

    @property
    def checkout_alert(self) -> dict:
        return {
            'error': self.find_element(by=Locators.CSS, selector='.woocommerce-error[role=alert] li')
        }

    def get_element(self, element: str, error: bool = False) -> list[WebElement] | WebElement:
        if not error:
            return self.checkout[f"{element}"]
        return self.checkout_alert[f"{element}"]

    def fill_billing_form(self, *inputs: [str]):
        input_fields = self.get_element(CheckOutElements.BILLING_INPUT_FIELDS.value)
        fields = {}
        for i in range(len(input_fields)):
            name = re.findall(r'[^*\xa0$]', input_fields[i].accessible_name)
            fields[''.join(name)] = input_fields[i]

        fields['Country/Region'] = self.get_element(CheckOutElements.BILLING_SELECT_COUNTRY.value)
        fields['Order Comments'] = self.get_element(CheckOutElements.ORDER_COMMENTS.value)

        billing_form = BillingForm()
        billing_form.fill_form(*inputs, **fields)

    def place_order(self):
        self.click(self.get_element(CheckOutElements.PLACE_ORDER.value))

    def get_errors(self):
        time.sleep(1.0)  # replace with Explicit wait
        return self.get_element(CheckOutElements.ERROR.value, error=True).text
