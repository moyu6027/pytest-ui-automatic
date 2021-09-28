# encoding: utf-8
"""
Base Page Object
"""
import allure
from playwright.sync_api import TimeoutError as TError
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step('Click locator - {locator}')
    def click(self, locator: str):
        self.page.click(locator)

    @allure.step('Check checkbox locator - {locator}')
    def check(self, locator: str):
        self.page.check(locator)

    @allure.step('Uncheck checkbox locator - {locator}')
    def uncheck(self, locator: str):
        self.page.check(locator)

    @allure.step('Hover locator - {locator}')
    def hover(self, locator: str):
        self.page.hover(locator)

    @allure.step('Go to url - {url}')
    def go_to_url(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state()

    @allure.step('Type text - {text} into locator - {locator}')
    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    @allure.step('Select option - {option} in locator - {locator}')
    def select_option(self, locator: str, option: str):
        self.page.select_option(locator, option)

    @allure.step('Is element - {locator} present')
    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator)
            return True
        except TError:
            return False

    @allure.step('Is element - {locator} hidden')
    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, state='hidden')
            return True
        except TError:
            return False
