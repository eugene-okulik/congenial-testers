import allure
import pytest


@allure.feature('Eco-friendly page')
@allure.story('Count of shown items')
def test_show_item_per_page(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.chang_items_per_page('24')
    eco_friendly_page.check_count_items(12, 24)
    eco_friendly_page.chang_items_per_page('12')
    eco_friendly_page.check_count_items(12, 12)


@allure.feature('Eco-friendly page')
@allure.story('Add item to compare')
def test_add_to_compare(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.add_to_compare()
    eco_friendly_page.check_compare_list()


@allure.feature('Eco-friendly page')
@allure.story('Filter by shopping options')
@pytest.mark.parametrize('sort_option', [
    'Climate',
    'Pattern',
    'Sale',
    'Material'
])
def test_shopping_options(eco_friendly_page, sort_option):
    eco_friendly_page.open()
    eco_friendly_page.sort_by(sort_option)
    eco_friendly_page.check_count_sort_items()
