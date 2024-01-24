import requests


def add_object():
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


# add_object()


def update_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.put(
        'https://api.restful-api.dev/objects/ff8081818d2cb651018d3af66c901587',
        json=payload,
        headers=headers
    ).json()

    print(response)


# update_object()


def partially_update():
    payload = {
        "name": "Apple MacBook Pro 17"
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.patch(
        'https://api.restful-api.dev/objects/ff8081818d2cb651018d3af66c901587',
        json=payload,
        headers=headers
    ).json()

    print(response)


# partially_update()


def delete_object():
    response = requests.delete('https://api.restful-api.dev/objects/ff8081818d2cb651018d3af66c901587')
    print(response.status_code)


# delete_object()
