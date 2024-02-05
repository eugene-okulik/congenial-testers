from typing import Optional, Dict, Any

import allure
import requests

from test_api_etimofeev.endpoints.base_endpoint import BaseEndpoint
from test_api_etimofeev.models.put_model import ProductUpdateRequestModel


class CreatePutRequest(BaseEndpoint):
    @allure.step("Create a Put request")
    def create_put_request(
        self, id: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        with allure.step("Validate request data according to a model"):
            validated_payload = ProductUpdateRequestModel(**payload).model_dump()

        self.response = requests.put(
            f"{self.url}/{id}",
            json=validated_payload,
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
