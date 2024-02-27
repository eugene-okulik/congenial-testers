from selenium.webdriver.common.by import By
import allure
from test_UI_eokulik.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


ERROR_MESSAGE = (By.CSS_SELECTOR, 'div[role="alert"] > div > div')


class SignIn(BasePage):
    page_url = '/customer/account/login'

    @allure.step('Enter email')
    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, 'email')
        email_field.send_keys(email)

    @allure.step('Enter password')
    def enter_password(self, password):
        passw = self.driver.find_element(By.ID, 'pass')
        passw.send_keys(password)

    @allure.step('Click the button')
    def click_submit_button(self):
        self.driver.find_element(By.ID, 'send2').click()

    @staticmethod
    def text_not_empty(locator):

        def _predicate(driver):
            return True if driver.find_element(*locator).text else False

        return _predicate

    @allure.step('Check message')
    def check_error_message(self, message):
        # message_elt = self.find(ERROR_MESSAGE)
        WebDriverWait(self.driver, 10).until(self.text_not_empty(ERROR_MESSAGE))
        assert self.find(ERROR_MESSAGE).text == message, f'Message text is {self.find(ERROR_MESSAGE).text}'
