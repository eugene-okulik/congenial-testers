def fibonacci_num(length):
    a = 0
    b = 1
    count = 0
    while count < length:
        yield a
        a = b
        b = a + b
        count += 1


desired_length = 100000

# Генерация последовательности чисел Фибоначчи указанной длины
fib_sequence = fibonacci_num(desired_length)
for index, number in enumerate(fib_sequence):
    if index + 1 in [5, 200, 1000]:
        print(f"Число с индексом {index + 1}: {number}")
