import random

salary = int(input('Введите свою зарплату: '))
bonus = random.choice([True, False])
if bonus is True:
    print(f"{salary}, True - '${salary + random.randint(100, 5000)}'")
else:
    print(f"{salary}, False - '${salary}'")
