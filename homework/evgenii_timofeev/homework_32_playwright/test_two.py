from playwright.sync_api import Page


def test_by_role(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator("#firstName").fill("Name")
    page.locator("#lastName").fill("Last")
    page.locator("#userEmail").fill("useremail@bred.com")
    page.locator('label[for="gender-radio-1"]').click()
    page.locator("#userNumber").fill("8800555353")
    page.locator("#dateOfBirthInput").click()
    page.locator("select.react-datepicker__month-select").select_option(value="11")
    page.locator("select.react-datepicker__year-select").select_option(value="1998")
    page.locator(".react-datepicker__day.react-datepicker__day--017").click()

    page.locator("#subjectsInput").fill("English")
    page.locator("#subjectsInput").press("Enter")

    page.locator("label[for=hobbies-checkbox-1]").click()
    page.locator("label[for=hobbies-checkbox-2]").click()
    page.locator("label[for=hobbies-checkbox-3]").click()

    page.locator("#react-select-3-input").fill("NCR")
    page.locator("#react-select-3-input").press("Enter")

    page.locator("#submit").click()
    print(page.locator(".modal-body").text_content())
