import allure

from test_api_etimofeev.models.patch_model import ProductResponseModel


@allure.feature("API Testing")
@allure.story("Send a valid PATCH request")
@allure.title("Test for a PATCH request")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_request(create_patch_endpoint, getting_id):
    data = {"name": "Iphone 122 (Russia)"}
    create_patch_endpoint.create_patch_request(id=getting_id, payload=data)
    create_patch_endpoint.validate_response(ProductResponseModel)
    create_patch_endpoint.check_name_is_updated(data["name"])
