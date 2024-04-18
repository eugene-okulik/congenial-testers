from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


language = 'Python'


def test_displayed():
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_line = driver.find_element(By.ID, 'id_choose_language')
    select = Select(choose_line)
    select.select_by_visible_text(language)
    driver.find_element(By.ID, 'submit-id-submit').click()
    result = driver.find_element(By.ID, "result-text").text
    print(result)
    assert result == language, f'result text is not {language}'
