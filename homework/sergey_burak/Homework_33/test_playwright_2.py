from playwright.sync_api import Page, expect, BrowserContext, Dialog
import re

def test_qapractice_confirm(page: Page):
    def ok_alert(alert: Dialog):
        alert.accept()
    page.on('dialog', ok_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    expect(page.locator('#result')).to_be_visible()
    expect(page.locator('#result-text')).to_have_text('Ok')


def test_qapractice_button(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button_click = page.locator('.a-button')
    with context.expect_page() as new_page_event:
        button_click.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(button_click).to_be_enabled()


def test_demoqa_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    red_button = page.locator('#colorChange')
    expect(red_button).to_have_class(re.compile('.text-danger'))
    red_button.click()
    page.close()
