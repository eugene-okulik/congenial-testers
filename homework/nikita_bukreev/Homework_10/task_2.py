
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


my_price = {line[0:-2].split()[0]: int(line[0:-2].split()[1]) for line in PRICE_LIST.split('\n')}
print(my_price)

new_dict = {}
for line in PRICE_LIST.split('\n'):
    new_line = line[0:-2].split()
    new_dict[new_line[0]] = int(new_line[1])
