from selenium.webdriver.common.by import By


BUTTON_CREATE = (By.CSS_SELECTOR, 'button.submit')
REQUIRED_FIELDS = (By.XPATH, "//div[text()='This is a required field.']")
INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
PASSWORD_INFO = (By.CSS_SELECTOR, '#password-strength-meter-label')
INPUT_FIRST_NAME = (By.CSS_SELECTOR, '#firstname')
INPUT_LAST_NAME = (By.CSS_SELECTOR, '#lastname')
INPUT_EMAIL = (By.CSS_SELECTOR, '#email_address')
INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#password-confirmation')
ALERT_MESSAGE = (By.XPATH, "//div[@data-ui-id='message-success']/div")
