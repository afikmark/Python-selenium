from page_objects.base_page import BasePage

from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass
class ContactUs:
    name: str
    email: str
    subject: str
    message: str

    def fill_form(self, **elements: WebElement):
        BasePage.fill_text(elements['name'], self.name)
        BasePage.fill_text(elements['email'], self.email)
        BasePage.fill_text(elements['subject'], self.subject)
        BasePage.fill_text(elements['message'], self.message)
