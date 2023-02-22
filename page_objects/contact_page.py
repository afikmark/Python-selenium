import allure
from page_objects.base_page import BasePage
from enums.locators import Locators
from utils.forms import ContactUsForm
from enums.page_elements import ContactUsElements
from selenium.webdriver.remote.webelement import WebElement


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def contact_us_form(self) -> dict:
        return {
            'name': self.find_element(by=Locators.CSS, selector='input#wpforms-15-field_0'),
            'email': self.find_element(by=Locators.CSS, selector='input#wpforms-15-field_4'),
            'subject': self.find_element(by=Locators.CSS, selector='input#wpforms-15-field_5'),
            'message': self.find_element(by=Locators.CSS, selector='textarea#wpforms-15-field_2'),
            'continue_btn': self.find_element(by=Locators.CSS, selector='button#wpforms-submit-15[type=submit]'),
        }

    @property
    def contact_us_after_submission(self) -> dict:
        return {
            'contact_submission_paragraph': self.find_element(by=Locators.CSS, selector='[data-id="063df41"].elementor-element >div p')
        }

    def get_element(self, element: str, after_submission: bool = False) -> WebElement | list[WebElement]:
        if not after_submission:
            return self.contact_us_form[element]
        elif after_submission:
            return self.contact_us_after_submission[element]

    def click_continue(self):
        continue_btn = self.get_element(ContactUsElements.CONTINUE_BTN.value)
        self.click(continue_btn)

    def contact(self, **user_info):
        contact_us_form = ContactUsForm()
        fields = {'name': self.get_element(ContactUsElements.NAME.value),
                  'subject': self.get_element(ContactUsElements.SUBJECT.value),
                  'email': self.get_element(ContactUsElements.EMAIL.value),
                  'message': self.get_element(ContactUsElements.MESSAGE.value)}
        contact_us_form.fill_form(fields, **user_info)
        with allure.step("Click Send Message button"):
            self.click_continue()
        return self.get_element(ContactUsElements.CONTACT_SUBMISSION_PARAGRAPH.value, after_submission=True).text
