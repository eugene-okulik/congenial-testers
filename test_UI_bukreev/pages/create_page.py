import allure
from test_UI_bukreev.pages.base_page import BasePage
from test_UI_bukreev.pages.locators import create_account as loc
from selenium.webdriver.common.action_chains import ActionChains


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Click submit button')
    def click_submit_button(self):
        submit_button = self.find(loc.BUTTON_CREATE)
        submit_button.click()

    @allure.step('Check count if required fields')
    def check_count_required_fields(self):
        required_fields = self.find_all(loc.REQUIRED_FIELDS)
        assert len(required_fields) == 5, 'There is no required field error message'

    @allure.step('Input password')
    def input_password(self, password):
        input_password = self.find(loc.INPUT_PASSWORD)
        action = ActionChains(self.driver)
        action.click(input_password)
        action.send_keys(password)
        action.perform()

    @allure.step('Check password strength')
    def check_password_strength(self, result):
        password_info = self.find(loc.PASSWORD_INFO)
        self.check_are_equal(password_info.text, result, 'Incorrect password strength')

    @allure.step('Fill all input fields')
    def fill_all_fields(self, first_name, last_name, email, password, confirm_password):
        input_first_name = self.find(loc.INPUT_FIRST_NAME).send_keys(first_name)
        input_last_name = self.find(loc.INPUT_LAST_NAME).send_keys(last_name)
        input_email = self.find(loc.INPUT_EMAIL).send_keys(email)
        input_password = self.find(loc.INPUT_PASSWORD).send_keys(password)
        input_confirm_password = self.find(loc.INPUT_CONFIRM_PASSWORD).send_keys(confirm_password)

    @allure.step('Check alert message')
    def check_alert_message(self):
        alert_message = self.find(loc.ALERT_MESSAGE)
        self.check_are_equal(
            alert_message.text,
            'Thank you for registering with Main Website Store.',
            'Incorrect alert message'
        )
