import os

import pytest
from page_tests.base_test import TestBase
from urls import ui_constants as uic
import allure
from decorators.decorators import default_logging
from enums.page_elements import NavBarElements
from utils.files import read_from_json
from paths.paths import execute_path


@allure.epic("Contact Us")
@allure.story("Contact Us functionality test")
@allure.severity(allure.severity_level.MINOR)
class TestContactUs(TestBase):

    @pytest.fixture
    def info(self, run_env) -> dict:
        contact_us_info = r"data\contact_us_info.json" if run_env == "docker" else r"..\data\contact_us_info.json"
        return read_from_json(os.path.join(execute_path, contact_us_info))

    @pytest.fixture
    def expected_message(self) -> str:
        return "Thanks for contacting us! We will be in touch with you shortly."

    @default_logging
    @allure.description("Send a message using the Contact Us Form")
    @allure.title("Test the contact Us form")
    def test_contact(self, driver, info, contact_page, nav_bar, expected_message):
        with allure.step(f"Navigate to Home Page: {uic.HOME_PAGE}"):
            driver.get(uic.HOME_PAGE)
        with allure.step(f"Navigate to {NavBarElements.CONTACT_US.value} category"):
            nav_bar.navigate(NavBarElements.CONTACT_US)
        assert driver.current_url == uic.CONTACT_US
        with allure.step(f"Fill the contact us form"):
            submission_text = contact_page.contact(
                name=info['name'],
                email=info['email'],
                subject=info['subject'],
                message=info['message'])
        with allure.step("Compare the expected submission message with the actual one"):
            expected = expected_message
            assert submission_text == expected, f"expected {expected_message} got {submission_text}"
