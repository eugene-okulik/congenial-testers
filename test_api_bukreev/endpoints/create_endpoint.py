import allure
import requests

from test_api_bukreev.endpoints.base_edpoint import BaseEndpoint


class CreateEndpoint(BaseEndpoint):
    @allure.step('Create new object')
    def create_object(self, my_object):
        self.response = requests.post(self.url, json=my_object)
        self.json = self.response.json()
        return self.response
