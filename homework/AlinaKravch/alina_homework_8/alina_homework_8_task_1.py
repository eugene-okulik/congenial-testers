import random


salary = int(input('Enter the salary: '))
bonus = random.choice([True, False])

if bonus:
    print(f"${salary}, 'True - ${salary + random.randrange(100, 10000)}'")
else:
    print(f"${salary}, 'False - ${salary}'")