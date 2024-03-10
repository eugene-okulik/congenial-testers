import allure
from test_UI_bukreev.pages.base_page import BasePage
from test_UI_bukreev.pages.locators import sale as loc
from selenium.webdriver.common.by import By


class Sale(BasePage):
    page_url = '/sale.html'

    @allure.step('Find all sale categories')
    def find_all_categories(self):
        categories_menu = self.find(loc.CATEGORIES_MENU)
        categories_title = self.find_all_in_element(categories_menu, loc.CATEGORIES_TITLE)
        self.all_title_texts = []
        for title_element in categories_title:
            title_text = title_element.text
            self.all_title_texts.append(title_text)

        return self.all_title_texts

    @allure.step('Check that all categories are exists')
    def check_categories_exists(self):
        needed_categories = ["WOMEN'S DEALS", "MENS'S DEALS", 'GEAR DEALS']
        self.check_are_equal(
            self.all_title_texts,
            needed_categories,
            f'Not all categories are exists. Exists only {self.all_title_texts}'
        )

    @allure.step('Click main block on page')
    def click_main_block(self):
        self.start_url = self.check_current_url()
        main_block = self.find(loc.MAIN_BANNER)
        main_block.click()
        print(self.start_url)

    @allure.step('Check that URL is change')
    def check_new_url(self):
        new_url = self.check_current_url()
        self.check_are_not_equal(self.start_url, new_url, "URL's are not different")

    @allure.step('Search all banners on page')
    def search_all_banners(self):
        main_block = self.find(loc.MAIN_BLOCK)
        self.banners = self.find_all_in_element(main_block, (By.XPATH, './/a'))

    @allure.step('Check count of banners on page')
    def check_banners_count(self):
        self.check_are_equal(len(self.banners), 6, 'Count of banners is not expected')
