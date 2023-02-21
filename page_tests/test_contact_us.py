import pytest
from page_tests.base_test import TestBase
from urls import ui_constants as uic
import allure
from decorators.decorators import default_logging
from enums.page_elements import NavBarElements


@allure.epic("Contact Us")
@allure.story("Contact Us functionality test")
@allure.severity(allure.severity_level.MINOR)
class TestContactUs(TestBase):

    @pytest.fixture
    def info(self) -> dict:
        info = {
            "name": "testername",
            'email': 'testermail@gmail.com',
            'subject': 'about shoes',
            'message': 'Hi, please contact me about Black Shoes!'
        }
        return info

    @pytest.fixture
    def expected_message(self) -> str:
        return "Thanks for contacting us! We will be in touch with you shortly."

    @default_logging
    @allure.description("Send a message using the Contact Us Form")
    @allure.title("Test the contact Us form")
    def test_contact(self, driver, info, contact_page, nav_bar, expected_message):
        driver.get(uic.HOME_PAGE)
        nav_bar.navigate(NavBarElements.CONTACT_US)
        assert driver.current_url == uic.CONTACT_US
        submission_text = contact_page.contact(
            name=info['name'],
            email=info['email'],
            subject=info['subject'],
            message=info['message'])
        expected = expected_message
        assert submission_text == expected, f"expected {expected_message} got {submission_text}"
