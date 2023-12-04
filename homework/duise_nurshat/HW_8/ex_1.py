import random

salary = int(input("Введите вашу зарплату: "))
bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randint(1, 5000)
    print(f"{salary}, TRue - '${salary + random.randrange(1, 1000000)}'")
else:
    print(f"{salary}, False - '${salary}'")
