import requests


def add_elem():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"

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


def put_a_post():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "BLACKSTAR"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.put(
        'https://api.restful-api.dev/objects/ff8081818d2cb651018d41716a561fee',
        json=payload,
        headers=headers
    ).json()
    print(response)


def patch_a_post():
    payload = {
        "name": "Apple MacBook Pro 16 777"
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.patch(
        'https://api.restful-api.dev/objects/ff8081818d2cb651018d41716a561fee',
        json=payload,
        headers=headers
    ).json()

    print(response)


def delete_a_post():
    response = requests.delete('https://api.restful-api.dev/objects/ff8081818d2cb651018d41716a561fee')
    print(response.status_code)


add_elem()
put_a_post()
patch_a_post()
delete_a_post()
