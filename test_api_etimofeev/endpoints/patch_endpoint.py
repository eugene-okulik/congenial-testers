from typing import Optional, Dict, Any

import requests

from test_api_etimofeev.endpoints.base_endpoint import BaseEndpoint
from test_api_etimofeev.models.patch_model import ProductUpdateRequestModel


class CreatePatchRequest(BaseEndpoint):
    def create_patch_request(
        self, id: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        validated_payload = ProductUpdateRequestModel(**payload).model_dump()
        self.response = requests.patch(
            f"{self.url}/{id}",
            json=payload,
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
