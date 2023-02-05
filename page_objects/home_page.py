from selenium.common import NoSuchElementException
from functools import cached_property
from page_objects.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @cached_property
    def elements(self):
        return {
            'search_button': self.find_element(by='css', selector='.ast-header-search[data-section]'),
            'search_bar': self.find_element(by='css', selector='.search-field[type=search]'),
            'contact_us_button': self.find_element(by='xpath', selector='//*[@id="ast-hf-menu-1"]/li/a[contains(text(),"Contact Us")]')
        }

    def search(self, search_params: str):
        """
        :param search_params: str
        searches in the search bar on the amazon website
        """
        try:
            self.click(self.elements['search_button'])
            self.fill_text(self.elements['search_bar'], search_params)
        except NoSuchElementException:
            print(NoSuchElementException)
            self.close_driver()
        self.action('enter')

    def nav_contact_us(self):
        self.click(self.elements['contact_us_button'])
