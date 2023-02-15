from functools import cached_property
from page_objects.base_page import BasePage
from utils.forms import ContactUs
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass(frozen=True)
class ContactUsElements:
    name: str = '#wpforms-15-field_0'
    email: str = '#wpforms-15-field_4'
    subject: str = '#wpforms-15-field_5'
    message: str = '#wpforms-15-field_2'
    continue_btn: str = '#wpforms-submit-15[type=submit]'
    submission_message: str = '[data-id="063df41"].elementor-element >div p'


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @cached_property
    def contact_us_form(self):
        return {
            'name': self.find_element(by='css', selector=ContactUsElements.name),
            'email': self.find_element(by='css', selector=ContactUsElements.email),
            'subject': self.find_element(by='css', selector=ContactUsElements.subject),
            'message': self.find_element(by='css', selector=ContactUsElements.message),
            'continue_btn': self.find_element(by='css', selector=ContactUsElements.continue_btn),
        }

    @cached_property
    def contact_us_after_submission(self):
        return {
            'contact_submission_paragraph': self.find_element(by='css', selector=ContactUsElements.submission_message)
        }

    def get_element(self, element: str) -> WebElement | list[WebElement]:
        if element in self.contact_us_form:
            return self.contact_us_form[element]
        elif element in self.contact_us_after_submission:
            return self.contact_us_after_submission[element]

    def click_continue(self):
        continue_btn = self.get_element('continue_btn')
        self.click(continue_btn)

    def contact(self, **user_info):
        contact_form = ContactUs(
            name=user_info['name'],
            email=user_info['email'],
            subject=user_info['subject'],
            message=user_info['message'])
        contact_form.fill_form(name=self.get_element('name'),
                               email=self.get_element('email'),
                               subject=self.get_element('subject'),
                               message=self.get_element('message'))

        self.click_continue()
        return self.get_element('contact_submission_paragraph').text
