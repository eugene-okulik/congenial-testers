import random

number_of_program = random.randint(1, 10)
number_of_user = int(input("Введите число от 1 до 10 "))

while number_of_program != number_of_user:
    print("Попробуйте снова")
    number_of_user = int(input("Введите число от 1 до 10 "))

print(f"Поздравляю! Вы угадали число {number_of_program}")
