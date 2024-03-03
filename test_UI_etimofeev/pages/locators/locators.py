from selenium.webdriver.common.by import By


class AccountCreateLocators:
    FIRST_NAME_FIELD = (By.ID, "firstname")
    LAST_NAME_FIELD = (By.ID, "lastname")
    EMAIL_FIELD = (By.ID, "email_address")
    PASSWORD_FILED = (By.ID, "password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "password-confirmation")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[class = 'action submit primary']")
    STRENGTH_PASSWORD = (By.ID, "password-strength-meter-label")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id='message-success']")
    CONTENT_ELEMENT = (By.CLASS_NAME, "box-content")


class CollectionsLocators:
    NAME_OF_THE_PAGE = (By.CSS_SELECTOR, "[data-ui-id='page-title-wrapper']")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "a.action.next")


class SaleLocators:
    NAME_OF_THE_PAGE = (By.CSS_SELECTOR, "[data-ui-id='page-title-wrapper']")
    WOMEN_DEAL_BUTTON = (By.CSS_SELECTOR, "[class='more button']")
