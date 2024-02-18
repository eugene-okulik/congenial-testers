import requests
import allure
from test_api_dmpopov.endpoints.base_endpoint import BaseEndpoint


class GetEndpoint(BaseEndpoint):
    @allure.step("Creating a Get request")
    def create_get_request(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/{post_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
