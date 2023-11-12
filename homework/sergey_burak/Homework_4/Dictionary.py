# Создание словаря
# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.
# Для каждого элемента задайте значение соответствующее названию ключа.
# Например в элемент с ключом ‘tuple’ добавьте кортеж в качестве значения.
# Содержимое этого кортежа (или что вы там добавляете) - на вашу фантазию,
# но количество элементов в каждом таком значении должно быть не меньше пяти.
# Т.е. если добавляете кортеж, то в нем как минимум должно быть (1, 2, 3, 4, 5),
# если список, то не меньше пяти элементов, если словарь, то не меньше пяти пар ключ-значение, итд.
#
# Действия с элементами словаря my_dict:
#     Для того, что хранится под ключом ‘tuple’:
#         выведите на экран последний элемент
#     Для того, что хранится под ключом ‘list’:
#         добавьте в конец списка еще один элемент
#         удалите второй элемент списка
#     Для того, что хранится под ключом ‘dict’:
#         добавьте элемент с ключом ('i am a tuple',) и любым значением
#         удалите какой-нибудь элемент
#     Для того, что хранится под ключом ‘set’:
#         добавьте новый элемент в множество
#         удалите элемент из множества
#
# В конце выведите на экран весь словарь

my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': ['six', 7, 8, 9, 10],
           'dict': {'mo': 'Monday', 'tu': 'Tuesday', 'we': 'Wednesday', 'th': 'Thursday', 'fr': 'Friday'},
           'set': {11, 12, 13, 14, 15}}

print('исходный вид словаря: ', my_dict)
print('последний элемент под ключом tuple: ', my_dict['tuple'][-1])
my_dict['list'].append('eleven')
my_dict['list'].pop(1)
print('добавим в конец списка list ещё один элемент и удалим второй: ', my_dict['list'])
my_dict['dict'][('i am a tuple',)] = 'Holyday'
del my_dict['dict']['mo']
print('добавим в dict элемент c ключом и любым значением, удаляем какой-нибудь элемент: ', my_dict['dict'])
my_dict['set'].add(10)
my_dict['set'].discard(12)
print('добавим новый элемент в множество, удалим элемент из множества: ', my_dict['set'])
print('в результате получаем вот такой словарь: ', my_dict)