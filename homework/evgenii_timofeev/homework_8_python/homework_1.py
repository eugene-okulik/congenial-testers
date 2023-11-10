import random

salary = int(input("Введите вашу salary "))
bonus = random.choice([True, False])

if bonus:
    print(f"{salary}, True - '${salary + random.randint(1, 10000)}'")
else:
    print(f"{salary}, False - '${salary}'")
