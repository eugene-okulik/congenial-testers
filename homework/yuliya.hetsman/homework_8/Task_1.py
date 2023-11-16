import random

salary = int(input('Enter your salary: '))
bonus = random.choice([True, False])
if bonus is True:
    print(f"{salary}, True - '${salary + random.randint(1, 10000)}'")
else:
    print(f"{salary}, False - '${salary}'")
