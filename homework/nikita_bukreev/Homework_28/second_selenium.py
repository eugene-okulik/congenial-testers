from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


data = {
    'first_name': 'Nikita',
    'last_name': 'Bukreev',
    'email': 'kek@lol.com',
    'mobile': '888005553535',
    'date_of_birth': '20 Mar 1993',
    'subject': 'maths',
    'current_address': 'Beaker Street'
}
driver = webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')
search_fname = driver.find_element(By.ID, 'firstName')
search_fname.send_keys(data['first_name'])
search_lname = driver.find_element(By.ID, 'lastName')
search_lname.send_keys(data['last_name'])
search_email = driver.find_element(By.ID, 'userEmail')
search_email.send_keys(data['email'])
search_gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
search_gender.click()
search_mobile = driver.find_element(By.ID, 'userNumber')
search_mobile.send_keys(data['mobile'])
search_date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
# Долго бился с выделением всей строки, мак не воспринимал команду "Keys.CONTROL + 'a'", но хорошо воспринимал
# команду "Keys.COMMAND + 'a'", но она не универсальная и на винде не работала бы (наверно)
# поэтому вспомнил про шифт + хом, надеюсь, что и на виндне, и на линуксе будет ралотать данное сочетание=)
search_date_of_birth.send_keys(Keys.SHIFT + Keys.HOME)
search_date_of_birth.send_keys(data['date_of_birth'])
search_date_of_birth.send_keys(Keys.ESCAPE)
search_subject = driver.find_element(By.ID, 'subjectsInput')
search_subject.send_keys(data['subject'])
search_subject.send_keys(Keys.ENTER)
search_hobbies = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
search_hobbies.click()
search_address = driver.find_element(By.ID, 'currentAddress')
search_address.send_keys(data['current_address'])
scroll_down = driver.find_element(By.TAG_NAME, 'body')
scroll_down.send_keys(Keys.END)
wait_state = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.ID, 'state')))
find_state = driver.find_element(By.ID, 'state')
find_state.click()
select_state = driver.find_element(By.ID, 'react-select-3-option-3')
select_state.click()
find_city = driver.find_element(By.ID, 'city')
find_city.click()
select_city = driver.find_element(By.ID, 'react-select-4-option-1')
select_city.click()
button_submit = driver.find_element(By.ID, 'submit')
button_submit.click()
read_table = driver.find_element(By.TAG_NAME, 'tbody')
print(read_table.text)
driver.quit()
