from typing import Optional, Dict, Any

import requests

from test_api_etimofeev.endpoints.base_endpoint import BaseEndpoint


class CreatePostRequest(BaseEndpoint):
    def create_post_request(
        self, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        self.response = requests.post(
            self.url, json=payload, headers=headers if headers else self.headers
        )
        self.json = self.response.json()
        return self.response
