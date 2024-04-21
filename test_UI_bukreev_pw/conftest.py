import pytest
from test_UI_bukreev_pw.pages.create_page import CreateAccount
from test_UI_bukreev_pw.pages.eco_friendly_page import EcoFriendly
from test_UI_bukreev_pw.pages.sale_page import Sale
from playwright.sync_api import BrowserContext


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_account_page(page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()
def sale_page(page):
    return Sale(page)
