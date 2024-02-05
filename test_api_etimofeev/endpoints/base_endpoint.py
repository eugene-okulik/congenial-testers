from typing import Optional, Dict, Any

import allure
import requests
from pydantic import BaseModel, ValidationError


class BaseEndpoint:
    url: str = "https://api.restful-api.dev/objects"
    response: Optional[requests.Response] = None
    json: Optional[Dict[str, Any]] = None
    headers: Dict[str, str] = {"Content-type": "application/json"}

    @allure.step("Creating a Get request with gotten id")
    def check_for_creating_a_record(self, id: str) -> None:
        self.response = requests.get(f"{self.url}/{id}")
        assert (
            self.response.status_code == 200
        ), f"Response code is {self.response.status_code}"

    @allure.step("Checking that name from data == name from response")
    def check_name_is_updated(self, name: str) -> None:
        assert (
            self.json is not None and self.json["name"] == name
        ), "Name is not updated properly."

    @allure.step("Checking that message about deleting == message from response")
    def check_message_about_deleting(self, id: str) -> None:
        assert (
            self.json is not None
            and self.json["message"] == f"Object with id = {id} has been deleted."
        ), "Delete message does not match."

    @allure.step("Debug function. Helps to see response data")
    def show_info(self):
        print(self.json)

    @allure.step("Validate response data according to a model")
    def validate_response(self, response_model: type[BaseModel]) -> None:
        if self.json is None:
            raise AssertionError("No data in JSON.")
        try:
            response_model.model_validate(self.json)
        except ValidationError as e:
            raise AssertionError(f"Validation error: {e}")
