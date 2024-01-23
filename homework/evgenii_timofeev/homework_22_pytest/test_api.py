import pytest
import requests


@pytest.fixture(scope="module")
def greetings_farwell():
    print("Start testing")
    yield
    print("\n Testing completed")


@pytest.fixture(scope="function")
def creating_record(greetings_farwell) -> str:
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    }
    url = "https://api.restful-api.dev/objects"
    responce = requests.post(url, json=payload).json()
    record_id = responce["id"]
    yield record_id
    requests.delete(f"https://api.restful-api.dev/objects/{record_id}")


def test_get_request(creating_record: str):
    response = requests.get(f"https://api.restful-api.dev/objects/{creating_record}")
    assert response.status_code == 200, "Status code is not 200"


def test_put_request(creating_record: str):
    payload = {
        "name": "Iphone 121 (China)",
        "data": {
            "year": 3019,
            "Hard disk size": "100000 TB",
        },
    }

    response_put = requests.put(
        f"https://api.restful-api.dev/objects/{creating_record}", json=payload
    ).json()

    response_get = requests.get(
        f"https://api.restful-api.dev/objects/{creating_record}"
    ).json()
    assert response_put["name"] == response_get["name"], "Put request is failed"


def test_patch_request(creating_record):
    payload = {"name": "Iphone 122 (Russia)"}

    responce_patch = requests.patch(
        f"https://api.restful-api.dev/objects/{creating_record}", json=payload
    ).json()

    responce_get = requests.get(
        f"https://api.restful-api.dev/objects/{creating_record}"
    ).json()

    assert responce_patch["name"] == responce_get["name"], "Patch request is failed"


def test_delete_request(creating_record):
    requests.delete(f"https://api.restful-api.dev/objects/{creating_record}").json()

    responce_get = requests.get(
        f"https://api.restful-api.dev/objects/{creating_record}"
    )
    assert responce_get.status_code == 404, "Record wasn't deleted"
