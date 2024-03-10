from playwright.sync_api import Page, expect, BrowserContext


def test_one(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", lambda dialog: dialog.accept())

    page.locator(".a-button").click()
    final_element = page.locator("#result")

    expect(final_element, f"Text is wrong").to_contain_text("Ok")


def test_two(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    click_button = page.locator("#new-page-button")

    with context.expect_page() as new_page_event:
        click_button.click()

    second_page = new_page_event.value
    result_text = second_page.locator("#result-text")

    expect(result_text, f"Text is wrong").to_have_text("I am a new page in a new tab")
    expect(click_button, f"Text is wrong").to_be_enabled()


def test_three(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")

    button = page.locator("#colorChange")
    page.wait_for_selector("#colorChange.text-danger")
    button.click()

    expect(button).to_have_class("mt-4 text-danger btn btn-primary")
