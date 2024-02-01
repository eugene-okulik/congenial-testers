import pytest
import requests


@pytest.fixture(scope='session')
def starting():
    print('\nStart testing\n')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='function')
def add_object(starting):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    new_object = response['id']
    yield new_object
    requests.delete(f'https://api.restful-api.dev/objects/{new_object}')
