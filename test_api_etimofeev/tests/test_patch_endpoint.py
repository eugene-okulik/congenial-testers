def test_patch_request(create_patch_endpoint, getting_id):
    data = {"name": "Iphone 122 (Russia)"}
    create_patch_endpoint.create_patch_request(id=getting_id, payload=data)
    create_patch_endpoint.check_name_is_updated(data["name"])
