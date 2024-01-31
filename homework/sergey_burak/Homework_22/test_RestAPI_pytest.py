import requests
import pytest

@pytest.fixture(scope='session')
def start():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='session')
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



def test_post(post_id):
    response = requests.request('GET', f'https://api.restful-api.dev/objects/{post_id}').json()
    print(response)
    assert response['id'] == post_id, 'Created incorrect object ID'
    assert response['name'] == "SamSung MacBook Pro 16", 'Incorrect name, or object not created'



def test_put(post_id):
    payload = {
        "name": "Sumsung 22",
        "data": {
            "year": 2028,
            "price": 12849.99,
            "CPU model": "AMD Core i19",
            "Hard disk size": "20 TB"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=payload,
        headers=headers
    ).json()
    print(response)
    assert response['name'] == payload['name'], 'Incorrect name, or object not created'
    assert response['data']['price'] == 12849.99, 'Price so mach!'


def test_patch(post_id):
    payload = {
        "name": "ZX Spectrum",
        "data": {
            "year": 1993,
            "CPU model": "Zilog Z80",
            "Hard disk size": "128 kB"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=payload,
        headers=headers
    ).json()
    print(response)
    assert response['name'] == payload['name'], 'Incorrect name, or object not patched'
    assert response['data']['CPU model'] == payload['data']['CPU model'], 'Incorrect computer'


def test_get_by_id(post_id):
    response = requests.request('GET', f'https://api.restful-api.dev/objects/{post_id}').json()
    print(response)
    assert response['id'] == post_id, 'incorrect ID'


def test_delete(post_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    print(response.status_code)
    assert requests.get(
        f'https://api.restful-api.dev/objects/{post_id}'
    ).status_code == 404, 'Not deleted!'
