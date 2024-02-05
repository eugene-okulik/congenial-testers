from typing import Optional, Dict

import allure
import requests

from test_api_etimofeev.endpoints.base_endpoint import BaseEndpoint


class CreateDeleteRequest(BaseEndpoint):
    @allure.step("Creating a Delete request")
    def create_delete_request(
        self, id: str, headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        self.response = requests.delete(
            f"{self.url}/{id}", headers=headers if headers else self.headers
        )
        self.json = self.response.json()
        return self.response
