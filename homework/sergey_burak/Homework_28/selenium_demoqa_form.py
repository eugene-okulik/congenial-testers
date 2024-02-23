from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/automation-practice-form')
driver.find_element(By.CSS_SELECTOR, '#firstName').send_keys('Sergey')
driver.find_element(By.CSS_SELECTOR, '#lastName').send_keys('Burak')

driver.find_element(By.CSS_SELECTOR, '#userEmail').send_keys('art-print@tut.by')
driver.find_element(By.CSS_SELECTOR, 'div.custom-radio:nth-child(1) > label:nth-child(2)').click()
driver.find_element(By.CSS_SELECTOR, '#userNumber').send_keys('1292929292')

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput').click()
driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select').send_keys('1978')
driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select').send_keys('Sep')
driver.find_element(By.CSS_SELECTOR, 'div.react-datepicker__day--028:nth-child(5)').click()

driver.find_element(By.CSS_SELECTOR, '#subjectsInput').send_keys('M')
driver.find_element(By.CSS_SELECTOR, '#react-select-2-option-0').click()
driver.find_element(By.CSS_SELECTOR, '#subjectsInput').send_keys('p')
driver.find_element(By.CSS_SELECTOR, '#react-select-2-option-0').click()

driver.find_element(By.CSS_SELECTOR, 'div.custom-checkbox:nth-child(1) > label:nth-child(2)').click()
driver.find_element(By.CSS_SELECTOR, 'div.custom-checkbox:nth-child(3) > label:nth-child(2)').click()

driver.find_element(By.CSS_SELECTOR, '#currentAddress').send_keys('14-5 Kremko str.')

driver.find_element(By.CSS_SELECTOR, '#state').click()
driver.find_element(By.CSS_SELECTOR, '#react-select-3-option-1').click()

driver.find_element(By.CSS_SELECTOR, '#city').click()
driver.find_element(By.CSS_SELECTOR, '#react-select-4-option-0').click()

driver.find_element(By.CSS_SELECTOR, '#submit').click()

print(driver.find_element(By.CLASS_NAME, 'modal-body').text)
