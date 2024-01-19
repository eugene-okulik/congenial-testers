import requests

URL_GET = "https://api.restful-api.dev/objects/"
URL_POST = "https://api.restful-api.dev/objects"
URL_PUT = "https://api.restful-api.dev/objects/"
URL_DELETE = "https://api.restful-api.dev/objects/"
URl_PATCH = "https://api.restful-api.dev/objects/"

payload_for_post = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
    },
}

payload_for_put = {
    "name": "Iphone 121 (China)",
    "data": {
        "year": 3019,
        "Hard disk size": "100000 TB",
    },
}

payload_for_patch = {"name": "Iphone 122 (Russia)"}


def get_request(url, id=""):
    url += id
    response = requests.get(url).json()
    return response


def post_request(url, test):
    responce = requests.post(url, json=test).json()

    created_id = responce["id"]
    url += "/"
    check_created_id = get_request(url, created_id)["id"]

    assert created_id == check_created_id, "Id from get request != id from post request"
    return created_id


def put_request(url, payload, id):
    url += id
    requests.put(url, json=payload).json()

    name_before_put = payload["name"]
    name_after_put = get_request(url)["name"]

    assert (
        name_before_put == name_after_put
    ), "Name from get request != name from put request"


def patch_request(url, payload, id):
    url += id
    requests.patch(url, json=payload).json()

    name_before_patch = payload["name"]
    name_after_patch = get_request(url)["name"]

    assert (
        name_before_patch == name_after_patch
    ), "Name from get request != name from patch request"


def delete_request(url, id):
    url += id
    responce = requests.delete(url).json()

    message_about_deleting = responce["message"]

    assert (
        message_about_deleting == f"Object with id = {id} has been deleted."
    ), f"Messages about deleting aren't matched"
    print(responce)


id = post_request(URL_POST, payload_for_post)
put_request(URL_PUT, payload_for_put, id)
patch_request(URl_PATCH, payload_for_patch, id)
delete_request(URL_DELETE, id)
