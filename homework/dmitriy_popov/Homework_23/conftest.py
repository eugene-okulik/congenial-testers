import pytest
import requests


@pytest.fixture(scope='session', autouse=True)
def start():
    print('Start testing')
    yield
    print("\nTesting completed")


@pytest.fixture(scope='function')
def create_object():
    payload = {
        "name": "Apple MacBook Pro 16 m3",
        "data": {
            "year": 2023,
            "price": 2500.99,
            "CPU model": "m3",
            "Hard disk size": "1 TB"
        },
    }
    headers = {"content-type": "application/json"}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    ).json()
    post_id = response['id']
    yield post_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
