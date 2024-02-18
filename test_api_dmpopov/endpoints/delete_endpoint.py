import requests
import allure
from test_api_dmpopov.endpoints.base_endpoint import BaseEndpoint


class DeleteEndpoint(BaseEndpoint):
    @allure.step("Creating a Delete request")
    def create_delete_request(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
