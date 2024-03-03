from test_UI_etimofeev.pages.base_page import BasePage
from test_UI_etimofeev.pages.locators.locators import SaleLocators as Loc


class SalePage(BasePage):
    page_url = "/sale.html"

    def check_current_url(self):
        assert self.driver.current_url == self.base_url + self.page_url

    def check_the_page_name(self):
        expected_name = "Sale"
        current_name = self.driver.find_element(*Loc.NAME_OF_THE_PAGE)
        assert expected_name == current_name.text, "Names aren't matched"

    def check_open_sale_product(self):
        women_deal_button = self.driver.find_element(*Loc.WOMEN_DEAL_BUTTON)
        women_deal_button.click()
