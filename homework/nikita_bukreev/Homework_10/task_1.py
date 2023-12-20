
def custom_decorator(funk):
    def wrapper(first, second):   # operation вообще не подсвечивается (тип не используется)
        if (first < 0) or (second < 0):
            result = funk(first, second, '*')
            return result
        elif first == second:
            result = funk(first, second, '+')
            return result
        elif first > second:
            result = funk(second, first, '-')
            return result
        elif second > first:
            result = funk(first, second, '/')
            return result

    return wrapper


@custom_decorator
def calc(first, second, operation):
    match operation:
        case '+':
            return first + second
        case '-':
            return first - second
        case '/':
            return first / second
        case '*':
            return first * second
        case _:
            print('Символ не является математическим символом')


print(calc(10, 10))
print(calc(12, 11))
print(calc(12, 13))
print(calc(-12, 11))
