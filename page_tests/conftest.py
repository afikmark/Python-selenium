from selenium import webdriver
from enum import Enum

from selenium.common import WebDriverException


class Drivers(Enum):
    CHROME = "Chrome"
    FIREFOX = "Firefox"
    EDGE = "Edge"


def create_options(browser_type):
    if browser_type == Drivers.CHROME:
        return webdriver.ChromeOptions()
    elif browser_type == Drivers.FIREFOX:
        return webdriver.FirefoxOptions()
    elif browser_type == Drivers.EDGE:
        return webdriver.EdgeOptions()


def create_driver(browser_type) -> webdriver:
    try:
        if browser_type == Drivers.CHROME:
            return webdriver.Chrome()
        elif browser_type == Drivers.FIREFOX:
            return webdriver.Firefox()
        elif browser_type == Drivers.EDGE:
            return webdriver.Edge()
    except WebDriverException as e:
        print(e)
