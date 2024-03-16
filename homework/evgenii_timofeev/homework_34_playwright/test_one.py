import json

from playwright.sync_api import Page, expect, Route


def test_one(page: Page):
    expected_text = "яблокофон 15 про"

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        new_iphone = "УГА БУГА"
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = expected_text
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route(
        "https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat",
        handle_route,
    )
    page.goto("https://www.apple.com/shop/buy-iphone")

    window_locator = page.locator(".rf-hcard-content-title").first
    window_locator.click()

    iphone_title_locator = page.locator("#rf-digitalmat-overlay-label").first
    expect(iphone_title_locator).to_have_text(expected_text)
