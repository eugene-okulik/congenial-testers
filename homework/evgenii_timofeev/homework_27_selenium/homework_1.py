from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

TEXT = "monkey"

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.qa-practice.com/elements/input/simple")

search_line = driver.find_element(By.ID, "id_text_string")
search_line.send_keys(TEXT)
search_line.submit()

result_element = driver.find_element(By.ID, "result-text")
print(result_element.text)
