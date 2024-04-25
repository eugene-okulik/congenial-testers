from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    my_driver.implicitly_wait(10)
    return my_driver


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    tovar_link = driver.find_element(By.CSS_SELECTOR, ".card-title a[href='prod.html?idp_=1']")
    tovar_name = tovar_link.text
    ActionChains(driver).key_down(Keys.CONTROL).click(tovar_link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]').click()
    alert = Alert(driver)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    item = driver.find_element(By.TAG_NAME, 'tbody')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'success')))
    assert tovar_name in item.text, 'Товар в корзине не совпадает с выбранным'


def test_two(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_product = driver.find_element(By.CSS_SELECTOR, "div.product-item-info")
    product_name = driver.find_element(By.CSS_SELECTOR, ".product-item-link").text
    ActionChains(driver).move_to_element(first_product).perform()
    driver.find_element(By.CSS_SELECTOR, "[title='Add to Compare']").click()
    compare_products = driver.find_element(By.CSS_SELECTOR, ".product-item.odd.last").text
    assert product_name in compare_products, "Имя товара не совпало"
