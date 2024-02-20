from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Попробовал явные и неявные ожидания, решил оставить в коде для себя, но неявные закоментил=)
driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
button_start = driver.find_element(By.CSS_SELECTOR, "#start>button")
button_start.click()
search_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'finish')))
# search_text = driver.find_element(By.ID, 'finish')
assert search_text.text == 'Hello World!'
