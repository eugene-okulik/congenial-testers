from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://www.qa-practice.com/elements/input/simple')
print(driver.current_url)
print(driver.title)
search_input = driver.find_element(By.NAME, 'text_string')
search_input.send_keys("HappyDay")
search_input.submit()
search_p = driver.find_element(By.ID, 'result-text')
print(search_p.text)
