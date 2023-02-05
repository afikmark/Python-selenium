import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from ui_test_urls import ui_constants as uic

class TestBase:
    @pytest.fixture
    def driver(self):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.get(uic.HOME_PAGE_URL)
            return driver
        except TimeoutException:
            print("The request has timed out")




