from selenium import webdriver
from enum import Enum
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common import WebDriverException
from pytest import fixture


class Drivers(Enum):
    CHROME = "Chrome"
    FIREFOX = "Firefox"
    EDGE = "Edge"




def create_options(browser_type) -> ChromeOptions | FirefoxOptions | EdgeOptions:
    if browser_type == Drivers.CHROME:
        chrome_options = webdriver.ChromeOptions()
        add_arguments(chrome_options)
        return chrome_options
    elif browser_type == Drivers.FIREFOX:
        firefox_options = webdriver.FirefoxOptions()
        return firefox_options
    elif browser_type == Drivers.EDGE:
        edge_options = webdriver.EdgeOptions()
        add_arguments(edge_options)
        return edge_options


def add_arguments(options: ChromeOptions | FirefoxOptions | EdgeOptions) -> None:
    options.add_argument("start-maximized")


def create_driver(browser_type) -> webdriver:
    try:
        if browser_type == Drivers.CHROME:
            chrome_options = create_options(browser_type)
            return webdriver.Chrome(options=chrome_options)
        elif browser_type == Drivers.FIREFOX:
            return webdriver.Firefox()
        elif browser_type == Drivers.EDGE:
            edge_options = create_options(browser_type)
            return webdriver.Edge(options=edge_options)
    except WebDriverException as e:
        print(e)
