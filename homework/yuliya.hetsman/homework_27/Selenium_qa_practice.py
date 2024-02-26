from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://www.qa-practice.com/elements/input/simple')
search_input = driver.find_element(By.NAME, 'text_string')
search_input.send_keys('cat')
search_input.submit()
result_input = driver.find_element(By.ID, 'result')
print(result_input.text)
