my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {100, 200, 300, 400, 500}
}

# Получение кортежа, хранящегося под ключом 'tuple'
my_tuple = my_dict['tuple']

# Вывод последнего элемента кортежа
last_element = my_tuple[-1]

print('Последний элемент кортежа:', last_element)

# Получение списка, под ключом 'list
my_list = my_dict['list']

# Добавление нового элемента в конец списка
my_list.append(60)

# Удаление второго элемента в списке
del my_list[1]

print('Список после добавления и удаления элементов:', my_list)

# Получение словаря, хранящегося под ключом 'dict'
my_dict_key = 'dict'
my_dict_value = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, ('i am a tuple',): 6}

# Удаление элемента с ключом 'b'
del my_dict_value['b']

# Обновление словаря в my_dict
my_dict[my_dict_key] = my_dict_value

# Вывод обновленного словаря
print("Словарь после добавления и удаления элементов:")
for key, value in my_dict[my_dict_key].items():
    print(key, ":", value)

# Получение множества, хранящегося под ключом 'set'
my_set = my_dict['set']

# Добавление нового элемента (600) в множество
my_set.add(600)

# Удаление элемента (300) из множества
my_set.remove(300)

# Вывод обновленного множества
print("Множество после добавления и удаления элементов:", my_set)

# Вывод словаря 'my_dict' на экран
for key, value in my_dict.items():
    print(key, ':', value)
