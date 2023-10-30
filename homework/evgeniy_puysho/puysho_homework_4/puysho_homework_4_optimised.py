my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [1, 'dva', 3.45, None, True],
           'dict': {'one': 1, 2: 'aga...', 3: 'blin4ik', 'four': 45, 'five': False},
           'set': {1, 2, 'aboba', 2, 3, 4}
           }

# добавил элемент в конец списка
my_dict['list'].append('Noviy element')

# удаление элемента 'dva' из списка
my_dict['list'].remove('dva')

# добавление нового элемента в словарь
my_dict['dict'][('i am a tuple',)] = 'luboe znachenie'

# удаление элемента из словаря
my_dict['dict'].pop('five')

# добавление элемента во множество
my_dict['set'].add('ya dobavil')

# удаление элемента из множетсва
my_dict['set'].remove('aboba')

# распечатывание последнего элемент кортежа
print(my_dict['tuple'][-1])

# выводим словарь на экран
print(my_dict)
