from test_api_etimofeev.models.get_model import ProductResponseModel


def test_get_request(create_get_endpoint, getting_id):
    create_get_endpoint.create_get_request(getting_id)
    create_get_endpoint.validate_response(ProductResponseModel)
