# Для тестирования возьмем небольшое тестовое API: https://restful-api.dev
# Нужно протестировать все перечисленные в спецификации функции, а именно:
#
#     Создание объекта
#     Изменение объекта с помощью метода PUT
#     Изменение объекта с помощью метода PATCH
#     Удаление объекта
#
# Выполняйте всё задание так же, как я делал на занятии, - каждый запрос в отдельной функции.
# Каждая функция должна заканчиваться проверкой того, что запрос отработал правильно.

import requests


def get_by_id(new_object_id):
    response = requests.request('GET', f'https://api.restful-api.dev/objects/{new_object_id}').json()
    print(response)
    assert response['id'] == new_object_id, 'incorrect ID'


def post():
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
    new_object_id = response.pop('id')
    assert response['name'] == 'SamSung MacBook Pro 16', 'Incorrect name, or object not created'
    return new_object_id


def patch(new_object_id):
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
        f'https://api.restful-api.dev/objects/{new_object_id}',
        json=payload,
        headers=headers
    ).json()
    print(response)
    assert response['data']['CPU model'] == 'Zilog Z80', 'Incorrect computer'


def put(new_object_id):
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
        f'https://api.restful-api.dev/objects/{new_object_id}',
        json=payload,
        headers=headers
    ).json()
    print(response)
    assert response['data']['price'] == 12849.99, 'Price so mach!'


def delete(new_object_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    print(response.status_code)
    assert requests.get(
        f'https://api.restful-api.dev/objects/{new_object_id}'
    ).status_code == 404, 'Not deleted!'


new_id = post()
put(new_id)
patch(new_id)
get_by_id(new_id)
delete(new_id)
