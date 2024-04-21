import allure


@allure.feature('Sale page')
@allure.story('Shown sale categories')
def test_show_item_per_page(sale_page):
    sale_page.open()
    sale_page.find_all_categories()
    sale_page.check_categories_exists()


@allure.feature('Sale page')
@allure.story('Check main block is clickable')
def test_clickable_block(sale_page):
    sale_page.open()
    sale_page.click_main_block()
    (sale_page
     .check_new_url())


@allure.feature('Sale page')
@allure.story('Check page have six banners')
def test_banners_count(sale_page):
    sale_page.open()
    sale_page.search_all_banners()
    sale_page.check_banners_count()
