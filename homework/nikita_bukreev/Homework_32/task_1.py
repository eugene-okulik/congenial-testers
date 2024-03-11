from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    name_input = page.get_by_role('textbox', name='username')
    name_input.fill('Nikita')
    password_input = page.get_by_role('textbox', name='password')
    password_input.fill('some_password')
    page.get_by_role('button', name='Login').click()
    info_message = page.locator('.flash.error')  # не смог найти по роли (пробовал 10+ вариантов)
    expect(info_message).to_be_visible()
