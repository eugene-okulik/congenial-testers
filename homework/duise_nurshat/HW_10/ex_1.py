
def decorator(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first < 0 or second < 0:
            return func(first, second, '*')
        elif first < second:
            return func(first, second, '/')
        elif first > second:
            return func(first, second, '-')
    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first1 = int(input("Введите первое число: "))
second2 = int(input("Введите второе число: "))

print((calc(first1, second2)))
