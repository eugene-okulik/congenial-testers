import random


def calc_salary(salary, bonus):
    if bonus:
        random_bonus = random.randint(1, 5000)
        yield salary + random_bonus
    else:
        yield salary


salary = int(input("Введите вашу зарплату: "))
bonus = random.choice([True, False])

result = calc_salary(salary, bonus)

final_salary = next(result)

print(f"Итоговая зарплата: ${final_salary}")
