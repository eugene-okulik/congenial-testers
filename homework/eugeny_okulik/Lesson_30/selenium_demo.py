from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    sleep(2)
    return my_driver


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    sleep(2)
    # cookies = driver.get_cookies()
    driver.delete_cookie('user')
    driver.add_cookie(
        {
            'domain': 'www.demoblaze.com',
            'httpOnly': False,
            'name': 'user',
            'path': '/',
            'sameSite': 'Lax',
            'secure': False,
            'value': 'my_value'
        }
    )
    # user_cookie = driver.get_cookie('user')
    print(driver.get_cookies())


def test_men(driver):
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    men = driver.find_elements(By.CSS_SELECTOR, '[class="product-item-info"]')
    price_0 = men[0].find_element(By.CLASS_NAME, 'price')
    print(price_0.text)


def test_tabs(driver):
    driver.maximize_window()
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    sleep(1.5)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()
    sleep(2)
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'new-page-link').click()


def test_stale_element(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    print(checkbox.id)
    checkbox.click()
    driver.find_element(By.ID, 'submit-id-submit').click()
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    print(checkbox.id)
    checkbox.click()


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    burger = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
    burger.click()
    driver.switch_to.default_content()
    tab = driver.find_element(By.LINK_TEXT, 'Iframe')
    tab.click()
    sleep(3)


def test_drop_menu(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'not-logged-in'),
            'Click “Write for us” link in the footer to submit a guest post'
        )
    )
    men = driver.find_element(By.ID, 'ui-id-5')
    tops = driver.find_element(By.ID, 'ui-id-17')
    jackets = driver.find_element(By.ID, 'ui-id-19')
    # ActionChains(driver).move_to_element(men).move_to_element(tops).click(jackets).perform()
    action = ActionChains(driver)
    action.move_to_element(men)
    action.move_to_element(tops)
    action.click(jackets)
    action.perform()
    sleep(3)


def test_dnd(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = driver.find_element(By.ID, 'rect-draggable')
    drag_here = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).drag_and_drop(drag_me, drag_here).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(drag_me)
    actions.move_to_element(drag_here)
    actions.release()
    actions.perform()
    sleep(3)


def test_open_in_new_tab(driver):
    driver.get('https://www.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    # ActionChains(driver).context_click(link).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(3)


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert = Alert(driver)
    alert.accept()
    sleep(3)


def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    upload.send_keys('/home/eugene/Downloads/hearts.jpg')
    sleep(3)
