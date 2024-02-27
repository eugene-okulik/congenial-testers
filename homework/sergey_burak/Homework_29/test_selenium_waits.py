from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()


def test_select():
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    Select(driver.find_element(By.ID, 'id_choose_language')).select_by_visible_text('Python')
    driver.find_element(By.ID, 'submit-id-submit').click()
    assert driver.find_element(By.ID, 'result-text').text == 'Python', 'You selected another language'


def test_waits():
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.CSS_SELECTOR, '#start > button:nth-child(1)').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'finish')))
    assert driver.find_element(By.ID, 'finish').is_displayed(), 'Result is not displayed!'
