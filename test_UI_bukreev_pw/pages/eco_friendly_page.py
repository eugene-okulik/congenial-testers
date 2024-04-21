import allure
from test_UI_bukreev_pw.pages.base_page import BasePage
from test_UI_bukreev_pw.pages.locators import eco_friendly as loc
from playwright.sync_api import expect
import re


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Change item per page')
    def chang_items_per_page(self, value):
        limiter = self.find(loc.SELECT_PER_PAGE).nth(1)
        limiter.select_option(value)
        # if value != '12':  #  костыль
        #     expect(self.page).to_have_url(re.compile('product_list_limit'))
        # else:
        #     expect(self.page).not_to_have_url(re.compile('product_list_limit'))
        # expect(self.page.locator('.not-logged-in').first).not_to_be_empty()

        # limiter.wait_for(timeout=10000) # тоже костыль

    @allure.step('Check that count of items is change')
    def check_count_items(self, minimum, maximum):
        items = self.find(loc.ITEMS)
        items_count = items.count()
        # оставил обычный ассерт, не смог подобрать нормальный экспект
        self.check_are_between(
            minimum,
            items_count,
            maximum,
            f'Count of items is not in normal range. Count = {items_count}'
        )

    @allure.step('Add item to compare list')
    def add_to_compare(self):
        items = self.find(loc.ITEMS)
        button_compare = self.find(loc.BUTTON_COMPARE).nth(0)
        self.item_name = items.nth(0).inner_text().split('\n')[0]
        items.nth(0).hover()
        button_compare.click()
        return self.item_name

    @allure.step('Check compare list')
    def check_compare_list(self):
        self.page.wait_for_load_state('networkidle')  # иначе плэйврайт не ждет перезагрухки страницы((
        compare_item = self.find_in_element(loc.COMPARE_LIST, loc.COMPARE_ITEM)
        # оставил ассерт, ибо простое сравнени в expect я не нашел,
        # а всякие to_have_text выдавали ошибку,
        # возможно из-за того, что compare_item это ElementHandle
        self.check_are_equal(self.item_name, compare_item.inner_text(), 'There is no such element in compare list')

    @allure.step('Sort items by something')
    def sort_by(self, sort_option):
        sort_by = self.find_in_element(loc.SORT_BLOCK, f"//div[contains(text(), '{sort_option}')]")
        sort_by.click()
        chose_first = self.find_all_in_element(sort_by, "..//a")
        self.sort_items_count = self.find_all_in_element(chose_first, loc.SORT_COUNT).text_content().split('\n')[0]
        chose_first.click()
        return self.sort_items_count

    @allure.step('Check count of sort items')
    def check_count_sort_items(self):
        items = self.find(loc.ITEMS)
        self.check_are_equal(
            items.count(),
            int(self.sort_items_count),
            f'Items count ({items.count()}) is not like number in sort block ({int(self.sort_items_count)})'
        )
