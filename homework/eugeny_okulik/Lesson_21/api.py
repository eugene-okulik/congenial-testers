import requests


def get_all():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    # response_text = response.text
    # print(response_text[0])
    response_json = response.json()
    # print(response_json[0]['title'])
    assert len(response_json) == 100, 'Incorrect quantity'


def get_one():
    post_id = 43
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    print(response['id'])
    assert response['id'] == 42, 'incorrect ID'


def post_a_post():
    payload = {
        "title": "My tile",
        "body": "my body",
        "userId": 1
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=payload,
        headers=headers
    ).json()
    print(response)


def put_a_post():
    payload = {
            "title": "My tileUPD",
            "body": "my bodyUPD",
            "userId": 2
        }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=payload,
        headers=headers
    ).json()
    print(response)


def patch_a_post():
    payload = {
                "title": "My tileUPD"
            }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=payload,
        headers=headers
    ).json()
    print(response)


def delete_a_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/101')
    print(response.status_code)
    assert requests.get('https://jsonplaceholder.typicode.com/posts/101').status_code == 404
