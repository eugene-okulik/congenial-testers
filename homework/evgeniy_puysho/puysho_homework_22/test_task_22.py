import requests
import pytest


@pytest.fixture(scope='session')
def starting():
    print('\nStart testing\n')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='function')
def add_object(starting):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
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
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    payload = {
        "name": "UPD: Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{add_object}',
        json=payload,
        headers=headers
    ).json()
    assert response['name'] == 'UPD: Apple MacBook Pro 16', 'Error: check request body'
    assert (requests.get(f'https://api.restful-api.dev/objects/{add_object}')
            .status_code == 200), 'Error: object does not exist'


def test_path_object(add_object):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    payload = {"name": "PATHCED: UPDATED"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{add_object}',
        json=payload,
        headers=headers).json()
    assert response['name'] == 'PATHCED: UPDATED', 'Error: check request body'
    assert (requests.get(f'https://api.restful-api.dev/objects/{add_object}')
            .status_code == 200), 'Error: object does not exist'


def test_get_object(add_object):
    response = requests.get(f'https://api.restful-api.dev/objects/{add_object}').json()
    assert response['id'] == add_object, 'Error: id does not match'
    assert (requests.get(f'https://api.restful-api.dev/objects/{add_object}')
            .status_code == 200), 'Error: object does not exist'


def test_delete_object(add_object):
    requests.delete(f'https://api.restful-api.dev/objects/{add_object}').json()
    assert (requests.get(f'https://api.restful-api.dev/objects/{add_object}')
            .status_code == 404), 'Error: object does not exist'


def test_add_object(starting):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
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
    full_url = f'https://api.restful-api.dev/objects/{new_object}'
    assert requests.get(full_url).status_code == 200, 'Error: object has not been added'
    assert response['id'] == new_object
