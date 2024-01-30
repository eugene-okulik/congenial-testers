import allure
import requests
import pytest
import random


@pytest.fixture(scope='session')
def connect():
    print('Connecting....')
    connection = 'connected'
    yield connection
    # connection.close()
    print('disconnecting....')


@pytest.fixture(scope='function')
def start(connect):
    print('Start\n')
    yield 'Hey-hey-hey!!!!!\n', 'h0-H0-H0'
    print('finish\n')


@pytest.fixture()
def dots():
    print('.........')


@pytest.fixture()
def post_id():
    payload = {
        "title": "My tile",
        "body": "my body",
        "userId": 1
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=payload,
        headers=headers
    ).json()
    post = response['id']
    # post = 100
    yield post
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post}')


@allure.feature('Get one post')
@allure.story('Existing post')
@allure.title('Получение одного поста по Id')
def test_get_one(start):
    with allure.step('Prepare test data'):
        post_id = 43
    with allure.step('Chat with user'):
        he, ho = start
        print(he, ho)
    with allure.step('Send request'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    with allure.step('Check that response id is the same as requested'):
        print(response['id'])
        assert response['id'] == post_id, 'incorrect ID'


@allure.feature('Create a post')
@allure.story('Positive')
def test_post_a_post(start, dots):
    with allure.step('Prepare test data'):
        payload = {
            "title": "My tile",
            "body": "my body",
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
    with allure.step(f'Send POST request to create a post with data {payload}'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        ).json()
    with allure.step('Check that title is the same as sent'):
        assert response['title'] == 'My tile'


@allure.feature('Create a post')
@allure.story('Positive')
def test_post_with_long_text(start, dots):
    with allure.step('Prepare test data'):
        payload = {
            "title": "My tile kadshkjadshf asdlkjahskldjfh asdlkjfhalksdjfh asdlkfjhaskldjfh",
            "body": "my body alksjdhflkasj asdlkjahlksdjfh asldkjfhakljdsf asdlkfjha kasdkfjhsdf askdjfhskjdfh",
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
    with allure.step(f'Send POST request to create a post with data {payload}'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        ).json()
    with allure.step('Check that title is the same as sent'):
        assert response['title'] == 'My tile kadshkjadshf asdlkjahskldjfh asdlkjfhalksdjfh asdlkfjhaskldjfh'


@allure.feature('Create a post')
@allure.story('Negative')
def test_post_with_array_in_title(start, dots):
    with allure.step('Prepare test data'):
        payload = {
            "title": ['sdf'],
            "body": "my body",
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
    with allure.step(f'Send POST request to create a post with data {payload}'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        ).json()
    with allure.step('Check that title is the same as sent'):
        assert response['title'] == ['sdf']


@allure.feature('Create a post')
@allure.story('Positive')
def test_post_with_obj_in_body(start, dots):
    with allure.step('Prepare test data'):
        payload = {
            "title": "My tile",
            "body": {},
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
    with allure.step(f'Send POST request to create a post with data {payload}'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        ).json()
    with allure.step('Check that title is the same as sent'):
        assert response['title'] == 'My tile'


@allure.feature('Updating a post')
@allure.story('PUT')
def test_put_a_post(post_id):
    with allure.step('Prepare test data'):
        payload = {
            "title": "My tileUPD",
            "body": "my bodyUPD",
            "userId": 2
        }
        headers = {
            'Content-type': 'application/json'
        }
    with allure.step(f'Send PUT request to update the post {post_id} with data {payload}'):
        response = requests.put(
            f'https://jsonplaceholder.typicode.com/posts/{post_id}',
            json=payload,
            headers=headers
        ).json()
    with allure.step('Check that title is the same as sent'):
        assert response['title'] == 'My tileUPD'


def test_one(connect):
    assert 1 == random.randrange(0, 3)
