from playwright.sync_api import Page, expect, Route
from time import sleep
import re
import json


def test_apple_to_yabloko(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('/api/digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone = page.locator('.rf-hcard-content-title').first
    iphone.click()
    expect(page.locator('#rf-digitalmat-overlay-label').first).to_have_text('яблокофон 15 про')
    sleep(3)
