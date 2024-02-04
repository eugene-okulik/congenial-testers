import allure
import requests

from test_api_bukreev.endpoints.base_edpoint import BaseEndpoint


class PutEndpoint(BaseEndpoint):

    @allure.step('Put something in object')
    def put_object(self, my_object, create_object_put):
        self.response = requests.put(f'{self.url}/{create_object_put}', json=my_object)
        self.json = self.response.json()
        return self.response
