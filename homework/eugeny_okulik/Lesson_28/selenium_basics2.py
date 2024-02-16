from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
sleep(3)
# driver.maximize_window()
# driver.set_window_size(1920, 1080)


def func1():
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    bags_link = driver.find_element(By.LINK_TEXT, 'Bags')
    print(bags_link.text)
    fit_eq_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Fitness')
    fit_eq_link.click()
    page_title = driver.find_element(By.TAG_NAME, 'h1')
    assert page_title.text == 'Fitness Equipment', 'incorrect title'
    driver.back()
    big_blue_button = driver.find_element(By.CLASS_NAME, 'button')
    big_blue_button.click()
    # cart = driver.find_element(By.CSS_SELECTOR, '''a[data-bind="scope: 'minicart_content'"]''')
    # cart = driver.find_element(By.XPATH, '''//a[@data-bind="scope: 'minicart_content'"]''')
    cart = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a')
    cart.click()


driver.get('https://magento.softwaretestingboard.com/customer/account/login')
login = driver.find_element(By.ID, 'email')
login.send_keys('swiwiwwjsksksksk')
login.send_keys(Keys.CONTROL + 'a')
sleep(3)
len_value = login.get_attribute('value')
for _ in range(len(len_value)):
    login.send_keys(Keys.BACKSPACE)
    sleep(0.5)
assert login.get_attribute('autocomplete') == 'off'
label = driver.find_element(By.CSS_SELECTOR, '[for="email"]')
print(label.text)
print(label.get_attribute('innerText'))
button = driver.find_element(By.ID, 'send2')
print(button.value_of_css_property('background'))

sleep(2)
driver.quit()
