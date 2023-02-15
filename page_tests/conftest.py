from selenium import webdriver
from enum import Enum
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common import WebDriverException
from enums.drivers import Drivers


def create_options(browser_type) -> ChromeOptions | FirefoxOptions | EdgeOptions:
    match browser_type:
        case Drivers.CHROME:

            chrome_options = webdriver.ChromeOptions()
            add_arguments(chrome_options)
            return chrome_options

        case Drivers.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            return firefox_options

        case Drivers.EDGE:
            edge_options = webdriver.EdgeOptions()
            add_arguments(edge_options)
            return edge_options


def add_arguments(options: ChromeOptions | FirefoxOptions | EdgeOptions) -> None:
    options.add_argument("start-maximized")


def create_driver(browser_type: Enum) -> webdriver:
    try:
        match browser_type:

            case Drivers.CHROME:
                chrome_options = create_options(browser_type)
                return webdriver.Chrome(options=chrome_options)

            case Drivers.FIREFOX:
                return webdriver.Firefox()

            case Drivers.EDGE:
                edge_options = create_options(browser_type)
                return webdriver.Edge(options=edge_options)

    except WebDriverException as e:
        print(e)
