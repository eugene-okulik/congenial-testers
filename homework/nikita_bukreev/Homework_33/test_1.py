from playwright.sync_api import Page, expect, Dialog


def test_one(page: Page):
    def accept_dialog(alert: Dialog):
        alert.accept()
    page.on('dialog', accept_dialog)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    button_click = page.locator('.a-button')
    button_click.click()
    result_text = page.locator('#result-text')
    expect(result_text, 'There is no "OK" in result').to_have_text('Ok')
