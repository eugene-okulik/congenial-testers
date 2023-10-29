my_dict = {
    'my_list': ["one", "two", "three", "four", "five"],
    'my_tuple': (1, 2, 3, 4, 5),
    'my_set': {1, 2, 3, 4, 5},
    'my_dict1': {'one': 'value1', 'two': 'value2', 'three': 'value3', 'four': "value4", 'five': 'value5'}
            }

#Для того, что хранится под ключом ‘tuple’:
#выведите на экран последний элемент
print(my_dict['my_tuple'][-1])

#Для того, что хранится под ключом ‘list’:
#добавьте в конец списка еще один элемент
#удалите второй элемент списка
my_dict['my_list'].append('asd')
my_dict['my_list'].pop(1)
print(my_dict)

#Для того, что хранится под ключом ‘set’:
#добавьте новый элемент в множество
#удалите элемент из множества
my_dict['my_set'].add(777)
my_dict['my_set'].remove(3)
print(my_dict)

#Для того, что хранится под ключом ‘dict’:
#добавьте элемент с ключом ('i am a tuple',) и любым значением
#удалите какой-нибудь элемент
my_dict['my_dict1'] = 'last'
my_dict['my_dict1']['i am a tuple'] = 2
print(my_dict)

#В конце выведите на экран весь словарь
print(my_dict)