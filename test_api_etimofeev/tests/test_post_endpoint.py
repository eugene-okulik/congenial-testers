def test_post_request(create_post_endpoint, getting_id):
    create_post_endpoint.check_for_creating_a_record(getting_id)
