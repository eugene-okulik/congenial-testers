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
    response = requests.post(url, json=payload).json()
    record_id = response["id"]
    yield record_id
    requests.delete(f"https://api.restful-api.dev/objects/{record_id}")
