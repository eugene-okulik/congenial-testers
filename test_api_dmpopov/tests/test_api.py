import allure
import pytest

test_data = {
    "name": "Apple iPad 2023",
    "data": {
        "year": 2023,
        "price": 1600.99,
        "CPU model": "m2",
        "Hard disk size": "1 TB"
    },
}

put_data = {"color": "silver"}
list_of_name = ['Huawei Ultra', 'Samsung pro14', 'Lenovo E47']
patch_data = {"name": "Apple MacBook Pro 16 m1(Updated Name)"}


@allure.feature("API Testing")
@allure.title("Test for a Post request")
def test_new_post(post_endpoint):
    post_endpoint.create_post_request(payload=test_data)
    post_endpoint.check_that_status_is_200()
    post_endpoint.check_response_title_is_correct(test_data['name'])


@allure.feature("API Testing")
@allure.title("Test for a Put request")
@pytest.mark.parametrize('name', list_of_name)
def test_put_edit_object(put_endpoint, post_id, name):
    with allure.step('Prepare test data'):
        test_data['name'] = name
        test_data['data'].update(put_data)
    put_endpoint.create_put_request(post_id, payload=test_data)
    put_endpoint.check_that_status_is_200()
    put_endpoint.check_response_title_is_correct(test_data['name'])


@allure.feature("API Testing")
@allure.title("Test for a Patch request")
def test_patch_object(patch_endpoint, post_id):
    patch_endpoint.create_patch_request(post_id, payload=patch_data)
    patch_endpoint.check_that_status_is_200()
    patch_endpoint.check_response_title_is_correct(patch_data['name'])


@allure.feature("API Testing")
@allure.title("Test for a Get request")
def test_get_object(get_endpoint, post_id):
    get_endpoint.create_get_request(post_id)
    get_endpoint.check_that_status_is_200()


@allure.feature("API Testing")
@allure.title("Test for a DELETE request")
def test_delete_object(delete_endpoint, post_id):
    delete_endpoint.create_delete_request(post_id)
    delete_endpoint.check_that_status_is_200()
