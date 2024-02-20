from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
sleep(3)


def test_displayed():
    driver.get('https://magento.softwaretestingboard.com/hero-hoodie.html#')
    tanks = driver.find_element(By.CSS_SELECTOR, '#ui-id-22')

    print(tanks.is_displayed())


def test_select():
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    select_input = driver.find_element(By.ID, 'id_select_state')
    driver.find_element(By.ID, 'submit-id-submit').click()
    # print(select_input.tag_name)
    select = Select(select_input)
    select.select_by_visible_text('Enabled')
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    assert submit_button.is_enabled(), 'button is not enabled'


def test_waits():
    driver.get('https://demoqa.com/dynamic-properties')
    after = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    # after = driver.find_element(By.ID, 'visibleAfter')
    assert after.is_displayed()


def test_waits2():
    driver.get('https://demoqa.com/dynamic-properties')
    enable_after = driver.find_element(By.ID, 'enableAfter')
    print(enable_after.is_enabled())
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
    print(enable_after.is_enabled())


def test_men():
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    men = driver.find_elements(By.CSS_SELECTOR, '[class="product-item-info"]')
    man = random.choice(men)
    print(men[0].text)
    print(men[-1].text)
    men[6].click()
    man.click()
    sleep(2)
