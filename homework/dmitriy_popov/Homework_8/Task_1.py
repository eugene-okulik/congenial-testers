import random


salary = int(input('Введите зарплату: '))
bonus = random.choice([True, False])

if bonus:
    print(f"{salary}, True - '${salary + random.randrange(1, salary*2)}'")
else:
    print(f"{salary}, False - '${salary}'")
