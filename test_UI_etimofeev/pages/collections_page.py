from test_UI_etimofeev.pages.base_page import BasePage
from test_UI_etimofeev.pages.locators.locators import CollectionsLocators as Loc


class CollectionsPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def check_current_url(self):
        assert self.driver.current_url == self.base_url + self.page_url

    def check_the_page_name(self):
        expected_name = "Eco Friendly"
        current_name = self.driver.find_element(*Loc.NAME_OF_THE_PAGE)
        assert expected_name == current_name.text, "Names aren't matched"

    def check_switching_pages(self):
        self.scroll_page()
        next_page_button = self.driver.find_elements(*Loc.NEXT_PAGE_BUTTON)
        next_page_button[1].click()
        assert (
            self.driver.current_url
            == "https://magento.softwaretestingboard.com/collections/eco-friendly.html?p=2"
        )
