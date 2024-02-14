from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


options = Options()
# options.add_argument('start-maximized')
options.add_argument('--window-size=1500,1000')
driver = webdriver.Chrome(options=options)
sleep(3)
# driver.maximize_window()
# driver.set_window_size(1920, 1080)
driver.get('https://www.google.com')
print(driver.current_url)
print(driver.title)
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('dog')
search_input.submit()
# search_button = driver.find_element(By.NAME, 'btnK')
# search_button.click()
assert 'dog' in driver.title
