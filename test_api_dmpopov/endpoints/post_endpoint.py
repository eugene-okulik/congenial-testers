import requests
import allure
from test_api_dmpopov.endpoints.base_endpoint import BaseEndpoint


class PostEndpoint(BaseEndpoint):
    post_id = None

    @allure.step('Create new post')
    def create_post_request(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response
