import random


salary = int(input('Введите желаемую зарплату: '))
bonus_choice = random.choice([True, False])
bonus = 0
if bonus_choice is True:  # тут можно легко if заменить на while, но информации, кто из них быстрее я не нашел(
    bonus = random.randint(1, 10000)
print(f"{salary}, {bonus_choice} - '${salary + bonus}'")
