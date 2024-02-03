from test_api_etimofeev.models.delete_model import ProductResponseModel


def test_delete_request(create_delete_endpoint, getting_id):
    create_delete_endpoint.create_delete_request(id=getting_id)
    create_delete_endpoint.validate_response(ProductResponseModel)
    create_delete_endpoint.check_message_about_deleting(getting_id)
