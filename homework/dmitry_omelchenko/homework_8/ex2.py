def fibonacci_generator(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


fibonacci_list = fibonacci_generator(100000)

# Вывод пятого, двухсотого, тысячного и стотысячного чисел из списка Фибоначчи
print(f"Пятое число Фибоначчи: {fibonacci_list[4]}")
print(f"Двухсотое число Фибоначчи: {fibonacci_list[199]}")
print(f"Тысячное число Фибоначчи: {fibonacci_list[999]}")
print(f"Сто тысячное число Фибоначчи: {fibonacci_list[99999]}")
