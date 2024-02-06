import allure
import requests

from test_api_bukreev.endpoints.base_edpoint import BaseEndpoint


class PatchEndpoint(BaseEndpoint):

    @allure.step('Put something in object')
    def patch_object(self, my_object, create_object_patch):
        self.response = requests.patch(f'{self.url}/{create_object_patch}', json=my_object)
        self.json = self.response.json()
        return self.response
