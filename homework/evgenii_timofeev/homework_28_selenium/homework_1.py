from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/automation-practice-form")

driver.find_element(By.ID, "firstName").send_keys("First Name")
driver.find_element(By.ID, "lastName").send_keys("Last Name")
driver.find_element(By.ID, "userEmail").send_keys("useremail@bred.com")
driver.find_element(By.CSS_SELECTOR, "[for=gender-radio-1]").click()
driver.find_element(By.ID, "userNumber").send_keys("8800555353")
driver.find_element(By.ID, "dateOfBirthInput").click()

month = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
select_month = Select(month)
select_month.select_by_value("11")


year = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
select_year = Select(year)
select_year.select_by_value("1998")

driver.find_element(
    By.CSS_SELECTOR,
    ".react-datepicker__day--017:not(.react-datepicker__day--outside-month)",
).click()

subjects_container = driver.find_element(
    By.CSS_SELECTOR,
    "[class='subjects-auto-complete__control css-yk16xz-control']",
)
subjects_container.click()
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("English")
subject.send_keys(Keys.ENTER)

driver.find_element(By.CSS_SELECTOR, "[for=hobbies-checkbox-1]").click()
driver.find_element(By.CSS_SELECTOR, "[for=hobbies-checkbox-2]").click()
driver.find_element(By.CSS_SELECTOR, "[for=hobbies-checkbox-3]").click()

adress = driver.find_element(By.ID, "currentAddress")
adress.click()
adress.send_keys("In the middle of nowhere")

state = driver.find_element(By.ID, "react-select-3-input")
driver.execute_script("arguments[0].click();", state)

state.send_keys("NCR")
state.send_keys(Keys.ENTER)

city = driver.find_element(By.ID, "react-select-4-input")
driver.execute_script("arguments[0].click();", city)

city.send_keys("Delhi")
city.send_keys(Keys.ENTER)

driver.find_element(By.ID, "submit").click()

text = driver.find_element(By.CLASS_NAME, "modal-body")


print(text.text)
