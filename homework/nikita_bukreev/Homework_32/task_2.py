from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    data = {
        'First Name': 'Nikita',
        'Last Name': 'Bukreev',
        'Student Email': 'kek@lol.com',
        'Mobile': '8800555353',
        'Date of Birth': '20 Mar 1993',
        'Subjects': 'Maths',
        'Hobbies': 'Sports',
        'Address': 'Berlin',
    }
    # мб в РФ сайт плохо работает, пришлось вводить большой таймаут для загрузки, иначе тест падал
    page.goto('https://demoqa.com/automation-practice-form', timeout=50000)
    first_name = page.locator('#firstName')
    first_name.fill(data['First Name'])
    last_name = page.locator('#lastName')
    last_name.fill(data['Last Name'])
    email = page.locator('#userEmail')
    email.fill(data['Student Email'])
    checkbox_male = page.locator("//label[@for='gender-radio-1']")
    checkbox_male.check()
    mobile_number = page.locator('#userNumber')
    mobile_number.fill(data['Mobile'])
    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.fill(data['Date of Birth'])
    subject = page.locator('#subjectsInput')
    subject.fill(data['Subjects'])
    subject.press('Enter')
    checkbox_sport = page.locator("//label[@for='hobbies-checkbox-1']")
    checkbox_sport.click()
    current_address = page.locator('#currentAddress')
    current_address.fill(data['Address'])
    select_state = page.locator('#state')
    select_state.click()
    select_first_state = page.locator('#react-select-3-option-0')
    select_first_state.click()
    select_city = page.locator('#city')
    select_city.click()
    select_first_city = page.locator('#react-select-4-option-0')
    select_first_city.click()
    button_submit = page.locator('#submit')
    button_submit.click()
    modal_result = page.locator('tbody')
    expect(modal_result).to_contain_text(data['First Name'])
