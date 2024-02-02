import requests
import pytest


@pytest.mark.parametrize('name', ['Huawei Ultra', 'Samsung pro14', 'Lenovo E47'])
def test_put_edit_object(create_object, name):
    payload = {
        "name": name,
        "data": {
            "year": 2022,
            "price": 2200.99,
            "CPU model": "m3",
            "Hard disk size": "1 TB",
            "color": "silver"
        },
    }
    headers = {"content-type": "application/json"}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{create_object}',
        json=payload,
        headers=headers
    ).json()
    assert response['id'] == create_object, 'incorrect ID'
    assert response['name'] == name


@pytest.mark.medium
def test_patch_object(create_object):
    payload = {"name": "Apple MacBook Pro 16 m1(Updated Name)"}
    headers = {"content-type": "application/json"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{create_object}',
        json=payload,
        headers=headers
    ).json()
    assert response['id'] == create_object, 'incorrect ID'
    assert response['name'] == 'Apple MacBook Pro 16 m1(Updated Name)'


def test_delete_object(create_object):
    response = requests.delete(f'https://api.restful-api.dev/objects/{create_object}')
    assert response.status_code == 200


@pytest.mark.medium
def test_get_object(create_object):
    response = requests.get(f'https://api.restful-api.dev/objects/{create_object}').json()
    assert response['id'] == create_object, 'incorrect ID'


def test_post_add_object():
    payload = {
        "name": "Apple iPad 2023",
        "data": {
            "year": 2023,
            "price": 1600.99,
            "CPU model": "m2",
            "Hard disk size": "1 TB"
        },
    }
    headers = {"content-type": "application/json"}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    ).json()
    assert response['name'] == payload['name']
