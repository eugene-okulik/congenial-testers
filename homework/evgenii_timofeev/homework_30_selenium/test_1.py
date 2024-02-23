import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver_my = webdriver.Chrome()
    driver_my.maximize_window()
    driver_my.implicitly_wait(10)
    return driver_my


def test_one(driver):
    driver.get("https://www.demoblaze.com/index.html")
    # Actions with opening of the product
    link_to_a_good = driver.find_element(
        By.CSS_SELECTOR, ".card-title a[href='prod.html?idp_=1']"
    )
    name_of_a_product = link_to_a_good.text
    ActionChains(driver).key_down(Keys.CONTROL).click(link_to_a_good).perform()
    # Actions with buying
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    button = driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(1)']")
    driver.execute_script("arguments[0].click();", button)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    # Acctions with a cart
    cart = driver.find_element(By.ID, "cartur")
    driver.execute_script("arguments[0].click();", cart)
    product_name = driver.find_element(
        By.XPATH, f"//td[contains(text(), '{name_of_a_product}')]"
    ).text
    assert name_of_a_product == product_name, (
        f"Names of products aren't matched. Product in a cart = {product_name},"
        f" Name of the appliance = {name_of_a_product}"
    )
