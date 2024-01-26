import pytest
import requests


URL = 'https://api.restful-api.dev/objects'
my_object = {
    "name": "Apple fignya",
    "data": {
        "year": 2024,
        "price": 100.500,
        "CPU model": "M0",
        "Hard disk size": "1 Mb"
    }
}

@pytest.fixture(scope='session')
def show_progress():
    yield print('\nStart testing')
    print('\nTesting completed')


@pytest.fixture()
def crud_function():
    create_my_object = requests.post(URL, json=my_object).json()
    my_id = create_my_object['id']
    yield my_id
    requests.delete(URL + my_id)
