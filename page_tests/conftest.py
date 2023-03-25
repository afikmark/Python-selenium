import os

from selenium import webdriver
from enum import Enum
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common import WebDriverException
from enums.drivers import Drivers
from utils.files import read_from_json
from utils.logger import logger
from urls.docker import DOCKER_URL
from paths.paths import browsers_json


def create_options(browser_type: Enum) -> ChromeOptions | FirefoxOptions | EdgeOptions:
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

        case Drivers.EDGE:
            edge_options = webdriver.EdgeOptions()
            add_arguments(edge_options)
            return edge_options


def add_arguments(options: ChromeOptions | FirefoxOptions | EdgeOptions) -> None:
    """
    Receives Options object
    adds arguments to options
    """
    options.add_argument("start-maximized")
    logger.info("Adding argument")


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
    except KeyError as e:
        logger.exception(f"{e}: Wrong browser or version. Selenoid doesn't support Edge browser, please run locally")
    except FileNotFoundError as e:
        logger.exception(f"{e}: Wrong profile path:\n"
                         "if running from jenkins: in paths.py change to jenkins profile\n"
                         "if running from local machine: change to local_profile\n")


def create_driver(browser_type: Enum) -> webdriver:
    """
    Receives browser type
    creates webdriver object
    """
    # Get the value of the 'RUN_ENV' environment variable
    run_env = os.environ.get('RUN_ENV')

    try:
        if run_env == 'docker':
            logger.info(f"Creating remote {browser_type.value} driver ")
            return webdriver.Remote(command_executor=DOCKER_URL,
                                    desired_capabilities=create_capabilities(browser_type),
                                    options=create_options(browser_type))
        else:
            match browser_type:
                case Drivers.CHROME:
                    logger.info("Creating local Chrome Driver")
                    return webdriver.Chrome(options=create_options(browser_type))

                case Drivers.FIREFOX:
                    logger.info("Creating local Firefox Driver")
                    return webdriver.Firefox(options=create_options(browser_type))
                case Drivers.EDGE:
                    logger.info("Creating local Edge Driver")
                    return webdriver.Edge(options=create_options(browser_type))

    except WebDriverException:
        logger.exception(WebDriverException)
