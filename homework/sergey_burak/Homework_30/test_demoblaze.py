from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    return my_driver


def test_demoblaze(driver):
    driver.get('https://www.demoblaze.com/index.html')
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, 'article')))
    next2 = driver.find_elements(By.CSS_SELECTOR, '[class="page-item"]')
    next2[1].click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'next2')))
    card_title = driver.find_elements(By.CLASS_NAME, 'card-block')
    h4 = card_title[-1].find_element(By.CSS_SELECTOR, 'h4.card-title')
    mac = h4.find_element(By.TAG_NAME, 'a')
    ActionChains(driver).key_down(Keys.CONTROL).click(mac).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn')))
    driver.find_element(By.CSS_SELECTOR, 'a.btn').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'cartur').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'success')))
    success = driver.find_element(By.CLASS_NAME, 'success')
    result = success.find_elements(By.TAG_NAME, 'td')
    assert result[1].text == 'MacBook Pro', 'Wrong product'
