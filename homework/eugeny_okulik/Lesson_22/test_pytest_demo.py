import requests
import pytest


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


def test_get_one(start):
    post_id = 43
    he, ho = start
    print(he, ho)
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    print(response['id'])
    assert response['id'] == post_id, 'incorrect ID'


def test_post_a_post(start, dots):
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
    assert response['title'] == 'My tile'


def test_put_a_post(post_id):
    payload = {
        "title": "My tileUPD",
        "body": "my bodyUPD",
        "userId": 2
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=payload,
        headers=headers
    ).json()
    assert response['title'] == 'My tileUPD'


def test_one(connect):
    assert 1 == 1
