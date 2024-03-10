import allure
from test_UI_bukreev.pages.base_page import BasePage
from test_UI_bukreev.pages.locators import eco_friendly as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Change item per page')
    def chang_items_per_page(self, value):
        limiter = self.find_all(loc.SELECT_PER_PAGE)
        select = Select(limiter[1])
        select.select_by_value(value)

    @allure.step('Check that count of items is change')
    def check_count_items(self, minimum, maximum):
        items = self.find_all(loc.ITEMS)
        self.check_are_between(
            minimum,
            len(items),
            maximum,
            f'Count of items is not in normal range. Count = {len(items)}'
        )

    @allure.step('Add item to compare list')
    def add_to_compare(self):
        items = self.find_all(loc.ITEMS)
        button_compare = self.find(loc.BUTTON_COMPARE)
        self.item_name = items[0].text.split('\n')[0]
        action = ActionChains(self.driver)
        action.move_to_element(items[0]).click(button_compare).perform()
        return self.item_name

    @allure.step('Check compare list')
    def check_compare_list(self):
        compare_list = self.find(loc.COMPARE_LIST)
        compare_item_text = self.find_in_element(compare_list, loc.COMPARE_ITEM).text
        self.check_are_equal(self.item_name, compare_item_text, 'There is no such element in compare list')

    @allure.step('Sort items by something')
    def sort_by(self, sort_option):
        sort_block = self.find(loc.SORT_BLOCK)
        sort_by = self.find_in_element(sort_block, (By.XPATH, f"//div[contains(text(), '{sort_option}')]"))
        sort_by.click()
        chose_first = self.find_in_element(sort_by, (By.XPATH, f"//div[contains(text(), '{sort_option}')]/..//a"))
        self.sort_items_count = self.find_in_element(chose_first, loc.SORT_COUNT).text.split('\n')[0]
        chose_first.click()
        return self.sort_items_count

    @allure.step('Check count of sort items')
    def check_count_sort_items(self):
        items = self.find_all(loc.ITEMS)
        print(len(items), int(self.sort_items_count))
        self.check_are_equal(
            len(items),
            int(self.sort_items_count),
            f'Items count ({len(items)}) is not like number in sort block ({int(self.sort_items_count)})'
        )
