import pytest
import requests
import allure


@allure.feature("API Testing")
@allure.story("Send a valid PUT request")
@allure.title("Редактирование объекта через PUT request")
@pytest.mark.parametrize('name', ['Huawei Ultra', 'Samsung pro14', 'Lenovo E47'])
def test_put_edit_object(create_object, name):
    with allure.step('Prepare test data'):
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
    with allure.step(f'Send PUT request to edit a post with data {payload}'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{create_object}',
            json=payload,
            headers=headers
        ).json()
    assert response['id'] == create_object, 'incorrect ID'
    assert response['name'] == name


@allure.feature("API Testing")
@allure.story("Send a valid PATCH request")
@allure.title("Редактирование имени через PATCH request")
@pytest.mark.medium
def test_patch_object(create_object):
    with allure.step('Prepare test data'):
        payload = {"name": "Apple MacBook Pro 16 m1(Updated Name)"}
        headers = {"content-type": "application/json"}
    with allure.step(f'Send PATCH request to patch a post with data {payload}'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{create_object}',
            json=payload,
            headers=headers
        ).json()
    assert response['id'] == create_object, 'incorrect ID'
    assert response['name'] == 'Apple MacBook Pro 16 m1(Updated Name)'


@allure.feature("API Testing")
@allure.story("Send a valid DELETE request")
@allure.title("Удаление объекта")
def test_delete_object(create_object):
    with allure.step(f'Send DELETE request to delete a post '):
        response = requests.delete(f'https://api.restful-api.dev/objects/{create_object}')
    assert response.status_code == 200


@allure.feature("API Testing")
@allure.story("Send a valid GET request")
@allure.title("Получение объекта через GET request")
@pytest.mark.medium
def test_get_object(create_object):
    with allure.step(f'Send GET request to get a post '):
        response = requests.get(f'https://api.restful-api.dev/objects/{create_object}').json()
    assert response['id'] == create_object, 'incorrect ID'


@allure.feature("API Testing")
@allure.story("Send a valid POST request")
@allure.title("Создание объекта через POST request")
def test_post_add_object():
    with allure.step('Prepare test data'):
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
    with allure.step(f'Send POST request to create a post with data {payload}'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=payload,
            headers=headers
        ).json()
    assert response['name'] == payload['name']
