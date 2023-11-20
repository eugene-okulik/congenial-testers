# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
#
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
#     если числа равны, то функция calc вызывается с операцией сложения этих чисел
#     если первое больше второго, то происходит вычитание второго из певрого
#     если второе больше первого - деление первого на второе
#     если одно из чисел отрицательное - умножение

def func_operation(*args):
    if first < 0 or second < 0:
        return first * second
    if first == second:
        return first + second
    if first > second:
        return first - second
    if first < second:
        return first / second


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
operation = func_operation()


@func_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc)
