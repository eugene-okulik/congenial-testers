import pytest
import requests


@pytest.fixture(scope='session')
def start():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='function')
def post_id(start):
    payload = {
        "name": "SamSung MacBook Pro 16",
        "data": {
            "year": 2025,
            "price": 2849.99,
            "CPU model": "AMD Core i9",
            "Hard disk size": "10 TB"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    ).json()
    print(response)
    post = response['id']
    yield post
    requests.delete(f'https://api.restful-api.dev/objects/{post}')
