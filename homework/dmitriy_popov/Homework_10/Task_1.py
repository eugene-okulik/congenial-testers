def decoration(func):
    def wrapper(num1, num2, operator):
        if num1 < 0 or num2 < 0:
            operator = '*'
        elif num1 == num2:
            operator = '+'
        elif num1 > num2:
            operator = '-'
        elif num1 < num2:
            operator = '/'

        return func(num1, num2, operator)

    return wrapper


@decoration
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))


print(calc(first_number, second_number, ''))
