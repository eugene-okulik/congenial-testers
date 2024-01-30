import allure
import pytest
import requests


@allure.title("ПРОВЕРКА2")
@allure.feature("API Testing")
@allure.story("Send a valid GET request")
@allure.title("Test for Get request")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.critical
def test_get_request(creating_record: str):
    with allure.step("Send GET request"):
        response = requests.get(
            f"https://api.restful-api.dev/objects/{creating_record}"
        )
    with allure.step("Check GET response"):
        assert response.status_code == 200, "Status code is not 200"


@allure.feature("API Testing")
@allure.story("Send a valid PUT request")
@allure.title("Test for Put request")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize(
    "name", ["Iphone 15 Pro Max", "Samsung S24 Ultra", "Nothing Phone 1"]
)
def test_put_request(creating_record: str, name: str):
    payload = {
        "name": name,
        "data": {
            "year": 3019,
            "Hard disk size": "100000 TB",
        },
    }
    with allure.step("Send PUT request"):
        response_put = requests.put(
            f"https://api.restful-api.dev/objects/{creating_record}", json=payload
        ).json()

    with allure.step("Send GET request for checking"):
        response_get = requests.get(
            f"https://api.restful-api.dev/objects/{creating_record}"
        ).json()
    with allure.step("Check responses from PUT and GET"):
        assert response_put["name"] == response_get["name"], "Put request is failed"


@allure.feature("API Testing")
@allure.story("Send a valid PATCH request")
@allure.title("Test for Patch request")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.medium
def test_patch_request(creating_record):
    payload = {"name": "Iphone 122 (Russia)"}

    with allure.step("Send Patch request"):
        responce_patch = requests.patch(
            f"https://api.restful-api.dev/objects/{creating_record}", json=payload
        ).json()

    responce_get = requests.get(
        f"https://api.restful-api.dev/objects/{creating_record}"
    ).json()

    with allure.step("Check Patch response"):
        assert responce_patch["name"] == responce_get["name"], "Patch request is failed"
    with allure.step("Send an image"):
        with open(
            "gtest.jpg",
            "rb",
        ) as image_file:
            allure.attach(
                image_file.read(),
                name="Скриншот",
                attachment_type=allure.attachment_type.PNG,
            )


@allure.feature("API Testing")
@allure.story("Send a valid DELETE request")
@allure.title("Test for Delete request")
@allure.severity(allure.severity_level.MINOR)
def test_delete_request(creating_record):
    requests.delete(f"https://api.restful-api.dev/objects/{creating_record}").json()

    responce_get = requests.get(
        f"https://api.restful-api.dev/objects/{creating_record}"
    )
    with allure.step("Check Delete response"):
        assert responce_get.status_code == 404, "Record wasn't deleted"
