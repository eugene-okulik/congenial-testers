my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [1, 'dva', 3.45, None, True],
           'dict': {'one': 1, 2: 'aga...', 3: 'blin4ik', 'four': 45, 'five': False},
           'set': {'aboba', 2, 3, 4}
           }

# присваиваю переменные для удобства их использования


my_tuple = my_dict['tuple']
my_list = my_dict['list']
internal_dict = my_dict['dict']
my_set = my_dict['set']
my_list.append('Noviy element')  # добавил элемент в конец списка
my_list.pop(1)  # удаление элемента 'dva' из списка
internal_dict['i am a tuple'] = 'luboe zna4enie))'  # добавление нового элемента в словарь
internal_dict.pop('five')  # удаление элемента из словаря
my_set.add('ya dobavil')  # добавление элемента во множество
my_set.remove('aboba')  # удаление элемента из множетсва
print(my_tuple[-1])  # распечатывание последнего элемент кортежа
print(my_dict)  # выводим словарь на экран
print(my_dict.values())  # просто чтобы было, потому что могу...
