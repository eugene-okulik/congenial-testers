import allure
import pytest

from test_api_etimofeev.endpoints.delete_endpoint import CreateDeleteRequest
from test_api_etimofeev.endpoints.get_endpoint import CreateGetRequest
from test_api_etimofeev.endpoints.patch_endpoint import CreatePatchRequest
from test_api_etimofeev.endpoints.post_endpoint import CreatePostRequest
from test_api_etimofeev.endpoints.put_endpoint import CreatePutRequest


@allure.step("Creating an instance of the class")
@pytest.fixture()
def create_post_endpoint() -> CreatePostRequest:
    return CreatePostRequest()


@allure.step("Creating an instance of the class")
@pytest.fixture()
def create_get_endpoint() -> CreateGetRequest:
    return CreateGetRequest()


@allure.step("Creating an instance of the class")
@pytest.fixture()
def create_put_endpoint() -> CreatePutRequest:
    return CreatePutRequest()


@allure.step("Creating an instance of the class")
@pytest.fixture()
def create_patch_endpoint() -> CreatePatchRequest:
    return CreatePatchRequest()


@allure.step("Creating an instance of the class")
@pytest.fixture()
def create_delete_endpoint() -> CreateDeleteRequest:
    return CreateDeleteRequest()


@allure.step("Creating a Post request and getting id from response")
@pytest.fixture()
def getting_id(create_post_endpoint: CreatePostRequest) -> str:
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    }
    headers = {"Content-type": "application/json"}

    create_post_endpoint.create_post_request(payload=data, headers=headers)
    return create_post_endpoint.json["id"]
