# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

from math import sqrt


katet_1 = float(input())
katet_2 = float(input())
gipotenyza = sqrt(katet_1 ** 2 + katet_2 ** 2)
area = (katet_1 * katet_2) / 2
print(f'Гипотенуза прямоугольного треугольника с катетами {katet_1} и {katet_2} равна {gipotenyza}')
print(f'Площадь прямоугольного треугольника с катетами {katet_1} и {katet_2} равна {area}')
