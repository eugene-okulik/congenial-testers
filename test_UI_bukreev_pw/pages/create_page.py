import allure
from test_UI_bukreev_pw.pages.base_page import BasePage
from test_UI_bukreev_pw.pages.locators import create_account as loc
from playwright.sync_api import expect


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Click submit button')
    def click_submit_button(self):
        submit_button = self.find(loc.BUTTON_CREATE)
        submit_button.click()

    @allure.step('Check count if required fields')
    def check_count_required_fields(self):
        required_fields = self.find(loc.REQUIRED_FIELDS)
        print(required_fields.count())
        expect(required_fields, 'There is no required field error message').to_have_count(5)

    @allure.step('Input password')
    def input_password(self, password):
        input_password = self.find(loc.INPUT_PASSWORD)
        input_password.press_sequentially(password)

    @allure.step('Check password strength')
    def check_password_strength(self, result):
        password_info = self.find(loc.PASSWORD_INFO)
        expect(password_info, 'Incorrect password strength').to_have_text(result)

    @allure.step('Fill all input fields')
    def fill_all_fields(self, first_name, last_name, email, password, confirm_password):
        input_first_name = self.find(loc.INPUT_FIRST_NAME)
        input_first_name.fill(first_name)
        input_last_name = self.find(loc.INPUT_LAST_NAME)
        input_last_name.fill(last_name)
        input_email = self.find(loc.INPUT_EMAIL)
        input_email.fill(email)
        input_password = self.find(loc.INPUT_PASSWORD)
        input_password.fill(password)
        input_confirm_password = self.find(loc.INPUT_CONFIRM_PASSWORD)
        input_confirm_password.fill(confirm_password)

    @allure.step('Check alert message')
    def check_alert_message(self):
        alert_message = self.find(loc.ALERT_MESSAGE)
        expect(
            alert_message,
            'Incorrect alert message'
        ).to_have_text('Thank you for registering with Main Website Store.')
