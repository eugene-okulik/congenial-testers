import requests

headers_req = {
    'Content-type': 'application/json; charset=UTF-8'
}
BASE_URL = 'https://api.restful-api.dev/objects'
ADD_PAYLOAD = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}
UPD_PUT_PAYLOAD = {
    "name": "UPD: Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "UPD: Intel Core i9",
        "Hard disk size": "228 TB"
    }
}
UPD_PATCH_PAYLOAD = {"name": "Updated with patch"}


def add_object(payload, url):
    headers = headers_req
    response = requests.post(BASE_URL, json=payload, headers=headers).json()
    print(f'Object created:\n {response}')
    new_object = response['id']
    assert requests.get(f'{url}/{new_object}').status_code == 200, 'Error: object has not been added'
    return response['id']


def update_object(obj_id, payload, url):
    headers = headers_req
    response = requests.put(f'{url}/{obj_id}', json=payload, headers=headers).json()
    print(f'Object updated:\n {response}')
    assert response['name'] == 'UPD: Apple MacBook Pro 16', 'Error: check request body'
    assert requests.get(f'{url}/{obj_id}').status_code == 200, 'Error: object does not exist'


def update_object_partly(obj_id, payload, url):
    headers = headers_req
    response = requests.patch(
        f'{url}/{obj_id}', json=payload, headers=headers).json()
    print(f'Object updated partly:\n {response}')
    assert response['name'] == 'Updated with patch', 'Error: check request body'
    assert requests.get(f'{url}/{obj_id}').status_code == 200, 'Error: object does not exist'


def delete_object(obj_id, url):
    response = requests.delete(f'{url}/{obj_id}')
    print(f'Status code: {response.status_code}')
    assert requests.get(f'{url}/{obj_id}').status_code == 404, 'Object has not been deleted'


added_object = add_object(ADD_PAYLOAD, BASE_URL)
update_object(added_object, UPD_PUT_PAYLOAD, BASE_URL)
update_object_partly(added_object, UPD_PATCH_PAYLOAD, BASE_URL)
delete_object(added_object, BASE_URL)
