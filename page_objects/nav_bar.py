import pytest
from selenium.common import NoSuchElementException
from .base_page import BasePage
from functools import cached_property


class NavBar(BasePage):
    def __init__(self, driver):
        super(NavBar, self).__init__(driver)

    @cached_property
    def navbar(self):
        return {
            'home': self.find_element(by='xpath', selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Home")]'),
            'store': self.find_element(by='xpath', selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Store")]'),
            'men': self.find_element(by='xpath', selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Men")]'),
            'women': self.find_element(by='xpath', selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Women")]'),
            'accessories': self.find_element(by='xpath', selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Accessories")]'),
            'about': self.find_element(by='xpath', selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"About")]'),
            'contact us': self.find_element(by='xpath', selector='//*[@id="ast-desktop-header"]//*[@class="menu-link"][contains(text(),"Contact Us")]'),
        }

    def navigate(self, category: str):
        if not category:
            pytest.exit("please use a valid selector")
        try:
            self.click(self.navbar[f"{category.lower()}"])
        except (KeyError, NoSuchElementException) as e:
            print(e)
            self.quit_driver()
