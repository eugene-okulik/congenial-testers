import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from test_UI_eokulik.pages.sign_in_page import SignIn
import random


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome = webdriver.Chrome(options=options)
    sleep(3)
    chrome.maximize_window()
    yield chrome
    chrome.save_screenshot(f'{random.randrange(100)}.png')


@pytest.fixture()
def sign_in_page(driver):
    return SignIn(driver)
