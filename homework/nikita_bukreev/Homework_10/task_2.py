# Получилось очень колхозно-костыльное решение чтобы соблюсти все условия задачи(
# Буду благодарен за подсказки, которые помогут сделать код чище и понятнее

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def separate_price(price):
    for line in price.split('\n'):
        new_line = line[0:-2].split()
        yield new_line[0], int(new_line[1])


my_price = dict([x for x in separate_price(PRICE_LIST)])
print(my_price)
