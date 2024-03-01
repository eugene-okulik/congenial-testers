from playwright.sync_api import Page, expect
from time import sleep
import re


def test_first(page: Page):
    sleep(3)
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^cat'))
    # assert page.title().startswith('cat')


def test_by_role(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/')
    sleep(1)
    page.get_by_role('menuitem', name="What's New").click()
    sleep(2)
    page.get_by_role('link', name='Search Terms').click()
    sleep(3)


def test_by_text(page: Page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single UI Elements').click()
    sleep(3)


def test_by_label(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_label('Text string').fill('skdjfhskdjfh')
    sleep(3)


def test_by_placeholder(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('skdjfhsk')
    sleep(3)


def test_alt_text(page):
    page.goto('https://www.epam.com/')
    page.get_by_alt_text('The Next Evolution of Software Engineering').click()
    sleep(3)


def test_by_title(page: Page):
    sleep(3)
    page.goto('https://google.com')
    page.get_by_title('Шукаць').fill('dog')
    sleep(3)


def test_by_test_id(page):
    page.goto('https://www.airbnb.com/')
    sleep(2)
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
    sleep(3)


def test_by_css_selector(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('.showcart').click()
    sleep(3)


def test_by_xpath(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('//*[@class="action showcart"]').click()
    sleep(3)


def test_input(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    sleep(1)
    field = page.get_by_label('Text string')
    field.press_sequentially('qwerty', delay=500)
    sleep(1)
    field.press('Control+a')
    sleep(1)
    field.press('Backspace')
    sleep(3)


def test_create_login(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/customer/account/create/')
    sleep(3)
    page.locator('#password').press_sequentially('qwerty')
    sleep(3)
