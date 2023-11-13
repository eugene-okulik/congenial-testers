# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
#     10000, True - '$10255'
#     25000, False - '$25000'
#     600, True - '$3785'

import random

bonus = random.choice([True, False])
addbonus = random.randint(250, 785)
salary = int(input("Введите salary: "))

if bonus is True:
    print(f'{salary}, {bonus} - ${salary + addbonus}')
else:
    print(f"{salary}, {bonus} - '${salary}'")
