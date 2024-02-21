import requests


def add_object(payload):
    headers = {"content-type": "application/json"}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    ).json()
    post_id = response['id']
    print(response)
    assert response['name'] == payload['name']
    return post_id


def update_object(payload, object_id):
    headers = {"content-type": "application/json"}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=payload,
        headers=headers
    ).json()
    print(response)
    assert response['id'] == object_id


def partially_object(payload, object_id):
    headers = {"content-type": "application/json"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=payload,
        headers=headers
    ).json()
    print(response)
    assert response['id'] == object_id


def delete_object(object_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    assert response.status_code == 200


def get_object(object_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
    print(f'{response.json()}')


payload_for_add = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    },
}

payload_for_put = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 2049.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}

payload_for_patch = {"name": "Apple MacBook Pro 16 (Updated Name)"}


post_object_id = add_object(payload_for_add)
get_object(post_object_id)
update_object(payload_for_put, post_object_id)
partially_object(payload_for_patch, post_object_id)
delete_object(post_object_id)
