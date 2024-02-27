import allure
from test_UI_eokulik.pages.base_page import BasePage
from test_UI_eokulik.pages.locators.whats_new import WhatsNewLocators as Loc


# SHOP_THE_YOGA_BUTTON = (By.CSS_SELECTOR, '.more.button')


class WhatsNew(BasePage):
    page_url = '/what-is-new.html'

    @allure.step('Click the button')
    def click_shop_the_yoga_button(self):
        # self.driver.find_element(By.CSS_SELECTOR, '.more.button').click()
        self.find(Loc.SHOP_THE_YOGA_BUTTON).click()

    @allure.step('Check that correct page is opened')
    def check_that_correct_url_is_opened(self):
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/collections/yoga-new.html'
