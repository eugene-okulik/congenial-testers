# Создание словаря и выполнение различных действий с ним
# комменты и отступы между выполнение действий не обязательны, но мне так было проще и, кмк, читается лучше=)

my_dict = {
    'tuple': ('korteg', 5, 7, 9, 11),
    'list': ['spisok', 6, 8, 10, 12],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {'mnogestvo', 11, 12, 13, 14}
}

print(my_dict['tuple'][-1])  # Кортеж, выведите на экран последний элемент

# список
my_dict['list'].append('last')  # добавьте в конец списка еще один элемент
my_dict['list'].pop(1)  # удалите второй элемент списка

# словарь
my_dict['dict'][('i am a tuple',)] = 666  # добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'].pop('one')  # удалите какой-нибудь элемент

# множество
my_dict['set'].add('new_element')  # добавьте новый элемент в множество
my_dict['set'].remove('mnogestvo')  # удалите элемент из множества

print(my_dict)