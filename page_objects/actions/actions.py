from abc import ABC, abstractmethod
from enum import Enum
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from enums.keyboard_keys import KeyboardKeys


class Actions(ABC):

    @abstractmethod
    def action(self, *value):
        """
        This method is responsible on performing an action in the webpage
        """


class KeyBoardActions(Actions):

    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(driver)
        super(KeyBoardActions, self).__init__()

    def action(self, key) -> None:
        """
        This method is responsible on performing a keyboard action in the webpage
        """
        match key:
            case KeyboardKeys.ENTER:
                self.action_chains.send_keys(Keys.ENTER).perform()
            case KeyboardKeys.PAGEUP:
                self.action_chains.send_keys(Keys.PAGE_UP).perform()
            case KeyboardKeys.PAGEDOWN:
                self.action_chains.send_keys(Keys.PAGE_DOWN).perform()

    def key_down_action(self, key: Enum):
        """
        This method is responsible on performing a key down without releasing it
        (useful for modifier keys (Control, Alt and Shift).
        """
        if key not in [KeyboardKeys.CONTROL, KeyboardKeys.ALT, KeyboardKeys.SHIFT]:
            raise ValueError('Keyboard keys should only be: Control, Alt and Shift')
        self.action_chains.key_down(key)


class MouseActions(Actions):
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        super(MouseActions, self).__init__()

    def key_down_action(self, element: WebElement = None) -> None:
        """
        This method is responsible on performing a double click mouse action in the webpage
        if provided an element, double on click an element
        """
        self.action.double_click(on_element=element)

    def action(self, source: WebElement, target: WebElement) -> None:
        """
        This method is responsible on performing drag and drop action in the webpage
        """
        self.action.drag_and_drop(source, target)
