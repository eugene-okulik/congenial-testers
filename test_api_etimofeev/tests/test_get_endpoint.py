import allure

from test_api_etimofeev.models.get_model import ProductResponseModel


@allure.feature("API Testing")
@allure.story("Send a valid Get request")
@allure.title("Test for a GET request")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_request(create_get_endpoint, getting_id):
    create_get_endpoint.create_get_request(getting_id)
    create_get_endpoint.validate_response(ProductResponseModel)
