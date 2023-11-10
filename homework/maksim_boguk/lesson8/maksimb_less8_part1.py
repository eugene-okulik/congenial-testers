import random

salary = int(input('Полученная зп: '))
sbonus = random.choice([True, False])
bonus = random.randint(2, 1000)
while sbonus is True:
    result = salary * bonus
    print(f'{result}')
    break
