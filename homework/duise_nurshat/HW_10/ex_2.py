PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

lines = (line.split() for line in PRICE_LIST.split('\n'))

prices_dict = {item[0]: int(item[1][:-1]) for item in lines}

print(prices_dict)
