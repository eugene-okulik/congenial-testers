import allure

from test_api_etimofeev.models.delete_model import ProductResponseModel


@allure.feature("API Testing")
@allure.story("Send a valid DELETE request")
@allure.title("Test for a DELETE request")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_request(create_delete_endpoint, getting_id):
    create_delete_endpoint.create_delete_request(id=getting_id)
    create_delete_endpoint.validate_response(ProductResponseModel)
    create_delete_endpoint.check_message_about_deleting(getting_id)
