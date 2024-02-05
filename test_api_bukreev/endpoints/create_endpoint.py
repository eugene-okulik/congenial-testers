import allure
import requests

from test_api_bukreev.endpoints.base_edpoint import BaseEndpoint


class CreateEndpoint(BaseEndpoint):
    object_id = None

    @allure.step('Create new object')
    def create_object(self, my_object):
        self.response = requests.post(self.url, json=my_object)
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
