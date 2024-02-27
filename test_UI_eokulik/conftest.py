import pytest
from selenium import webdriver
from time import sleep
from test_UI_eokulik.pages.sign_in_page import SignIn


@pytest.fixture()
def driver():
    chrome = webdriver.Chrome()
    sleep(3)
    chrome.maximize_window()
    return chrome


@pytest.fixture()
def sign_in_page(driver):
    return SignIn(driver)
