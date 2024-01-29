import requests


def post_add_object(payload):
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


def put_edit_object(payload, object_id):
    headers = {"content-type": "application/json"}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=payload,
        headers=headers
    ).json()
    print(response)
    assert response['id'] == object_id


def patch_object(payload, object_id):
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


payload_for_post = {
    "name": "Apple MacBook Pro 16 m3",
    "data": {
        "year": 2023,
        "price": 2500.99,
        "CPU model": "m3",
        "Hard disk size": "1 TB"
    },
}

payload_for_put = {
    "name": "Apple MacBook Pro 16 m2",
    "data": {
        "year": 2022,
        "price": 2200.99,
        "CPU model": "m3",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}

payload_for_patch = {"name": "Apple MacBook Pro 16 m1(Updated Name)"}


post_object_id = post_add_object(payload_for_post)
get_object(post_object_id)
put_edit_object(payload_for_put, post_object_id)
patch_object(payload_for_patch, post_object_id)
delete_object(post_object_id)
