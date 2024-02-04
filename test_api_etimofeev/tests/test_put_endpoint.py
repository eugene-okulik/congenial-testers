import allure
import pytest

from test_api_etimofeev.models.put_model import ProductResponseModel


@allure.feature("API Testing")
@allure.story("Send a valid PUT request")
@allure.title("Test for a PUT request")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "name", ["Iphone 15 Pro Max", "Samsung S24 Ultra", "Nothing Phone 1"]
)
def test_put_request(create_put_endpoint, getting_id, name):
    data = {
        "name": name,
        "data": {
            "year": 3019,
            "Hard disk size": "100000 TB",
        },
    }
    id = getting_id
    create_put_endpoint.create_put_request(id=id, payload=data)
    create_put_endpoint.validate_response(ProductResponseModel)
    create_put_endpoint.check_name_is_updated(data["name"])
