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
