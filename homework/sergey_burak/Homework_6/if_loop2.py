# Задание №2 - "FuzzBuzz"
# Напишите программу, которая перебирает последовательность от 1 до 100.
# Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz".
# Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.
# Вывод должен быть следующим:
# 1
# 2
# fuzz
# 4
# buzz
# fuzz
# 7
# 8
# ..
# 14
# FuzzBuzz
# 16
# ...
# Подсказка: При тестировании своей программы обращайте внимание на числа 3, 5 и 15
# (точнее на то, что должно быть напечатано вместо них)
# Последовательность от 1 до 100 можно создасть с помощью range(1, 101)

for sub in range(1, 101):
    if sub % 5 == 0 and sub % 3 == 0:
        print("FuzzBuzz")
    elif sub % 3 == 0:
        print("Fuzz")
    elif sub % 5 == 0:
        print("Buzz")
    else: print(sub)
