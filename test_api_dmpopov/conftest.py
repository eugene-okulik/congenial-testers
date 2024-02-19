import pytest
from test_api_dmpopov.endpoints.post_endpoint import PostEndpoint
from test_api_dmpopov.endpoints.put_endpoint import PutEndpoint
from test_api_dmpopov.endpoints.patch_endpoint import PatchEndpoint
from test_api_dmpopov.endpoints.delete_endpoint import DeleteEndpoint
from test_api_dmpopov.endpoints.get_endpoint import GetEndpoint


@pytest.fixture()
def post_endpoint():
    return PostEndpoint()


@pytest.fixture()
def put_endpoint():
    return PutEndpoint()


@pytest.fixture()
def patch_endpoint():
    return PatchEndpoint()


@pytest.fixture()
def delete_endpoint():
    return DeleteEndpoint()


@pytest.fixture()
def get_endpoint():
    return GetEndpoint()


@pytest.fixture()
def post_id(post_endpoint, delete_endpoint):
    payload = {
        "name": "Apple iPad 2023",
        "data": {
            "year": 2023,
            "price": 1600.99,
            "CPU model": "m2",
            "Hard disk size": "1 TB"
        },
    }
    post_endpoint.create_post_request(payload)
    yield post_endpoint.post_id
    delete_endpoint.create_delete_request(post_endpoint.post_id)
