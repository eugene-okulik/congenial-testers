import random
import pytest
import allure


@allure.feature('Create account page')
@allure.story('Shown required fields')
def test_required_fields(create_account_page):
    create_account_page.open()
    create_account_page.click_submit_button()
    create_account_page.check_count_required_fields()


@allure.feature('Create account page')
@allure.story('Different password strength')
@pytest.mark.parametrize('password, result', [
    ('', 'No Password'),
    ('qwerty', 'Weak'),
    ('KekLol123', 'Strong'),
    ('KekLol123kek', 'Very Strong')
])
def test_password_strength(create_account_page, password, result):
    create_account_page.open()
    create_account_page.input_password(password)
    create_account_page.check_password_strength(result)


@allure.feature('Create account page')
@allure.story('Success creating account')
def test_create_account(create_account_page):
    user = {
        'first_name': 'Nikita',
        'last_name': 'Bukreev',
        'email': f'kek+{random.randint(99, 9999)}@lol.com',
        'password': 'KekLol123kek'
    }
    create_account_page.open()
    create_account_page.fill_all_fields(
        user['first_name'],
        user['last_name'],
        user['email'],
        user['password'],
        user['password']
    )
    create_account_page.click_submit_button()
    create_account_page.check_alert_message()
