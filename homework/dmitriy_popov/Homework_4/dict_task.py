my_dict = {
    'tuple': (1, 3, 7, "text", False, 2.42),
    'list': [4, 2, 6, 8, None, "text1", False, 2.42, ],
    'dict': {"one": 1, "two": 2, "three": 3, "for": 4, "five": 5},
    'set': {1, 3, 6, 7, None, "text3", 3, 7}
}

# Кортеж, выведите на экран последний элемент
print(my_dict['tuple'][-1])

# Список, добавьте в конец списка еще один элемент и удалите второй элемент списка
my_dict['list'].append(444222)
my_dict['list'].pop(1)

# Словарь, добавьте элемент с ключом ('i am a tuple',) и любым значением и удалите какой-нибудь элемент
my_dict['dict'][('i am a tuple',)] = 377
my_dict['dict'].pop('two')

# Множество, добавьте новый элемент в множество и удалите элемент из множества
my_dict['set'].add('new_element')
my_dict['set'].remove('text3')

# Выведите на экран весь словарь
print(my_dict)
