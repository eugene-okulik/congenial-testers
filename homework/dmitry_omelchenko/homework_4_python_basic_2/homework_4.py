my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {100, 200, 300, 400, 500}
}

# Вывод последнего элемента из кортежа, хранящегося под ключом 'tuple'
last_element = my_dict['tuple'][-1]
print("Последний элемент кортежа 'tuple':", last_element)

# Добавление нового элемента в список, хранящийся под ключом 'list'
my_dict['list'].append(60)

# Удаление второго элемента из списка, хранящегося под ключом 'list'
del my_dict['list'][1]

# Добавление новой пары ключ-значение в словарь, хранящийся под ключом 'dict'
my_dict['dict'][('i am a tuple,')] = 'value'

# Удаление элемента с ключом 'b'
del my_dict['dict']['b']

# Добавление нового элемента во множество, хранящееся под ключом 'set'
my_dict['set'].add(600)

# Удаление элемента из множества, хранящегося под ключом 'set'
my_dict['set'].discard(300)

# Вывод всего словаря
print(my_dict)
