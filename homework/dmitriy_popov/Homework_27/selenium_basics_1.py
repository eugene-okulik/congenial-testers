from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.qa-practice.com/elements/input/simple')

search_input = driver.find_element(By.NAME, 'text_string')
search_input.send_keys('d1amosha')
search_input.submit()

search_output = driver.find_element(By.NAME, 'result')
print(search_output.text)
