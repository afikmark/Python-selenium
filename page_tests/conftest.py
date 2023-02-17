from selenium import webdriver
from enum import Enum
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common import WebDriverException
from enums.drivers import Drivers
from utils.files import read_from_json
from urls.docker import DOCKER_URL
from paths.paths import browsers_json


def create_options(browser_type: Enum) -> ChromeOptions | FirefoxOptions:
    """
    Receives browser type
    creates webdriver options object matching browser type enum input
    returns options object
    """
    match browser_type:
        case Drivers.CHROME:

            chrome_options = webdriver.ChromeOptions()
            add_arguments(chrome_options)
            return chrome_options

        case Drivers.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            return firefox_options


def add_arguments(options: ChromeOptions | FirefoxOptions) -> None:
    """
    Receives Options object
    adds arguments to options
    """
    options.add_argument("start-maximized")


def create_capabilities(browser_type: Enum) -> dict:
    """
     Receives a browser type Enum
     defines a capabilities dictionary to pass
     reads from browser.json file located in selenoid folder
     sets capabilities browser type and version via the input given
     and browser.json file
     returns capabilities
    """
    try:

        capabilities = {
            "browserName": "",
            "browserVersion": "",
            "selenoid:options": {
                "enableVideo": True
            }
        }
        browsers = read_from_json(browsers_json)
        browser_type_val = browser_type.value.lower()
        version = browsers[browser_type_val]['default']
        capabilities["browserName"] = browser_type_val
        capabilities["browserVersion"] = version
        return capabilities
    except (FileNotFoundError, KeyError) as e:
        print("Wrong browser or version", e.message)


def create_driver(browser_type: Enum) -> webdriver:
    """
    Receives browser type
    creates webdriver object
    """
    try:
        return webdriver.Remote(command_executor=DOCKER_URL,
                                desired_capabilities=create_capabilities(browser_type),
                                options=create_options(browser_type))
    except WebDriverException as e:
        print(e)
