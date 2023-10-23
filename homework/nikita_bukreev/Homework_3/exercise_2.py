# Даны действительные числа x и y. Получить x − y / 1 + xy

x = float(input())
y = float(input())
formula = x - y + x * y  # y / 1 = y, слеодвательно можно упростить вычисления
print(f'Результат вычислений равен {formula}')
