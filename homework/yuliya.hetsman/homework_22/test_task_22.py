import requests
import pytest


@pytest.fixture(scope='session')
def start():
    print('Start testing')
    yield
    print('\n Testing completed')


@pytest.fixture(scope='function')
def add_object(start):
    headers = {"content-type": "application/json"}
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers).json()
    new_object = response['id']
    yield new_object
    requests.delete(f'https://api.restful-api.dev/objects/{new_object}')


def test_update_object(add_object):
    headers = {"content-type": "application/json"}
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{add_object}',
        json=payload,
        headers=headers
    ).json()
    assert response['id'] == add_object


def test_partially_object(add_object):
    headers = {"content-type": "application/json"}
    payload = {"name": "Apple MacBook Pro 16 (Updated Name)"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{add_object}',
        json=payload,
        headers=headers
    ).json()
    assert response['id'] == add_object


def test_delete_object(add_object):
    response = requests.delete(f'https://api.restful-api.dev/objects/{add_object}')
    assert response.status_code == 200


def test_get_object(add_object):
    response = requests.get(f'https://api.restful-api.dev/objects/{add_object}')
    print(f'{response.json()}')


def test_add_object(start):
    headers = {"content-type": "application/json"}
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers).json()
    assert response['name'] == payload['name']
