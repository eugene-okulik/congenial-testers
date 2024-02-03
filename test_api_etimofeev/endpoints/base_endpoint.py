from typing import Optional, Dict, Any

import requests


class BaseEndpoint:
    url: str = "https://api.restful-api.dev/objects"
    response: Optional[requests.Response] = None
    json: Optional[Dict[str, Any]] = None
    headers: Dict[str, str] = {"Content-type": "application/json"}

    def check_for_creating_a_record(self, id: str) -> None:
        self.response = requests.get(f"{self.url}/{id}")
        assert (
            self.response.status_code == 200
        ), f"Response code is {self.response.status_code}"

    def check_name_is_updated(self, name: str) -> None:
        assert (
            self.json is not None and self.json["name"] == name
        ), "Name is not updated properly."

    def check_message_about_deleting(self, id: str) -> None:
        assert (
            self.json is not None
            and self.json["message"] == f"Object with id = {id} has been deleted."
        ), "Delete message does not match."

    def show_info(self):
        print(self.json)
