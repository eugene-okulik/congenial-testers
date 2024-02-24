import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

languages = {1: "Python", 2: "Ruby", 3: "JavaScript", 4: "Java", 5: "C#"}
random_key = random.choice(list(languages.keys()))


@pytest.fixture
def driver():
    driver_my = webdriver.Chrome()
    driver_my.maximize_window()
    return driver_my


def test_one(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    search_line = driver.find_element(By.ID, "id_choose_language")
    select = Select(search_line)
    select.select_by_value(str(random_key))
    driver.find_element(By.ID, "submit-id-submit").click()
    result = driver.find_element(By.ID, "result-text").text
    assert (
        result == languages[random_key]
    ), f"Text on the page {result} is not matched to {languages[random_key]}"
