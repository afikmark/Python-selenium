import pytest
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from functools import cached_property
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass
class NavBarElements:
    home: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Home")]'
    store: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Store")]'
    men: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Men")]'
    women: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Women")]'
    accessories: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Accessories")]'
    about: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"About")]'
    contact_us: str = '//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Contact Us")]'


class NavBar(BasePage):
    def __init__(self, driver):
        super(NavBar, self).__init__(driver)

    @cached_property
    def navbar(self) -> dict:
        return {
            'home': self.find_element(by='xpath', selector=NavBarElements.home),
            'store': self.find_element(by='xpath', selector=NavBarElements.store),
            'men': self.find_element(by='xpath', selector=NavBarElements.men),
            'women': self.find_element(by='xpath', selector=NavBarElements.women),
            'accessories': self.find_element(by='xpath', selector=NavBarElements.accessories),
            'about': self.find_element(by='xpath', selector=NavBarElements.about),
            'contact us': self.find_element(by='xpath', selector=NavBarElements.contact_us),
        }

    def get_element(self, category: str) -> WebElement:
        return self.navbar[f"{category.lower()}"]

    def navigate(self, category: str):
        if not category:
            pytest.exit("please use a valid selector")
        try:
            self.click(self.get_element(category))
        except (KeyError, NoSuchElementException) as e:
            print(e)
            self.quit_driver()
