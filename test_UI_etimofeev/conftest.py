import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    return chrome
