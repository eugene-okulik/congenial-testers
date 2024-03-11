from playwright.sync_api import Page, expect, BrowserContext


def test_two(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button_click = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        button_click.click()
    new_page = new_page_event.value
    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(button_click).to_be_enabled()
