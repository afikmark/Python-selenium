from abc import ABC, abstractmethod
from typing import Any

import allure
from selenium.webdriver.remote.webelement import WebElement
from page_objects.base_page import BasePage


class Forms(ABC):
    @abstractmethod
    def fill_form(self, *inputs, **input_fields):
        """
        This method is responsible to fill a form
        """


class BillingForm(Forms):

    def fill_form(self, inputs: dict, **fields):
        with allure.step(f"fill name using: '{inputs['name']}'"):
            fields['First name'].send_keys(inputs['First name'])
        with allure.step(f"fill last name using: '{inputs['Last name']}'"):
            fields['Last name'].send_keys(inputs['Last name'])
        with allure.step(f"fill Company using: '{inputs['Company']}'"):
            fields['Company name(optional)'].send_keys(inputs['Company'])
        with allure.step(f"select a Country using: '{inputs['Country']}'"):
            BasePage.select(fields['Country/Region'], value=inputs['Country'])
        with allure.step(f"fill Street address using: '{inputs['Street address']}'"):
            fields['Street address'].send_keys(inputs['Street address'])
        with allure.step(f"fill Apartment using: '{inputs['Apartment']}'"):
            fields['Apartment, suite, unit, etc. (optional)'].send_keys(inputs['Apartment'])
        with allure.step(f"fill Post code using: '{inputs['Post code']}'"):
            fields['Postcode / ZIP'].send_keys(inputs['Post code'])
        with allure.step(f"fill City using: '{inputs['City']}'"):
            fields['Town / City'].send_keys(inputs['City'])
        with allure.step(f"fill Order notes using: '{inputs['Order notes']}'"):
            fields['Order Comments'].send_keys(inputs['Order notes'])
        with allure.step(f"fill Phone using: '{inputs['Phone']}'"):
            fields['Phone'].send_keys(inputs['Phone'])
        with allure.step(f"fill Email address using: '{inputs['Email address']}'"):
            fields['Email address'].send_keys(inputs['Email address'])


class ContactUsForm(Forms):

    def fill_form(self, *fields, **user_info):
        with allure.step(f"fill name using: '{user_info['name']}'"):
            fields[0]['name'].send_keys(user_info['name'])
        with allure.step(f"fill subject using: '{user_info['subject']}'"):
            fields[0]['subject'].send_keys(user_info['subject'])
        with allure.step(f"fill email using: '{user_info['email']}'"):
            fields[0]['email'].send_keys(user_info['email'])
        with allure.step(f"fill message using: '{user_info['message']}'"):
            fields[0]['message'].send_keys(user_info['message'])
