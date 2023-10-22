# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел

from math import sqrt


digit_1 = float(input())
digit_2 = float(input())
average_math = (digit_1 + digit_2) / 2
average_geo = sqrt(digit_1 * digit_2)
print(f'Среднее арифметичское значение чисел {digit_1} и {digit_2} равно {average_math}')
print(f'Среднее геометрическое значение чисел {digit_1} и {digit_2} равно {average_geo}')
