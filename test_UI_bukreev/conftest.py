from selenium import webdriver
import pytest
from test_UI_bukreev.pages.create_page import CreateAccount
from test_UI_bukreev.pages.eco_friendly_page import EcoFriendly
from test_UI_bukreev.pages.sale_page import Sale


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return Sale(driver)
