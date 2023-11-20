# Дан такой кусок прайс листа: (Копируйте эту переменную (константу) в код прямо как есть)
#
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
#
# При помощи генераторов превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
#
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# price_list = list(PRICE_LIST.split('\n'))
# new_price = []
# for i in price_list:
#     new_price.append((i[:-1]))
# super_price = []
# for i in new_price:
#     super_price.append(i.split())
#
# price_dict = {key: int(value) for key, value in super_price}
#
# # print(price_list)
# # print(new_price)
# # print(super_price)
# print(price_dict)
###################################################

print({key: int(value) for key, value in [x.split() for x in [(i[:-1]) for i in list(PRICE_LIST.split('\n'))]]})

###################################################
# price_list = list(PRICE_LIST.split())
# new_price = []
# for i in price_list[1::2]:
#     new_price.append(int(i.replace('р', '')))
#
# print(price_list )
# print(list(PRICE_LIST.split())[::2])
# print(new_price)
###################################################
# new_price = map(lambda i: int(i.replace('р', '')), list(PRICE_LIST.split())[1::2])
# print(dict(zip(list(PRICE_LIST.split())[::2], new_price)))
####################################################
# print(dict(zip(list(PRICE_LIST.split())[::2],
#                map(lambda i: int(i.replace('р', '')), list(PRICE_LIST.split())[1::2]))))
####################################################

print(dict(zip(list(PRICE_LIST.split())[::2], [int(i.replace('р', '')) for i in list(PRICE_LIST.split())[1::2]])))
