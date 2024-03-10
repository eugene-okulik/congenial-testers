from selenium.webdriver.remote.webdriver import WebDriver
import allure
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.item_name = None
        self.sort_items_count = None
        self.all_title_texts = None
        self.start_url = None
        self.banners = None

    @allure.step('Open the page')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened by URL for this page')

    @allure.step('Find element by locator')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Find elements by locator')
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Find element by locator in element')
    def find_in_element(self, element, locator):
        return element.find_element(*locator)

    @allure.step('Find all elements by locator in element')
    def find_all_in_element(self, element, locator):
        return element.find_elements(*locator)

    @allure.step('Start action')
    def action(self):
        action = ActionChains(self.driver)
        return action

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
        current_url = self.driver.current_url
        return current_url
