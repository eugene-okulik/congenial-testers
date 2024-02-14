import pytest
import requests


@pytest.mark.critical
def test_post(start):
    # response = requests.request('GET', f'https://api.restful-api.dev/objects/{post_id}').json()
    # print(response)
    # assert response['id'] == post_id, 'Created incorrect object ID'
    # assert response['name'] == "SamSung MacBook Pro 16", 'Incorrect name, or object not created'
    payload = {
        "name": "SamSung Pro 16",
        "data": {
            "year": 2025,
            "price": 7449.99,
            "CPU model": "AMD Core i11",
            "Hard disk size": "80 TB"
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
    assert response['name'] == 'SamSung Pro 16', 'Incorrect name, or object not created'


@pytest.mark.parametrize('name', ['Apple 21', 'Sumsung 22', 'Sumsung 23'])
def test_put(post_id, name):
    payload = {
        "name": name,
        "data": {
            "year": 2028,
            "price": 99999.99,
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
    assert response['name'] == name, 'Incorrect name, or object not created'
    assert response['data']['price'] == payload['data']['price'], 'Price so mach!'
    assert response['data']['year'] == payload['data']['year'], 'Incorrect year!'


@pytest.mark.medium
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
