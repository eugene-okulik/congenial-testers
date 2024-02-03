from test_api_etimofeev.models.post_model import ProductResponseModel


def test_post_request(create_post_endpoint):
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    }
    create_post_endpoint.create_post_request(payload=data)
    create_post_endpoint.validate_response(ProductResponseModel)
    create_post_endpoint.check_for_creating_a_record(create_post_endpoint.json["id"])
