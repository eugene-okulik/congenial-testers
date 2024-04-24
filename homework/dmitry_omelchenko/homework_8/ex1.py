import random

salary = int(input("Введите вашу зарплату (целое число): "))

bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randint(1, 5000)
    salary += random_bonus

print(f"Результат: ${salary}")
