from selenium.webdriver.remote.webdriver import WebDriver
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

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

    def scroll_page(self, pixels=None):
        height = pixels if pixels else 'document.body.scrollHeight'
        self.driver.execute_script(f"window.scrollTo(0, {height});")
