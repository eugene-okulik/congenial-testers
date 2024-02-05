import allure
import pytest


MY_OBJECT = {
    "name": "Apple fignya",
    "data": {
        "year": 2024,
        "price": 100.500,
        "CPU model": "M0",
        "Hard disk size": "1 Mb"
    }
}

EDITED_DATA = [{"name": "Apple polnaya fignya"}, {"name": "111"}, {"name": "small"}]

PATCHED_DATA = {
    "data": {
        "year": 2025,
        "price": 123.321,
        "CPU model": "M100500",
        "Hard disk size": "1 GB"
    }
}


@allure.feature('Homework 25')
@allure.story('Main test')
@pytest.mark.critical
def test_create_object(create_fun, get_fun, del_fun):
    create_fun.create_object(my_object=MY_OBJECT)
    create_fun.status_code_is_200()
    create_fun.day_is_today()
    get_fun.get_object_by_id(create_fun.json['id'])
    get_fun.are_equal(get_fun.json, create_fun.del_element_from_dict('createdAt'))
    del_fun.del_object(get_fun.json['id'])


@allure.feature('Homework 25')
@pytest.mark.parametrize('edited_data', EDITED_DATA)
def test_edit_by_put(put_fun, edited_data, get_fun, del_fun, crud_fun):
    put_fun.put_object(edited_data, crud_fun)
    get_fun.get_object_by_id(put_fun.json['id'])
    get_fun.are_equal(get_fun.json['name'], edited_data['name'])
    get_fun.data_is_none(get_fun.json['data'])


@allure.feature('Homework 23')
@pytest.mark.medium
def test_edit_by_putch(crud_fun, patch_fun, get_fun, del_fun):
    patch_fun.patch_object(PATCHED_DATA, crud_fun)
    get_fun.get_object_by_id(patch_fun.json['id'])
    get_fun.are_equal(get_fun.json['data'], PATCHED_DATA['data'])
    get_fun.are_equal(get_fun.json['name'], MY_OBJECT['name'])


@allure.feature('Homework 23')
def test_delete_object(crud_fun, del_fun, get_fun):
    del_fun.del_object(crud_fun)
    del_fun.check_del_message(del_fun.json, crud_fun)
    get_fun.get_object_by_id(crud_fun)
    del_fun.check_not_found_message(get_fun.json, crud_fun)
