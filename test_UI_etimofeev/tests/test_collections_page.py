from test_UI_etimofeev.pages.collections_page import CollectionsPage


def test_button(driver):
    collections_page = CollectionsPage(driver)
    collections_page.open()
    collections_page.check_current_url()
    collections_page.check_the_page_name()
    collections_page.check_switching_pages()
