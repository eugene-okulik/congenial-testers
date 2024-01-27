import pytest
import requests


@pytest.mark.critical
def test_get_request(creating_record: str):
    response = requests.get(f"https://api.restful-api.dev/objects/{creating_record}")
    assert response.status_code == 200, "Status code is not 200"


@pytest.mark.parametrize(
    "name", ["Iphone 15 Pro Max", "Samsung S24 Ultra", "Nothing Phone 1"]
)
def test_put_request(creating_record: str, name: str):
    payload = {
        "name": name,
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


@pytest.mark.medium
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
