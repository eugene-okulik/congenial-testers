from test_UI_eokulik.pages.whats_new_page import WhatsNew
from test_UI_eokulik.pages.promo_page import PromoPage


def test_button(driver):
    whats_new_page = WhatsNew(driver)
    whats_new_page.open()
    whats_new_page.click_shop_the_yoga_button()
    whats_new_page.check_that_correct_url_is_opened()
    promo_page = PromoPage(driver)
    promo_page.page_has_correct_title('New Luma Yoga Collection')
