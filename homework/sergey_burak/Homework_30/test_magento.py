from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    my_driver.implicitly_wait(10)
    return my_driver


def test_magento(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'not-logged-in'),
            'Click “Write for us” link in the footer to submit a guest post'
        )
    )
    product = driver.find_element(By.CLASS_NAME, 'product-item-link')
    product_text = driver.find_element(By.CLASS_NAME, 'product-item-link').text
    add_to = driver.find_element(By.CSS_SELECTOR, '[title="Add to Compare"]')
    action = ActionChains(driver)
    action.move_to_element(product)
    action.move_to_element(add_to)
    action.click(add_to)
    action.perform()
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '[data-ui-id="message-success"]')))
    sidebar_additional = driver.find_element(By.CSS_SELECTOR, '.sidebar-additional')
    result = sidebar_additional.find_element(By.CSS_SELECTOR, "a.product-item-link")
    assert result.text == product_text, 'product did not add to Compare Products, or another product was selected'
