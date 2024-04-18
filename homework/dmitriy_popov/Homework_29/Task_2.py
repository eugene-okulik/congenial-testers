from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()


def test_wait():
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.CSS_SELECTOR, '#start > button').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
        (By.ID, 'finish'), 'Hello World!')
    )
    final_text = driver.find_element(By.ID, 'finish').text
    assert final_text == 'Hello World!', 'Text is not "Hello World"'
