import allure
from playwright.sync_api import Page


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page
        self.item_name = None
        self.sort_items_count = None
        self.all_title_texts = None
        self.start_url = None
        self.banners = None

    @allure.step('Open the page')
    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}', wait_until='load', timeout=100000)
        else:
            raise NotImplementedError('Page can not be opened by URL for this page')

    @allure.step('Find element by locator')
    def find(self, locator):
        return self.page.locator(locator)

    @allure.step('Find element by locator in element')
    def find_in_element(self, parrent_locator, child_locator):
        parent = self.page.query_selector(parrent_locator)
        return parent.query_selector_all(child_locator)

    @allure.step('Find all elements by locator in element')
    def find_all_in_element(self, element, locator):
        return element.query_selector(locator)

    @allure.step('Check a == b')
    def check_are_equal(self, a, b, message):
        assert a == b, message

    @allure.step('Check a != b')
    def check_are_not_equal(self, a, b, message):
        assert a != b, message

    @allure.step('Check a < result < b')
    def check_are_between(self, a, result, b, message):
        assert a <= result <= b, message

    @allure.step('Check current URL')
    def check_current_url(self):
        current_url = self.page.url
        return current_url
