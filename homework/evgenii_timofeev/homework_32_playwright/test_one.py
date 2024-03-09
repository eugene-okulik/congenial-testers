from playwright.sync_api import Page, expect


def test_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    log_out_button = page.get_by_role("link", name="Logout")
    expect(log_out_button).to_be_visible()
