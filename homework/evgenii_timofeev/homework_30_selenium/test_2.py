import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver_my = webdriver.Chrome()
    driver_my.maximize_window()
    driver_my.implicitly_wait(10)
    return driver_my


def test_one(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")

    first_product = driver.find_element(By.CSS_SELECTOR, "div.product-item-info")
    product_name = driver.find_element(By.CSS_SELECTOR, ".product-item-link").text

    ActionChains(driver).move_to_element(first_product).perform()
    driver.find_element(By.CSS_SELECTOR, "[title='Add to Compare']").click()

    name_of_comparable_product = driver.find_element(
        By.CSS_SELECTOR, ".product-item.odd.last"
    ).text

    assert product_name in name_of_comparable_product, "Names aren't matched"
