from functools import cached_property
from page_objects.base_page import BasePage
from utils.forms import ContactUsForm


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @cached_property
    def contact_us_form(self):
        return {
            'name': self.find_element(by='css', selector='#wpforms-15-field_0'),
            'email': self.find_element(by='css', selector='#wpforms-15-field_4'),
            'subject': self.find_element(by='css', selector='#wpforms-15-field_5'),
            'message': self.find_element(by='css', selector='#wpforms-15-field_2'),
            'continue_btn': self.find_element(by='css', selector='#wpforms-submit-15[type=submit]'),
        }

    @cached_property
    def contact_us_after_submission(self):
        return {
            'contact_submission_paragraph': self.find_element(by='css', selector='[data-id="063df41"].elementor-element >div p')
        }

    def click_continue(self):
        continue_btn = self.contact_us_form['continue_btn']
        self.click(continue_btn)

    def contact(self, **user_info):
        contact_form = ContactUsForm(
            self.get_driver(),
            name=user_info['name'],
            email=user_info['email'],
            subject=user_info['subject'],
            message=user_info['message'])
        contact_form.fill_form(name=self.contact_us_form['name'], email=self.contact_us_form['email'], subject=self.contact_us_form['subject'], message=self.contact_us_form['message'])

        self.click_continue()
        return self.contact_us_after_submission['contact_submission_paragraph'].text
