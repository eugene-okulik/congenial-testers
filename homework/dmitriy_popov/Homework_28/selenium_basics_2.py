from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://demoqa.com/automation-practice-form')

driver.find_element(By.ID, 'firstName').send_keys('Dmitriy')
driver.find_element(By.ID, 'lastName').send_keys('Popov')
driver.find_element(By.ID, 'userEmail').send_keys('diamosha@gmail.com')
driver.find_element(By.CSS_SELECTOR, "[for=gender-radio-1]").click()
driver.find_element(By.ID, 'userNumber').send_keys('7912777884')

date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth.clear()
date_of_birth.send_keys('01.01.1991')
date_of_birth.send_keys(Keys.ENTER)

subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("English")
subject.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label').click()
driver.find_element(By.ID, 'currentAddress').send_keys('ul. Ololoshkina')

driver.find_element(By.ID, 'state').click()
driver.find_element(By.ID, 'react-select-3-option-2').click()

driver.find_element(By.ID, 'city').click()
driver.find_element(By.ID, 'react-select-4-option-1').click()

driver.find_element(By.ID, 'submit').click()
print(driver.find_element(By.CLASS_NAME, "modal-body").text)
