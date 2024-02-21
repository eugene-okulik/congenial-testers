from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


language = 'Python'

driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/select/single_select')
search_select = driver.find_element(By.ID, 'id_choose_language')
search_select.click()
select = Select(search_select)
select.select_by_visible_text(language)
button_submit = driver.find_element(By.ID, 'submit-id-submit')
button_submit.click()
result_text = driver.find_element(By.ID, 'result-text')
assert result_text.text == language, f'result text is not {language}'
