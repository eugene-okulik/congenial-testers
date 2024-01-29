import datetime
import requests


my_object = {
    "name": "Apple fignya",
    "data": {
        "year": 2024,
        "price": 100.500,
        "CPU model": "M0",
        "Hard disk size": "1 Mb"
    }
}


def create_object():
    create_my_object = requests.post('https://api.restful-api.dev/objects', json=my_object)

    # т.к. это превый тест, то проверяю статус ответа
    assert create_my_object.status_code == 200, f'Пришел статус код {create_my_object.status_code}, а должен быть 200'

    # перевожу в словарь, вычленяю айди и дату создания для дальнейших проверок
    create_object_json = create_my_object.json()
    new_object_id = create_object_json.pop('id')
    created_at = create_object_json.pop('createdAt')
    assert created_at[:10] == str(datetime.datetime.now())[:10], "Дата на сервере некорректа"
    assert create_object_json == my_object, 'Ответ от сервера пришел с неверным объектом'

    # Проверяю, что созданный объект соответствует заданным параметрам и возварщаю айди для дальнейшей работы
    get_my_object = requests.get(f'https://api.restful-api.dev/objects/{new_object_id}').json()
    get_my_object_id = get_my_object.pop('id')
    assert get_my_object_id == new_object_id, 'Айди на сервере не соответствует айди в респонсе при создании'
    assert get_my_object == create_object_json, 'Созданный объект не соответствует изначальному'
    return new_object_id


def edit_by_put(id_object):
    edited_data = {"name": "Apple polnaya fignya"}
    edit_object_put = requests.put(f'https://api.restful-api.dev/objects/{id_object}', json=edited_data).json()
    assert edit_object_put['name'] == edited_data['name'], "Метод отработал некорректно, имя не поменялось"
    assert edit_object_put['data'] is None, "Метод отработал некорректно, data осталась у объекта"


def edit_by_putch(id_object):
    putched_data = {
        "data": {
            "year": 2025,
            "price": 123.321,
            "CPU model": "M100500",
            "Hard disk size": "1 GB"
        }
    }
    get_object = requests.get(f'https://api.restful-api.dev/objects/{id_object}').json()
    putched_object = requests.patch(f'https://api.restful-api.dev/objects/{id_object}', json=putched_data).json()
    assert putched_object['data'] == putched_data['data']
    assert putched_object['name'] == get_object['name']


def delete_object(id_object):
    delete_my_object = requests.delete(f'https://api.restful-api.dev/objects/{id_object}').json()
    assert delete_my_object['message'] == f'Object with id = {id_object} has been deleted.', \
        'Ответ об успешном удалении не получен'
    find_my_object = requests.get(f'https://api.restful-api.dev/objects/{id_object}').json()
    assert find_my_object['error'] == f'Oject with id={id_object} was not found.', \
        'Не получена ошибка о ненайденном объекте'


object_id = create_object()
edit_by_put(object_id)
edit_by_putch(object_id)
delete_object(object_id)
