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
    match browser_type:
        case Drivers.CHROME:

            chrome_options = webdriver.ChromeOptions()
            add_arguments(chrome_options)
            return chrome_options

        case Drivers.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            return firefox_options


def add_arguments(options: ChromeOptions | FirefoxOptions) -> None:
    options.add_argument("start-maximized")


def create_capabilities(browser_type: Enum):
    try:
        # define capabilities
        capabilities = {
            "browserName": "",
            "browserVersion": "",
            "selenoid:options": {
                "enableVideo": True
            }
        }
        # read from browsers json file
        browsers = read_from_json(browsers_json)
        # get the browser string from browser type enum
        browser_type_val = browser_type.value.lower()
        # access the default version from browsers.json
        version = browsers[browser_type_val]['default']
        # change capabilities dictionary with new values
        capabilities["browserName"] = browser_type_val
        capabilities["browserVersion"] = version
        return capabilities
    except (FileNotFoundError, KeyError) as e:
        print("Wrong browser or version", e.message)


def create_driver(browser_type: Enum) -> webdriver:
    #
    try:
        return webdriver.Remote(command_executor=DOCKER_URL,
                                desired_capabilities=create_capabilities(browser_type),
                                options=create_options(browser_type))
    except WebDriverException as e:
        print(e)
