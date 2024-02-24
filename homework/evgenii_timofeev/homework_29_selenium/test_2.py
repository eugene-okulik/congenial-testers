import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver_my = webdriver.Chrome()
    driver_my.maximize_window()
    return driver_my


def test_one(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "#start > button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!"))
    final_text = driver.find_element(By.ID, "finish").text
    assert final_text == "Hello World!", "Text isn't matched"
