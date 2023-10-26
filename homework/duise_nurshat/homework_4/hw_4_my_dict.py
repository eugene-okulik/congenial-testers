# 'Создание словаря, внутри есть кортеж, лист, словарь и сет. В каждом из них есть 5 элементов внутри
print('New dictionary:')
my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': [1.1, 2.2, 3.3, 4.4, 5.5],
           'dict': {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'},
           'set': {'mini_set', 7.77, 'seven_eleven', 1, 2}}
print(my_dict)

# вывод последнего элемента на экран с ключа 'tuple'
print('Вывод последнего элемента на экран с ключа "tuple":')
print(my_dict['tuple'][-1])

# добавление в конец списка нового элемента в ключе 'list'
print('Добавление в конец списка нового элемента в ключе "list":')
new_list_el = 7.7
my_dict['list'].append(new_list_el)
print(my_dict)
print('Добавленный элемент:')
print(new_list_el)

# удаление второго элемента в списке ключа 'list'
print('Удаление второго элемента в списке ключа "list":')
poped = my_dict['list'].pop(1)
print(my_dict)
print('Удаленный элемент:')
print(poped)

# добавление нового элемента в ключ 'dict'
print('Добавление нового элемента в ключ "dict":')
my_dict['dict']['i am a tuple'] = '5458'
print(my_dict)
print('Добавленный элемент:')
print(my_dict['dict']['i am a tuple'])

# удаление элемента с ключа 'dict'
print('Удаление элемента с ключа "dict":')
poped2 = my_dict['dict'].pop(1)
print(my_dict)
print('Удаленный элемент:')
print(poped2)

# добавление нового элемента в ключ 'set'
print('Добавление нового элемента в ключ "set":')
new_set_el = 'new_one'
my_dict['set'].add(new_set_el)
print(my_dict)
print('Добавленный элемент:')
print(new_set_el)

# удаление элемента с ключа 'set'
print('Удаление элемента с ключа "set":')
poped3 = my_dict['set'].remove(2)
print(my_dict)
print('Удаленный элемент:')
print(poped3)

print('Весь словарь:')
print(my_dict)
