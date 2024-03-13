from playwright.sync_api import Page, expect, Route
import json


def test_iphone_15(page: Page):
    new_iphone = 'яблокофон 15 про'

    def edit_request(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_iphone
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat', edit_request)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone_15 = page.locator('//button[@data-autom="DigitalMat-1"]')
    iphone_15.click()
    new_title = page.locator('//h2[@data-autom="DigitalMat-overlay-header-0-0"]')
    expect(new_title, 'Заголовок попапа не изменен!').to_have_text(new_iphone)
