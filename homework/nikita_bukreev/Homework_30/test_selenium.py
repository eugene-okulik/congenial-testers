from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest
import os


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    gadget = 'Nexus 6'
    find_nexus = driver.find_element(By.LINK_TEXT, gadget)
    action = ActionChains(driver)
    # не смог побоброть мак и сделть не через комманд на маке, но решил сделать тест кроссплатформенным
    match os.uname().sysname:
        case 'Darwin':
            action.key_down(Keys.COMMAND)
        case 'Linux':
            action.key_down(Keys.CONTROL)
        case 'Windows':
            action.key_down(Keys.CONTROL)
        case _:
            action.key_down(Keys.CONTROL)
    action.click(find_nexus).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.LINK_TEXT, 'Add to cart')
    driver.execute_script("arguments[0].click();", add_to_cart)
    alert = Alert(driver)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.ID, 'cartur')
    driver.execute_script("arguments[0].click();", cart)
    item = driver.find_element(By.TAG_NAME, 'tbody')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'success')))
    assert gadget in item.text, 'В корзине другой товар'


def test_two(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    item = driver.find_elements(By.CSS_SELECTOR, '[class="product-item-info"]')
    item_name = item[0].text.split('\n')[0]
    compare = item[0].find_element(By.CSS_SELECTOR, 'a.action.tocompare')
    action = ActionChains(driver)
    action.move_to_element(item[0]).click(compare).perform()
    find_compare = driver.find_element(By.CSS_SELECTOR, '.product-item.odd.last')
    find_in_compare = find_compare.find_element(By.CSS_SELECTOR, '.product-item-name')
    assert item_name == find_in_compare.text, 'Элемент не появился в списке сравнения'
