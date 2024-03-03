from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_UI_etimofeev.pages.base_page import BasePage
from test_UI_etimofeev.pages.locators.locators import AccountCreateLocators as Loc


class AccountCreatePage(BasePage):
    page_url = "/customer/account/create/"

    def fill_personal_information(self, first_name, last_name):
        first_name_field = self.driver.find_element(*Loc.FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(*Loc.LAST_NAME_FIELD)
        last_name_field.send_keys(last_name)

    def fill_sign_in_information(self, email, password):
        email_field = self.driver.find_element(*Loc.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.driver.find_element(*Loc.PASSWORD_FILED)
        ActionChains(self.driver).click(password_field).send_keys(password).perform()

        confirm_password = self.driver.find_element(*Loc.CONFIRM_PASSWORD_FIELD)
        confirm_password.send_keys(password)

    def press_create_account_button(self):
        self.driver.find_element(*Loc.CREATE_ACCOUNT_BUTTON).click()

    def check_strength_password(self):
        expected_strength = "Strong"
        base_strength = "No Password"
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(Loc.STRENGTH_PASSWORD, base_strength)
        )
        current_strength = self.driver.find_element(*Loc.STRENGTH_PASSWORD).text
        assert (
            expected_strength == current_strength
        ), f"Strength of the password isn't correct {current_strength}"

    def check_created_account_message(self):
        message = "Thank you for registering with Main Website Store."
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Loc.SUCCESS_MESSAGE)
        )
        actual_message = self.driver.find_element(*Loc.SUCCESS_MESSAGE).text
        assert message in actual_message, "The account creation message did not match."

    def check_names(self, first_name, last_name):
        current_data = self.driver.find_element(*Loc.CONTENT_ELEMENT)
        assert first_name in current_data.text and last_name in current_data.text, (
            f"First name {first_name} or Last " f"name {last_name} aren't matched"
        )
