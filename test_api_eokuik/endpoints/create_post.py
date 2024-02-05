import requests
import allure

from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step('Create new post')
    def create_new_post(self, payload, headers=None):
        if len(payload['body']) > 1000:
            self.url = f'{self.url}/dlinnopost'
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        print(self.response, self.url)
        self.json = self.response.json()
        return self.response
