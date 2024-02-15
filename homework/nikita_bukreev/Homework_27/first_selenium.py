from selenium import webdriver
from selenium.webdriver.common.by import By


some_text = 'kek'
driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/input/simple')
search_input = driver.find_element(By.NAME, 'text_string')
search_input.send_keys(some_text)
search_input.submit()
find_input_text = driver.find_element(By.ID, 'result-text')
assert find_input_text.text == some_text
print(f'Your input was: {find_input_text.text}')
