import allure
import requests

from test_api_bukreev.endpoints.base_edpoint import BaseEndpoint


class DelEndpoint(BaseEndpoint):
    @allure.step('Delete object')
    def del_object(self, needed_id):
        self.response = requests.delete(f'{self.url}/{needed_id}')
        self.json = self.response.json()
        return self.response

    @allure.step('Check message about delete')
    def check_del_message(self, json, object_id):
        assert json['message'] == f'Object with id = {object_id} has been deleted.', 'Message is incorrect'

    @allure.step('Check message that object not found')
    def check_not_found_message(self, json, object_id):
        assert json['error'] == f'Oject with id={object_id} was not found.', 'Не получена ошибка о ненайденном объекте'
