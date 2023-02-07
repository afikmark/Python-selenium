import pytest
from page_tests.base_test import TestBase
from ui_test_urls import ui_constants as uic

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

    def test_contact(self, driver, info, contact_page, nav_bar):
        driver.get(uic.HOME_PAGE_URL)
        nav_bar.navigate('Contact Us')
        submission_text = contact_page.contact(
            name=info['name'],
            email=info['email'],
            subject=info['subject'],
            message=info['message'])
        expected = "Thanks for contacting us! We will be in touch with you shortly."
        assert submission_text == expected
