import requests
import allure
from test_api_dmpopov.endpoints.base_endpoint import BaseEndpoint


class PatchEndpoint(BaseEndpoint):
    @allure.step("Creating a Patch request")
    def create_patch_request(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
