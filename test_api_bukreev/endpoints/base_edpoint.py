import allure
import datetime
import requests


class BaseEndpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None

    @allure.step('Get object by ID')
    def get_object_by_id(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.response

    @allure.step(f'Delete needed element from dict')
    def del_element_from_dict(self, element):
        self.json.pop(element)
        return self.json

    @allure.step('Check that status code is 200')
    def status_code_is_200(self):
        assert self.response.status_code == 200, "Статус код не 200"

    @allure.step('Check that day is today')
    def day_is_today(self):
        assert self.json['createdAt'][:10] == str(datetime.datetime.now())[:10], "Дата на сервере некорректа"

    @allure.step('Check elements are equal')
    def are_equal(self, a, b):
        assert a == b, 'Elements are not equal'

    @allure.step('Check that data is None')
    def data_is_none(self, data):
        assert data is None, 'Data is not None'
