import pytest

from page_tests.base_test import TestBase
from page_objects.contact_page import ContactUsPage


class TestRegistration(TestBase):

    @pytest.fixture
    def info(self):
        info = {
            "name": "testername",
            'email': 'testermail@gmail.com',
            'subject': 'about shoes',
            'message': 'Hi, please contact me about Black Shoes!'
        }
        return info

    @pytest.fixture
    def contact_page(self, driver) -> ContactUsPage:
        """
        :returns regitration page
        """
        return ContactUsPage(driver)

    def test_contact(self, driver, info, contact_page, home_page_obj):
        home_page_obj.nav_contact_us()
        submission_text = contact_page.contact(
            name=info['name'],
            email=info['email'],
            subject=info['subject'],
            message=info['message'])
        expected = "Thanks for contacting us! We will be in touch with you shortly."
        assert submission_text == expected
