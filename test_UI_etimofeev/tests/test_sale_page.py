from test_UI_etimofeev.pages.sale_page import SalePage


def test_button(driver):
    collections_page = SalePage(driver)
    collections_page.open()
    collections_page.check_current_url()
    collections_page.check_the_page_name()
    collections_page.check_open_sale_product()
