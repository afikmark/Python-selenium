import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common import WebDriverException
from enums.drivers import Drivers
from enums.run_env import RunEnv
from utils.files import read_from_json
from utils.logger import logger
from urls.docker import DOCKER_URL
from paths.paths import browsers_json_remote, browsers_json_local

# Get the value of the 'RUN_ENV' and 'BROWSER' environment variables
run_env: str | None = os.environ.get('RUN_ENV')
browser: str = os.environ.get('BROWSER') if os.environ.get('BROWSER') is not None else Drivers.CHROME.value


def create_options(browser_type: str) -> ChromeOptions | FirefoxOptions | EdgeOptions:
    """
    Receives browser type
    creates webdriver options object matching browser type enum input
    returns options object
    """
    match browser_type:
        case Drivers.CHROME.value:

            chrome_options = webdriver.ChromeOptions()
            add_arguments(chrome_options)
            return chrome_options

        case Drivers.FIREFOX.value:
            firefox_options = webdriver.FirefoxOptions()
            return firefox_options

        case Drivers.EDGE.value:
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


def create_capabilities(browser_type) -> dict:
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
        profile_path = browsers_json_local
        if run_env == RunEnv.DOCKER.value:
            profile_path = browsers_json_remote
        browsers_path = read_from_json(profile_path)
        browser_type_val = browser_type
        version = browsers_path[browser_type_val]['default']
        capabilities["browserName"] = browser_type_val
        capabilities["browserVersion"] = version
        return capabilities
    except KeyError as e:
        logger.exception(f"{e}: Wrong browser or version. Selenoid doesn't support Edge browser, please run locally")
    except FileNotFoundError as e:
        logger.exception(f"{e}: Wrong profile path:\n"
                         "if running from jenkins: in paths.py change to jenkins profile\n"
                         "if running from local machine: change to local_profile\n")


def create_driver() -> webdriver:
    """
    Receives browser type
    creates webdriver object
    """

    try:
        if run_env == RunEnv.DOCKER.value:
            logger.info(f"Creating remote {browser} driver ")
            return webdriver.Remote(command_executor=DOCKER_URL,
                                    desired_capabilities=create_capabilities(browser),
                                    options=create_options(browser))
        else:
            match browser:
                case Drivers.FIREFOX.value:
                    logger.info("Creating local Firefox Driver")
                    print("Creating local Firefox Driver")
                    return webdriver.Firefox(options=create_options(browser_type=browser))
                case Drivers.EDGE.value:
                    logger.info("Creating local Edge Driver")
                    print("Creating local Edge Driver")
                    return webdriver.Edge(options=create_options(browser_type=browser))
                case _:
                    logger.info("Creating local Chrome Driver")
                    print("Creating local Chrome Driver")
                    return webdriver.Chrome(options=create_options(browser_type=Drivers.CHROME.value))

    except (WebDriverException, AttributeError) as e:
        print(e)
        logger.exception(e)
