from playwright.sync_api import Page, expect


def test_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('tomsmith')
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')
    page.get_by_role('button').click()
    expect(page).to_have_url('https://the-internet.herokuapp.com/secure')


def test_demoqa_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Sergey')
    page.get_by_placeholder('Last Name').fill('Burak')
    page.get_by_placeholder('name@example.com').fill('art-print@mail.com')
    page.locator('label[for="gender-radio-1"]').click()
    page.locator('#userNumber').fill('1292929292')
    page.locator('#dateOfBirth').click()
    page.locator('#dateOfBirthInput').press('Control+a')
    page.locator('#dateOfBirthInput').fill('28Sep1978')
    page.keyboard.press('Enter')
    page.keyboard.press('PageDown')
    page.locator('#subjectsInput').press_sequentially('M')
    page.locator('#react-select-2-option-0').click()
    page.locator('#subjectsInput').press_sequentially('p')
    page.locator('#react-select-2-option-0').click()
    page.locator('//*[@for="hobbies-checkbox-1"]').check()
    page.locator('//*[@for="hobbies-checkbox-3"]').click()
    page.locator('#currentAddress').fill('14-5 Kremko str.')
    page.locator('#state').click()
    page.locator('#react-select-3-option-1').click()
    page.locator('#state').click()
    page.locator('#react-select-3-option-1').click()
    page.locator('#city').click()
    page.locator('#react-select-4-option-0').click()
    page.locator('#submit').click()
    expect(page.locator('.modal-dialog')).to_be_visible()
