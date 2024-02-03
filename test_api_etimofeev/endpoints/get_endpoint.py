from typing import Optional, Dict

import requests

from test_api_etimofeev.endpoints.base_endpoint import BaseEndpoint


class CreateGetRequest(BaseEndpoint):
    def create_get_request(
        self, id: str, headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        self.response = requests.get(
            f"{self.url}/{id}", headers=headers if headers else self.headers
        )
        self.json = self.response.json()
        assert (
            self.response.status_code == 200
        ), f"Response code is {self.response.status_code}"
        return self.response
