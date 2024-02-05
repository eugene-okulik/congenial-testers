import pytest

from endpoints.create_endpoint import CreateEndpoint
from endpoints.base_edpoint import BaseEndpoint
from endpoints.delete_endpoint import DelEndpoint
from endpoints.put_endpoint import PutEndpoint
from endpoints.patch_endpoint import PatchEndpoint


@pytest.fixture()
def create_fun():
    return CreateEndpoint()


@pytest.fixture()
def get_fun():
    return BaseEndpoint()


@pytest.fixture()
def put_fun():
    return PutEndpoint()


@pytest.fixture()
def patch_fun():
    return PatchEndpoint()


@pytest.fixture()
def del_fun():
    return DelEndpoint()

@pytest.fixture()
def crud_fun(create_fun, del_fun):
    payload = {
        "name": "Apple fignya",
        "data": {
            "year": 2024,
            "price": 100.500,
            "CPU model": "M0",
            "Hard disk size": "1 Mb"
        }
    }
    create_fun.create_object(my_object=payload)
    yield create_fun.object_id
    del_fun.del_object(create_fun.object_id)
